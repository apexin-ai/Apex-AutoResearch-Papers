# paper reviewer consistency check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_reviewer_consistency_check_20260515T031759.log`
- **Structured JSON:** [`eb29b2e0d025b37b5203.json`](../../sessions/eb/eb29b2e0d025b37b5203.json)

## Before a recorded user message

57 recorded events

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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
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
  "uuid": "c1df978d-09a9-4a14-a490-974b5600cd96",
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
    "resetsAt": 1778832600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a152f76f-35a0-49a2-a122-99f597882749",
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9"
}
```

---

### Assistant

_source line 4_

I'll read all the paper sections first to perform the consistency audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "72793658-81aa-42ab-8a93-e1a2bf0ffa5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

<details open><summary>🔧 Tool call — Read · `toolu_014H7DC3F8D7J48ztco5zzv3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "5bd043c3-0b71-43da-9fbc-cef2f8277680",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 6 · 2026-05-15T03:18:08.470Z_

<details><summary>↩ Tool result · `toolu_014H7DC3F8D7J48ztco5zzv3`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "aea62014-ec1a-4587-b84e-2fca0c430aad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that the strongest signals achieve $\\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
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

<details open><summary>🔧 Tool call — Read · `toolu_011iKPvkYiPwPGxzTT3kzkbC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "800b04a9-da9f-4ad3-98f3-e94124c6f59b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 8 · 2026-05-15T03:18:08.960Z_

<details><summary>↩ Tool result · `toolu_011iKPvkYiPwPGxzTT3kzkbC`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but (i)~relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs,'' (ii)~evaluates only quality estimation without studying best-of-$N$ selection, and (iii)~covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
17	No existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.
18	
19	Our central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.
20	Entity voting achieves $\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.
21	Yet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
22	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): instance-level signals predict \textit{which inputs} are hard, not \textit{which output} is best.
23	
24	\begin{figure*}[t]
25	\centering
26	\includegraphics[width=\textwidth]{fig_overview}
27	\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\rho{\approx}0.38$, AUROC${\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}
28	\label{fig:overview}
29	\end{figure*}
30	
31	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
32	
33	Our contributions are as follows:
34	\begin{enumerate}
35	    \item \textbf{First multi-family comparison of confidence signals for generative IE.}
36	    We evaluate five signals from three families on quality estimation for NER and RE.
37	    Entity voting achieves the strongest $\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).
38	
39	    \item \textbf{Identification of the correlation-selection gap.}
40	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
41	    Despite strong instance-level correlations ($\rho$ up to 0.38), no signal reliably surpasses greedy on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
42	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
43	
44	    \item \textbf{Task-complexity boundary conditions.}
45	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 54\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.
46	    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.
47	\end{enumerate}
48	
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "4bd25569-1216-44d4-8afd-90042c9f9fe4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but (i)~relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs,'' (ii)~evaluates only quality estimation without studying best-of-$N$ selection, and (iii)~covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.\nNo existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.\n\nOur central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.\nEntity voting achieves $\\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.\nYet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): instance-level signals predict \\textit{which inputs} are hard, not \\textit{which output} is best.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\\rho{\\approx}0.38$, AUROC${\\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First multi-family comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves the strongest $\\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.38), no signal reliably surpasses greedy on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 54\\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.\n    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.\n\\end{enumerate}\n\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01VVRjawJM2B7DipYzjvs7CB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "787ebb36-58be-4e35-94bc-b4614199a9aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 10 · 2026-05-15T03:18:09.420Z_

<details><summary>↩ Tool result · `toolu_01VVRjawJM2B7DipYzjvs7CB`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
32	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
33	\begin{equation}\label{eq:fk}
34	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
35	\end{equation}
36	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
37	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
38	
39	\paragraph{Soft Jaccard (structural, instance-level).}
40	Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
41	For samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:
42	\begin{equation}\label{eq:sj}
43	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
44	\end{equation}
45	where $M$ is the matched set from the Hungarian algorithm, $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
46	The instance-level signal averages over all pairs:
47	\begin{equation}\label{eq:sj_instance}
48	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{SJ}(y_i, y_j)
49	\end{equation}
50	
51	\paragraph{Entity voting confidence (structural, instance-level).}
52	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
53	The instance-level confidence is the mean frequency:
54	\begin{equation}\label{eq:voting}
55	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
56	\end{equation}
57	
58	\subsection{Evaluation Framework}\label{sec:evaluation}
59	
60	\paragraph{Quality estimation.}
61	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
62	
63	\paragraph{Sample selection.}
64	We report best-of-$N$ F1: for each instance, the signal selects one sample.
65	Per-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
66	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
67	
68	\paragraph{Complementarity.}
69	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "8bdb5a6e-8fb0-45ff-a6df-14a2102e2c52",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe compare five signals from three families: \\textit{model-internal} (log-probability), \\textit{surface} (exact match, Fleiss' $\\kappa$), and \\textit{structural} (Soft Jaccard, entity voting).\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm, $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01FkUkrdThVq8sHEkk45QFfp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "d0882d13-61f5-4033-a6d3-28fdf31d7131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 12 · 2026-05-15T03:18:10.073Z_

<details><summary>↩ Tool result · `toolu_01FkUkrdThVq8sHEkk45QFfp`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	\multicolumn{10}{l}{\textit{$N{=}8$}} \\
35	Voting Conf. & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
36	Soft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
37	Fleiss' $\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
38	Exact Match  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	Log-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
40	\midrule
41	\multicolumn{10}{l}{\textit{$N{=}16$ (3-seed)}} \\
42	Voting Conf. & Structural & & & & & & & .458${\pm}$.003 & \\
43	Soft Jaccard  & Structural & & & & & & & \textbf{.463${\pm}$.007} & \\
44	Fleiss' $\kappa$ & Surface & & & & & & & .455${\pm}$.006 & \\
45	Exact Match  & Surface    & & & & & & & .460${\pm}$.008 & \\
46	Log-prob     & Model      & & & & & & & .310${\pm}$.005 & \\
47	\bottomrule
48	\end{tabular}
49	\end{table*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig_signal_heatmap}
54	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while logprob RE collapses to near-zero ($\rho{=}0.011$).}
55	\label{fig:signal_heatmap}
56	\end{figure*}
57	
58	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
59	
60	\paragraph{Structural signals dominate on complex schemas.}
61	On SciERC NER, Voting achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and logprob ($\rho{=}0.205$).
62	The structural advantage persists on RE (Voting $\rho{=}0.350$), though all signals weaken due to the 44\% zero-F1 floor effect.
63	Entity voting and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
64	While $\rho{=}0.38$ explains approximately 14\% of F1 variance, the corresponding AUROC of 0.749 indicates strong discriminative power for the binary quality/failure classification most relevant to practitioners in quality-aware routing.
65	
66	\paragraph{$\rho$--AUROC dissociation.}
67	On NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\rho$ (0.134).
68	Binary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.
69	On CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307), confirming this dissociation across datasets.
70	
71	\paragraph{Signal rankings shift with task difficulty.}
72	On CoNLL (greedy F1${>}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.
73	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
74	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.
75	Cross-model stability is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
76	On WNUT-17, where 54\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.).
77	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
78	
79	\paragraph{Conditional filtering.}
80	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
81	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
82	Logprob RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
83	This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
84	
85	%% ============================================================
86	\subsection{The Correlation-Selection Gap}
87	\label{sec:selection_gap}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_selection_gap}
92	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}
93	\label{fig:selection_gap}
94	\end{figure*}
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking.}
100	\label{tab:selection}
101	\begin{tabular}{lcc}
102	\toprule
103	Method & NER F1 & RE F1 \\
104	\midrule
105	Oracle & 0.776 & 0.585 \\
106	\midrule
107	Log-prob           & \textbf{0.650} & 0.395 \\
108	Soft Jaccard       & 0.645 & 0.386 \\
109	Voting             & 0.634 & 0.359 \\
110	Exact Match        & ---   & ---   \\
111	\midrule
112	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
113	Random             & 0.608 & 0.354 \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
119	
120	\paragraph{No signal reliably surpasses greedy.}
121	We evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over $n{=}529$ NER instances, reporting 95\% percentile CIs.
122	The three random seeds (42, 123, 456) refer to independent inference runs; we average $\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\ greedy).
123	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
124	Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\%${=}$46.6\%).
125	On RE, the gap is complete: no signal exceeds greedy (0.404) despite 18.1~pp of oracle headroom.
126	Voting ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
127	
128	\paragraph{Quality estimation $\neq$ output selection.}
129	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
130	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
131	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
132	
133	%% ============================================================
134	\subsection{Robustness}
135	\label{sec:robustness_main}
136	
137	Consistency-based signals (SJ, Voting, FK) show robust performance across $T{\in}\{0.7, 1.0\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
138	SJ NER $\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).
139	Doubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
140	The structural-over-logprob advantage is consistent across tested model families, holding across all four $N{=}16$ settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$).
141	NER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).
142	For RE at $N{=}16$, SJ, FK, and logprob all plateau at $\rho{\approx}0.28$, suggesting compound errors impose a ceiling.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "3c298b0d-de44-4fa6-8ead-397742e92250",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). Best value per block and column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\\pm}$std.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}8$}} \\\\\nVoting Conf. & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}16$ (3-seed)}} \\\\\nVoting Conf. & Structural & & & & & & & .458${\\pm}$.003 & \\\\\nSoft Jaccard  & Structural & & & & & & & \\textbf{.463${\\pm}$.007} & \\\\\nFleiss' $\\kappa$ & Surface & & & & & & & .455${\\pm}$.006 & \\\\\nExact Match  & Surface    & & & & & & & .460${\\pm}$.008 & \\\\\nLog-prob     & Model      & & & & & & & .310${\\pm}$.005 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while logprob RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and logprob ($\\rho{=}0.205$).\nThe structural advantage persists on RE (Voting $\\rho{=}0.350$), though all signals weaken due to the 44\\% zero-F1 floor effect.\nEntity voting and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile $\\rho{=}0.38$ explains approximately 14\\% of F1 variance, the corresponding AUROC of 0.749 indicates strong discriminative power for the binary quality/failure classification most relevant to practitioners in quality-aware routing.\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nOn NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\\rho$ (0.134).\nBinary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.\nOn CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307), confirming this dissociation across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${>}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.\nCross-model stability is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 54\\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.).\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLogprob RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLog-prob           & \\textbf{0.650} & 0.395 \\\\\nSoft Jaccard       & 0.645 & 0.386 \\\\\nVoting             & 0.634 & 0.359 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\n\n\\paragraph{No signal reliably surpasses greedy.}\nWe evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over $n{=}529$ NER instances, reporting 95\\% percentile CIs.\nThe three random seeds (42, 123, 456) refer to independent inference runs; we average $\\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\\ greedy).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLogprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\\%${=}$46.6\\%).\nOn RE, the gap is complete: no signal exceeds greedy (0.404) despite 18.1~pp of oracle headroom.\nVoting ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals (SJ, Voting, FK) show robust performance across $T{\\in}\\{0.7, 1.0\\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nSJ NER $\\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).\nDoubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nThe structural-over-logprob advantage is consistent across tested model families, holding across all four $N{=}16$ settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$).\nNER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).\nFor RE at $N{=}16$, SJ, FK, and logprob all plateau at $\\rho{\\approx}0.28$, suggesting compound errors impose a ceiling.\n",
      "numLines": 143,
      "startLine": 1,
      "totalLines": 143
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01UfqwPrubSqxpYBn2LXTbuV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "ec97dc92-1017-4b71-9300-16fc80c4823e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 14 · 2026-05-15T03:18:10.301Z_

<details><summary>↩ Tool result · `toolu_01UfqwPrubSqxpYBn2LXTbuV`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\rho{=}0.724$, conditional $\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quality estimation ranks \textit{instances} by expected output quality; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
15	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
16	We observe a notable $\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\ref{app:additional} for details).
17	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
18	
19	\paragraph{Why logprob fails as a selector.}
20	Log-probability---the sole per-sample signal---also fails at selection despite its structural advantage for candidate ranking.
21	Under constrained decoding, logprob primarily reflects grammar compliance rather than semantic extraction quality: a sample may have high token-level confidence yet extract the wrong relation arguments.
22	Bootstrap analysis reveals that 75\% of instance-level logprob comparisons are effectively ties (win\%${=}$46.6\%, comparable to random), consistent with the non-significant selection result ($p{=}0.39$).
23	Mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.39$; RE: $\rho{=}0.33$; Figure~\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.
24	NER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.
25	Constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity beyond what free-form generation would exhibit.
26	The random baseline gap (3.6~pp) confirms meaningful variance exists even under constraints, but the correlation-selection gap may partially reflect this reduced diversity.
27	Future work should compare constrained vs.\ unconstrained decoding to disentangle these effects.
28	
29	\paragraph{Methodological implications.}
30	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
31	Effective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.
32	Further $N$-scaling analysis (Appendix~\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "bb2c6305-97a1-4689-af2a-c4532b0d5797",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, entity voting provides the strongest rank correlation ($\\rho{=}0.38$, Table~\\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}).\nUnder conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.\nSignal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\\rho{=}0.724$, conditional $\\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.\nThis ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.\nConditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\\to}0.241$).\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\n\\paragraph{Why quality estimators fail as selectors.}\nThe four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\\S\\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\\ref{tab:selection}) shows this conversion adds no reliable value.\nQuality estimation ranks \\textit{instances} by expected output quality; sample selection ranks \\textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.\nOn SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).\nWe observe a notable $\\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\\ref{app:additional} for details).\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Why logprob fails as a selector.}\nLog-probability---the sole per-sample signal---also fails at selection despite its structural advantage for candidate ranking.\nUnder constrained decoding, logprob primarily reflects grammar compliance rather than semantic extraction quality: a sample may have high token-level confidence yet extract the wrong relation arguments.\nBootstrap analysis reveals that 75\\% of instance-level logprob comparisons are effectively ties (win\\%${=}$46.6\\%, comparable to random), consistent with the non-significant selection result ($p{=}0.39$).\nMean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.39$; RE: $\\rho{=}0.33$; Figure~\\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.\nNER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.\nConstrained decoding enforces schema compliance at the token level, which may compress per-sample diversity beyond what free-form generation would exhibit.\nThe random baseline gap (3.6~pp) confirms meaningful variance exists even under constraints, but the correlation-selection gap may partially reflect this reduced diversity.\nFuture work should compare constrained vs.\\ unconstrained decoding to disentangle these effects.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\nEffective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.\nFurther $N$-scaling analysis (Appendix~\\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.\n",
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01QD6rxzrw9SLLuUcx8fbxXK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "719468c1-ecdd-4b11-82cb-3f0edd4d211f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 16 · 2026-05-15T03:18:11.578Z_

<details><summary>↩ Tool result · `toolu_01QD6rxzrw9SLLuUcx8fbxXK`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "8b6faaee-44d5-4432-88da-3dbe5e004d39",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.\nThis ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01SaMyZbp5gTk13Bd3sH7QGD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "aef4b109-b336-4945-ab4d-5d9f8ef862e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 18 · 2026-05-15T03:18:11.747Z_

<details><summary>↩ Tool result · `toolu_01SaMyZbp5gTk13Bd3sH7QGD`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "3ee0f132-a3f8-48cd-b628-31968aa1ea82",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01KxF69V15uFvVfzKQ9hbUrZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "58db14ab-99b3-4fbb-8e05-c95a38b1fd21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wmh6vPa4ALVvi7CA2LvQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11877,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11877
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

_source line 20 · 2026-05-15T03:18:12.146Z_

<details><summary>↩ Tool result · `toolu_01KxF69V15uFvVfzKQ9hbUrZ`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad Voting &  & $0.458{\pm}0.003$ & --- \\
57	\quad Logprob &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	Voting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Cross-model transfer.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\rho{=}0.411$ vs.\ logprob 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ logprob 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\rho{=}0.452$ vs.\ logprob 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ logprob $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
97	
98	\section{Additional Analyses}\label{app:additional}
99	
100	\paragraph{Per-relation diagnostic.}
101	RE signal degradation is relation-specific.
102	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
103	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
104	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
105	
106	\paragraph{Capability stratification.}
107	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
108	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
109	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
110	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
111	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
112	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\rho{=}0.630$, logprob $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
113	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
114	
115	\paragraph{Length vs.\ log-probability.}
116	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
117	
118	\begin{figure}[t]
119	\centering
120	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
121	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
122	\label{fig:length_logprob_scatter}
123	\end{figure}
124	
125	\paragraph{Evaluation circularity.}
126	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
127	Evaluation circularity is negligible.
128	
129	\paragraph{Conditional filtering details.}
130	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
131	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while logprob drops to $\rho{=}{-}0.026$.
132	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
133	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
134	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
135	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
136	
137	\paragraph{Diminishing returns of $N$-scaling.}
138	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
139	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
140	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
141	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ logprob $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.
142	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
143	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "fbc83bd0-925b-420b-9d76-12f800319f89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n$c_{\\text{vote}}$ & Entity voting confidence \\\\\n$c_{\\text{lp}}$ & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad Voting &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad Logprob &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVoting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\\rho{=}0.411$ vs.\\ logprob 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ logprob 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\\rho{=}0.452$ vs.\\ logprob 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ logprob $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\\rho{=}0.630$, logprob $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while logprob drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ logprob $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
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
Now let me also check if there are any other files in the paper directory that I should look at, like the main tex file and bibliography.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "cd9252cc-cdf2-4e96-a994-54fd8d2a0272",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsTJABgjL86iGmQNgDXmK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15691,
      "cache_read_input_tokens": 23578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15691
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

Now let me check the main tex file and bibliography for cross-reference completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "f5a1ecfc-0ca8-4d87-beef-c3d064f749c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsTJABgjL86iGmQNgDXmK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15691,
      "cache_read_input_tokens": 23578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15691
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

<details open><summary>🔧 Tool call — Glob · `toolu_01DqQtcXgpy2qxcsTpqYpjjZ`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "75363dd1-b93c-4fb5-ab84-fab87e51b3cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsTJABgjL86iGmQNgDXmK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15691,
      "cache_read_input_tokens": 23578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15691
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

_source line 24 · 2026-05-15T03:18:19.349Z_

<details><summary>↩ Tool result · `toolu_01DqQtcXgpy2qxcsTpqYpjjZ`</summary>

```text
docs/paper/main.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/limitations.tex
docs/paper/sections/experiments.tex
docs/paper/sections/discussion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/abstract.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "9d86ee99-1d89-4a60-b8a4-361c21ce7943",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/appendix.tex"
    ],
    "durationMs": 15,
    "numFiles": 10,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Glob · `toolu_01GXiyWbyqyZw65kkFMjG8Ju`</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "f8b146a0-84db-4800-8261-f95c6271ac34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsTJABgjL86iGmQNgDXmK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15691,
      "cache_read_input_tokens": 23578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15691
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

