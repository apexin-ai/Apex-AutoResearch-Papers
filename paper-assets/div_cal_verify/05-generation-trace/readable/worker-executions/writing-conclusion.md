# writing conclusion

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_writing_conclusion_20260513T223523.log`
- **Structured JSON:** [`0005b5acc2f0e4d86683.json`](../../sessions/00/0005b5acc2f0e4d86683.json)

## Before a recorded user message

7 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
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
  "uuid": "6603a082-3201-46de-9cbc-cc6d342b97a6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-div-cal-verify/memory/"
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
    "resetsAt": 1778725800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d8dd4984-b217-4902-8a05-150a10a0c325",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me first check if there are existing paper files to understand the context, labels, and style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "e7298b5d-5526-4f9c-b24e-b5fa582e1290",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDgWiR3dedcVHrEEPxhGzn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11602
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

Let me check the existing paper files for style and label references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "3b33f7d1-1055-4fb6-bec2-5c959b7afea5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDgWiR3dedcVHrEEPxhGzn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11602
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01UAy2wNNGkDsScD5VnZfAH4`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Check paper files for labels",
  "prompt": "Find and read the discussion.tex file and any other .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/ to understand:\n1. What labels exist in discussion.tex (especially for Limitations and Future Work subsections)\n2. The writing style and formatting conventions used\n3. Any macros or custom commands defined\n\nRead discussion.tex fully, and check for main.tex or any preamble file for macro definitions. Report the exact label names for limitations and future work sections, and any relevant style conventions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "69e0a37b-6e2b-4348-ac22-08081310f558",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDgWiR3dedcVHrEEPxhGzn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11602
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "description": "Check paper files for labels",
  "task_type": "local_agent",
  "prompt": "Find and read the discussion.tex file and any other .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/ to understand:\n1. What labels exist in discussion.tex (especially for Limitations and Future Work subsections)\n2. The writing style and formatting conventions used\n3. Any macros or custom commands defined\n\nRead discussion.tex fully, and check for main.tex or any preamble file for macro definitions. Report the exact label names for limitations and future work sections, and any relevant style conventions.",
  "uuid": "08bf36cb-cc2f-4324-a2e5-809725041493",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

## Round 1

27 recorded events

### User

_source line 8 · 2026-05-13T22:35:37.719Z_

Find and read the discussion.tex file and any other .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/ to understand:
1. What labels exist in discussion.tex (especially for Limitations and Future Work subsections)
2. The writing style and formatting conventions used
3. Any macros or custom commands defined

Read discussion.tex fully, and check for main.tex or any preamble file for macro definitions. Report the exact label names for limitations and future work sections, and any relevant style conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "f2540ef7-4d95-4449-a7e5-486ff2a983e0"
}
```

</details>

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 15537,
    "tool_uses": 1,
    "duration_ms": 1501
  },
  "last_tool_name": "Bash",
  "uuid": "70b84a6e-74cf-44fd-b71c-d898f6bf8e15",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_01LS3cmtDfE2wtKXfQSY8FQx`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/ -type f -name \"*.tex\" 2>/dev/null | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "3be552bd-0f40-43a7-bd1f-76bf042db082",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Doox1JBQZ1U78mF3jJtuVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15520,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15520,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 11 · 2026-05-13T22:35:39.544Z_

