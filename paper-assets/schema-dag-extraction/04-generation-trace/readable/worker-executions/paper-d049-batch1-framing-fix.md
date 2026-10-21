# paper d049 batch1 framing fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 115
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/workers/worker_paper_d049_batch1_framing_fix_20260516T154125.log`
- **Structured JSON:** [`8e22eb53a0af661bff17.json`](../../sessions/8e/8e22eb53a0af661bff17.json)

## Before a recorded user message

115 recorded events

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
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
    "mcp__agent-ml-research__read_project_file"
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
  "uuid": "baf98c14-056b-42fb-a236-c9307a070a5a",
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
    "resetsAt": 1778958000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "562dc6d2-9660-4b8f-96dc-117bb8f1bd2d",
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a complex multi-step task involving LaTeX paper editing. Let me break it down and start executing systematically. I need to:

1. Read the current files to understand their state
2. Make 11 modifications in priority order
3. Search for and verify references
4. Compile and check page count

Let me start by reading the relevant files and searching for references in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "70dee2fa-f7bd-4e31-85c3-5efa886aa007",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

开始执行 11 项修改。先并行读取所有需要修改的文件和搜索引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "2320e7dd-8a86-4838-b96e-4f06e74fb9cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

<details open><summary>🔧 Tool call — Read · `toolu_013BQAYu9c3YPDAAP9XEu5BV`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "37d170ae-91e5-4aa7-bfd5-969b5c98891a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 7 · 2026-05-16T15:41:40.406Z_

<details><summary>↩ Tool result · `toolu_013BQAYu9c3YPDAAP9XEu5BV`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction, the gap widens substantially (Table~\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "1cc9f769-1fe6-4bb2-a97e-d52086c98f41",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction, the gap widens substantially (Table~\\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01YJjB1ScnwVAbbQeKR6npyf`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "a5a939e4-8dda-4ae7-86f7-3554ca0b7243",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 9 · 2026-05-16T15:41:40.852Z_

<details><summary>↩ Tool result · `toolu_01YJjB1ScnwVAbbQeKR6npyf`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
11	
12	Our experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\approx}\,2.2$\,pp (quartile $\Delta = -5.3$\,pp, 95\% CI: [$-$7.4, $-$3.2]; up to 31.2\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\,pp gain.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\S\ref{sec:multi_channel}).
17	    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).
19	    \item \textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\,pp, $p\approx 0.19$). Oracle routing (+29.8\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "bda8fe20-ebdf-43d6-85fb-5aacae79c111",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01RCBgYwwyao4y3JVhs6mG3f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "803f17ee-07f2-4ec2-be49-8ff54cb8ff39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 11 · 2026-05-16T15:41:41.859Z_

<details><summary>↩ Tool result · `toolu_01RCBgYwwyao4y3JVhs6mG3f`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{llrrrrr}
36	\toprule
37	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
38	\midrule
39	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
40	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
41	\bottomrule
42	\end{tabular}}
43	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). We omit FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}
44	\label{tab:pairwise}
45	\end{table}
46	
47	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
48	
49	The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching (\S\ref{sec:practical_magnitude}).
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	We fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
55	
56	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16), confirming monotonic decline.
57	
58	\paragraph{Document-level RE (DocRED).}
59	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p < 0.001$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0])---roughly 7\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The 31.2\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \approx 7\%$ among non-zero confusion pairs (vs.\ $r^2 = 1.3$--$1.7\%$ across all pairs; Table~\ref{tab:pairwise}) aggregates to batch-level $R^2 \approx 22\%$ ($\sim$3$\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\ref{app:aggregation-sim}).
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).
71	
72	\paragraph{Prompt sensitivity.}
73	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\ref{sec:appendix_prompt_sensitivity}).
74	
75	\subsection{Multi-Channel Degradation}
76	\label{sec:multi_channel}
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
81	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
82	\label{fig:error_taxonomy}
83	\end{figure}
84	
85	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
86	
87	These results establish two channels: \textbf{Channel~1} (count predicts recall decline) and \textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\,pp, $p_{\text{TOST}} = .003$; Appendix~\ref{sec:appendix_factorial}).
88	
89	\subsection{Centrality Confound on Homogeneous Schemas}
90	\label{sec:centrality_confound}
91	
92	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "907205a1-ec3a-4af7-9dfe-34f2af76314b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}).\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01GxHh4UYQATzdZZbyrTRoEZ`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "0bf35b8e-f136-4a97-b3fe-cb9d6a895634",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 13 · 2026-05-16T15:41:42.349Z_