_source line 26 · 2026-05-15T03:18:19.762Z_

<details><summary>↩ Tool result · `toolu_01GXiyWbyqyZw65kkFMjG8Ju`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "f2e75e9c-e235-4852-b9eb-3c46c14db94b",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01FMkK3x8ZzArVs3XXYAARov`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "7662f87c-a56c-4d81-8245-fc6a4c168da4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwJF4i77qm8SWoq14ZsnKp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 39269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 28 · 2026-05-15T03:18:23.765Z_

<details><summary>↩ Tool result · `toolu_01FMkK3x8ZzArVs3XXYAARov`</summary>

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "4942c84c-648b-4a28-a8d1-039260e59653",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01Duh4YmGBKRgGYmt5zWsDKb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "62e1975b-0eeb-48ae-a0a6-6ba0de913381",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwJF4i77qm8SWoq14ZsnKp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 39269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 30 · 2026-05-15T03:18:24.387Z_

<details><summary>↩ Tool result · `toolu_01Duh4YmGBKRgGYmt5zWsDKb`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
45	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
46	  booktitle = {W-NUT Workshop at EMNLP 2017},
47	  year = {2017},
48	  url = {https://aclanthology.org/W17-4418/}
49	}
50	
51	@inproceedings{desai2020calibration,
52	  title = {Calibration of Pre-trained Transformers},
53	  author = {Desai, Shrey and Durrett, Greg},
54	  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
55	  year = {2020},
56	  doi = {10.18653/v1/2020.emnlp-main.21},
57	  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}
58	}
59	
60	@inproceedings{fisch2021conformal,
61	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
62	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
63	  booktitle = {ICML 2021},
64	  year = {2021},
65	  doi = {10.5555/3524938.3525234},
66	  url = {https://arxiv.org/abs/2102.08898}
67	}
68	
69	@article{fleiss1971agreement,
70	  title = {Measuring nominal scale agreement among many raters.},
71	  author = {Fleiss, Joseph L.},
72	  journal = {Psychological Bulletin},
73	  year = {1971},
74	  doi = {10.1037/h0031619},
75	  url = {http://dx.doi.org/10.1037/h0031619}
76	}
77	
78	@inproceedings{gal2016dropout,
79	  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
80	  author = {Gal, Yarin and Ghahramani, Zoubin},
81	  booktitle = {ICML 2016},
82	  year = {2016},
83	  url = {https://arxiv.org/abs/1506.02142}
84	}
85	
86	@inproceedings{geifman2017selective,
87	  title = {Selective Classification for Deep Neural Networks},
88	  author = {Geifman, Yonatan and El-Yaniv, Ran},
89	  booktitle = {NeurIPS 2017},
90	  year = {2017},
91	  url = {https://arxiv.org/abs/1705.08500}
92	}
93	
94	@article{feng2025optimal,
95	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
96	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
97	  journal = {arXiv preprint arXiv:2511.12309},
98	  year = {2025},
99	  url = {https://arxiv.org/abs/2511.12309}
100	}
101	
102	@inproceedings{geng2024confidence,
103	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
104	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
105	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
106	  year = {2024},
107	  doi = {10.18653/v1/2024.naacl-long.366},
108	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
109	}
110	
111	@inproceedings{guo2017calibration,
112	  title = {On Calibration of Modern Neural Networks},
113	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
114	  booktitle = {ICML 2017},
115	  year = {2017},
116	  url = {https://arxiv.org/abs/1706.04599}
117	}
118	
119	@article{hobelsberger2025systematic,
120	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
121	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
122	  journal = {arXiv preprint arXiv:2510.20460},
123	  year = {2025},
124	  url = {https://arxiv.org/abs/2510.20460}
125	}
126	
127	@article{jaccard1901distribution,
128	  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},
129	  author = {Jaccard, Paul},
130	  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},
131	  year = {1901},
132	  url = {https://www.researchgate.net/publication/225035806}
133	}
134	
135	@inproceedings{josifoski2022genie,
136	  title = {{GenIE}: Generative Information Extraction},
137	  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
138	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
139	  year = {2022},
140	  doi = {10.18653/v1/2022.naacl-main.342},
141	  url = {https://arxiv.org/abs/2112.08340}
142	}
143	
144	@article{kadavath2022language,
145	  title = {Language Models (Mostly) Know What They Know},
146	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
147	  journal = {arXiv preprint arXiv:2207.05221},
148	  year = {2022},
149	  url = {https://arxiv.org/abs/2207.05221}
150	}
151	
152	@inproceedings{kang2025selfcertainty,
153	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
154	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
155	  booktitle = {NeurIPS 2025},
156	  year = {2025},
157	  url = {https://arxiv.org/abs/2502.18581}
158	}
159	
160	@inproceedings{kim2026reasc,
161	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
162	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
163	  booktitle = {ACL 2026},
164	  year = {2026},
165	  url = {https://arxiv.org/abs/2601.02970}
166	}
167	
168	@article{kossen2024semantic,
169	  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},
170	  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
171	  journal = {arXiv preprint arXiv:2406.15927},
172	  year = {2024},
173	  url = {https://arxiv.org/abs/2406.15927}
174	}
175	
176	@article{li2025llms,
177	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
178	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
179	  journal = {arXiv preprint arXiv:2503.04104},
180	  year = {2025},
181	  url = {https://arxiv.org/abs/2503.04104}
182	}
183	
184	@inproceedings{kuhn2023semantic,
185	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
186	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
187	  booktitle = {ICLR 2023},
188	  year = {2023},
189	  url = {https://arxiv.org/abs/2302.09664}
190	}
191	
192	@inproceedings{lakshminarayanan2017ensembles,
193	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
194	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
195	  booktitle = {NeurIPS 2017},
196	  year = {2017},
197	  url = {https://arxiv.org/abs/1612.01474}
198	}
199	
200	@inproceedings{li2023codeie,
201	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
202	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
203	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
204	  year = {2023},
205	  doi = {10.18653/v1/2023.acl-long.855},
206	  url = {https://arxiv.org/abs/2305.05711}
207	}
208	
209	@inproceedings{lightman2024verify,
210	  title = {Let's Verify Step by Step},
211	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
212	  booktitle = {ICLR 2024},
213	  year = {2024},
214	  url = {https://arxiv.org/abs/2305.20050}
215	}
216	
217	@inproceedings{luan2018scierc,
218	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
219	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
220	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
221	  year = {2018},
222	  doi = {10.18653/v1/D18-1360},
223	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
224	}
225	
226	@inproceedings{manakul2023selfcheckgpt,
227	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
228	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
229	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
230	  year = {2023},
231	  doi = {10.18653/v1/2023.emnlp-main.557},
232	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
233	}
234	
235	@article{nedellec2026consistency,
236	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
237	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
238	  journal = {Genomics \& Informatics},
239	  year = {2026},
240	  doi = {10.1186/s44342-025-00063-2},
241	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
242	}
243	
244	@article{oh2025latentsc,
245	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
246	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
247	  journal = {arXiv preprint arXiv:2508.18395},
248	  year = {2025},
249	  url = {https://arxiv.org/abs/2508.18395}
250	}
251	
252	@inproceedings{sainz2024gollie,
253	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
254	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
255	  booktitle = {ICLR 2024},
256	  year = {2024},
257	  url = {https://arxiv.org/abs/2310.03668}
258	}
259	
260	@inproceedings{shelmanov2021active,
261	  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},
262	  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},
263	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
264	  year = {2021},
265	  doi = {10.18653/v1/2021.eacl-main.145},
266	  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}
267	}
268	
269	@inproceedings{snell2024scaling,
270	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
271	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
272	  booktitle = {ICLR 2025},
273	  year = {2024},
274	  url = {https://arxiv.org/abs/2408.03314}
275	}
276	
277	@inproceedings{taubenfeld2025cisc,
278	  title = {Confidence Improves Self-Consistency in LLMs},
279	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
280	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
281	  year = {2025},
282	  doi = {10.18653/v1/2025.findings-acl.1030},
283	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
284	}
285	
286	@inproceedings{thirukovalluru2024atomic,
287	  title = {Atomic Self-Consistency for Better Long Form Generations},
288	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
289	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
290	  year = {2024},
291	  doi = {10.18653/v1/2024.emnlp-main.706},
292	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
293	}
294	
295	@inproceedings{tjongkimsang2003conll,
296	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
297	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
298	  booktitle = {CoNLL 2003},
299	  year = {2003},
300	  url = {https://aclanthology.org/W03-0419/}
301	}
302	
303	@inproceedings{vashurin2025cocoa,
304	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
305	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
306	  booktitle = {NeurIPS 2025},
307	  year = {2025},
308	  url = {https://arxiv.org/abs/2502.04964}
309	}
310	
311	@inproceedings{wadhwa2023revisiting,
312	  title = {Revisiting Relation Extraction in the era of Large Language Models},
313	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
314	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
315	  year = {2023},
316	  doi = {10.18653/v1/2023.acl-long.868},
317	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
318	}
319	
320	@article{wang2023instructuie,
321	  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
322	  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
323	  journal = {arXiv preprint arXiv:2304.08085},
324	  year = {2023},
325	  url = {https://arxiv.org/abs/2304.08085}
326	}
327	
328	@inproceedings{wang2023selfconsistency,
329	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
330	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
331	  booktitle = {ICLR 2023},
332	  year = {2023},
333	  url = {https://arxiv.org/abs/2203.11171}
334	}
335	
336	@inproceedings{wang2025make,
337	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
338	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
339	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
340	  pages = {6919--6932},
341	  year = {2025}
342	}
343	
344	@inproceedings{wang2024mathshepherd,
345	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
346	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
347	  booktitle = {ACL 2024},
348	  year = {2024},
349	  url = {https://arxiv.org/abs/2312.08935}
350	}
351	
352	@inproceedings{wang2025rankedvoting,
353	  title = {Ranked Voting based Self-Consistency of Large Language Models},
354	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
355	  booktitle = {ACL Findings 2025},
356	  year = {2025},
357	  url = {https://arxiv.org/abs/2505.10772}
358	}
359	
360	@article{wen2025know,
361	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
362	  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},
363	  journal = {Transactions of the Association for Computational Linguistics},
364	  year = {2025},
365	  doi = {10.1162/tacl_a_00754},
366	  url = {http://dx.doi.org/10.1162/tacl_a_00754}
367	}
368	
369	@article{willard2023guided,
370	  title = {Efficient Guided Generation for Large Language Models},
371	  author = {Willard, Brandon T. and Louf, Rémi},
372	  journal = {arXiv preprint arXiv:2307.09702},
373	  year = {2023},
374	  url = {https://arxiv.org/abs/2307.09702}
375	}
376	
377	@inproceedings{xia2025survey,
378	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
379	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
380	  booktitle = {ACL Findings 2025},
381	  year = {2025},
382	  url = {https://aclanthology.org/2025.findings-acl.1101/}
383	}
384	
385	@article{xiao2019uncertainty,
386	  title = {Quantifying Uncertainties in Natural Language Processing Tasks},
387	  author = {Xiao, Yijun and Wang, William Yang},
388	  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
389	  year = {2019},
390	  doi = {10.1609/aaai.v33i01.33017322},
391	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
392	}
393	
394	@inproceedings{zhang2023ener,
395	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
396	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
397	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
398	  year = {2023},
399	  doi = {10.18653/v1/2023.findings-acl.103},
400	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
401	}
402	
403	@inproceedings{zhou2024uniner,
404	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
405	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
406	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
407	  year = {2024},
408	  url = {https://arxiv.org/abs/2308.03279}
409	}
410	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "a4bb4a7b-76c1-49a1-a081-7334482532ab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@article{li2025llms,\n  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},\n  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},\n  journal = {arXiv preprint arXiv:2503.04104},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.04104}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n",
      "numLines": 410,
      "startLine": 1,
      "totalLines": 410
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_0179unaVY631eMv3YMoyfqQQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "f44ad330-40bd-460f-b5a9-c425f275c157",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwJF4i77qm8SWoq14ZsnKp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 39269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 32 · 2026-05-15T03:18:24.715Z_

<details><summary>↩ Tool result · `toolu_0179unaVY631eMv3YMoyfqQQ`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
15	Our Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Several surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic} for LLMs.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \textit{structure}.
22	Modern neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.
23	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.
24	Prior NER uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn per-sample scoring from labeled data.
26	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\ sample selection for generative IE.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "b5841cf8-18bf-4de3-9248-99d1cf2f2b42",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nHowever, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.\nOur Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSeveral surveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \\cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \\textit{structure}.\nModern neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.\nPrior NER uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring from labeled data.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\\ sample selection for generative IE.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
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
Now I have read all the paper sections. Let me also check the artifacts directory for the bootstrap CI tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "d6312191-25b1-4626-8537-a89565dbb178",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015EGP5PQXz2NiDtADhYqG7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9831,
      "cache_read_input_tokens": 39791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9831
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

Let me check the bootstrap CI artifact and verify all cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "c4ed83b4-8066-47a3-932e-5e3142fea1db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015EGP5PQXz2NiDtADhYqG7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9831,
      "cache_read_input_tokens": 39791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9831
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

<details open><summary>🔧 Tool call — Glob · `toolu_012uLeyqVMREpEAbafj9fCpN`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "a63c116f-5e9e-4cb1-8c0a-75a1f3525202",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015EGP5PQXz2NiDtADhYqG7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9831,
      "cache_read_input_tokens": 39791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9831
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

_source line 36 · 2026-05-15T03:18:30.098Z_

<details><summary>↩ Tool result · `toolu_012uLeyqVMREpEAbafj9fCpN`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "5742f3ac-43cd-4c89-a28e-b143bed2d07d",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T093336/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/worst/paper.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/dream_reports/dream_20260514T203201/best/paper.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T203201/worst/paper.tex",
      "artifacts/bootstrap_ci_tables.tex"
    ],
    "durationMs": 8,
    "numFiles": 17,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rfpuiu9ZXYKkJ6zyG8Reho`</summary>