<details><summary>↩ Tool result · `toolu_01LS3cmtDfE2wtKXfQSY8FQx`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "8699fd3b-2a29-4e9f-878e-af23c3d6b9ff"
}
```

</details>

---

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 16770,
    "tool_uses": 2,
    "duration_ms": 3453
  },
  "last_tool_name": "Read",
  "uuid": "9581bfd5-2efd-4f8c-bc87-abeae74d91d9",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_017erXvFDrwWkqarCnBiQspR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "067650db-9b69-4f37-b98a-851515e7ae59",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017Z9Hb753qJCkLYUiz4acco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1229,
      "cache_read_input_tokens": 15520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1229,
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

_source line 14 · 2026-05-13T22:35:41.189Z_

<details><summary>↩ Tool result · `toolu_017erXvFDrwWkqarCnBiQspR`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{The Embedding Alignment Gap as Goodhart's Law}
5	
6	The selection ratio trajectory of RGDS---declining from ${\sim}1.04$ at Generation~0 to $0.52 \pm 0.004$ at Generation~7---instantiates a specific form of Goodhart's law in representation space \citep{gao2023scaling, karwowski2024goodhart}. The proxy measure (embedding diversity) and the true objective (content diversity) are initially correlated: at Generation~0, RGDS's selection ratio exceeds~1, and the method preferentially retains content-rich samples. But as the model trains on its own selected outputs, the embedding space drifts: regions that formerly encoded distinct content merge, effective dimensionality shrinks, and the proxy's correlation with the target degrades.
7	
8	The selection ratio crossing~1.0 marks the critical transition. Above~1.0, the proxy---while imperfect---points in the right direction. Below~1.0, the proxy has fully inverted: the model's internal notion of ``diverse'' anti-correlates with content diversity, and selection actively filters out the samples that would slow collapse. This inversion is irreversible within the self-training loop because the next generation's embeddings are shaped by the content-depleted training data, further degrading the proxy.
9	
10	\citet{karwowski2024goodhart} formalize Goodhart's law in the context of reward model overoptimization, showing that proxy performance peaks and then degrades as optimization pressure increases. The embedding alignment gap follows an analogous trajectory: RGDS's selection ratio rises slightly during Generations~1--3 before sustained decline, mirroring the peak-then-degrade pattern characteristic of Goodhart dynamics. The structural difference is that here the proxy (embedding space) is itself a function of the optimization outcome, creating a feedback loop absent from standard Goodhart settings where the proxy is fixed.
11	
12	\subsection{The Normal Cluster and the Floor of Self-Training}
13	
14	Three of our four methods---Random~50\%, External-only, and Uncurated---cluster in a band of Generation~7 perplexities between 43 and 51 despite substantial differences in design (ANOVA $p = 0.219$, $n{=}3$ per method). Random selection applies no intelligent curation; External-only applies greedy diversity maximization with frozen embeddings; Uncurated retains all data without filtering. That these methods converge to comparable PPL outcomes indicates that the floor of perplexity degradation in this self-training protocol is determined by the iterative feedback loop itself \citep{shumailov2024ai}, not by the data selection strategy.
15	
16	Critically, this convergence is specific to perplexity. When measured by rare n-gram ratio, the same three methods show statistically significant differences (ANOVA $p = 0.007$): Uncurated retains fewer rare n-grams ($0.0090 \pm 0.0004$) than both Random~50\% ($0.0098 \pm 0.0003$) and External-only ($0.0102 \pm 0.0004$). Content diversity can degrade silently---without perplexity penalty---indicating that PPL alone is insufficient to capture all dimensions of model collapse.
17	
18	This convergence is consistent with theoretical analyses showing that self-consuming generative processes converge toward the modes of the original distribution regardless of training procedure \citep{seddik2024how}. Within the non-catastrophic regime, data selection method variation produces second-order effects relative to the first-order dynamics of iterative self-training. RGDS is the outlier precisely because it introduces a systematic bias---toward content-depleted samples---that compounds across generations, pushing it outside the natural convergence band.
19	
20	\subsection{Practical Implications}
21	
22	The results yield a direct prescription: do not use the training model's own embeddings for data selection in iterative self-training settings. Any embedding-based curation method whose embedding source co-evolves with the model---including methods based on facility location objectives, kernel density estimation, or clustering over internal representations---is vulnerable to the same proxy-target inversion. The risk is highest when curation occurs at every generation and no external anchor stabilizes the embedding space.
23	
24	Random sampling provides a zero-cost alternative that avoids the alignment gap entirely and, in our experiments, slightly outperforms both Uncurated and External-only baselines (though the difference is not statistically significant at $n{=}3$; \S\ref{sec:result_s3}). When informed selection is desired, frozen external embeddings maintain selection quality across generations at the cost of an additional inference pass through the external encoder.
25	
26	\subsection{Connection to Concept Drift}
27	
28	The embedding alignment gap can be understood as a special case of concept drift \citep{lu2019learning, gama2014survey} in which the drift is endogenous: the model's own outputs define its future training distribution, which in turn reshapes its representations. In standard concept drift settings, the data distribution shifts due to external factors, and the model must adapt. In self-consuming training, the model \emph{causes} the distribution shift, creating a feedback loop where representation degradation and distributional shift co-amplify.
29	
30	This endogenous drift is particularly insidious for embedding-based data selection because the selection mechanism relies on the very representations undergoing drift. Concept drift detection methods that monitor distributional divergence between training batches would flag the symptom (changing distributions) but not the cause (embedding-selection feedback). Addressing this failure mode requires either anchoring selection to a stable external reference---as External-only does---or monitoring the selection ratio to detect proxy inversion before it compounds.
31	
32	\subsection{Limitations}
33	
34	Several limitations scope our conclusions:
35	\begin{enumerate}
36	    \item Our experiments use GPT2-125M and GPT2-Medium (355M, preliminary $n{=}1$); the embedding alignment gap may manifest differently in larger models with richer representational capacity.
37	    \item We train and evaluate exclusively on WikiText-103; other domains (code, dialogue, scientific text) may exhibit different collapse dynamics.
38	    \item Our self-training protocol uses cumulative fine-tuning with fixed hyperparameters; instruction-tuning and RLHF pipelines introduce additional variables (reward signals, preference data) that could interact with the alignment gap.
39	    \item Our analysis of dimensional collapse is empirical and analogical \citep{jing2022understanding}---we do not provide a formal theoretical proof linking effective dimensionality reduction to selection ratio decline.
40	    \item GPT2-Medium results are based on a single seed at time of writing; multi-seed confirmation is pending.
41	\end{enumerate}
42	
43	\subsection{Future Work}
44	
45	Three directions extend this work. First, scaling to 1B+ parameter models would test whether richer embedding spaces resist or amplify the alignment gap. Second, replicating across diverse pretraining corpora (OpenWebText, C4, The Pile) would establish domain generality. Third, \emph{embedding re-anchoring} strategies---periodically resetting the selection embeddings to an external encoder or a cached earlier checkpoint---could retain the benefits of informed selection while preventing proxy inversion. Finally, a theoretical analysis relating the selection ratio trajectory to the rate of effective dimensionality reduction would provide a predictive framework for identifying when the alignment gap becomes critical before the proxy has fully inverted.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "b018b7a7-8d98-4db3-bf38-4b51fbf783a4"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 16771,
    "tool_uses": 3,
    "duration_ms": 3553
  },
  "last_tool_name": "Read",
  "uuid": "f8e8af87-bb5e-4aa8-af6a-b922f1602bd7",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01DBkgNp2fw4X7n3nmotsDdr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "9a974b44-b2e4-4819-880e-b3675e78a337",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017Z9Hb753qJCkLYUiz4acco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1229,
      "cache_read_input_tokens": 15520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1229,
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

_source line 17 · 2026-05-13T22:35:41.279Z_

<details><summary>↩ Tool result · `toolu_01DBkgNp2fw4X7n3nmotsDdr`</summary>

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
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	
17	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
18	
19	\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\Accelerates Model Collapse in Iterative Self-Training}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Iterative self-training on model-generated data risks \emph{model collapse}---a progressive degradation of output quality across generations. A natural mitigation is diversity-based data curation: selecting training subsets that maximize coverage in the model's own embedding space. We show that this intuitive strategy backfires. In controlled iterative self-training experiments with GPT-2 (125M and 355M parameters) on WikiText-103, Representation-Guided Diversity Selection (RGDS)---which uses the training model's embeddings to greedily maximize diversity---\emph{accelerates} collapse rather than preventing it, producing roughly 80\% higher perplexity than a random selection baseline operating under the same 50\% data budget. We identify the mechanism behind this failure as the \emph{Embedding Alignment Gap}: the model's internal notion of ``diversity'' progressively diverges from actual content diversity as its representations co-degrade with the generated data, causing the selection ratio to decline from approximately 1.0 to 0.5 over eight generations. Critically, all selection strategies that bypass the model's own embeddings---random sampling (PPL 43.18$\pm$1.43), external frozen embeddings (PPL 46.36$\pm$2.97), and uncurated full-corpus training (PPL 47.04$\pm$2.90)---cluster within a narrow perplexity range with no catastrophic failure. Meanwhile, standard representation quality diagnostics such as RankMe effective dimensionality and $k$-NN accuracy remain stable throughout training, rendering the alignment gap invisible to conventional monitoring. Our results demonstrate that coupling data selection to co-degrading internal representations creates a feedback loop that amplifies rather than mitigates collapse, and that zero-cost random sampling is a more robust alternative for iterative self-training pipelines.
28	\end{abstract}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{methodology}
35	
36	\input{experiments}
37	
38	\input{results}
39	
40	\input{discussion}
41	
42	\input{conclusion}
43	
44	\bibliography{references}
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
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "46b53de7-e33a-4cce-8675-246efcf22812"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 19607,
    "tool_uses": 4,
    "duration_ms": 6656
  },
  "last_tool_name": "Bash",
  "uuid": "ac0d56b8-8375-4fdd-844e-7e071ad1aa94",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01KPzEtrWbL4LdBSLpQdbE9S`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/ | grep -E \"\\.tex$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "ed1ffe52-7aa3-479c-8a03-0dbb323d370f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DnNEv6hADSanupLi24XLvH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2833,
      "cache_read_input_tokens": 16749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2833,
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

