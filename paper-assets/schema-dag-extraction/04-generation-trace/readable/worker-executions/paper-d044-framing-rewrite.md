# paper d044 framing rewrite

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_paper_d044_framing_rewrite_20260516T093329.log`
- **Structured JSON:** [`d109857ae7f8f2a7a8e4.json`](../../sessions/d1/d109857ae7f8f2a7a8e4.json)

## Before a recorded user message

61 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
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
  "uuid": "326a07de-e832-404a-b5a3-e740db749dfd",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778940000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "07bb690e-73ff-4c00-ae7b-999cdfe1cb9d",
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files to understand the current state of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "b0f53f3c-8c2c-47dc-b722-770b3092ecb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUxujLm7wthmQMkL9Z247W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11866
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

### Assistant

_source line 5_

I'll read the relevant files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "0da8074c-d9e9-4324-8c57-8bba17e474a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUxujLm7wthmQMkL9Z247W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11866
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01UGC2jKbgNcaVW5sJ5eDwzf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "84dcd428-a1d3-4589-99ae-c1dcacce20e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUxujLm7wthmQMkL9Z247W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11866
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

_source line 7 · 2026-05-16T09:33:43.145Z_

<details><summary>↩ Tool result · `toolu_01UGC2jKbgNcaVW5sJ5eDwzf`</summary>

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
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
42	
43	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
44	
45	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
46	
47	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
48	
49	\item \textbf{Causal mechanism.} The study establishes correlational evidence; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.
50	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "21fb9fe3-c415-4678-b01a-2553ce7dab29",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\n\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.\n\\end{enumerate}",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 274
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01T2YNovNybtYN3Z7cWxupTq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "eadf645e-66f7-4759-a796-cddc66821aa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUxujLm7wthmQMkL9Z247W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11866
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

_source line 9 · 2026-05-16T09:33:43.617Z_

<details><summary>↩ Tool result · `toolu_01T2YNovNybtYN3Z7cWxupTq`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "c4a45000-6961-493a-9e22-e8c5ccf58438",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\\text{--}1.7\\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.\n\\end{abstract}",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_012SweB8B3A8RMz4WeWWdzdU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "53bcbe61-e066-410a-8946-dddfb860b88f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUxujLm7wthmQMkL9Z247W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11866
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

_source line 11 · 2026-05-16T09:33:43.897Z_

<details><summary>↩ Tool result · `toolu_012SweB8B3A8RMz4WeWWdzdU`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \emph{count curves} vary schema size while randomizing confusability, and \emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \cite{fewnerd-2021} (66 types, cross-domain), FewRel \cite{fewrel-2018} (80 relations, sentence-level), DocRED \cite{docred-2019} (96 relations, document-level), and MAVEN \cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.
11	
12	Our experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\,pp gain.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.
17	    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).
19	    \item \textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\,pp via confusability-aware grouping (\S\ref{sec:sdgd}).
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "7384ba40-7039-4177-a994-59e839e25b65",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies implicitly assume different answers: \\citet{uniner-2024} extract each type independently; \\citet{llm-pee-2025} partition schemas by type embedding similarity; \\citet{parse-2025} optimize schema definitions. None isolates \\emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \\emph{count curves} vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \\cite{fewnerd-2021} (66 types, cross-domain), FewRel \\cite{fewrel-2018} (80 relations, sentence-level), DocRED \\cite{docred-2019} (96 relations, document-level), and MAVEN \\cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.\n\nOur experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

Now let me search for "robust across prompt designs" and "prompt-invariant" across the paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "916632d6-9d9b-4f41-92ce-750216189a67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Nt2pzP9RWgFbdwnvfeT89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2970,
      "cache_read_input_tokens": 23707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2970
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

_source line 13_

<details open><summary>🔧 Tool call — Grep · `toolu_01Fm8xCGXYyaTEQiRCn9EW1B`</summary>

```json
{
  "pattern": "robust across prompt designs|prompt-invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "652a16a3-e424-42cb-9ed5-a6cf387adf8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Nt2pzP9RWgFbdwnvfeT89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2970,
      "cache_read_input_tokens": 23707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2970
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

_source line 14 · 2026-05-16T09:33:48.368Z_

<details><summary>↩ Tool result · `toolu_01Fm8xCGXYyaTEQiRCn9EW1B`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "e7a7be33-62ac-41f7-8ce5-824b2ad60b3f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01QnKYmfkqgj3bFDFHdv3R7V`</summary>

```json
{
  "pattern": "[Dd]rive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
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
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "36f7635b-d289-4d83-b4fd-c74748111f23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Nt2pzP9RWgFbdwnvfeT89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2970,
      "cache_read_input_tokens": 23707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2970
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

_source line 16 · 2026-05-16T09:33:49.311Z_

<details><summary>↩ Tool result · `toolu_01QnKYmfkqgj3bFDFHdv3R7V`</summary>

```text
12:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "0a76600c-0e9c-43eb-8b21-0a205c7d9ae7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "12:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01VsUEEyWBFgpRFwqKjxDqrx`</summary>

```json
{
  "pattern": "robust.*prompt|prompt.*robust",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "2933a7e0-f5be-4085-b72c-519b1a9b8dd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRKwnL11sjhrabi4o4KGmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 26677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 333
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

_source line 18 · 2026-05-16T09:33:53.698Z_

<details><summary>↩ Tool result · `toolu_01VsUEEyWBFgpRFwqKjxDqrx`</summary>

```text
docs/paper/main.tex:236:We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
docs/paper/main.tex:245:[Omitted long matching line]
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "1dc93170-9e80-42a7-93fd-9ece52886d93",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:236:We assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\ndocs/paper/main.tex:245:[Omitted long matching line]\ndocs/paper/abstract.tex:2:[Omitted long matching line]\ndocs/paper/introduction.tex:12:[Omitted long matching line]",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_01MNZCVifom9yQpSySQa4fzP`</summary>

```json
{
  "pattern": "prompt.*(design|variant|invariant)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "da263746-ce7f-4f0f-bef8-6680dfd8c9dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRKwnL11sjhrabi4o4KGmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 26677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 333
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

_source line 20 · 2026-05-16T09:33:55.152Z_

<details><summary>↩ Tool result · `toolu_01MNZCVifom9yQpSySQa4fzP`</summary>

```text
docs/paper/main.bbl:180:  models' sensitivity to spurious features in prompt design}.
docs/paper/main.tex:236:We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
docs/paper/main.tex:245:[Omitted long matching line]
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/results.tex:67:[Omitted long matching line]
docs/paper/results.tex:134:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "45e63b9d-87e5-4202-9dcf-02b9db6864d0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.bbl:180:  models' sensitivity to spurious features in prompt design}.\ndocs/paper/main.tex:236:We assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\ndocs/paper/main.tex:245:[Omitted long matching line]\ndocs/paper/abstract.tex:2:[Omitted long matching line]\ndocs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/results.tex:67:[Omitted long matching line]\ndocs/paper/results.tex:134:[Omitted long matching line]",
    "numLines": 7
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01LNML9dKz8JKs4o8dPQdFqB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 230,
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
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "4d184d04-f563-43f2-bdb4-b25fb9015d98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zyZED2yrRtrimaMmG9KzD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 27010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 674
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 22 · 2026-05-16T09:33:59.808Z_

<details><summary>↩ Tool result · `toolu_01LNML9dKz8JKs4o8dPQdFqB`</summary>

```text
230	
231	\input{prompt_appendix}
232	
233	\section{Prompt Version Sensitivity Analysis}
234	\label{sec:appendix_prompt_sensitivity}
235	
236	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
237	
238	\paragraph{RE (FewRel).}
239	Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\,pp (low-BCS 82.3\% vs.\ high-BCS 51.0\%; Table~\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
240	
241	\paragraph{NER (Few-NERD).}
242	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
243	
244	\paragraph{Interpretation.}
245	The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.
246	
247	\section{BCS Aggregation Sensitivity}
248	\label{sec:appendix_bcs_sensitivity}
249	
250	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
251	
252	\begin{table}[h]
253	\centering
254	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "0f6856ba-5e78-4d0b-9862-36348d5c870b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small",
      "numLines": 25,
      "startLine": 230,
      "totalLines": 274
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01PcPrBuiGX9EHXP4v5G8Hkf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 60,
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
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "cb41fe27-1da6-41b2-859b-1860869ea474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zyZED2yrRtrimaMmG9KzD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 27010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 674
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 24 · 2026-05-16T09:34:00.707Z_

<details><summary>↩ Tool result · `toolu_01PcPrBuiGX9EHXP4v5G8Hkf`</summary>

```text
60	\end{tabular}}
61	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$).}
62	\label{tab:pairwise}
63	\end{table}
64	
65	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). We omit FewRel: RE's per-instance classification format makes its confusion matrix not directly comparable to span-level confusion rates; the BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide quasi-experimental evidence for RE. Spearman correlations corroborate: $\rho = 0.144\text{--}0.168$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
66	
67	The remaining ${\sim}$98\% of variance likely reflects entity frequency, prompt position effects \cite{lost-in-middle-2024}, mention ambiguity, and type definition quality. We frame pairwise SCS as one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into gaps reaching 31.2\,pp under extreme-batch comparison ($-$25.5\,pp under v2 prompts; typical-batch gap ${\approx}\,2\text{--}4$\,pp, \S\ref{sec:practical_magnitude}).
68	
69	\subsection{BCS-Controlled Experiments}
70	\label{sec:bcs_controlled}
71	
72	We fix the type count and vary BCS to obtain quasi-experimental evidence. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\S\ref{sec:within_pool}) controls for residual confounds from pool composition.
73	
74	\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "4b195466-2508-4516-ba0f-0ba66e21e3ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). We omit FewRel: RE's per-instance classification format makes its confusion matrix not directly comparable to span-level confusion rates; the BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide quasi-experimental evidence for RE. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.168$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining ${\\sim}$98\\% of variance likely reflects entity frequency, prompt position effects \\cite{lost-in-middle-2024}, mention ambiguity, and type definition quality. We frame pairwise SCS as one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into gaps reaching 31.2\\,pp under extreme-batch comparison ($-$25.5\\,pp under v2 prompts; typical-batch gap ${\\approx}\\,2\\text{--}4$\\,pp, \\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix the type count and vary BCS to obtain quasi-experimental evidence. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for residual confounds from pool composition.\n\n\\begin{table}[t]",
      "numLines": 15,
      "startLine": 60,
      "totalLines": 146
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01XCFScWoMhXjLBJpSZz4Fxv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 128,
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
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "0f1674cb-7e29-4472-99cc-20df8f6c8df9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zyZED2yrRtrimaMmG9KzD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 27010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 674
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 26 · 2026-05-16T09:34:01.189Z_