```json
{
  "pattern": "\\\\ref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "b444997d-17f0-4f21-a123-871280220978",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015EGP5PQXz2NiDtADhYqG7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9831,
      "cache_read_input_tokens": 39791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9831
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

_source line 38 · 2026-05-15T03:18:31.676Z_

<details><summary>↩ Tool result · `toolu_01Rfpuiu9ZXYKkJ6zyG8Reho`</summary>

```text
docs/paper/sections/related_work.tex:15:Our Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
docs/paper/sections/experiments.tex:15:We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
docs/paper/sections/experiments.tex:58:Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
docs/paper/sections/experiments.tex:76:On WNUT-17, where 54\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
docs/paper/sections/experiments.tex:80:Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
docs/paper/sections/experiments.tex:83:This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
docs/paper/sections/experiments.tex:118:Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
docs/paper/sections/experiments.tex:137:Consistency-based signals (SJ, Voting, FK) show robust performance across $T{\in}\{0.7, 1.0\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
docs/paper/sections/experiments.tex:141:NER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).
docs/paper/sections/discussion.tex:4:For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
docs/paper/sections/discussion.tex:5:When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
docs/paper/sections/discussion.tex:13:The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
docs/paper/sections/discussion.tex:16:We observe a notable $\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\ref{app:additional} for details).
docs/paper/sections/discussion.tex:23:Mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.39$; RE: $\rho{=}0.33$; Figure~\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.
docs/paper/sections/discussion.tex:24:NER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.
docs/paper/sections/discussion.tex:32:Further $N$-scaling analysis (Appendix~\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.
docs/paper/sections/method.tex:12:Notation is summarized in Appendix~\ref{app:notation}.
docs/paper/sections/method.tex:69:High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
docs/paper/sections/appendix.tex:3:Table~\ref{tab:notation} summarizes the notation used throughout the paper.
docs/paper/sections/appendix.tex:77:LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
docs/paper/sections/appendix.tex:84:On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
docs/paper/sections/appendix.tex:116:Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
docs/paper/sections/appendix.tex:138:Table~\ref{tab:wnut} reports all five signals on WNUT-17.
docs/paper/sections/appendix.tex:162:Table~\ref{tab:cross_selection} extends the correlation-selection gap analysis across all six tested configurations.
docs/paper/sections/appendix.tex:185:Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
docs/paper/sections/introduction.tex:22:We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): instance-level signals predict \textit{which inputs} are hard, not \textit{which output} is best.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "8d2be4e3-22e9-4c9e-94ca-1a9b28917865",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:15:Our Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\ndocs/paper/sections/experiments.tex:15:We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\ndocs/paper/sections/experiments.tex:58:Table~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\ndocs/paper/sections/experiments.tex:76:On WNUT-17, where 54\\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\ndocs/paper/sections/experiments.tex:80:Filtering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\ndocs/paper/sections/experiments.tex:83:This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\ndocs/paper/sections/experiments.tex:118:Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\ndocs/paper/sections/experiments.tex:137:Consistency-based signals (SJ, Voting, FK) show robust performance across $T{\\in}\\{0.7, 1.0\\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\ndocs/paper/sections/experiments.tex:141:NER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).\ndocs/paper/sections/discussion.tex:4:For per-instance quality ranking, entity voting provides the strongest rank correlation ($\\rho{=}0.38$, Table~\\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).\ndocs/paper/sections/discussion.tex:5:When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}).\ndocs/paper/sections/discussion.tex:13:The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\\S\\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\\ref{tab:selection}) shows this conversion adds no reliable value.\ndocs/paper/sections/discussion.tex:16:We observe a notable $\\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\\ref{app:additional} for details).\ndocs/paper/sections/discussion.tex:23:Mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.39$; RE: $\\rho{=}0.33$; Figure~\\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.\ndocs/paper/sections/discussion.tex:24:NER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.\ndocs/paper/sections/discussion.tex:32:Further $N$-scaling analysis (Appendix~\\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.\ndocs/paper/sections/method.tex:12:Notation is summarized in Appendix~\\ref{app:notation}.\ndocs/paper/sections/method.tex:69:High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\ndocs/paper/sections/appendix.tex:3:Table~\\ref{tab:notation} summarizes the notation used throughout the paper.\ndocs/paper/sections/appendix.tex:77:LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\ndocs/paper/sections/appendix.tex:84:On CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\ndocs/paper/sections/appendix.tex:116:Figure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\ndocs/paper/sections/appendix.tex:138:Table~\\ref{tab:wnut} reports all five signals on WNUT-17.\ndocs/paper/sections/appendix.tex:162:Table~\\ref{tab:cross_selection} extends the correlation-selection gap analysis across all six tested configurations.\ndocs/paper/sections/appendix.tex:185:Our $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\ndocs/paper/sections/introduction.tex:22:We term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): instance-level signals predict \\textit{which inputs} are hard, not \\textit{which output} is best.",
    "numLines": 26
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Grep · `toolu_01BhhAcmznoLVo8qZ6fhDzr4`</summary>