<details><summary>↩ Tool result · `toolu_01GxHh4UYQATzdZZbyrTRoEZ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1 extreme-batch gap; Appendix~\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \approx 7\%$) but amplifies ${\sim}3\times$ at the batch level through inter-pair correlation (Appendix~\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\%---sufficient for pre-hoc schema screening.
9	
10	\paragraph{Schema design implications.}
11	Since typical random batches differ by only ${\approx}\,2.2$\,pp (\S\ref{sec:practical_magnitude}), the practical impact depends on schema composition.
12	Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:
13	(i)~\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;
14	(ii)~\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;
15	(iii)~\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\S\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.
16	We deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.
17	
18	\paragraph{Future directions.}
19	Three directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\S\ref{sec:sdgd}).
20	
21	\section{Conclusion}
22	\label{sec:conclusion}
23	
24	We presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "459b73b4-f1ca-407a-bada-6362fcd54b40",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01M5jGbtAWdjKck4UMYsfSZs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "3aadbd38-1bcf-4e76-b536-9be3f5412038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 15 · 2026-05-16T15:41:43.262Z_

<details><summary>↩ Tool result · `toolu_01M5jGbtAWdjKck4UMYsfSZs`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.
9	
10	\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\cite{rastogi2020towards} and SGD-X~\cite{lee2022sgd} document performance degradation with schema linguistic variation. \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \citet{volkanovska2024ner} categorize LLM NER errors including type confusion.
11	
12	\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.
13	
14	\paragraph{Embedding anisotropy.}
15	Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality.
16	
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "bd906032-425a-4c29-bb58-01301914f291",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_019bGzT8YyFVaxBMDdRTG4i8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "d808e87e-c321-40ac-845c-f4e6ca445b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Tgt8a49a1gSGAML3tpCmJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "9ed8bdf4-656f-4dca-932a-e6fa2c73fd6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ZDap5Y8VzG7B8LDy2mLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14147
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

_source line 18 · 2026-05-16T15:41:43.805Z_

<details><summary>↩ Tool result · `toolu_01Tgt8a49a1gSGAML3tpCmJ5`</summary>

```text
1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
37	    year      = {2025},
38	    url       = {https://aclanthology.org/2025.findings-acl.718/},
39	}
40	
41	
42	@inproceedings{cmas-ner-2025,
43	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
44	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
45	    booktitle = {Proceedings of the ACM Web Conference 2025},
46	    year      = {2025},
47	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
48	    doi       = {10.1145/3696410.3714923},
49	}
50	
51	% =============================================================================
52	% METHOD COMPONENTS
53	% =============================================================================
54	
55	@inproceedings{uniner-2024,
56	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
57	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
58	    booktitle = {International Conference on Learning Representations},
59	    year      = {2024},
60	    url       = {https://arxiv.org/abs/2308.03279},
61	}
62	
63	@inproceedings{gollie-2024,
64	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
65	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
66	    booktitle = {International Conference on Learning Representations},
67	    year      = {2024},
68	    url       = {https://arxiv.org/abs/2310.03668},
69	}
70	
71	@inproceedings{gliner-2024,
72	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
73	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
74	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
75	    year      = {2024},
76	    url       = {https://arxiv.org/abs/2311.08526},
77	}
78	
79	@inproceedings{gliner2-2025,
80	    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},
81	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
82	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
83	    year      = {2025},
84	    url       = {https://arxiv.org/abs/2507.18546},
85	}
86	
87	
88	@inproceedings{iepile-2024,
89	    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},
90	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
91	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
92	    year      = {2024},
93	    url       = {https://arxiv.org/abs/2402.14710},
94	}
95	
96	@article{lost-in-middle-2024,
97	    title   = {Lost in the Middle: How Language Models Use Long Contexts},
98	    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
99	    journal = {Transactions of the Association for Computational Linguistics},
100	    volume  = {12},
101	    pages   = {157--173},
102	    year    = {2024},
103	    url     = {https://arxiv.org/abs/2307.03172},
104	    doi     = {10.1162/tacl_a_00638},
105	}
106	
107	% =============================================================================
108	% ZERO-SHOT NER / RE BASELINES
109	% =============================================================================
110	
111	
112	
113	% =============================================================================
114	% EVALUATION / BENCHMARKING
115	% =============================================================================
116	
117	% =============================================================================
118	% SURVEYS / BACKGROUND
119	% =============================================================================
120	
121	@article{llm4ie-survey-2024,
122	    title   = {Large Language Models for Generative Information Extraction: A Survey},
123	    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
124	    journal = {Frontiers of Computer Science},
125	    volume  = {18},
126	    number  = {6},
127	    year    = {2024},
128	    url     = {https://arxiv.org/abs/2312.17617},
129	    doi     = {10.1007/s11704-024-40555-y},
130	}
131	
132	@inproceedings{knowcoder-2024,
133	    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},
134	    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
135	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
136	    year      = {2024},
137	    url       = {https://arxiv.org/abs/2403.07969},
138	}
139	
140	@inproceedings{slot-2025,
141	    title     = {{SLOT}: Structuring the Output of Large Language Models},
142	    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},
143	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
144	    year      = {2025},
145	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
146	}
147	
148	% =============================================================================
149	% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
150	% =============================================================================
151	
152	@inproceedings{gao-repr-degen-2019,
153	    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},
154	    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
155	    booktitle = {International Conference on Learning Representations},
156	    year      = {2019},
157	    url       = {https://arxiv.org/abs/1907.12009},
158	}
159	
160	@inproceedings{ethayarajh-contextual-2019,
161	    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},
162	    author    = {Ethayarajh, Kawin},
163	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
164	    year      = {2019},
165	    url       = {https://aclanthology.org/D19-1006/},
166	}
167	
168	@inproceedings{cai-isotropy-clusters-2021,
169	    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},
170	    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},
171	    booktitle = {International Conference on Learning Representations},
172	    year      = {2021},
173	    url       = {https://openreview.net/forum?id=xYGNO86OWDH},
174	}
175	
176	
177	% =============================================================================
178	% ADDITIONAL REFERENCES (from references_survey.md only)
179	% =============================================================================
180	
181	@article{instructuie-2023,
182	    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
183	    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
184	    journal = {arXiv preprint arXiv:2304.08085},
185	    year    = {2023},
186	    url     = {https://arxiv.org/abs/2304.08085},
187	}
188	
189	@inproceedings{codeie-2023,
190	    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
191	    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
192	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
193	    year      = {2023},
194	    url       = {https://aclanthology.org/2023.acl-long.855/},
195	}
196	
197	@inproceedings{adelie-2024,
198	    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
199	    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
200	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
201	    year      = {2024},
202	    url       = {https://aclanthology.org/2024.emnlp-main.419/},
203	}
204	
205	@inproceedings{oneke-2025,
206	    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},
207	    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},
208	    booktitle = {Companion Proceedings of the ACM Web Conference 2025},
209	    year      = {2025},
210	    url       = {https://arxiv.org/abs/2412.20005},
211	    doi       = {10.1145/3701716.3715189},
212	}
213	
214	
215	@inproceedings{llm-calibration-survey-2024,
216	    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},
217	    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
218	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
219	    year      = {2024},
220	    url       = {https://aclanthology.org/2024.naacl-long.366/},
221	}
222	
223	
224	% =============================================================================
225	% DATASETS
226	% =============================================================================
227	
228	@inproceedings{fewnerd-2021,
229	    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
230	    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},
231	    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
232	    year      = {2021},
233	    url       = {https://aclanthology.org/2021.acl-long.248/},
234	}
235	
236	@inproceedings{fewrel-2018,
237	    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},
238	    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},
239	    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
240	    year      = {2018},
241	    url       = {https://aclanthology.org/D18-1514/},
242	}
243	
244	@inproceedings{maven-2020,
245	    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},
246	    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},
247	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
248	    year      = {2020},
249	    url       = {https://aclanthology.org/2020.emnlp-main.129/},
250	}
251	
252	@inproceedings{docred-2019,
253	    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
254	    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
255	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
256	    year      = {2019},
257	    url       = {https://aclanthology.org/P19-1074/},
258	}
259	
260	% =============================================================================
261	% MODELS AND TOOLS
262	% =============================================================================
263	
264	@article{qwen3-2025,
265	    title   = {Qwen3 Technical Report},
266	    author  = {{Qwen Team}},
267	    journal = {arXiv preprint arXiv:2505.09388},
268	    year    = {2025},
269	    url     = {https://arxiv.org/abs/2505.09388},
270	}
271	
272	@article{llama3-2024,
273	    title   = {The {Llama} 3 Herd of Models},
274	    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and others},
275	    journal = {arXiv preprint arXiv:2407.21783},
276	    year    = {2024},
277	    url     = {https://arxiv.org/abs/2407.21783},
278	}
279	
280	@inproceedings{sentence-bert-2019,
281	    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
282	    author    = {Reimers, Nils and Gurevych, Iryna},
283	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
284	    year      = {2019},
285	    url       = {https://aclanthology.org/D19-1410/},
286	}
287	
288	@inproceedings{minilm-2020,
289	    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},
290	    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},
291	    booktitle = {Advances in Neural Information Processing Systems},
292	    volume    = {33},
293	    year      = {2020},
294	    url       = {https://arxiv.org/abs/2002.10957},
295	}
296	
297	@inproceedings{reflect-learn-2026,
298	    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},
299	    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},
300	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
301	    pages     = {34923--34931},
302	    year      = {2026},
303	    url       = {https://arxiv.org/abs/2508.10036},
304	    doi       = {10.1609/aaai.v40i41.40796},
305	}
306	
307	@article{sclar-sensitivity-2024,
308	    title   = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},
309	    author  = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
310	    journal = {Transactions of the Association for Computational Linguistics},
311	    volume  = {12},
312	    year    = {2024},
313	    url     = {https://arxiv.org/abs/2310.11324},
314	}
315	
316	@inproceedings{vllm-2023,
317	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
318	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
319	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
320	    year      = {2023},
321	    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},
322	}
323	
324	@inproceedings{xie-zeroshot-ner-2023,
325	    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
326	    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
327	    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
328	    year      = {2023},
329	    url       = {https://aclanthology.org/2023.emnlp-main.493/},
330	}
331	
332	@inproceedings{wadhwa-re-llm-2023,
333	    title     = {Revisiting Relation Extraction in the era of Large Language Models},
334	    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},
335	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
336	    pages     = {15566--15589},
337	    year      = {2023},
338	    url       = {https://aclanthology.org/2023.acl-long.868/},
339	}
340	
341	@inproceedings{relationprompt-2022,
342	    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},
343	    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},
344	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
345	    pages     = {45--57},
346	    year      = {2022},
347	    url       = {https://aclanthology.org/2022.findings-acl.5/},
348	}
349	
350	@article{promptner-2023,
351	    title   = {{PromptNER}: Prompting For Named Entity Recognition},
352	    author  = {Ashok, Dhananjay and Lipton, Zachary C.},
353	    journal = {arXiv preprint arXiv:2305.15444},
354	    year    = {2023},
355	    url     = {https://arxiv.org/abs/2305.15444},
356	}
357	
358	@article{json-schema-bench-2025,
359	    title   = {Generating Structured Outputs from Language Models: Benchmark and Studies},
360	    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},
361	    journal = {arXiv preprint arXiv:2501.10868},
362	    year    = {2025},
363	    url     = {https://arxiv.org/abs/2501.10868},
364	}
365	
366	@inproceedings{rastogi2020towards,
367	    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},
368	    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Srinivas, Sber and Guber, Raghav and Nakhost, Mehran},
369	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
370	    volume    = {34},
371	    pages     = {8689--8696},
372	    year      = {2020},
373	    url       = {https://arxiv.org/abs/1909.05855},
374	}
375	
376	@article{li2023evaluating,
377	    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},
378	    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},
379	    journal = {arXiv preprint arXiv:2304.11633},
380	    year    = {2023},
381	    url     = {https://arxiv.org/abs/2304.11633},
382	}
383	
384	@inproceedings{lee2022sgd,
385	    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},
386	    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},
387	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
388	    volume    = {36},
389	    pages     = {10938--10946},
390	    year      = {2022},
391	    url       = {https://arxiv.org/abs/2110.06800},
392	}
393	
394	@article{volkanovska2024ner,
395	    title   = {A Study of Errors in the Output of Large Language Models for Named Entity Recognition},
396	    author  = {Volkanovska, Elena and Padó, Sebastian and Möller, Knud},
397	    journal = {Journal for Language Technology and Computational Linguistics},
398	    volume  = {37},
399	    number  = {1},
400	    year    = {2024},
401	    url     = {https://jlcl.org/article/download/281/263/423},
402	}
403	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "aee2f831-3e3d-48b8-8948-bccc5f3caeb6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "% References for Schema-DAG-Extraction\n% Generated: 2026-05-15\n% Sources: literature_map.yaml + references_survey.md\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@article{parse-2025,\n    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    journal = {arXiv preprint arXiv:2510.08623},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.08623},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2507.18546},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.14710},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n@inproceedings{gao-repr-degen-2019,\n    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},\n    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1907.12009},\n}\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n@inproceedings{llm-calibration-survey-2024,\n    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.366/},\n}\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and others},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@article{sclar-sensitivity-2024,\n    title   = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author  = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {Generating Structured Outputs from Language Models: Benchmark and Studies},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Srinivas, Sber and Guber, Raghav and Nakhost, Mehran},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{volkanovska2024ner,\n    title   = {A Study of Errors in the Output of Large Language Models for Named Entity Recognition},\n    author  = {Volkanovska, Elena and Padó, Sebastian and Möller, Knud},\n    journal = {Journal for Language Technology and Computational Linguistics},\n    volume  = {37},\n    number  = {1},\n    year    = {2024},\n    url     = {https://jlcl.org/article/download/281/263/423},\n}\n",
      "numLines": 403,
      "startLine": 1,
      "totalLines": 403
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T15:41:43.940Z_

<details><summary>↩ Tool result · `toolu_019bGzT8YyFVaxBMDdRTG4i8`</summary>

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
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\text{TOST}} = .003$, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
47	
48	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
49	
50	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.
51	
52	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\%$\to$50.4\%) cannot be explained by uniform contamination, which would elevate all conditions equally.
53	\end{enumerate}
54	
55	\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.
56	
57	\input{checklist}
58	
59	\bibliography{references}
60	
61	\appendix
62	
63	\section{Additional Figures}
64	\label{sec:appendix_figures}
65	
66	\begin{table}[h]
67	\centering
68	\small
69	\begin{tabular}{lrr}
70	\toprule
71	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
72	\midrule
73	1 & 0.702 & 0.640 \\
74	64 & 0.273 & 0.304 \\
75	\midrule
76	Decline & $-$43\,pp & $-$34\,pp \\
77	\bottomrule
78	\end{tabular}
79	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
80	\label{tab:cross_model}
81	\end{table}
82	
83	\begin{table}[h]
84	\centering
85	\small
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{crrrrrr}
88	\toprule
89	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
90	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
91	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
92	\midrule
93	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
94	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
95	\bottomrule
96	\end{tabular}}
97	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
98	\label{tab:cross_model_bcs}
99	\end{table}
100	
101	\begin{table}[h]
102	\centering
103	\small
104	\resizebox{\columnwidth}{!}{%
105	\begin{tabular}{llrrrrrrr}
106	\toprule
107	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
108	\cmidrule(lr){3-7}
109	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
110	\midrule
111	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
112	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
113	\midrule
114	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
115	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
116	\bottomrule
117	\end{tabular}}
118	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
119	\label{tab:error_taxonomy}
120	\end{table}
121	
122	\section{SDGD Full Protocol and Results}
123	\label{sec:appendix_sdgd}
124	
125	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
126	
127	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
128	
129	\begin{table}[h]
130	\centering
131	\small
132	\resizebox{\columnwidth}{!}{%
133	\begin{tabular}{lrccc}
134	\toprule
135	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
136	\midrule
137	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
138	\midrule
139	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
140	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
141	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
142	\midrule
143	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
144	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
145	\bottomrule
146	\end{tabular}}
147	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
148	\label{tab:sdgd_results}
149	\end{table}
150	
151	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.
152	
153	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
154	
155	\section{Factorial Analysis and Separability Test}
156	\label{sec:appendix_factorial}
157	
158	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = .003$), supporting an additive model of count and confusability effects.
159	
160	A separate within-dataset $2 \times 2$ factorial on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
161	
162	\section{Within-Pool CI Details}
163	\label{sec:appendix_within_pool}
164	
165	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
166	
167	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
168	\label{sec:appendix_residualized_bcs}
169	
170	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
171	
172	\paragraph{Confound identification.}
173	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
174	\begin{itemize}[itemsep=2pt,leftmargin=*]
175	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.
176	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.
177	\end{itemize}
178	
179	\paragraph{Partial correlation results.}
180	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
181	
182	\begin{table}[h]
183	\centering
184	\small
185	\resizebox{\columnwidth}{!}{%
186	\begin{tabular}{llcccc}
187	\toprule
188	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
189	\midrule
190	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
191	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
192	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
193	\midrule
194	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
195	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
196	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
197	\bottomrule
198	\end{tabular}}
199	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
200	\label{tab:residualized_bcs}
201	\end{table}
202	
203	\paragraph{Interpretation.}
204	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
205	
206	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
207	
208	\section{Batch Composition Results}
209	\label{sec:appendix_batch_composition}
210	
211	See Table~\ref{tab:batch_composition} and the accompanying discussion in \S\ref{sec:sdgd}.
212	
213	\input{prompt_appendix}
214	
215	\section{Prompt Version Sensitivity Analysis}
216	\label{sec:appendix_prompt_sensitivity}
217	
218	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
219	
220	\paragraph{RE (FewRel).}
221	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
222	
223	\paragraph{NER (Few-NERD).}
224	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
225	
226	\paragraph{Interpretation.}
227	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.
228	
229	\section{BCS Aggregation Sensitivity}
230	\label{sec:appendix_bcs_sensitivity}
231	
232	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\resizebox{\columnwidth}{!}{%
238	\begin{tabular}{llcccc}
239	\toprule
240	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
241	\midrule
242	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
243	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
244	\midrule
245	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
246	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
247	\bottomrule
248	\end{tabular}}
249	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
250	\label{tab:bcs_aggregation}
251	\end{table}
252	
253	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
254	
255	\section{BCS-Controlled Detailed Results}
256	\label{app:bcs-controlled-table}
257	
258	\begin{table}[h]
259	\centering
260	\small
261	\resizebox{\columnwidth}{!}{%
262	\begin{tabular}{lcrrrr}
263	\toprule
264	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
265	\midrule
266	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
267	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
268	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
269	\bottomrule
270	\end{tabular}}
271	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
272	\label{tab:bcs_controlled}
273	\end{table}
274	
275	\section{Within-Pool Analysis Methodology}
276	\label{app:within-pool-method}
277	
278	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
279	
280	\begin{table}[h]
281	\centering
282	\small
283	\resizebox{\columnwidth}{!}{%
284	\begin{tabular}{lrrrrrrr}
285	\toprule
286	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
287	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
288	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
289	\midrule
290	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
291	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
292	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
293	\midrule
294	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
295	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
296	\bottomrule
297	\end{tabular}}
298	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
299	\label{tab:within_pool}
300	\end{table}
301	
302	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
303	
304	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
305	
306	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
307	\label{app:scs-ablation}
308	
309	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
310	
311	\begin{table}[h]
312	\centering
313	\small
314	\begin{tabular}{lcccc}
315	\toprule
316	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
317	\midrule
318	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
319	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
320	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
321	\bottomrule
322	\end{tabular}
323	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates no systematic benefit from including definitions.}
324	\label{tab:scs-ablation}
325	\end{table}
326	
327	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
328	
329	\section{Pair-to-Batch Aggregation Simulation}
330	\label{app:aggregation-sim}
331	
332	We verify that the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation.
333	
334	\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
335	
336	\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
337	
338	\section{Cross-Domain Connections}
339	\label{app:cross-domain}
340	
341	The schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
342	
343	\end{document}
344	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4863a638-1e46-4f3e-864e-3868973e5b0e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
      "numLines": 344,
      "startLine": 1,
      "totalLines": 344
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good, I've read all the files. Now let me start the WebSearch for the references, and make the edits in parallel. Let me first search for the references using WebSearch, and then make all the edits.

Let me fetch the WebSearch tool first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "af51ae6e-fe20-4215-b528-c69733c6ab81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011igyctmShARYCKRbZFJMJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7703,
      "cache_creation_input_tokens": 17929,
      "cache_read_input_tokens": 25988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17929
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

_source line 21_

Files read. Now searching for references and making edits. Let me fetch the WebSearch tool first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "37f26d71-ce95-46db-8385-e6ac3ee082eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011igyctmShARYCKRbZFJMJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7703,
      "cache_creation_input_tokens": 17929,
      "cache_read_input_tokens": 25988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17929
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

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LP9kFPAf9zkqwyRWR8hSiY`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "8cf24f4b-ae16-4002-a605-c27b06def474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011igyctmShARYCKRbZFJMJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7703,
      "cache_creation_input_tokens": 17929,
      "cache_read_input_tokens": 25988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17929
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

_source line 23 · 2026-05-16T15:41:48.416Z_

<details><summary>↩ Tool result · `toolu_01LP9kFPAf9zkqwyRWR8hSiY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "eab1b926-9795-4314-ac6d-383b5ad2ed84",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 20
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Let me start the WebSearch calls for all 5 references in parallel, and also start making the straightforward edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "9088af78-ba3e-4407-91e3-82c0ee41c56e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 25_

Searching for all references in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "ba402d28-b035-44f4-a04b-69be8a0f6def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vp9EbdQ53hpSbxd2ifNs32`</summary>

```json
{
  "query": "From Haystack to Needle LLM label space reduction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "18f51460-2b70-46db-8d3b-f89f5dcfa64e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NsRo4rxpvrEshhgsrRoqN1`</summary>

```json
{
  "query": "Lakens 2013 calculating reporting effect sizes Frontiers Psychology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "21804d8b-959a-4ac0-82a7-cd3169676164",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QgsYtsxZVZw6JzmcEzuMgr`</summary>

```json
{
  "query": "Deng 2010 classifying 10000 image categories ECCV"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "5e232f84-8c54-41fb-9f9d-229b422bf18c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013uPGQwi7fA81xHfH6Fb6aw`</summary>

```json
{
  "query": "Rothman 1990 no adjustments multiple comparisons Epidemiology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "6dcf07c8-b1dd-4a28-8149-012edfc9ead3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LT1jNGyT8pvCwLRWudw1JY`</summary>

```json
{
  "query": "Cohen 1988 Statistical Power Analysis Behavioral Sciences Routledge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "eafb696f-4c30-4655-a9f5-3ebc759fa0c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCp4h2AT3gasoDYK9pYXyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8500,
      "cache_read_input_tokens": 43917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8500
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 31 · 2026-05-16T15:41:57.840Z_

<details><summary>↩ Tool result · `toolu_01NsRo4rxpvrEshhgsrRoqN1`</summary>

```text
Web search results for query: "Lakens 2013 calculating reporting effect sizes Frontiers Psychology"

Links: [{"title":"Daniel Lakens - Effect Sizes","url":"https://sites.google.com/site/lakens2/effect-sizes"},{"title":"Frontiers | Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00863/full"},{"title":"[PDF] Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calculating-and-reporting-effect-sizes-to-science:-Lakens/c65c650de3de909adfa0028d170e21489000162c"},{"title":"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/24324449/"},{"title":"Calculating and reporting effect sizes to facilitate ...","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00863/pdf"},{"title":"Lakens D. Calculating and reporting effect sizes to facilitate ...","url":"https://www.researchgate.net/publication/259268673_Lakens_D_Calculating_and_reporting_effect_sizes_to_facilitate_cumulative_science_a_practical_primer_for_t-tests_and_ANOVAs_Front_Psychol_4_863"},{"title":"Lakens, D. (2013) Calculating and Reporting Effect Sizes to Facilitate Cumulative Science Practical Primer t-Tests and ANOVAs. Frontiers in Psychology, 4, Article 863. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3475328"},{"title":"Lakens, D, „Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-test and ANOVAs,” &lt;i>Frontiers in Psychology&lt;/i>, 4, 1-12, 2013.","url":"https://www.sciepub.com/reference/195896"},{"title":"Calculating and reporting effect sizes to facilitate cumulative science : a practical primer for t-tests and ANOVAs - Research portal Eindhoven University of Technology","url":"https://research.tue.nl/en/publications/calculating-and-reporting-effect-sizes-to-facilitate-cumulative-s"},{"title":"Lakens, D. (2013) Calculating and Reporting Effect Sizes to Facilitate Cumulatie Science A Practical Primer for T-Tests and ANOVAs. Front in Psychology, 4, 863. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2257684"}]

