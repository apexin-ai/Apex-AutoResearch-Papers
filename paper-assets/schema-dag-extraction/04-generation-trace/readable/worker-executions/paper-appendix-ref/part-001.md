# paper appendix ref  — Part 1 of 2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

[Transcript overview](../paper-appendix-ref.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/34/3438a37bcd4db9c61a9e.json)

## Before a recorded user message

## Before a recorded user message

91 recorded events


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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
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
  "uuid": "bab4abbd-56bf-4089-bef8-167e253c1628",
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
    "resetsAt": 1779432600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fa77a20c-258c-43bb-9912-d6941834c91b",
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c"
}
```

---


### Assistant

_source line 4_

I'll start by reading the main.tex file to locate all orphan labels and their surrounding context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "7b12eaa9-e821-46a4-be76-c6a68f03343d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DTWcGJTbyoynWnmCr7QgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12517,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12517
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

<details open><summary>🔧 Tool call — Read · `toolu_014647HXU6EhoP8DP6VaVTt7`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "1c6aaa4d-b616-4cb3-af77-1950c6b54f46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DTWcGJTbyoynWnmCr7QgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12517,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12517
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

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_019YmnmGoitw2FyXZXo5BPS9`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "6b197a6e-a3a7-4d67-81c6-2a27349b2245",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DTWcGJTbyoynWnmCr7QgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12517,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12517
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

_source line 7 · 2026-05-22T01:59:35.340Z_

<details><summary>↩ Tool result · reported error · `toolu_014647HXU6EhoP8DP6VaVTt7`</summary>

```text
File content (25898 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "8f8fbe8b-0508-4902-912d-55a4b2141020",
  "tool_use_result": "Error: File content (25898 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-22T01:59:35.266Z_

<details><summary>↩ Tool result · `toolu_019YmnmGoitw2FyXZXo5BPS9`</summary>

```text
docs/paper/conclusion.tex
docs/paper/supplementary.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
docs/paper/sdgd_negative.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "d84d77c7-7cc2-4447-a4f3-d92832ed588a",
  "tool_use_result": {
    "filenames": [
      "docs/paper/conclusion.tex",
      "docs/paper/supplementary.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/checklist.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/abstract.tex",
      "docs/paper/discussion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/results.tex",
      "docs/paper/main.tex"
    ],
    "durationMs": 9,
    "numFiles": 12,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The file is too large. Let me read it in chunks and also grep for the orphan labels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "56672230-8661-4cee-9518-c4874db64a54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQhaPRErTqdSU9ZeXavbBV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 24358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 10_

Let me find all the orphan labels and their locations first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "5dc7a779-6221-4770-976e-7df7973f4c56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQhaPRErTqdSU9ZeXavbBV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 24358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 11_

<details open><summary>🔧 Tool call — Grep · `toolu_019dhQcGfcB2vvhFoPW31qwe`</summary>

```json
{
  "pattern": "\\\\label\\{(tab:partial_corr|tab:error_examples|tab:prompt_variants|tab:variance_decomposition|tab:scs_baselines|tab:format_independence|tab:relaxed_matching|app:bcs-composition|app:cross-domain|sec:appendix_batch_composition|sec:appendix_cross_model_70b|sec:appendix_figures|sec:appendix_prompt_sensitivity|sec:appendix_type_defs|sec:conclusion|sec:metrics|sec:results|tab:bcs_aggregation|tab:fewshot_bcs|tab:renaming)\\}",
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "b4affba5-55ab-4e64-a937-774da70adb1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQhaPRErTqdSU9ZeXavbBV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 24358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 12 · 2026-05-22T01:59:40.863Z_

<details><summary>↩ Tool result · `toolu_019dhQcGfcB2vvhFoPW31qwe`</summary>

```text
docs/paper/main.tex:61:\label{sec:appendix_figures}
docs/paper/main.tex:325:\label{tab:partial_corr}
docs/paper/main.tex:336:\label{sec:appendix_batch_composition}
docs/paper/main.tex:360:\label{sec:appendix_prompt_sensitivity}
docs/paper/main.tex:396:\label{tab:prompt_variants}
docs/paper/main.tex:422:\label{tab:bcs_aggregation}
docs/paper/main.tex:472:\label{tab:format_independence}
docs/paper/main.tex:597:\label{app:bcs-composition}
docs/paper/main.tex:624:\label{tab:scs_baselines}
docs/paper/main.tex:661:\label{tab:variance_decomposition}
docs/paper/main.tex:667:\label{app:cross-domain}
docs/paper/main.tex:672:\label{sec:appendix_cross_model_70b}
docs/paper/main.tex:780:\label{tab:fewshot_bcs}
docs/paper/main.tex:853:\label{tab:error_examples}
docs/paper/main.tex:873:\label{tab:renaming}
docs/paper/main.tex:897:\label{tab:relaxed_matching}
docs/paper/experimental_setup.tex:90:\label{sec:metrics}
docs/paper/results.tex:2:\label{sec:results}
docs/paper/prompt_appendix.tex:200:\label{sec:appendix_type_defs}
docs/paper/discussion.tex:9:\label{sec:conclusion}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "a905e874-117e-43fb-822c-ccc78ba95ab3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:61:\\label{sec:appendix_figures}\ndocs/paper/main.tex:325:\\label{tab:partial_corr}\ndocs/paper/main.tex:336:\\label{sec:appendix_batch_composition}\ndocs/paper/main.tex:360:\\label{sec:appendix_prompt_sensitivity}\ndocs/paper/main.tex:396:\\label{tab:prompt_variants}\ndocs/paper/main.tex:422:\\label{tab:bcs_aggregation}\ndocs/paper/main.tex:472:\\label{tab:format_independence}\ndocs/paper/main.tex:597:\\label{app:bcs-composition}\ndocs/paper/main.tex:624:\\label{tab:scs_baselines}\ndocs/paper/main.tex:661:\\label{tab:variance_decomposition}\ndocs/paper/main.tex:667:\\label{app:cross-domain}\ndocs/paper/main.tex:672:\\label{sec:appendix_cross_model_70b}\ndocs/paper/main.tex:780:\\label{tab:fewshot_bcs}\ndocs/paper/main.tex:853:\\label{tab:error_examples}\ndocs/paper/main.tex:873:\\label{tab:renaming}\ndocs/paper/main.tex:897:\\label{tab:relaxed_matching}\ndocs/paper/experimental_setup.tex:90:\\label{sec:metrics}\ndocs/paper/results.tex:2:\\label{sec:results}\ndocs/paper/prompt_appendix.tex:200:\\label{sec:appendix_type_defs}\ndocs/paper/discussion.tex:9:\\label{sec:conclusion}",
    "numLines": 20
  }
}
```

</details>

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01D9RAs6e9y1pBLbPPHJ2319`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 50,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "e5b89417-5a0a-485b-ac07-600a7741c61d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DaR6QY4nqEs6vdnf6UshJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 24761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 14 · 2026-05-22T01:59:43.443Z_

<details><summary>↩ Tool result · `toolu_01D9RAs6e9y1pBLbPPHJ2319`</summary>