```json
{
  "pattern": "\\\\label\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "5e66c314-2a95-4ecf-becc-1db635df1536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015EGP5PQXz2NiDtADhYqG7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9831,
      "cache_read_input_tokens": 39791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9831
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

_source line 40 · 2026-05-15T03:18:32.369Z_

<details><summary>↩ Tool result · `toolu_01BhhAcmznoLVo8qZ6fhDzr4`</summary>

```text
docs/paper/sections/related_work.tex:1:\section{Related Work}\label{sec:related}
docs/paper/sections/experiments.tex:2:\label{sec:experiments}
docs/paper/sections/experiments.tex:5:\label{sec:setup}
docs/paper/sections/experiments.tex:21:\label{sec:qe_results}
docs/paper/sections/experiments.tex:27:\label{tab:quality_estimation}
docs/paper/sections/experiments.tex:55:\label{fig:signal_heatmap}
docs/paper/sections/experiments.tex:87:\label{sec:selection_gap}
docs/paper/sections/experiments.tex:93:\label{fig:selection_gap}
docs/paper/sections/experiments.tex:100:\label{tab:selection}
docs/paper/sections/experiments.tex:135:\label{sec:robustness_main}
docs/paper/sections/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/sections/discussion.tex:1:\section{Discussion}\label{sec:discussion}
docs/paper/sections/method.tex:1:\section{Method}\label{sec:method}
docs/paper/sections/method.tex:3:\subsection{Problem Formulation}\label{sec:formulation}
docs/paper/sections/method.tex:14:\subsection{Confidence Signals}\label{sec:signals}
docs/paper/sections/method.tex:21:\begin{equation}\label{eq:logprob}
docs/paper/sections/method.tex:27:\begin{equation}\label{eq:em}
docs/paper/sections/method.tex:33:\begin{equation}\label{eq:fk}
docs/paper/sections/method.tex:42:\begin{equation}\label{eq:sj}
docs/paper/sections/method.tex:47:\begin{equation}\label{eq:sj_instance}
docs/paper/sections/method.tex:54:\begin{equation}\label{eq:voting}
docs/paper/sections/method.tex:58:\subsection{Evaluation Framework}\label{sec:evaluation}
docs/paper/sections/appendix.tex:1:\section{Notation}\label{app:notation}
docs/paper/sections/appendix.tex:26:\label{tab:notation}
docs/paper/sections/appendix.tex:29:\section{Robustness Analysis}\label{app:robustness}
docs/paper/sections/appendix.tex:35:\label{tab:robustness}
docs/paper/sections/appendix.tex:66:\label{fig:temperature_robustness}
docs/paper/sections/appendix.tex:87:\section{Calibration Analysis}\label{app:calibration}
docs/paper/sections/appendix.tex:93:\label{fig:reliability}
docs/paper/sections/appendix.tex:98:\section{Additional Analyses}\label{app:additional}
docs/paper/sections/appendix.tex:122:\label{fig:length_logprob_scatter}
docs/paper/sections/appendix.tex:147:\label{tab:wnut}
docs/paper/sections/appendix.tex:169:\label{tab:cross_selection}
docs/paper/sections/introduction.tex:1:\section{Introduction}\label{sec:introduction}
docs/paper/sections/introduction.tex:28:\label{fig:overview}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "29fa1c96-9a4f-4985-89a3-4eddd622350a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:1:\\section{Related Work}\\label{sec:related}\ndocs/paper/sections/experiments.tex:2:\\label{sec:experiments}\ndocs/paper/sections/experiments.tex:5:\\label{sec:setup}\ndocs/paper/sections/experiments.tex:21:\\label{sec:qe_results}\ndocs/paper/sections/experiments.tex:27:\\label{tab:quality_estimation}\ndocs/paper/sections/experiments.tex:55:\\label{fig:signal_heatmap}\ndocs/paper/sections/experiments.tex:87:\\label{sec:selection_gap}\ndocs/paper/sections/experiments.tex:93:\\label{fig:selection_gap}\ndocs/paper/sections/experiments.tex:100:\\label{tab:selection}\ndocs/paper/sections/experiments.tex:135:\\label{sec:robustness_main}\ndocs/paper/sections/conclusion.tex:1:\\section{Conclusion}\\label{sec:conclusion}\ndocs/paper/sections/discussion.tex:1:\\section{Discussion}\\label{sec:discussion}\ndocs/paper/sections/method.tex:1:\\section{Method}\\label{sec:method}\ndocs/paper/sections/method.tex:3:\\subsection{Problem Formulation}\\label{sec:formulation}\ndocs/paper/sections/method.tex:14:\\subsection{Confidence Signals}\\label{sec:signals}\ndocs/paper/sections/method.tex:21:\\begin{equation}\\label{eq:logprob}\ndocs/paper/sections/method.tex:27:\\begin{equation}\\label{eq:em}\ndocs/paper/sections/method.tex:33:\\begin{equation}\\label{eq:fk}\ndocs/paper/sections/method.tex:42:\\begin{equation}\\label{eq:sj}\ndocs/paper/sections/method.tex:47:\\begin{equation}\\label{eq:sj_instance}\ndocs/paper/sections/method.tex:54:\\begin{equation}\\label{eq:voting}\ndocs/paper/sections/method.tex:58:\\subsection{Evaluation Framework}\\label{sec:evaluation}\ndocs/paper/sections/appendix.tex:1:\\section{Notation}\\label{app:notation}\ndocs/paper/sections/appendix.tex:26:\\label{tab:notation}\ndocs/paper/sections/appendix.tex:29:\\section{Robustness Analysis}\\label{app:robustness}\ndocs/paper/sections/appendix.tex:35:\\label{tab:robustness}\ndocs/paper/sections/appendix.tex:66:\\label{fig:temperature_robustness}\ndocs/paper/sections/appendix.tex:87:\\section{Calibration Analysis}\\label{app:calibration}\ndocs/paper/sections/appendix.tex:93:\\label{fig:reliability}\ndocs/paper/sections/appendix.tex:98:\\section{Additional Analyses}\\label{app:additional}\ndocs/paper/sections/appendix.tex:122:\\label{fig:length_logprob_scatter}\ndocs/paper/sections/appendix.tex:147:\\label{tab:wnut}\ndocs/paper/sections/appendix.tex:169:\\label{tab:cross_selection}\ndocs/paper/sections/introduction.tex:1:\\section{Introduction}\\label{sec:introduction}\ndocs/paper/sections/introduction.tex:28:\\label{fig:overview}",
    "numLines": 35
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the rest of the appendix to see the WNUT and cross_selection tables that I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "92669102-875e-40f2-a014-cfc96bce3c8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JBDgtfvMBNVCvRS1pV6ik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3468,
      "cache_read_input_tokens": 49622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3468
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

Let me read the rest of the appendix that was cut off, specifically the WNUT and cross-selection tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "81ff9de7-f9d9-4432-b456-d87bca15dc68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JBDgtfvMBNVCvRS1pV6ik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3468,
      "cache_read_input_tokens": 49622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3468
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

<details open><summary>🔧 Tool call — Read · `toolu_01JKqkh2L9Kf5KcpJyQekMnq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 125
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "4a533e35-67e5-4f14-bffc-148557f14dcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JBDgtfvMBNVCvRS1pV6ik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3468,
      "cache_read_input_tokens": 49622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3468
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

_source line 44 · 2026-05-15T03:18:36.832Z_

<details><summary>↩ Tool result · `toolu_01JKqkh2L9Kf5KcpJyQekMnq`</summary>

```text
125	\paragraph{Evaluation circularity.}
126	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
127	Evaluation circularity is negligible.
128	
129	\paragraph{Conditional filtering details.}
130	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
131	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while logprob drops to $\rho{=}{-}0.026$.
132	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
133	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
134	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
135	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
136	
137	\paragraph{WNUT-17 full signal analysis.}
138	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
139	Voting achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
140	Logprob shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
141	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$). Full: all 1{,}287 instances; Cond: non-zero F1 only.}
147	\label{tab:wnut}
148	\begin{tabular}{lcccc}
149	\toprule
150	Signal & Full $\rho$ & AUROC & Cond $\rho$ & Cond $p$ \\
151	\midrule
152	Voting  & .724 & .913 & .038 & .49 \\
153	FK      & .125 & .555 & .169 & --- \\
154	SJ      & .089 & .517 & .288 & --- \\
155	EM      & .050 & .487 & .333 & --- \\
156	Logprob & $-$.410 & .219 & .350 & --- \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	\paragraph{Cross-configuration selection analysis.}
162	Table~\ref{tab:cross_selection} extends the correlation-selection gap analysis across all six tested configurations.
163	No signal significantly outperforms greedy decoding in any setting, confirming the gap is not specific to a single model--dataset combination.
164	
165	\begin{table}[t]
166	\centering
167	\small
168	\caption{Best-of-$N$ selection F1 across configurations. $\Delta$ = best signal $-$ greedy. No configuration yields a statistically significant improvement.}
169	\label{tab:cross_selection}
170	\begin{tabular}{lcccl}
171	\toprule
172	Config & Greedy & Best & $\Delta$ & $p$ \\
173	\midrule
174	Qwen SciERC NER $N{=}8$ & .644 & .650 & +.006 & .39 \\
175	Qwen SciERC RE $N{=}8$ & .404 & .410 & +.006 & --- \\
176	LLaMA SciERC NER $N{=}8$ & .646 & .652 & +.006 & .39 \\
177	LLaMA SciERC NER $N{=}16$ & .645 & .649 & +.005 & n.s. \\
178	Qwen CoNLL $N{=}8$ & .908 & --- & $<$0 & $<$.001 \\
179	LLaMA CoNLL $N{=}8$ & .924 & --- & $|\Delta|{<}$.001 & n.s. \\
180	\bottomrule
181	\end{tabular}
182	\end{table}
183	
184	\paragraph{Diminishing returns of $N$-scaling.}
185	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
186	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
187	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
188	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ logprob $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.
189	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
190	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
191	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "cbde5f0e-a8ad-44c9-9bf2-37eed30960dc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while logprob drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVoting achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLogprob shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$). Full: all 1{,}287 instances; Cond: non-zero F1 only.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Full $\\rho$ & AUROC & Cond $\\rho$ & Cond $p$ \\\\\n\\midrule\nVoting  & .724 & .913 & .038 & .49 \\\\\nFK      & .125 & .555 & .169 & --- \\\\\nSJ      & .089 & .517 & .288 & --- \\\\\nEM      & .050 & .487 & .333 & --- \\\\\nLogprob & $-$.410 & .219 & .350 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the correlation-selection gap analysis across all six tested configurations.\nNo signal significantly outperforms greedy decoding in any setting, confirming the gap is not specific to a single model--dataset combination.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations. $\\Delta$ = best signal $-$ greedy. No configuration yields a statistically significant improvement.}\n\\label{tab:cross_selection}\n\\begin{tabular}{lcccl}\n\\toprule\nConfig & Greedy & Best & $\\Delta$ & $p$ \\\\\n\\midrule\nQwen SciERC NER $N{=}8$ & .644 & .650 & +.006 & .39 \\\\\nQwen SciERC RE $N{=}8$ & .404 & .410 & +.006 & --- \\\\\nLLaMA SciERC NER $N{=}8$ & .646 & .652 & +.006 & .39 \\\\\nLLaMA SciERC NER $N{=}16$ & .645 & .649 & +.005 & n.s. \\\\\nQwen CoNLL $N{=}8$ & .908 & --- & $<$0 & $<$.001 \\\\\nLLaMA CoNLL $N{=}8$ & .924 & --- & $|\\Delta|{<}$.001 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ logprob $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n",
      "numLines": 67,
      "startLine": 125,
      "totalLines": 191
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
Now I have all the content. Let me also check citations used vs bib entries.

Let me now do a comprehensive analysis. I'll compile all findings systematically.

### 1. Numerical Consistency

Let me trace each key number through the paper:

**SciERC NER: SJ ρ=0.360, Voting ρ=0.379**
- Abstract: ρ=0.38 (entity voting) ✓ (rounded from 0.379)
- Introduction line 20: ρ=0.38 ✓ (rounded)
- Introduction line 37: ρ=0.38 ✓


- Introduction line 41: ρ up to 0.38 ✓
- Table (experiments.tex line 35-36): Voting .379, SJ .360 ✓
- Experiments line 61: Voting ρ=0.379, SJ ρ=0.360 ✓
- Discussion line 4: ρ=0.38 ✓ (rounded)
- Conclusion line 8: ρ=0.38 ✓ (rounded)
- Related work line 10: ρ=0.38 ✓

Now checking the EM AUROC values across all sections...

the abstract rounds 0.749 to 0.75, and I'm seeing this same value consistently reported in the introduction, table, and experiments sections, with the discussion keeping the full precision at 0.749. For the logprob correlation, I'm verifying the ρ=0.205 value appears in the table and experiments line.