_source line 20 · 2026-05-13T22:35:44.448Z_

<details><summary>↩ Tool result · `toolu_01KPzEtrWbL4LdBSLpQdbE9S`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  7680 May 13 22:00 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  6190 May 13 21:57 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  7672 May 13 21:57 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  2602 May 13 22:35 main.tex
-rw-r--r-- 1 ubuntu ubuntu  8272 May 13 20:32 methodology.tex
-rw-r--r-- 1 ubuntu ubuntu  7518 May 13 21:37 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  8056 May 13 22:00 results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "ae930d63-01e5-455f-9fb5-4efce813d5c6"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 19950,
    "tool_uses": 5,
    "duration_ms": 8082
  },
  "last_tool_name": "Bash",
  "uuid": "d6332c4a-3309-4f96-8740-438f00c3b8bf",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01WUePEvXftMzLSZwZ5fNpce`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/conclusion.tex 2>&1 || echo \"File not found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "d6aeb809-a802-4492-af65-9b30346c1d3e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Wf82oTSymuFXrbVbpLAQgZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 342,
      "cache_read_input_tokens": 19582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 342,
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

_source line 23 · 2026-05-13T22:35:45.860Z_

<details><summary>↩ Tool result · `toolu_01WUePEvXftMzLSZwZ5fNpce`</summary>

```text
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/conclusion.tex': No such file or directory
File not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "4a47b82e-d298-42f9-a5d3-783e801dcbed"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9ea3f382ccbbef33",
  "tool_use_id": "toolu_01UAy2wNNGkDsScD5VnZfAH4",
  "status": "completed",
  "output_file": "",
  "summary": "Check paper files for labels",
  "usage": {
    "total_tokens": 20132,
    "tool_uses": 5,
    "duration_ms": 16084
  },
  "uuid": "9719cfbe-1e89-484c-90e0-9892ffb196b6",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8"
}
```

---

### Tool result

_source line 25 · 2026-05-13T22:35:53.805Z_

<details><summary>↩ Tool result · `toolu_01UAy2wNNGkDsScD5VnZfAH4`</summary>

````text
Perfect! I now have all the information needed. Let me compile my findings:

## Analysis of discussion.tex and Paper Structure

### Label Names for Limitations and Future Work

From **discussion.tex**:

1. **Limitations subsection label**: `\label{sec:discussion}` (for the entire Discussion section)
   - The Limitations subsection itself (line 32-41) does NOT have its own `\label` command
   - It is a `\subsection{Limitations}` without a dedicated label

2. **Future Work subsection label**: Similar to Limitations, there is NO dedicated `\label` for the Future Work subsection
   - It is a `\subsection{Future Work}` (line 43) without its own label
   - However, line 24 contains a reference: `\S\ref{sec:result_s3}` which suggests other sections use `sec:` prefix for labels

### Section Label Conventions

The paper follows this labeling pattern:
- Main sections use: `\label{sec:sectionname}` (e.g., `\label{sec:discussion}`)
- Cross-references use: `\ref{sec:name}` format
- Result subsections appear to use: `sec:result_s3` (supplementary results)

### Writing Style and Formatting Conventions

1. **Mathematical notation**: Uses inline math mode with `$...$` for variables and symbols
2. **Citations**: Uses `\citep{...}` for parenthetical citations (ACL style)
3. **Emphasis**: Uses `\emph{...}` for emphasized text
4. **Numerical precision**: Reports uncertainties with ±notation (e.g., `0.52 \pm 0.004`)
5. **Statistical references**: Uses standard notation like "ANOVA $p = 0.219$", "n{=}3"
6. **Enumeration**: Uses `\begin{enumerate}...\end{enumerate}` for numbered lists (see Limitations section)

### Macros and Custom Commands

From **main.tex** (preamble):

One custom command is defined:
```latex
\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
```

This command creates red-colored placeholders for unfinished text, though it doesn't appear to be used in discussion.tex.

### Document Class and Packages

- Document class: `\documentclass[11pt]{article}` with `acl` package (review mode)
- Key packages: times, latexsym, fontenc, inputenc, microtype, inconsolata, graphicx, booktabs, amsmath, amssymb, xcolor

### Key Observation

The Limitations (line 32) and Future Work (line 43) subsections in discussion.tex **do not have their own `\label` commands**. If you need to reference these sections, you would need to add labels like:
- `\label{sec:limitations}` after `\subsection{Limitations}`
- `\label{sec:future_work}` after `\subsection{Future Work}`

The file uses the convention of labeling main sections with `sec:` prefix, so these would follow that pattern consistently.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "ed5ae5ba-0917-4af7-87e5-d86a2642ee0b",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find and read the discussion.tex file and any other .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/ to understand:\n1. What labels exist in discussion.tex (especially for Limitations and Future Work subsections)\n2. The writing style and formatting conventions used\n3. Any macros or custom commands defined\n\nRead discussion.tex fully, and check for main.tex or any preamble file for macro definitions. Report the exact label names for limitations and future work sections, and any relevant style conventions.",
    "agentId": "a9ea3f382ccbbef33",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have all the information needed. Let me compile my findings:\n\n## Analysis of discussion.tex and Paper Structure\n\n### Label Names for Limitations and Future Work\n\nFrom **discussion.tex**:\n\n1. **Limitations subsection label**: `\\label{sec:discussion}` (for the entire Discussion section)\n   - The Limitations subsection itself (line 32-41) does NOT have its own `\\label` command\n   - It is a `\\subsection{Limitations}` without a dedicated label\n\n2. **Future Work subsection label**: Similar to Limitations, there is NO dedicated `\\label` for the Future Work subsection\n   - It is a `\\subsection{Future Work}` (line 43) without its own label\n   - However, line 24 contains a reference: `\\S\\ref{sec:result_s3}` which suggests other sections use `sec:` prefix for labels\n\n### Section Label Conventions\n\nThe paper follows this labeling pattern:\n- Main sections use: `\\label{sec:sectionname}` (e.g., `\\label{sec:discussion}`)\n- Cross-references use: `\\ref{sec:name}` format\n- Result subsections appear to use: `sec:result_s3` (supplementary results)\n\n### Writing Style and Formatting Conventions\n\n1. **Mathematical notation**: Uses inline math mode with `$...$` for variables and symbols\n2. **Citations**: Uses `\\citep{...}` for parenthetical citations (ACL style)\n3. **Emphasis**: Uses `\\emph{...}` for emphasized text\n4. **Numerical precision**: Reports uncertainties with ±notation (e.g., `0.52 \\pm 0.004`)\n5. **Statistical references**: Uses standard notation like \"ANOVA $p = 0.219$\", \"n{=}3\"\n6. **Enumeration**: Uses `\\begin{enumerate}...\\end{enumerate}` for numbered lists (see Limitations section)\n\n### Macros and Custom Commands\n\nFrom **main.tex** (preamble):\n\nOne custom command is defined:\n```latex\n\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n```\n\nThis command creates red-colored placeholders for unfinished text, though it doesn't appear to be used in discussion.tex.\n\n### Document Class and Packages\n\n- Document class: `\\documentclass[11pt]{article}` with `acl` package (review mode)\n- Key packages: times, latexsym, fontenc, inputenc, microtype, inconsolata, graphicx, booktabs, amsmath, amssymb, xcolor\n\n### Key Observation\n\nThe Limitations (line 32) and Future Work (line 43) subsections in discussion.tex **do not have their own `\\label` commands**. If you need to reference these sections, you would need to add labels like:\n- `\\label{sec:limitations}` after `\\subsection{Limitations}`\n- `\\label{sec:future_work}` after `\\subsection{Future Work}`\n\nThe file uses the convention of labeling main sections with `sec:` prefix, so these would follow that pattern consistently."
      }
    ],
    "totalDurationMs": 16086,
    "totalTokens": 20857,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 19924,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 181
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 747,
          "cache_read_input_tokens": 19924,
          "cache_creation_input_tokens": 181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 181,
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
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01BaD5w3ob7DsvQhNfbi3zcU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "496576bf-d465-4e45-b763-ad6ca38906db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WATH5Me7sDuFQzB1E6wRsb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 23443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
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

_source line 27 · 2026-05-13T22:35:56.399Z_

<details><summary>↩ Tool result · `toolu_01BaD5w3ob7DsvQhNfbi3zcU`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{The Embedding Alignment Gap as Goodhart's Law}
5	
6	The selection ratio trajectory of RGDS---declining from ${\sim}1.04$ at Generation~0 to $0.52 \pm 0.004$ at Generation~7---instantiates a specific form of Goodhart's law in representation space \citep{gao2023scaling, karwowski2024goodhart}. The proxy measure (embedding diversity) and the true objective (content diversity) are initially correlated: at Generation~0, RGDS's selection ratio exceeds~1, and the method preferentially retains content-rich samples. But as the model trains on its own selected outputs, the embedding space drifts: regions that formerly encoded distinct content merge, effective dimensionality shrinks, and the proxy's correlation with the target degrades.
7	
8	The selection ratio crossing~1.0 marks the critical transition. Above~1.0, the proxy---while imperfect---points in the right direction. Below~1.0, the proxy has fully inverted: the model's internal notion of ``diverse'' anti-correlates with content diversity, and selection actively filters out the samples that would slow collapse. This inversion is irreversible within the self-training loop because the next generation's embeddings are shaped by the content-depleted training data, further degrading the proxy.
9	
10	\citet{karwowski2024goodhart} formalize Goodhart's law in the context of reward model overoptimization, showing that proxy performance peaks and then degrades as optimization pressure increases. The embedding alignment gap follows an analogous trajectory: RGDS's selection ratio rises slightly during Generations~1--3 before sustained decline, mirroring the peak-then-degrade pattern characteristic of Goodhart dynamics. The structural difference is that here the proxy (embedding space) is itself a function of the optimization outcome, creating a feedback loop absent from standard Goodhart settings where the proxy is fixed.
11	
12	\subsection{The Normal Cluster and the Floor of Self-Training}
13	
14	Three of our four methods---Random~50\%, External-only, and Uncurated---cluster in a band of Generation~7 perplexities between 43 and 51 despite substantial differences in design (ANOVA $p = 0.219$, $n{=}3$ per method). Random selection applies no intelligent curation; External-only applies greedy diversity maximization with frozen embeddings; Uncurated retains all data without filtering. That these methods converge to comparable PPL outcomes indicates that the floor of perplexity degradation in this self-training protocol is determined by the iterative feedback loop itself \citep{shumailov2024ai}, not by the data selection strategy.
15	
16	Critically, this convergence is specific to perplexity. When measured by rare n-gram ratio, the same three methods show statistically significant differences (ANOVA $p = 0.007$): Uncurated retains fewer rare n-grams ($0.0090 \pm 0.0004$) than both Random~50\% ($0.0098 \pm 0.0003$) and External-only ($0.0102 \pm 0.0004$). Content diversity can degrade silently---without perplexity penalty---indicating that PPL alone is insufficient to capture all dimensions of model collapse.
17	
18	This convergence is consistent with theoretical analyses showing that self-consuming generative processes converge toward the modes of the original distribution regardless of training procedure \citep{seddik2024how}. Within the non-catastrophic regime, data selection method variation produces second-order effects relative to the first-order dynamics of iterative self-training. RGDS is the outlier precisely because it introduces a systematic bias---toward content-depleted samples---that compounds across generations, pushing it outside the natural convergence band.
19	
20	\subsection{Practical Implications}
21	
22	The results yield a direct prescription: do not use the training model's own embeddings for data selection in iterative self-training settings. Any embedding-based curation method whose embedding source co-evolves with the model---including methods based on facility location objectives, kernel density estimation, or clustering over internal representations---is vulnerable to the same proxy-target inversion. The risk is highest when curation occurs at every generation and no external anchor stabilizes the embedding space.
23	
24	Random sampling provides a zero-cost alternative that avoids the alignment gap entirely and, in our experiments, slightly outperforms both Uncurated and External-only baselines (though the difference is not statistically significant at $n{=}3$; \S\ref{sec:result_s3}). When informed selection is desired, frozen external embeddings maintain selection quality across generations at the cost of an additional inference pass through the external encoder.
25	
26	\subsection{Connection to Concept Drift}
27	
28	The embedding alignment gap can be understood as a special case of concept drift \citep{lu2019learning, gama2014survey} in which the drift is endogenous: the model's own outputs define its future training distribution, which in turn reshapes its representations. In standard concept drift settings, the data distribution shifts due to external factors, and the model must adapt. In self-consuming training, the model \emph{causes} the distribution shift, creating a feedback loop where representation degradation and distributional shift co-amplify.
29	
30	This endogenous drift is particularly insidious for embedding-based data selection because the selection mechanism relies on the very representations undergoing drift. Concept drift detection methods that monitor distributional divergence between training batches would flag the symptom (changing distributions) but not the cause (embedding-selection feedback). Addressing this failure mode requires either anchoring selection to a stable external reference---as External-only does---or monitoring the selection ratio to detect proxy inversion before it compounds.
31	
32	\subsection{Limitations}
33	
34	Several limitations scope our conclusions:
35	\begin{enumerate}
36	    \item Our experiments use GPT2-125M and GPT2-Medium (355M, preliminary $n{=}1$); the embedding alignment gap may manifest differently in larger models with richer representational capacity.
37	    \item We train and evaluate exclusively on WikiText-103; other domains (code, dialogue, scientific text) may exhibit different collapse dynamics.
38	    \item Our self-training protocol uses cumulative fine-tuning with fixed hyperparameters; instruction-tuning and RLHF pipelines introduce additional variables (reward signals, preference data) that could interact with the alignment gap.
39	    \item Our analysis of dimensional collapse is empirical and analogical \citep{jing2022understanding}---we do not provide a formal theoretical proof linking effective dimensionality reduction to selection ratio decline.
40	    \item GPT2-Medium results are based on a single seed at time of writing; multi-seed confirmation is pending.
41	\end{enumerate}
42	
43	\subsection{Future Work}
44	
45	Three directions extend this work. First, scaling to 1B+ parameter models would test whether richer embedding spaces resist or amplify the alignment gap. Second, replicating across diverse pretraining corpora (OpenWebText, C4, The Pile) would establish domain generality. Third, \emph{embedding re-anchoring} strategies---periodically resetting the selection embeddings to an external encoder or a cached earlier checkpoint---could retain the benefits of informed selection while preventing proxy inversion. Finally, a theoretical analysis relating the selection ratio trajectory to the rate of effective dimensionality reduction would provide a predictive framework for identifying when the alignment gap becomes critical before the proxy has fully inverted.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "56bf1055-5104-43c9-a84b-2477106165dc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{The Embedding Alignment Gap as Goodhart's Law}\n\nThe selection ratio trajectory of RGDS---declining from ${\\sim}1.04$ at Generation~0 to $0.52 \\pm 0.004$ at Generation~7---instantiates a specific form of Goodhart's law in representation space \\citep{gao2023scaling, karwowski2024goodhart}. The proxy measure (embedding diversity) and the true objective (content diversity) are initially correlated: at Generation~0, RGDS's selection ratio exceeds~1, and the method preferentially retains content-rich samples. But as the model trains on its own selected outputs, the embedding space drifts: regions that formerly encoded distinct content merge, effective dimensionality shrinks, and the proxy's correlation with the target degrades.\n\nThe selection ratio crossing~1.0 marks the critical transition. Above~1.0, the proxy---while imperfect---points in the right direction. Below~1.0, the proxy has fully inverted: the model's internal notion of ``diverse'' anti-correlates with content diversity, and selection actively filters out the samples that would slow collapse. This inversion is irreversible within the self-training loop because the next generation's embeddings are shaped by the content-depleted training data, further degrading the proxy.\n\n\\citet{karwowski2024goodhart} formalize Goodhart's law in the context of reward model overoptimization, showing that proxy performance peaks and then degrades as optimization pressure increases. The embedding alignment gap follows an analogous trajectory: RGDS's selection ratio rises slightly during Generations~1--3 before sustained decline, mirroring the peak-then-degrade pattern characteristic of Goodhart dynamics. The structural difference is that here the proxy (embedding space) is itself a function of the optimization outcome, creating a feedback loop absent from standard Goodhart settings where the proxy is fixed.\n\n\\subsection{The Normal Cluster and the Floor of Self-Training}\n\nThree of our four methods---Random~50\\%, External-only, and Uncurated---cluster in a band of Generation~7 perplexities between 43 and 51 despite substantial differences in design (ANOVA $p = 0.219$, $n{=}3$ per method). Random selection applies no intelligent curation; External-only applies greedy diversity maximization with frozen embeddings; Uncurated retains all data without filtering. That these methods converge to comparable PPL outcomes indicates that the floor of perplexity degradation in this self-training protocol is determined by the iterative feedback loop itself \\citep{shumailov2024ai}, not by the data selection strategy.\n\nCritically, this convergence is specific to perplexity. When measured by rare n-gram ratio, the same three methods show statistically significant differences (ANOVA $p = 0.007$): Uncurated retains fewer rare n-grams ($0.0090 \\pm 0.0004$) than both Random~50\\% ($0.0098 \\pm 0.0003$) and External-only ($0.0102 \\pm 0.0004$). Content diversity can degrade silently---without perplexity penalty---indicating that PPL alone is insufficient to capture all dimensions of model collapse.\n\nThis convergence is consistent with theoretical analyses showing that self-consuming generative processes converge toward the modes of the original distribution regardless of training procedure \\citep{seddik2024how}. Within the non-catastrophic regime, data selection method variation produces second-order effects relative to the first-order dynamics of iterative self-training. RGDS is the outlier precisely because it introduces a systematic bias---toward content-depleted samples---that compounds across generations, pushing it outside the natural convergence band.\n\n\\subsection{Practical Implications}\n\nThe results yield a direct prescription: do not use the training model's own embeddings for data selection in iterative self-training settings. Any embedding-based curation method whose embedding source co-evolves with the model---including methods based on facility location objectives, kernel density estimation, or clustering over internal representations---is vulnerable to the same proxy-target inversion. The risk is highest when curation occurs at every generation and no external anchor stabilizes the embedding space.\n\nRandom sampling provides a zero-cost alternative that avoids the alignment gap entirely and, in our experiments, slightly outperforms both Uncurated and External-only baselines (though the difference is not statistically significant at $n{=}3$; \\S\\ref{sec:result_s3}). When informed selection is desired, frozen external embeddings maintain selection quality across generations at the cost of an additional inference pass through the external encoder.\n\n\\subsection{Connection to Concept Drift}\n\nThe embedding alignment gap can be understood as a special case of concept drift \\citep{lu2019learning, gama2014survey} in which the drift is endogenous: the model's own outputs define its future training distribution, which in turn reshapes its representations. In standard concept drift settings, the data distribution shifts due to external factors, and the model must adapt. In self-consuming training, the model \\emph{causes} the distribution shift, creating a feedback loop where representation degradation and distributional shift co-amplify.\n\nThis endogenous drift is particularly insidious for embedding-based data selection because the selection mechanism relies on the very representations undergoing drift. Concept drift detection methods that monitor distributional divergence between training batches would flag the symptom (changing distributions) but not the cause (embedding-selection feedback). Addressing this failure mode requires either anchoring selection to a stable external reference---as External-only does---or monitoring the selection ratio to detect proxy inversion before it compounds.\n\n\\subsection{Limitations}\n\nSeveral limitations scope our conclusions:\n\\begin{enumerate}\n    \\item Our experiments use GPT2-125M and GPT2-Medium (355M, preliminary $n{=}1$); the embedding alignment gap may manifest differently in larger models with richer representational capacity.\n    \\item We train and evaluate exclusively on WikiText-103; other domains (code, dialogue, scientific text) may exhibit different collapse dynamics.\n    \\item Our self-training protocol uses cumulative fine-tuning with fixed hyperparameters; instruction-tuning and RLHF pipelines introduce additional variables (reward signals, preference data) that could interact with the alignment gap.\n    \\item Our analysis of dimensional collapse is empirical and analogical \\citep{jing2022understanding}---we do not provide a formal theoretical proof linking effective dimensionality reduction to selection ratio decline.\n    \\item GPT2-Medium results are based on a single seed at time of writing; multi-seed confirmation is pending.\n\\end{enumerate}\n\n\\subsection{Future Work}\n\nThree directions extend this work. First, scaling to 1B+ parameter models would test whether richer embedding spaces resist or amplify the alignment gap. Second, replicating across diverse pretraining corpora (OpenWebText, C4, The Pile) would establish domain generality. Third, \\emph{embedding re-anchoring} strategies---periodically resetting the selection embeddings to an external encoder or a cached earlier checkpoint---could retain the benefits of informed selection while preventing proxy inversion. Finally, a theoretical analysis relating the selection ratio trajectory to the rate of effective dimensionality reduction would provide a predictive framework for identifying when the alignment gap becomes critical before the proxy has fully inverted.\n",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_014vWUsnDAULPNkiY3D4Urzx`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/",
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
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "7c87e8f5-fcc9-4320-88d9-28c251d5a9a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015af7chEMuoAhucxb8wyv5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 24472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1902
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

