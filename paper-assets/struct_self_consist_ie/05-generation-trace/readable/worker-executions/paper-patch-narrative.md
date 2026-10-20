# paper patch narrative

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_paper_patch-narrative_20260516T024638.log`
- **Structured JSON:** [`f36bac0dd4a24f464e5a.json`](../../sessions/f3/f36bac0dd4a24f464e5a.json)

## Before a recorded user message

68 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
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
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__verify_references",
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
  "uuid": "b81c9ef4-3a40-4ea8-8c26-332e69a67621",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778907000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ee0d1400-8f35-40f2-99cf-25f2e35f9015",
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de"
}
```

---

### Assistant

_source line 4_

I'll start by reading all the files that need editing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "7a8c4254-b366-425d-90b2-4186fbbd17a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU71dru2caCPfAiGYvGCBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13294,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13294
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

<details open><summary>🔧 Tool call — Read · `toolu_01P1YWjseo9e1Yk5F3D1xN1u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "72c5b8ec-a2b2-437b-8000-8ce56f836ce2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU71dru2caCPfAiGYvGCBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13294,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13294
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

_source line 6 · 2026-05-16T02:46:47.064Z_

<details><summary>↩ Tool result · `toolu_01P1YWjseo9e1Yk5F3D1xN1u`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "300728c6-7569-4e30-8500-baf6f86e7da5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_011DFWNs2dX9WsW7rr5yDm7V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "a92df96b-8e62-4910-ba1b-c78ec3564859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU71dru2caCPfAiGYvGCBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13294,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13294
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

_source line 8 · 2026-05-16T02:46:47.456Z_

<details><summary>↩ Tool result · `toolu_011DFWNs2dX9WsW7rr5yDm7V`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives.
14	\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.
15	\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.
16	These require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.
17	Existing evaluations rarely separate the two.
18	Self-consistency methods designed for discrete answers \cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.
19	Weighted variants that incorporate model confidence \cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.
20	The most directly relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.
21	No existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.
22	
23	Our central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.
24	Consistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.
25	Entity voting confidence, our best signal, achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.
26	Yet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.
27	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}).
28	The gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \textit{which inputs} are hard, not \textit{which output} is best.
29	Only log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.
30	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
31	
32	Our contributions are as follows:
33	\begin{enumerate}
34	    \item \textbf{First systematic comparison of confidence signals for generative IE.}
35	    We evaluate five signals from three families on quality estimation for NER and RE.
36	    Entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).
37	
38	    \item \textbf{Identification of the correlation-selection gap.}
39	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
40	    Despite strong instance-level correlations ($\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).
41	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
42	
43	    \item \textbf{Task-complexity boundary conditions.}
44	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\% of instances receive zero F1).
45	    This establishes practical guidance for signal selection based on expected task difficulty.
46	\end{enumerate}
47	
48	The remainder of this paper is organized as follows.
49	\S\ref{sec:method} formalizes the problem and defines the five confidence signals.
50	\S\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.
51	\S\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "c94e0785-4d50-4be3-bd81-e0f93a584d1a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \\cite{wang2023selfconsistency}.\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives.\n\\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.\n\\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.\nExisting evaluations rarely separate the two.\nSelf-consistency methods designed for discrete answers \\cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.\nWeighted variants that incorporate model confidence \\cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.\nThe most directly relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.\nNo existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.\n\nOur central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.\nConsistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.\nEntity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.\nYet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\nThe gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \\textit{which inputs} are hard, not \\textit{which output} is best.\nOnly log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First systematic comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\\% of instances receive zero F1).\n    This establishes practical guidance for signal selection based on expected task difficulty.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_019jQx6nXV2vMU28x28hna5N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "4cf39126-7e48-439d-b2fd-a1b9ecff0570",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU71dru2caCPfAiGYvGCBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13294,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13294
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

_source line 10 · 2026-05-16T02:46:48.384Z_

<details><summary>↩ Tool result · `toolu_019jQx6nXV2vMU28x28hna5N`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	Our results suggest different signal choices depending on the deployment scenario.
5	For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
6	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.
7	Under conditional filtering, SJ achieves $\rho{\approx}0.4$ on both NER and RE (\S\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.
8	For binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).
9	For best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\ref{tab:selection}).
10	
11	\paragraph{Signals discriminate between instances, not within strata.}
12	When instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.
13	Confidence signals capture \textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.
14	This is the complementary face of the correlation-selection gap (\S\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.
15	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
16	
17	\paragraph{Task-difficulty-dependent signal selection.}
18	Across all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\S\ref{sec:complexity_robustness}).
19	However, the \textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\% zero F1).
20	This ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.
21	
22	\paragraph{Capability boundary framework.}
23	Structural signals are most effective within the model's capability range.
24	Beyond it---RE with 44\% zero-F1 instances, WNUT-17 with 54\%---all signals converge toward zero or negative correlation.
25	Within the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$) than the full set.
26	Conditional filtering further separates signal families: at $N{=}16$, SJ maintains $\rho{=}0.308$ on RE while logprob collapses to $\rho{=}{-}0.026$ (\S\ref{sec:complexity_robustness}).
27	The ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.
28	
29	\paragraph{Methodological implications of $\rho$--AUROC separation.}
30	The logprob paradox on CoNLL with LLaMA---lowest $\rho$ (0.307) yet highest AUROC (0.761, Table~\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.
31	Logprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.
32	Different downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.
33	Evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "66d0bb24-4a75-437a-8a4f-a163abb6328c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nOur results suggest different signal choices depending on the deployment scenario.\nFor per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.\nUnder conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.\nFor binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).\nFor best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\\ref{tab:selection}).\n\n\\paragraph{Signals discriminate between instances, not within strata.}\nWhen instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.\nConfidence signals capture \\textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.\nThis is the complementary face of the correlation-selection gap (\\S\\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Task-difficulty-dependent signal selection.}\nAcross all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\\S\\ref{sec:complexity_robustness}).\nHowever, the \\textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\\% zero F1).\nThis ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.\n\n\\paragraph{Capability boundary framework.}\nStructural signals are most effective within the model's capability range.\nBeyond it---RE with 44\\% zero-F1 instances, WNUT-17 with 54\\%---all signals converge toward zero or negative correlation.\nWithin the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.\nConditional filtering further separates signal families: at $N{=}16$, SJ maintains $\\rho{=}0.308$ on RE while logprob collapses to $\\rho{=}{-}0.026$ (\\S\\ref{sec:complexity_robustness}).\nThe ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.\n\n\\paragraph{Methodological implications of $\\rho$--AUROC separation.}\nThe logprob paradox on CoNLL with LLaMA---lowest $\\rho$ (0.307) yet highest AUROC (0.761, Table~\\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.\nLogprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.\nDifferent downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.\nEvaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\n",
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01WRVnGDJaHZLZKq9cSRYQeb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "3bebc9d5-26f4-405c-a972-0aa11253b5d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU71dru2caCPfAiGYvGCBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13294,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13294
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

_source line 12 · 2026-05-16T02:46:49.101Z_

<details><summary>↩ Tool result · `toolu_01WRVnGDJaHZLZKq9cSRYQeb`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL, the SJ--FK gap is only 0.004 ($\rho{=}0.436$ vs.\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "92e08e23-ad93-42b0-8db7-6a99021b6809",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL, the SJ--FK gap is only 0.004 ($\\rho{=}0.436$ vs.\\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_014mQeXnu3kgmv5NR8DmJyxd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "b9452144-6506-4152-864f-7bbe4c36856c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU71dru2caCPfAiGYvGCBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13294,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13294
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

_source line 14 · 2026-05-16T02:46:49.233Z_

<details><summary>↩ Tool result · `toolu_014mQeXnu3kgmv5NR8DmJyxd`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
15	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
16	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "a93b58c1-1ccb-45c8-8d19-17f800a53dfd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
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
Now I have all files read. Let me execute the edits systematically.

### Task 1: introduction.tex - Add fig:overview figure environment near line 27
I need to add the figure environment after line 27 (after "We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}).").

### Task 2: introduction.tex - Complete section references (lines 48-51)
Replace the current lines 48-51 with the expanded version.

### Task 3: abstract.tex - Adjust WNUT-17 positioning (line 2-3)


I'll change the phrasing to clarify that WNUT-17 serves as a boundary probe rather than being grouped with the main datasets.

### Task 4: discussion.tex line 7 - AUROC=0.735 source
Replace "its ensemble with voting reaches AUROC${=}0.735$." with "its ensemble with voting reaches AUROC${=}0.735$ (\S\ref{sec:selection_gap})."

### Task 5: discussion.tex line 25 - n=81 subset

I need to expand the definition of the high-complexity RE subset to specify what makes instances high-complexity (those with 3 or more relation triples) and add a reference to the relevant section.

### Task 6: limitations.tex line 7-8 - Remove LR reference
Replace "Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound." with "Our analysis of selection potential uses unsupervised signals."

### Task 7: Terminology check
I should search through the files to ensure consistent terminology around entity voting and related confidence measures.

### Task 8: conclusion
Now I'm reviewing the conclusion section to make sure it's concise and doesn't duplicate information already covered in the rewritten thinking.

Let me proceed with all the edits since many of them are independent changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "81c9983d-c90f-40e4-8b96-10519ca1f173",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

Now executing all edits. Starting with the independent ones in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "5f22eb2e-8ad8-46c6-9923-8c2f2c44993b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

<details open><summary>🔧 Tool call — Edit · `toolu_01CAra8nCMDAfYSx3Nx6741q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
  "old_string": "across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17)",
  "new_string": "across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "6e503475-6b22-451e-9d8d-4dfbeebf0b8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