Now I'm checking the selection metrics for logprob NER—the oracle score of 0.776 is substantially higher than greedy at 0.644, a difference of 13.2 percentage points, while logprob itself scores 0.650, only 0.6 pp above greedy with a p-value of 0.39 indicating no statistical significance. I'm confirming these values across the table, experiments section, and abstract.

Moving to WNUT-17, I'm verifying the voting approach achieves a correlation of 0.724 with an AUROC of 0.913, while conditional voting drops to 0.038, and checking these numbers against the appendix tables. I'm confirming that SJ achieves ρ=0.089 with p=0.020 on the full WNUT set, which matches what's reported across the experiments section and discussion—the p-value isn't displayed in the table but that's consistent with the findings.

Now I'm checking the N=16 3-seed results: SJ 0.463±0.007, FK 0.455±0.006, and EM 0.460±0.008 appear consistently in both the quality estimation table and the robustness table in the appendix, so those numbers check out.

For the bootstrap confidence interval showing SJ−logprob with Δρ=+0.1547 [+0.0737, +0.2340], I'm searching through the paper to verify this appears somewhere, but I'm not finding this exact CI mentioned in the text—though the paper does discuss the structural-over-logprob advantage with various Δρ values, including references to the LLaMA CoNLL 3-seed comparison.

Looking at the length-logprob correlations, the discussion rounds the values to ρ=0.39 for NER and ρ=0.33 for RE, while the appendix shows the more precise measurements of ρ=0.386 and ρ=0.326 respectively.

Now I'm checking the claim about structural signals dominating across the paper.  Looking at the correlation values: the structural signals (ERC NER Voting at 0.379 and SJ at 0.360) both outperform the surface signals (EM at 0.295 and FK at 0.267), which supports the claim across all four settings. For the selection-performance gap, the paper consistently frames this as a null result—no signal reliably surpasses greedy selection, with p=0.39, and the language avoids claiming significance anywhere.

Now I'm checking the RE selection results more carefully. The log-prob signal actually underperforms greedy on RE (0.395 vs 0.404), but the cross-selection table shows a "Best" value of 0.410 for Qwen SciERC RE at N=8, which I need to trace back to see which signal achieves that. Looking at the cross-selection table more carefully, it seems "Best" refers to the best signal-based selection performance, which shows 0.410 for RE. But the main selection table reports Log-prob RE at 0.395 — these don't match, suggesting either different signals were used or there's a calculation difference I'm missing. The conclusion mentions "RE: −0.9 pp" which would be 0.404 minus 0.009, but that still doesn't explain the 0.410 discrepancy. Looking at the main selection table for RE, Log-prob achieves 0.395 compared to Greedy's 0.404, which is a −0.9 pp difference that matches the conclusion. But the cross-selection table shows a Best of 0.410 with Δ=+0.006 for the same metric, which is contradictory—either the cross-selection table is using different data or there's an error in one of these comparisons. I'm noticing a fundamental inconsistency across these tables—the main selection table shows Log-prob at 0.395 for RE, but the cross-selection table claims Best at 0.410, and the conclusion states −0.9 pp, which doesn't align with either value. If 0.410 is correct, the delta should be +0.006 against the greedy baseline of 0.404, not negative. One of these sources has to be wrong, or they're using different definitions of what counts as "best."

But wait, I'm re-reading the experiments section and it explicitly states no signal exceeds greedy at 0.404 on RE—yet the cross-selection table shows 0.410, which contradicts that directly. This is a critical error somewhere in the tables.

Let me verify the oracle headroom math: NER checks out at 13.2 pp, and RE at 18.1 pp, which matches what's mentioned in the abstract, so at least those calculations are consistent.

Now I'm tracking down the ρ-AUROC dissociation claim—EM leads in AUROC at 0.749 but ranks third in ρ at 0.295, which the discussion confirms. But I can't find any mention of an ensemble AUROC of 0.666 anywhere in the paper, so that claim seems unsupported.

Moving on to check how the paper frames WNUT-17 as a capability boundary rather than a method failure—it's consistently referenced across the introduction, experiments, and conclusion as a limitation tied to insufficient model capability.

Now I need to verify all the cross-references in the paper by matching the defined labels against their usage. I'm checking the reference to tab:wnut in the experiments section—line 76 mentions it in the context of WNUT-17 results, but looking more carefully at the actual text, there's no explicit table reference there, just the correlation statistics embedded in the narrative. The line wrapping was just throwing me off—the grep confirmed the reference exists. Now I'm systematically verifying all the cross-references throughout the document, checking that each label is properly defined. Most of them are checking out so far.

Moving on to citations now, I'm collecting all the citation keys used in the paper and matching them against what's in the bibliography file to make sure everything cited actually exists in the bib file. Continuing through the bibliography, checking off more papers on uncertainty quantification, calibration methods, and verification approaches in language models.

Now I'm verifying that all six equations in the method section are properly defined—the log probability, EM formulation, and various scoring functions including the Hungarian algorithm-based SJ metric. The equations are labeled consistently throughout, even though they're referenced descriptively rather than with explicit equation references, which is stylistically acceptable.

I'm also checking the distinction between how similarity is computed internally versus how evaluation metrics are calculated. The method uses token-level IoU for the SJ confidence signal, which allows approximate matching, while the actual F1 evaluation uses exact span matching for NER tasks. This separation is intentional and clearly justified.

Finally, I'm confirming that all the key claims from the abstract are substantiated in the paper—the dominance of structural signals on harder tasks, the dissociation between ranking and classification performance, the gap between correlation and selection gains, and the boundary effects observed in WNUT-17 when model capability is limited.

Now I'm verifying that the conclusion properly addresses the main findings: the effectiveness of quality estimation, the correlation-selection gap, and how task complexity influences which signals matter most. The limitations section is also appropriately transparent about the constraints—single RE dataset, only two model families tested, no trained verifier, and limited sample sizes of N=8 and N=16.

I'm checking for any reference to exp_012 or 512 truncation in the paper, but I don't see either mentioned.  The paper consistently uses N=8 and N=16 at T=1.0, and without access to the actual experiment artifacts, I can't determine if the data comes from _rerun_1024 experiments. From what's visible in the text, there's no explicit contamination. The selection claims also check out—the paper avoids overstating results and reports non-significant p-values appropriately. I don't find any ensemble AUROC discussion either, so that's not an issue.

But I'm noticing a critical inconsistency in the cross-selection table in the appendix: the Qwen SciERC RE results at N=8 show conflicting information that needs to be resolved. = .410, Δ=+.006
   - tab:selection (experiments line 107-112): Best RE signal is Log-prob at 0.395
   - Experiments line 125: "On RE, the gap is complete: no signal exceeds greedy (0.404)"
   - Conclusion line 9: "RE: −0.9 pp"
   
   The main text consistently says the best signal on RE (0.395) is BELOW greedy (0.404), giving −0.9 pp. But the cross-selection table shows Best = 0.410, Δ=+0.006. These are contradictory.

2. **WARNING: WNUT conditional voting p-value**
   - Experiments line 76: "conditional ρ=0.038, n.s." — says non-significant
   - WNUT table (appendix line 152): Cond p = .49
   - The task says to check "SJ ρ=0.089 (p=0.020)" — this appears in experiments line 77 ✓

Now I'm looking at the voting results more carefully. The full-set SJ correlation of ρ=0.089 with p=0.020 is actually statistically significant despite the small effect size, which makes sense — the p-value reflects the full dataset while the correlation coefficient itself is just weak. .089. ✓

Now I'm verifying the Voting RE full-set correlation of 0.350 against the quality estimation table, which checks out. ✓

For Logprob RE on the conditional set, the experiments section mentions it collapses to ρ=0.011, and I'm cross-referencing this with the signal heatmap figure caption which discusses EM emerging as the strongest signal for both NER and RE on the conditional set.

I'm also checking the N=16 Qwen SciERC improvement claim of +0.052 across multiple locations—the robustness table shows the jump from 0.360 to 0.412, the limitations section repeats this figure, and the appendix confirms it as well. ✓

For the bootstrap test, the experiments section mentions B=10,000 resamples over n=529 NER instances, but SciERC has 551 test instances total. The discrepancy of 22 instances could mean some were filtered out—perhaps those with empty outputs or missing NER entities—which seems reasonable as long as it's applied consistently.

Now I'm looking at the figure overview section...

the caption reports ρ≈0.38 and AUROC≈0.69, which match the Voting method's results (ρ=0.379, AUROC=0.684) rather than EM's higher scores. The caption explicitly specifies "entity voting," so it's correctly reporting Voting's metrics, not EM's.

Now I'm verifying several other claims: the test set has 3,453 sentences, the RE oracle-to-greedy gap is about 18.1 percentage points (fitting within the stated 13-18 pp range), 54% of instances have zero F1, and the CoNLL greedy F1 exceeds 91%.

Looking at the cross-selection results, I notice Qwen achieves 0.908 on CoNLL greedy while LLaMA reaches 0.924—so the claim that models achieve >91% micro F1 doesn't hold for Qwen (90.8%), though it does for LLaMA (92.4%). This suggests the statement should be qualified or adjusted to ">90%". So 0.908 is actually 90.8%, which means the ">91%" claim is technically inaccurate for Qwen, though it's close enough that it might not be a major issue. Let me flag this as a warning but keep in mind the greedy F1 scores might be computed differently than the standard evaluation metrics.

Now I'm checking the SJ correlation coefficient claim in line 77 against what's stated in the intro.  The introduction doesn't explicitly mention SJ's ρ=0.089 value—it only appears in the experiments section, so that's consistent. But I'm noticing a potential issue with the robustness table: the N=16 SJ result for Qwen on SciERC NER shows 0.412 as the mean across 3 seeds, with individual values of 0.428, 0.424, and 0.384. Let me verify that arithmetic.

The sum is 1.236, which divided by 3 gives 0.412, so that checks out. However, I'm seeing different N=16 numbers in the quality estimation table—those report SJ at .463±.007 for LLaMA on CoNLL, which is a different dataset entirely. So these aren't contradictory; they're just measuring different model-dataset combinations.

Now I'm verifying the cross-model section in the appendix robustness table for LLaMA on CoNLL with N=16, and those values match the quality estimation table exactly. Then I'm checking the signal heatmap caption, which reports EM as the strongest signal with correlations of 0.360 for NER and 0.417 for RE.

These same correlation values appear consistently across the experiments section, discussion, and appendix. I'm also verifying the RE oracle calculation—the selection table shows 0.585, and subtracting the current performance of 0.404 gives 0.181, which matches the "18.1 pp of oracle headroom" mentioned in the experiments.

For the sign test, I'm checking the math: 61 wins out of 131 total comparisons (wins plus losses) gives 46.6%, which checks out. The remaining 398 instances are ties, accounting for about 75% of all comparisons, which aligns with what's stated in the discussion.

Now I'm looking at the appendix WNUT table to verify the conditional p-value for Voting.

The appendix shows p=0.49 for the conditional correlation, and the experiments section confirms this is non-significant with ρ=0.038. Both sources are consistent.

For the SJ values, the task reports ρ=0.089 with p=0.020, which matches what I'm seeing in the experiments text and the WNUT table.

Now I'm re-examining the cross-selection table more carefully to check those delta values and p-values... I'm noticing a direct contradiction between two tables in the results. The main selection table shows greedy achieving 0.404 on RE, outperforming all signal-based methods, which aligns with the text stating no signal exceeds greedy. But the cross-selection table reports a best RE score of 0.410 with a +0.006 improvement, suggesting a signal method did beat greedy—these findings are incompatible.

Looking at the conclusion's notation of "RE: −0.9 pp," this calculates to 0.395, matching the Log-prob result in the main table, not the 0.410 from cross-selection. I'm wondering if the cross-selection table might include a different signal method not shown in the main selection table, like FK, which could explain the discrepancy. The difference is −0.009, which matches the −0.9 pp reported in the conclusion, so that's internally consistent. The cross-selection table remains the anomaly—that 0.410 value doesn't appear anywhere in the main selection table. Now I'm spot-checking the terminology consistency across sections: the three families (structural, surface, model-internal) and five signals are labeled the same way throughout the abstract, introduction, and methods.

I'm also verifying the experimental details like the LoRA configuration, epoch count, and temperature settings are all consistent where mentioned. The equations for log-probability and entity matching look correct as well.

Now I'm checking whether the correlation values reported between entity voting and soft Jaccard are consistent with what would be expected from the diagnostic analysis, and I'm starting to trace through the quality estimation results to verify the Qwen CoNLL numbers line up properly. ρ=.424, SJ ρ=.436, FK ρ=.400, EM ρ=.451, Logprob ρ=.316

Experiments line 72: "EM leads (ρ=0.451, AUROC=0.816)" on CoNLL. Table confirms EM ρ=.451, AUROC=.816 ✓