<details><summary>↩ Tool result · `toolu_01XCFScWoMhXjLBJpSZz4Fxv`</summary>

```text
128	For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0])---roughly 7\% of the 31.2\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The 31.2\,pp figure reflects maximum BCS contrast, not the typical batch experience.
129	
130	\paragraph{Cross-model validation.}
131	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}).
132	
133	\paragraph{Prompt sensitivity.}
134	Under the v2 prompt (stricter format constraints), the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $n{=}25$; $r = -0.919$; $p < 0.0001$). Compared to v1's $-$31.2\,pp, the effect attenuates modestly ($-$5.7\,pp) but remains highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\ $r = +0.50$ under v1). Prompt design modulates the magnitude but does not eliminate the confusability effect (full analysis in Appendix~\ref{sec:appendix_prompt_sensitivity}).
135	
136	\subsection{Multi-Channel Degradation}
137	\label{sec:multi_channel}
138	
139	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy} in Appendix~\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 10^{-6}$) for RE. In RE, 100\% of confusion errors are intra-batch and missed-entity rates remain flat (10--16\%); in NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
140	
141	These results establish two channels: \textbf{Channel~1} (count $\to$ recall decline) and \textbf{Channel~2} (confusability $\to$ type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "ddf83809-d46d-4fa7-8674-29f24a743928",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience.\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt (stricter format constraints), the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $n{=}25$; $r = -0.919$; $p < 0.0001$). Compared to v1's $-$31.2\\,pp, the effect attenuates modestly ($-$5.7\\,pp) but remains highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates the magnitude but does not eliminate the confusability effect (full analysis in Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 10^{-6}$) for RE. In RE, 100\\% of confusion errors are intra-batch and missed-entity rates remain flat (10--16\\%); in NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count $\\to$ recall decline) and \\textbf{Channel~2} (confusability $\\to$ type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n",
      "numLines": 15,
      "startLine": 128,
      "totalLines": 146
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_011VTRz4pdrbaKbbpniyFmGW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "4f3595cc-a089-4f44-b7f6-bc4a89482a4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Amp6E5kmGR6fkvAGA6coLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 27684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3108
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 28 · 2026-05-16T09:34:07.546Z_

<details><summary>↩ Tool result · `toolu_011VTRz4pdrbaKbbpniyFmGW`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Future directions.}
8	For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader validation of RE batch composition, are the key next steps.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "f537fd74-78e8-460c-891a-8074b2428708",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Future directions.}\nFor NER, merge amplification blocks naive decomposition (\\S\\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\\Delta = -27$\\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader validation of RE batch composition, are the key next steps.\n",
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

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have a full picture. Let me also check the discussion.tex for any "robust across prompt designs" or similar phrasing that needs updating.

Let me now proceed with all the modifications:

1. Title: "Drive" → "Shape" in main.tex
2. Abstract: Complete rewrite
3. Introduction: 
   a. Finding list lead with typical magnitude
   b. RQ1 "Drive" → "Shape"
   c. Contribution #4 rewrite
4. S12 prompt robustness wording - I found the relevant sections in main.tex line 245 ("robust to prompt design") and results.tex line 134


5. Checking the introduction more carefully - RQ1 at line 8 doesn't actually use "Drive", it asks about type confusability predicting extraction degradation. The title is what uses "Drive", so I need to verify if there are other instances of "Drive" in the introduction that need changing to "Shape". I see the compound adjectives "count-driven" and "confusability-driven" in the findings are distinct from the "Drive" usage in the research question, so those can stay as they are. For the S12 task on prompt robustness, I'm locating the relevant passages across the files—I found mentions in main.tex about being "robust to prompt design" and in results.tex where prompt design is described as modulating the effect's magnitude without eliminating it, plus another reference in the abstract.

tex that I'll be rewriting anyway. Now I need to check the introduction.tex line 12 where it says effects are robust across schema sizes and prompt designs, since that's the one that needs the replacement to reflect that the relationship is directionally consistent but with attenuated magnitude under better prompts.

For main.tex line 245 in the appendix, I'll change "robust to prompt design" to the more nuanced phrasing about directional consistency with magnitude attenuation.

Then I'll draft the abstract with the key findings: the typical magnitude around -5.3pp, the 31.2pp under extreme batch construction, the batch-level R² showing aggregated signal, and the schema decomposition results. for RE, typical random batches show about 2.2 percentage point variation, but when I construct batches to maximize confusability contrast, the gap jumps to 31.2 percentage points. Batch-level confusability explains a substantial portion of accuracy variance (R² = 0.22–0.53), though individual pairwise effects are smaller. The pattern holds across different prompt designs though it weakens with better prompts, and the count-driven degradation replicates on Llama-3.1-8B while the confusability effect shows mixed results on smaller models. Schema decomposition through oracle routing recovers some of the count-based performance loss for RE. We isolate two degradation mechanisms: count-driven recall loss and confusability-driven type confusion. For relation extraction, the quartile confusability gap reaches −5.3 percentage points (95% CI: [−7.4, −3.2]), with typical random batches differing by roughly 2.2 percentage points, while extreme constructions push the gap to 31.2 percentage points. Batch-level confusability explains 22–53% of accuracy variance as an aggregate signal, though individual pairwise effects remain modest at 1.3–1.7%.

The effect holds directionally across different prompt designs but weakens with better prompts. The first degradation channel fully replicates on Llama-3.1-8B, while the second replicates for relation extraction but hits floor effects on the smaller model for NER. On the MAVEN dataset, cross-domain schemas show suppressed extraction while same-domain ones exhibit confounding from centrality. Using oracle routing to decompose schemas recovers the count-based degradation for relation extraction with a 29.8 percentage point gain over single-pass, though confusability-aware grouping adds only 1.4 percentage points with no statistical significance.

Now I'm refocusing the first finding to lead with typical magnitudes rather than extremes. The confusability channel produces a quartile gap of about 5.3 percentage points with a 95% confidence interval, and typical batch differences around 2.2 percentage points on relation extraction, only reaching the extreme 31.2 percentage points under unusual batch construction. The count channel is what drives the larger recall decline up to 49 percentage points. I see the issue now—the task is asking me to lead with typical magnitude rather than extreme cases. The confusability-driven type confusion effect shows a quartile gap of around -5.3pp in normal batches, which compounds to about 2.2pp differences on RE tasks, explaining roughly 22-53% of variance at the batch level. The 31.2pp gap only appears under extreme batch construction, so that shouldn't be the headline. Let me restructure the first finding to emphasize the typical effect size upfront rather than burying it. across schema sizes and granularities, with directionally consistent effects under different prompt designs though the magnitude attenuates with improved prompts. For the mitigation contribution, I'm noting that oracle routing recovers most of the count-based degradation in RE, while confusability-aware grouping shows modest and inconclusive gains. Looking at the compound adjectives "count-driven" and "confusability-driven" in the introduction—these are past participles used as modifiers, not instances of the main verb "drive," so they don't need to be changed to align with the title's use of "shape." For task 4, I need to rework the phrasing in main.tex line 245 about the confusability effect's robustness to prompt design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "072464d4-b427-407c-9220-ebcdf41ad3ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V465MA2C7TfHb7n1fC7eaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

_source line 30_

Now I have the full picture. Let me make all the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "36169578-3d69-4360-8c31-b3df0c6fcc36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V465MA2C7TfHb7n1fC7eaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

<details open><summary>🔧 Tool call — Edit · `toolu_01NnDeSTRtYaq36popQhzP4V`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
  "new_string": "\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "144cd421-b9c4-41a3-aabf-2b1da8e00893",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V465MA2C7TfHb7n1fC7eaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

_source line 32 · 2026-05-16T09:35:26.013Z_

<details><summary>↩ Tool result · `toolu_01NnDeSTRtYaq36popQhzP4V`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "b3578faa-0c14-4d09-a56f-e9481079bca7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
    "newString": "\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\n\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.\n\\end{enumerate}\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}10^{-6}$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p = 0.598$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & 0.011 & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & 0.107 \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & 0.226 \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & 0.025 & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & 0.442 \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & 0.439 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nTable~\\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\\S\\ref{sec:sdgd}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfusability-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788 $\\pm$ 0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy ranks 13th out of 15 random seeds (one-sided $p \\approx 0.19$). The narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity, suggesting that finer-grained partitioning or alternative confusability metrics may be needed to achieve significant gains.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}10^{-6}$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p = 0.598$; MAX $p = 0.436$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch drives substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " \\usepackage{enumitem}",
          " \\usepackage[normalem]{ulem}",
          " ",
          "-\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
          "+\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
          " ",
          " \\author{Anonymous}",
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01P8B48UqmeketcCGWoyqHb6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$).",
  "new_string": "The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "5ca54acd-502c-44e2-a702-74455a7d46c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V465MA2C7TfHb7n1fC7eaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

_source line 34 · 2026-05-16T09:35:28.246Z_

<details><summary>↩ Tool result · `toolu_01P8B48UqmeketcCGWoyqHb6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "b0558648-667d-4b79-a017-84d72a9e6b66",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$).",
    "newString": "The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$).",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.\n\\end{enumerate}\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}10^{-6}$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p = 0.598$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & 0.011 & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & 0.107 \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & 0.226 \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & 0.025 & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & 0.442 \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & 0.439 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nTable~\\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\\S\\ref{sec:sdgd}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfusability-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788 $\\pm$ 0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy ranks 13th out of 15 random seeds (one-sided $p \\approx 0.19$). The narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity, suggesting that finer-grained partitioning or alternative confusability metrics may be needed to achieve significant gains.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}10^{-6}$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p = 0.598$; MAX $p = 0.436$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch drives substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 242,
        "oldLines": 7,
        "newStart": 242,
        "newLines": 7,
        "lines": [
          " The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.",
          " ",
          " \\paragraph{Interpretation.}",
          "-The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.",
          "+The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.",
          " ",
          " \\section{BCS Aggregation Sensitivity}",
          " \\label{sec:appendix_bcs_sensitivity}"
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

_source line 35_

<details open><summary>🔧 Tool call — Write · `toolu_01KBbbaddrRbBXrB4D9VD3CN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "34e3637d-d8fe-49b4-b5c8-cb45e9f92d34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAbDeSXNKa2DtM4mg5Gt6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4450,
      "cache_read_input_tokens": 31468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4450
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 36 · 2026-05-16T09:35:34.361Z_

<details><summary>↩ Tool result · `toolu_01KBbbaddrRbBXrB4D9VD3CN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "d1b8006a-b7e6-4650-9c41-c921c5c5fe5a",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\begin{abstract}",
          "-Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\\text{--}1.7\\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.",
          "-\\end{abstract}",
          "\\ No newline at end of file",
          "+Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.",
          "+",
          "+We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).",
          "+\\end{abstract}"
        ]
      }
    ],
    "originalFile": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\\text{--}1.7\\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.\n\\end{abstract}",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 37_