```text
50	\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.
51	
52	\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \citep{dror-2018-significance,card-2020-power}.
53	
54	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
55	
56	\bibliography{references}
57	
58	\appendix
59	
60	\section{Additional Figures}
61	\label{sec:appendix_figures}
62	
63	\begin{table}[h]
64	\centering
65	\small
66	\begin{tabular}{lrr}
67	\toprule
68	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
69	\midrule
70	1 & 0.702 & 0.640 \\
71	64 & 0.273 & 0.304 \\
72	\midrule
73	Decline & $-$43\,pp & $-$34\,pp \\
74	\bottomrule
75	\end{tabular}
76	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
77	\label{tab:cross_model}
78	\end{table}
79	
80	\begin{table}[h]
81	\centering
82	\small
83	\resizebox{\columnwidth}{!}{%
84	\begin{tabular}{crrrrrr}
85	\toprule
86	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
87	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
88	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
89	\midrule
90	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
91	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
92	\bottomrule
93	\end{tabular}}
94	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
95	\label{tab:cross_model_bcs}
96	\end{table}
97	
98	\begin{table}[h]
99	\centering
100	\small
101	\begin{tabular}{lcl}
102	\toprule
103	\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
104	\midrule
105	Qwen3-32B & $0.004$ ($p = 0.94$) & Null \\
106	LLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\rlap{$^\dagger$} & Null \\
107	LLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\rlap{$^\ddagger$} & Null \\
108	Gemini 2.5 Flash & --- & Not tested \\
109	\bottomrule
110	\end{tabular}
111	\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
112	\label{tab:cross_model_ner_null}
113	\end{table}
114	
115	\begin{table}[h]
116	\centering
117	\small
118	\resizebox{\columnwidth}{!}{%
119	\begin{tabular}{llrrrrrrr}
120	\toprule
121	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
122	\cmidrule(lr){3-7}
123	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
124	\midrule
125	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
126	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
127	DocRE & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
128	\midrule
129	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "56c6bc9f-307b-4e4f-bb3c-35669ca7b7ea",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\",
      "numLines": 80,
      "startLine": 50,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01FzcC8cGUEHDgKfUa4zBbWi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 310,
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "cfed4f69-31e9-4662-86b6-999964168d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DaR6QY4nqEs6vdnf6UshJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 24761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 16 · 2026-05-22T01:59:43.966Z_

<details><summary>↩ Tool result · `toolu_01FzcC8cGUEHDgKfUa4zBbWi`</summary>

```text
310	
311	To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).
312	
313	\begin{table}[h]
314	\centering
315	\small
316	\begin{tabular}{lrrrrr}
317	\toprule
318	\textbf{Dataset} & \textbf{$n$} & \textbf{$r_{\text{zero}}$} & \textbf{$r_{\text{partial}}$} & \textbf{$p_{\text{partial}}$} & \textbf{VIF} \\
319	\midrule
320	FewRel & 204 & $-$0.570 & $-$0.537 & ${<}\,0.001$ & 1.18 \\
321	DocRED & 110 & $-$0.760 & $-$0.348 & ${<}\,0.001$ & 50.9 \\
322	\bottomrule
323	\end{tabular}
324	\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\,=\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\,=\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}
325	\label{tab:partial_corr}
326	\end{table}
327	
328	On FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
329	
330	\subsection{NER BCS-Null Power Analysis}
331	\label{sec:appendix_ner_power}
332	
333	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
334	
335	\section{Batch Composition Results}
336	\label{sec:appendix_batch_composition}
337	
338	\begin{table}[h]
339	\centering
340	\small
341	\resizebox{\columnwidth}{!}{%
342	\begin{tabular}{@{}lcc@{}}
343	\toprule
344	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
345	\midrule
346	Single-pass (80 types) & 0.504 & 0.557 \\
347	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
348	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
349	\bottomrule
350	\end{tabular}}
351	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
352	\label{tab:batch_composition}
353	\end{table}
354	
355	See the accompanying discussion in \S\ref{sec:sdgd}.
356	
357	\input{prompt_appendix}
358	
359	\section{Prompt Version Sensitivity Analysis}
360	\label{sec:appendix_prompt_sensitivity}
361	
362	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
363	
364	\paragraph{RE (FewRel).}
365	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (95\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
366	
367	\paragraph{NER (Few-NERD).}
368	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
369	
370	\paragraph{Interpretation.}
371	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
372	
373	\subsection{Cross-Prompt-Variant BCS Correlation}
374	\label{sec:appendix_prompt_variants}
375	
376	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.
377	
378	\begin{table}[h]
379	\centering
380	\small
381	\resizebox{\columnwidth}{!}{\begin{tabular}{llrrrr}
382	\toprule
383	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
384	\midrule
385	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
386	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
387	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
388	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
389	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
390	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
391	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
392	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
393	\bottomrule
394	\end{tabular}}
395	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
396	\label{tab:prompt_variants}
397	\end{table}
398	
399	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
400	
401	\section{BCS Aggregation Sensitivity}
402	\label{sec:appendix_bcs_sensitivity}
403	
404	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
405	
406	\begin{table}[h]
407	\centering
408	\small
409	\resizebox{\columnwidth}{!}{%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "4f08e2f0-2d90-4567-bced-878aa16488c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nOn FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%",
      "numLines": 100,
      "startLine": 310,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01AMHUoqKTCZSYS1GH4TR5E7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 350,
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "8f29b173-5f18-445f-9fb9-3414b71684de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DaR6QY4nqEs6vdnf6UshJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 24761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 18 · 2026-05-22T01:59:44.848Z_

<details><summary>↩ Tool result · `toolu_01AMHUoqKTCZSYS1GH4TR5E7`</summary>

```text
350	\end{tabular}}
351	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
352	\label{tab:batch_composition}
353	\end{table}
354	
355	See the accompanying discussion in \S\ref{sec:sdgd}.
356	
357	\input{prompt_appendix}
358	
359	\section{Prompt Version Sensitivity Analysis}
360	\label{sec:appendix_prompt_sensitivity}
361	
362	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
363	
364	\paragraph{RE (FewRel).}
365	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (95\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
366	
367	\paragraph{NER (Few-NERD).}
368	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
369	
370	\paragraph{Interpretation.}
371	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
372	
373	\subsection{Cross-Prompt-Variant BCS Correlation}
374	\label{sec:appendix_prompt_variants}
375	
376	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.
377	
378	\begin{table}[h]
379	\centering
380	\small
381	\resizebox{\columnwidth}{!}{\begin{tabular}{llrrrr}
382	\toprule
383	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
384	\midrule
385	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
386	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
387	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
388	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
389	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
390	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
391	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
392	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
393	\bottomrule
394	\end{tabular}}
395	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
396	\label{tab:prompt_variants}
397	\end{table}
398	
399	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
400	
401	\section{BCS Aggregation Sensitivity}
402	\label{sec:appendix_bcs_sensitivity}
403	
404	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
405	
406	\begin{table}[h]
407	\centering
408	\small
409	\resizebox{\columnwidth}{!}{%
410	\begin{tabular}{llcccc}
411	\toprule
412	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
413	\midrule
414	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
415	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
416	\midrule
417	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
418	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
419	\bottomrule
420	\end{tabular}}
421	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
422	\label{tab:bcs_aggregation}
423	\end{table}
424	
425	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
426	
427	\section{BCS-Controlled Detailed Results}
428	\label{app:bcs-controlled-table}
429	
430	\begin{table}[h]
431	\centering
432	\small
433	\resizebox{\columnwidth}{!}{%
434	\begin{tabular}{lcrrrr}
435	\toprule
436	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
437	\midrule
438	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
439	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
440	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
441	\bottomrule
442	\end{tabular}}
443	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
444	\label{tab:bcs_controlled}
445	\end{table}
446	
447	\paragraph{Adjusted $R^2$ and confidence intervals.}
448	DocRED regressions (\S\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\% CI [0.47, 0.75]). The small shrinkage ($\Delta R^2 \leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.
449	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "6c51988c-9a37-46ae-bbac-5d8f1b6eb389",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n",
      "numLines": 100,
      "startLine": 350,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01Jn4WFypcPXCisAmzKUWUf7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 460,
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "a3739989-1bb1-4612-8222-f2c03af9db6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DaR6QY4nqEs6vdnf6UshJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 24761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 20 · 2026-05-22T01:59:45.778Z_

<details><summary>↩ Tool result · `toolu_01Jn4WFypcPXCisAmzKUWUf7`</summary>

```text
460	\textbf{Metric} & \textbf{Constrained} & \textbf{Unconstrained} \\
461	\midrule
462	Mean accuracy & 79.5\% & 79.6\% \\
463	Pearson $r$ (BCS vs.\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\
464	Spearman $\rho$ (BCS vs.\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\
465	\midrule
466	\multicolumn{3}{l}{\textit{Paired Fisher $z$-test for correlation equality}} \\
467	\quad Pearson $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
468	\quad Spearman $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
469	\bottomrule
470	\end{tabular}
471	\caption{Paired comparison of constrained vs.\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\Delta = -0.08$\,pp), ruling out a format-driven accuracy shift.}
472	\label{tab:format_independence}
473	\end{table}
474	
475	The near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\sim}2$\,pp; \S\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.
476	
477	\paragraph{Per-batch paired results.}
478	Table~\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \emph{identical} accuracy; the two exceptions (high\_5, high\_11) differ by a single sample (1/96 $\approx$ 1.04\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\%), confirming that the model generates valid type labels even without format constraints.
479	
480	\begin{table}[h]
481	\centering
482	\small
483	\resizebox{\columnwidth}{!}{%
484	\begin{tabular}{lcrrrr}
485	\toprule
486	\textbf{Batch} & \textbf{Group} & \textbf{BCS} & \textbf{Constr.} & \textbf{Unconstr.} & \textbf{$\Delta$} \\
487	\midrule
488	low\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\
489	low\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\
490	low\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\
491	low\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\
492	low\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\
493	low\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\
494	low\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\
495	low\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\
496	low\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\
497	low\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\
498	low\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\
499	low\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\
500	low\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\
501	\midrule
502	high\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\
503	high\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\
504	high\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\
505	high\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\
506	high\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\
507	high\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\
508	high\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\
509	high\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "6f083c70-5bfd-4bcb-868e-a4d6d04af79d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\",
      "numLines": 50,
      "startLine": 460,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_013egSBzfyjeQ7GxsvmoNcYP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 585,
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "f94526b1-1708-4e5a-b291-35b3454e1841",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DaR6QY4nqEs6vdnf6UshJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 24761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 22 · 2026-05-22T01:59:46.263Z_

<details><summary>↩ Tool result · `toolu_013egSBzfyjeQ7GxsvmoNcYP`</summary>

```text
585	\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
586	
587	\paragraph{Unconditional baseline.}
588	When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\text{SNR} \times \text{EF} / (\text{SNR} \times \text{EF} + 1) = 0.042$ with the same effective factor $\text{EF} = 3.35$. This ${\sim}5\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \emph{active} confusable pairs, not uniform contributions from all pairs.
589	
590	\paragraph{Sensitivity to $\rho$.}
591	The inter-pair SCS correlation $\rho = 0.35$ is estimated from pairs sharing a common type. At $\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \approx 0.22$, still matching the observed value; at $\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.
592	
593	\paragraph{Non-independence and ecological inference.}
594	Types within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\text{--}0.578$ (\S\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.
595	
596	\section{BCS Independence from Type Composition}
597	\label{app:bcs-composition}
598	
599	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.
600	
601	\section{SCS vs.\ Simple Baselines}
602	\label{app:scs-baselines}
603	
604	\begin{table}[h]
605	\centering
606	\small
607	\resizebox{\columnwidth}{!}{%
608	\begin{tabular}{llrr}
609	\toprule
610	\textbf{Dataset} & \textbf{Metric} & \textbf{Spearman $\rho$} & \textbf{$p$} \\
611	\midrule
612	FewRel & SCS (embedding) & \textbf{0.218} & $< 0.001$ \\
613	(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\
614	& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\
615	& Levenshtein & 0.016 & 0.363 (n.s.) \\
616	\midrule
617	Few-NERD & SCS (embedding) & \textbf{0.166} & $< 0.001$ \\
618	(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\
619	& Same-parent (prefix) & 0.146 & $< 0.001$ \\
620	& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\dagger$ \\
621	\bottomrule
622	\end{tabular}}
623	\caption{Pairwise confusion prediction: SCS vs.\ simple baselines. Spearman $\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\dagger$42\% of pairs lack WordNet coverage.}
624	\label{tab:scs_baselines}
625	\end{table}
626	
627	\section{Split-Origin Covariate Analysis}
628	\label{app:split-origin}
629	
630	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
631	
632	\paragraph{Method.}  Across 213 multi-type batches ($k \geq 2$) from the batch-composition experiment (\S\ref{sec:sdgd}) and the factorial design (\S\ref{sec:bcs_controlled}), we compute $\texttt{train\_origin\_ratio} = n_{\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:
633	{\small\begin{equation*}
634	\text{acc} = \beta_0 + \beta_{\text{BCS}} \!\cdot\! \text{BCS} + \beta_{\text{orig}} \!\cdot\! \text{train\_origin\_ratio} + \varepsilon
635	\end{equation*}}
636	
637	\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 0.001$ (vs.\ $\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
638	
639	Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.
640	
641	\section{Cross-Seed Variance Decomposition}
642	\label{app:variance-decomposition}
643	
644	\begin{table}[h]
645	\centering
646	\small
647	\begin{tabular}{rrrr}
648	\toprule
649	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
650	\midrule
651	4 & 0.0889 & 0.0122 & 53.5 \\
652	8 & 0.0820 & 0.0098 & 70.0 \\
653	16 & 0.0626 & 0.0270 & 5.4 \\
654	32 & 0.0462 & 0.0091 & 26.0 \\
655	40 & 0.0421 & 0.0019 & 474.4 \\
656	64 & 0.0245 & 0.0022 & 119.8 \\
657	80 & 0.0001 & 0.0088 & $<$0.1 \\
658	\bottomrule
659	\end{tabular}
660	\caption{Variance decomposition on FewRel (3 seeds $\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}
661	\label{tab:variance_decomposition}
662	\end{table}
663	
664	Intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\,=\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\,pp, likely attributable to FP8 quantization non-determinism).
665	
666	\section{Cross-Domain Connections}
667	\label{app:cross-domain}
668	
669	The schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
670	
671	\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
672	\label{sec:appendix_cross_model_70b}
673	
674	To test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
675	
676	\begin{table}[h]
677	\centering
678	\small
679	\begin{tabular}{lrr}
680	\toprule
681	\textbf{Count} & \textbf{LLaMA-70B} & \textbf{Qwen3-32B} \\
682	\midrule
683	\multicolumn{3}{l}{\textit{RE (FewRel, Classification Accuracy)}} \\
684	8  & 0.757 & 0.805 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "18aa398a-cbd1-450a-8825-933735bbb00f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\",
      "numLines": 100,
      "startLine": 585,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the remaining sections to find all orphan labels and their context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "eb3ec31b-441d-4040-9869-de4f27397d4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnPcbu2xiPjyEqGY4g5abH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13889,
      "cache_read_input_tokens": 25508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13889
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

_source line 24_

Let me continue reading the remaining sections with orphan labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "3dd86ed5-1583-4f89-a583-d4d0ffa15df1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnPcbu2xiPjyEqGY4g5abH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13889,
      "cache_read_input_tokens": 25508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13889
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01QufcCjDUBffWDJ6mR4RZvF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 760,
  "limit": 160
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "d9dd2075-5177-4850-bf45-b148bec81ee1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnPcbu2xiPjyEqGY4g5abH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13889,
      "cache_read_input_tokens": 25508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13889
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

_source line 26 · 2026-05-22T01:59:53.325Z_

<details><summary>↩ Tool result · `toolu_01QufcCjDUBffWDJ6mR4RZvF`</summary>

```text
760	\end{table}
761	
762	\section{Few-Shot Prompting and Confusability}
763	\label{sec:appendix_fewshot_bcs}
764	
765	To test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.
766	
767	\begin{table}[h]
768	\centering
769	\small
770	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
771	\toprule
772	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
773	\midrule
774	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
775	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
776	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
777	\bottomrule
778	\end{tabular}}
779	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
780	\label{tab:fewshot_bcs}
781	\end{table}
782	
783	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \citep{lost-in-middle-2024}.
784	
785	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
786	
787	\section{Qualitative Error Analysis}
788	\label{app:error-analysis}
789	
790	Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).
791	
792	\begin{table}[h]
793	\centering
794	\footnotesize
795	\begin{tabular}{clllr}
796	\toprule
797	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
798	\midrule
799	1 & instance of & taxon rank & 0.53 & 875 \\
800	2 & child & father & 0.84 & 700 \\
801	3 & participant of & participating team & 0.75 & 675 \\
802	4 & mountain range & part of & 0.57 & 575 \\
803	5 & mouth of watercourse & tributary & 0.65 & 549 \\
804	6 & child & mother & 0.84 & 500 \\
805	7 & league & member of & 0.66 & 450 \\
806	8 & country of citizenship & country of origin & 0.76 & 400 \\
807	9 & followed by & follows & 0.90 & 400 \\
808	10 & occupation & voice type & 0.57 & 400 \\
809	\bottomrule
810	\end{tabular}
811	\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \textit{followed by}/\textit{follows}, SCS\,=\,0.90) and family-relation pairs (\textit{child}/\textit{father}, \textit{child}/\textit{mother}) dominate. Some low-SCS pairs (\textit{instance of}/\textit{taxon rank}, SCS\,=\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}
812	\label{tab:top10_re}
813	\end{table}
814	
815	\begin{table}[h]
816	\centering
817	\footnotesize
818	\begin{tabular}{clllr}
819	\toprule
820	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
821	\midrule
822	1 & person-other & person-politician & 0.93 & 121 \\
823	2 & location-GPE & organization-other & 0.83 & 81 \\
824	3 & art-film & location-GPE & 0.69 & 57 \\
825	4 & building-other & location-GPE & 0.85 & 56 \\
826	5 & building-other & person-other & 0.90 & 43 \\
827	6 & location-GPE & product-other & 0.69 & 39 \\
828	7 & org-gov/agency & person-other & 0.85 & 34 \\
829	8 & person-actor & person-other & 0.90 & 34 \\
830	9 & building-other & location-road/transit & 0.76 & 32 \\
831	10 & location-GPE & org-sportsleague & 0.81 & 30 \\
832	\bottomrule
833	\end{tabular}
834	\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \textit{person-other}/\textit{person-politician}, SCS\,=\,0.93) and cross-category pairs sharing referent overlap (\textit{building-other}/\textit{location-GPE}, SCS\,=\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}
835	\label{tab:top10_ner}
836	\end{table}
837	
838	\begin{table*}[t]
839	\centering
840	\small
841	\begin{tabular}{p{8cm}llc}
842	\toprule
843	\textbf{Sentence} & \textbf{Gold} & \textbf{Pred.} & \textbf{SCS} \\
844	\midrule
845	\ldots\ played for \textbf{Valencia} \ldots\ [\textbf{EuroLeague}] & participant & participant of & .97 \\
846	\addlinespace
847	\textbf{Pilões} is a municipality in \textbf{Rio Grande do Norte} \ldots & contains a.t.e. & located in a.t.e. & .92 \\
848	\addlinespace
849	Davies \ldots\ appointed to \textbf{Cabinet} as \textbf{Sec.\ of State} & part of & member of & .90 \\
850	\bottomrule
851	\end{tabular}
852	\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\,$>$\,0.90: \textit{participant} vs.\ \textit{participant of} reverses directionality; \textit{contains} vs.\ \textit{located in} inverts containment; \textit{part of} vs.\ \textit{member of} conflates meronymy with membership. a.t.e.\ = admin.\ territorial entity.}
853	\label{tab:error_examples}
854	\end{table*}
855	
856	\section{Schema Label Renaming Experiment}
857	\label{app:renaming}
858	
859	To test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \textit{participant of} $\to$ \textit{event involvement} (SCS: 0.97 $\to$ 0.72), \textit{follows} $\to$ \textit{prior entry} (0.90 $\to$ 0.69), \textit{part of} $\to$ \textit{integral segment of} (0.90 $\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.
860	
861	\begin{table}[h!]
862	\centering
863	\small
864	\begin{tabular}{lccc}
865	\toprule
866	& \textbf{Control} & \textbf{Treatment} & \textbf{$\Delta$\,(pp)} \\
867	\midrule
868	Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\
869	High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\
870	\bottomrule
871	\end{tabular}
872	\caption{Accuracy (\%) under original vs.\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\Delta_{\text{high}} - \Delta_{\text{low}} = -5.9$\,pp ($t = -7.23$, $p < 0.001$).}
873	\label{tab:renaming}
874	\end{table}
875	
876	Renaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\geq$ original $-5$\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.
877	
878	\section{Relaxed Matching Evaluation (NER)}
879	\label{app:relaxed-matching}
880	
881	To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\times$ 25 batches $\times$ 3 seeds).
882	
883	\begin{table}[h!]
884	\centering
885	\small
886	\begin{tabular}{lrrrrr}
887	\toprule
888	\textbf{Match mode} & \textbf{$r$} & \textbf{$p$} & \textbf{$\rho$} & \textbf{$p$} & \textbf{F1} \\
889	\midrule
890	Exact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\
891	Relaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\
892	Token overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\
893	Type-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\
894	\bottomrule
895	\end{tabular}
896	\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\,pp (98.4\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}
897	\label{tab:relaxed_matching}
898	\end{table}
899	
900	A per-error-mode analysis confirms this null extends to all individual categories: miss ($\rho = 0.017$), boundary ($\rho = -0.043$), and type substitution ($\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.
901	
902	\end{document}
903	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "93a4043c-641b-4a64-ab8b-56c5c9834cdf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
      "numLines": 144,
      "startLine": 760,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01LafdXKsCPoeZY1U4veRjr1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 450,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "ab6f13a3-f818-4a5e-b07d-486563f476d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnPcbu2xiPjyEqGY4g5abH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13889,
      "cache_read_input_tokens": 25508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13889
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

_source line 28 · 2026-05-22T01:59:53.406Z_

<details><summary>↩ Tool result · `toolu_01LafdXKsCPoeZY1U4veRjr1`</summary>

```text
450	\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
451	\label{app:format-independence}
452	
453	To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.
454	
455	\begin{table}[h]
456	\centering
457	\small
458	\begin{tabular}{lrr}
459	\toprule
460	\textbf{Metric} & \textbf{Constrained} & \textbf{Unconstrained} \\
461	\midrule
462	Mean accuracy & 79.5\% & 79.6\% \\
463	Pearson $r$ (BCS vs.\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\
464	Spearman $\rho$ (BCS vs.\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\
465	\midrule
466	\multicolumn{3}{l}{\textit{Paired Fisher $z$-test for correlation equality}} \\
467	\quad Pearson $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
468	\quad Spearman $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
469	\bottomrule
470	\end{tabular}
471	\caption{Paired comparison of constrained vs.\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\Delta = -0.08$\,pp), ruling out a format-driven accuracy shift.}
472	\label{tab:format_independence}
473	\end{table}
474	
475	The near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\sim}2$\,pp; \S\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.
476	
477	\paragraph{Per-batch paired results.}
478	Table~\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \emph{identical} accuracy; the two exceptions (high\_5, high\_11) differ by a single sample (1/96 $\approx$ 1.04\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\%), confirming that the model generates valid type labels even without format constraints.
479	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "08132b4f-35b2-4f8b-96c5-233c690a682f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n",
      "numLines": 30,
      "startLine": 450,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01QDuxS8LmayKcpeLgxQAKUy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
  "offset": 190,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "fc75ea6e-9554-4098-acb8-585c90368a99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnPcbu2xiPjyEqGY4g5abH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13889,
      "cache_read_input_tokens": 25508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13889
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

_source line 30 · 2026-05-22T01:59:53.488Z_

<details><summary>↩ Tool result · `toolu_01QDuxS8LmayKcpeLgxQAKUy`</summary>

```text
190	\begin{lstlisting}
191	{"type": "object",
192	 "properties": {
193	   "relation": {"type": "string",
194	     "enum": [&lt;sorted_types>, "none"]}},
195	 "required": ["relation"]}
196	\end{lstlisting}
197	\end{small}
198	
199	\subsection{Type Definitions}
200	\label{sec:appendix_type_defs}
201	
202	All prompts include per-type natural-language definitions sourced from the respective dataset documentation:
203	\begin{itemize}[leftmargin=*,itemsep=2pt]
204	\item \textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \citep{fewnerd-2021}.
205	\item \textbf{MAVEN:} 168 event types with FrameNet-based definitions \citep{maven-2020}.
206	\item \textbf{FewRel:} 80 relation types with Wikidata property descriptions \citep{fewrel-2018}.
207	\end{itemize}
208	
209	\noindent Type definitions are injected as ``\texttt{- \{type\_name\}: \{definition\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \S\ref{sec:exp_design}).
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "4f1be3f7-f2cc-4a89-a2e4-d9b84959521b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
      "content": "\\begin{lstlisting}\n{\"type\": \"object\",\n \"properties\": {\n   \"relation\": {\"type\": \"string\",\n     \"enum\": [&lt;sorted_types>, \"none\"]}},\n \"required\": [\"relation\"]}\n\\end{lstlisting}\n\\end{small}\n\n\\subsection{Type Definitions}\n\\label{sec:appendix_type_defs}\n\nAll prompts include per-type natural-language definitions sourced from the respective dataset documentation:\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \\citep{fewnerd-2021}.\n\\item \\textbf{MAVEN:} 168 event types with FrameNet-based definitions \\citep{maven-2020}.\n\\item \\textbf{FewRel:} 80 relation types with Wikidata property descriptions \\citep{fewrel-2018}.\n\\end{itemize}\n\n\\noindent Type definitions are injected as ``\\texttt{- \\{type\\_name\\}: \\{definition\\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \\S\\ref{sec:exp_design}).\n",
      "numLines": 21,
      "startLine": 190,
      "totalLines": 210
    }
  }
}
```

</details>

---


### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of all orphan labels and their context. Let me also check for existing \ref calls to these labels to make sure they're truly orphan, and check results.tex for mentions of appendix sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "22dafd63-bdc0-48c2-9279-fb04f47cd8d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMERZV5rf8uiPFf6x6caj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5890,
      "cache_read_input_tokens": 39397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5890
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

_source line 32_

Now let me check which labels are truly orphan by searching for existing `\ref` calls, and check results.tex for appendix mentions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "25c93b53-6765-4a99-ab70-30415e35233b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMERZV5rf8uiPFf6x6caj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5890,
      "cache_read_input_tokens": 39397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5890
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

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01JFJYW44NxVaXAhUxnKbSAK`</summary>