Experiments line 75: "SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL"
Table: CoNLL Qwen SJ=.436, CoNLL LLaMA SJ=.431 ✓

Now the claim about CoNLL >91%: Qwen CoNLL greedy = .908 (cross-selection table).

Looking at the >91% claim more carefully—0.908 falls short, but LLaMA hits 0.924, so the plural "models" is technically accurate even if misleading. The parenthetical in line 72 specifically references greedy F1, though there's a possibility the >91% claim refers to standard CoNLL evaluation rather than the selection pipeline metrics, which would resolve the discrepancy.

The cross-selection table also shows Qwen CoNLL has no positive selection result—the best signal is significantly worse than greedy (p < .001), while LLaMA shows no significant difference. I'll mark the >91% claim as a minor issue since 0.908 is close enough to round to 0.91.

Let me verify the discussion section uses the correct rounded correlation values before finalizing the report. I need to verify the bootstrap confidence interval for the SJ-logprob comparison. The checklist mentions a specific CI of [+0.0737, +0.2340], but I'm not finding that exact range in the paper—I see the delta values reported differently across sections, with +0.153 appearing in the appendix for the LLaMA CoNLL setting, which is close to the +0.1547 in the checklist.

Now I'm checking the oracle headroom calculations mentioned throughout the paper. The NER gap checks out at 13.2 percentage points, and the RE gap is 18.1 percentage points, which aligns with the "13-18 pp of oracle headroom" stated in the abstract, introduction, and conclusion.

Looking at the cross-selection table though, I notice the other configurations like LLaMA on SciERC show different greedy scores, so the 13-18 pp range is specific to the Qwen SciERC setup rather than a universal claim.

I've identified two issues so far: a critical contradiction in the cross-selection table's RE row that conflicts with the main results and text claims, and a warning about the CoNLL ">91%" claim not holding for Qwen's greedy performance at 90.8%.

Now examining the selection table more carefully—the caption explains why EM shows "---" since it produces binary agreement without sample ranking, which makes sense. But I'm noticing FK (Fleiss' κ) is conspicuously absent from the table even though it could theoretically be converted to a per-sample selector like SJ and Voting, and if it achieves around 0.410 on RE, that's worth flagging.

The methods section clarifies that consensus-proximity applies to all instance-level signals (SJ, Voting, FK, EM), with EM unable to discriminate due to its binary nature. So FK should appear in the main selection table alongside SJ and Voting, but it doesn't—yet it seems to show up in the cross-selection table as 0.410, which creates an inconsistency with the claim that "no signal exceeds greedy."

Given that the main text, primary table, and conclusion all consistently state no signal beats greedy on RE, the cross-selection table's FK value of 0.410 is probably the error. But before finalizing the report, I should verify whether FK is even suitable for selection—it measures inter-sample agreement, not per-sample proximity scores like SJ does, so using it for instance-level selection might not be straightforward.

That absence from both tables makes sense if FK isn't naturally convertible to a selector. But then where does that 0.410 come from? It doesn't match Log-prob, SJ, or Voting. I'm wondering if the cross-selection table might be using a different approach entirely—perhaps a consensus output method where we pick the most frequently occurring output rather than the closest sample.

Now I need to verify the figure references are actually present in the figures directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "2cf386b0-d298-413f-868b-04fe68df5f60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDgvLyeXqyM8DvKupWhxEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 53090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2188
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

Let me verify figures exist and check a couple more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "8608d334-8326-4d6f-a8d2-3cba2f8b3834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDgvLyeXqyM8DvKupWhxEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 53090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2188
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

<details open><summary>🔧 Tool call — Glob · `toolu_01XjxaxHWaCkLZt7B9y6eG5U`</summary>

```json
{
  "pattern": "fig*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "82f457db-7a18-4b62-85ea-88618629e2f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDgvLyeXqyM8DvKupWhxEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 53090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2188
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

_source line 48 · 2026-05-15T03:23:06.900Z_

<details><summary>↩ Tool result · `toolu_01XjxaxHWaCkLZt7B9y6eG5U`</summary>

```text
docs/paper/figures/fig_overview.pdf
docs/paper/figures/fig_reliability.pdf
docs/paper/figures/fig_signal_heatmap.pdf
docs/paper/figures/fig_selection_gap.pdf
docs/paper/figures/fig_temperature_robustness.pdf
docs/paper/figures/fig_length_logprob_scatter.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "895d1911-7821-45f7-8ff5-8b4db2f6d438",
  "tool_use_result": {
    "filenames": [
      "docs/paper/figures/fig_overview.pdf",
      "docs/paper/figures/fig_reliability.pdf",
      "docs/paper/figures/fig_signal_heatmap.pdf",
      "docs/paper/figures/fig_selection_gap.pdf",
      "docs/paper/figures/fig_temperature_robustness.pdf",
      "docs/paper/figures/fig_length_logprob_scatter.pdf"
    ],
    "durationMs": 10,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Grep · `toolu_01Wd9JwKkoED35ywyuS63n4C`</summary>

```json
{
  "pattern": "\\\\cite(alp)?\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "261e1892-0c50-47b0-a551-020918cfc2e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDgvLyeXqyM8DvKupWhxEi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 53090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2188
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

_source line 50 · 2026-05-15T03:23:08.080Z_

<details><summary>↩ Tool result · `toolu_01Wd9JwKkoED35ywyuS63n4C`</summary>

```text
docs/paper/sections/related_work.tex:4:Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
docs/paper/sections/related_work.tex:5:Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
docs/paper/sections/related_work.tex:7:Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
docs/paper/sections/related_work.tex:16:CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
docs/paper/sections/related_work.tex:17:Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
docs/paper/sections/related_work.tex:20:Several surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic} for LLMs.
docs/paper/sections/related_work.tex:21:Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \textit{structure}.
docs/paper/sections/related_work.tex:22:Modern neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.
docs/paper/sections/related_work.tex:23:Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.
docs/paper/sections/related_work.tex:24:Prior NER uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.
docs/paper/sections/related_work.tex:25:Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn per-sample scoring from labeled data.
docs/paper/sections/related_work.tex:26:Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\ sample selection for generative IE.
docs/paper/sections/experiments.tex:9:\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
docs/paper/sections/experiments.tex:10:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
docs/paper/sections/experiments.tex:11:\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
docs/paper/sections/experiments.tex:17:Inference uses vLLM with constrained decoding \cite{willard2023guided}.
docs/paper/sections/experiments.tex:64:While $\rho{=}0.38$ explains approximately 14\% of F1 variance, the corresponding AUROC of 0.749 indicates strong discriminative power for the binary quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For context, semantic entropy achieves AUROC $\approx$ 0.75--0.85 on discrete-answer QA tasks \cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}
docs/paper/sections/experiments.tex:135:This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
docs/paper/sections/discussion.tex:31:Effective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.
docs/paper/sections/method.tex:5:Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
docs/paper/sections/method.tex:41:Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
docs/paper/sections/appendix.tex:185:Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
docs/paper/sections/introduction.tex:4:On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
docs/paper/sections/introduction.tex:5:More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
docs/paper/sections/introduction.tex:15:Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
docs/paper/sections/introduction.tex:31:We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "8d9e91bd-a63a-4eaa-8b30-2697f5561879",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:4:Self-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\ndocs/paper/sections/related_work.tex:5:Extensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\ndocs/paper/sections/related_work.tex:7:Recent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\ndocs/paper/sections/related_work.tex:16:CoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\ndocs/paper/sections/related_work.tex:17:Our evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\ndocs/paper/sections/related_work.tex:20:Several surveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic} for LLMs.\ndocs/paper/sections/related_work.tex:21:Semantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \\cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \\textit{structure}.\ndocs/paper/sections/related_work.tex:22:Modern neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.\ndocs/paper/sections/related_work.tex:23:Deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.\ndocs/paper/sections/related_work.tex:24:Prior NER uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.\ndocs/paper/sections/related_work.tex:25:Conformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring from labeled data.\ndocs/paper/sections/related_work.tex:26:Selective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\\ sample selection for generative IE.\ndocs/paper/sections/experiments.tex:9:\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\ndocs/paper/sections/experiments.tex:10:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\\% micro F1.\ndocs/paper/sections/experiments.tex:11:\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\\% zero F1).\ndocs/paper/sections/experiments.tex:17:Inference uses vLLM with constrained decoding \\cite{willard2023guided}.\ndocs/paper/sections/experiments.tex:64:While $\\rho{=}0.38$ explains approximately 14\\% of F1 variance, the corresponding AUROC of 0.749 indicates strong discriminative power for the binary quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For context, semantic entropy achieves AUROC $\\approx$ 0.75--0.85 on discrete-answer QA tasks \\cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}\ndocs/paper/sections/experiments.tex:135:This gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\ndocs/paper/sections/discussion.tex:31:Effective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.\ndocs/paper/sections/method.tex:5:Given a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\ndocs/paper/sections/method.tex:41:Our core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\ndocs/paper/sections/appendix.tex:185:Our $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\ndocs/paper/sections/introduction.tex:4:On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\ndocs/paper/sections/introduction.tex:5:More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\ndocs/paper/sections/introduction.tex:15:Self-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\ndocs/paper/sections/introduction.tex:31:We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.",
    "numLines": 26
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I also need to check for a footnote in experiments line 64 that I may have missed. Let me also verify that the experiments.tex has a reference to tab:wnut that I thought I saw in grep. Let me re-read experiments line 76 more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "d11c2743-aacf-41c4-9eda-62b2db349ca5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xh2LbK7BiS582vnip4EaK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16833,
      "cache_read_input_tokens": 55278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16833
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

_source line 52_

Let me re-read experiments.tex line 76 precisely to verify a reference I saw in grep output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "811d5685-ab8c-47cd-94e7-14f4dd49135c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xh2LbK7BiS582vnip4EaK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16833,
      "cache_read_input_tokens": 55278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16833
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

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01Q2J2kxxpeVWUGgQfpFwngM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 60,
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
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "d92a679b-b13a-4df4-8016-a3be8fc33a3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xh2LbK7BiS582vnip4EaK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16833,
      "cache_read_input_tokens": 55278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16833
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

_source line 54 · 2026-05-15T03:23:13.706Z_

<details><summary>↩ Tool result · `toolu_01Q2J2kxxpeVWUGgQfpFwngM`</summary>