_source line 29 · 2026-05-13T22:36:00.526Z_

<details><summary>↩ Tool result · `toolu_014vWUsnDAULPNkiY3D4Urzx`</summary>

```text
acl.sty
acl_natbib.bst
discussion.tex
experiments.tex
introduction.tex
main.tex
methodology.tex
references.bib
related_work.tex
results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "4b5d43ac-eb2c-44ad-8fbd-9957b4a7b18c",
  "tool_use_result": {
    "stdout": "acl.sty\nacl_natbib.bst\ndiscussion.tex\nexperiments.tex\nintroduction.tex\nmain.tex\nmethodology.tex\nreferences.bib\nrelated_work.tex\nresults.tex",
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

_source line 30_

No dedicated labels on Limitations/Future Work subsections. I'll reference them via `\S\ref{sec:discussion}`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "85a6b51f-60ea-49be-86bb-17c22a5011d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WgwY4G2YLgA2ZkfBUihNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 26374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 165
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

_source line 31_

<details open><summary>🔧 Tool call — Write · `toolu_01Ek3zPw8FByQd7z39GLam6a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nThis work introduces the \\emph{embedding alignment gap}---the progressive decorrelation between a model's internal embedding similarity and actual content diversity during iterative self-training---and demonstrates its consequences for embedding-based data curation. Through controlled self-training experiments with GPT2-125M over eight generations, we establish three principal findings.\n\nFirst, the embedding alignment gap is real and self-reinforcing. The internal embedding diversity selection ratio declines from ${\\sim}1.04$ at Generation~0 to ${\\sim}0.52$ by Generation~7, indicating that the model's own embeddings increasingly select \\emph{against} content-rich samples. Once the selection ratio crosses below~1.0, the proxy has inverted: diversity-maximizing selection over internal embeddings actively accelerates the loss of content diversity.\n\nSecond, this proxy inversion has catastrophic practical consequences. Representation-guided diversity selection (RGDS) using internal embeddings produces Generation~7 perplexity approximately 80\\% higher than random baseline at the same 50\\% data budget. Meanwhile, Random~50\\% ($43.18 \\pm 1.43$), External-only ($46.36 \\pm 2.97$), and Uncurated ($47.04 \\pm 2.90$) converge to a statistically indistinguishable cluster ($n{=}3$), confirming that the catastrophic degradation of RGDS is not an artifact of data reduction but a direct consequence of co-degrading embeddings.\n\nThird, standard representation quality diagnostics fail to detect the alignment gap. Both RankMe effective dimensionality and $k$-NN probing accuracy remain stable throughout the collapse trajectory, rendering the proxy inversion invisible to conventional monitoring tools.\n\nThese findings carry several caveats. Our experiments are limited to GPT2-scale models, a single pretraining corpus, and a fixed self-training protocol; the generality of these results to larger models, diverse domains, and alternative training paradigms remains to be established (see the limitations and future directions discussed in \\S\\ref{sec:discussion}).\n\nThe practical implication is direct: internal embeddings that co-evolve with the training model should not serve as the selection criterion in iterative self-training pipelines. Random sampling---requiring no additional computation---provides a robust alternative that avoids proxy inversion entirely. When informed selection is desired, frozen external embeddings maintain alignment across generations. For practitioners who cannot abandon internal embeddings, the selection ratio offers a lightweight, real-time diagnostic: an overall declining trend below~1.0 signals that selection has begun to work against its intended objective, and corrective action---such as re-anchoring to an external encoder---should be taken before the degradation compounds.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "11386235-d625-447c-a736-0c8aedfc7f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WgwY4G2YLgA2ZkfBUihNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 26374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 165
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