```json
{
  "pattern": "\\\\ref\\{(tab:partial_corr|tab:error_examples|tab:prompt_variants|tab:variance_decomposition|tab:scs_baselines|tab:format_independence|tab:relaxed_matching|app:bcs-composition|app:cross-domain|sec:appendix_batch_composition|sec:appendix_cross_model_70b|sec:appendix_figures|sec:appendix_prompt_sensitivity|sec:appendix_type_defs|sec:conclusion|sec:metrics|sec:results|tab:bcs_aggregation|tab:fewshot_bcs|tab:renaming)\\}",
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "476190e2-03ed-4528-937d-7da0650ef25a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMERZV5rf8uiPFf6x6caj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5890,
      "cache_read_input_tokens": 39397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5890
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

_source line 34 · 2026-05-22T02:00:03.382Z_

<details><summary>↩ Tool result · `toolu_01JFJYW44NxVaXAhUxnKbSAK`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "09b3d73a-214a-4117-b955-ee2203a4390c",
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

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_01Lxi5hSV6ngjEyZTToHUMFt`</summary>

```json
{
  "pattern": "Appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "8b76eeec-b0f4-44c5-884d-0557c037a9e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMERZV5rf8uiPFf6x6caj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5890,
      "cache_read_input_tokens": 39397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5890
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

_source line 36 · 2026-05-22T02:00:04.355Z_

<details><summary>↩ Tool result · `toolu_01Lxi5hSV6ngjEyZTToHUMFt`</summary>

```text
4:All experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}).
9:[Omitted long matching line]
34:[Omitted long matching line]
47:[Omitted long matching line]
49:[Omitted long matching line]
56:Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
61:[Omitted long matching line]
65:[Omitted long matching line]
69:[Omitted long matching line]
78:[Omitted long matching line]
83:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "96fb5a94-7e4c-49ab-a786-a6500463d367",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "4:All experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}).\n9:[Omitted long matching line]\n34:[Omitted long matching line]\n47:[Omitted long matching line]\n49:[Omitted long matching line]\n56:Within-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n61:[Omitted long matching line]\n65:[Omitted long matching line]\n69:[Omitted long matching line]\n78:[Omitted long matching line]\n83:[Omitted long matching line]",
    "numLines": 11
  }
}
```

</details>

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01AzJRUEw8z25yLryCf8vLDN`</summary>