```text
60	\paragraph{Structural signals dominate on complex schemas.}
61	On SciERC NER, Voting achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and logprob ($\rho{=}0.205$).
62	The structural advantage persists on RE (Voting $\rho{=}0.350$), though all signals weaken due to the 44\% zero-F1 floor effect.
63	Entity voting and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
64	While $\rho{=}0.38$ explains approximately 14\% of F1 variance, the corresponding AUROC of 0.749 indicates strong discriminative power for the binary quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For context, semantic entropy achieves AUROC $\approx$ 0.75--0.85 on discrete-answer QA tasks \cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}
65	Bootstrap CIs for signal pair differences on SciERC NER ($N{=}8$): SJ$-$logprob $\Delta\rho{=}{+}0.155$ [+0.074, +0.234]; Voting$-$SJ $\Delta\rho{=}{+}0.019$ [$-$0.033, +0.073]; SJ$-$EM $\Delta\rho{=}{+}0.065$ [+0.003, +0.130].
66	The SJ advantage over logprob is significant, while the Voting--SJ gap is not; the SJ--EM difference is marginal (CI lower bound +0.003).
67	
68	\paragraph{$\rho$--AUROC dissociation.}
69	On NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\rho$ (0.134).
70	Binary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.
71	On CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307), confirming this dissociation across datasets.
72	
73	\paragraph{Signal rankings shift with task difficulty.}
74	On CoNLL (greedy F1${>}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.
75	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
76	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.
77	Cross-model stability is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
78	On WNUT-17, where 54\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
79	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
80	
81	\paragraph{Conditional filtering.}
82	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
83	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
84	Logprob RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "765f33bc-98d6-40fb-a39f-0d06694a252e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and logprob ($\\rho{=}0.205$).\nThe structural advantage persists on RE (Voting $\\rho{=}0.350$), though all signals weaken due to the 44\\% zero-F1 floor effect.\nEntity voting and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile $\\rho{=}0.38$ explains approximately 14\\% of F1 variance, the corresponding AUROC of 0.749 indicates strong discriminative power for the binary quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For context, semantic entropy achieves AUROC $\\approx$ 0.75--0.85 on discrete-answer QA tasks \\cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}\nBootstrap CIs for signal pair differences on SciERC NER ($N{=}8$): SJ$-$logprob $\\Delta\\rho{=}{+}0.155$ [+0.074, +0.234]; Voting$-$SJ $\\Delta\\rho{=}{+}0.019$ [$-$0.033, +0.073]; SJ$-$EM $\\Delta\\rho{=}{+}0.065$ [+0.003, +0.130].\nThe SJ advantage over logprob is significant, while the Voting--SJ gap is not; the SJ--EM difference is marginal (CI lower bound +0.003).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nOn NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\\rho$ (0.134).\nBinary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.\nOn CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307), confirming this dissociation across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${>}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.\nCross-model stability is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 54\\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLogprob RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.",
      "numLines": 25,
      "startLine": 60,
      "totalLines": 147
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Now I see the bootstrap CIs in experiments line 65:
"SJ−logprob Δρ=+0.155 [+0.074, +0.234]"

The task checklist says: "Bootstrap CI: SJ−logprob Δρ=+0.1547 [+0.0737, +0.2340] significant"

The paper says: Δρ=+0.155 [+0.074, +0.234]

So +0.1547 is rounded to +0.155 ✓ (close, 0.1547 → 0.155 is a rounding at 3 decimal places)


And [+0.0737, +0.2340] → [+0.074, +0.234] ✓ (rounded to 3 decimals)

These are consistent. ✓

Now checking the WNUT conditional set claim from experiments line 79 that says "all signals collapse toward weak or non-significant correlations (ρ≤0.35)" — but looking at the actual WNUT table, I see the conditional correlations are .038, .169, .288, and .333, which means most of them do fall below 0.35, though the EM conditional is right at the boundary.

The logprob conditional at 0.350 technically satisfies ρ≤0.35 since 0.350 equals 0.35, but calling it "weak" is debatable — with n ~590 instances, a correlation of 0.350 could actually be significant, and it reads more as moderate than weak. This feels like a characterization issue rather than a factual error, though the paper's language is a bit generous in describing this pattern. Looking at the variance calculation—if ρ=0.38, that should explain roughly 14% of the F1 variance (since 0.38² ≈ 0.144). Let me verify this math checks out. ✓

Now I'm noticing a potential discrepancy with the Qwen CoNLL result. The cross-selection table shows Qwen achieving 90.8% on CoNLL with greedy selection, but the experiments section claims "greedy F1>0.91" which would be over 91%. That's a gap of about 0.3 percentage points—though the context suggests this statement might be referring to the broader CoNLL signal rankings rather than Qwen specifically. The Qwen model falls slightly short at 90.8%, making the claim that models achieve >91% technically inaccurate for that specific case, though the average across both models does exceed 91%. I'll mark this as a minor issue and move forward with compiling my findings.

I'm seeing a critical contradiction across multiple sections: the cross-selection table reports a best RE value of 0.410 with a delta of +0.006, but this directly conflicts with what the main selection table shows (0.395 as the best signal) and the experiments section's statement that no RE signal exceeds the greedy baseline of 0.404. Let me document all these discrepancies in my final report.

There's also a potential confusion in how the correlation and AUROC metrics are presented—the text mentions ρ=0.38 explaining 14% of variance alongside an AUROC of 0.749, but these appear to come from different methods (Voting and EM respectively), which could mislead readers into thinking they're directly comparable measurements. I'm realizing the ambiguity hinges on what "corresponding" means—whether it refers to the AUROC of the same signal (Voting) or just the best AUROC achieved on that task (EM's). If it's the former, 0.749 is incorrect since Voting's AUROC is 0.684; if it's the latter, the numbers are right but the phrasing misleadingly mixes different signals. Either way, it's a minor clarity issue worth flagging since the sentence reads as though both metrics come from the same source. The "corresponding" phrasing is genuinely ambiguous—readers could easily interpret the ρ=0.38 and AUROC=0.749 as belonging to the same signal when they actually come from different ones, so I should flag this as a warning. Now checking the conclusion's reported numbers: NER logprob shows +0.6 pp and RE shows −0.9 pp, both of which match the main selection table, but I want to verify the context around that RE figure.

Log-prob is indeed the best signal for RE, so the −0.9 pp result is consistent with the paper's narrative. The cross-selection table's RE row claiming a +0.006 improvement contradicts all other evidence, so that's almost certainly where the error lies. Before finalizing the report, I need to double-check the CoNLL greedy F1 baseline to verify the ">91%" claim.

Looking at the cross-selection table, Qwen's greedy micro F1 on CoNLL is 0.908—that's 90.8%, which falls short of 91%. The paper states "where models achieve >91% micro F1" when describing CoNLL-2003, but this phrasing is ambiguous—it could refer to typical performance in the literature rather than specifically our models' results.

Line 74 is clearer: "On CoNLL (greedy F1>0.91)" explicitly references our models' performance, and Qwen's 90.8% doesn't meet that threshold. I'll flag both instances as minor issues since the difference is small and doesn't impact the conclusions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "08acbe1f-b242-47e4-8d54-a9c33206596b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E88scgz5UziBCJE6M4nYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 72111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1477
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

_source line 56_

Now I have all the data needed. Here's the full consistency audit report.

---

## 全文一致性审查报告

### 1. 数值一致性

- [PASS] **SciERC NER Voting ρ=0.379**: Abstract (ρ=0.38 rounded), intro:20 (ρ=0.38), experiments:35 (.379), experiments:61 (0.379), discussion:4 (0.38), conclusion:8 (0.38), related_work:10 (0.38). 所有引用一致。

- [PASS] **SciERC NER SJ ρ=0.360**: experiments:36 (.360), experiments:61 (0.360), appendix:47 (0.360). 一致。

- [PASS] **EM AUROC=0.749**: Abstract (0.75 rounded), intro:20 (0.75), intro:37 (0.75), experiments:38 (.749), experiments:64 (0.749), experiments:67 (0.749), discussion:4 (0.749), discussion:16 (0.749), conclusion:8 (0.75). 一致。

- [PASS] **logprob ρ=0.205**: experiments:39 (.205), experiments:61 (0.205). 一致。

- [PASS] **Selection NER: logprob F1=0.650, greedy=0.644, oracle=0.776, p=0.39**: experiments:105-113 (table), experiments:123-124 (text), conclusion:9 (+0.6 pp, p=0.39). 一致。Oracle headroom 0.776−0.644=0.132=13.2 pp ✓.

- [ISSUE] **Selection RE: cross-selection table 与主表/正文矛盾**
  1. **位置**: `appendix.tex:175` (tab:cross_selection)
  2. **当前内容**: `Qwen SciERC RE N=8 | .404 | .410 | +.006 | ---`
  3. **应该是**: Best ≤ .404, Δ ≤ 0（与主表一致）
  4. **严重程度**: **CRITICAL**
  
  主 selection 表 (`experiments.tex:107-112`) 显示 RE 最佳信号 Log-prob=0.395 < Greedy=0.404。正文 (`experiments.tex:125`) 明确说 "On RE, the gap is complete: no signal exceeds greedy (0.404)"。Conclusion (`conclusion.tex:9`) 写 "RE: −0.9 pp"（0.395−0.404=−0.009）。但 cross-selection 表却显示 Best=.410, Δ=+.006，直接矛盾。

- [PASS] **WNUT-17 voting ρ=0.724, AUROC=0.913, conditional ρ=0.038**: experiments:78, appendix:139, WNUT table (appendix:152). 一致。Conditional p=0.49 标记 "n.s." ✓.

- [PASS] **WNUT-17 SJ ρ=0.089 (p=0.020)**: experiments:79, WNUT table (appendix:154). 一致。

- [PASS] **N=16 3-seed (LLaMA CoNLL)**: SJ .463±.007, FK .455±.006, EM .460±.008, Voting .458±.003, Logprob .310±.005. Quality estimation table (experiments:42-46) = robustness table (appendix:53-57). 完全一致。

- [PASS] **Bootstrap CI SJ−logprob**: experiments:65 报 Δρ=+0.155 [+0.074, +0.234]，与 checklist 值 +0.1547 [+0.0737, +0.2340] 一致（3位小数 rounded）。

- [PASS] **N=16 SJ improvement +0.052**: Robustness table SJ N=8=0.360 → N=16=0.412, Δ=0.052. experiments:139, limitations:12, appendix:75, appendix:186 均为 +0.052。

- [PASS] **Length-logprob correlation**: discussion:23 (NER ρ=0.39, RE ρ=0.33) = appendix:116 (0.386, 0.326) rounded。0.386→0.39 ✓, 0.326→0.33 ✓.

- [PASS] **Oracle headroom 13-18 pp**: NER 13.2 pp, RE 18.1 pp. Abstract, intro:21, intro:41, conclusion:9 均写 "13-18 pp". ✓

### 2. Claim 强度

- [PASS] **"structural signals dominate"**: SciERC NER: Voting(0.379) > SJ(0.360) > EM(0.295) > FK(0.267) > logprob(0.205)。两个 structural 信号均胜过所有其他信号。Bootstrap CI (experiments:65-66) 确认 SJ−logprob 差异显著。N=16 四个设置均成立 (experiments:140, Δρ=+0.135 to +0.175)。Claim 有充分支持。

- [PASS] **"correlation-selection gap" is null result**: 全文一致使用 "no signal reliably surpasses greedy"，p=0.39, 未出现 "significantly outperforms"。

- [PASS] **"ρ-AUROC dissociation"**: experiments:67-69 EM leads AUROC but ranks 3rd/last in ρ. discussion:16 确认。CoNLL logprob AUROC=0.761 but lowest ρ=0.307 (experiments:71) 提供跨数据集验证。

- [ISSUE] **"corresponding AUROC of 0.749" 归属模糊**
  1. **位置**: `experiments.tex:64`
  2. **当前内容**: "While ρ=0.38 explains approximately 14% of F1 variance, the corresponding AUROC of 0.749..."
  3. **应该是**: ρ=0.38 来自 Voting，AUROC=0.749 来自 EM（不同信号）。"corresponding" 暗示同一信号，但 Voting 的 AUROC=0.684。建议改为 "while the best AUROC reaches 0.749 (EM)" 或类似表述以消除歧义。
  4. **严重程度**: **WARNING**

- [PASS] **Ensemble AUROC (0.666) < EM (0.749)**: 论文未提及 ensemble AUROC 0.666，无正面 framing。PASS。

- [PASS] **WNUT-17 as capability boundary**: experiments:79 "suggesting a capability boundary", intro:45 "when model capability is insufficient", conclusion:10 同。一致使用 "boundary" 框架而非 "method failure"。

### 3. 交叉引用完整性

- [PASS] **所有 \ref{} 均有对应 \label{}**: 核查 22 个 \ref 引用，均有对应 label。包括 fig:overview, tab:quality_estimation, tab:selection, tab:robustness, tab:wnut, tab:cross_selection, fig:signal_heatmap, fig:selection_gap, fig:temperature_robustness, fig:reliability, fig:length_logprob_scatter, tab:notation, 以及所有 section/appendix 引用。

- [PASS] **所有 \cite{} 均有 bib 条目**: 核查 48 个 citation key，全部存在于 references.bib。

- [PASS] **所有 figure 文件存在**: figures/ 目录包含 fig_overview.pdf, fig_signal_heatmap.pdf, fig_selection_gap.pdf, fig_temperature_robustness.pdf, fig_reliability.pdf, fig_length_logprob_scatter.pdf。

### 4. 公式一致性

- [PASS] **六个公式均定义于 method.tex**: eq:logprob (L21), eq:em (L27), eq:fk (L33), eq:sj (L42), eq:sj_instance (L47), eq:voting (L54)。

- [PASS] **SJ 定义一致**: method.tex:41-45 定义 Hungarian algorithm + token-level IoU。experiments:16 使用 "exact span matching" 区分评估指标 (F1) 与信号计算 (SJ)，无混淆。

- [PASS] **信号分类一致**: 三族五信号 (structural: Voting, SJ; surface: EM, FK; model-internal: logprob) 在 abstract, intro:31, method:16, conclusion:4 中分类一致。

### 5. 结构完整性

- [PASS] **Abstract 覆盖所有 core findings**:
  - structural > logprob: L6 "structural signals dominate hard tasks" ✓
  - ρ-AUROC dissociation: L4 "ranking and classification favoring different signals" ✓
  - correlation-selection gap: L4-5 "does not translate into selection gains" ✓
  - WNUT-17 boundary: L6 "when model capability is insufficient" ✓

- [PASS] **Conclusion 与 findings 对齐**: 三个 anchor findings (quality estimation, correlation-selection gap, task-complexity boundary) 均有对应段落。

- [PASS] **Limitations 诚实**: 单一 RE 数据集 (L1), 两个模型家族 (L3-5), 无 trained verifier (L8-9), N≤16 (L11), SJ-FK gap on CoNLL only 0.003 (L14), logprob temperature sensitivity uncharacterized (L15)。覆盖全面。

### 6. 已知问题检查

- [PASS] **exp_012 (512 截断) 数据未出现**: 论文中无 512 truncation 或 exp_012 的引用。

- [PASS] **Selection 未写 "significantly outperforms"**: 所有 selection 讨论使用 "not statistically significant", "no signal reliably surpasses", p=0.39。

- [PASS] **Ensemble 未正面 framing**: 论文不讨论 ensemble AUROC。

- [ISSUE] **CoNLL ">91%" claim 对 Qwen 不成立**
  1. **位置**: `experiments.tex:10` 和 `experiments.tex:74`
  2. **当前内容**: L10: "where models achieve >91% micro F1"; L74: "On CoNLL (greedy F1>0.91)"
  3. **应该是**: Qwen CoNLL greedy F1 = 0.908 (90.8%), 不满足 >91%。LLaMA=0.924 满足。建议改为 ">90%" 或 "≈91%" 或 "90.8--92.4%"。
  4. **严重程度**: **MINOR** (0.908 ≈ 0.91, 不影响结论)

---

## 汇总

| 类别 | PASS | ISSUE |
|------|------|-------|
| 数值一致性 | 12 | 1 CRITICAL |
| Claim 强度 | 5 | 1 WARNING |
| 交叉引用 | 3 | 0 |
| 公式一致性 | 3 | 0 |
| 结构完整性 | 3 | 0 |
| 已知问题 | 3 | 1 MINOR |
| **合计** | **29** | **1 CRITICAL, 1 WARNING, 1 MINOR** |

**需修复**:
1. **CRITICAL**: `appendix.tex:175` — cross-selection table RE 行 (Best=.410) 与主表及正文 (Best=.395, Δ=−0.9 pp) 矛盾。需修正为与 tab:selection 一致的值。
2. **WARNING**: `experiments.tex:64` — "corresponding AUROC of 0.749" 暗示与 ρ=0.38 来自同一信号 (Voting)，但实际来自 EM (Voting AUROC=0.684)。
3. **MINOR**: `experiments.tex:10,74` — ">91%" 对 Qwen CoNLL (90.8%) 不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "uuid": "2a7f1cb6-8a2f-432c-96ba-ed1e5711b59b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E88scgz5UziBCJE6M4nYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 72111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1477
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

_source line 57_

Now I have all the data needed. Here's the full consistency audit report.

---

## 全文一致性审查报告

### 1. 数值一致性

- [PASS] **SciERC NER Voting ρ=0.379**: Abstract (ρ=0.38 rounded), intro:20 (ρ=0.38), experiments:35 (.379), experiments:61 (0.379), discussion:4 (0.38), conclusion:8 (0.38), related_work:10 (0.38). 所有引用一致。

- [PASS] **SciERC NER SJ ρ=0.360**: experiments:36 (.360), experiments:61 (0.360), appendix:47 (0.360). 一致。

- [PASS] **EM AUROC=0.749**: Abstract (0.75 rounded), intro:20 (0.75), intro:37 (0.75), experiments:38 (.749), experiments:64 (0.749), experiments:67 (0.749), discussion:4 (0.749), discussion:16 (0.749), conclusion:8 (0.75). 一致。

- [PASS] **logprob ρ=0.205**: experiments:39 (.205), experiments:61 (0.205). 一致。

- [PASS] **Selection NER: logprob F1=0.650, greedy=0.644, oracle=0.776, p=0.39**: experiments:105-113 (table), experiments:123-124 (text), conclusion:9 (+0.6 pp, p=0.39). 一致。Oracle headroom 0.776−0.644=0.132=13.2 pp ✓.

- [ISSUE] **Selection RE: cross-selection table 与主表/正文矛盾**
  1. **位置**: `appendix.tex:175` (tab:cross_selection)
  2. **当前内容**: `Qwen SciERC RE N=8 | .404 | .410 | +.006 | ---`
  3. **应该是**: Best ≤ .404, Δ ≤ 0（与主表一致）
  4. **严重程度**: **CRITICAL**
  
  主 selection 表 (`experiments.tex:107-112`) 显示 RE 最佳信号 Log-prob=0.395 < Greedy=0.404。正文 (`experiments.tex:125`) 明确说 "On RE, the gap is complete: no signal exceeds greedy (0.404)"。Conclusion (`conclusion.tex:9`) 写 "RE: −0.9 pp"（0.395−0.404=−0.009）。但 cross-selection 表却显示 Best=.410, Δ=+.006，直接矛盾。

- [PASS] **WNUT-17 voting ρ=0.724, AUROC=0.913, conditional ρ=0.038**: experiments:78, appendix:139, WNUT table (appendix:152). 一致。Conditional p=0.49 标记 "n.s." ✓.

- [PASS] **WNUT-17 SJ ρ=0.089 (p=0.020)**: experiments:79, WNUT table (appendix:154). 一致。

- [PASS] **N=16 3-seed (LLaMA CoNLL)**: SJ .463±.007, FK .455±.006, EM .460±.008, Voting .458±.003, Logprob .310±.005. Quality estimation table (experiments:42-46) = robustness table (appendix:53-57). 完全一致。

- [PASS] **Bootstrap CI SJ−logprob**: experiments:65 报 Δρ=+0.155 [+0.074, +0.234]，与 checklist 值 +0.1547 [+0.0737, +0.2340] 一致（3位小数 rounded）。

- [PASS] **N=16 SJ improvement +0.052**: Robustness table SJ N=8=0.360 → N=16=0.412, Δ=0.052. experiments:139, limitations:12, appendix:75, appendix:186 均为 +0.052。

- [PASS] **Length-logprob correlation**: discussion:23 (NER ρ=0.39, RE ρ=0.33) = appendix:116 (0.386, 0.326) rounded。0.386→0.39 ✓, 0.326→0.33 ✓.

- [PASS] **Oracle headroom 13-18 pp**: NER 13.2 pp, RE 18.1 pp. Abstract, intro:21, intro:41, conclusion:9 均写 "13-18 pp". ✓

### 2. Claim 强度

- [PASS] **"structural signals dominate"**: SciERC NER: Voting(0.379) > SJ(0.360) > EM(0.295) > FK(0.267) > logprob(0.205)。两个 structural 信号均胜过所有其他信号。Bootstrap CI (experiments:65-66) 确认 SJ−logprob 差异显著。N=16 四个设置均成立 (experiments:140, Δρ=+0.135 to +0.175)。Claim 有充分支持。

- [PASS] **"correlation-selection gap" is null result**: 全文一致使用 "no signal reliably surpasses greedy"，p=0.39, 未出现 "significantly outperforms"。

- [PASS] **"ρ-AUROC dissociation"**: experiments:67-69 EM leads AUROC but ranks 3rd/last in ρ. discussion:16 确认。CoNLL logprob AUROC=0.761 but lowest ρ=0.307 (experiments:71) 提供跨数据集验证。

- [ISSUE] **"corresponding AUROC of 0.749" 归属模糊**
  1. **位置**: `experiments.tex:64`
  2. **当前内容**: "While ρ=0.38 explains approximately 14% of F1 variance, the corresponding AUROC of 0.749..."
  3. **应该是**: ρ=0.38 来自 Voting，AUROC=0.749 来自 EM（不同信号）。"corresponding" 暗示同一信号，但 Voting 的 AUROC=0.684。建议改为 "while the best AUROC reaches 0.749 (EM)" 或类似表述以消除歧义。
  4. **严重程度**: **WARNING**

- [PASS] **Ensemble AUROC (0.666) < EM (0.749)**: 论文未提及 ensemble AUROC 0.666，无正面 framing。PASS。

- [PASS] **WNUT-17 as capability boundary**: experiments:79 "suggesting a capability boundary", intro:45 "when model capability is insufficient", conclusion:10 同。一致使用 "boundary" 框架而非 "method failure"。

### 3. 交叉引用完整性

- [PASS] **所有 \ref{} 均有对应 \label{}**: 核查 22 个 \ref 引用，均有对应 label。包括 fig:overview, tab:quality_estimation, tab:selection, tab:robustness, tab:wnut, tab:cross_selection, fig:signal_heatmap, fig:selection_gap, fig:temperature_robustness, fig:reliability, fig:length_logprob_scatter, tab:notation, 以及所有 section/appendix 引用。

- [PASS] **所有 \cite{} 均有 bib 条目**: 核查 48 个 citation key，全部存在于 references.bib。

- [PASS] **所有 figure 文件存在**: figures/ 目录包含 fig_overview.pdf, fig_signal_heatmap.pdf, fig_selection_gap.pdf, fig_temperature_robustness.pdf, fig_reliability.pdf, fig_length_logprob_scatter.pdf。

### 4. 公式一致性

- [PASS] **六个公式均定义于 method.tex**: eq:logprob (L21), eq:em (L27), eq:fk (L33), eq:sj (L42), eq:sj_instance (L47), eq:voting (L54)。

- [PASS] **SJ 定义一致**: method.tex:41-45 定义 Hungarian algorithm + token-level IoU。experiments:16 使用 "exact span matching" 区分评估指标 (F1) 与信号计算 (SJ)，无混淆。

- [PASS] **信号分类一致**: 三族五信号 (structural: Voting, SJ; surface: EM, FK; model-internal: logprob) 在 abstract, intro:31, method:16, conclusion:4 中分类一致。

### 5. 结构完整性

- [PASS] **Abstract 覆盖所有 core findings**:
  - structural > logprob: L6 "structural signals dominate hard tasks" ✓
  - ρ-AUROC dissociation: L4 "ranking and classification favoring different signals" ✓
  - correlation-selection gap: L4-5 "does not translate into selection gains" ✓
  - WNUT-17 boundary: L6 "when model capability is insufficient" ✓

- [PASS] **Conclusion 与 findings 对齐**: 三个 anchor findings (quality estimation, correlation-selection gap, task-complexity boundary) 均有对应段落。

- [PASS] **Limitations 诚实**: 单一 RE 数据集 (L1), 两个模型家族 (L3-5), 无 trained verifier (L8-9), N≤16 (L11), SJ-FK gap on CoNLL only 0.003 (L14), logprob temperature sensitivity uncharacterized (L15)。覆盖全面。

### 6. 已知问题检查

- [PASS] **exp_012 (512 截断) 数据未出现**: 论文中无 512 truncation 或 exp_012 的引用。

- [PASS] **Selection 未写 "significantly outperforms"**: 所有 selection 讨论使用 "not statistically significant", "no signal reliably surpasses", p=0.39。

- [PASS] **Ensemble 未正面 framing**: 论文不讨论 ensemble AUROC。

- [ISSUE] **CoNLL ">91%" claim 对 Qwen 不成立**
  1. **位置**: `experiments.tex:10` 和 `experiments.tex:74`
  2. **当前内容**: L10: "where models achieve >91% micro F1"; L74: "On CoNLL (greedy F1>0.91)"
  3. **应该是**: Qwen CoNLL greedy F1 = 0.908 (90.8%), 不满足 >91%。LLaMA=0.924 满足。建议改为 ">90%" 或 "≈91%" 或 "90.8--92.4%"。
  4. **严重程度**: **MINOR** (0.908 ≈ 0.91, 不影响结论)

---

## 汇总

| 类别 | PASS | ISSUE |
|------|------|-------|
| 数值一致性 | 12 | 1 CRITICAL |
| Claim 强度 | 5 | 1 WARNING |
| 交叉引用 | 3 | 0 |
| 公式一致性 | 3 | 0 |
| 结构完整性 | 3 | 0 |
| 已知问题 | 3 | 1 MINOR |
| **合计** | **29** | **1 CRITICAL, 1 WARNING, 1 MINOR** |

**需修复**:
1. **CRITICAL**: `appendix.tex:175` — cross-selection table RE 行 (Best=.410) 与主表及正文 (Best=.395, Δ=−0.9 pp) 矛盾。需修正为与 tab:selection 一致的值。
2. **WARNING**: `experiments.tex:64` — "corresponding AUROC of 0.749" 暗示与 ρ=0.38 来自同一信号 (Voting)，但实际来自 EM (Voting AUROC=0.684)。
3. **MINOR**: `experiments.tex:10,74` — ">91%" 对 Qwen CoNLL (90.8%) 不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 439469,
  "duration_api_ms": 440369,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "93f5e239-cf89-46d2-ae5f-27efd465cae9",
  "total_cost_usd": 1.1441247499999998,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 61887,
    "cache_read_input_tokens": 344440,
    "output_tokens": 23330,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 61887,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 6676,
        "cache_read_input_tokens": 72111,
        "cache_creation_input_tokens": 1477,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1477
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1741,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001811,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 23330,
      "cacheReadInputTokens": 344440,
      "cacheCreationInputTokens": 61887,
      "webSearchRequests": 0,
      "costUSD": 1.1423137499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "08222070-59b3-4a50-8a32-9b61dec5c75b"
}
```

</details>

---