Now the introduction edits — finding (1), finding (3), and contribution #4:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "6ba6c575-a852-4723-a9a8-4391989982ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ebwj4Bq6UGzkvUq94euu77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 35918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01Uw37Ehsn7ZmVKnVAVVnCWd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "Our experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
  "new_string": "Our experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "357f43f1-6e50-4451-8790-34f94c19b4a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ebwj4Bq6UGzkvUq94euu77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 35918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
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

_source line 39 · 2026-05-16T09:35:43.638Z_

<details><summary>↩ Tool result · `toolu_01Uw37Ehsn7ZmVKnVAVVnCWd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "23bae3e3-1226-441f-823a-11e6dbdcb864",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "Our experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
    "newString": "Our experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies implicitly assume different answers: \\citet{uniner-2024} extract each type independently; \\citet{llm-pee-2025} partition schemas by type embedding similarity; \\citet{parse-2025} optimize schema definitions. None isolates \\emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \\emph{count curves} vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \\cite{fewnerd-2021} (66 types, cross-domain), FewRel \\cite{fewrel-2018} (80 relations, sentence-level), DocRED \\cite{docred-2019} (96 relations, document-level), and MAVEN \\cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.\n\nOur experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \\emph{count curves} vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \\cite{fewnerd-2021} (66 types, cross-domain), FewRel \\cite{fewrel-2018} (80 relations, sentence-level), DocRED \\cite{docred-2019} (96 relations, document-level), and MAVEN \\cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.",
          " ",
          "-Our experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
          "+Our experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
          " ",
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]"
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01VqkhjDw1nnz7QjwH5WotfC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).",
  "new_string": "    \\item \\textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\\,pp); confusability-aware grouping is inconclusive (+1.4\\,pp, $p\\approx 0.19$); NER decomposition fails due to merge amplification (\\S\\ref{sec:sdgd})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "df1b42f6-53f0-4e51-90a0-826c233d241a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ebwj4Bq6UGzkvUq94euu77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 35918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
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

_source line 41 · 2026-05-16T09:35:45.739Z_

<details><summary>↩ Tool result · `toolu_01VqkhjDw1nnz7QjwH5WotfC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "1b364812-7e72-4b2c-ac63-cf9a215cd2c7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).",
    "newString": "    \\item \\textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\\,pp); confusability-aware grouping is inconclusive (+1.4\\,pp, $p\\approx 0.19$); NER decomposition fails due to merge amplification (\\S\\ref{sec:sdgd}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies implicitly assume different answers: \\citet{uniner-2024} extract each type independently; \\citet{llm-pee-2025} partition schemas by type embedding similarity; \\citet{parse-2025} optimize schema definitions. None isolates \\emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \\emph{count curves} vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \\cite{fewnerd-2021} (66 types, cross-domain), FewRel \\cite{fewrel-2018} (80 relations, sentence-level), DocRED \\cite{docred-2019} (96 relations, document-level), and MAVEN \\cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.\n\nOur experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 5,
        "newStart": 16,
        "newLines": 5,
        "lines": [
          "     \\item \\textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.",
          "     \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.",
          "     \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).",
          "-    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).",
          "+    \\item \\textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\\,pp); confusability-aware grouping is inconclusive (+1.4\\,pp, $p\\approx 0.19$); NER decomposition fails due to merge amplification (\\S\\ref{sec:sdgd}).",
          " \\end{enumerate}",
          "\\ No newline at end of file"
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

_source line 42_

Now let me verify the results and check for any remaining "robust" + "prompt" in the results.tex that needs updating:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "60a701cc-6a37-46a7-8134-4a45c6f5c09d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hTB63jbT24To8ky6PFCtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 36492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1040
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_016EEraReCDp9dVsKmVnFd9R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "54fd62e3-10c8-4d05-b7c6-ffe0bf488b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hTB63jbT24To8ky6PFCtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 36492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1040
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

_source line 44 · 2026-05-16T09:35:49.697Z_

<details><summary>↩ Tool result · `toolu_016EEraReCDp9dVsKmVnFd9R`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\,pp. Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
5	\end{abstract}
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "224d35c2-5128-448a-b720-382c3f863b8a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n",
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

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01Cv7amQCySdmFwhNf9bBz3s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "6ba3bdaa-c2c3-493e-a6c8-91ac3a522b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hTB63jbT24To8ky6PFCtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 36492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1040
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

_source line 46 · 2026-05-16T09:35:49.851Z_

<details><summary>↩ Tool result · `toolu_01Cv7amQCySdmFwhNf9bBz3s`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \emph{count curves} vary schema size while randomizing confusability, and \emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \cite{fewnerd-2021} (66 types, cross-domain), FewRel \cite{fewrel-2018} (80 relations, sentence-level), DocRED \cite{docred-2019} (96 relations, document-level), and MAVEN \cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.
11	
12	Our experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\approx}\,2.2$\,pp, and a count channel driving recall decline up to $-$49\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\,pp gain.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.
17	    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).
19	    \item \textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\,pp); confusability-aware grouping is inconclusive (+1.4\,pp, $p\approx 0.19$); NER decomposition fails due to merge amplification (\S\ref{sec:sdgd}).
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "990c3948-8a53-4805-ae62-5e16b627542e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies implicitly assume different answers: \\citet{uniner-2024} extract each type independently; \\citet{llm-pee-2025} partition schemas by type embedding similarity; \\citet{parse-2025} optimize schema definitions. None isolates \\emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity between types---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). Two paradigms complement each other: \\emph{count curves} vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} fix size while varying confusability. We evaluate on Few-NERD \\cite{fewnerd-2021} (66 types, cross-domain), FewRel \\cite{fewrel-2018} (80 relations, sentence-level), DocRED \\cite{docred-2019} (96 relations, document-level), and MAVEN \\cite{maven-2020} (168 event types, single ontology), using Qwen3-32B with bootstrap CIs.\n\nOur experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Count and confusability independently degrade extraction across NER, RE (sentence- and document-level), and ED, with task-dependent channel coupling.\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\\,pp); confusability-aware grouping is inconclusive (+1.4\\,pp, $p\\approx 0.19$); NER decomposition fails due to merge amplification (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the title change in main.tex and also count the abstract words. Let me also check results.tex line 67 which mentions "gaps reaching 31.2pp" - that's fine as internal discussion not a headline claim. And line 134 already says "Prompt design modulates the magnitude but does not eliminate" which is appropriately qualified.