I found the article you're looking for. Here are the search results:

## Publication Details

Lakens, D. (2013) published "Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs" in Frontiers in Psychology, 4:863.

## Article Overview

The article aims to provide a practical primer on how to calculate and report effect sizes for t-tests and ANOVA's such that effect sizes can be used in a-priori power analyses and meta-analyses. 

Whereas many articles about effect sizes focus on between-subjects designs and address within-subjects designs only briefly, the article provides a detailed overview of the similarities and differences between within- and between-subjects designs.

A supplementary spreadsheet is provided to make it as easy as possible for researchers to incorporate effect size calculations into their workflow.

## Access

The article is available through Frontiers in Psychology. You can access the full text at: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00863/full

The DOI is: 10.3389/fpsyg.2013.00863


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "ca6de53b-1325-47fd-b9ea-1951e43c4354",
  "tool_use_result": {
    "query": "Lakens 2013 calculating reporting effect sizes Frontiers Psychology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EvUfsYk2AX9KXevmKNyBoV",
        "content": [
          {
            "title": "Daniel Lakens - Effect Sizes",
            "url": "https://sites.google.com/site/lakens2/effect-sizes"
          },
          {
            "title": "Frontiers | Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs",
            "url": "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00863/full"
          },
          {
            "title": "[PDF] Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Calculating-and-reporting-effect-sizes-to-science:-Lakens/c65c650de3de909adfa0028d170e21489000162c"
          },
          {
            "title": "Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/24324449/"
          },
          {
            "title": "Calculating and reporting effect sizes to facilitate ...",
            "url": "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00863/pdf"
          },
          {
            "title": "Lakens D. Calculating and reporting effect sizes to facilitate ...",
            "url": "https://www.researchgate.net/publication/259268673_Lakens_D_Calculating_and_reporting_effect_sizes_to_facilitate_cumulative_science_a_practical_primer_for_t-tests_and_ANOVAs_Front_Psychol_4_863"
          },
          {
            "title": "Lakens, D. (2013) Calculating and Reporting Effect Sizes to Facilitate Cumulative Science Practical Primer t-Tests and ANOVAs. Frontiers in Psychology, 4, Article 863. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3475328"
          },
          {
            "title": "Lakens, D, „Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-test and ANOVAs,” &lt;i>Frontiers in Psychology&lt;/i>, 4, 1-12, 2013.",
            "url": "https://www.sciepub.com/reference/195896"
          },
          {
            "title": "Calculating and reporting effect sizes to facilitate cumulative science : a practical primer for t-tests and ANOVAs - Research portal Eindhoven University of Technology",
            "url": "https://research.tue.nl/en/publications/calculating-and-reporting-effect-sizes-to-facilitate-cumulative-s"
          },
          {
            "title": "Lakens, D. (2013) Calculating and Reporting Effect Sizes to Facilitate Cumulatie Science A Practical Primer for T-Tests and ANOVAs. Front in Psychology, 4, 863. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=2257684"
          }
        ]
      },
      "I found the article you're looking for. Here are the search results:\n\n## Publication Details\n\nLakens, D. (2013) published \"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\" in Frontiers in Psychology, 4:863.\n\n## Article Overview\n\nThe article aims to provide a practical primer on how to calculate and report effect sizes for t-tests and ANOVA's such that effect sizes can be used in a-priori power analyses and meta-analyses. \n\nWhereas many articles about effect sizes focus on between-subjects designs and address within-subjects designs only briefly, the article provides a detailed overview of the similarities and differences between within- and between-subjects designs.\n\nA supplementary spreadsheet is provided to make it as easy as possible for researchers to incorporate effect size calculations into their workflow.\n\n## Access\n\nThe article is available through Frontiers in Psychology. You can access the full text at: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00863/full\n\nThe DOI is: 10.3389/fpsyg.2013.00863"
    ],
    "durationSeconds": 4.243794995
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T15:41:59.805Z_

<details><summary>↩ Tool result · `toolu_01LT1jNGyT8pvCwLRWudw1JY`</summary>

```text
Web search results for query: "Cohen 1988 Statistical Power Analysis Behavioral Sciences Routledge"

Links: [{"title":"Statistical Power Analysis for the Behavioral Sciences - 2nd Edition -","url":"https://www.routledge.com/Statistical-Power-Analysis-for-the-Behavioral-Sciences/Cohen/p/book/9780805802832"},{"title":"Statistical Power Analysis for the Behavioral Sciences | Jacob Cohen |","url":"https://www.taylorfrancis.com/books/mono/10.4324/9780203771587/statistical-power-analysis-behavioral-sciences-jacob-cohen"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition): Cohen, Jacob: 9780805802832: Amazon.com: Books","url":"https://www.amazon.com/Statistical-Power-Analysis-Behavioral-Sciences/dp/0805802835"},{"title":"Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3845582"},{"title":"Statistical Power Analysis for the Behavioral Sciences - Jacob Cohen - Google Books","url":"https://books.google.com/books/about/Statistical_Power_Analysis_for_the_Behav.html?id=gA04ngAACAAJ"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition) - Cohen, Jacob: 9780805802832 - AbeBooks","url":"https://www.abebooks.com/9780805802832/Statistical-Power-Analysis-Behavioral-Sciences-0805802835/plp"},{"title":"Statistical Power Analysis for the Behavioral Sciences by Jacob Cohen | Hardcover | 1988-07-01 | Routledge | 9780805802832 | Biblio","url":"https://www.biblio.com/9780805802832"},{"title":"Statistical Power Analysis for the Behavioral Sciences | ScienceDirect","url":"https://www.sciencedirect.com/book/monograph/9780121790608/statistical-power-analysis-for-the-behavioral-sciences"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition) by Cohen, Jacob | Hardcover | 1988-07-01 | Routledge | 9780805802832 | Biblio","url":"https://www.biblio.com/book/statistical-power-analysis-behavioral-sciences-2nd/d/1396498660"},{"title":"Cohen J. &lt;i>Statistical Power Analysis for the Behavioral Sciences&lt;/i>. Routledge; 1988.","url":"https://www.sciepub.com/reference/386702"}]

Based on the search results, I found information about the book you're looking for:

Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge.

The publication date was July 1, 1988, and it is 590 pages long. Statistical Power Analysis is a nontechnical guide to power analysis in research planning that provides users of applied statistics with the tools they need for more effective analysis.

The Second Edition includes a chapter covering power analysis in set correlation and multivariate methods; a chapter considering effect size, psychometric reliability, and the efficacy of "qualifying" dependent variables; and expanded power and sample size tables for multiple regression/correlation.

The book is highly regarded in the research community. It ranks as a required reference for research grant applications in the social sciences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "f734e8fb-4697-49f2-9d5c-12e1419a77db",
  "tool_use_result": {
    "query": "Cohen 1988 Statistical Power Analysis Behavioral Sciences Routledge",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S24iJgLqnD5CnKyKQmZUTg",
        "content": [
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences - 2nd Edition -",
            "url": "https://www.routledge.com/Statistical-Power-Analysis-for-the-Behavioral-Sciences/Cohen/p/book/9780805802832"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences | Jacob Cohen |",
            "url": "https://www.taylorfrancis.com/books/mono/10.4324/9780203771587/statistical-power-analysis-behavioral-sciences-jacob-cohen"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences (2nd Edition): Cohen, Jacob: 9780805802832: Amazon.com: Books",
            "url": "https://www.amazon.com/Statistical-Power-Analysis-Behavioral-Sciences/dp/0805802835"
          },
          {
            "title": "Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3845582"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences - Jacob Cohen - Google Books",
            "url": "https://books.google.com/books/about/Statistical_Power_Analysis_for_the_Behav.html?id=gA04ngAACAAJ"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences (2nd Edition) - Cohen, Jacob: 9780805802832 - AbeBooks",
            "url": "https://www.abebooks.com/9780805802832/Statistical-Power-Analysis-Behavioral-Sciences-0805802835/plp"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences by Jacob Cohen | Hardcover | 1988-07-01 | Routledge | 9780805802832 | Biblio",
            "url": "https://www.biblio.com/9780805802832"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences | ScienceDirect",
            "url": "https://www.sciencedirect.com/book/monograph/9780121790608/statistical-power-analysis-for-the-behavioral-sciences"
          },
          {
            "title": "Statistical Power Analysis for the Behavioral Sciences (2nd Edition) by Cohen, Jacob | Hardcover | 1988-07-01 | Routledge | 9780805802832 | Biblio",
            "url": "https://www.biblio.com/book/statistical-power-analysis-behavioral-sciences-2nd/d/1396498660"
          },
          {
            "title": "Cohen J. &lt;i>Statistical Power Analysis for the Behavioral Sciences&lt;/i>. Routledge; 1988.",
            "url": "https://www.sciepub.com/reference/386702"
          }
        ]
      },
      "Based on the search results, I found information about the book you're looking for:\n\nCohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge.\n\nThe publication date was July 1, 1988, and it is 590 pages long. Statistical Power Analysis is a nontechnical guide to power analysis in research planning that provides users of applied statistics with the tools they need for more effective analysis.\n\nThe Second Edition includes a chapter covering power analysis in set correlation and multivariate methods; a chapter considering effect size, psychometric reliability, and the efficacy of \"qualifying\" dependent variables; and expanded power and sample size tables for multiple regression/correlation.\n\nThe book is highly regarded in the research community. It ranks as a required reference for research grant applications in the social sciences."
    ],
    "durationSeconds": 3.934159437000002
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T15:42:00.178Z_

<details><summary>↩ Tool result · `toolu_01Vp9EbdQ53hpSbxd2ifNs32`</summary>

```text
Web search results for query: "From Haystack to Needle LLM label space reduction 2025"

Links: [{"title":"[2502.08436] From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/abs/2502.08436"},{"title":"From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/html/2502.08436v2"},{"title":"[Literature Review] From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://www.themoonlight.io/en/review/from-haystack-to-needle-label-space-reduction-for-zero-shot-classification"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3175&show=50"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=1500&show=50"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=1700&show=25"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=4050&show=2000"},{"title":"Hidden in the Haystack: Smaller Needles are More Difficult for LLMs to Find | OpenReview","url":"https://openreview.net/forum?id=PlH3YDvGhF"},{"title":"Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/pdf/2502.08436"},{"title":"Can LLMs Find a Needle in a Haystack? A Look at Anomaly Detection Language Modeling - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.341/"}]

I found relevant information about your search query. Here are the key results:

## "From Haystack to Needle: Label Space Reduction for Zero-shot Classification"

This paper presents Label Space Reduction (LSR), a novel method for improving zero-shot classification performance of Large Language Models (LLMs). LSR iteratively refines the classification label space by systematically ranking and reducing candidate classes, enabling the model to concentrate on the most relevant options.

### Key Features:

- **Dynamic Optimization**: LSR leverages unlabeled data with the statistical learning capabilities of data-driven models to dynamically optimize the label space representation at test time.

- **Performance Improvements**: Experiments across seven benchmarks demonstrate that LSR improves macro-F1 scores by an average of 7.0% (up to 14.2%) with Llama-3.1-70B and 3.3% (up to 11.1%) with Claude-3.5-Sonnet compared to standard zero-shot classification baselines.

- **Computational Efficiency**: To reduce the computational overhead of LSR, which requires an additional LLM call at each iteration, the authors propose distilling the model into a probabilistic classifier, allowing for efficient inference.

### Authors and Status:

The paper is by Nathan Vandemoortele, Bram Steenwinckel, Femke Ongenae, and Sofie Van Hoecke and is under review at ICML 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "f18b8dfb-c342-454c-824a-41a7efce7478",
  "tool_use_result": {
    "query": "From Haystack to Needle LLM label space reduction 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KDSzuUwm9Xn3qQusPBoWfv",
        "content": [
          {
            "title": "[2502.08436] From Haystack to Needle: Label Space Reduction for Zero-shot Classification",
            "url": "https://arxiv.org/abs/2502.08436"
          },
          {
            "title": "From Haystack to Needle: Label Space Reduction for Zero-shot Classification",
            "url": "https://arxiv.org/html/2502.08436v2"
          },
          {
            "title": "[Literature Review] From Haystack to Needle: Label Space Reduction for Zero-shot Classification",
            "url": "https://www.themoonlight.io/en/review/from-haystack-to-needle-label-space-reduction-for-zero-shot-classification"
          },
          {
            "title": "Machine Learning Feb 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-02?skip=3175&show=50"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=1500&show=50"
          },
          {
            "title": "Artificial Intelligence Feb 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-02?skip=1700&show=25"
          },
          {
            "title": "Computer Science Feb 2025",
            "url": "https://arxiv.org/list/cs/2025-02?skip=4050&show=2000"
          },
          {
            "title": "Hidden in the Haystack: Smaller Needles are More Difficult for LLMs to Find | OpenReview",
            "url": "https://openreview.net/forum?id=PlH3YDvGhF"
          },
          {
            "title": "Label Space Reduction for Zero-shot Classification",
            "url": "https://arxiv.org/pdf/2502.08436"
          },
          {
            "title": "Can LLMs Find a Needle in a Haystack? A Look at Anomaly Detection Language Modeling - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.341/"
          }
        ]
      },
      "I found relevant information about your search query. Here are the key results:\n\n## \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\"\n\nThis paper presents Label Space Reduction (LSR), a novel method for improving zero-shot classification performance of Large Language Models (LLMs). LSR iteratively refines the classification label space by systematically ranking and reducing candidate classes, enabling the model to concentrate on the most relevant options.\n\n### Key Features:\n\n- **Dynamic Optimization**: LSR leverages unlabeled data with the statistical learning capabilities of data-driven models to dynamically optimize the label space representation at test time.\n\n- **Performance Improvements**: Experiments across seven benchmarks demonstrate that LSR improves macro-F1 scores by an average of 7.0% (up to 14.2%) with Llama-3.1-70B and 3.3% (up to 11.1%) with Claude-3.5-Sonnet compared to standard zero-shot classification baselines.\n\n- **Computational Efficiency**: To reduce the computational overhead of LSR, which requires an additional LLM call at each iteration, the authors propose distilling the model into a probabilistic classifier, allowing for efficient inference.\n\n### Authors and Status:\n\nThe paper is by Nathan Vandemoortele, Bram Steenwinckel, Femke Ongenae, and Sofie Van Hoecke and is under review at ICML 2025."
    ],
    "durationSeconds": 7.127962219999998
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T15:42:00.369Z_