_source line 32 · 2026-05-13T22:36:21.526Z_

<details><summary>↩ Tool result · `toolu_01Ek3zPw8FByQd7z39GLam6a`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "3eadba08-a5b0-4b7d-bb93-37644cb83bf1",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nThis work introduces the \\emph{embedding alignment gap}---the progressive decorrelation between a model's internal embedding similarity and actual content diversity during iterative self-training---and demonstrates its consequences for embedding-based data curation. Through controlled self-training experiments with GPT2-125M over eight generations, we establish three principal findings.\n\nFirst, the embedding alignment gap is real and self-reinforcing. The internal embedding diversity selection ratio declines from ${\\sim}1.04$ at Generation~0 to ${\\sim}0.52$ by Generation~7, indicating that the model's own embeddings increasingly select \\emph{against} content-rich samples. Once the selection ratio crosses below~1.0, the proxy has inverted: diversity-maximizing selection over internal embeddings actively accelerates the loss of content diversity.\n\nSecond, this proxy inversion has catastrophic practical consequences. Representation-guided diversity selection (RGDS) using internal embeddings produces Generation~7 perplexity approximately 80\\% higher than random baseline at the same 50\\% data budget. Meanwhile, Random~50\\% ($43.18 \\pm 1.43$), External-only ($46.36 \\pm 2.97$), and Uncurated ($47.04 \\pm 2.90$) converge to a statistically indistinguishable cluster ($n{=}3$), confirming that the catastrophic degradation of RGDS is not an artifact of data reduction but a direct consequence of co-degrading embeddings.\n\nThird, standard representation quality diagnostics fail to detect the alignment gap. Both RankMe effective dimensionality and $k$-NN probing accuracy remain stable throughout the collapse trajectory, rendering the proxy inversion invisible to conventional monitoring tools.\n\nThese findings carry several caveats. Our experiments are limited to GPT2-scale models, a single pretraining corpus, and a fixed self-training protocol; the generality of these results to larger models, diverse domains, and alternative training paradigms remains to be established (see the limitations and future directions discussed in \\S\\ref{sec:discussion}).\n\nThe practical implication is direct: internal embeddings that co-evolve with the training model should not serve as the selection criterion in iterative self-training pipelines. Random sampling---requiring no additional computation---provides a robust alternative that avoids proxy inversion entirely. When informed selection is desired, frozen external embeddings maintain alignment across generations. For practitioners who cannot abandon internal embeddings, the selection ratio offers a lightweight, real-time diagnostic: an overall declining trend below~1.0 signals that selection has begun to work against its intended objective, and corrective action---such as re-anchoring to an external encoder---should be taken before the degradation compounds.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 33_