_source line 18 · 2026-05-16T02:47:04.092Z_

<details><summary>↩ Tool result · `toolu_01CAra8nCMDAfYSx3Nx6741q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "33e57d18-e267-47ff-b17c-02b70e5aca3b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
    "oldString": "across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17)",
    "newString": "across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe",
    "originalFile": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\begin{abstract}",
          " Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.",
          "-We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).",
          "+We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe with two model families (Qwen3-8B, LLaMA-3.1-8B).",
          " We find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).",
          " We term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.",
          " Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application."
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01N9NCCgYcwfxizfDi26gE5F`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
  "old_string": "We term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\nThe gap arises because",
  "new_string": "We term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_correlation_selection_gap}\n\\caption{The correlation-selection gap in structured IE. Confidence signals achieve strong rank correlation with instance-level quality ($\\rho$ up to 0.50) but fail to improve best-of-$N$ selection over greedy decoding. The gap arises because instance-level signals predict input difficulty, not output quality among candidates.}\n\\label{fig:overview}\n\\end{figure}\n\nThe gap arises because"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "f563c540-04d9-4af7-8723-65900a98ed5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

_source line 20 · 2026-05-16T02:47:07.531Z_

<details><summary>↩ Tool result · `toolu_01N9NCCgYcwfxizfDi26gE5F`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "56887c6b-6051-42d2-8514-96e6905e5122",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
    "oldString": "We term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\nThe gap arises because",
    "newString": "We term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_correlation_selection_gap}\n\\caption{The correlation-selection gap in structured IE. Confidence signals achieve strong rank correlation with instance-level quality ($\\rho$ up to 0.50) but fail to improve best-of-$N$ selection over greedy decoding. The gap arises because instance-level signals predict input difficulty, not output quality among candidates.}\n\\label{fig:overview}\n\\end{figure}\n\nThe gap arises because",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \\cite{wang2023selfconsistency}.\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives.\n\\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.\n\\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.\nExisting evaluations rarely separate the two.\nSelf-consistency methods designed for discrete answers \\cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.\nWeighted variants that incorporate model confidence \\cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.\nThe most directly relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.\nNo existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.\n\nOur central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.\nConsistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.\nEntity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.\nYet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\nThe gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \\textit{which inputs} are hard, not \\textit{which output} is best.\nOnly log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First systematic comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\\% of instances receive zero F1).\n    This establishes practical guidance for signal selection based on expected task difficulty.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.\n",
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 6,
        "newStart": 25,
        "newLines": 14,
        "lines": [
          " Entity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.",
          " Yet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.",
          " We term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).",
          "+",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\columnwidth]{figures/fig_correlation_selection_gap}",
          "+\\caption{The correlation-selection gap in structured IE. Confidence signals achieve strong rank correlation with instance-level quality ($\\rho$ up to 0.50) but fail to improve best-of-$N$ selection over greedy decoding. The gap arises because instance-level signals predict input difficulty, not output quality among candidates.}",
          "+\\label{fig:overview}",
          "+\\end{figure}",
          "+",
          " The gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \\textit{which inputs} are hard, not \\textit{which output} is best.",
          " Only log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.",
          " We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B."
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01XDXqaNPULwSTGUoBUHCnXM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
  "old_string": "The remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.",
  "new_string": "The remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape.\n\\S\\ref{sec:discussion} derives practical recommendations, and \\S\\ref{sec:conclusion} concludes with open directions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "a368408f-83d4-4fd5-b8a5-167c0919f30e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