<details><summary>↩ Tool result · `toolu_013uPGQwi7fA81xHfH6Fb6aw`</summary>

```text
Web search results for query: "Rothman 1990 no adjustments multiple comparisons Epidemiology"

Links: [{"title":"No Adjustments Are Needed for Multiple Comparisons : Epidemiology","url":"https://journals.lww.com/epidem/abstract/1990/01000/no_adjustments_are_needed_for_multiple_comparisons.10.aspx"},{"title":"[PDF] No Adjustments Are Needed for Multiple Comparisons | Semantic Scholar","url":"https://www.semanticscholar.org/paper/No-Adjustments-Are-Needed-for-Multiple-Comparisons-Rothman/7cdae9ece0e94ad740189e7b328bbf6993b4c8d5"},{"title":"Empirical-Bayes adjustments for multiple comparisons are sometimes useful - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/1912039/"},{"title":"Rothman (1990) No adjustments are needed for multiple comparisons.pdf","url":"https://www.scribd.com/document/321113650/Rothman-1990-No-adjustments-are-needed-for-multiple-comparisons-pdf"},{"title":"No adjustments are needed for multiple comparisons","url":"https://pubmed.ncbi.nlm.nih.gov/2081237/"},{"title":"Rothman, K.J. (1990) No adjustments are needed for multiple comparisons. Epidemiology, 1, 43-46. doi10.1097/00001648-199001000-00010 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=768985"},{"title":"Dealing with multiple testing: To adjust or not to adjust","url":"https://arxiv.org/pdf/2010.02205"},{"title":"K. J. Rothman, “No Adjustments Are Needed for Multiple Comparisons,” Epidemi-ology, Vol. 1, No. 1, 1990, pp. 43-46. doi10.1097/00001648-199001000-00010 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=411541"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=No+adjustments+are+needed+for+multiple+comparisons&amp=&author=KJ+Rothman&amp=&publication_year=1990&amp=&journal=Epidemiology&amp=&pages=43-46&amp=&doi=10.1097/00001648-199001000-00010&amp=&pmid=2081237"},{"title":"GraphPad Prism 11 Statistics Guide - When it makes sense to not correct for multiple comparisons","url":"https://www.graphpad.com/guides/prism/latest/statistics/stat_when_to_not_correct_for_2.htm"}]

I found the paper you're searching for. Kenneth J. Rothman published "No Adjustments Are Needed for Multiple Comparisons" in Epidemiology, volume 1, issue 1 in January 1990.

The paper's main argument is that a policy of not making adjustments for multiple comparisons is preferable because it will lead to fewer errors of interpretation when the data under evaluation are not random numbers but actual observations.

Rothman's key critique of adjustment procedures is that reducing the type I error for null associations increases the type II error for those associations that are not null. He argues that the theoretical basis for advocating a routine adjustment for multiple comparisons is the "universal null hypothesis" that "chance" serves as the first-order explanation for observed phenomena, which he contends undermines empirical research.

This paper has become highly influential in epidemiology and statistics, and has over 5,500 citations. It remains a key reference point in debates about whether multiple comparison adjustments should be routinely applied.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "005e1f94-ce02-4b68-bc66-4625cc60cf93",
  "tool_use_result": {
    "query": "Rothman 1990 no adjustments multiple comparisons Epidemiology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GNiGKHTQDuxoHzdgb5XPEr",
        "content": [
          {
            "title": "No Adjustments Are Needed for Multiple Comparisons : Epidemiology",
            "url": "https://journals.lww.com/epidem/abstract/1990/01000/no_adjustments_are_needed_for_multiple_comparisons.10.aspx"
          },
          {
            "title": "[PDF] No Adjustments Are Needed for Multiple Comparisons | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/No-Adjustments-Are-Needed-for-Multiple-Comparisons-Rothman/7cdae9ece0e94ad740189e7b328bbf6993b4c8d5"
          },
          {
            "title": "Empirical-Bayes adjustments for multiple comparisons are sometimes useful - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/1912039/"
          },
          {
            "title": "Rothman (1990) No adjustments are needed for multiple comparisons.pdf",
            "url": "https://www.scribd.com/document/321113650/Rothman-1990-No-adjustments-are-needed-for-multiple-comparisons-pdf"
          },
          {
            "title": "No adjustments are needed for multiple comparisons",
            "url": "https://pubmed.ncbi.nlm.nih.gov/2081237/"
          },
          {
            "title": "Rothman, K.J. (1990) No adjustments are needed for multiple comparisons. Epidemiology, 1, 43-46. doi10.1097/00001648-199001000-00010 - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=768985"
          },
          {
            "title": "Dealing with multiple testing: To adjust or not to adjust",
            "url": "https://arxiv.org/pdf/2010.02205"
          },
          {
            "title": "K. J. Rothman, “No Adjustments Are Needed for Multiple Comparisons,” Epidemi-ology, Vol. 1, No. 1, 1990, pp. 43-46. doi10.1097/00001648-199001000-00010 - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=411541"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=No+adjustments+are+needed+for+multiple+comparisons&amp=&author=KJ+Rothman&amp=&publication_year=1990&amp=&journal=Epidemiology&amp=&pages=43-46&amp=&doi=10.1097/00001648-199001000-00010&amp=&pmid=2081237"
          },
          {
            "title": "GraphPad Prism 11 Statistics Guide - When it makes sense to not correct for multiple comparisons",
            "url": "https://www.graphpad.com/guides/prism/latest/statistics/stat_when_to_not_correct_for_2.htm"
          }
        ]
      },
      "I found the paper you're searching for. Kenneth J. Rothman published \"No Adjustments Are Needed for Multiple Comparisons\" in Epidemiology, volume 1, issue 1 in January 1990.\n\nThe paper's main argument is that a policy of not making adjustments for multiple comparisons is preferable because it will lead to fewer errors of interpretation when the data under evaluation are not random numbers but actual observations.\n\nRothman's key critique of adjustment procedures is that reducing the type I error for null associations increases the type II error for those associations that are not null. He argues that the theoretical basis for advocating a routine adjustment for multiple comparisons is the \"universal null hypothesis\" that \"chance\" serves as the first-order explanation for observed phenomena, which he contends undermines empirical research.\n\nThis paper has become highly influential in epidemiology and statistics, and has over 5,500 citations. It remains a key reference point in debates about whether multiple comparison adjustments should be routinely applied."
    ],
    "durationSeconds": 4.871678219999998
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T15:42:00.883Z_

<details><summary>↩ Tool result · `toolu_01QgsYtsxZVZw6JzmcEzuMgr`</summary>

```text
Web search results for query: "Deng 2010 classifying 10000 image categories ECCV"

Links: [{"title":"What does classifying more than 10000 image categories ...","url":"https://collaborate.princeton.edu/en/publications/what-does-classifying-more-than-10000-image-categories-tell-us"},{"title":"What Does Classifying More Than 10,000 Image Categories Tell Us?","url":"http://vision.stanford.edu/documents/DengBergLiFei-Fei_ECCV2010.pdf"},{"title":"What Does Classifying More Than 10, 000 Image Categories Tell Us? | Request PDF","url":"https://www.researchgate.net/publication/221305119_What_Does_Classifying_More_Than_10_000_Image_Categories_Tell_Us"},{"title":"What Does Classifying More Than 10,000 Image Categories Tell Us? | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-15555-0_6"},{"title":"What Does Classifying More Than 10,000 Image Categories ...","url":"http://vision.stanford.edu/pdf/DengBergLiFei-Fei_ECCV2010.pdf"},{"title":"[PDF] What Does Classifying More Than 10, 000 Image Categories Tell Us? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/What-Does-Classifying-More-Than-10,-000-Image-Tell-Deng-Berg/9800e3c3394c569be83379ee2ebe3424e09c2919"},{"title":"AMMAI(Week 15) – What does classifying more than 10,000 image categories tell us? | Mr.pojenlai","url":"https://pojenlai.wordpress.com/2015/06/09/ammaiweek-15-what-does-classifying-more-than-10000-image-categories-tell-us/"},{"title":"What Does Classifying More Than 10, 000 Image Categories Tell Us? - Google Search","url":"https://google.com/search?hl=en&ie=UTF-8&oq=What+Does+Classifying+More+Than+10%2C+000+Image+Categories+Tell+Us%3F&q=What+Does+Classifying+More+Than+10%2C+000+Image+Categories+Tell+Us%3F&sourceid=chrome"},{"title":"What does classifying more than 10,000 image categories tell ...","url":"http://acberg.com/papers/10000_categories_eccv2010.pdf"},{"title":"Large Scale Visual Classification with Many Classes | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-642-39712-7_48"}]

Based on the search results, here's what I found about the Deng 2010 paper:

## Paper Details

The paper "What does classifying more than 10,000 image categories tell us?" was authored by Deng J, Berg AC, Li K, and Fei-Fei L, and was published at the ECCV 2010 (11th European Conference on Computer Vision).

## Key Contribution

The paper presents a study of large scale categorization including a series of challenging experiments on classification with more than 10,000 image classes, which no computer vision algorithm today had been tested at that scale.

## Main Findings

The study found that: a) computational issues become crucial in algorithm design; b) conventional wisdom from a couple of hundred image categories on relative performance of different classifiers does not necessarily hold when the number of categories increases.

## Datasets Used