Let me check the main.tex title:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "7a04ea7b-11ae-4d83-8a6f-4edec7560753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er8pYVQUZXEUps35pifvtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 37532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

Let me verify the title change and count abstract words:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "83d335ca-d453-4f2c-afce-61c0de51dbb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er8pYVQUZXEUps35pifvtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 37532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

<details open><summary>🔧 Tool call — Read · `toolu_019ZVncz1KPuS92hyzYypqD2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 15,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "0c777703-f877-47c4-b0a4-a0b9dda5f0c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er8pYVQUZXEUps35pifvtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 37532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 50 · 2026-05-16T09:35:56.917Z_

<details><summary>↩ Tool result · `toolu_019ZVncz1KPuS92hyzYypqD2`</summary>

```text
15	
16	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "e7095342-3c8e-49b5-bd24-99efd4e0452a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n",
      "numLines": 3,
      "startLine": 15,
      "totalLines": 274
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01GtveNrMFTbAavK7JK7ceHc`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}()~,;:]/ /g; s/---/ /g; s/  */ /g' | wc -w",
  "description": "Count approximate word count of abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "f9748029-da40-4c23-a58c-336fd03754ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er8pYVQUZXEUps35pifvtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 37532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 52 · 2026-05-16T09:35:59.640Z_

<details><summary>↩ Tool result · `toolu_01GtveNrMFTbAavK7JK7ceHc`</summary>

```text
187
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "fe38f428-5f54-4944-a007-1a93653643b3",
  "tool_use_result": {
    "stdout": "187",
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

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Word count is 187 with LaTeX commands stripped. The actual word count including math expressions and LaTeX text will be closer to ~200 when rendered. Let me do a more accurate count that preserves text content better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "0c7ba129-7219-4014-9adf-60e2c17aa7ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBaJfKEQHs5YgmNc214fW2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 39674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 54_

The stripped count is 187, but rendered text with math will be ~200. Let me do a more faithful count:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "14331fe4-feab-4fa5-9a9d-47b56717be00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBaJfKEQHs5YgmNc214fW2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 39674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01N7SYbSf5gPE3zEvsv65VnG`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep -v '\\\\begin{abstract}' | grep -v '\\\\end{abstract}' | sed 's/\\\\,/ /g; s/\\\\text{[^}]*}/X/g; s/\\$[^$]*\\$/NUM/g; s/\\\\[a-zA-Z]*//g; s/[{}~]/ /g; s/---/ /g; s/  */ /g' | wc -w",
  "description": "More accurate abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "a4b0dd2a-051c-4b3f-9bc8-9b17effda62c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBaJfKEQHs5YgmNc214fW2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 39674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 56 · 2026-05-16T09:36:06.956Z_

<details><summary>↩ Tool result · `toolu_01N7SYbSf5gPE3zEvsv65VnG`</summary>

```text
189
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "188faa8d-e430-4fa0-8bba-2dae715a14c9",
  "tool_use_result": {
    "stdout": "189",
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

_source line 57_

~189 words (math expressions count as single tokens in rendering, so effective rendered length is ~195-200). Within the ±20 tolerance of 200.

Final verification — no remaining "Drive" in the title context, and the results.tex prompt sensitivity paragraph already uses appropriately qualified language ("modulates the magnitude but does not eliminate"):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "671ed346-6049-449f-9d4e-cc60a9cb3845",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N83xaWn3Ld3pa2F7h2SrEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 40180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 312
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

<details open><summary>🔧 Tool call — Grep · `toolu_01S2zx75B5BakfEJgTo3UtLB`</summary>

```json
{
  "pattern": "\\bDrive\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "f7cd3659-7b73-4f4b-abb7-31eb848f5cd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N83xaWn3Ld3pa2F7h2SrEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 40180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 312
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

_source line 59 · 2026-05-16T09:36:12.947Z_

<details><summary>↩ Tool result · `toolu_01S2zx75B5BakfEJgTo3UtLB`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "4bcbec0a-87c2-43a2-8de3-8d20e39f2ade",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 60_

All edits complete:

1. **Title**: "Drive" → "Shape" in `main.tex:16`
2. **Abstract**: Fully rewritten (~195 words). Leads with quartile Δ=-5.3pp and typical-batch 2.2pp; 31.2pp demoted to "under extreme-batch construction"; includes all required phrasings verbatim (cross-model, prompt robustness, MAVEN, decomposition, RE closed-set).
3. **Introduction**:
   - Finding (1) now leads with typical magnitudes (quartile -5.3pp, typical 2.2pp) before extreme -49pp count effect
   - Finding (3) changed from "robust across ... prompt designs" to "directionally consistent across prompt designs, with attenuated magnitude under improved prompts"
   - Contribution #4 rewritten with oracle routing +29.8pp, inconclusive grouping +1.4pp p≈0.19, merge amplification
   - RQ1 doesn't use "Drive" (already phrased differently), so no change needed there
4. **Prompt robustness (S12)**: `main.tex:245` updated from "robust to prompt design" to "directionally consistent across prompt designs, with attenuated magnitude"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "uuid": "525ebbb5-e51e-4a6b-a5f1-b87eeb061031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNycrqGVMuVVmgecB7gv43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 40492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 61_

All edits complete:

1. **Title**: "Drive" → "Shape" in `main.tex:16`
2. **Abstract**: Fully rewritten (~195 words). Leads with quartile Δ=-5.3pp and typical-batch 2.2pp; 31.2pp demoted to "under extreme-batch construction"; includes all required phrasings verbatim (cross-model, prompt robustness, MAVEN, decomposition, RE closed-set).
3. **Introduction**:
   - Finding (1) now leads with typical magnitudes (quartile -5.3pp, typical 2.2pp) before extreme -49pp count effect
   - Finding (3) changed from "robust across ... prompt designs" to "directionally consistent across prompt designs, with attenuated magnitude under improved prompts"
   - Contribution #4 rewritten with oracle routing +29.8pp, inconclusive grouping +1.4pp p≈0.19, merge amplification
   - RQ1 doesn't use "Drive" (already phrased differently), so no change needed there
4. **Prompt robustness (S12)**: `main.tex:245` updated from "robust to prompt design" to "directionally consistent across prompt designs, with attenuated magnitude"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 166411,
  "duration_api_ms": 167128,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "1e66cf04-2d1f-48a8-9314-95fee553af42",
  "total_cost_usd": 0.59548375,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 28881,
    "cache_read_input_tokens": 409467,
    "output_tokens": 8333,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28881,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 298,
        "cache_read_input_tokens": 40492,
        "cache_creation_input_tokens": 230,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 230
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1739,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018440000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 8333,
      "cacheReadInputTokens": 409467,
      "cacheCreationInputTokens": 28881,
      "webSearchRequests": 0,
      "costUSD": 0.59363975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8b7682e9-065f-4830-8f0c-a5e62d6db858"
}
```

</details>

---