_source line 22 · 2026-05-16T02:47:10.361Z_

<details><summary>↩ Tool result · `toolu_01XDXqaNPULwSTGUoBUHCnXM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "a3b1b3c0-f50f-4744-84e9-6e506f712b2f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
    "oldString": "The remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.",
    "newString": "The remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape.\n\\S\\ref{sec:discussion} derives practical recommendations, and \\S\\ref{sec:conclusion} concludes with open directions.",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \\cite{wang2023selfconsistency}.\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives.\n\\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.\n\\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.\nExisting evaluations rarely separate the two.\nSelf-consistency methods designed for discrete answers \\cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.\nWeighted variants that incorporate model confidence \\cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.\nThe most directly relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.\nNo existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.\n\nOur central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.\nConsistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.\nEntity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.\nYet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_correlation_selection_gap}\n\\caption{The correlation-selection gap in structured IE. Confidence signals achieve strong rank correlation with instance-level quality ($\\rho$ up to 0.50) but fail to improve best-of-$N$ selection over greedy decoding. The gap arises because instance-level signals predict input difficulty, not output quality among candidates.}\n\\label{fig:overview}\n\\end{figure}\n\nThe gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \\textit{which inputs} are hard, not \\textit{which output} is best.\nOnly log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First systematic comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\\% of instances receive zero F1).\n    This establishes practical guidance for signal selection based on expected task difficulty.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.\n",
    "structuredPatch": [
      {
        "oldStart": 56,
        "oldLines": 4,
        "newStart": 56,
        "newLines": 5,
        "lines": [
          " The remainder of this paper is organized as follows.",
          " \\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.",
          " \\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.",
          "-\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.",
          "+\\S\\ref{sec:related} situates our work in the broader landscape.",
          "+\\S\\ref{sec:discussion} derives practical recommendations, and \\S\\ref{sec:conclusion} concludes with open directions."
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01GA24G4f38YyUHygAerqQoE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
  "old_string": "its ensemble with voting reaches AUROC${=}0.735$.",
  "new_string": "its ensemble with voting reaches AUROC${=}0.735$ (\\S\\ref{sec:selection_gap})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "42503c09-86ba-4390-9df2-c29b7e0ac312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

_source line 24 · 2026-05-16T02:47:11.172Z_

<details><summary>↩ Tool result · `toolu_01GA24G4f38YyUHygAerqQoE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "e0847ef5-2b39-4033-9e6a-93572398635b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
    "oldString": "its ensemble with voting reaches AUROC${=}0.735$.",
    "newString": "its ensemble with voting reaches AUROC${=}0.735$ (\\S\\ref{sec:selection_gap}).",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nOur results suggest different signal choices depending on the deployment scenario.\nFor per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.\nUnder conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.\nFor binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).\nFor best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\\ref{tab:selection}).\n\n\\paragraph{Signals discriminate between instances, not within strata.}\nWhen instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.\nConfidence signals capture \\textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.\nThis is the complementary face of the correlation-selection gap (\\S\\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Task-difficulty-dependent signal selection.}\nAcross all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\\S\\ref{sec:complexity_robustness}).\nHowever, the \\textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\\% zero F1).\nThis ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.\n\n\\paragraph{Capability boundary framework.}\nStructural signals are most effective within the model's capability range.\nBeyond it---RE with 44\\% zero-F1 instances, WNUT-17 with 54\\%---all signals converge toward zero or negative correlation.\nWithin the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.\nConditional filtering further separates signal families: at $N{=}16$, SJ maintains $\\rho{=}0.308$ on RE while logprob collapses to $\\rho{=}{-}0.026$ (\\S\\ref{sec:complexity_robustness}).\nThe ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.\n\n\\paragraph{Methodological implications of $\\rho$--AUROC separation.}\nThe logprob paradox on CoNLL with LLaMA---lowest $\\rho$ (0.307) yet highest AUROC (0.761, Table~\\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.\nLogprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.\nDifferent downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.\nEvaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " Our results suggest different signal choices depending on the deployment scenario.",
          " For per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).",
          " When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.",
          "-Under conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.",
          "+Under conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$ (\\S\\ref{sec:selection_gap}).",
          " For binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).",
          " For best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\\ref{tab:selection}).",
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01Mmv8kfALfenc1HghjiBofD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
  "old_string": "the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$)",
  "new_string": "the high-complexity RE subset ($n{=}81$; instances with ${\\geq}3$ relation triples, see \\S\\ref{sec:complexity_robustness}) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "622dcb3a-b7ef-49c8-ac92-00cdce592bcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