The paper used several datasets including Rand200 (three datasets each containing 200 randomly selected leaf categories), ImageNet1K, ImageNet7K, and ImageNet10K, as well as Ungulate183, Fungus134, and Vehicle262 containing all leaf nodes that are descendants of particular parent nodes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "9904b712-a53b-4fc8-af66-1f15c35db262",
  "tool_use_result": {
    "query": "Deng 2010 classifying 10000 image categories ECCV",
    "results": [
      {
        "tool_use_id": "srvtoolu_014W6Edd1CvNZgc4Mw5PymTD",
        "content": [
          {
            "title": "What does classifying more than 10000 image categories ...",
            "url": "https://collaborate.princeton.edu/en/publications/what-does-classifying-more-than-10000-image-categories-tell-us"
          },
          {
            "title": "What Does Classifying More Than 10,000 Image Categories Tell Us?",
            "url": "http://vision.stanford.edu/documents/DengBergLiFei-Fei_ECCV2010.pdf"
          },
          {
            "title": "What Does Classifying More Than 10, 000 Image Categories Tell Us? | Request PDF",
            "url": "https://www.researchgate.net/publication/221305119_What_Does_Classifying_More_Than_10_000_Image_Categories_Tell_Us"
          },
          {
            "title": "What Does Classifying More Than 10,000 Image Categories Tell Us? | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-642-15555-0_6"
          },
          {
            "title": "What Does Classifying More Than 10,000 Image Categories ...",
            "url": "http://vision.stanford.edu/pdf/DengBergLiFei-Fei_ECCV2010.pdf"
          },
          {
            "title": "[PDF] What Does Classifying More Than 10, 000 Image Categories Tell Us? | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/What-Does-Classifying-More-Than-10,-000-Image-Tell-Deng-Berg/9800e3c3394c569be83379ee2ebe3424e09c2919"
          },
          {
            "title": "AMMAI(Week 15) – What does classifying more than 10,000 image categories tell us? | Mr.pojenlai",
            "url": "https://pojenlai.wordpress.com/2015/06/09/ammaiweek-15-what-does-classifying-more-than-10000-image-categories-tell-us/"
          },
          {
            "title": "What Does Classifying More Than 10, 000 Image Categories Tell Us? - Google Search",
            "url": "https://google.com/search?hl=en&ie=UTF-8&oq=What+Does+Classifying+More+Than+10%2C+000+Image+Categories+Tell+Us%3F&q=What+Does+Classifying+More+Than+10%2C+000+Image+Categories+Tell+Us%3F&sourceid=chrome"
          },
          {
            "title": "What does classifying more than 10,000 image categories tell ...",
            "url": "http://acberg.com/papers/10000_categories_eccv2010.pdf"
          },
          {
            "title": "Large Scale Visual Classification with Many Classes | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-642-39712-7_48"
          }
        ]
      },
      "Based on the search results, here's what I found about the Deng 2010 paper:\n\n## Paper Details\n\nThe paper \"What does classifying more than 10,000 image categories tell us?\" was authored by Deng J, Berg AC, Li K, and Fei-Fei L, and was published at the ECCV 2010 (11th European Conference on Computer Vision).\n\n## Key Contribution\n\nThe paper presents a study of large scale categorization including a series of challenging experiments on classification with more than 10,000 image classes, which no computer vision algorithm today had been tested at that scale.\n\n## Main Findings\n\nThe study found that: a) computational issues become crucial in algorithm design; b) conventional wisdom from a couple of hundred image categories on relative performance of different classifiers does not necessarily hold when the number of categories increases.\n\n## Datasets Used\n\nThe paper used several datasets including Rand200 (three datasets each containing 200 randomly selected leaf categories), ImageNet1K, ImageNet7K, and ImageNet10K, as well as Ungulate183, Fungus134, and Vehicle262 containing all leaf nodes that are descendants of particular parent nodes."
    ],
    "durationSeconds": 6.328858311
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
All 5 references are confirmed. Let me also note:
1. `haystack-to-needle-2025` — confirmed: Vandemoortele et al. (2025), "From Haystack to Needle: Label Space Reduction for Zero-shot Classification", arXiv:2502.08436. Under review at ICML 2025.
2. `cohen-1988-power` — confirmed: Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge.


3. `lakens-2013-effect-size` — confirmed: Lakens, D. (2013). "Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs". Frontiers in Psychology, 4, 863.
4. `deng-2010-imagenet` — confirmed: Deng, J., Berg, A.C., Li, K., Fei-Fei, L. (2010). "What does classifying more than 10,000 image categories tell us?" ECCV 2010.
5. `rothman-1990` — confirmed: Rothman, K.J. (1990). "No Adjustments Are Needed for Multiple Comparisons". Epidemiology, 1(1), 43-46.

I see that `lost-in-middle-2024` is already in the bibliography, so I don't need to add it. Now I'm mapping out all the changes I need to make across the document — rewriting the abstract, updating citations in the introduction and results, revising the discussion, adding references to related work, and fixing p-value formatting throughout. Let me start by scanning for any p-value inconsistencies across the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "455f1c82-7bc9-4128-a2fb-9202215d5a6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 37_

All 5 references confirmed. `lost-in-middle-2024` already in bib. Now making all edits in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "ae1ea89b-02cc-48d0-b951-f38bd03a3801",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

<details open><summary>🔧 Tool call — Edit · `toolu_017LTLSyYYkLgqZSHwUoDWXk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction, the gap widens substantially (Table~\\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\\approx}\\,2.2$\\,pp accuracy difference; under quartile contrast the gap reaches $-5.3$\\,pp, and batch-level BCS explains up to 53\\% of cross-batch variance. The channels are cleanly separable in RE (TOST equivalence test, $p = 0.003$) but coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers +29.8\\,pp for RE, but confusability-aware grouping yields no significant improvement over random grouping (+1.4\\,pp, $p \\approx 0.19$, n.s.).\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "82393f61-808b-445e-b737-df63465aabfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 39 · 2026-05-16T15:42:34.696Z_

<details><summary>↩ Tool result · `toolu_017LTLSyYYkLgqZSHwUoDWXk`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "d5efcc6c-3ccd-4a8e-bae4-495bf993a13a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "oldString": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction, the gap widens substantially (Table~\\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}",
    "newString": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\\approx}\\,2.2$\\,pp accuracy difference; under quartile contrast the gap reaches $-5.3$\\,pp, and batch-level BCS explains up to 53\\% of cross-batch variance. The channels are cleanly separable in RE (TOST equivalence test, $p = 0.003$) but coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers +29.8\\,pp for RE, but confusability-aware grouping yields no significant improvement over random grouping (+1.4\\,pp, $p \\approx 0.19$, n.s.).\n\\end{abstract}",
    "originalFile": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction, the gap widens substantially (Table~\\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\begin{abstract}",
          "-Training-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.",
          "+Training-free LLM information extraction degrades as schema complexity grows. We present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).",
          " ",
          "-We identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction, the gap widens substantially (Table~\\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).",
          "+We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\\approx}\\,2.2$\\,pp accuracy difference; under quartile contrast the gap reaches $-5.3$\\,pp, and batch-level BCS explains up to 53\\% of cross-batch variance. The channels are cleanly separable in RE (TOST equivalence test, $p = 0.003$) but coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers +29.8\\,pp for RE, but confusability-aware grouping yields no significant improvement over random grouping (+1.4\\,pp, $p \\approx 0.19$, n.s.).",
          " \\end{abstract}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01AzChs5nxZuNAaKWj6JADTe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "(1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp",
  "new_string": "(1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "74c5a6bf-9c9b-4c91-a414-778d05b45452",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 41 · 2026-05-16T15:42:39.343Z_

<details><summary>↩ Tool result · `toolu_01AzChs5nxZuNAaKWj6JADTe`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "d9e8a11d-b429-4f80-a7d5-e0e2728a86b9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "(1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp",
    "newString": "(1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).",
          " ",
          "-Our experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
          "+Our experiments yield five findings: (1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_011t3pChMiXFGx7BAQ84QDai`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "(5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
  "new_string": "(5)~NER decomposition fails due to merge amplification; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing recovering +29.8\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "51ca3be9-7fd0-41d6-b1f5-67bf30c3e6e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 43 · 2026-05-16T15:42:41.699Z_

<details><summary>↩ Tool result · `toolu_011t3pChMiXFGx7BAQ84QDai`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "d4ea35f0-f879-499e-85cf-1c56d97e60ae",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "(5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
    "newString": "(5)~NER decomposition fails due to merge amplification; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing recovering +29.8\\,pp.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).",
          " ",
          "-Our experiments yield five findings: (1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
          "+Our experiments yield five findings: (1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing recovering +29.8\\,pp.",
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01Lxybk7LB2PtDo7yxugDyQx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).",
  "new_string": "    \\item \\textbf{Controlled empirical evidence for two degradation channels.} Through stratified design isolating count from confusability, we show these dimensions predict distinct error types---count predicts recall decline, confusability predicts type substitution---with clean separability in RE and coupling in NER (\\S\\ref{sec:multi_channel})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "70364447-b7a0-4e55-b446-3c1ae827f035",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 45 · 2026-05-16T15:42:45.957Z_

<details><summary>↩ Tool result · `toolu_01Lxybk7LB2PtDo7yxugDyQx`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "230f800a-0770-4266-8a63-2d76210ab249",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).",
    "newString": "    \\item \\textbf{Controlled empirical evidence for two degradation channels.} Through stratified design isolating count from confusability, we show these dimensions predict distinct error types---count predicts recall decline, confusability predicts type substitution---with clean separability in RE and coupling in NER (\\S\\ref{sec:multi_channel}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp; quartile $\\Delta = -5.3$\\,pp)---cleanly separable in RE (TOST $p = 0.003$) but coupled in NER; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing recovering +29.8\\,pp.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " ",
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]",
          "-    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).",
          "+    \\item \\textbf{Controlled empirical evidence for two degradation channels.} Through stratified design isolating count from confusability, we show these dimensions predict distinct error types---count predicts recall decline, confusability predicts type substitution---with clean separability in RE and coupling in NER (\\S\\ref{sec:multi_channel}).",
          "     \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.",
          "     \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).",
          "     \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains."
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_012qbWsZWeLJhvX6i8NnYpoF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise})",
  "new_string": "Conditional pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ unconditional $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}; we note the conditioning inflates this estimate)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "3d59ea3c-3968-41d1-81e6-4ad0c833f113",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 47 · 2026-05-16T15:42:49.305Z_

<details><summary>↩ Tool result · `toolu_012qbWsZWeLJhvX6i8NnYpoF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "5659f691-ab48-42fa-bb24-621e30821e84",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise})",
    "newString": "Conditional pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ unconditional $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}; we note the conditioning inflates this estimate)",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}).\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 7,
        "newStart": 64,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Practical magnitude.}",
          " \\label{sec:practical_magnitude}",
          "-For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).",
          "+For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Conditional pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ unconditional $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}; we note the conditioning inflates this estimate) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).",
          " ",
          " \\paragraph{Cross-model validation.}",
          " The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1)."
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rq9iR3JtzUC56xFz87HfDG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies",
  "new_string": "The pair-level effect is modest (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\\%$) but amplifies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4ae6c827-f91a-4bcb-8eef-dd4723385a02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRdPiCvx2DjC38uG3bSKsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1868,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 52417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 49 · 2026-05-16T15:42:50.963Z_

<details><summary>↩ Tool result · `toolu_01Rq9iR3JtzUC56xFz87HfDG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "f529a7e0-2669-436b-bdef-c56d09ea7253",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies",
    "newString": "The pair-level effect is modest (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\\%$) but amplifies",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).",
          " ",
          " \\paragraph{Why does embedding similarity predict LLM confusion?}",
          "-Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.",
          "+Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.",
          " ",
          " \\paragraph{Schema design implications.}",
          " Since typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition."
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

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Good, 6 edits done. Now I need to:
1. Insert the "Prompt length as mechanism" paragraph in discussion.tex (W10)
2. Replace the Conclusion paragraph in discussion.tex (W1+W9)
3. Add 3 citations to related_work.tex (W12)
4. Add 5 bib entries to references.bib
5. Modify 2 things in main.tex Limitations
6. Fix p-value formats

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "7beaae7f-0109-433a-bd54-206f75b079f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 51_

First batch of edits done. Continuing with remaining edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "88df8c79-e1d2-4541-a99f-f33152aa9c2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_013P8FcFCXcvqbWiESKcV3yM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}",
  "new_string": "The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Prompt length as mechanism.}\nCount-driven degradation (Channel~1) may partly reflect prompt length increase: adding types mechanically lengthens the prompt, and per-type recall (0.586) substantially exceeds single-pass recall (0.368), consistent with lost-in-middle effects \\cite{lost-in-middle-2024}. Disentangling count from prompt length would require fixed-count variable-length experiments, which we leave to future work.\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "bf9661a7-a7a6-40a9-8b30-c0381659701e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 53 · 2026-05-16T15:43:09.821Z_