```json
{
  "pattern": "Appendix|\\\\S\\\\\\\\ref",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "e9a479c0-761a-444e-be2b-c2a0df634e2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxMERZV5rf8uiPFf6x6caj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5890,
      "cache_read_input_tokens": 39397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5890
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

_source line 38 · 2026-05-22T02:00:05.487Z_

<details><summary>↩ Tool result · `toolu_01AzJRUEw8z25yLryCf8vLDN`</summary>

```text
6:[Omitted long matching line]
11:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "d0e24778-3e08-4d68-97b8-0556d64e8ac7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "6:[Omitted long matching line]\n11:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Grep · `toolu_01RmFYqX3YM1WRSYEaKdvnZu`</summary>

```json
{
  "pattern": "Appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "9e80ca27-c0d9-4346-8353-6f34e97096c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDaP84kcXv7mXP86F3Vrce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 45287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 995
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 40 · 2026-05-22T02:00:09.682Z_

<details><summary>↩ Tool result · `toolu_01RmFYqX3YM1WRSYEaKdvnZu`</summary>

```text
4:All experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}).
9:[Omitted long matching line]
34:[Omitted long matching line]
47:[Omitted long matching line]
49:[Omitted long matching line]
56:Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
61:[Omitted long matching line]
65:[Omitted long matching line]
69:[Omitted long matching line]
78:[Omitted long matching line]
83:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "03dbdc77-d63f-4fd1-a574-2adc81ddb43e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "4:All experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}).\n9:[Omitted long matching line]\n34:[Omitted long matching line]\n47:[Omitted long matching line]\n49:[Omitted long matching line]\n56:Within-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n61:[Omitted long matching line]\n65:[Omitted long matching line]\n69:[Omitted long matching line]\n78:[Omitted long matching line]\n83:[Omitted long matching line]",
    "numLines": 11
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_01Tuia2ZaZJEu8Mhro4Ps4Zh`</summary>

```json
{
  "pattern": "Appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "10e5130e-21c1-4c7e-b3cc-a6501761a802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDaP84kcXv7mXP86F3Vrce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 45287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 995
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 42 · 2026-05-22T02:00:10.763Z_

<details><summary>↩ Tool result · `toolu_01Tuia2ZaZJEu8Mhro4Ps4Zh`</summary>

```text
6:[Omitted long matching line]
11:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "79c60a87-1336-4ff6-a963-2fc8a211d0b0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "6:[Omitted long matching line]\n11:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_013F4cBWstSYn27zQiGozFSJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 1,
  "limit": 90
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "e83ec14a-c041-4bb6-8b04-d9435353866e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N9229ovpznnAGzMJjehVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 46282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 44 · 2026-05-22T02:00:13.099Z_

<details><summary>↩ Tool result · `toolu_013F4cBWstSYn27zQiGozFSJ`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{llrrrrr}
21	\toprule
22	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
23	\midrule
24	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
25	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
26	\bottomrule
27	\end{tabular}}
28	\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}
29	\label{tab:pairwise}
30	\end{table}
31	
32	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
33	
34	The remaining variance reflects entity frequency, prompt position \citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\sim}$22\% of RE accuracy variance on FewRel (\S\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\ Qwen3 $r = 0.138$; Appendix), which indicates that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\ref{app:scs-baselines}). Appendix~\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.
35	
36	\begin{figure*}[t]
37	\centering
38	\includegraphics[width=\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}
39	\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\rho = 0.84\text{--}1.0$; Table~\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
40	\label{fig:error_taxonomy}
41	\end{figure*}
42	
43	\subsection{BCS-Controlled Experiments}
44	\label{sec:bcs_controlled}
45	
46	\looseness=-1
47	On FewRel, BCS explains ${\sim}$22\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\,=\,1.18$). DocRED partial correlation ($r_{\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\,=\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\ref{sec:appendix_partial_corr}).} the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
48	
49	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (95\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
50	
51	\paragraph{Document-level RE (DocRED).}
52	The effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\footnote{DocRED uses 5 batches per count level (vs.\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\,pp at count 16 ($\rho = -0.762$, 95\% CI [$-$0.88, $-$0.58]) and $-$15.7\,pp at count 32 ($\rho = -0.693$, 95\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\,=\,50.9$): semipartial $R^2_{\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\% of the explained variance is shared with centrality. The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\,=\,1.18$).
53	
54	\paragraph{Within-pool controlled comparison.}
55	\label{sec:within_pool}
56	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
57	
58	\paragraph{Practical magnitude.}
59	\label{sec:practical_magnitude}
60	\looseness=-1
61	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\text{BCS}} = 0.056$ after centrality; Appendix~\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The amplification from pairwise $r^2 \approx 1.5\%$ to batch-level $R^2 \approx 22\%$ is not a statistical artifact but the operative mechanism: correlated confusable-type interactions compound within shared prompts \citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\sim}3\times$ amplification illustrated by Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}).
62	
63	\paragraph{Cross-model validation.}
64	\looseness=-1
65	The effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap (Table~\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\Delta = -17.6$\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \to -0.42$, $p = 0.22$; Spearman: $\rho = -0.40 \to -0.18$, $p = 0.64$; Appendix~\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\ref{tab:cross_model_ner_null}).
66	
67	\paragraph{Prompt sensitivity.}
68	\looseness=-1
69	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\ref{sec:appendix_fewshot_bcs}).
70	
71	\subsection{Multi-Dimensional Degradation}
72	\label{sec:multi_channel}
73	
74	\looseness=-1
75	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\% of errors in high-BCS batches vs.\ 15\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\ref{tab:cross_model_error_taxonomy}).
76	
77	\looseness=-1
78	These results establish two dimensions: \textbf{Dimension~1} (count predicts recall decline) and \textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\,pp yields $\pm 2.3$\,pp. Both converge on $\pm 2\text{--}3$\,pp.\footnote{Margin sensitivity (Table~\ref{tab:tost_sensitivity}) confirms equivalence from $\pm 2$\,pp ($p = 0.047$) through $\pm 5$\,pp.} On the linear scale, TOST \citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\pm 3$\,pp ($p = 0.003$); at $\pm 2$\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\pm 3$\,pp; Appendix~\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\,pp, consistent with bounded interaction (Appendix~\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\S\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\%) limits statistical detection power to 65\% (Appendix~\ref{sec:appendix_ner_power}); the factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\,=\,0.027$, the minimum detectable correlation is $|r| \approx 0.132$ ($\alpha = 0.05$, power${}\,=\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\ref{app:renaming},~\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.
79	
80	\subsection{Centrality as a Potential Confound on Homogeneous Schemas}
81	\label{sec:centrality_confound}
82	
83	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation ($\rho = +0.184\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "b48e2ff3-0f22-4b02-90b8-fd4c8446612c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nAll experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}). The pattern is stable across three seeds (max $\\Delta = 10.7$\\,pp, within 1\\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$; Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\\sim}$22\\% of RE accuracy variance on FewRel (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), which indicates that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure*}\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\n\\looseness=-1\nOn FewRel, BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\\,=\\,1.18$). DocRED partial correlation ($r_{\\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\\,=\\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\\ref{sec:appendix_partial_corr}).} the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (95\\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\\footnote{DocRED uses 5 batches per count level (vs.\\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\\,pp at count 16 ($\\rho = -0.762$, 95\\% CI [$-$0.88, $-$0.58]) and $-$15.7\\,pp at count 32 ($\\rho = -0.693$, 95\\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\\,=\\,50.9$): semipartial $R^2_{\\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\\% of the explained variance is shared with centrality. The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\\,=\\,1.18$).\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\n\\looseness=-1\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\\text{BCS}} = 0.056$ after centrality; Appendix~\\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The amplification from pairwise $r^2 \\approx 1.5\\%$ to batch-level $R^2 \\approx 22\\%$ is not a statistical artifact but the operative mechanism: correlated confusable-type interactions compound within shared prompts \\citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\\sim}3\\times$ amplification illustrated by Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\n\\looseness=-1\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap (Table~\\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\\Delta = -17.6$\\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \\to -0.42$, $p = 0.22$; Spearman: $\\rho = -0.40 \\to -0.18$, $p = 0.64$; Appendix~\\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\\ref{tab:cross_model_ner_null}).\n\n\\paragraph{Prompt sensitivity.}\n\\looseness=-1\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\\ref{sec:appendix_fewshot_bcs}).\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\looseness=-1\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).\n\n\\looseness=-1\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}); the factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.\n\n\\subsection{Centrality as a Potential Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation ($\\rho = +0.184\\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \\citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.",
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

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me also check lines around specific sections I haven't read yet for context. Let me look at `app:bcs-composition` (line 597), `app:cross-domain` (line 667), `sec:appendix_cross_model_70b` (line 672), `sec:appendix_figures` (line 61), `sec:appendix_batch_composition` (line 336), and the tables around error_examples and renaming.

Now let me also check the remaining labels in the other tex files. Let me look at what `\ref` patterns exist for the discussion labels (sec:conclusion), experimental_setup (sec:metrics), and results (sec:results).


I'm finding the main section labels across the files—`sec:conclusion` in discussion.tex, `sec:metrics` in experimental_setup.tex, and `sec:results` in results.tex. Since the task specifies not to modify the main text, I should only add references in the appendix sections.

Now I'm identifying which labels need fixing. The director specified `tab:partial_corr` at line 325 in Appendix E.1, where the text discusses the table's content without actually referencing it. Looking at the paragraph around lines 328-329, I can see it describes the correlation findings but doesn't use `\ref` to point to the table itself, so I need to add that reference.

For `tab:error_examples` at line 853, the error analysis section mentions other tables but doesn't reference this one, so I'll need to integrate it into the existing discussion.

Looking at the remaining orphaned tables: `tab:prompt_variants` needs a reference in the prompt variants discussion around line 376, `tab:variance_decomposition` needs one in the variance decomposition section starting at line 641, and `tab:scs_baselines` needs integration into the SCS baselines appendix section around line 601.

I also need to add references for `tab:format_independence` in the format independence appendix and `tab:relaxed_matching` in the relaxed matching section. There are several section labels like `app:bcs-composition`, `app:cross-domain`, and `sec:appendix_batch_composition` that might need cross-references elsewhere in the document if there's relevant discussion pointing to them.

Looking at the remaining orphan labels, I see several appendix section labels and main-text sections like `sec:conclusion`, `sec:metrics`, and `sec:results` that would typically be referenced from other parts of the document.

For the appendix tables, I need to add explicit references in the nearby descriptive text since I can only modify appendix content. Let me focus on `tab:partial_corr` first—the paragraph around line 311 discusses computing partial correlations to rule out degree centrality as a confound, so I can introduce the table reference right at the start of that explanation.

For `tab:error_examples`, I'm looking at the error analysis section to find where this table naturally fits into the discussion. The intro mentions other tables, but this one shows illustrative confusion instances, so I need to locate the right spot to add the reference without disrupting the flow. I'm extending the caption for the top10 tables to also reference the error_examples table, so it reads: "Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\ref{tab:error_examples} provides illustrative confusion instances with their SCS values." Now for the prompt_variants table, I'm considering whether to add a reference in the intro text at line 376 or modify the discussion text at line 399 to explicitly call out the table.

For the variance_decomposition table, I need to add a reference somewhere in that section—either by modifying the discussion text at line 663 to start with the table reference, or by inserting it parenthetically after a relevant phrase. And I still need to handle the scs_baselines table at line 624.

Looking at the scs_baselines section, there's no body text after the table ends at line 625—the next section starts immediately at line 627. I should add a brief introductory or concluding sentence that references the table. For format_independence, I'm checking lines 450-475 to see how the section text introduces the table and whether I need to add references there as well. Looking at the remaining orphan labels, I need to add references for the BCS aggregation table around line 422, the few-shot BCS table at line 780, and the renaming table at line 873—each has introductory text, the table itself, and discussion that I can tie together with a reference. For the app:bcs-composition section label, I should search the appendix for any mentions of BCS independence or type composition that could naturally incorporate a section reference. I need to focus on the most critical missing references first—the tables that are actively broken or orphaned. Let me prioritize fixing `tab:partial_corr` and `tab:error_examples` since those are definitely referenced in the text but don't have labels yet. Then I'll work through the other orphaned table labels, starting with the ones that appear most frequently or are most important to the analysis like `tab:prompt_variants`, `tab:variance_decomposition`, and the baseline comparison tables. For the appendix section labels, I should only add references where the text naturally mentions them rather than forcing refs everywhere. I'm checking the existing references in results.tex to see where the partial correlation appendix is already mentioned—I found it at lines 47 and 61 with section references, but those don't point to the specific table within that appendix. The task allows me to add table references where the appendix section is already cited, so I can enhance those existing references with the table label. in both cases, adding the table reference would alter the narrative flow of the main text, which goes against the instruction to preserve existing narratives. The safer approach is to leave results.tex unchanged and ensure the table is properly documented in the appendix itself.

Let me finalize the edits I'll make: I'll add a clear reference to the table in the appendix section where it appears, making sure readers can easily locate it without modifying the main text's discussion of the findings. I need to be careful here—the instruction is to only add references, not change the narrative. For the section with no body text, I could either skip it or add a minimal sentence, but I'm second-guessing whether that violates the constraint. Let me double-check the actual line numbers to see if there's existing text I missed, then work through the remaining tables and appendix sections that need references added.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "e6323c7b-f00c-4d7d-b0ae-4a0bdaf89004",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VivZCrjNQAfb7rcPtvjM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5385,
      "cache_read_input_tokens": 47027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5385
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

_source line 46_

Now let me read the specific sections I haven't fully seen yet to plan precise edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "54456e5e-04ea-4b6f-adf0-689489d2b00b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VivZCrjNQAfb7rcPtvjM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5385,
      "cache_read_input_tokens": 47027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5385
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_012WGgAFj8evaeDbMCHW8BeT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 596,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "2e06ba44-8456-4407-88fc-560cdb4af81e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VivZCrjNQAfb7rcPtvjM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5385,
      "cache_read_input_tokens": 47027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5385
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

_source line 48 · 2026-05-22T02:02:01.630Z_

<details><summary>↩ Tool result · `toolu_012WGgAFj8evaeDbMCHW8BeT`</summary>

```text
596	\section{BCS Independence from Type Composition}
597	\label{app:bcs-composition}
598	
599	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.
600	
601	\section{SCS vs.\ Simple Baselines}
602	\label{app:scs-baselines}
603	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "6de798c6-0b28-4b84-87d3-89145f55c7b4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n",
      "numLines": 8,
      "startLine": 596,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01WAPXEDmALWC54njqbEB5wW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 835,
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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "2b7f2c3b-c2c6-436e-97cf-860dbb382746",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VivZCrjNQAfb7rcPtvjM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5385,
      "cache_read_input_tokens": 47027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5385
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

_source line 50 · 2026-05-22T02:02:02.247Z_

<details><summary>↩ Tool result · `toolu_01WAPXEDmALWC54njqbEB5wW`</summary>

```text
835	\label{tab:top10_ner}
836	\end{table}
837	
838	\begin{table*}[t]
839	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "16d8a9b6-bedf-478b-9896-f289fbcf11ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering",
      "numLines": 5,
      "startLine": 835,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Assistant

_source line 51_

Good. Now I have full context. Let me make all the edits. I'll start with the table references in main.tex appendix paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "d8727273-5059-457b-9620-a54fb1d536c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

<details open><summary>🔧 Tool call — Edit · `toolu_01HRK2YS2SHTkzhWaoMWH74r`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "On FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$).",
  "new_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "949c7a98-7a5d-4b91-84c1-21079b6d44cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

_source line 53 · 2026-05-22T02:02:09.613Z_

<details><summary>↩ Tool result · `toolu_01HRK2YS2SHTkzhWaoMWH74r`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "60d2ff8b-3f09-4a2d-8e48-7dd060d4f750",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "On FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$).",
    "newString": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$).",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nOn FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 325,
        "oldLines": 7,
        "newStart": 325,
        "newLines": 7,
        "lines": [
          " \\label{tab:partial_corr}",
          " \\end{table}",
          " ",
          "-On FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.",
          "+As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.",
          " ",
          " \\subsection{NER BCS-Null Power Analysis}",
          " \\label{sec:appendix_ner_power}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01NnVfekjuWiRXiG4gb3NGu4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).",
  "new_string": "Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "b3a8409b-d211-4423-be9c-ca608dfd49b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

_source line 55 · 2026-05-22T02:02:14.246Z_

<details><summary>↩ Tool result · `toolu_01NnVfekjuWiRXiG4gb3NGu4`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "4d0bcc4b-9fab-445c-9e80-2bbe65fbe378",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).",
    "newString": "Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 787,
        "oldLines": 7,
        "newStart": 787,
        "newLines": 7,
        "lines": [
          " \\section{Qualitative Error Analysis}",
          " \\label{app:error-analysis}",
          " ",
          "-Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).",
          "+Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.",
          " ",
          " \\begin{table}[h]",
          " \\centering"
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

<details open><summary>🔧 Tool call — Edit · `toolu_013NHk1yLHK8oaHf4JJnhbZc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.",
  "new_string": "we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "11430783-b5cf-4892-8cc1-c990e49b7540",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

_source line 57 · 2026-05-22T02:02:17.085Z_

<details><summary>↩ Tool result · `toolu_013NHk1yLHK8oaHf4JJnhbZc`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "d349903b-7fcd-437f-855d-bb6217de95ff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.",
    "newString": "we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 373,
        "oldLines": 7,
        "newStart": 373,
        "newLines": 7,
        "lines": [
          " \\subsection{Cross-Prompt-Variant BCS Correlation}",
          " \\label{sec:appendix_prompt_variants}",
          " ",
          "-To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.",
          "+To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).",
          " ",
          " \\begin{table}[h]",
          " \\centering"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Sc8V2d7mDsRSVRYYFaaP2n`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "Intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$)",
  "new_string": "Table~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "ec706b07-f209-4ca3-acbb-bcf0a07c3c22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

_source line 59 · 2026-05-22T02:02:19.789Z_

<details><summary>↩ Tool result · `toolu_01Sc8V2d7mDsRSVRYYFaaP2n`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "36d9e9bb-2c10-4059-98fa-27648d726ea3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "Intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$)",
    "newString": "Table~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$)",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 661,
        "oldLines": 7,
        "newStart": 661,
        "newLines": 7,
        "lines": [
          " \\label{tab:variance_decomposition}",
          " \\end{table}",
          " ",
          "-Intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).",
          "+Table~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).",
          " ",
          " \\section{Cross-Domain Connections}",
          " \\label{app:cross-domain}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01VpNjnCLKcruJ5XRghurrHC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "Here we compare both aggregation methods to verify that core conclusions are robust to this choice.",
  "new_string": "Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "53283b37-b1ca-462c-b3af-2470727f15cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

_source line 61 · 2026-05-22T02:02:21.366Z_

<details><summary>↩ Tool result · `toolu_01VpNjnCLKcruJ5XRghurrHC`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "c97a8791-1e2f-4f95-8337-554acb6bf652",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "Here we compare both aggregation methods to verify that core conclusions are robust to this choice.",
    "newString": "Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 401,
        "oldLines": 7,
        "newStart": 401,
        "newLines": 7,
        "lines": [
          " \\section{BCS Aggregation Sensitivity}",
          " \\label{sec:appendix_bcs_sensitivity}",
          " ",
          "-We define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.",
          "+We define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).",
          " ",
          " \\begin{table}[h]",
          " \\centering"
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

<details open><summary>🔧 Tool call — Edit · `toolu_011PWu55BybytuLqbZ6q4WmF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.",
  "new_string": "we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "7ef2c420-8c5a-4608-a3f0-b4e2048670e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153QiQF9QqzjZ44t4FG1Kva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5894,
      "cache_read_input_tokens": 52412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5894
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

_source line 63 · 2026-05-22T02:02:24.935Z_

<details><summary>↩ Tool result · `toolu_011PWu55BybytuLqbZ6q4WmF`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "3a1b77b1-4fae-4624-aeea-d7cfe10bb216",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.",
    "newString": "we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 450,
        "oldLines": 7,
        "newStart": 450,
        "newLines": 7,
        "lines": [
          " \\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}",
          " \\label{app:format-independence}",
          " ",
          "-To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs.",
          "+To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).",
          " ",
          " \\begin{table}[h]",
          " \\centering"
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

_source line 64_

Now let me handle the remaining table labels: `tab:scs_baselines`, `tab:relaxed_matching`, `tab:fewshot_bcs`, and `tab:renaming`. I also need to check the `tab:scs_baselines` section which has no body text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "868974bc-0d86-4e7d-9fd2-946024f3d797",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qU6YQbVDn3rwuwqDaYvfi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2082,
      "cache_read_input_tokens": 58306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2082
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

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_016i3aRN3Mdp3zuoxBhufRCL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 601,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "50a29d3b-15c0-4c68-a883-9d14b7dee682",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qU6YQbVDn3rwuwqDaYvfi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2082,
      "cache_read_input_tokens": 58306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2082
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

_source line 66 · 2026-05-22T02:02:30.891Z_

<details><summary>↩ Tool result · `toolu_016i3aRN3Mdp3zuoxBhufRCL`</summary>

```text
601	\section{SCS vs.\ Simple Baselines}
602	\label{app:scs-baselines}
603	
604	\begin{table}[h]
605	\centering
606	\small
607	\resizebox{\columnwidth}{!}{%
608	\begin{tabular}{llrr}
609	\toprule
610	\textbf{Dataset} & \textbf{Metric} & \textbf{Spearman $\rho$} & \textbf{$p$} \\
611	\midrule
612	FewRel & SCS (embedding) & \textbf{0.218} & $< 0.001$ \\
613	(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\
614	& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\
615	& Levenshtein & 0.016 & 0.363 (n.s.) \\
616	\midrule
617	Few-NERD & SCS (embedding) & \textbf{0.166} & $< 0.001$ \\
618	(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\
619	& Same-parent (prefix) & 0.146 & $< 0.001$ \\
620	& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\dagger$ \\
621	\bottomrule
622	\end{tabular}}
623	\caption{Pairwise confusion prediction: SCS vs.\ simple baselines. Spearman $\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\dagger$42\% of pairs lack WordNet coverage.}
624	\label{tab:scs_baselines}
625	\end{table}
626	
627	\section{Split-Origin Covariate Analysis}
628	\label{app:split-origin}
629	
630	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "7df98414-eeb3-4d0a-aaf8-71f432f4fcbf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.",
      "numLines": 30,
      "startLine": 601,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

````text
The `tab:scs_baselines` section has no body text. I need to add a brief sentence. Let me add it between the section header and the table.

For `tab:relaxed_matching`:
Let me re-read:
```
\section{Relaxed Matching Evaluation (NER)}
\label{app:relaxed-matching}

To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\times$ 25 batches $\times$ 3 seeds).


```

Then the table, then the discussion. I can add `(Table~\ref{tab:relaxed_matching})` at the end of the intro sentence.

For `tab:fewshot_bcs`:
The intro text describes testing whether in-context demonstrations reduce the BCS confusability effect across 0-shot, 1-shot, and 5-shot conditions on FewRel 80-relation RE at count 8, using the same extreme-BCS batch design. I can reference the table in the intro and note that each condition uses 50 batches with specific BCS distributions.

For `tab:renaming`:
I'm setting up a controlled intervention testing whether label renaming reduces pairwise SCS and improves accuracy on FewRel 80-relation RE with Qwen3-32B. The table will follow the description, and I can add the reference at an appropriate point.

Let me check the exact text placement for these tables.
```

I'm looking at where to insert the table references more precisely. For the renaming experiment, I can add `(Table~\ref{tab:renaming})` right after describing the controlled batch setup on line 859, since that's where the table results will be presented.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "4961a836-8cbd-4080-a944-a43163998031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ru5oCaJ2etjgpst72CpVG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 60388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01QZEDPfBFsCPv4vULEHXSXx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]",
  "new_string": "\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "a58a8d08-22bd-4548-bf2b-585925f14bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ru5oCaJ2etjgpst72CpVG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 60388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
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

_source line 69 · 2026-05-22T02:02:52.243Z_

<details><summary>↩ Tool result · `toolu_01QZEDPfBFsCPv4vULEHXSXx`</summary>

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
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "eb0ea3c1-f5d8-4bf9-9878-b5d06835b523",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]",
    "newString": "\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & .97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & .92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & .90 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 601,
        "oldLines": 6,
        "newStart": 601,
        "newLines": 8,
        "lines": [
          " \\section{SCS vs.\\ Simple Baselines}",
          " \\label{app:scs-baselines}",
          " ",
          "+Table~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.",
          "+",
          " \\begin{table}[h]",
          " \\centering",
          " \\small"
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

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_0158JXqEpNMFSQAqNSy5sm2T`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds).",
  "new_string": "we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f2564c-7f59-4832-b949-7a64ee42c97c",
  "uuid": "23c80e06-567f-4466-8b07-070a16bf1a02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ru5oCaJ2etjgpst72CpVG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 60388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
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