文件已创建。约 370 词，覆盖三个核心发现、limitations/future work 引用（`\S\ref{sec:discussion}`）、以及 selection ratio 作为实时诊断指标的收尾。数字使用近似表述，未 overclaim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "uuid": "b3bf600d-cc97-42de-81b1-e40973b987ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLL5eYYnUBXBWkvRRatKTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 26539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
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

文件已创建。约 370 词，覆盖三个核心发现、limitations/future work 引用（`\S\ref{sec:discussion}`）、以及 selection ratio 作为实时诊断指标的收尾。数字使用近似表述，未 overclaim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 56662,
  "duration_api_ms": 57355,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "cf094c73-ff2e-4298-91e6-922b508f83d8",
  "total_cost_usd": 0.22606900000000002,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 15503,
    "cache_read_input_tokens": 112669,
    "output_tokens": 1297,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15503,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 80,
        "cache_read_input_tokens": 26539,
        "cache_creation_input_tokens": 805,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 805
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1502,
      "outputTokens": 1315,
      "cacheReadInputTokens": 71775,
      "cacheCreationInputTokens": 20105,
      "webSearchRequests": 0,
      "costUSD": 0.040385750000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 1297,
      "cacheReadInputTokens": 112669,
      "cacheCreationInputTokens": 15503,
      "webSearchRequests": 0,
      "costUSD": 0.18568325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e015d093-9c10-466a-8a70-71933330bf70"
}
```

</details>

---