<details><summary>↩ Tool result · `toolu_013P8FcFCXcvqbWiESKcV3yM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "e9e9835f-7282-4c6f-8722-bded048fe292",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}",
    "newString": "The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Prompt length as mechanism.}\nCount-driven degradation (Channel~1) may partly reflect prompt length increase: adding types mechanically lengthens the prompt, and per-type recall (0.586) substantially exceeds single-pass recall (0.368), consistent with lost-in-middle effects \\cite{lost-in-middle-2024}. Disentangling count from prompt length would require fixed-count variable-length experiments, which we leave to future work.\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 6,
        "newStart": 4,
        "newLines": 9,
        "lines": [
          " \\paragraph{Boundary conditions.}",
          " The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).",
          " ",
          "+\\paragraph{Prompt length as mechanism.}",
          "+Count-driven degradation (Channel~1) may partly reflect prompt length increase: adding types mechanically lengthens the prompt, and per-type recall (0.586) substantially exceeds single-pass recall (0.368), consistent with lost-in-middle effects \\cite{lost-in-middle-2024}. Disentangling count from prompt length would require fixed-count variable-length experiments, which we leave to future work.",
          "+",
          " \\paragraph{Why does embedding similarity predict LLM confusion?}",
          " Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.",
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01TK91b3LNTvQ2cBdnntYKGp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "We presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.",
  "new_string": "We presented controlled evidence that schema-induced degradation in training-free LLM extraction operates through two channels---count-driven recall decline and confusability-driven type confusion. These channels are additively separable in RE (TOST $p = 0.003$) but coupled in NER where boundary and type ambiguity interact; Channel~1 replicates across model scales while Channel~2 shows floor effects on smaller models ($R^2$ up to 0.53 on RE). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schema compositions before deployment. Future work should address non-oracle routing for deployable decomposition and broader model coverage including proprietary APIs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "aa099788-2bff-4a57-a0aa-5f8e240a5c72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 55 · 2026-05-16T15:43:15.935Z_

<details><summary>↩ Tool result · `toolu_01TK91b3LNTvQ2cBdnntYKGp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "2d4ef689-fefe-49ee-ab6f-c2c9b1e24185",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "We presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.",
    "newString": "We presented controlled evidence that schema-induced degradation in training-free LLM extraction operates through two channels---count-driven recall decline and confusability-driven type confusion. These channels are additively separable in RE (TOST $p = 0.003$) but coupled in NER where boundary and type ambiguity interact; Channel~1 replicates across model scales while Channel~2 shows floor effects on smaller models ($R^2$ up to 0.53 on RE). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schema compositions before deployment. Future work should address non-oracle routing for deployable decomposition and broader model coverage including proprietary APIs.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Prompt length as mechanism.}\nCount-driven degradation (Channel~1) may partly reflect prompt length increase: adding types mechanically lengthens the prompt, and per-type recall (0.586) substantially exceeds single-pass recall (0.368), consistent with lost-in-middle effects \\cite{lost-in-middle-2024}. Disentangling count from prompt length would require fixed-count variable-length experiments, which we leave to future work.\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 4,
        "newStart": 24,
        "newLines": 4,
        "lines": [
          " \\section{Conclusion}",
          " \\label{sec:conclusion}",
          " ",
          "-We presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.",
          "+We presented controlled evidence that schema-induced degradation in training-free LLM extraction operates through two channels---count-driven recall decline and confusability-driven type confusion. These channels are additively separable in RE (TOST $p = 0.003$) but coupled in NER where boundary and type ambiguity interact; Channel~1 replicates across model scales while Channel~2 shows floor effects on smaller models ($R^2$ up to 0.53 on RE). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schema compositions before deployment. Future work should address non-oracle routing for deployable decomposition and broader model coverage including proprietary APIs."
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

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rcdu2aCjZ7ptUjKvAkYW2w`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.",
  "new_string": "Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "6bb578dd-9fbd-49f0-b7de-ef61ea4a5fd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 57 · 2026-05-16T15:43:25.016Z_

<details><summary>↩ Tool result · `toolu_01Rcdu2aCjZ7ptUjKvAkYW2w`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "a64c4c0d-a5eb-4788-a0dd-b5cb469f3ec1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.",
    "newString": "Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " Training-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.",
          " ",
          " \\paragraph{Schema complexity in IE.}",
          "-The most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.",
          "+The most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.",
          " ",
          " \\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.",
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

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_014NmA2vEK9uk39LBXzaVQKq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.",
  "new_string": "\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "32d7b9c5-a7a7-49b4-89e1-2ae8ff3bf4d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 59 · 2026-05-16T15:43:29.132Z_

<details><summary>↩ Tool result · `toolu_014NmA2vEK9uk39LBXzaVQKq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4f187567-981a-4ee3-ba17-bed7be436106",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.",
    "newString": "\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.",
          " ",
          "-\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work.",
          "+\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.",
          " ",
          " \\paragraph{Embedding anisotropy.}",
          " Our centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality."
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_018vG5pKU4398GSynD97KB7Y`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.",
  "new_string": "\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "763cef44-6a53-4531-b822-c84f86fe847e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 61 · 2026-05-16T15:43:35.366Z_

<details><summary>↩ Tool result · `toolu_018vG5pKU4398GSynD97KB7Y`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "46f187c0-efba-468a-a2d5-f4a0b42f8fa7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.",
    "newString": "\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\paragraph{Schema complexity in IE.}",
          " The most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.",
          " ",
          "-\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion.",
          "+\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2024ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}.",
          " ",
          " \\paragraph{SCS novelty.} SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.",
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01WLXRQhJhaQdxDhNv8mtg7n`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.",
  "new_string": "\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "88b0a9cf-16fd-4e5a-85ef-6e0979c75a03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 63 · 2026-05-16T15:43:41.460Z_

<details><summary>↩ Tool result · `toolu_01WLXRQhJhaQdxDhNv8mtg7n`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "a72655f1-bf88-44e8-af99-8f311b81870f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.",
    "newString": "\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 49,
        "oldLines": 7,
        "newStart": 49,
        "newLines": 7,
        "lines": [
          " ",
          " \\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.",
          " ",
          "-\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.",
          "+\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).",
          " \\end{enumerate}",
          " ",
          " \\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$."
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

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_015iVhZWFQdL2zxPfdVjbKez`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication.",
  "new_string": "\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, we treat each dataset as a separate test of the same hypothesis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "80d0f992-2d72-411d-bf7a-929ae7e67772",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JawYqrfsPpZyWnArkUeDME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 55645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 65 · 2026-05-16T15:43:44.275Z_

<details><summary>↩ Tool result · `toolu_015iVhZWFQdL2zxPfdVjbKez`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "bf36bf6c-1d83-45dc-845d-66be0168a485",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication.",
    "newString": "\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, we treat each dataset as a separate test of the same hypothesis.",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 52,
        "oldLines": 7,
        "newStart": 52,
        "newLines": 7,
        "lines": [
          " \\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).",
          " \\end{enumerate}",
          " ",
          "-\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.",
          "+\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, we treat each dataset as a separate test of the same hypothesis. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.",
          " ",
          " \\input{checklist}",
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

_source line 66_

Now adding bib entries and fixing p-value formats. Let me first search for all p-value occurrences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "9f20d384-cc9f-45f7-a395-e8c51daaa657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhujQAHKJqMPPb4tHjxzNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 60712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
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

_source line 67_

<details open><summary>🔧 Tool call — Grep · `toolu_01AAHhhigzpuMzW1bxhDww7j`</summary>

```json
{
  "pattern": "p\\s*=\\s*\\.\\d",
  "glob": "*.tex",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4452630d-50d4-42ca-95fd-8d3e8b1edaec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhujQAHKJqMPPb4tHjxzNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 60712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
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

_source line 68 · 2026-05-16T15:43:50.106Z_

<details><summary>↩ Tool result · `toolu_01AAHhhigzpuMzW1bxhDww7j`</summary>

```text
docs/paper/main.tex:158:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "858b7749-e647-4e2a-bc93-8d52f2c4d239",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:158:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01A96kLa8gTqUKKRws77qPJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "offset": 395
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "b9b1e4d7-5990-4628-8e4d-88ccab20c7d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhujQAHKJqMPPb4tHjxzNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 60712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
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

_source line 70 · 2026-05-16T15:43:50.503Z_

<details><summary>↩ Tool result · `toolu_01A96kLa8gTqUKKRws77qPJ5`</summary>

```text
395	    title   = {A Study of Errors in the Output of Large Language Models for Named Entity Recognition},
396	    author  = {Volkanovska, Elena and Padó, Sebastian and Möller, Knud},
397	    journal = {Journal for Language Technology and Computational Linguistics},
398	    volume  = {37},
399	    number  = {1},
400	    year    = {2024},
401	    url     = {https://jlcl.org/article/download/281/263/423},
402	}
403	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "7bf0ef11-0ab6-47aa-906e-d6f7fa3ae6dc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "    title   = {A Study of Errors in the Output of Large Language Models for Named Entity Recognition},\n    author  = {Volkanovska, Elena and Padó, Sebastian and Möller, Knud},\n    journal = {Journal for Language Technology and Computational Linguistics},\n    volume  = {37},\n    number  = {1},\n    year    = {2024},\n    url     = {https://jlcl.org/article/download/281/263/423},\n}\n",
      "numLines": 9,
      "startLine": 395,
      "totalLines": 403
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
The grep found only one match in main.tex line 158. Let me check that specific line. The appendix factorial section has `$p = .008$` and `$p = .0002$` and `$p_{\text{TOST}} = .003$`. Let me read that part of main.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "aea66a90-ee31-42d0-91dc-82109961e457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYG6P9xqtjh7AohrUnkMhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 64255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
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

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01J4DjV1MFgZsmituRCkowkf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 155,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4810f47b-dcfa-4fde-bf52-3b35fd8687d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYG6P9xqtjh7AohrUnkMhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 64255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
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

_source line 73 · 2026-05-16T15:43:57.290Z_

<details><summary>↩ Tool result · `toolu_01J4DjV1MFgZsmituRCkowkf`</summary>

```text
155	\section{Factorial Analysis and Separability Test}
156	\label{sec:appendix_factorial}
157	
158	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = .003$), supporting an additive model of count and confusability effects.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "3c428d52-47d0-4577-b47c-e4d58e0855ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n",
      "numLines": 5,
      "startLine": 155,
      "totalLines": 344
    }
  }
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Found the p-value issues. Line 158 has `$p = .008$`, `$p = .0002$`, and `$p_{\text{TOST}} = .003$`.

Let me also check results.tex line 87 which has `$p_{\text{TOST}} = .003$`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "8107fa8a-210a-4709-9987-ac829bd8ccce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sufr1NPbBQfaQyaCzVcCJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 64829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 75_

Now let me also check results.tex for p-value format issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4c6bce39-bccb-4f98-8a5d-2501bb1681e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sufr1NPbBQfaQyaCzVcCJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 64829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 76_

<details open><summary>🔧 Tool call — Grep · `toolu_01KuwhjUmcmMr5S2q2MHcpcD`</summary>

```json
{
  "pattern": "p.*=\\s*\\.\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "83cca3e0-8c37-4e34-ab22-4bad18e2c94e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sufr1NPbBQfaQyaCzVcCJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 64829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 77 · 2026-05-16T15:44:01.767Z_

<details><summary>↩ Tool result · `toolu_01KuwhjUmcmMr5S2q2MHcpcD`</summary>

```text
87:These results establish two channels: \textbf{Channel~1} (count predicts recall decline) and \textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\,pp, $p_{\text{TOST}} = .003$; Appendix~\ref{sec:appendix_factorial}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "11fbb944-8c14-4448-84d2-002d0012a4a2",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "87:These results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}).",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Grep · `toolu_012x4oBWJCnmWn77hin6kwnA`</summary>

```json
{
  "pattern": "p_\\{\\\\text\\{TOST\\}\\}\\s*=\\s*\\.",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "46a4ecb6-facf-4469-a6f4-341cf70b019e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sufr1NPbBQfaQyaCzVcCJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 64829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 79 · 2026-05-16T15:44:02.735Z_

<details><summary>↩ Tool result · `toolu_012x4oBWJCnmWn77hin6kwnA`</summary>

```text
docs/paper/main.tex:44:\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\text{TOST}} = .003$, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
docs/paper/main.tex:158:[Omitted long matching line]
docs/paper/results.tex:87:These results establish two channels: \textbf{Channel~1} (count predicts recall decline) and \textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\,pp, $p_{\text{TOST}} = .003$; Appendix~\ref{sec:appendix_factorial}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "e28f0dd6-982d-440f-999e-38293dfe412f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:44:\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\ndocs/paper/main.tex:158:[Omitted long matching line]\ndocs/paper/results.tex:87:These results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}).",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 80_

Found all p-value format issues. Now applying all remaining edits in parallel: bib entries, and p-value fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "25399961-43c2-4aa0-9601-9328b69d9513",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hb8JmpMFg23g5t8Cgv8Yej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 65283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 81_

<details open><summary>🔧 Tool call — Edit · `toolu_01U9XfVdfJtBmMpTaxPnSdPs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    url     = {https://jlcl.org/article/download/281/263/423},\n}",
  "new_string": "    url     = {https://jlcl.org/article/download/281/263/423},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@book{cohen-1988-power,\n    title     = {Statistical Power Analysis for the Behavioral Sciences},\n    author    = {Cohen, Jacob},\n    edition   = {2nd},\n    publisher = {Routledge},\n    year      = {1988},\n    doi       = {10.4324/9780203771587},\n}\n\n@article{lakens-2013-effect-size,\n    title   = {Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and {ANOVA}s},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Frontiers in Psychology},\n    volume  = {4},\n    pages   = {863},\n    year    = {2013},\n    doi     = {10.3389/fpsyg.2013.00863},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "2824a593-a5e2-4192-ae0f-065991920a2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hb8JmpMFg23g5t8Cgv8Yej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 65283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 82 · 2026-05-16T15:44:16.084Z_

<details><summary>↩ Tool result · `toolu_01U9XfVdfJtBmMpTaxPnSdPs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4d275ab7-4397-45dd-95db-264fcc106abc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    url     = {https://jlcl.org/article/download/281/263/423},\n}",
    "newString": "    url     = {https://jlcl.org/article/download/281/263/423},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@book{cohen-1988-power,\n    title     = {Statistical Power Analysis for the Behavioral Sciences},\n    author    = {Cohen, Jacob},\n    edition   = {2nd},\n    publisher = {Routledge},\n    year      = {1988},\n    doi       = {10.4324/9780203771587},\n}\n\n@article{lakens-2013-effect-size,\n    title   = {Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and {ANOVA}s},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Frontiers in Psychology},\n    volume  = {4},\n    pages   = {863},\n    year    = {2013},\n    doi     = {10.3389/fpsyg.2013.00863},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}",
    "originalFile": "% References for Schema-DAG-Extraction\n% Generated: 2026-05-15\n% Sources: literature_map.yaml + references_survey.md\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@article{parse-2025,\n    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    journal = {arXiv preprint arXiv:2510.08623},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.08623},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2507.18546},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.14710},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n@inproceedings{gao-repr-degen-2019,\n    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},\n    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1907.12009},\n}\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n@inproceedings{llm-calibration-survey-2024,\n    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.366/},\n}\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and others},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@article{sclar-sensitivity-2024,\n    title   = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author  = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {Generating Structured Outputs from Language Models: Benchmark and Studies},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Srinivas, Sber and Guber, Raghav and Nakhost, Mehran},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{volkanovska2024ner,\n    title   = {A Study of Errors in the Output of Large Language Models for Named Entity Recognition},\n    author  = {Volkanovska, Elena and Padó, Sebastian and Möller, Knud},\n    journal = {Journal for Language Technology and Computational Linguistics},\n    volume  = {37},\n    number  = {1},\n    year    = {2024},\n    url     = {https://jlcl.org/article/download/281/263/423},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 400,
        "oldLines": 3,
        "newStart": 400,
        "newLines": 50,
        "lines": [
          "     year    = {2024},",
          "     url     = {https://jlcl.org/article/download/281/263/423},",
          " }",
          "+",
          "+@article{haystack-to-needle-2025,",
          "+    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},",
          "+    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},",
          "+    journal = {arXiv preprint arXiv:2502.08436},",
          "+    year    = {2025},",
          "+    url     = {https://arxiv.org/abs/2502.08436},",
          "+}",
          "+",
          "+@book{cohen-1988-power,",
          "+    title     = {Statistical Power Analysis for the Behavioral Sciences},",
          "+    author    = {Cohen, Jacob},",
          "+    edition   = {2nd},",
          "+    publisher = {Routledge},",
          "+    year      = {1988},",
          "+    doi       = {10.4324/9780203771587},",
          "+}",
          "+",
          "+@article{lakens-2013-effect-size,",
          "+    title   = {Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and {ANOVA}s},",
          "+    author  = {Lakens, Dani{\\\"e}l},",
          "+    journal = {Frontiers in Psychology},",
          "+    volume  = {4},",
          "+    pages   = {863},",
          "+    year    = {2013},",
          "+    doi     = {10.3389/fpsyg.2013.00863},",
          "+}",
          "+",
          "+@inproceedings{deng-2010-imagenet,",
          "+    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},",
          "+    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},",
          "+    booktitle = {Proceedings of the 11th European Conference on Computer Vision},",
          "+    pages     = {71--84},",
          "+    year      = {2010},",
          "+    doi       = {10.1007/978-3-642-15555-0\\_6},",
          "+}",
          "+",
          "+@article{rothman-1990,",
          "+    title   = {No Adjustments Are Needed for Multiple Comparisons},",
          "+    author  = {Rothman, Kenneth J.},",
          "+    journal = {Epidemiology},",
          "+    volume  = {1},",
          "+    number  = {1},",
          "+    pages   = {43--46},",
          "+    year    = {1990},",
          "+    doi     = {10.1097/00001648-199001000-00010},",
          "+}"
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

_source line 83_

<details open><summary>🔧 Tool call — Edit · `toolu_01THCbjLUK1p6fg1hZqQpUTQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "$p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}",
  "new_string": "$p_{\\text{TOST}} = 0.003$; Appendix~\\ref{sec:appendix_factorial}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "b4f27e9d-c47d-4bf1-90d5-15c3bcf2f23f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hb8JmpMFg23g5t8Cgv8Yej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 65283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 84 · 2026-05-16T15:44:17.372Z_

<details><summary>↩ Tool result · `toolu_01THCbjLUK1p6fg1hZqQpUTQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "d9d39fac-8235-4037-9117-ec9b41fd70ac",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "$p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}",
    "newString": "$p_{\\text{TOST}} = 0.003$; Appendix~\\ref{sec:appendix_factorial}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Conditional pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ unconditional $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}; we note the conditioning inflates this estimate) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}).\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 7,
        "lines": [
          " ",
          " Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.",
          " ",
          "-These results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = .003$; Appendix~\\ref{sec:appendix_factorial}).",
          "+These results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact. A FewRel factorial with TOST equivalence testing formally confirms additive separability (interaction = 0.47\\,pp, $p_{\\text{TOST}} = 0.003$; Appendix~\\ref{sec:appendix_factorial}).",
          " ",
          " \\subsection{Centrality Confound on Homogeneous Schemas}",
          " \\label{sec:centrality_confound}"
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

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_01312WgB1NDCqgjvXrTiHbEm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "$p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool",
  "new_string": "$p_{\\text{TOST}} = 0.003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "23bbdc69-80cc-4439-a538-aaa9ebdac24f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hb8JmpMFg23g5t8Cgv8Yej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 65283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 86 · 2026-05-16T15:44:19.323Z_

<details><summary>↩ Tool result · `toolu_01312WgB1NDCqgjvXrTiHbEm`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "2c57bead-9eb4-4b0a-a8f9-09ff39fe670a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "$p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool",
    "newString": "$p_{\\text{TOST}} = 0.003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, we treat each dataset as a separate test of the same hypothesis. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " \\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.",
          " ",
          "-\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = .003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.",
          "+\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = 0.003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.",
          " ",
          " \\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.",
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

_source line 87_

<details open><summary>🔧 Tool call — Edit · `toolu_01EyDuY2v3Lu9bBMz6o4kMnh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "count: $p = .008$; BCS: $p = .0002$",
  "new_string": "count: $p = 0.008$; BCS: $p = 0.0002$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "07acd839-bfc6-4b54-a398-58b5fb1547db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hb8JmpMFg23g5t8Cgv8Yej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 65283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 88 · 2026-05-16T15:44:20.252Z_

<details><summary>↩ Tool result · `toolu_01EyDuY2v3Lu9bBMz6o4kMnh`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "c7149d12-20d4-4c2d-aff8-7fd2ec467102",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "count: $p = .008$; BCS: $p = .0002$",
    "newString": "count: $p = 0.008$; BCS: $p = 0.0002$",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = 0.003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, we treat each dataset as a separate test of the same hypothesis. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 155,
        "oldLines": 7,
        "newStart": 155,
        "newLines": 7,
        "lines": [
          " \\section{Factorial Analysis and Separability Test}",
          " \\label{sec:appendix_factorial}",
          " ",
          "-To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = .008$; BCS: $p = .0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.",
          "+To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.",
          " ",
          " A separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.",
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

_source line 89_

<details open><summary>🔧 Tool call — Edit · `toolu_01KbKrhEXGvPF3XPtduMGsCJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "$p_{\\text{TOST}} = .003$), supporting an additive model",
  "new_string": "$p_{\\text{TOST}} = 0.003$), supporting an additive model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "3597cd39-a44f-4976-a57d-d7bb06dd7c31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hb8JmpMFg23g5t8Cgv8Yej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 65283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 90 · 2026-05-16T15:44:21.557Z_

<details><summary>↩ Tool result · `toolu_01KbKrhEXGvPF3XPtduMGsCJ`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "53aa6677-24e8-42ba-a743-01ce27ca254f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "$p_{\\text{TOST}} = .003$), supporting an additive model",
    "newString": "$p_{\\text{TOST}} = 0.003$), supporting an additive model",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\\text{TOST}} = 0.003$, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Following the argument that independent replications do not require family-wise correction \\citep{rothman-1990}, we treat each dataset as a separate test of the same hypothesis. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.\n\nA separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 155,
        "oldLines": 7,
        "newStart": 155,
        "newLines": 7,
        "lines": [
          " \\section{Factorial Analysis and Separability Test}",
          " \\label{sec:appendix_factorial}",
          " ",
          "-To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = .003$), supporting an additive model of count and confusability effects.",
          "+To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting an additive model of count and confusability effects.",
          " ",
          " A separate within-dataset $2 \\times 2$ factorial on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) did not reach equivalence ($p_{\\text{TOST}} = 0.56$), likely due to limited power from fewer count levels and narrower BCS contrast. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.",
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

_source line 91_

All edits complete. Let me do a final check for any remaining p-value format issues, then compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "2525f9c3-8f64-45f6-8c66-b7e243473365",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxB2PqisovANmVLBswHZoX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 66132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1991
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

_source line 92_

<details open><summary>🔧 Tool call — Grep · `toolu_01HB2zx3KWWdHM9QASFVdPPh`</summary>

```json
{
  "pattern": "\\$p[^)]*=\\s*\\.\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4b57b99a-4663-4a97-81fc-319b439f2d91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxB2PqisovANmVLBswHZoX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 66132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1991
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

_source line 93 · 2026-05-16T15:44:25.773Z_

<details><summary>↩ Tool result · `toolu_01HB2zx3KWWdHM9QASFVdPPh`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "7bbbeb21-bfff-4056-8655-6fde325be20f",
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

_source line 94_

<details open><summary>🔧 Tool call — Grep · `toolu_016u6k9CCRmxJtAC4WJK1Jem`</summary>

```json
{
  "pattern": "p\\s*=\\s*\\.\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "eab1d755-f0a6-4b1c-9ec2-9dc868ef0caa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxB2PqisovANmVLBswHZoX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 66132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1991
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

_source line 95 · 2026-05-16T15:44:26.565Z_

<details><summary>↩ Tool result · `toolu_016u6k9CCRmxJtAC4WJK1Jem`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "a3a17e40-f8b3-4e13-a31c-276bd45f4162",
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

_source line 96_

All p-value formats fixed. Compiling the PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "6f98e060-97f9-4c9a-8214-f9814cdc2449",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MCmLaiXQ9KWFANYwSfatUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 68123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_013fzim4kWPuvTY8Zmj4DU6u`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX PDF",
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "60abbfc3-e064-4a5e-bd52-2296c07f3f20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MCmLaiXQ9KWFANYwSfatUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 68123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "byuyqydzj",
  "tool_use_id": "toolu_013fzim4kWPuvTY8Zmj4DU6u",
  "description": "Compile LaTeX PDF",
  "task_type": "local_bash",
  "uuid": "8009809d-de0f-4b94-80db-ae21e3a6b076",
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651"
}
```

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "byuyqydzj",
  "tool_use_id": "toolu_013fzim4kWPuvTY8Zmj4DU6u",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX PDF",
  "uuid": "5ebd9222-0e58-4eb1-8435-643bc5f3729a",
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651"
}
```

---

### Tool result

_source line 100 · 2026-05-16T15:44:36.592Z_

<details><summary>↩ Tool result · `toolu_013fzim4kWPuvTY8Zmj4DU6u`</summary>

```text
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (19 pages, 422161 bytes).
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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "683a27e4-b47c-4103-b238-0f83d043c17b",
  "tool_use_result": {
    "stdout": "1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (19 pages, 422161 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 101_

<details><summary>Logged reasoning block</summary>

```text
Compiled successfully, 19 pages. But I need to check if there are any warnings about citations and verify the Conclusion ends on p8. Let me check the log for warnings and also check where the Conclusion is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "30649f8e-c2d2-40e7-8cdc-607ec9086a6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeWUzyEbcS48rimazV59JS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 68492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 102_

Compiled successfully. Let me check for citation warnings and verify Conclusion position.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "708ad1b8-6d99-44d6-acc2-1fd7dc17e006",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeWUzyEbcS48rimazV59JS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 68492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_017YcXEwFkYnsMqXW6V9ZFku`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -i \"undefined\\|warning.*cit\" main.log | head -20",
  "description": "Check for undefined citation warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "88a608fa-5377-4fb2-bdfb-b09249d23bb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeWUzyEbcS48rimazV59JS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 68492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 104 · 2026-05-16T15:44:42.191Z_

<details><summary>↩ Tool result · `toolu_017YcXEwFkYnsMqXW6V9ZFku`</summary>

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
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "e4a0ea03-13e9-420a-b49d-5c3cea9fb3f6",
  "tool_use_result": {
    "stdout": "",
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

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_015yv6AnApYTjnCj1KpzMy6w`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -i \"rerun\\|citation.*undefined\" main.log | head -10",
  "description": "Check if rerun needed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "be02d203-2035-41c6-9884-1b4a4406c7a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeWUzyEbcS48rimazV59JS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 68492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 106 · 2026-05-16T15:44:43.089Z_

<details><summary>↩ Tool result · `toolu_015yv6AnApYTjnCj1KpzMy6w`</summary>

```text
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
Package uniquecounter Info: New unique counter `rerunfilecheck' on input line 2
Package rerunfilecheck Info: File `main.out' has not changed.
(rerunfilecheck)             Checksum: CB6EC27A8173A945FEBD78BFC62C5BC3;6703.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "d40a2ccc-02a5-486c-ad8f-59e12db4b087",
  "tool_use_result": {
    "stdout": "(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\nPackage: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)\nPackage uniquecounter Info: New unique counter `rerunfilecheck' on input line 2\nPackage rerunfilecheck Info: File `main.out' has not changed.\n(rerunfilecheck)             Checksum: CB6EC27A8173A945FEBD78BFC62C5BC3;6703.",
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

_source line 107_

No undefined citations. Let me check where the Conclusion ends relative to page 8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "94fd3226-6654-44b4-a1fd-d184a0cce128",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrkJ9o4RyJ6Uz4jkJYujDm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 69521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01J35nycZBfvNboHuqmTuNK6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\n')\npage = 0\nfor i, line in enumerate(lines):\n    if '\\x0c' in line:\n        page += 1\n    if 'Conclusion' in line and page <= 10:\n        print(f'Page {page}: {line.strip()[:80]}')\n    if 'Limitations' in line and page <= 10:\n        print(f'Page {page}: {line.strip()[:80]}')\n    if 'Future work should' in line:\n        print(f'Page {page}: {line.strip()[:80]}')\n    if 'proprietary APIs' in line:\n        print(f'Page {page}: {line.strip()[:80]}')\n\"",
  "description": "Check Conclusion and Limitations page positions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "e0cbb59b-977c-4bd9-84c9-c809e953515d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrkJ9o4RyJ6Uz4jkJYujDm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 69521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

_source line 109 · 2026-05-16T15:44:49.797Z_

<details><summary>↩ Tool result · `toolu_01J35nycZBfvNboHuqmTuNK6`</summary>

```text
Page 5: 459   on 8B NER (Limitations, item 1).
Page 7: 642   leave to future work.                                           7   Conclu
Page 8: 704   before deployment. Future work should address
Page 8: 708   Limitations
Page 8: 727      pendix C), and cross-pool slope consistency                   Yes. The
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "4457d1b7-202f-4f88-a280-365bc7c8d764",
  "tool_use_result": {
    "stdout": "Page 5: 459   on 8B NER (Limitations, item 1).\nPage 7: 642   leave to future work.                                           7   Conclu\nPage 8: 704   before deployment. Future work should address\nPage 8: 708   Limitations\nPage 8: 727      pendix C), and cross-pool slope consistency                   Yes. The",
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

_source line 110_

Conclusion header starts on page 7 and ends on page 8. Limitations starts on page 8. The body (Introduction→Conclusion) fits within 8 pages.

Let me get the git diff stat.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "a1ec2c1a-ba5f-475f-bbcc-fa8911f37ed1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnCajQU7pf1cbeNYpiLkR3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 70036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 111_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qk4Qn2uyRLDHeW1vDDdNqY`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction && git diff --stat docs/paper/",
  "description": "Show diff stats for paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "bd0ed5ca-1d4d-454c-86e5-af319c6da2db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnCajQU7pf1cbeNYpiLkR3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 70036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 112 · 2026-05-16T15:44:53.856Z_

<details><summary>↩ Tool result · reported error · `toolu_01Qk4Qn2uyRLDHeW1vDDdNqY`</summary>

```text
Exit code 129
warning: Not a git repository. Use --no-index to compare two paths outside a working tree
usage: git diff --no-index [&lt;options>] &lt;path> &lt;path> [&lt;pathspec>...]

Diff output format options
    -p, --patch           generate patch
    -s, --no-patch        suppress diff output
    -u                    generate patch
    -U, --unified[=&lt;n>]   generate diffs with &lt;n> lines context
    -W, --[no-]function-context
                          generate diffs with &lt;n> lines context
    --raw                 generate the diff in raw format
    --patch-with-raw      synonym for '-p --raw'
    --patch-with-stat     synonym for '-p --stat'
    --numstat             machine friendly --stat
    --shortstat           output only the last line of --stat
    -X, --dirstat[=&lt;param1>,&lt;param2>...]
                          output the distribution of relative amount of changes for each sub-directory
    --cumulative          synonym for --dirstat=cumulative
    --dirstat-by-file[=&lt;param1>,&lt;param2>...]
                          synonym for --dirstat=files,&lt;param1>,&lt;param2>...
    --check               warn if changes introduce conflict markers or whitespace errors
    --summary             condensed summary such as creations, renames and mode changes
    --name-only           show only names of changed files
    --name-status         show only names and status of changed files
    --stat[=&lt;width>[,&lt;name-width>[,&lt;count>]]]
                          generate diffstat
    --stat-width &lt;width>  generate diffstat with a given width
    --stat-name-width &lt;width>
                          generate diffstat with a given name width
    --stat-graph-width &lt;width>
                          generate diffstat with a given graph width
    --stat-count &lt;count>  generate diffstat with limited lines
    --[no-]compact-summary
                          generate compact summary in diffstat
    --binary              output a binary diff that can be applied
    --[no-]full-index     show full pre- and post-image object names on the "index" lines
    --[no-]color[=&lt;when>] show colored diff
    --ws-error-highlight &lt;kind>
                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff
    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat
    --[no-]abbrev[=&lt;n>]   use &lt;n> digits to display object names
    --src-prefix &lt;prefix> show the given source prefix instead of "a/"
    --dst-prefix &lt;prefix> show the given destination prefix instead of "b/"
    --line-prefix &lt;prefix>
                          prepend an additional prefix to every line of output
    --no-prefix           do not show any source or destination prefix
    --default-prefix      use default prefixes a/ and b/
    --inter-hunk-context &lt;n>
                          show context between diff hunks up to the specified number of lines
    --output-indicator-new &lt;char>
                          specify the character to indicate a new line instead of '+'
    --output-indicator-old &lt;char>
                          specify the character to indicate an old line instead of '-'
    --output-indicator-context &lt;char>
                          specify the character to indicate a context instead of ' '

Diff rename options
    -B, --break-rewrites[=&lt;n>[/&lt;m>]]
                          break complete rewrite changes into pairs of delete and create
    -M, --find-renames[=&lt;n>]
                          detect renames
    -D, --irreversible-delete
                          omit the preimage for deletes
    -C, --find-copies[=&lt;n>]
                          detect copies
    --[no-]find-copies-harder
                          use unmodified files as source to find copies
    --no-renames          disable rename detection
    --[no-]rename-empty   use empty blobs as rename source
    --[no-]follow         continue listing the history of a file beyond renames
    -l &lt;n>                prevent rename/copy detection if the number of rename/copy targets exceeds given limit

Diff algorithm options
    --minimal             produce the smallest possible diff
    -w, --ignore-all-space
                          ignore whitespace when comparing lines
    -b, --ignore-space-change
                          ignore changes in amount of whitespace
    --ignore-space-at-eol ignore changes in whitespace at EOL
    --ignore-cr-at-eol    ignore carrier-return at the end of line
    --ignore-blank-lines  ignore changes whose lines are all blank
    -I, --[no-]ignore-matching-lines &lt;regex>
                          ignore changes whose all lines match &lt;regex>
    --[no-]indent-heuristic
                          heuristic to shift diff hunk boundaries for easy reading
    --patience            generate diff using the "patience diff" algorithm
    --histogram           generate diff using the "histogram diff" algorithm
    --diff-algorithm &lt;algorithm>
                          choose a diff algorithm
    --anchored &lt;text>     generate diff using the "anchored diff" algorithm
    --word-diff[=&lt;mode>]  show word diff, using &lt;mode> to delimit changed words
    --word-diff-regex &lt;regex>
                          use &lt;regex> to decide what a word is
    --color-words[=&lt;regex>]
                          equivalent to --word-diff=color --word-diff-regex=&lt;regex>
    --[no-]color-moved[=&lt;mode>]
                          moved lines of code are colored differently
    --[no-]color-moved-ws &lt;mode>
                          how white spaces are ignored in --color-moved

Other diff options
    --[no-]relative[=&lt;prefix>]
                          when run from subdir, exclude changes outside and show relative paths
    -a, --[no-]text       treat all files as text
    -R                    swap two inputs, reverse the diff
    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise
    --[no-]quiet          disable all output of the program
    --[no-]ext-diff       allow an external diff helper to be executed
    --[no-]textconv       run external text conversion filters when comparing binary files
    --ignore-submodules[=&lt;when>]
                          ignore changes to submodules in the diff generation
    --submodule[=&lt;format>]
                          specify how differences in submodules are shown
    --ita-invisible-in-index
                          hide 'git add -N' entries from the index
    --ita-visible-in-index
                          treat 'git add -N' entries as real in the index
    -S &lt;string>           look for differences that change the number of occurrences of the specified string
    -G &lt;regex>            look for differences that change the number of occurrences of the specified regex
    --pickaxe-all         show all changes in the changeset with -S or -G
    --pickaxe-regex       treat &lt;string> in -S as extended POSIX regular expression
    -O &lt;file>             control the order in which files appear in the output
    --rotate-to &lt;path>    show the change in the specified path first
    --skip-to &lt;path>      skip the output to the specified path
    --find-object &lt;object-id>
                          look for differences that change the number of occurrences of the specified object
    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]
                          select files by diff type
    --max-depth &lt;depth>   maximum tree depth to recurse
    --output &lt;file>       output to a specific file
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "0c1bb609-09ce-429a-908f-3a2b45e6a452",
  "tool_use_result": "Error: Exit code 129\nwarning: Not a git repository. Use --no-index to compare two paths outside a working tree\nusage: git diff --no-index [&lt;options>] &lt;path> &lt;path> [&lt;pathspec>...]\n\nDiff output format options\n    -p, --patch           generate patch\n    -s, --no-patch        suppress diff output\n    -u                    generate patch\n    -U, --unified[=&lt;n>]   generate diffs with &lt;n> lines context\n    -W, --[no-]function-context\n                          generate diffs with &lt;n> lines context\n    --raw                 generate the diff in raw format\n    --patch-with-raw      synonym for '-p --raw'\n    --patch-with-stat     synonym for '-p --stat'\n    --numstat             machine friendly --stat\n    --shortstat           output only the last line of --stat\n    -X, --dirstat[=&lt;param1>,&lt;param2>...]\n                          output the distribution of relative amount of changes for each sub-directory\n    --cumulative          synonym for --dirstat=cumulative\n    --dirstat-by-file[=&lt;param1>,&lt;param2>...]\n                          synonym for --dirstat=files,&lt;param1>,&lt;param2>...\n    --check               warn if changes introduce conflict markers or whitespace errors\n    --summary             condensed summary such as creations, renames and mode changes\n    --name-only           show only names of changed files\n    --name-status         show only names and status of changed files\n    --stat[=&lt;width>[,&lt;name-width>[,&lt;count>]]]\n                          generate diffstat\n    --stat-width &lt;width>  generate diffstat with a given width\n    --stat-name-width &lt;width>\n                          generate diffstat with a given name width\n    --stat-graph-width &lt;width>\n                          generate diffstat with a given graph width\n    --stat-count &lt;count>  generate diffstat with limited lines\n    --[no-]compact-summary\n                          generate compact summary in diffstat\n    --binary              output a binary diff that can be applied\n    --[no-]full-index     show full pre- and post-image object names on the \"index\" lines\n    --[no-]color[=&lt;when>] show colored diff\n    --ws-error-highlight &lt;kind>\n                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff\n    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat\n    --[no-]abbrev[=&lt;n>]   use &lt;n> digits to display object names\n    --src-prefix &lt;prefix> show the given source prefix instead of \"a/\"\n    --dst-prefix &lt;prefix> show the given destination prefix instead of \"b/\"\n    --line-prefix &lt;prefix>\n                          prepend an additional prefix to every line of output\n    --no-prefix           do not show any source or destination prefix\n    --default-prefix      use default prefixes a/ and b/\n    --inter-hunk-context &lt;n>\n                          show context between diff hunks up to the specified number of lines\n    --output-indicator-new &lt;char>\n                          specify the character to indicate a new line instead of '+'\n    --output-indicator-old &lt;char>\n                          specify the character to indicate an old line instead of '-'\n    --output-indicator-context &lt;char>\n                          specify the character to indicate a context instead of ' '\n\nDiff rename options\n    -B, --break-rewrites[=&lt;n>[/&lt;m>]]\n                          break complete rewrite changes into pairs of delete and create\n    -M, --find-renames[=&lt;n>]\n                          detect renames\n    -D, --irreversible-delete\n                          omit the preimage for deletes\n    -C, --find-copies[=&lt;n>]\n                          detect copies\n    --[no-]find-copies-harder\n                          use unmodified files as source to find copies\n    --no-renames          disable rename detection\n    --[no-]rename-empty   use empty blobs as rename source\n    --[no-]follow         continue listing the history of a file beyond renames\n    -l &lt;n>                prevent rename/copy detection if the number of rename/copy targets exceeds given limit\n\nDiff algorithm options\n    --minimal             produce the smallest possible diff\n    -w, --ignore-all-space\n                          ignore whitespace when comparing lines\n    -b, --ignore-space-change\n                          ignore changes in amount of whitespace\n    --ignore-space-at-eol ignore changes in whitespace at EOL\n    --ignore-cr-at-eol    ignore carrier-return at the end of line\n    --ignore-blank-lines  ignore changes whose lines are all blank\n    -I, --[no-]ignore-matching-lines &lt;regex>\n                          ignore changes whose all lines match &lt;regex>\n    --[no-]indent-heuristic\n                          heuristic to shift diff hunk boundaries for easy reading\n    --patience            generate diff using the \"patience diff\" algorithm\n    --histogram           generate diff using the \"histogram diff\" algorithm\n    --diff-algorithm &lt;algorithm>\n                          choose a diff algorithm\n    --anchored &lt;text>     generate diff using the \"anchored diff\" algorithm\n    --word-diff[=&lt;mode>]  show word diff, using &lt;mode> to delimit changed words\n    --word-diff-regex &lt;regex>\n                          use &lt;regex> to decide what a word is\n    --color-words[=&lt;regex>]\n                          equivalent to --word-diff=color --word-diff-regex=&lt;regex>\n    --[no-]color-moved[=&lt;mode>]\n                          moved lines of code are colored differently\n    --[no-]color-moved-ws &lt;mode>\n                          how white spaces are ignored in --color-moved\n\nOther diff options\n    --[no-]relative[=&lt;prefix>]\n                          when run from subdir, exclude changes outside and show relative paths\n    -a, --[no-]text       treat all files as text\n    -R                    swap two inputs, reverse the diff\n    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise\n    --[no-]quiet          disable all output of the program\n    --[no-]ext-diff       allow an external diff helper to be executed\n    --[no-]textconv       run external text conversion filters when comparing binary files\n    --ignore-submodules[=&lt;when>]\n                          ignore changes to submodules in the diff generation\n    --submodule[=&lt;format>]\n                          specify how differences in submodules are shown\n    --ita-invisible-in-index\n                          hide 'git add -N' entries from the index\n    --ita-visible-in-index\n                          treat 'git add -N' entries as real in the index\n    -S &lt;string>           look for differences that change the number of occurrences of the specified string\n    -G &lt;regex>            look for differences that change the number of occurrences of the specified regex\n    --pickaxe-all         show all changes in the changeset with -S or -G\n    --pickaxe-regex       treat &lt;string> in -S as extended POSIX regular expression\n    -O &lt;file>             control the order in which files appear in the output\n    --rotate-to &lt;path>    show the change in the specified path first\n    --skip-to &lt;path>      skip the output to the specified path\n    --find-object &lt;object-id>\n                          look for differences that change the number of occurrences of the specified object\n    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]\n                          select files by diff type\n    --max-depth &lt;depth>   maximum tree depth to recurse\n    --output &lt;file>       output to a specific file"
}
```

</details>

---

### Assistant

_source line 113_

<details><summary>Logged reasoning block</summary>

```text
Not a git repo. Let me just provide a summary of changes instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "41f5e444-ba4d-461c-96b8-e37c8488f32b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjMoYg9Xezim9yLmm5Vadp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2056,
      "cache_read_input_tokens": 70588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2056
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

_source line 114_

Not a git repo — no diff stat available. Here's the completion report:

---

## 产出报告

### 修改完成状态

| # | 项目 | 文件 | 状态 |
|---|------|------|------|
| 1 | W1 — Abstract 重写 | abstract.tex | ✓ |
| 2 | W2 — Introduction Finding (1) | introduction.tex | ✓ |
| 2 | W2 — Introduction Finding (5) | introduction.tex | ✓ |
| 2 | W2 — Introduction Contribution 1 | introduction.tex | ✓ |
| 3 | W5 — Results practical magnitude | results.tex | ✓ |
| 4 | W5 — Discussion R² qualifier | discussion.tex | ✓ |
| 4 | W10 — Prompt length paragraph | discussion.tex | ✓ |
| 4 | W1+W9 — Conclusion 重写 | discussion.tex | ✓ |
| 5 | W12 — Related work 3 citations | related_work.tex | ✓ |
| 6 | Bib entries (5 new) | references.bib | ✓ |
| 7 | W8 — Limitations #7 contamination | main.tex | ✓ |
| 7 | W13 — Multiple comparisons + cite | main.tex | ✓ |
| 8 | W14 — p-value 格式统一 | results.tex, main.tex (×3) | ✓ |

### 引用核实结果

| Key | 核实结果 |
|-----|---------|
| `haystack-to-needle-2025` | ✓ Vandemoortele et al., arXiv:2502.08436 |
| `cohen-1988-power` | ✓ Cohen (1988), Routledge, 2nd ed. |
| `lakens-2013-effect-size` | ✓ Lakens (2013), Frontiers in Psychology 4:863 |
| `deng-2010-imagenet` | ✓ Deng et al. (2010), ECCV |
| `rothman-1990` | ✓ Rothman (1990), Epidemiology 1(1):43-46 |
| `lost-in-middle-2024` | ✓ 已存在于 bib |

### 编译 & 页数

- 编译：无错误，无 undefined citation 警告
- 总页数：19（含附录）
- Conclusion 结束位置：**page 8**（正文 ≤ 8 页约束满足）
- Limitations 起始位置：page 8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "uuid": "da6779ec-354f-49df-bfbd-844e14e78077",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjMoYg9Xezim9yLmm5Vadp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2056,
      "cache_read_input_tokens": 70588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2056
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

_source line 115_

Not a git repo — no diff stat available. Here's the completion report:

---

## 产出报告

### 修改完成状态

| # | 项目 | 文件 | 状态 |
|---|------|------|------|
| 1 | W1 — Abstract 重写 | abstract.tex | ✓ |
| 2 | W2 — Introduction Finding (1) | introduction.tex | ✓ |
| 2 | W2 — Introduction Finding (5) | introduction.tex | ✓ |
| 2 | W2 — Introduction Contribution 1 | introduction.tex | ✓ |
| 3 | W5 — Results practical magnitude | results.tex | ✓ |
| 4 | W5 — Discussion R² qualifier | discussion.tex | ✓ |
| 4 | W10 — Prompt length paragraph | discussion.tex | ✓ |
| 4 | W1+W9 — Conclusion 重写 | discussion.tex | ✓ |
| 5 | W12 — Related work 3 citations | related_work.tex | ✓ |
| 6 | Bib entries (5 new) | references.bib | ✓ |
| 7 | W8 — Limitations #7 contamination | main.tex | ✓ |
| 7 | W13 — Multiple comparisons + cite | main.tex | ✓ |
| 8 | W14 — p-value 格式统一 | results.tex, main.tex (×3) | ✓ |

### 引用核实结果

| Key | 核实结果 |
|-----|---------|
| `haystack-to-needle-2025` | ✓ Vandemoortele et al., arXiv:2502.08436 |
| `cohen-1988-power` | ✓ Cohen (1988), Routledge, 2nd ed. |
| `lakens-2013-effect-size` | ✓ Lakens (2013), Frontiers in Psychology 4:863 |
| `deng-2010-imagenet` | ✓ Deng et al. (2010), ECCV |
| `rothman-1990` | ✓ Rothman (1990), Epidemiology 1(1):43-46 |
| `lost-in-middle-2024` | ✓ 已存在于 bib |

### 编译 & 页数

- 编译：无错误，无 undefined citation 警告
- 总页数：19（含附录）
- Conclusion 结束位置：**page 8**（正文 ≤ 8 页约束满足）
- Limitations 起始位置：page 8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 215357,
  "duration_api_ms": 232114,
  "num_turns": 44,
  "stop_reason": "end_turn",
  "session_id": "1389c552-ad3e-4c91-a267-9445a451c651",
  "total_cost_usd": 1.2742822500000002,
  "usage": {
    "input_tokens": 9587,
    "cache_creation_input_tokens": 60803,
    "cache_read_input_tokens": 857779,
    "output_tokens": 11201,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 60803,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 746,
        "cache_read_input_tokens": 70588,
        "cache_creation_input_tokens": 2056,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2056
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 77524,
      "outputTokens": 1978,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.137414,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9587,
      "outputTokens": 11201,
      "cacheReadInputTokens": 857779,
      "cacheCreationInputTokens": 60803,
      "webSearchRequests": 0,
      "costUSD": 1.13686825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a7dcbfc7-230d-4937-b40c-4bbca5c7fa35"
}
```

</details>

---