_source line 26 · 2026-05-16T02:47:13.100Z_

<details><summary>↩ Tool result · `toolu_01Mmv8kfALfenc1HghjiBofD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "94fd18ac-4c96-456c-9993-3e48f557ddba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
    "oldString": "the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$)",
    "newString": "the high-complexity RE subset ($n{=}81$; instances with ${\\geq}3$ relation triples, see \\S\\ref{sec:complexity_robustness}) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$)",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nOur results suggest different signal choices depending on the deployment scenario.\nFor per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.\nUnder conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$ (\\S\\ref{sec:selection_gap}).\nFor binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).\nFor best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\\ref{tab:selection}).\n\n\\paragraph{Signals discriminate between instances, not within strata.}\nWhen instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.\nConfidence signals capture \\textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.\nThis is the complementary face of the correlation-selection gap (\\S\\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Task-difficulty-dependent signal selection.}\nAcross all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\\S\\ref{sec:complexity_robustness}).\nHowever, the \\textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\\% zero F1).\nThis ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.\n\n\\paragraph{Capability boundary framework.}\nStructural signals are most effective within the model's capability range.\nBeyond it---RE with 44\\% zero-F1 instances, WNUT-17 with 54\\%---all signals converge toward zero or negative correlation.\nWithin the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.\nConditional filtering further separates signal families: at $N{=}16$, SJ maintains $\\rho{=}0.308$ on RE while logprob collapses to $\\rho{=}{-}0.026$ (\\S\\ref{sec:complexity_robustness}).\nThe ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.\n\n\\paragraph{Methodological implications of $\\rho$--AUROC separation.}\nThe logprob paradox on CoNLL with LLaMA---lowest $\\rho$ (0.307) yet highest AUROC (0.761, Table~\\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.\nLogprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.\nDifferent downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.\nEvaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " \\paragraph{Capability boundary framework.}",
          " Structural signals are most effective within the model's capability range.",
          " Beyond it---RE with 44\\% zero-F1 instances, WNUT-17 with 54\\%---all signals converge toward zero or negative correlation.",
          "-Within the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.",
          "+Within the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$; instances with ${\\geq}3$ relation triples, see \\S\\ref{sec:complexity_robustness}) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.",
          " Conditional filtering further separates signal families: at $N{=}16$, SJ maintains $\\rho{=}0.308$ on RE while logprob collapses to $\\rho{=}{-}0.026$ (\\S\\ref{sec:complexity_robustness}).",
          " The ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.",
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_0131vz339ATLCPg68LjmicVj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
  "old_string": "Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.",
  "new_string": "Our analysis of selection potential uses unsupervised signals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "8d8a5840-f5b1-4601-94ff-44ee20e76b37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01173gQedoNXqedqeVonczLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 24995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4607
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

_source line 28 · 2026-05-16T02:47:13.885Z_

<details><summary>↩ Tool result · `toolu_0131vz339ATLCPg68LjmicVj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "1079f5e8-b5b5-4567-8d13-b8e4932f571c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
    "oldString": "Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.",
    "newString": "Our analysis of selection potential uses unsupervised signals.",
    "originalFile": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL, the SJ--FK gap is only 0.004 ($\\rho{=}0.436$ vs.\\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.",
          " Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.",
          " ",
          "-Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.",
          "+Our analysis of selection potential uses unsupervised signals.",
          " We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.",
          " ",
          " We evaluate at $N{=}8$ and $N{=}16$."
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

<details><summary>Logged reasoning block</summary>

```text
All 6 main edits done. Now I need to:
1. Task 7: Check terminology consistency across all files
2. Task 8: Check conclusion.tex for consistency, particularly whether scale ablation is mentioned

Let me grep for terminology variations and check the conclusion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "15ff03f8-1b24-4e15-b2c0-22c7bee0c11b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4tXwagEDgjm8ZL64gRapv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 29602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2541
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

All 6 primary edits done. Now checking terminology (task 7) and conclusion consistency (task 8).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "68a8c09e-ed92-4f61-98da-65379071eb9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4tXwagEDgjm8ZL64gRapv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 29602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2541
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

<details open><summary>🔧 Tool call — Grep · `toolu_018Ek1nvX9oRnYYPm54WXf9P`</summary>

```json
{
  "pattern": "entity voting|Voting Confidence|Voting Conf|voting confidence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-i": false,
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "b67900f3-d643-4bac-8469-eef91c11366d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4tXwagEDgjm8ZL64gRapv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 29602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2541
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

_source line 32 · 2026-05-16T02:47:18.818Z_

<details><summary>↩ Tool result · `toolu_018Ek1nvX9oRnYYPm54WXf9P`</summary>

```text
artifacts/_project/paper/experiments.tex:28:\textit{Structural} signals operate on extracted entity/relation sets: \textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \textbf{Soft Jaccard (SJ)} measures pairwise set similarity \cite{jaccard1901distribution}.
artifacts/_project/paper/experiments.tex:52:Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
artifacts/_project/paper/experiments.tex:64:On SciERC NER, Voting Confidence achieves $\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\rho{=}0.357$), and all remaining signals ($\rho{\leq}0.265$).
artifacts/_project/paper/conclusion.tex:8:First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
artifacts/_project/paper/discussion.tex:5:For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
artifacts/_project/paper/method.tex:35:\paragraph{Voting Confidence (VC).}
artifacts/_project/paper/method.tex:37:The voting confidence of an instance is the mean normalized frequency:
artifacts/_project/paper/abstract.tex:3:We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe with two model families (Qwen3-8B, LLaMA-3.1-8B).
artifacts/_project/paper/abstract.tex:4:We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
artifacts/_project/paper/introduction.tex:25:Entity voting confidence, our best signal, achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.
artifacts/_project/paper/introduction.tex:38:We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "35a7d01c-77e8-4c87-8d1d-4ccaa2feea54",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/experiments.tex:28:\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\nartifacts/_project/paper/experiments.tex:52:Voting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nartifacts/_project/paper/experiments.tex:64:On SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nartifacts/_project/paper/conclusion.tex:8:First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.\nartifacts/_project/paper/discussion.tex:5:For per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).\nartifacts/_project/paper/method.tex:35:\\paragraph{Voting Confidence (VC).}\nartifacts/_project/paper/method.tex:37:The voting confidence of an instance is the mean normalized frequency:\nartifacts/_project/paper/abstract.tex:3:We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe with two model families (Qwen3-8B, LLaMA-3.1-8B).\nartifacts/_project/paper/abstract.tex:4:We find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nartifacts/_project/paper/introduction.tex:25:Entity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.\nartifacts/_project/paper/introduction.tex:38:We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.",
    "numLines": 11
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01RzVjayzwoUe32hV6Jx2q7V`</summary>

```json
{
  "pattern": "ablation|scale|4B|free.form",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "5f466ee3-04d6-40ba-aa9c-434b9cf26cb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4tXwagEDgjm8ZL64gRapv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 29602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2541
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

_source line 34 · 2026-05-16T02:47:20.314Z_

<details><summary>↩ Tool result · `toolu_01RzVjayzwoUe32hV6Jx2q7V`</summary>

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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "0d4c77b5-ee32-4252-9a6a-d312dc270406",
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

<details open><summary>🔧 Tool call — Grep · `toolu_01Gq7ijcQ9yVjJfzmsEbfHq7`</summary>

```json
{
  "pattern": "ablation|4B|free.form|scale",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "output_mode": "content",
  "-i": true,
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "52aac01c-9fe3-44d4-b529-ea122589d19c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4tXwagEDgjm8ZL64gRapv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 29602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2541
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

_source line 36 · 2026-05-16T02:47:21.361Z_

<details><summary>↩ Tool result · `toolu_01Gq7ijcQ9yVjJfzmsEbfHq7`</summary>

```text
161:SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "4415ddb8-e5bd-4ee1-bc5d-1c941a211a53",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "161:SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Terminology analysis:
- `abstract.tex`: uses "entity voting" — correct
- `introduction.tex`: uses "entity voting" in signal lists, "Entity voting confidence" when describing the result — mostly consistent. "Entity voting confidence" on line 25 is fine, it's describing the confidence value.
- `discussion.tex`: uses "entity voting" — correct
- `conclusion.tex`: uses "entity voting" — correct
- `experiments.tex`: uses "Voting Confidence" as the formal name (defined in method), "Voting Conf." in tables — correct per convention


- `method.tex`: formally defines "Voting Confidence (VC)" — the terminology is consistent across the paper, with informal "entity voting" used in narrative sections and the formal "Voting Confidence" designation in technical sections.

For the conclusion, the +2.3pp improvement on RE checks out against Table 2, but I need to add a sentence covering the ablation studies, scaling behavior, and 4B model results since those aren't mentioned.

Looking through experiments.tex to see if there's explicit scale ablation or model-size analysis I can reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "b6f693ee-feef-46c8-8004-d40398105a40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jtu8QPcp4Km7LJYcz1BMiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 32143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1551
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Grep · `toolu_015xviasGfcpP66wtPDfAdte`</summary>

```json
{
  "pattern": "4B|ablat|model.size|parameter|scale.*analy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-i": true,
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "83292043-d530-4349-8c44-7753e3521a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jtu8QPcp4Km7LJYcz1BMiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 32143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1551
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 39 · 2026-05-16T02:47:33.070Z_

<details><summary>↩ Tool result · `toolu_015xviasGfcpP66wtPDfAdte`</summary>

```text
artifacts/_project/paper/related_work.tex:57:Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.
artifacts/_project/paper/related_work.tex:58:Our multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.
artifacts/_project/paper/freeform_ablation_appendix_table.tex:5:\label{tab:freeform-ablation}
artifacts/_project/paper/limitations.tex:4:We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
artifacts/_project/paper/n_scaling_appendix_tables.tex:1:% DEPRECATED: This file has been superseded by n_scaling_appendix_tables_44b000.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "08746238-022b-477d-a0bd-56a837100373",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:57:Deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.\nartifacts/_project/paper/related_work.tex:58:Our multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.\nartifacts/_project/paper/freeform_ablation_appendix_table.tex:5:\\label{tab:freeform-ablation}\nartifacts/_project/paper/limitations.tex:4:We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nartifacts/_project/paper/n_scaling_appendix_tables.tex:1:% DEPRECATED: This file has been superseded by n_scaling_appendix_tables_44b000.tex",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
There's a `freeform_ablation_appendix_table.tex` file. Let me check if the conclusion should mention this. Let me also check if there's a reference to it from experiments or appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "32f19bd0-663b-4ccb-a991-1df25b1c88fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoNnSz2TdBzuMC9sdYHrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 33694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

<details open><summary>🔧 Tool call — Grep · `toolu_01GLrvTrtWYLKRdxv2juewzY`</summary>

```json
{
  "pattern": "freeform|free.form",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "05836f7e-d1b3-4f98-ae52-116c0a8afad4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoNnSz2TdBzuMC9sdYHrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 33694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

_source line 42 · 2026-05-16T02:47:37.483Z_

<details><summary>↩ Tool result · `toolu_01GLrvTrtWYLKRdxv2juewzY`</summary>

```text
artifacts/_project/paper/related_work.tex:7:\paragraph{Self-consistency for discrete and free-form tasks.}
artifacts/_project/paper/related_work.tex:10:\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.
artifacts/_project/paper/related_work.tex:52:These approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.
artifacts/_project/paper/experiments.tex:239:NER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\ref{tab:freeform-ablation} in the Appendix).
artifacts/_project/paper/freeform_ablation_appendix_table.tex:4:\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
artifacts/_project/paper/freeform_ablation_appendix_table.tex:5:\label{tab:freeform-ablation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "35d96d5a-70a9-444e-8854-0525d0f78864",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:7:\\paragraph{Self-consistency for discrete and free-form tasks.}\nartifacts/_project/paper/related_work.tex:10:\\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \\cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.\nartifacts/_project/paper/related_work.tex:52:These approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \\textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.\nartifacts/_project/paper/experiments.tex:239:NER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nartifacts/_project/paper/freeform_ablation_appendix_table.tex:4:\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\nartifacts/_project/paper/freeform_ablation_appendix_table.tex:5:\\label{tab:freeform-ablation}",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
The freeform ablation is mentioned in experiments.tex (line 239) and has an appendix table. The conclusion doesn't mention this. The task says to add a mention of scale ablation results before "Several directions remain open" if not present.

Let me check what's in experiments around line 239 to understand the freeform ablation better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "3d8885a2-2c8b-45c7-996c-2c5bd70999d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o3Naynb6vv1myhJLNC1po",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 34491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 557
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01RpFjZLXqFGGnM3fDEKLkJa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "offset": 230,
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "b9725d8a-8389-46a5-b27d-10947bec868f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o3Naynb6vv1myhJLNC1po",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 34491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 557
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

_source line 45 · 2026-05-16T02:47:42.066Z_

<details><summary>↩ Tool result · `toolu_01RpFjZLXqFGGnM3fDEKLkJa`</summary>

```text
230	Yet the selection gap persists: on SciERC NER, all 4B signals perform \textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.
231	On CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\leq$0.1~pp of greedy---marginal by any standard.
232	The gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.
233	
234	\paragraph{Free-form decoding ablation.}
235	One concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.
236	We test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.
237	The fine-tuned model achieves a 99.95\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.
238	Crucially, LP standard deviation is virtually unchanged (0.0206 $\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\% $\to$ 57.7\%).
239	NER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\ref{tab:freeform-ablation} in the Appendix).
240	Score compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.
241	This reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.
242	
243	\paragraph{Cross-model transfer.}
244	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, 3-seed mean).
245	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
246	On conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
247	
248	\paragraph{Evaluation circularity.}
249	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "354a9950-d2b5-475d-a62c-65be1c82c2a4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
      "content": "Yet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.",
      "numLines": 20,
      "startLine": 230,
      "totalLines": 270
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
There's a 4B model scale ablation (line 230-232) and a free-form decoding ablation (line 234-241). The conclusion doesn't mention either. The task says to add a sentence mentioning scale ablation results before "Several directions remain open."

Let me add a sentence about both the 4B scale ablation and the free-form ablation in the conclusion. The key finding from both is that the correlation-selection gap is robust/universal.

I'll add something like: "Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints."


Now I should check the abstract to make sure my edit flows well with the rest of the text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "132ea914-e4c7-487d-a9db-5a7632b5e27f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYh5PDHrQ1fjxjtTp1PCwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 35048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 47_

The conclusion needs a sentence about the scale/free-form ablations. Also, I noticed the abstract edit created a grammar issue — "boundary probe with two model families" needs a comma. Let me fix both.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "fd455cbb-bc25-4be6-85b8-273848416641",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYh5PDHrQ1fjxjtTp1PCwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 35048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01DEuYQ1pxDvoRzWTGVSdZfV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
  "old_string": "Several directions remain open.",
  "new_string": "Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\\S\\ref{sec:experiments}).\n\nSeveral directions remain open."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "6cec5612-e145-42a2-b7e7-3197c02d3efa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYh5PDHrQ1fjxjtTp1PCwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 35048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 49 · 2026-05-16T02:47:49.769Z_

<details><summary>↩ Tool result · `toolu_01DEuYQ1pxDvoRzWTGVSdZfV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "65913e0a-3075-4140-8bae-1daf7abb160f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
    "oldString": "Several directions remain open.",
    "newString": "Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\\S\\ref{sec:experiments}).\n\nSeveral directions remain open.",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " Second, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.",
          " Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.",
          " ",
          "+Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\\S\\ref{sec:experiments}).",
          "+",
          " Several directions remain open.",
          " Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.",
          " Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings."
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01U6yp3t1Ziu4dqFj6Twixey`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
  "old_string": "with WNUT-17 as a boundary probe with two model families",
  "new_string": "with WNUT-17 as a boundary probe, using two model families"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "a08eb18a-8126-4c88-8a4c-c318c8cffde6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYh5PDHrQ1fjxjtTp1PCwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 35048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 51 · 2026-05-16T02:47:50.666Z_

<details><summary>↩ Tool result · `toolu_01U6yp3t1Ziu4dqFj6Twixey`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "ae30e3dc-3a2d-4459-b154-92c6afa90cef",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
    "oldString": "with WNUT-17 as a boundary probe with two model families",
    "newString": "with WNUT-17 as a boundary probe, using two model families",
    "originalFile": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\begin{abstract}",
          " Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.",
          "-We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe with two model families (Qwen3-8B, LLaMA-3.1-8B).",
          "+We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).",
          " We find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).",
          " We term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.",
          " Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application."
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

_source line 52_

Now verifying all edits — reading all modified files and running grep checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "d398172f-ddb0-402b-bde2-8be541838c5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01REiB9KTsUYYxqPyReUnXpo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "11ea3725-d220-44f1-b718-06de4b65cabb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 54 · 2026-05-16T02:47:53.834Z_

<details><summary>↩ Tool result · `toolu_01REiB9KTsUYYxqPyReUnXpo`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "9b1ed163-56a3-47e6-bdd0-327c3d2595df",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01DQ2RErVhkXakhWm6RNhbbu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "79baa1d1-10c7-4680-98bd-b0a32a908468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 56 · 2026-05-16T02:47:54.924Z_

<details><summary>↩ Tool result · `toolu_01DQ2RErVhkXakhWm6RNhbbu`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives.
14	\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.
15	\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.
16	These require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.
17	Existing evaluations rarely separate the two.
18	Self-consistency methods designed for discrete answers \cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.
19	Weighted variants that incorporate model confidence \cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.
20	The most directly relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.
21	No existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.
22	
23	Our central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.
24	Consistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.
25	Entity voting confidence, our best signal, achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.
26	Yet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.
27	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}).
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/fig_correlation_selection_gap}
32	\caption{The correlation-selection gap in structured IE. Confidence signals achieve strong rank correlation with instance-level quality ($\rho$ up to 0.50) but fail to improve best-of-$N$ selection over greedy decoding. The gap arises because instance-level signals predict input difficulty, not output quality among candidates.}
33	\label{fig:overview}
34	\end{figure}
35	
36	The gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \textit{which inputs} are hard, not \textit{which output} is best.
37	Only log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.
38	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
39	
40	Our contributions are as follows:
41	\begin{enumerate}
42	    \item \textbf{First systematic comparison of confidence signals for generative IE.}
43	    We evaluate five signals from three families on quality estimation for NER and RE.
44	    Entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).
45	
46	    \item \textbf{Identification of the correlation-selection gap.}
47	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
48	    Despite strong instance-level correlations ($\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).
49	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
50	
51	    \item \textbf{Task-complexity boundary conditions.}
52	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\% of instances receive zero F1).
53	    This establishes practical guidance for signal selection based on expected task difficulty.
54	\end{enumerate}
55	
56	The remainder of this paper is organized as follows.
57	\S\ref{sec:method} formalizes the problem and defines the five confidence signals.
58	\S\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.
59	\S\ref{sec:related} situates our work in the broader landscape.
60	\S\ref{sec:discussion} derives practical recommendations, and \S\ref{sec:conclusion} concludes with open directions.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "6efb37bc-8ef8-4094-b30b-fa3ee7193d20",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \\cite{wang2023selfconsistency}.\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives.\n\\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.\n\\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.\nExisting evaluations rarely separate the two.\nSelf-consistency methods designed for discrete answers \\cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.\nWeighted variants that incorporate model confidence \\cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.\nThe most directly relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.\nNo existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.\n\nOur central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.\nConsistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.\nEntity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.\nYet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_correlation_selection_gap}\n\\caption{The correlation-selection gap in structured IE. Confidence signals achieve strong rank correlation with instance-level quality ($\\rho$ up to 0.50) but fail to improve best-of-$N$ selection over greedy decoding. The gap arises because instance-level signals predict input difficulty, not output quality among candidates.}\n\\label{fig:overview}\n\\end{figure}\n\nThe gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \\textit{which inputs} are hard, not \\textit{which output} is best.\nOnly log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First systematic comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\\% of instances receive zero F1).\n    This establishes practical guidance for signal selection based on expected task difficulty.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape.\n\\S\\ref{sec:discussion} derives practical recommendations, and \\S\\ref{sec:conclusion} concludes with open directions.\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01A1Xux4SZFSdjw3QbFC37Db`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "494dc542-88ed-4b57-b1d5-d2eb477af1f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 58 · 2026-05-16T02:47:55.127Z_

<details><summary>↩ Tool result · `toolu_01A1Xux4SZFSdjw3QbFC37Db`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	Our results suggest different signal choices depending on the deployment scenario.
5	For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
6	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.
7	Under conditional filtering, SJ achieves $\rho{\approx}0.4$ on both NER and RE (\S\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$ (\S\ref{sec:selection_gap}).
8	For binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).
9	For best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\ref{tab:selection}).
10	
11	\paragraph{Signals discriminate between instances, not within strata.}
12	When instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.
13	Confidence signals capture \textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.
14	This is the complementary face of the correlation-selection gap (\S\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.
15	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
16	
17	\paragraph{Task-difficulty-dependent signal selection.}
18	Across all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\S\ref{sec:complexity_robustness}).
19	However, the \textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\% zero F1).
20	This ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.
21	
22	\paragraph{Capability boundary framework.}
23	Structural signals are most effective within the model's capability range.
24	Beyond it---RE with 44\% zero-F1 instances, WNUT-17 with 54\%---all signals converge toward zero or negative correlation.
25	Within the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$; instances with ${\geq}3$ relation triples, see \S\ref{sec:complexity_robustness}) yields substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$) than the full set.
26	Conditional filtering further separates signal families: at $N{=}16$, SJ maintains $\rho{=}0.308$ on RE while logprob collapses to $\rho{=}{-}0.026$ (\S\ref{sec:complexity_robustness}).
27	The ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.
28	
29	\paragraph{Methodological implications of $\rho$--AUROC separation.}
30	The logprob paradox on CoNLL with LLaMA---lowest $\rho$ (0.307) yet highest AUROC (0.761, Table~\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.
31	Logprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.
32	Different downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.
33	Evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "3364215b-197b-48df-b326-9a5f8def735d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nOur results suggest different signal choices depending on the deployment scenario.\nFor per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.\nUnder conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$ (\\S\\ref{sec:selection_gap}).\nFor binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).\nFor best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\\ref{tab:selection}).\n\n\\paragraph{Signals discriminate between instances, not within strata.}\nWhen instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.\nConfidence signals capture \\textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.\nThis is the complementary face of the correlation-selection gap (\\S\\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Task-difficulty-dependent signal selection.}\nAcross all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\\S\\ref{sec:complexity_robustness}).\nHowever, the \\textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\\% zero F1).\nThis ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.\n\n\\paragraph{Capability boundary framework.}\nStructural signals are most effective within the model's capability range.\nBeyond it---RE with 44\\% zero-F1 instances, WNUT-17 with 54\\%---all signals converge toward zero or negative correlation.\nWithin the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$; instances with ${\\geq}3$ relation triples, see \\S\\ref{sec:complexity_robustness}) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.\nConditional filtering further separates signal families: at $N{=}16$, SJ maintains $\\rho{=}0.308$ on RE while logprob collapses to $\\rho{=}{-}0.026$ (\\S\\ref{sec:complexity_robustness}).\nThe ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.\n\n\\paragraph{Methodological implications of $\\rho$--AUROC separation.}\nThe logprob paradox on CoNLL with LLaMA---lowest $\\rho$ (0.307) yet highest AUROC (0.761, Table~\\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.\nLogprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.\nDifferent downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.\nEvaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\n",
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

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_0116nU6rk8TBE2p7tKF7uSRd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "f81f4e7b-6b83-4962-bcb9-54b321175b19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 60 · 2026-05-16T02:47:55.646Z_

<details><summary>↩ Tool result · `toolu_0116nU6rk8TBE2p7tKF7uSRd`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL, the SJ--FK gap is only 0.004 ($\rho{=}0.436$ vs.\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "c2d66161-c797-48b5-aa53-6f9a866a37e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL, the SJ--FK gap is only 0.004 ($\\rho{=}0.436$ vs.\\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_012pKpYsfLLi8fgNKMViTe7h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "0c40c2ce-17b8-487e-b2e1-d5cf0ab182e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 62 · 2026-05-16T02:47:56.066Z_

<details><summary>↩ Tool result · `toolu_012pKpYsfLLi8fgNKMViTe7h`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\S\ref{sec:experiments}).
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
16	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
17	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
18	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "abcf465d-7154-44cb-997c-bc9cb9ddbb0d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.\n\nAblations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\\S\\ref{sec:experiments}).\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Grep · `toolu_01RMqgD9XLkm6fuo8fdbvSpY`</summary>

```json
{
  "pattern": "\\\\label\\{fig:overview\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "d51698e9-45c5-4620-bc1d-6dbfd4a67479",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 64 · 2026-05-16T02:47:57.551Z_

<details><summary>↩ Tool result · `toolu_01RMqgD9XLkm6fuo8fdbvSpY`</summary>

```text
artifacts/_project/paper/introduction.tex:33:\label{fig:overview}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "31b9f11d-3c5d-4ec1-8906-d5bdbf162d8e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/introduction.tex:33:\\label{fig:overview}",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_01Arfwi9nUCs9JyEbZdTs9NK`</summary>

```json
{
  "pattern": "logistic regression",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "1a7f8a59-68b8-4cae-8321-5c955aa92ea3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gxKsoaiqye3wxyKU7NhcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 36041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
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

_source line 66 · 2026-05-16T02:47:58.143Z_

<details><summary>↩ Tool result · `toolu_01Arfwi9nUCs9JyEbZdTs9NK`</summary>

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
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "1774853f-9142-460d-b61d-787581f0998a",
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

_source line 67_

All edits verified. Summary of changes:

1. **introduction.tex**: Added `fig:overview` figure environment (lines 29-34) with the correlation-selection gap figure. Added `\S Discussion` and `\S Conclusion` to paper outline (line 60).

2. **abstract.tex**: Changed WNUT-17 from equal-status dataset to "boundary probe" — now reads "on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families".

3. **discussion.tex**: AUROC=0.735 now cites `\S\ref{sec:selection_gap}` (line 7). The n=81 subset now includes its definition and a cross-reference to `\S\ref{sec:complexity_robustness}` (line 25).

4. **limitations.tex**: "logistic regression proxy as an upper bound" removed (line 8).

5. **conclusion.tex**: Added sentence about 4B scale and free-form decoding ablations confirming gap robustness (line 12).

6. **Terminology**: Consistent — abstract/intro/discussion/conclusion use "entity voting"; experiments/method use formal "Voting Confidence" / "Voting Conf." in tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "uuid": "72223ea1-e202-4214-a13c-ffa859ba1362",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nETQKrddRdK5a4xE6hYjT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5137,
      "cache_read_input_tokens": 36868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5137
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

_source line 68_

All edits verified. Summary of changes:

1. **introduction.tex**: Added `fig:overview` figure environment (lines 29-34) with the correlation-selection gap figure. Added `\S Discussion` and `\S Conclusion` to paper outline (line 60).

2. **abstract.tex**: Changed WNUT-17 from equal-status dataset to "boundary probe" — now reads "on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families".

3. **discussion.tex**: AUROC=0.735 now cites `\S\ref{sec:selection_gap}` (line 7). The n=81 subset now includes its definition and a cross-reference to `\S\ref{sec:complexity_robustness}` (line 25).

4. **limitations.tex**: "logistic regression proxy as an upper bound" removed (line 8).

5. **conclusion.tex**: Added sentence about 4B scale and free-form decoding ablations confirming gap robustness (line 12).

6. **Terminology**: Consistent — abstract/intro/discussion/conclusion use "entity voting"; experiments/method use formal "Voting Confidence" / "Voting Conf." in tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 83982,
  "duration_api_ms": 84914,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "b5f6cecf-efc6-4d13-8ff1-9b214857a2de",
  "total_cost_usd": 0.4613805000000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 30304,
    "cache_read_input_tokens": 274583,
    "output_tokens": 5290,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30304,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 297,
        "cache_read_input_tokens": 36868,
        "cache_creation_input_tokens": 5137,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5137
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2294,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002384,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 5290,
      "cacheReadInputTokens": 274583,
      "cacheCreationInputTokens": 30304,
      "webSearchRequests": 0,
      "costUSD": 0.45899650000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9f22808f-6c75-460e-9c19-47d0ea010db5"
}
```

</details>

---
