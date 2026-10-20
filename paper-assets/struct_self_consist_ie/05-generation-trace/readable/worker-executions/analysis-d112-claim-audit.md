# analysis d112 claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_analysis_d112_claim_audit_20260516T094502.log`
- **Structured JSON:** [`4fdadeb7aad044da83db.json`](../../sessions/4f/4fdadeb7aad044da83db.json)

## Before a recorded user message

53 recorded events

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "88d58ff1-3fa9-4779-b756-a92b2ccb750b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778942400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "34c8e347-d5ca-42aa-b99b-787252c3f80e",
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the paper sections to extract numerical claims, then cross-check them for consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "e52bfe49-f6bb-4db5-a591-fc312476a8f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3MpnBm9VfZg6LEzrUxejv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11898,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11898
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

开始系统性检查论文数值一致性。先读取所有章节文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "ace8ded8-ba60-47da-8aa3-731afb1ace14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3MpnBm9VfZg6LEzrUxejv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11898,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11898
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01UA5oZMV6TGvM4wMqrJp9dZ`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "8c769e28-0cfc-4b81-a500-23ad3e7883cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3MpnBm9VfZg6LEzrUxejv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11898,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11898
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 7 · 2026-05-16T09:45:15.831Z_

<details><summary>↩ Tool result · `toolu_01UA5oZMV6TGvM4wMqrJp9dZ`</summary>

```text
docs/paper/sections/appendix.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/limitations.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/discussion.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "b5c3f395-a541-4282-85cc-adc4268dcb1f",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/experiments.tex"
    ],
    "durationMs": 9,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Qvp1JUYZSqzyhcyuzoPrtf`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "0ede0bb3-28be-4cee-8ec6-954ba1e5b9fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 9 · 2026-05-16T09:45:19.591Z_

<details><summary>↩ Tool result · `toolu_01Qvp1JUYZSqzyhcyuzoPrtf`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---on a medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) controls, within a narrow model-scale range (4B--8B).
4	All signals achieve moderate quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control), yet best-of-$N$ selection fails to outperform greedy decoding ($T{=}0$)---the \textit{correlation-selection gap}.
5	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats, with entity-token isolation revealing intrinsic overconfidence rather than format-token dilution.
6	A five-layer ablation chain (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding.
7	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "77c2e656-b249-43fb-88f8-aa74de01f8c0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---on a medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) controls, within a narrow model-scale range (4B--8B).\nAll signals achieve moderate quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control), yet best-of-$N$ selection fails to outperform greedy decoding ($T{=}0$)---the \\textit{correlation-selection gap}.\nWe diagnose two mechanisms: (a)~\\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\\rho{=}0.52$); and (b)~\\textit{log-probability compression}---median within-instance range of 0.041 nats, with entity-token isolation revealing intrinsic overconfidence rather than format-token dilution.\nA five-layer ablation chain (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding.\nSignal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.\n\\end{abstract}\n",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01Kt8mMpwjGhmWqpHPKwjmJx`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "2de79ccc-86b8-409c-aaf3-3571e94f4cda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 11 · 2026-05-16T09:45:19.935Z_

<details><summary>↩ Tool result · `toolu_01Kt8mMpwjGhmWqpHPKwjmJx`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing two failure mechanisms---instance degeneracy and LP compression---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	We define the \textbf{correlation-selection gap} as the disparity between a signal's rank correlation with F1 ($\rho$) and its ability to select the best output from $N$ candidates (Figure~\ref{fig:overview}): on SciERC, signals achieve moderate quality estimation ($\rho{=}0.38$, up to 0.45 on a ceiling-effect control) yet selection fails to improve over greedy decoding ($T{=}0$; single forward pass, no sampling overhead) despite 13--18~pp oracle headroom.
12	The gap has two empirical causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---median within-instance range of 0.041 nats (\S\ref{sec:discussion}).
13	
14	\begin{figure*}[t]
15	\centering
16	\includegraphics[width=\textwidth]{fig_overview}
17	\caption{The correlation-selection gap. \textbf{Left}: consistency signals predict instance-level quality ($\rho{=}0.38$). \textbf{Right}: all selection methods---including LP and consensus-proximity (MBR)---fail to outperform greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
18	\label{fig:overview}
19	\end{figure*}
20	
21	We evaluate five signals from three families---structural, surface, and model-internal---on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control) and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
22	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
23	Our contributions:
24	\begin{enumerate}
25	    \item \textbf{Two failure mechanisms.}
26	    We diagnose instance degeneracy and log-probability compression as mechanisms explaining why quality estimation signals fail to translate into selection gains in fine-tuned IE models.
27	    Instance degeneracy: MBR utility correlates positively with F1 within instances (median $\rho{=}0.52$), but 21--58\% of instances produce identical F1 across all $N$ samples, eliminating headroom; on non-degenerate instances, MBR closes 23--41\% of the oracle gap.
28	    Unlike prior MBR failures attributed to utility misalignment, our signals achieve positive within-instance correlation; the failure stems from vanishing headroom due to instance degeneracy.
29	    LP compression: median within-instance range of 0.041 nats ($\rho(\text{LP}, \text{F1}){=}0.248$); entity-token LP increases variance ($4{\times}$) but worsens selection, pointing to intrinsic overconfidence.
30	
31	    \item \textbf{Diagnostic ablation chain.}
32	    A five-layer ablation (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding or signal design. Signal rankings shift with task difficulty and collapse at the capability boundary.
33	
34	    \item \textbf{Practical implication.}
35	    Greedy decoding ($T{=}0$, F1${=}0.663$) surpasses all $N{=}8$ selection strategies (best: 0.647) despite 13--18~pp oracle headroom---multi-sample selection adds cost without benefit under current signal families.
36	\end{enumerate}
37	
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "abc64a7a-828f-4365-9329-d91a8346ddd3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut named entity recognition (NER) poses a structurally different challenge: the output is a \\textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\n\\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing two failure mechanisms---instance degeneracy and LP compression---within the dominant deployment paradigm for production NER.\n\nA methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.\nWe define the \\textbf{correlation-selection gap} as the disparity between a signal's rank correlation with F1 ($\\rho$) and its ability to select the best output from $N$ candidates (Figure~\\ref{fig:overview}): on SciERC, signals achieve moderate quality estimation ($\\rho{=}0.38$, up to 0.45 on a ceiling-effect control) yet selection fails to improve over greedy decoding ($T{=}0$; single forward pass, no sampling overhead) despite 13--18~pp oracle headroom.\nThe gap has two empirical causes: (a)~\\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\\rho{=}0.52$); and (b)~\\textit{LP compression}---median within-instance range of 0.041 nats (\\S\\ref{sec:discussion}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals predict instance-level quality ($\\rho{=}0.38$). \\textbf{Right}: all selection methods---including LP and consensus-proximity (MBR)---fail to outperform greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\\S\\ref{sec:discussion}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families---structural, surface, and model-internal---on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control) and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nAn exploratory extension to relation extraction is reported in Appendix~\\ref{app:re_extension}.\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Two failure mechanisms.}\n    We diagnose instance degeneracy and log-probability compression as mechanisms explaining why quality estimation signals fail to translate into selection gains in fine-tuned IE models.\n    Instance degeneracy: MBR utility correlates positively with F1 within instances (median $\\rho{=}0.52$), but 21--58\\% of instances produce identical F1 across all $N$ samples, eliminating headroom; on non-degenerate instances, MBR closes 23--41\\% of the oracle gap.\n    Unlike prior MBR failures attributed to utility misalignment, our signals achieve positive within-instance correlation; the failure stems from vanishing headroom due to instance degeneracy.\n    LP compression: median within-instance range of 0.041 nats ($\\rho(\\text{LP}, \\text{F1}){=}0.248$); entity-token LP increases variance ($4{\\times}$) but worsens selection, pointing to intrinsic overconfidence.\n\n    \\item \\textbf{Diagnostic ablation chain.}\n    A five-layer ablation (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding or signal design. Signal rankings shift with task difficulty and collapse at the capability boundary.\n\n    \\item \\textbf{Practical implication.}\n    Greedy decoding ($T{=}0$, F1${=}0.663$) surpasses all $N{=}8$ selection strategies (best: 0.647) despite 13--18~pp oracle headroom---multi-sample selection adds cost without benefit under current signal families.\n\\end{enumerate}\n\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Nx7UFXvVW1ayqy9LoWruk1`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "ceb91785-cc9c-4399-bb25-31bae381b694",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 13 · 2026-05-16T09:45:20.670Z_

<details><summary>↩ Tool result · `toolu_01Nx7UFXvVW1ayqy9LoWruk1`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
27	\begin{equation}\label{eq:fk}
28	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
29	\end{equation}
30	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
31	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_independence}), which does not inflate FK.
32	Unlike structural signals, FK relies on exact string matching.
33	
34	\paragraph{Soft Jaccard (structural, instance-level).}
35	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:
36	\begin{equation}\label{eq:sj}
37	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
38	\end{equation}
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.\footnote{The denominator uses $\max(|g_i|, |g_j|)$ per type group rather than $|A \cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; robustness to this choice is verified in Table~\ref{tab:sj_normalizer}.}
40	The instance-level signal averages over all pairs:
41	\begin{equation}\label{eq:sj_instance}
42	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
43	\end{equation}
44	
45	\paragraph{Entity voting confidence (structural, instance-level).}
46	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
47	The instance-level confidence is the mean frequency:
48	\begin{equation}\label{eq:voting}
49	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
50	\end{equation}
51	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
52	
53	\subsection{Evaluation Framework}\label{sec:evaluation}
54	
55	\paragraph{Quality estimation.}
56	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
57	Both quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\ref{app:additional}.}
58	
59	\paragraph{Sample selection.}
60	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.
61	Baselines: \textit{oracle} (highest-F1 sample) and \textit{single-sample} (one $T{=}1.0$ draw, not argmax decoding; labeled ``Single'' in tables).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "1f12e965-b887-494e-a0fe-68069582eecf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\nA \\textbf{per-sample signal} $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$ scores each output independently; an \\textbf{instance-level signal} $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$ produces a single score per input (notation in Appendix~\\ref{app:notation}).\nThis distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\\S\\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nFour are \\textit{consistency signals}: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]); log-probability [LP] is the sole \\textit{model-internal}, per-sample signal.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed and $\\bar{P}_e$ expected agreement.\nTemperature-based sampling introduces mild negative dependence ($-$0.4\\% to $-$4.0\\%; Appendix~\\ref{app:fk_independence}), which does not inflate FK.\nUnlike structural signals, FK relies on exact string matching.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\\max(|g_i|, |g_j|)$ penalizes length asymmetry.\\footnote{The denominator uses $\\max(|g_i|, |g_j|)$ per type group rather than $|A \\cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; robustness to this choice is verified in Table~\\ref{tab:sj_normalizer}.}\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$, we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{Equation~\\ref{eq:voting} defines the continuous QE signal; for voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nSpearman $\\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.\nBoth quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\\ref{app:additional}.}\n\n\\paragraph{Sample selection.}\nBest-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.\nBaselines: \\textit{oracle} (highest-F1 sample) and \\textit{single-sample} (one $T{=}1.0$ draw, not argmax decoding; labeled ``Single'' in tables).\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01Dk1vS2yZdqpVujKLp4vxQu`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "8f498b29-757a-43a7-af45-f113db3dcbfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 15 · 2026-05-16T09:45:21.330Z_

<details><summary>↩ Tool result · `toolu_01Dk1vS2yZdqpVujKLp4vxQu`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
35	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
36	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
37	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
38	\midrule
39	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models.\footnote{$\varepsilon{=}0.05$ applies only to selection (\S\ref{sec:selection_gap}); quality estimation is $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
45	
46	\paragraph{Signal rankings are difficulty-dependent.}
47	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over surface ($\rho{\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
48	On CoNLL (ceiling-effect control, single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
49	At the signal-collapse boundary---WNUT-17 (52\% zero F1)---all conditional signals collapse (Table~\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest ($\rho{=}0.360$; Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}).
50	
51	%% ============================================================
52	\subsection{The Correlation-Selection Gap}
53	\label{sec:selection_gap}
54	
55	We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
56	
57	\begin{table}[t]
58	\centering
59	\small
60	\caption{Best-of-$N$ NER selection F1 on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$, Fisher combined $p$ vs.\ single-sample). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. $^\ddagger$Single: one $T{=}1.0$ draw (expected performance of a single sample); Random: uniform random selection from $N$ candidates; $^\dagger$Greedy: deterministic argmax decoding ($T{=}0$), no sampling variance. Non-tied LP subset analysis in \S\ref{sec:discussion}; RE selection in Appendix~\ref{app:re_extension}.}
61	\label{tab:selection}
62	\begin{tabular}{lcc}
63	\toprule
64	Method & NER F1 & $p$ \\
65	\midrule
66	Oracle & $0.778 \pm 0.003$ & --- \\
67	Greedy ($T{=}0$)$^\dagger$ & $0.663$ & --- \\
68	\midrule
69	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
70	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
71	\midrule
72	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
73	SJ           & $0.646 \pm 0.002$ & .68 \\
74	FK           & $0.646 \pm 0.001$ & .79 \\
75	EM           & $0.637 \pm 0.001$ & .45 \\
76	VC           & $0.623 \pm 0.004$ & .26 \\
77	\midrule
78	Single$^\ddagger$ & $0.645 \pm 0.001$ & --- \\
79	Random           & $0.610 \pm 0.003$ & --- \\
80	\bottomrule
81	\end{tabular}
82	\end{table}
83	
84	Despite moderate quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
85	Instance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none improves over single-sample.
86	The key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.
87	
88	\paragraph{No significant improvement over single-sample.}
89	On SciERC NER (2-seed sign tests\footnote{Multi-seed NER experiments confirm seed variation is small ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above single-sample (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
90	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\ref{app:re_extension}).
91	CoNLL's near-ceiling single-sample F1 (0.91) with only ${\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.
92	Under stringent external TOST anchors ($\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation, indicating signals can actively harm selection (Appendix~\ref{app:tost}).
93	Greedy decoding ($T{=}0$; single forward pass, no sampling overhead) achieves F1${=}0.663$, surpassing all $N{=}8$ selection strategies (best: LP at 0.647).
94	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
95	
96	%% ============================================================
97	\subsection{Robustness}
98	\label{sec:robustness_main}
99	
100	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
101	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; Table~\ref{tab:ranking-stability}).
102	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
108	\label{tab:scale_ablation}
109	\begin{tabular}{@{}ll cc r@{}}
110	\toprule
111	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
112	\midrule
113	CoNLL & SJ & .436 & .422 & $-$.014 \\
114	      & FK & .400 & .418 & $+$.018 \\
115	SciERC & SJ & .360 & .422 & $+$.062 \\
116	       & FK & .267 & .326 & $+$.059 \\
117	\bottomrule
118	\end{tabular}
119	\end{table}
120	
121	\paragraph{Scale robustness.}
122	Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below single-sample on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale.
123	Instance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\% vs.\ 10.4\%) despite comparable within-instance utility correlation (Table~\ref{tab:degeneracy}).
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "1b121b3c-ba8c-4f08-89df-f5175c711f45",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures.\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\\ref{app:n_scaling}).}\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ applies only to selection (\\S\\ref{sec:selection_gap}); quality estimation is $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over surface ($\\rho{\\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (ceiling-effect control, single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$); the $\\rho$--AUROC dissociation across datasets reflects use-case alignment.\nAt the signal-collapse boundary---WNUT-17 (52\\% zero F1)---all conditional signals collapse (Table~\\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest ($\\rho{=}0.360$; Figure~\\ref{fig:signal_heatmap}, Appendix~\\ref{app:additional}).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nWe define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection F1 on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$, Fisher combined $p$ vs.\\ single-sample). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. $^\\ddagger$Single: one $T{=}1.0$ draw (expected performance of a single sample); Random: uniform random selection from $N$ candidates; $^\\dagger$Greedy: deterministic argmax decoding ($T{=}0$), no sampling variance. Non-tied LP subset analysis in \\S\\ref{sec:discussion}; RE selection in Appendix~\\ref{app:re_extension}.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- \\\\\nGreedy ($T{=}0$)$^\\dagger$ & $0.663$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & .45 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 \\\\\n\\midrule\nSingle$^\\ddagger$ & $0.645 \\pm 0.001$ & --- \\\\\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite moderate quality estimation, confidence signals yield limited selection gains (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nInstance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none improves over single-sample.\nThe key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.\n\n\\paragraph{No significant improvement over single-sample.}\nOn SciERC NER (2-seed sign tests\\footnote{Multi-seed NER experiments confirm seed variation is small ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above single-sample (0.645), yet LP achieves only 0.647 ($\\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\\ref{app:tost}).\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\\ref{app:re_extension}).\nCoNLL's near-ceiling single-sample F1 (0.91) with only ${\\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.\nUnder stringent external TOST anchors ($\\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation, indicating signals can actively harm selection (Appendix~\\ref{app:tost}).\nGreedy decoding ($T{=}0$; single forward pass, no sampling overhead) achieves F1${=}0.663$, surpassing all $N{=}8$ selection strategies (best: LP at 0.647).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nRepeating with Qwen3-4B (Table~\\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below single-sample on SciERC ($\\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale.\nInstance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\\% vs.\\ 10.4\\%) despite comparable within-instance utility correlation (Table~\\ref{tab:degeneracy}).\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_011kq8czo3UiMVitb3Uhcf3i`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "b3de526b-84b7-4489-9ef6-50b74c785b1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 17 · 2026-05-16T09:45:21.801Z_

<details><summary>↩ Tool result · `toolu_011kq8czo3UiMVitb3Uhcf3i`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
11	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
12	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
13	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero---the tension between model quality and selection utility is inherent.
14	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
15	Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\ref{app:mbr_discussion}).
16	Meanwhile, deterministic greedy decoding ($T{=}0$)---requiring no sampling cost---achieves F1${=}0.663$ on SciERC, surpassing all $N{=}8$ selection strategies (best: LP at 0.647; Table~\ref{tab:selection}).
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
22	\label{tab:degeneracy}
23	\begin{tabular}{lccc}
24	\toprule
25	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
26	\midrule
27	Constant F1 & 21\% & 10.4\% & 58\% \\
28	Constant utility & 13\% & 7.0\% & 49\% \\
29	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
30	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
36	Where compression is mitigated ($n{=}210$ instances with above-median LP spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), suggesting compression as a bottleneck; this subset analysis uses $\varepsilon{=}0.05$ tie-breaking, and the effect size is sensitive to subset definition (Appendix~\ref{app:diversity}).
37	Stratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
38	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection (Appendix~\ref{app:n_scaling}).
39	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidence}; \citealp{bhattacharyya2026beyond}).
40	
41	\paragraph{Signal combinations.}
42	We test three LP${\times}$VC combination strategies: VC-stratified LP selection, LP${\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.
43	All three fail to improve over single-sample (best: $+0.1$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.
44	An oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \textit{exists} within VC-equivalent groups but current signals cannot extract it.
45	
46	\paragraph{Hypotheses for LP compression.}
47	We identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.
48	Two are \textit{constraint-imposed}:
49	(b) \textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;
50	(c) \textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.
51	Two are \textit{model-learned}:
52	(a) \textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;
53	(d) \textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\texttt{\{"entities": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\% confirm that format tokens dominate the sequence.
54	The constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.
55	
56	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
57	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
58	On RE, free-form decoding consistently reverses LP selection direction ($+1.8{\pm}0.1$~pp, 4 seeds), suggesting regime-dependent behavior (Appendix~\ref{app:re_extension}).
59	VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling, deguchi2024centroid}.
60	More broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\ref{tab:degeneracy}; Appendix~\ref{app:mbr_discussion}).
61	
62	\paragraph{Ablation: entity-token LP.}
63	We directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.
64	On SciERC, entity-token LP exhibits $4{\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.
65	However, entity-token LP selection performs \textit{worse} than full-sequence LP ($-2.0$~pp), and on CoNLL, entity-token LP variance collapses to near-zero (median $2{\times}10^{-10}$) with 79\% of instances tied---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.
66	This rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.
67	
68	\paragraph{Pilot remedy.}
69	Entity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.
70	Its failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.
71	
72	\paragraph{Methodological implications.}
73	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
74	Effective selection likely requires trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
75	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "e3e82ca8-c64c-4da9-99c6-e3d612fafff7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Implications for practitioners.}\nVC leads on medium-difficulty NER ($\\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).\nRankings hold across model families and a 4B ablation (Table~\\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\\ref{app:re_extension}.\n\n\\paragraph{Why the gap exists.}\nWe identify two mechanisms: \\textit{instance degeneracy} (affecting consensus-proximity selection) and \\textit{LP compression} (affecting per-sample selection).\n\nWithin-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \\cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\\% (SciERC) to 41\\% (CoNLL) of the oracle gap.\nHowever, fine-tuned models exhibit pervasive \\textit{instance degeneracy}: 21\\% of SciERC instances (58\\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\\% (49\\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\\ref{tab:degeneracy}).\nInstance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.\nCoNLL (91\\% single-sample F1) exhibits 58\\% degeneracy; SciERC (66\\%) shows 21\\%; WNUT-17 (48\\%) shows near-zero---the tension between model quality and selection utility is inherent.\nScale ablation confirms this tension: Qwen3-8B shows 21\\% instance degeneracy on SciERC vs.\\ 10.4\\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\\rho{=}0.52$ vs.\\ $0.55$; Table~\\ref{tab:degeneracy}).\nDespite MBR's success in machine translation \\cite{freitag2022high}, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\\ref{app:mbr_discussion}).\nMeanwhile, deterministic greedy decoding ($T{=}0$)---requiring no sampling cost---achieves F1${=}0.663$ on SciERC, surpassing all $N{=}8$ selection strategies (best: LP at 0.647; Table~\\ref{tab:selection}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\n& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\\n\\midrule\nConstant F1 & 21\\% & 10.4\\% & 58\\% \\\\\nConstant utility & 13\\% & 7.0\\% & 49\\% \\\\\nOracle gap closed (non-deg.) & 23\\% & 25.2\\% & 41\\% \\\\\nWithin-inst.\\ SJ $\\rho$ (median) & 0.524 & 0.550 & 0.994 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLog-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\\ref{tab:logprob_ties}), with pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ confirming weak but positive signal.\nWhere compression is mitigated ($n{=}210$ instances with above-median LP spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), suggesting compression as a bottleneck; this subset analysis uses $\\varepsilon{=}0.05$ tie-breaking, and the effect size is sensitive to subset definition (Appendix~\\ref{app:diversity}).\nStratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\\ref{app:vc_quartile}).\nDoubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection (Appendix~\\ref{app:n_scaling}).\nA verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\\rho$ than LP (Appendix~\\ref{app:verbalized_confidence}; \\citealp{bhattacharyya2026beyond}).\n\n\\paragraph{Signal combinations.}\nWe test three LP${\\times}$VC combination strategies: VC-stratified LP selection, LP${\\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.\nAll three fail to improve over single-sample (best: $+0.1$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.\nAn oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \\textit{exists} within VC-equivalent groups but current signals cannot extract it.\n\n\\paragraph{Hypotheses for LP compression.}\nWe identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.\nTwo are \\textit{constraint-imposed}:\n(b) \\textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;\n(c) \\textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.\nTwo are \\textit{model-learned}:\n(a) \\textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;\n(d) \\textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\\texttt{\\{\"entities\": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\\% confirm that format tokens dominate the sequence.\nThe constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.\nOn RE, free-form decoding consistently reverses LP selection direction ($+1.8{\\pm}0.1$~pp, 4 seeds), suggesting regime-dependent behavior (Appendix~\\ref{app:re_extension}).\nVC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \\cite{eikema2022sampling, deguchi2024centroid}.\nMore broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\\ref{tab:degeneracy}; Appendix~\\ref{app:mbr_discussion}).\n\n\\paragraph{Ablation: entity-token LP.}\nWe directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.\nOn SciERC, entity-token LP exhibits $4{\\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.\nHowever, entity-token LP selection performs \\textit{worse} than full-sequence LP ($-2.0$~pp), and on CoNLL, entity-token LP variance collapses to near-zero (median $2{\\times}10^{-10}$) with 79\\% of instances tied---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.\nThis rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.\n\n\\paragraph{Pilot remedy.}\nEntity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.\nIts failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEffective selection likely requires trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (Appendix~\\ref{app:ood}).\n",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01HcMCCkqhqMZfejkJu78F3D`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "75a717d4-f4f6-439c-b807-8d31f9b11a59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 19 · 2026-05-16T09:45:22.293Z_

<details><summary>↩ Tool result · `toolu_01HcMCCkqhqMZfejkJu78F3D`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate quality estimation ($\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform greedy decoding ($T{=}0$).
4	The gap stems from two mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, scaling with model capability and eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).
5	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
6	The gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).
7	Whether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) are promising directions.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "a11c603a-3339-4287-9498-88cfd74f05b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \\textit{correlation-selection gap}: moderate quality estimation ($\\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform greedy decoding ($T{=}0$).\nThe gap stems from two mechanisms: instance degeneracy (21--58\\% of instances produce identical F1 across all $N$ samples, scaling with model capability and eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).\nDiagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.\nThe gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).\nWhether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\\ref{app:re_extension}) are promising directions.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01TXoxZke5S6huyECKCzrdCx`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "018b03d0-8e3c-4690-9df4-6fa39171d02b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 21 · 2026-05-16T09:45:22.746Z_

<details><summary>↩ Tool result · `toolu_01TXoxZke5S6huyECKCzrdCx`</summary>

```text
1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.4$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}); calibration-based approaches remain unexplored.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "30ed6ec9-b700-41f3-be54-87524b8ba4a6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.\nWe cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.\nWe do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\\ref{app:re_extension}.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\nAd-hoc LP${\\times}$VC combinations yield at most $+0.4$~pp over greedy (not significant; \\S\\ref{sec:discussion}); whether \\textit{learned} combinations could close the gap remains open.\nThe $\\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.\nWe tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\\times}$); LP${\\times}$VC combinations also fail to recover selection (\\S\\ref{sec:discussion}); calibration-based approaches remain unexplored.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01GDTjTEjPXbhaYr2qPGRXnF`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "b08fc687-3934-4432-82cd-6dc1c52ed3ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 23 · 2026-05-16T09:45:23.461Z_

<details><summary>↩ Tool result · reported error · `toolu_01GDTjTEjPXbhaYr2qPGRXnF`</summary>

```text
File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "dc9ca8dc-f496-4ff9-8ee4-7a36139d10d1",
  "tool_use_result": "Error: File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01GKyn6HQqZf4Dm4JrHbp6im`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "f7ef7ae0-a49d-45e0-97ca-f121a65fff7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHWheGWArvz7sCTm5UZNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 23739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 25 · 2026-05-16T09:45:23.895Z_

<details><summary>↩ Tool result · `toolu_01GKyn6HQqZf4Dm4JrHbp6im`</summary>

```text
1	paper:
2	  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence
3	    Signals for Test-Time Scaling in Information Extraction'
4	  version: 100
5	  generated_at: '2026-05-16T08:28:21.069996+00:00'
6	  source: manual provenance build by Paper Agent
7	claims:
8	- id: c001_voting_rho_scierc_ner
9	  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation
10	    artifact)
11	  sections:
12	  - abstract
13	  - introduction
14	  - experiments
15	  - conclusion
16	  - discussion
17	  - related_work
18	  tier: 1
19	  evidence:
20	  - exp_id: exp_012_rerun_1024
21	    metric: ner.voting_rho_full
22	    value: 0.379
23	  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected
24	    via exp_012_rerun_1024 (max_tokens=1024).
25	- id: c002_auroc_dissociation_scierc
26	  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while
27	    Voting leads ρ (NER 0.379, RE 0.422)
28	  sections:
29	  - abstract
30	  - introduction
31	  - experiments
32	  - conclusion
33	  - discussion
34	  tier: 1
35	  evidence:
36	  - exp_id: exp_012_rerun_1024
37	    metric: ner.em_auroc
38	    value: 0.749
39	  - exp_id: exp_012_rerun_1024
40	    metric: re.em_auroc
41	    value: 0.706
42	  - exp_id: exp_012_rerun_1024
43	    metric: ner.voting_auroc
44	    value: 0.684
45	  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected
46	    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline
47	    claim changed from "entity voting achieves ρ=0.38 and AUROC=0.74" to split ρ (Voting
48	    0.38) / AUROC (EM 0.75) claim.
49	- id: c003_sj_rho_scierc_ner
50	  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)
51	  sections:
52	  - experiments
53	  tier: 1
54	  evidence:
55	  - exp_id: exp_012_rerun_1024
56	    metric: ner.sj_rho_full
57	    value: 0.36
58	  - exp_id: exp_004_re_diagnostic
59	    metric: bootstrap_ci_95.ner_sj
60	    value:
61	    - 0.2946
62	    - 0.4586
63	- id: c004_voting_leads_re
64	  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)
65	  sections:
66	  - experiments
67	  tier: 1
68	  evidence:
69	  - exp_id: exp_012_rerun_1024
70	    metric: re.voting_rho_full
71	    value: 0.35
72	  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.
73	- id: c005_fk_beats_sj_re
74	  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER
75	  sections:
76	  - experiments
77	  tier: 1
78	  evidence:
79	  - exp_id: exp_012_rerun_1024
80	    metric: re.fk_rho_full
81	    value: 0.275
82	  - exp_id: exp_012_rerun_1024
83	    metric: re.sj_rho_full
84	    value: 0.25
85	  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.
86	- id: c006_re_40pct_zero_f1
87	  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)
88	  sections:
89	  - experiments
90	  - discussion
91	  tier: 1
92	  evidence:
93	  - exp_id: mvp_pilot_004
94	    metric: re_sample_f1_pct_zero
95	    value: 44.3
96	    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)
97	  - exp_id: exp_008_re_n16_v2
98	    metric: f1_zero_pct
99	    value: 44.3
100	    note: 44.3% at N=16; zero-F1 fraction varies with N and seed
101	- id: c007_em_leads_conll
102	  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816
103	  sections:
104	  - experiments
105	  tier: 1
106	  evidence:
107	  - exp_id: exp_002
108	    metric: em_rho_full
109	    value: 0.4507
110	  - exp_id: exp_002
111	    metric: em_auroc_full
112	    value: 0.8156
113	  - exp_id: exp_015_v2
114	    metric: auroc_best.EM.conll_ner
115	    value: 0.8156
116	- id: c008_cross_model_sj_stability
117	  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'
118	  sections:
119	  - experiments
120	  tier: 1
121	  evidence:
122	  - exp_id: exp_002
123	    metric: sj_rho_full
124	    value: 0.4357
125	  - exp_id: exp_017_llama_conll_infer
126	    metric: full.SJ_rho
127	    value: 0.4314
128	- id: c009_logprob_paradox
129	  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA
130	  sections:
131	  - experiments
132	  - discussion
133	  tier: 1
134	  evidence:
135	  - exp_id: exp_017_llama_conll_infer
136	    metric: full.logprob_AUROC
137	    value: 0.761
138	  - exp_id: exp_017_llama_conll_infer
139	    metric: full.logprob_rho
140	    value: 0.3072
141	- id: c010_conll_oracle_headroom
142	  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'
143	  sections:
144	  - experiments
145	  tier: 1
146	  evidence:
147	  - exp_id: exp_002
148	    metric: oracle_headroom
149	    value: 0.042
150	  - exp_id: exp_017_llama_conll_infer
151	    metric: oracle_headroom
152	    value: 0.0177
153	- id: c011_ner_no_reliable_selection
154	  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed
155	    bootstrap)
156	  sections:
157	  - abstract
158	  - introduction
159	  - experiments
160	  - conclusion
161	  - discussion
162	  - related_work
163	  tier: 1
164	  evidence:
165	  - exp_id: exp_016_rerun_1024_bootstrap
166	    metric: selection_f1_ner
167	    value:
168	      greedy: 0.644
169	      logprob: 0.65
170	      sj: 0.645
171	      voting: 0.634
172	      random: 0.608
173	      oracle: 0.776
174	  - exp_id: exp_016_rerun_1024_bootstrap
175	    metric: bootstrap_selection_test
176	    value:
177	      logprob_vs_greedy_p: 0.39
178	      ci_95:
179	      - -0.03
180	      - 0.042
181	      cohens_d: 0.038
182	      sign_test: 61W/70L
183	  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified
184	    with c012 — no signal reliably helps on either task.
185	- id: c012_re_no_signal_beats_greedy
186	  text: No signal surpasses greedy on RE; logprob drops to −0.9pp
187	  sections:
188	  - abstract
189	  - introduction
190	  - experiments
191	  - conclusion
192	  - discussion
193	  tier: 1
194	  evidence:
195	  - exp_id: exp_016_rerun_1024_bootstrap
196	    metric: selection_f1_re
197	    value:
198	      greedy: 0.404
199	      logprob: 0.395
200	      sj: 0.386
201	      voting: 0.359
202	      random: 0.354
203	      oracle: 0.585
204	  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was "only logprob
205	    helps on RE (+2.3pp)". Corrected via exp_016_rerun_1024_bootstrap.
206	- id: c013_oracle_headroom_ner
207	  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER
208	  sections:
209	  - experiments
210	  - discussion
211	  tier: 1
212	  evidence:
213	  - exp_id: exp_016_rerun_1024_bootstrap
214	    metric: selection_f1_ner.oracle
215	    value: 0.776
216	  - exp_id: exp_016_rerun_1024_bootstrap
217	    metric: selection_f1_ner.greedy
218	    value: 0.644
219	- id: c014_re_oracle_headroom
220	  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'
221	  sections:
222	  - experiments
223	  - discussion
224	  tier: 1
225	  evidence:
226	  - exp_id: exp_016_rerun_1024_bootstrap
227	    metric: selection_f1_re.oracle
228	    value: 0.585
229	  - exp_id: exp_016_rerun_1024_bootstrap
230	    metric: selection_f1_re.greedy
231	    value: 0.404
232	- id: c015_ensemble_auroc
233	  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)
234	  sections:
235	  - discussion
236	  tier: 1
237	  evidence:
238	  - exp_id: exp_016_rerun_1024_bootstrap
239	    metric: ensemble_ner_auroc
240	    value: 0.666
241	  note: Ensemble does NOT improve over best individual. Changed from positive to negative
242	    finding.
243	- id: c016_ece_calibration
244	  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater
245	    miscalibration (ECE 0.109-0.339)
246	  sections:
247	  - experiments
248	  tier: 1
249	  evidence:
250	  - exp_id: exp_016_rerun_1024_bootstrap
251	    metric: calibration_ece
252	    value:
253	      ner_range: 0.069-0.096
254	      re_range: 0.109-0.339
255	  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration
256	    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has
257	    moderate miscalibration. Consistent with fig_reliability_1024.
258	- id: c017_fisher_z_ner_vs_re
259	  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'
260	  sections:
261	  - experiments
262	  tier: 1
263	  evidence:
264	  - exp_id: exp_004_re_diagnostic
265	    metric: fisher_z_ner_vs_re.sj_z
266	    value: 2.31
267	  - exp_id: exp_004_re_diagnostic
268	    metric: fisher_z_ner_vs_re.sj_p
269	    value: 0.0209
270	- id: c018_per_relation_diagnostic
271	  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646
272	  sections:
273	  - experiments
274	  tier: 1
275	  evidence:
276	  - exp_id: exp_004_re_diagnostic
277	    metric: per_relation_type.FEATURE-OF.rho_sj
278	    value: 0.004
279	  - exp_id: exp_004_re_diagnostic
280	    metric: per_relation_type.HYPONYM-OF.rho_fk
281	    value: 0.646
282	- id: c019_entity_span_errors
283	  text: Entity span errors account for 55.5% of RE false negatives
284	  sections:
285	  - experiments
286	  tier: 1
287	  evidence:
288	  - exp_id: exp_004_re_diagnostic
289	    metric: error_propagation
290	    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error
291	      21.7% → entity span errors ~55.5%
292	  note: Computed from error_propagation breakdown in exp_004
293	- id: c020_capability_stratification_ner
294	  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities
295	  sections:
296	  - experiments
297	  tier: 1
298	  evidence:
299	  - exp_id: exp_009_capability_stratification
300	    metric: scierc_ner.by_ent_count.6plus_sj_rho
301	    value: 0.547
302	  - exp_id: exp_009_capability_stratification
303	    metric: scierc_ner.by_ent_count.1_2_sj_rho
304	    value: 0.415
305	- id: c021_wnut_boundary
306	  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'
307	  sections:
308	  - experiments
309	  - conclusion
310	  tier: 1
311	  evidence:
312	  - exp_id: exp_003_wnut17_eval
313	    metric: rho_sj
314	    value: 0.089
315	  - exp_id: exp_003_wnut17_eval
316	    metric: sample_f1_pct_zero
317	    value: 53.7
318	  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered
319	    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'
320	- id: c022_wnut_logprob_negative
321	  text: WNUT logprob shows strong negative correlation
322	  sections:
323	  - experiments
324	  tier: 1
325	  evidence:
326	  - exp_id: exp_003_ner_wnut17
327	    metric: ner.rho_logprob_full
328	    value: -0.414
329	  - exp_id: exp_003_wnut17_eval
330	    metric: rho_logprob_full
331	    value: -0.409
332	- id: c023_re_sent_length_sj
333	  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'
334	  sections:
335	  - experiments
336	  tier: 2
337	  evidence:
338	  - exp_id: exp_009_v2_re_rerun
339	    metric: by_sent_len_quartiles
340	    value:
341	      Q1_sj_rho: 0.11
342	      Q4_sj_rho: 0.473
343	      fisher_z_p: 0.004
344	  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).
345	    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'
346	- id: c024_high_complexity_re_subset
347	  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'
348	  sections:
349	  - experiments
350	  tier: 2
351	  evidence:
352	  - exp_id: exp_009_capability_stratification
353	    metric: scierc_re.by_rel_count
354	    value:
355	      6plus_sj_rho: 0.527
356	  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and
357	    logprob values not in registry summary.
358	- id: c025_temperature_sj_stable
359	  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028
360	  sections:
361	  - experiments
362	  tier: 1
363	  evidence:
364	  - exp_id: exp_005
365	    metric: sj_rho_t07_ner
366	    value: 0.388
367	  - exp_id: exp_012_rerun_1024
368	    metric: ner.sj_rho_full
369	    value: 0.36
370	  note: T=0.7 data from exp_005; T=1.0 from exp_015
371	- id: c026_n_scaling_sj
372	  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen
373	    SciERC NER
374	  sections:
375	  - experiments
376	  tier: 1
377	  evidence:
378	  - exp_id: exp_012_rerun_1024
379	    metric: ner.sj_rho_full
380	    value: 0.36
381	  - exp_id: exp_001_seed42_v2
382	    metric: sj_rho_full
383	    value: 0.428
384	  - exp_id: exp_001_seed123_v2
385	    metric: sj_rho_full
386	    value: 0.424
387	  - exp_id: exp_001_seed456_v2_ner
388	    metric: full.SJ.rho
389	    value: 0.384
390	  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'
391	- id: c027_llama_conll_3seed
392	  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'
393	  sections:
394	  - experiments
395	  tier: 1
396	  evidence:
397	  - exp_id: exp_017_llama_conll_n16
398	    metric: full.SJ_rho
399	    value: 0.4642
400	  - exp_id: exp_017_llama_conll_n16_s123
401	    metric: full.SJ_rho
402	    value: 0.4698
403	  - exp_id: exp_017_llama_conll_n16_s456
404	    metric: full.SJ_rho
405	    value: 0.4552
406	  - exp_id: exp_017_llama_conll_n16
407	    metric: full.logprob_rho
408	    value: 0.3058
409	  - exp_id: exp_017_llama_conll_n16_s123
410	    metric: full.logprob_rho
411	    value: 0.3161
412	  - exp_id: exp_017_llama_conll_n16_s456
413	    metric: full.logprob_rho
414	    value: 0.3078
415	- id: c028_loo_sj_circularity
416	  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible
417	  sections:
418	  - experiments
419	  tier: 1
420	  evidence:
421	  - exp_id: exp_015_v2
422	    metric: loo_sj.max_delta_rho
423	    value: 0.000305
424	  - exp_id: exp_015_v2
425	    metric: loo_sj.all_no_circularity
426	    value: true
427	- id: c029_llama_scierc_cross_model
428	  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;
429	    conditional RE SJ ρ=0.405 > FK ρ=0.259'
430	  sections:
431	  - experiments
432	  tier: 1
433	  evidence:
434	  - exp_id: exp_007_llama_inference
435	    metric: ner.rho_sj
436	    value: 0.363
437	  - exp_id: exp_007_llama_inference
438	    metric: ner.rho_fk
439	    value: 0.327
440	  - exp_id: exp_007_llama_inference
441	    metric: re.sj_rho_cond
442	    value: 0.405
443	  - exp_id: exp_007_llama_inference
444	    metric: re.fk_rho_cond
445	    value: 0.259
446	- id: c030_em_conditional_dominance
447	  text: 'EM ranks #1 on conditional set across all 4 configurations'
448	  sections:
449	  - experiments
450	  tier: 1
451	  evidence:
452	  - exp_id: exp_015_metrics_expansion
453	    metric: ner.em_rho_cond
454	    value: 0.3427
455	  - exp_id: exp_015_metrics_expansion
456	    metric: re.em_rho_cond
457	    value: 0.3607
458	  - exp_id: exp_002_conll_n16
459	    metric: conditional.EM_rho
460	    value: 0.4658
461	  - exp_id: exp_017_llama_conll_n16_s123
462	    metric: conditional.EM_rho
463	    value: 0.4732
464	  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,
465	    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different
466	    seed/N combinations.'
467	- id: c031_em_conditional_scierc
468	  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'
469	  sections:
470	  - experiments
471	  tier: 1
472	  evidence:
473	  - exp_id: exp_001_ner_n16_scierc
474	    metric: ner_cond_em_rho
475	    value: 0.414
476	  - exp_id: exp_001_ner_n16_scierc
477	    metric: re_cond_em_rho
478	    value: 0.475
479	  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'
480	- id: c032_logprob_re_cond_collapse
481	  text: Logprob conditional RE collapses to ρ=0.011
482	  sections:
483	  - experiments
484	  tier: 1
485	  evidence:
486	  - exp_id: exp_012_rerun_1024
487	    metric: re_cond.logprob.rho
488	    value: 0.0112
489	  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).
490	    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text
491	    0.002 was stale and untraceable.'
492	- id: c033_sj_n16_cond_re
493	  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026
494	  sections:
495	  - experiments
496	  - discussion
497	  tier: 1
498	  evidence:
499	  - exp_id: exp_008_re_n16_v2
500	    metric: sj_rho_cond
501	    value: 0.308
502	- id: c034_structural_over_logprob_n16
503	  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124
504	    to +0.175)
505	  sections:
506	  - experiments
507	  - discussion
508	  tier: 1
509	  evidence:
510	  - exp_id: exp_001_ner_n16_scierc
511	    metric: ner_voting_conf_rho
512	    value: 0.399
513	  - exp_id: exp_001_ner_n16_scierc
514	    metric: ner_logprob_rho
515	    value: 0.237
516	  - exp_id: exp_002_conll_n16
517	    metric: full.EM_rho
518	    value: 0.4627
519	  - exp_id: exp_002_conll_n16
520	    metric: full.logprob_rho
521	    value: 0.3146
522	  - exp_id: exp_007_llama_n16
523	    metric: full.voting_conf_rho
524	    value: 0.4515
525	  - exp_id: exp_007_llama_n16
526	    metric: full.logprob_rho
527	    value: 0.2041
528	  - exp_id: exp_017_llama_conll_n16
529	    metric: full.SJ_rho
530	    value: 0.4642
531	  - exp_id: exp_017_llama_conll_n16
532	    metric: full.logprob_rho
533	    value: 0.3058
534	- id: c035_n_scaling_diminishing
535	  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'
536	  sections:
537	  - discussion
538	  tier: 1
539	  evidence:
540	  - exp_id: exp_001_seed42_v2
541	    metric: sj_rho_full
542	    value: 0.428
543	  - exp_id: exp_015_metrics_expansion
544	    metric: ner.sj_rho_full
545	    value: 0.3565
546	  - exp_id: exp_017_llama_conll_n16
547	    metric: full.SJ_rho
548	    value: 0.4642
549	  - exp_id: exp_017_llama_conll_infer
550	    metric: full.SJ_rho
551	    value: 0.4314
552	  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)
553	    - 0.431 = +0.032'
554	- id: c036_sj_ece_calibration
555	  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across
556	    settings)'
557	  sections: []
558	  tier: X
559	  evidence: []
560	  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)
561	    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all
562	    signals ECE 0.27-0.77.
563	- id: C001
564	  location:
565	    section: abstract
566	    paragraph: 0
567	    sentence: 0
568	  text: No signal significantly improves sample selection over greedy decoding despite
569	    13-18pp oracle headroom
570	  type: empirical
571	  evidence:
572	  - exp_012_rerun_1024
573	  decisions:
574	  - D070
575	  - D071
576	  deprecated: false
577	- id: C003
578	  location:
579	    section: abstract
580	    paragraph: 0
581	    sentence: 0
582	  text: LP scores compressed into effective ties for 60% of instances under constrained
583	    decoding
584	  type: empirical
585	  evidence:
586	  - exp_012_rerun_1024
587	  decisions: []
588	  deprecated: false
589	- id: C006
590	  location:
591	    section: abstract
592	    paragraph: 0
593	    sentence: 0
594	  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)
595	  type: empirical
596	  evidence:
597	  - exp_012_rerun_1024
598	  decisions: []
599	  deprecated: false
600	- id: C010
601	  location:
602	    section: abstract
603	    paragraph: 0
604	    sentence: 0
605	  text: Constrained-decoding score compression is the primary bottleneck
606	  type: empirical
607	  evidence:
608	  - exp_012_rerun_1024
609	  decisions: []
610	  deprecated: false
611	- id: C011
612	  location:
613	    section: discussion
614	    paragraph: 0
615	    sentence: 0
616	  text: LP carries useful per-sample quality information; score compression is the
617	    primary bottleneck
618	  type: empirical
619	  evidence:
620	  - exp_012_rerun_1024
621	  decisions:
622	  - D071
623	  deprecated: false
624	- id: C013
625	  location:
626	    section: discussion
627	    paragraph: 0
628	    sentence: 0
629	  text: MBR utility correlates with F1 across instances but not within
630	  type: empirical
631	  evidence:
632	  - exp_012_rerun_1024
633	  decisions: []
634	  deprecated: false
635	- id: C016
636	  location:
637	    section: discussion
638	    paragraph: 0
639	    sentence: 0
640	  text: Free-form ablation would test if bottleneck is decoding-regime-specific
641	  type: planned
642	  evidence: []
643	  decisions:
644	  - D071
645	  deprecated: false
646	- id: C017
647	  location:
648	    section: conclusion
649	    paragraph: 0
650	    sentence: 0
651	  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail
652	    at selection
653	  type: empirical
654	  evidence:
655	  - exp_012_rerun_1024
656	  decisions: []
657	  deprecated: false
658	- id: C019
659	  location:
660	    section: conclusion
661	    paragraph: 0
662	    sentence: 0
663	  text: LP fails due to constrained-decoding score compression
664	  type: empirical
665	  evidence:
666	  - exp_012_rerun_1024
667	  decisions: []
668	  deprecated: false
669	- id: C022
670	  location:
671	    section: conclusion
672	    paragraph: 0
673	    sentence: 0
674	  text: RE findings preliminary, single benchmark
675	  type: scope_limitation
676	  evidence:
677	  - exp_012_rerun_1024
678	  decisions: []
679	  deprecated: false
680	- id: C023
681	  location:
682	    section: sections/discussion
683	    paragraph: 0
684	    sentence: 0
685	  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence
686	    LP on SciERC, but selection performs worse (-2.0pp)
687	  type: quantitative
688	  evidence:
689	  - exp_id: exp_entity_token_lp
690	    metric: scierc_entity_lp_variance_ratio
691	    value: 4.0x
692	  - exp_id: exp_entity_token_lp
693	    metric: scierc_entity_lp_selection_delta
694	    value: -1.68
695	  decisions: []
696	  deprecated: false
697	- id: C024
698	  location:
699	    section: sections/discussion
700	    paragraph: 0
701	    sentence: 0
702	  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with
703	    79% tied
704	  type: quantitative
705	  evidence:
706	  - exp_id: exp_entity_token_lp
707	    metric: conll_entity_lp_variance_median
708	    value: 2e-10
709	  - exp_id: exp_entity_token_lp
710	    metric: conll_entity_lp_tied_fraction
711	    value: 0.794
712	  decisions: []
713	  deprecated: false
714	- id: C025
715	  location:
716	    section: sections/discussion
717	    paragraph: 0
718	    sentence: 0
719	  text: Entity-token LP rules out format-token dilution as primary cause; points to
720	    intrinsic model overconfidence on entity tokens
721	  type: interpretive
722	  evidence:
723	  - exp_id: exp_entity_token_lp
724	  decisions: []
725	  deprecated: false
726	- id: C026
727	  location:
728	    section: sections/limitations
729	    paragraph: 0
730	    sentence: 0
731	  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches
732	    are unexplored
733	  type: scope
734	  evidence:
735	  - exp_id: exp_entity_token_lp
736	  decisions: []
737	  deprecated: false
738	- id: C027
739	  location:
740	    section: sections/introduction
741	    paragraph: 0
742	    sentence: 0
743	  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance
744	    failure are the findings'
745	  type: structural
746	  evidence: []
747	  decisions: []
748	  deprecated: false
749	- id: C028
750	  location:
751	    section: sections/introduction
752	    paragraph: 0
753	    sentence: 0
754	  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous
755	    characterization'
756	  type: structural
757	  evidence: []
758	  decisions: []
759	  deprecated: false
760	- id: C029
761	  location:
762	    section: sections/introduction
763	    paragraph: 0
764	    sentence: 0
765	  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'
766	  type: structural
767	  evidence:
768	  - exp_id: exp_entity_token_lp
769	  decisions: []
770	  deprecated: false
771	- id: C030
772	  location:
773	    section: sections/abstract
774	    paragraph: 0
775	    sentence: 0
776	  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up
777	    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined
778	    from 9 to 6 sentences'
779	  type: structural
780	  evidence: []
781	  decisions: []
782	  deprecated: false
783	- id: C031
784	  location:
785	    section: sections/discussion
786	    paragraph: 0
787	    sentence: 0
788	  text: 21% of SciERC instances produce identical F1 across all N samples
789	  type: quantitative
790	  evidence: Q1 within-instance analysis
791	  decisions: []
792	  deprecated: false
793	- id: C032
794	  location:
795	    section: sections/discussion
796	    paragraph: 0
797	    sentence: 0
798	  text: 58% of CoNLL instances produce identical F1 across all N samples
799	  type: quantitative
800	  evidence: Q1 within-instance analysis
801	  decisions: []
802	  deprecated: false
803	- id: C033
804	  location:
805	    section: sections/discussion
806	    paragraph: 0
807	    sentence: 0
808	  text: 13% of SciERC instances yield constant utility scores
809	  type: quantitative
810	  evidence: Q1 within-instance analysis
811	  decisions: []
812	  deprecated: false
813	- id: C034
814	  location:
815	    section: sections/discussion
816	    paragraph: 0
817	    sentence: 0
818	  text: 49% of CoNLL instances yield constant utility scores
819	  type: quantitative
820	  evidence: Q1 within-instance analysis
821	  decisions: []
822	  deprecated: false
823	- id: C035
824	  location:
825	    section: sections/discussion
826	    paragraph: 0
827	    sentence: 0
828	  text: SJ median within-instance rho = 0.524 on SciERC
829	  type: quantitative
830	  evidence: Q1 within-instance analysis
831	  decisions: []
832	  deprecated: false
833	- id: C036
834	  location:
835	    section: sections/discussion
836	    paragraph: 0
837	    sentence: 0
838	  text: SJ median within-instance rho = 0.994 on CoNLL
839	  type: quantitative
840	  evidence: Q1 within-instance analysis
841	  decisions: []
842	  deprecated: false
843	- id: C037
844	  location:
845	    section: sections/discussion
846	    paragraph: 0
847	    sentence: 0
848	  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances
849	  type: quantitative
850	  evidence: Q1 within-instance analysis
851	  decisions: []
852	  deprecated: false
853	- id: C038
854	  location:
855	    section: sections/discussion
856	    paragraph: 0
857	    sentence: 0
858	  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances
859	  type: quantitative
860	  evidence: Q1 within-instance analysis
861	  decisions: []
862	  deprecated: false
863	- id: C039
864	  location:
865	    section: sections/discussion
866	    paragraph: 0
867	    sentence: 0
868	  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies
869	  type: quantitative
870	  evidence: SF4 greedy data
871	  decisions: []
872	  deprecated: false
873	tables:
874	- id: tab:notation
875	  section: method
876	  caption: Notation used throughout the paper
877	  evidence: []
878	  note: Notation table—no experimental data.
879	- id: tab:quality_estimation
880	  section: experiments
881	  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)
882	  evidence:
883	  - exp_id: exp_012_rerun_1024
884	    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)
885	  - exp_id: exp_015_metrics_expansion
886	    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix
887	  - exp_id: exp_015_v2
888	    role: AUROC values across settings
889	  - exp_id: exp_002
890	    role: CoNLL Qwen N=8 ρ and AUROC
891	  - exp_id: exp_017_llama_conll_infer
892	    role: CoNLL LLaMA N=8 ρ and AUROC
893	  - exp_id: exp_017_llama_conll_n16
894	    role: LLaMA CoNLL N=16 3-seed (seed=42)
895	  - exp_id: exp_017_llama_conll_n16_s123
896	    role: LLaMA CoNLL N=16 3-seed (seed=123)
897	  - exp_id: exp_017_llama_conll_n16_s456
898	    role: LLaMA CoNLL N=16 3-seed (seed=456)
899	- id: tab:selection
900	  section: experiments
901	  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)
902	  evidence:
903	  - exp_id: exp_016_signal_ensemble
904	    role: All selection F1 values (NER and RE)
905	- id: tab:robustness
906	  section: experiments
907	  caption: Signal robustness across configurations (Spearman ρ)
908	  evidence:
909	  - exp_id: exp_005
910	    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)
911	  - exp_id: exp_015_metrics_expansion
912	    role: N=8 baseline values
913	  - exp_id: exp_001_seed42_v2
914	    role: N=16 SJ ρ seed=42
915	  - exp_id: exp_001_seed123_v2
916	    role: N=16 SJ ρ seed=123
917	  - exp_id: exp_001_seed456_v2_ner
918	    role: N=16 SJ ρ seed=456
919	  - exp_id: exp_017_llama_conll_n16
920	    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'
921	  - exp_id: exp_017_llama_conll_n16_s123
922	    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'
923	  - exp_id: exp_017_llama_conll_n16_s456
924	    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'
925	figures:
926	- id: fig:overview
927	  section: introduction
928	  caption: The correlation-selection gap conceptual diagram
929	  evidence:
930	  - exp_id: exp_015_metrics_expansion
931	    role: Quality estimation data (ρ, AUROC for left panel)
932	  - exp_id: exp_016_signal_ensemble
933	    role: Selection F1 data (right panel)
934	- id: fig:signal_heatmap
935	  section: experiments
936	  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations
937	  evidence:
938	  - exp_id: exp_015_metrics_expansion
939	    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)
940	  - exp_id: exp_002
941	    role: CoNLL Qwen full set ρ values
942	  - exp_id: exp_001_ner_n16_scierc
943	    role: Conditional set ρ values
944	- id: fig:selection_gap
945	  section: experiments
946	  caption: The correlation-selection gap on SciERC (N=8)
947	  evidence:
948	  - exp_id: exp_016_signal_ensemble
949	    role: Best-of-N selection F1 bars and quality estimation ρ line
950	- id: fig:temperature_robustness
951	  section: experiments
952	  caption: Temperature robustness on SciERC (N=8)
953	  evidence:
954	  - exp_id: exp_005
955	    role: SJ, FK ρ values at T=0.7 and T=1.0
956	- id: fig:reliability
957	  section: experiments
958	  caption: Reliability diagrams on SciERC (N=8, T=1.0)
959	  evidence:
960	  - exp_id: exp_015_metrics_expansion
961	    role: Calibration/ECE data for all signals
962	  - exp_id: exp_002
963	    role: ECE values across signals
964	_completeness:
965	  coverage: 58/68
966	  claims: 63
967	  tables: 4
968	  figures: 5
969	  tier_counts:
970	    tier1: 0
971	    tier2: 58
972	    tier3: 10
973	    tierX: 0
974	  last_checked: '2026-05-16T08:28:21.070042+00:00'
975	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "8c60a35a-d1aa-47e7-80cb-8870da9e53b6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml",
      "content": "paper:\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\n    Signals for Test-Time Scaling in Information Extraction'\n  version: 100\n  generated_at: '2026-05-16T08:28:21.069996+00:00'\n  source: manual provenance build by Paper Agent\nclaims:\n- id: c001_voting_rho_scierc_ner\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\n    artifact)\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  - related_work\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.voting_rho_full\n    value: 0.379\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\n    via exp_012_rerun_1024 (max_tokens=1024).\n- id: c002_auroc_dissociation_scierc\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\n    Voting leads ρ (NER 0.379, RE 0.422)\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.em_auroc\n    value: 0.749\n  - exp_id: exp_012_rerun_1024\n    metric: re.em_auroc\n    value: 0.706\n  - exp_id: exp_012_rerun_1024\n    metric: ner.voting_auroc\n    value: 0.684\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\n    claim changed from \"entity voting achieves ρ=0.38 and AUROC=0.74\" to split ρ (Voting\n    0.38) / AUROC (EM 0.75) claim.\n- id: c003_sj_rho_scierc_ner\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.sj_rho_full\n    value: 0.36\n  - exp_id: exp_004_re_diagnostic\n    metric: bootstrap_ci_95.ner_sj\n    value:\n    - 0.2946\n    - 0.4586\n- id: c004_voting_leads_re\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: re.voting_rho_full\n    value: 0.35\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\n- id: c005_fk_beats_sj_re\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: re.fk_rho_full\n    value: 0.275\n  - exp_id: exp_012_rerun_1024\n    metric: re.sj_rho_full\n    value: 0.25\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\n- id: c006_re_40pct_zero_f1\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: mvp_pilot_004\n    metric: re_sample_f1_pct_zero\n    value: 44.3\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\n  - exp_id: exp_008_re_n16_v2\n    metric: f1_zero_pct\n    value: 44.3\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\n- id: c007_em_leads_conll\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_002\n    metric: em_rho_full\n    value: 0.4507\n  - exp_id: exp_002\n    metric: em_auroc_full\n    value: 0.8156\n  - exp_id: exp_015_v2\n    metric: auroc_best.EM.conll_ner\n    value: 0.8156\n- id: c008_cross_model_sj_stability\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_002\n    metric: sj_rho_full\n    value: 0.4357\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.SJ_rho\n    value: 0.4314\n- id: c009_logprob_paradox\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.logprob_AUROC\n    value: 0.761\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.logprob_rho\n    value: 0.3072\n- id: c010_conll_oracle_headroom\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_002\n    metric: oracle_headroom\n    value: 0.042\n  - exp_id: exp_017_llama_conll_infer\n    metric: oracle_headroom\n    value: 0.0177\n- id: c011_ner_no_reliable_selection\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\n    bootstrap)\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  - related_work\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_ner\n    value:\n      greedy: 0.644\n      logprob: 0.65\n      sj: 0.645\n      voting: 0.634\n      random: 0.608\n      oracle: 0.776\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: bootstrap_selection_test\n    value:\n      logprob_vs_greedy_p: 0.39\n      ci_95:\n      - -0.03\n      - 0.042\n      cohens_d: 0.038\n      sign_test: 61W/70L\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\n    with c012 — no signal reliably helps on either task.\n- id: c012_re_no_signal_beats_greedy\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_re\n    value:\n      greedy: 0.404\n      logprob: 0.395\n      sj: 0.386\n      voting: 0.359\n      random: 0.354\n      oracle: 0.585\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \"only logprob\n    helps on RE (+2.3pp)\". Corrected via exp_016_rerun_1024_bootstrap.\n- id: c013_oracle_headroom_ner\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_ner.oracle\n    value: 0.776\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_ner.greedy\n    value: 0.644\n- id: c014_re_oracle_headroom\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_re.oracle\n    value: 0.585\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_re.greedy\n    value: 0.404\n- id: c015_ensemble_auroc\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\n  sections:\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: ensemble_ner_auroc\n    value: 0.666\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\n    finding.\n- id: c016_ece_calibration\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\n    miscalibration (ECE 0.109-0.339)\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: calibration_ece\n    value:\n      ner_range: 0.069-0.096\n      re_range: 0.109-0.339\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\n    moderate miscalibration. Consistent with fig_reliability_1024.\n- id: c017_fisher_z_ner_vs_re\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_004_re_diagnostic\n    metric: fisher_z_ner_vs_re.sj_z\n    value: 2.31\n  - exp_id: exp_004_re_diagnostic\n    metric: fisher_z_ner_vs_re.sj_p\n    value: 0.0209\n- id: c018_per_relation_diagnostic\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_004_re_diagnostic\n    metric: per_relation_type.FEATURE-OF.rho_sj\n    value: 0.004\n  - exp_id: exp_004_re_diagnostic\n    metric: per_relation_type.HYPONYM-OF.rho_fk\n    value: 0.646\n- id: c019_entity_span_errors\n  text: Entity span errors account for 55.5% of RE false negatives\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_004_re_diagnostic\n    metric: error_propagation\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\n      21.7% → entity span errors ~55.5%\n  note: Computed from error_propagation breakdown in exp_004\n- id: c020_capability_stratification_ner\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_009_capability_stratification\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\n    value: 0.547\n  - exp_id: exp_009_capability_stratification\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\n    value: 0.415\n- id: c021_wnut_boundary\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\n  sections:\n  - experiments\n  - conclusion\n  tier: 1\n  evidence:\n  - exp_id: exp_003_wnut17_eval\n    metric: rho_sj\n    value: 0.089\n  - exp_id: exp_003_wnut17_eval\n    metric: sample_f1_pct_zero\n    value: 53.7\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\n- id: c022_wnut_logprob_negative\n  text: WNUT logprob shows strong negative correlation\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_003_ner_wnut17\n    metric: ner.rho_logprob_full\n    value: -0.414\n  - exp_id: exp_003_wnut17_eval\n    metric: rho_logprob_full\n    value: -0.409\n- id: c023_re_sent_length_sj\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\n  sections:\n  - experiments\n  tier: 2\n  evidence:\n  - exp_id: exp_009_v2_re_rerun\n    metric: by_sent_len_quartiles\n    value:\n      Q1_sj_rho: 0.11\n      Q4_sj_rho: 0.473\n      fisher_z_p: 0.004\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\n- id: c024_high_complexity_re_subset\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\n  sections:\n  - experiments\n  tier: 2\n  evidence:\n  - exp_id: exp_009_capability_stratification\n    metric: scierc_re.by_rel_count\n    value:\n      6plus_sj_rho: 0.527\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\n    logprob values not in registry summary.\n- id: c025_temperature_sj_stable\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_005\n    metric: sj_rho_t07_ner\n    value: 0.388\n  - exp_id: exp_012_rerun_1024\n    metric: ner.sj_rho_full\n    value: 0.36\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\n- id: c026_n_scaling_sj\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\n    SciERC NER\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.sj_rho_full\n    value: 0.36\n  - exp_id: exp_001_seed42_v2\n    metric: sj_rho_full\n    value: 0.428\n  - exp_id: exp_001_seed123_v2\n    metric: sj_rho_full\n    value: 0.424\n  - exp_id: exp_001_seed456_v2_ner\n    metric: full.SJ.rho\n    value: 0.384\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\n- id: c027_llama_conll_3seed\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.SJ_rho\n    value: 0.4642\n  - exp_id: exp_017_llama_conll_n16_s123\n    metric: full.SJ_rho\n    value: 0.4698\n  - exp_id: exp_017_llama_conll_n16_s456\n    metric: full.SJ_rho\n    value: 0.4552\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.logprob_rho\n    value: 0.3058\n  - exp_id: exp_017_llama_conll_n16_s123\n    metric: full.logprob_rho\n    value: 0.3161\n  - exp_id: exp_017_llama_conll_n16_s456\n    metric: full.logprob_rho\n    value: 0.3078\n- id: c028_loo_sj_circularity\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_015_v2\n    metric: loo_sj.max_delta_rho\n    value: 0.000305\n  - exp_id: exp_015_v2\n    metric: loo_sj.all_no_circularity\n    value: true\n- id: c029_llama_scierc_cross_model\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_007_llama_inference\n    metric: ner.rho_sj\n    value: 0.363\n  - exp_id: exp_007_llama_inference\n    metric: ner.rho_fk\n    value: 0.327\n  - exp_id: exp_007_llama_inference\n    metric: re.sj_rho_cond\n    value: 0.405\n  - exp_id: exp_007_llama_inference\n    metric: re.fk_rho_cond\n    value: 0.259\n- id: c030_em_conditional_dominance\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    metric: ner.em_rho_cond\n    value: 0.3427\n  - exp_id: exp_015_metrics_expansion\n    metric: re.em_rho_cond\n    value: 0.3607\n  - exp_id: exp_002_conll_n16\n    metric: conditional.EM_rho\n    value: 0.4658\n  - exp_id: exp_017_llama_conll_n16_s123\n    metric: conditional.EM_rho\n    value: 0.4732\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\n    seed/N combinations.'\n- id: c031_em_conditional_scierc\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_001_ner_n16_scierc\n    metric: ner_cond_em_rho\n    value: 0.414\n  - exp_id: exp_001_ner_n16_scierc\n    metric: re_cond_em_rho\n    value: 0.475\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\n- id: c032_logprob_re_cond_collapse\n  text: Logprob conditional RE collapses to ρ=0.011\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: re_cond.logprob.rho\n    value: 0.0112\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\n    0.002 was stale and untraceable.'\n- id: c033_sj_n16_cond_re\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_008_re_n16_v2\n    metric: sj_rho_cond\n    value: 0.308\n- id: c034_structural_over_logprob_n16\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\n    to +0.175)\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_001_ner_n16_scierc\n    metric: ner_voting_conf_rho\n    value: 0.399\n  - exp_id: exp_001_ner_n16_scierc\n    metric: ner_logprob_rho\n    value: 0.237\n  - exp_id: exp_002_conll_n16\n    metric: full.EM_rho\n    value: 0.4627\n  - exp_id: exp_002_conll_n16\n    metric: full.logprob_rho\n    value: 0.3146\n  - exp_id: exp_007_llama_n16\n    metric: full.voting_conf_rho\n    value: 0.4515\n  - exp_id: exp_007_llama_n16\n    metric: full.logprob_rho\n    value: 0.2041\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.SJ_rho\n    value: 0.4642\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.logprob_rho\n    value: 0.3058\n- id: c035_n_scaling_diminishing\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\n  sections:\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_001_seed42_v2\n    metric: sj_rho_full\n    value: 0.428\n  - exp_id: exp_015_metrics_expansion\n    metric: ner.sj_rho_full\n    value: 0.3565\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.SJ_rho\n    value: 0.4642\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.SJ_rho\n    value: 0.4314\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\n    - 0.431 = +0.032'\n- id: c036_sj_ece_calibration\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\n    settings)'\n  sections: []\n  tier: X\n  evidence: []\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\n    signals ECE 0.27-0.77.\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: No signal significantly improves sample selection over greedy decoding despite\n    13-18pp oracle headroom\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions:\n  - D070\n  - D071\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: LP scores compressed into effective ties for 60% of instances under constrained\n    decoding\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Constrained-decoding score compression is the primary bottleneck\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: LP carries useful per-sample quality information; score compression is the\n    primary bottleneck\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions:\n  - D071\n  deprecated: false\n- id: C013\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: MBR utility correlates with F1 across instances but not within\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\n  type: planned\n  evidence: []\n  decisions:\n  - D071\n  deprecated: false\n- id: C017\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\n    at selection\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C019\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: LP fails due to constrained-decoding score compression\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: RE findings preliminary, single benchmark\n  type: scope_limitation\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\n    LP on SciERC, but selection performs worse (-2.0pp)\n  type: quantitative\n  evidence:\n  - exp_id: exp_entity_token_lp\n    metric: scierc_entity_lp_variance_ratio\n    value: 4.0x\n  - exp_id: exp_entity_token_lp\n    metric: scierc_entity_lp_selection_delta\n    value: -1.68\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\n    79% tied\n  type: quantitative\n  evidence:\n  - exp_id: exp_entity_token_lp\n    metric: conll_entity_lp_variance_median\n    value: 2e-10\n  - exp_id: exp_entity_token_lp\n    metric: conll_entity_lp_tied_fraction\n    value: 0.794\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\n    intrinsic model overconfidence on entity tokens\n  type: interpretive\n  evidence:\n  - exp_id: exp_entity_token_lp\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: sections/limitations\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\n    are unexplored\n  type: scope\n  evidence:\n  - exp_id: exp_entity_token_lp\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\n    failure are the findings'\n  type: structural\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\n    characterization'\n  type: structural\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\n  type: structural\n  evidence:\n  - exp_id: exp_entity_token_lp\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: sections/abstract\n    paragraph: 0\n    sentence: 0\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\n    from 9 to 6 sentences'\n  type: structural\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 21% of SciERC instances produce identical F1 across all N samples\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 58% of CoNLL instances produce identical F1 across all N samples\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C033\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 13% of SciERC instances yield constant utility scores\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 49% of CoNLL instances yield constant utility scores\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: SJ median within-instance rho = 0.524 on SciERC\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: SJ median within-instance rho = 0.994 on CoNLL\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\n  type: quantitative\n  evidence: SF4 greedy data\n  decisions: []\n  deprecated: false\ntables:\n- id: tab:notation\n  section: method\n  caption: Notation used throughout the paper\n  evidence: []\n  note: Notation table—no experimental data.\n- id: tab:quality_estimation\n  section: experiments\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\n  - exp_id: exp_015_metrics_expansion\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\n  - exp_id: exp_015_v2\n    role: AUROC values across settings\n  - exp_id: exp_002\n    role: CoNLL Qwen N=8 ρ and AUROC\n  - exp_id: exp_017_llama_conll_infer\n    role: CoNLL LLaMA N=8 ρ and AUROC\n  - exp_id: exp_017_llama_conll_n16\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\n  - exp_id: exp_017_llama_conll_n16_s123\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\n  - exp_id: exp_017_llama_conll_n16_s456\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\n- id: tab:selection\n  section: experiments\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\n  evidence:\n  - exp_id: exp_016_signal_ensemble\n    role: All selection F1 values (NER and RE)\n- id: tab:robustness\n  section: experiments\n  caption: Signal robustness across configurations (Spearman ρ)\n  evidence:\n  - exp_id: exp_005\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\n  - exp_id: exp_015_metrics_expansion\n    role: N=8 baseline values\n  - exp_id: exp_001_seed42_v2\n    role: N=16 SJ ρ seed=42\n  - exp_id: exp_001_seed123_v2\n    role: N=16 SJ ρ seed=123\n  - exp_id: exp_001_seed456_v2_ner\n    role: N=16 SJ ρ seed=456\n  - exp_id: exp_017_llama_conll_n16\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\n  - exp_id: exp_017_llama_conll_n16_s123\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\n  - exp_id: exp_017_llama_conll_n16_s456\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\nfigures:\n- id: fig:overview\n  section: introduction\n  caption: The correlation-selection gap conceptual diagram\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    role: Quality estimation data (ρ, AUROC for left panel)\n  - exp_id: exp_016_signal_ensemble\n    role: Selection F1 data (right panel)\n- id: fig:signal_heatmap\n  section: experiments\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\n  - exp_id: exp_002\n    role: CoNLL Qwen full set ρ values\n  - exp_id: exp_001_ner_n16_scierc\n    role: Conditional set ρ values\n- id: fig:selection_gap\n  section: experiments\n  caption: The correlation-selection gap on SciERC (N=8)\n  evidence:\n  - exp_id: exp_016_signal_ensemble\n    role: Best-of-N selection F1 bars and quality estimation ρ line\n- id: fig:temperature_robustness\n  section: experiments\n  caption: Temperature robustness on SciERC (N=8)\n  evidence:\n  - exp_id: exp_005\n    role: SJ, FK ρ values at T=0.7 and T=1.0\n- id: fig:reliability\n  section: experiments\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    role: Calibration/ECE data for all signals\n  - exp_id: exp_002\n    role: ECE values across signals\n_completeness:\n  coverage: 58/68\n  claims: 63\n  tables: 4\n  figures: 5\n  tier_counts:\n    tier1: 0\n    tier2: 58\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T08:28:21.070042+00:00'\n",
      "numLines": 975,
      "startLine": 1,
      "totalLines": 975
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the appendix and related_work files as well. The appendix was too long, let me read it in parts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "24fb62e0-8597-4934-ae21-fd820079dfdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmeX59JXJsvMkqf9N7jCt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25092,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25092
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

_source line 27_

Now let me read the appendix in parts and the related_work file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "17d7ae26-6027-4716-b9f5-f29bd4995ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmeX59JXJsvMkqf9N7jCt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25092,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25092
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01EycfDcvNPaLiAPWhYJfLo1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "5b34bd66-a9e6-4b99-8f6e-a6e5bb291f75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmeX59JXJsvMkqf9N7jCt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25092,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25092
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

_source line 29 · 2026-05-16T09:45:30.441Z_

<details><summary>↩ Tool result · `toolu_01EycfDcvNPaLiAPWhYJfLo1`</summary>

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
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
95	
96	To verify that Fleiss' $\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.
97	For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
103	\label{tab:fk_independence}
104	\begin{tabular}{lrcccc}
105	\toprule
106	Config & $n$ & FK mean & 95\% CI & $t$ & Split-half $r$ \\
107	\midrule
108	SciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\
109	CoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\
110	CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Table~\ref{tab:fk_independence} reports the results.
116	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.
117	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
118	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
119	
120	\section{Calibration Analysis}\label{app:calibration}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{fig_reliability}
125	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
126	\label{fig:reliability}
127	\end{figure*}
128	
129	Reliability diagrams use 10 equal-width bins.
130	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
131	
132	\section{Additional Analyses}\label{app:additional}
133	
134	\begin{figure*}[t]
135	\centering
136	\includegraphics[width=\textwidth]{fig_signal_heatmap}
137	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
138	\label{fig:signal_heatmap}
139	\end{figure*}
140	
141	\paragraph{Per-relation diagnostic.}
142	RE signal degradation is relation-specific.
143	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
144	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
145	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
146	
147	\paragraph{Capability stratification.}
148	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
149	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
150	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
151	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
152	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
153	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
154	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
155	
156	\paragraph{Length vs.\ log-probability.}
157	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
158	
159	\begin{figure}[t]
160	\centering
161	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
162	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
163	\label{fig:length_logprob_scatter}
164	\end{figure}
165	
166	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
167	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
168	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
169	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
170	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
171	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
172	Evaluation circularity is negligible.
173	
174	\paragraph{SJ normalizer robustness.}
175	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
176	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
182	\label{tab:sj_normalizer}
183	\begin{tabular}{@{}ll ccc@{}}
184	\toprule
185	Dataset & Model & $\rho$(max) & $\rho$(union) & $\Delta\rho$ \\
186	\midrule
187	CoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\
188	CoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\
189	CoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\
190	SciERC & Qwen3-8B & .360 & .365 & $-$.005 \\
191	SciERC & Qwen3-4B & .422 & .423 & $-$.001 \\
192	SciERC & LLaMA-8B & .363 & .372 & $-$.009 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\paragraph{Conditional filtering details.}
198	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
199	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
217	\toprule
218	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
219	\midrule
220	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
221	FK      & .125 & .001 & .555 & .169 & .002 \\
222	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
223	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
224	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Cross-configuration selection analysis.}
230	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
231	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
232	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
233	
234	\begin{table*}[t]
235	\centering
236	\small
237	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms single-sample in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where single-sample already exceeds 0.90.}
238	\label{tab:cross_selection}
239	\begin{tabular}{llccccccc}
240	\toprule
241	Config & $n$ & Single & Oracle & SJ & FK & EM & LP & VC \\
242	\midrule
243	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
245	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
246	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
247	\bottomrule
248	\end{tabular}
249	\end{table*}
250	
251	\paragraph{Diminishing returns of $N$-scaling.}
252	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
253	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
254	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
255	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
256	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
257	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
258	
259	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
260	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
261	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
262	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
263	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
264	
265	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
266	
267	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
268	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
269	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
270	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
271	
272	\begin{table}[t]
273	\centering
274	\small
275	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
276	\label{tab:bootstrap_signal_ci}
277	\begin{tabular}{lcc}
278	\toprule
279	Signal & $\rho$ & 95\% CI \\
280	\midrule
281	VC & +0.379 & [+0.299, +0.456] \\
282	SJ & +0.360 & [+0.277, +0.437] \\
283	EM & +0.295 & [+0.212, +0.371] \\
284	FK & +0.267 & [+0.176, +0.354] \\
285	LP & +0.205 & [+0.119, +0.291] \\
286	\bottomrule
287	\end{tabular}
288	
289	\vspace{0.5em}
290	
291	\begin{tabular}{lccc}
292	\toprule
293	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
294	\midrule
295	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
296	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
297	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
298	\bottomrule
299	\end{tabular}
300	
301	\smallskip
302	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
303	\end{table}
304	
305	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
306	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
307	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
308	
309	\section{Diversity and Selection Analysis}\label{app:diversity}
310	
311	\begin{figure*}[t]
312	\centering
313	\includegraphics[width=\textwidth]{fig_selection_gap}
314	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
315	\label{fig:selection_gap}
316	\end{figure*}
317	
318	\paragraph{Output diversity quantification.}
319	Table~\ref{tab:diversity} summarizes output diversity across configurations.
320	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
321	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
322	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.
323	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
324	
325	\begin{table}[t]
326	\centering
327	\small
328	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
329	\label{tab:diversity}
330	\begin{tabular}{lcc}
331	\toprule
332	Config & Identical & Unique \\
333	\midrule
334	Qwen/SciERC & 11\% & 43\% \\
335	LLaMA/SciERC & 18\% & 39\% \\
336	Qwen/CoNLL & 57\% & --- \\
337	LLaMA/CoNLL & 88\% & --- \\
338	WNUT-17 & 55\% & --- \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	\paragraph{Oracle-improvable fraction.}
344	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding single-sample\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
345	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
346	
347	\paragraph{Diversity-stratified selection gap.}
348	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
349	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
350	This rules out insufficient diversity as an explanation for the correlation-selection gap.
351	
352	\paragraph{TOST equivalence testing.}\label{app:tost}
353	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
354	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
355	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
356	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
357	We address this below with externally anchored equivalence margins.
358	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
359	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
360	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
361	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
362	
363	\begin{table}[t]
364	\centering
365	\small
366	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
367	\label{tab:tost}
368	\begin{tabular}{l cccc cccc}
369	\toprule
370	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
371	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
372	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
373	\midrule
374	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
375	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
376	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
377	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
378	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
379	\bottomrule
380	\end{tabular}
381	\end{table}
382	
383	\paragraph{External equivalence margins.}
384	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
385	To resolve this, we supplement with three externally grounded margins:
386	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;
387	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \cite{ratinov2009design};
388	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
389	
390	Results under these external anchors diverge sharply by configuration.
391	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
392	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\delta_{\mathrm{literature}}$.
393	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
394	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
395	
396	\section{Multi-Seed Stability}\label{app:multiseed}
397	
398	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
399	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
400	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
401	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
402	
403	\begin{table}[t]
404	\centering
405	\small
406	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
407	\label{tab:multiseed}
408	\begin{tabular}{lccccc}
409	\toprule
410	& LP & FK & SJ & VC & EM \\
411	\midrule
412	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
413	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
414	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
415	\midrule
416	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
417	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
418	\midrule
419	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
420	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
421	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
422	\bottomrule
423	\end{tabular}
424	\end{table}
425	
426	\section{Training Configuration}\label{app:training}
427	
428	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
429	
430	\begin{table}[t]
431	\centering
432	\small
433	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
434	\label{tab:training}
435	\begin{tabular}{ll}
436	\toprule
437	Parameter & Value \\
438	\midrule
439	LoRA rank / $\alpha$ & 32 / 64 \\
440	LoRA target & All linear modules \\
441	LoRA dropout & 0 \\
442	Optimizer & AdamW \\
443	Learning rate & 2e-4, cosine schedule \\
444	Warmup ratio & 0.1 \\
445	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
446	Epochs & 5 \\
447	Max sequence length & 2048 \\
448	Precision & bf16 \\
449	Gradient checkpointing & Enabled \\
450	Max gradient norm & 1.0 \\
451	Training seed & 42 \\
452	Framework & LLaMA Factory \\
453	\midrule
454	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
455	SciERC split & 1861 / 275 / 551 \\
456	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
457	& eval\_steps${=}$200, save\_limit${=}$5 \\
458	\bottomrule
459	\end{tabular}
460	\end{table}
461	
462	\paragraph{Prompt template.}
463	For NER, we use a structured prompt:
464	\begin{quote}
465	\small
466	\texttt{System:} You are an expert in Named Entity Recognition.\\
467	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
468	Text: \texttt{\{input\_text\}}\\
469	Entity types: \texttt{\{schema\_types\}}
470	\end{quote}
471	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
472	
473	\paragraph{Constrained decoding.}
474	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
475	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
476	
477	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
478	
479	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
480	We quantify the potential impact on LP scores through three complementary arguments.
481	
482	\paragraph{LP shift magnitude.}
483	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
484	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
485	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
486	
487	\paragraph{Constant prefix cancellation.}
488	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
489	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
490	
491	\paragraph{CoNLL control group.}
492	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
493	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
494	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
495	
496	\section{Log-Probability Score Compression}\label{app:logprob_ties}
497	
498	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
499	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "43aa3aa0-852c-465b-a771-393a1523a018",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms single-sample in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where single-sample already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Single & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\\ref{tab:selection}.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding single-sample\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 1017
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01NiunDUpfTvPi3sNP8tZDRZ`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "b2f13015-2afe-44be-bc3d-ba36aa08d20f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmeX59JXJsvMkqf9N7jCt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25092,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25092
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

_source line 31 · 2026-05-16T09:45:30.823Z_

<details><summary>↩ Tool result · `toolu_01NiunDUpfTvPi3sNP8tZDRZ`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy scales with model capability: CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero (\S\ref{sec:discussion}).
13	This creates an inherent tension between model quality and selection utility that we expect to intensify as models improve.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
15	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \cite{schall2025hidden} and inference efficiency \cite{yun2025price}.
17	
18	\paragraph{Uncertainty estimation and calibration.}
19	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
20	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.
21	Our structural signals instead measure agreement over output \textit{structure}, requiring no model modification.
22	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.
23	Unlike machine translation where MBR yields consistent gains \cite{freitag2022high}, we find that utility \textit{is} aligned with quality (within-instance SJ--F1 $\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.
24	\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches; our diagnosis is complementary---the bottleneck is not utility misalignment but output concentration driven by model capability (\S\ref{sec:discussion}).
25	\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.
26	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \cite{fernandes2022quality} learn per-sample scoring that may bridge this gap.
27	Conformal prediction constructs prediction sets with coverage guarantees \cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "d59be19c-ca3f-4219-9e78-9a151c716504",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \\cite{chen2024usc}, sub-claim decomposition \\cite{thirukovalluru2024atomic}, or hallucination detection \\cite{manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.\nOur experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.\nDegeneracy scales with model capability: CoNLL (91\\% single-sample F1) exhibits 58\\% degeneracy; SciERC (66\\%) shows 21\\%; WNUT-17 (48\\%) shows near-zero (\\S\\ref{sec:discussion}).\nThis creates an inherent tension between model quality and selection utility that we expect to intensify as models improve.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.\n\\citet{culotta2004confidence} and \\citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \\cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \\cite{schall2025hidden} and inference efficiency \\cite{yun2025price}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.\nOur structural signals instead measure agreement over output \\textit{structure}, requiring no model modification.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.\nUnlike machine translation where MBR yields consistent gains \\cite{freitag2022high}, we find that utility \\textit{is} aligned with quality (within-instance SJ--F1 $\\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.\n\\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches; our diagnosis is complementary---the bottleneck is not utility misalignment but output concentration driven by model capability (\\S\\ref{sec:discussion}).\n\\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \\cite{fernandes2022quality} learn per-sample scoring that may bridge this gap.\nConformal prediction constructs prediction sets with coverage guarantees \\cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the rest of the appendix (from line 500 onwards).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "c874c6b2-0b0a-4d84-9ee4-784983b9bd08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Eedjbq9VrXXLmPVfAP6EE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16073,
      "cache_read_input_tokens": 49104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16073
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

_source line 33_

Let me read the rest of the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "4e6062ee-c001-4468-9363-e4b8d689fbad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Eedjbq9VrXXLmPVfAP6EE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16073,
      "cache_read_input_tokens": 49104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16073
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

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01SXtGJwZJvvkTus5sp1FHG2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "028330ef-2587-4eb0-bc5a-6119af114ce9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Eedjbq9VrXXLmPVfAP6EE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16073,
      "cache_read_input_tokens": 49104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16073
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

_source line 35 · 2026-05-16T09:45:40.770Z_

<details><summary>↩ Tool result · `toolu_01SXtGJwZJvvkTus5sp1FHG2`</summary>

```text
500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
532	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
533	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
534	
535	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
536	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
537	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
538	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
539	
540	\begin{table}[t]
541	\centering
542	\small
543	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
544	\label{tab:epsilon_sweep}
545	\begin{tabular}{ccccc}
546	\toprule
547	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
548	\midrule
549	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
550	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
551	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
552	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
553	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
554	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
555	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
556	\bottomrule
557	\end{tabular}
558	\end{table}
559	
560	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
561	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
562	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
563	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
564	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
565	
566	\begin{table}[t]
567	\centering
568	\small
569	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
570	\label{tab:epsilon_robustness}
571	\begin{tabular}{lcccc}
572	\toprule
573	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
574	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
575	Signal & Qwen & LLaMA & Qwen & LLaMA \\
576	\midrule
577	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
578	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
579	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
580	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
581	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
587	
588	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
589	
590	\begin{table}[t]
591	\centering
592	\small
593	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
594	\label{tab:vc_quartile}
595	\begin{tabular}{lcccc}
596	\toprule
597	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
598	\midrule
599	\multicolumn{5}{l}{\textit{NER}} \\
600	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
601	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
602	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
603	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
604	\midrule
605	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
606	Q1 (low) & --- & $-$3.56 & --- & --- \\
607	Q4 (high) & --- & $+$4.01 & --- & --- \\
608	\bottomrule
609	\end{tabular}
610	\end{table}
611	
612	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
613	\begin{itemize}
614	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.
615	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\Delta$ signs across quartiles.
616	\end{itemize}
617	
618	On $^\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.
619	
620	On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.
621	
622	\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
623	
624	We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
625	RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
626	All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
627	
628	\paragraph{Quality estimation.}
629	RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).
630	The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal reflecting RE's higher sensitivity to per-sample scoring.
631	RE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\ref{fig:reliability}).
632	
633	\paragraph{Selection.}
634	Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
635	At $N{=}16$ (Qwen3-4B, Table~\ref{tab:re_n16_selection}), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.
636	
637	\paragraph{Scale ablation.}
638	At 4B scale (Qwen3-4B, $N{=}8$, $\text{seed}{=}42$), RE quality estimation shows FK $\rho{=}0.359$ and LP $\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\ $0.250$).
639	Selection remains below single-sample on RE ($\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.
640	
641	\paragraph{Free-form decoding.}
642	RE LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp across 4 seeds vs.\ $-0.9$~pp under constrained decoding at 8B; \S\ref{app:freeform_ablation}), suggesting constrained decoding's fixed template obscures LP signal in RE (\S\ref{app:mbr_discussion}).
643	
644	\section{RE Conditional Selection}\label{app:re_conditional_selection}
645	
646	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
647	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
648	All five signals underperform single-sample on both subsets.
649	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
650	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
651	
652	\begin{table}[t]
653	\centering
654	\small
655	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms single-sample on either subset.}
656	\label{tab:re_cond_selection}
657	\begin{tabular}{lcc}
658	\toprule
659	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
660	\midrule
661	Oracle & 0.585 & 0.757 \\
662	\midrule
663	LP & 0.395 & 0.600 \\
664	SJ & 0.386 & 0.604 \\
665	EM & 0.372 & 0.583 \\
666	VC & 0.359 & 0.574 \\
667	\midrule
668	Single & 0.404 & 0.674 \\
669	\bottomrule
670	\end{tabular}
671	\end{table}
672	
673	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
674	
675	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
676	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
677	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
678	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
679	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
680	
681	\begin{table}[t]
682	\centering
683	\small
684	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ single-sample. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
685	\label{tab:re_n16_selection}
686	\begin{tabular}{lccc}
687	\toprule
688	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
689	\midrule
690	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
691	\midrule
692	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
693	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
694	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
695	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
696	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
697	\midrule
698	Single & $.291{\pm}.000$ & --- & --- \\
699	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
700	\bottomrule
701	\end{tabular}
702	\end{table}
703	
704	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
705	
706	\paragraph{Connection to MBR decoding.}
707	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
708	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy---the core of the correlation-selection gap.
709	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
710	
711	\paragraph{Task-specific decoding interactions.}
712	The free-form ablation reveals divergent behavior across tasks.
713	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
714	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
715	This interaction does not generalize to NER, where selection remains negligible under both regimes.
716	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
717	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
718	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
719	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
720	
721	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
722	
723	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
724	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
725	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
726	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
727	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
728	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
729	
730	\begin{table*}[t]
731	\centering
732	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
733	\label{tab:freeform_ablation}
734	
735	\vspace{2pt}
736	{\small\textsc{Panel A: Logprob Distribution}}
737	\vspace{2pt}
738	
739	\begin{tabular}{lccc}
740	\toprule
741	Metric & Constrained & Free-form & $\Delta$ \\
742	\midrule
743	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
744	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
745	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
746	\bottomrule
747	\end{tabular}
748	
749	\vspace{8pt}
750	
751	{\small\textsc{Panel B: Selection F1}}
752	\vspace{2pt}
753	
754	\begin{tabular}{llccc}
755	\toprule
756	Task & Method & Constrained & Free-form & $\Delta$ \\
757	\midrule
758	\multirow{3}{*}{NER}
759	  & Single        & 0.6182 & 0.6204 & $+$0.0022 \\
760	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
761	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
762	\midrule
763	\multirow{3}{*}{RE}
764	  & Single        & 0.2913 & 0.2880 & $-$0.0033 \\
765	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
766	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
767	\bottomrule
768	\end{tabular}
769	
770	\vspace{8pt}
771	
772	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
773	\vspace{2pt}
774	
775	\begin{tabular}{l ccc ccc}
776	\toprule
777	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
778	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
779	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
780	\midrule
781	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
782	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
783	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
784	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
785	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
786	\bottomrule
787	\end{tabular}
788	
789	\vspace{8pt}
790	
791	{\small\textsc{Panel D: Parse Rate (Free-form)}}
792	\vspace{2pt}
793	
794	\begin{tabular}{lc}
795	\toprule
796	Metric & Value \\
797	\midrule
798	Total samples          & 4408 \\
799	Parse rate             & 99.95\% \\
800	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
801	\bottomrule
802	\end{tabular}
803	
804	\end{table*}
805	
806	\paragraph{CoNLL NER free-form results.}
807	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
808	Free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\ single-sample $0.904$ ($\Delta{=}{-}0.77$~pp).
809	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$---comparable to constrained results (Table~\ref{tab:quality_estimation}).
810	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
811	
812	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
813	
814	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
815	
816	\paragraph{Pairwise overlap.}
817	LP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
818	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
819	
820	\paragraph{Instance complexity drives failure.}
821	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
822	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
823	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
824	
825	\begin{table}[t]
826	\centering
827	\small
828	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
829	\label{tab:stable_failures}
830	\begin{tabular}{lcccc}
831	\toprule
832	Group & $n$ & Gold rels & Single F1 & LP $\Delta$F1 \\
833	\midrule
834	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
835	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
836	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
837	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
838	\bottomrule
839	\end{tabular}
840	\end{table}
841	
842	\paragraph{Flip instances.}
843	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
844	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
845	
846	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
847	
848	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
849	
850	\begin{table}[t]
851	\centering
852	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
853	\label{tab:n-scaling}
854	\small
855	\begin{tabular}{l ccc ccc}
856	\toprule
857	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
858	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
859	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
860	\midrule
861	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
862	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
863	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
864	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
865	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
866	\midrule
867	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
868	\bottomrule
869	\end{tabular}
870	\end{table}
871	
872	\begin{table}[t]
873	\centering
874	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
875	\label{tab:ranking-stability}
876	\small
877	\begin{tabular}{ll cc l}
878	\toprule
879	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
880	\midrule
881	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
882	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
883	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
884	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
885	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
886	\bottomrule
887	\end{tabular}
888	\end{table}
889	
890	\begin{table}[t]
891	\centering
892	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
893	\label{tab:sigma-comparison}
894	\small
895	\begin{tabular}{l cc cc}
896	\toprule
897	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
898	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
899	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
900	\midrule
901	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
902	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
903	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
904	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
905	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
906	\midrule
907	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
908	\bottomrule
909	\end{tabular}
910	\end{table}
911	
912	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
913	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
914	
915	\section{Cross-Dataset OOD Analysis}\label{app:ood}
916	
917	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
918	
919	\begin{table}[t]
920	\centering
921	\small
922	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
923	\label{tab:ood}
924	\begin{tabular}{l ccc ccc}
925	\toprule
926	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
927	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
928	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
929	\midrule
930	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
931	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
932	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
933	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
934	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
935	\bottomrule
936	\end{tabular}
937	\end{table}
938	
939	\paragraph{Wider-to-narrower schema transfer.}
940	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
941	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
942	
943	\paragraph{Narrower-to-wider schema transfer (excluded).}
944	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
945	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).
946	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
947	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
948	
949	\paragraph{Asymmetry interpretation.}
950	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
951	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
952	
953	\section{Verbalized Confidence}\label{app:verbalized_confidence}
954	
955	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
956	Table~\ref{tab:verbconf} reports quality estimation and selection results.
957	
958	\begin{table}[t]
959	\centering
960	\small
961	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
962	\label{tab:verbconf}
963	\begin{tabular}{l cc cc}
964	\toprule
965	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
966	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
967	Metric & VerbConf & LP & VerbConf & LP \\
968	\midrule
969	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
970	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
971	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
972	$\Delta$ vs.\ single-sample & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
973	\midrule
974	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
975	Parse fail rate & 0.26\% & --- & 0\% & --- \\
976	\bottomrule
977	\end{tabular}
978	\end{table}
979	
980	\paragraph{Severe overconfidence.}
981	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.
982	This compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.
983	
984	\paragraph{QE--selection decoupling.}
985	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
986	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
987	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
988	
989	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
990	
991	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
992	
993	\begin{table}[t]
994	\centering
995	\small
996	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Single-sample F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
997	\label{tab:llama3b}
998	\begin{tabular}{l cc cc}
999	\toprule
1000	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ single-sample \\
1001	\midrule
1002	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
1003	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
1004	EM & .334 & \textbf{.776} & --- & --- \\
1005	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
1006	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
1007	\midrule
1008	Single & --- & --- & 0.627 & --- \\
1009	Oracle & --- & --- & 0.763 & --- \\
1010	\bottomrule
1011	\end{tabular}
1012	\end{table}
1013	
1014	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.
1015	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\rho$--AUROC dissociation noted in the main text.
1016	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1017	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "3f088a58-cec4-424b-951e-a6c88da42a69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "At this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep (post-hoc exploratory).}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Consistency-Stratified Selection Analysis}\\label{app:vc_quartile}\n\nTable~\\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\\Delta$ (gain over single-sample) for LP and SJ.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n\\label{tab:vc_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\nQuartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NER}} \\\\\nQ1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\\\\nQ2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\\\\nQ3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\\\\nQ4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$^\\dagger$RE}} \\\\\nQ1 (low) & --- & $-$3.56 & --- & --- \\\\\nQ4 (high) & --- & $+$4.01 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:\n\\begin{itemize}\n\\item \\textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.\n\\item \\textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\\Delta$ signs across quartiles.\n\\end{itemize}\n\nOn $^\\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.\n\nOn CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.\n\n\\section{Exploratory Extension to Relation Extraction}\\label{app:re_extension}\n\nWe extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.\nRE produces sets of (head, relation, tail) triples with partial overlap; 40\\% of RE instances receive zero F1, and entity span errors account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect (\\S\\ref{app:additional}).\nAll RE results use Qwen3-8B unless noted; single-seed ($\\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.\n\n\\paragraph{Quality estimation.}\nRE quality estimation is reported in Table~\\ref{tab:multiseed} (3-seed means).\nThe signal ranking differs from NER: VC leads ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal reflecting RE's higher sensitivity to per-sample scoring.\nRE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\\ref{fig:reliability}).\n\n\\paragraph{Selection.}\nTable~\\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.\nAt $N{=}16$ (Qwen3-4B, Table~\\ref{tab:re_n16_selection}), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.\n\n\\paragraph{Scale ablation.}\nAt 4B scale (Qwen3-4B, $N{=}8$, $\\text{seed}{=}42$), RE quality estimation shows FK $\\rho{=}0.359$ and LP $\\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\\ $0.250$).\nSelection remains below single-sample on RE ($\\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.\n\n\\paragraph{Free-form decoding.}\nRE LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp across 4 seeds vs.\\ $-0.9$~pp under constrained decoding at 8B; \\S\\ref{app:freeform_ablation}), suggesting constrained decoding's fixed template obscures LP signal in RE (\\S\\ref{app:mbr_discussion}).\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform single-sample on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms single-sample on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nSingle & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform single-sample, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ single-sample. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nSingle & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{MBR Decoding and Task-Specific Interactions}\\label{app:mbr_discussion}\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy---the core of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Single        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Single        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\paragraph{CoNLL NER free-form results.}\nExtending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\nFree-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\\ single-sample $0.904$ ($\\Delta{=}{-}0.77$~pp).\nQuality estimation under free-form decoding yields SJ $\\rho{=}0.461$, EM $\\rho{=}0.471$, LP $\\rho{=}0.326$---comparable to constrained results (Table~\\ref{tab:quality_estimation}).\nThe failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Single F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n\n\\section{Verbalized Confidence}\\label{app:verbalized_confidence}\n\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ single-sample & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Single-sample F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ single-sample \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nSingle & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n",
      "numLines": 518,
      "startLine": 500,
      "totalLines": 1017
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me systematically extract all numerical claims and cross-check them for consistency. Let me organize my findings.

Key numerical claims to cross-check:

**Abstract:**
- ρ up to 0.38 on primary test bed (SciERC)
- 0.45 on ceiling-effect control (CoNLL)
- 21-58% of instances have identical outputs
- median ρ=0.52 (within-instance)
- 0.041 nats median within-instance LP range

**Introduction:**
- ρ=0.38, up to 0.45 on ceiling-effect control


- 13-18 percentage point oracle headroom
- 21-58% instances with identical outputs
- median ρ=0.52 within-instance
- 0.041 nats LP range
- Greedy baseline at F1=0.663, best selection method at 0.647
- 13 percentage point oracle headroom mentioned in figure caption
- 2.9 percentage point improvement for non-tied LP subset (p=0.004)

**Experiments:**
- SciERC: 551 test instances with ~65% F1
- CoNLL: 3,453 test instances with ~91% F1
- WNUT-17: 1,287 test instances with 52% zero F1

Now I'm looking at the correlation metrics across datasets. VC shows ρ=0.379 while SJ is 0.360, and EM leads on CoNLL with ρ=0.451 and AUROC=0.816. The gap between SJ and LP methods is substantial at Δρ=+0.155. The oracle achieves 0.778 versus single-sample at 0.645, giving 13.3 percentage points of headroom, though LP only gains 0.2pp (p=0.29) and greedy reaches F1=0.663. Selection methods fail to show significance across the board with all p-values above 0.05, except for the non-tied LP subset which improves by 2.9pp (p=0.004). The 4B selection method surprisingly underperforms by 3.4pp despite having 13.0pp oracle headroom available, while CoNLL shows minimal gains under 0.3pp with only 1.7pp headroom, and the 8B model exhibits severe degeneracy at 21 instances.

Looking at the discussion section, MBR closes the gap substantially—23% on SciERC and 41% on CoNLL—while a significant portion of instances show constant F1 scores (21% on SciERC, 58% on CoNLL). Greedy F1 at 0.663 outperforms all N=8 baselines, with LP's best reaching 0.647. The LP utility estimates show tight clustering with a range of 0.041 nats and interquartile range between 0.024 and 0.073.

For the next chunk, the within-instance correlation between LP and F1 is weak at 0.248, and among non-tied instances (n=210), there's a modest 2.9 percentage point improvement with statistical significance. The oracle with N=16 shows what's theoretically possible at 4.4 percentage points gain. Signal combinations don't meaningfully help, but the oracle tiebreaker achieves 7.9 percentage points—suggesting the main challenge is distinguishing tied cases. Entity-token LP exhibits much higher variance and actually hurts selection performance, while free-form approaches show more consistent behavior with a standard deviation ratio near 1.0 and modest gains of 1.8 percentage points on relation extraction.

The findings suggest medium-difficulty NER with a correlation ceiling around 0.45, where the core limitation is the prevalence of identical F1 scores across many instances and the narrow range of LP values available for discrimination.

Now examining the 8B model scale results and their limitations. The key issue is that ad-hoc combinations of LP and confidence scores only yield 0.4 percentage points over greedy selection, which isn't statistically significant—this is the main problematic finding. Confidence scores themselves are quite high (8.58/10 on SciERC, 9.24/10 on CoNLL), and the tied fraction on CoNLL reaches 95.8% at the threshold of 0.7, which severely constrains what any selection method can achieve.

Looking more carefully at the numbers, there's actually a discrepancy in the claims: the Discussion section says signal combinations improve by only 0.1 percentage points over single-sample selection, while the Limitations section claims 0.4 percentage points over greedy. But if single-sample F1 is 0.645 and the best combination is 0.1pp higher at 0.646, that's actually 1.7 percentage points *worse* than greedy's 0.663—so the "+0.4pp over greedy" claim appears to be incorrect. So the contradiction is clear: if combinations achieve +0.1pp over single-sample (0.646), that's actually -1.7pp compared to greedy (0.663), not the +0.4pp claimed in the limitations section. Either the limitations statement is wrong, or the numbers being compared are from different baselines entirely.

But wait—I'm seeing a note that the "Single" row in Table 2 might actually be mislabeled T=0 greedy, not a true single draw. If that's the case, then the table shows both Greedy (T=0) = 0.663 and Single = 0.645 as separate rows, which would mean they're genuinely different results, not the same thing. That would resolve part of the confusion, but I need to figure out what "Single" actually represents if it's not what the label claims. The method section explicitly defines "Single" as one T=1.0 draw, but the task suggests it was actually collected as T=0 greedy—which would create a contradiction since the paper also reports a separate "Greedy (T=0)" result with a different F1 score. I need to think through whether these could both be T=0 greedy with different results, or if there's another explanation for the discrepancy.

The variance reported for Single (±0.001) is actually a clue here—if it were truly deterministic T=0 greedy, there should be zero variance, but the presence of any variance suggests it's either a stochastic sample or averaged across multiple seeds. This small variance is more consistent with the paper's stated definition of Single as a T=1.0 draw rather than greedy decoding.

Let me check the provenance data to see if there's additional context about how these runs were actually executed, since the discrepancy between the two T=0 greedy results (0.663 vs 0.645) could indicate they're from different evaluation setups or there's a labeling error somewhere. I'm noticing a key inconsistency: the provenance data shows greedy F1 at 0.644 from exp_016_rerun_1024_bootstrap, but Table 2 in the paper reports 0.663, and the claim c013 about the oracle headroom is calculated using the 0.644 value. This suggests the paper may be citing results from a different experiment (exp_016_signal_ensemble) than what the provenance actually documents. I see the oracle headroom of 13-18pp actually spans two tasks: 13.3pp for NER (oracle vs single) and 18.1pp for RE, which explains the range in the introduction. But there's still a discrepancy where the provenance shows greedy at 0.644 while the paper table lists 0.663—if single is actually the T=0 greedy baseline, that might resolve the inconsistency. Looking at the reviewer's point about the inconsistency between the Discussion and Limitations sections—the Discussion claims LP×VC combinations improve by at most +0.1pp over single-sample, but the Limitations says +0.4pp over greedy, which would actually be negative relative to single-sample given the greedy F1 values. I'm also tracking three major discrepancies: the greedy F1 differs by 1.9pp between provenance (0.644) and the paper (0.663), the oracle F1 has a minor 0.2pp difference, and there's confusion about which row in the table corresponds to which baseline.

Now checking the rounding claims—the ρ values round appropriately (0.379→0.38, 0.451→0.45), but there's a discrepancy on the WNUT-17 zero F1 rate where the experiments section reports 52% while the provenance shows 54%.

Looking at the related work and discussion sections, there's ambiguity around what "48%" refers to for WNUT-17—it could mean the model's F1 performance level rather than the zero-F1 fraction, which would be a different metric entirely from the 52-54% zero-F1 rate mentioned in experiments. I'm trying to pin down where the 48% figure for WNUT-17 comes from—the paper mentions 52% of instances have zero F1, which would suggest the single-sample F1 is lower, maybe around 20-30% overall rather than 48%. Let me trace back through the discussion section to see if there's a clearer breakdown of these metrics. Looking at the WNUT-17 data more carefully: the filtered dataset has 689 instances with 334 non-zero F1 scores, meaning about 355 instances have zero F1—that's roughly 51.5%, which aligns with the 52% figure mentioned in the experiments section. But I'm still uncertain what the "48%" in the discussion actually refers to, since it doesn't cleanly match the single-sample F1 or any other metric I can identify from the documented numbers.

Wait, I think I've been misreading the sentence structure. The percentages in parentheses are all single-sample F1 levels: CoNLL has 91% single-sample F1 with 58% degeneracy, SciERC has 66% with 21% degeneracy, and WNUT-17 has 48% single-sample F1 with near-zero degeneracy. So for WNUT-17, that 48% is the single-sample F1 metric itself.

But that doesn't quite add up—if 52% of the 689 instances have zero F1 and the overall macro F1 is 48%, the math suggests the remaining instances would need to average 100% F1, which seems unrealistic.

Let me reconsider what the 48% actually represents. The paper doesn't explicitly state a single-sample F1 for WNUT, only that 52% of instances have zero F1. Maybe the 48% refers to something else entirely—possibly a degeneracy rate rather than F1—but the phrasing "shows near-zero" makes that interpretation unclear too. I think the 48% might be a typo or mislabeling for what should be the single-sample F1, though the 52% zero F1 rate elsewhere in the paper creates an inconsistency I need to resolve.

Actually, I'm realizing the 48% could work as a macro-averaged F1 if I think about it differently. If 52% of instances have zero F1 and the remaining 48% have some positive F1, the overall average would depend on how high those non-zero instances score. For instance, if those 48% of instances average around 1.0 F1, the macro average would be roughly 0.48, though realistically the non-zero instances probably score lower, which would pull the overall average down further.

Looking at the WNUT-17 appendix table, I don't actually see the single-sample F1 metric listed there—just quality estimation metrics and a diversity note showing 55% identical outputs. This makes me think the 48% figure might be mislabeled or could refer to something else entirely, like the proportion of instances with non-zero F1 rather than the F1 score itself. I should flag this as a potential inconsistency.

The SciERC numbers are also confusing me—the paper mentions around 65% F1 in the experiments, and Table 2 shows 0.645 for the single-sample metric, but the discussion seems to reference different numbers, so I'm not entirely sure what's being compared.

For WNUT specifically, if 52% of samples have zero F1 and the remaining 48% somehow averaged to perfect scores, that would only give 48% overall—which seems unrealistic. I'm wondering if the 52% zero F1 is actually a sample-level metric rather than instance-level, or if there's just an error in how these numbers are being reported.

Looking at the different sources, I'm seeing 52% in the experiments section, 54% in the provenance data, and 48% mentioned in the discussion—which might actually refer to the non-zero portion (100% - 52%). The related work section seems to suggest a pattern where single-sample F1 percentages correlate with degeneracy rates: CoNLL at 91% F1 shows 58% degeneracy, SciERC at 66% shows 21%, and WNUT-17 at 48% shows near-zero degeneracy.

But there's a wrinkle here—the experiments describe "52% zero F1" for WNUT-17's 1,287 social media instances, which appears to be an instance-level metric rather than an overall F1 score. So the 48% mentioned in the discussion and the 52% zero rate might actually be measuring different things, which explains the discrepancy. I'll note this as a potential inconsistency but move forward.

The MBR method closes 23-41% of the oracle gap according to the discussion and Table 3, with 23% for SciERC and 41% for CoNLL—that checks out. For the oracle headroom, the figure caption rounds 13.3 percentage points down to 13 pp, which is just standard rounding. Now I'm looking at the SciERC F1 discrepancy between the experiments section mentioning "≈65%" and the discussion citing "66%"—these are close enough that it's likely just rounding or measurement variation.

But there's a real problem with the Provenance VC AUROC: the provenance file shows 0.684, yet Table 1 in the paper reports 0.663. Those numbers don't align, and I need to figure out where this gap comes from.

The introduction cites ρ=0.38 for VC on SciERC, which checks out at 0.379 rounded, and mentions 0.45 as the ceiling-effect control on CoNLL, which also matches the EM value of 0.451. Now looking at the multi-seed results, the standard deviations across all entries max out around 0.025, so claiming σ≤0.026 is technically correct but slightly loose.

For the N=16 oracle headroom claim of +4.4pp, I'm cross-referencing the tables and finding that LLaMA shows +2.8pp when going from N=8 (0.778) to N=16 (0.806), which doesn't match the stated +4.4pp—I need to verify whether this is comparing different models or if there's another calculation I'm missing. The SciERC dataset details appear to be cut off mid-sentence.

Looking at the dataset sizes, SciERC has 551 test instances that filter down to 529 after excluding empty annotations, and CoNLL's 3,453 test sentences reduce to 2,756 after filtering—both are internally consistent. However, there's a discrepancy with the LP selection improvement: the experiments section reports +0.2pp (p=0.29) while the provenance data shows +0.6pp (p=0.39), so I need to determine which is the correct figure. Looking at the provenance data more carefully, I see logprob=0.650 and sj=0.645, which matches the paper's LP and Single values respectively—so the +0.6pp difference in provenance comes from comparing logprob to greedy (0.644), while the paper's +0.2pp compares LP to Single (0.645). There's also a small discrepancy between the paper's LP value of 0.647 and the provenance's 0.650, a difference of 0.003. Single 0.645 = +0.2pp). Provenance shows no single listed, but assuming greedy=single based on the task background about mislabeling, LP-greedy would be 0.650-0.644 = +0.6pp. If Single actually is greedy, then the LP versus Single comparison matches provenance c011 at +0.6pp, but the paper reports +0.2pp with slightly different values (LP 0.647 vs provenance 0.650, greedy 0.663 vs provenance 0.644), suggesting they're from different experiments—the paper cites exp_016_signal_ensemble while provenance references exp_016_rerun_1024_bootstrap.

Now looking at the NER temperature sensitivity claims: the experiments section states consistency signals are robust across temperatures 0.7 and 1.0 with sublinear scaling gains, while the main text claims LP shows the largest temperature sensitivity at Δρ=+0.044. The appendix robustness table confirms SJ has minimal temperature variation (0.364 to 0.360, Δ=0.004) while LP shows the claimed sensitivity (0.249 to 0.205, Δ=0.044), but provenance c025 appears to have additional information that's cut off. I'm checking the abstract claims against the actual results—the "up to 0.38" refers to VC's best performance of 0.379 on SciERC, while the "0.45" is EM's 0.451 on CoNLL, which are different models on different datasets, not the same signal as the abstract might suggest.

The conclusion mentions testing a 3B-8B model range, and looking at what was actually used—Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B, plus LLaMA-3.2-3B in the appendix—that range checks out.

Now I'm noticing a discrepancy with the Provenance c002 results: it claims EM leads on AUROC for NER at 0.749 and RE at 0.706, but Table 1 shows VC's AUROC as 0.663, which doesn't align with what Provenance is reporting.

Looking more carefully at Table 1's structure, the columns represent different datasets and metrics—SciERC (ρ, AUC), CoNLL Qwen (ρ, AUC), and CoNLL LLaMA (ρ, AUC)—so VC's SciERC AUROC is indeed 0.663, but I need to find where EM's SciERC AUROC appears in the table.

Now I see EM Surface shows 0.295 and 0.614, meaning EM's SciERC AUROC is 0.614. But the provenance notes mention 0.749 for EM NER AUROC from a corrected experiment, which doesn't match what's currently displayed in Table 1—there's a discrepancy between what the paper shows and what the provenance documentation claims about the corrected values. Looking at the multi-seed results, I see VC AUROC = 0.697 and EM = 0.661 as 3-seed averages, but Table 1 shows VC = 0.663 and EM = 0.614 for a single seed. The discrepancy suggests Table 1 might be using seed 42 specifically, while the multi-seed table averages across seeds 42, 123, and 456—which would mean the other seeds produced notably higher scores for both models. I'm realizing this is a contradiction—the first term alone exceeds the total sum of squares, so either the seed=42 value for VC isn't 0.663, or there's an error in the multi-seed statistics. Let me look more carefully at the table headers to see what's actually being reported.

Now I'm checking the Spearman correlation values across seeds for the same metrics, and the pattern is similar: the seed=42 result for VC is 0.379, but the multi-seed mean is 0.386±0.019, which means other seeds must be averaging higher around 0.390. The standard deviation suggests the seed=42 value should deviate from the mean by about 0.007, but the math isn't quite working out.

However, when I look at the AUROC values, there's a serious inconsistency: Table 1 reports VC AUROC as 0.663 for seed=42, but the multi-seed mean is 0.697±0.010. That deviation of 0.034 is far too large to be explained by a standard deviation of only 0.010—mathematically it's impossible. This suggests either the seed=42 value in Table 1 isn't actually from seed=42, the multi-seed values are incorrect, or they're using different evaluation protocols.

Let me check if the Spearman ρ values are consistent instead. Table 1 shows VC ρ=0.379, and the multi-seed mean is 0.386±0.019, which could work if seed=42 is slightly below the mean. But the AUROC math still doesn't work out—if seed=42 contributes 0.663 and the mean is 0.697 with such a tight standard deviation, something is fundamentally wrong with one of these numbers. The calculation confirms there's a real discrepancy—the seed=42 value of .663 can't possibly produce a mean of .697 with σ=.010 across multiple seeds, suggesting Table 1 might come from a different experimental setup than the multi-seed results. However, the NER ranking order is consistent between the two tables, with VC performing best across both.

Now looking at the signal combinations claim: if the single-sample F1 was .645 and the best combination only reached .646, that's nowhere near the "+0.4pp over greedy" improvement they're claiming, which doesn't add up. This raises a bigger question about what "Single" actually represents in Table 2—the method definition says it should be one T=1.0 draw without argmax decoding, but the task suggests it might actually be mislabeled T=0 greedy results instead.

If Single really is T=0 greedy, then having both Greedy (0.663) and Single (0.645) as separate T=0 rows makes no sense for deterministic decoding unless they're using different evaluation sets or metrics. This would mean all the comparisons claiming improvements "over single-sample"—like the +0.2pp for LP or the 13.3pp headroom for oracle—are actually being measured against greedy, not against what they claim. The 1.8pp gap between these two supposedly identical methods suggests they're fundamentally different things, not just mislabeled versions of the same approach.

Now checking the AUROC claims in Table 1 for SciERC: the table shows VC at 0.663, SJ at 0.650, and EM at 0.614, which contradicts the claim that EM leads on AUROC.

The provenance notes reference different experiments and values than what appears in the final paper table, suggesting the table was updated after the provenance was recorded. I should treat the published paper as the authoritative source and look for internal consistency issues rather than trying to reconcile with earlier experimental logs.

Now I'm systematically cataloging the major inconsistencies I've found: the Discussion claims LP×VC combinations improve by +0.1pp over single-sample baselines, but the Limitations section states +0.4pp over greedy—these can't both be accurate. The Table 1 value for VC AUROC (.663) conflicts with the multi-seed mean (.697±.010), which shouldn't happen if seed=42 is part of that distribution. And there's a substantial gap between the provenance record showing EM NER AUROC at 0.749 versus Table 1's 0.614.

Beyond those high-severity issues, I'm also tracking medium-level discrepancies: the greedy baseline shifts between 0.644 and 0.663 across sources, SciERC F1 fluctuates depending on whether it's compared against single-sample or greedy performance, and the WNUT zero-F1 rate varies across three different citations. The VC correlation for RE appears as both 0.422 and 0.350, and LP's improvement margin changes from +0.2pp to +0.6pp depending on the comparison anchor. There's also a minor Oracle F1 discrepancy between 0.778 and 0.776.

For the N=16 SJ correlation gain, the appendix reports +0.047 but the actual calculation from the three seeds yields +0.051—the mean of 0.398, 0.423, and 0.410 is approximately 0.410, which rounds to 0.411, so the gain from the baseline 0.360 should be +0.051 rather than +0.047.

The discrepancy stems from how the baseline is chosen: the N-scaling table uses a 3-seed mean baseline of 0.364 for N=8, giving a gain of +0.046, while the appendix text mixes the primary seed baseline of 0.360 with the 3-seed mean of 0.411 for N=16, yielding +0.051 but reporting it as +0.047.

Now looking at issue #7, the provenance shows a correction for the voting RE result: the text claims ρ=0.350 after correction, but the note traces it back through two experiments with different values, and the multi-seed table shows a different ρ for the same condition entirely.

The discrepancy comes down to single-seed versus multi-seed metrics—the provenance references a single-seed run while the appendix reports the 3-seed mean, so both could technically be correct but they're measuring different things.

For the "Single" definition issue, if Table 2's "Single" actually refers to T=0 greedy sampling rather than what Method.tex claims, then the method definition itself would be inaccurate, and the table footnote would need to clarify this distinction.

The ±0.001 variance on Single is the real puzzle—a deterministic T=0 greedy approach should show zero variance across seeds, but that small non-zero variance suggests either it's actually T=1.0 with minimal randomness, or something else is introducing variation in the evaluation process itself.

Maybe the explanation is that Single represents the mean F1 of individual T=1.0 samples, and the model's outputs at T=1.0 happen to be nearly identical to T=0 most of the time, making the practical behavior equivalent to greedy even though technically it's sampling. Or there could be a bug somewhere in how these results were computed.

I should flag any claims about Single and note this discrepancy. Now let me start writing the reports, but first I want to verify the VerbConf numbers across the discussion, limitations, and appendix to make sure they're consistent—checking that 8.58 rounds to 8.6 as stated. And I need to look for any other metrics that might have similar issues. I'm verifying the consistency of these key metrics across the paper—the correlation coefficient of 0.52, the range of 21-58% for affected instances, the 0.041 nats logprob range, and checking where the oracle headroom figures appear in the introduction and other sections. Looking at the specific numbers, greedy decoding at 0.663 does beat the best selection strategy at 0.647, but the oracle headroom claim needs clarification—it's 11.5pp for NER when comparing to greedy, not the 13pp mentioned for single decoding, and 18.1pp for RE across both comparisons. The phrasing in that sentence is a bit ambiguous—it references oracle headroom above single-sample (13-18pp) while discussing greedy's superiority over selection strategies, when the actual oracle gap above greedy is smaller (11.5pp for NER, 18.1pp for RE). It's not technically wrong since the paper consistently defines oracle headroom relative to single-sample, but the framing could be clearer. Now I'm ready to compile the findings into a comprehensive report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "089df791-9748-43f1-b3ab-a29a3d31cf73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLBd4DzxB447VemnfpEmfC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13925,
      "cache_read_input_tokens": 65177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13925
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

Now I have all the data. Let me create the output directory and write the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "d04b3ee5-5856-4fdc-a141-ca745d10aaba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLBd4DzxB447VemnfpEmfC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13925,
      "cache_read_input_tokens": 65177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13925
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

<details open><summary>🔧 Tool call — Bash · `toolu_01GaNoxNH4cdUcAEvwFkssfz`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit",
  "description": "Create audit output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "9a4b6ea5-eb21-464e-9f44-a5decbf8d84c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLBd4DzxB447VemnfpEmfC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13925,
      "cache_read_input_tokens": 65177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13925
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

_source line 39 · 2026-05-16T09:51:01.429Z_

<details><summary>↩ Tool result · `toolu_01GaNoxNH4cdUcAEvwFkssfz`</summary>

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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "8470e062-2b90-402c-9389-7e8e4233d807",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Write · `toolu_012Ft1V8419crGMeVBnChafX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
  "content": "# Claim Audit Report: Numerical Consistency Check\n\n**Paper**: Strong Predictors, Weak Selectors  \n**Date**: 2026-05-16  \n**Scope**: All sections in `docs/paper/sections/` + `paper_provenance.yaml`\n\n---\n\n## Inconsistency List\n\n| # | Location 1 | Value 1 | Location 2 | Value 2 | Severity | Issue | Suggested Fix |\n|---|-----------|---------|-----------|---------|----------|-------|---------------|\n| 1 | discussion.tex:L43 | LP×VC best: +0.1pp over single-sample | limitations.tex:L10 | LP×VC: +0.4pp over greedy | **HIGH** | Mathematically contradictory. If best=single+0.1pp=0.646, then vs greedy (0.663)=-1.7pp, not +0.4pp. | Limitations should read \"+0.4pp over single-sample\" OR discussion value needs correction. Verify from exp data which is correct. |\n| 2 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | appendix.tex tab:multiseed (L419) | VC NER AUROC mean = .697±.010 | **HIGH** | Mathematically impossible: if seed=42 gives .663, population σ over 3 seeds cannot be .010 with mean .697 (seed=42 deviation alone = .034 > 3×σ). | Either Table 1 AUROC is not from seed=42, or multi-seed AUROC values are from a different eval protocol. Reconcile. |\n| 3 | paper_provenance.yaml c002 | EM NER AUROC = 0.749 | experiments.tex Table 1 (L37) | EM SciERC AUROC = .614 | **HIGH** | Provenance claims EM leads AUROC at 0.749; published Table 1 shows EM=.614, VC leads at .663. Provenance narrative contradicts paper. | Update provenance to match final Table 1 values. |\n| 4 | paper_provenance.yaml c013 | greedy F1 = 0.644 | experiments.tex Table 2 (L67) | Greedy (T=0) F1 = 0.663 | **HIGH** | 1.9pp discrepancy in greedy baseline between provenance (exp_016_rerun_1024_bootstrap) and paper Table 2 (exp_016_signal_ensemble). | Clarify which experiment sources Table 2. If different experiments, provenance should reference the correct one. |\n| 5 | paper_provenance.yaml c013 | oracle = 0.776 | experiments.tex Table 2 (L66) | Oracle = 0.778±0.003 | MEDIUM | Minor discrepancy (0.002). Different source experiments. | Align provenance to published value. |\n| 6 | experiments.tex:L9 | SciERC: ≈65% F1 | discussion.tex:L13 | SciERC (66%) | MEDIUM | \"≈65%\" refers to single-sample (0.645), \"66%\" refers to greedy (0.663). With the \"Single=greedy\" issue, these become entangled. | Standardize: if \"Single\" is the reference, use \"65%\"; if greedy, use \"66%\". Pick one. |\n| 7 | experiments.tex:L11 | WNUT-17: 52% zero F1 | paper_provenance.yaml c021 | 54% zero F1 (evidence: 53.7%) | MEDIUM | Paper says 52%, provenance says 54%/53.7%. Different filtering or rounding. | Verify exact number from exp_003 data and standardize. |\n| 8 | experiments.tex:L89 | LP Δ=+0.2pp (LP 0.647 - Single 0.645) | paper_provenance.yaml c011 | logprob +0.6pp (LP 0.650 - greedy 0.644) | MEDIUM | Different source experiments produce different LP values (0.647 vs 0.650) and different baselines. | Provenance should reference the same experiment as Table 2. |\n| 9 | appendix.tex:L81 | SJ N=8→N=16 gain = +0.047 | appendix.tex tab:n-scaling (L861) | SJ N=8→N=16 Δ = +0.0464 | LOW | Appendix text uses different baseline (single-seed 0.360) vs N-scaling table (3-seed mean 0.3641). Reported as +0.047 but actual calculation from text values: 0.411-0.360=0.051. | Use consistent baselines; if comparing 3-seed means, use both from N-scaling table (+0.046). |\n| 10 | paper_provenance.yaml c025 | SJ T=0.7 ρ = 0.388 | appendix.tex tab:robustness (L44) | SJ T=0.7 ρ = 0.364 | MEDIUM | Provenance cites exp_005 value (0.388); published table uses different value (0.364). Provenance is stale. | Update provenance to match published appendix table. |\n| 11 | paper_provenance.yaml c002 | VC AUROC (corrected) = 0.684 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | **HIGH** | Provenance note says \"Corrected to .684 via exp_012_rerun_1024\" but Table 1 shows .663. | Provenance values don't match final paper. Update provenance. |\n| 12 | introduction.tex:L35 | \"13-18 pp oracle headroom\" (context: greedy surpasses) | experiments.tex Table 2 | Oracle-Greedy = 0.778-0.663 = 11.5pp | MEDIUM | \"13-18pp\" is oracle vs single-sample (13.3 NER, 18.1 RE), not oracle vs greedy. The sentence juxtaposes greedy performance with headroom measured from a different baseline. Technically correct but misleading in context. | Consider rephrasing: \"despite 13pp oracle headroom above single-sample\" to avoid conflation with the greedy baseline in the same sentence. |\n| 13 | paper_provenance.yaml c004 | Voting RE ρ=0.350 (corrected) | appendix.tex tab:multiseed (L417) | RE VC mean ρ=0.309±0.024 | LOW | Provenance (single seed=42) vs appendix (3-seed mean). Both can be correct for their context but provenance should note this is single-seed. | Add note to provenance that 0.350 is seed=42 only; 3-seed mean is 0.309. |\n\n---\n\n## Provenance-Paper Alignment Summary\n\nThe provenance yaml (version 100, built 2026-05-16) has multiple values that don't match the final published tables. Key mismatches:\n\n| Provenance Claim | Provenance Value | Paper Value | Status |\n|-----------------|-----------------|-------------|--------|\n| c002: EM NER AUROC | 0.749 | 0.614 | **STALE** |\n| c002: VC NER AUROC | 0.684 | 0.663 | **STALE** |\n| c013: greedy NER F1 | 0.644 | 0.663 | **STALE** |\n| c013: oracle NER F1 | 0.776 | 0.778 | Minor |\n| c011: LP F1 | 0.650 | 0.647 | **STALE** |\n| c025: SJ T=0.7 ρ | 0.388 | 0.364 | **STALE** |\n\n**Root cause**: Provenance references experiments (exp_012_rerun_1024, exp_016_rerun_1024_bootstrap) that differ from the experiment sourcing Table 2 (exp_016_signal_ensemble). The provenance was not updated after the final table values were finalized.\n\n---\n\n## Cross-Section Consistency for Key Numbers\n\n### Consistent across sections (verified):\n- ρ up to 0.38 (abstract/intro/conclusion) ← VC 0.379 rounds to 0.38 ✓\n- 0.45 on ceiling control (abstract/intro/conclusion) ← EM CoNLL 0.451 ✓\n- 21-58% instance degeneracy (abstract/intro/discussion/conclusion) ← Table 3 ✓\n- median ρ=0.52 within-instance (abstract/intro/discussion) ← Table 3: 0.524 ✓\n- 0.041 nats LP range (abstract/intro/discussion/conclusion/appendix) ✓\n- MBR closes 23-41% (intro/discussion/Table 3) ✓\n- Greedy F1=0.663 (intro/experiments/discussion) ✓\n- Non-tied LP: +2.9pp, p=0.004 (experiments/discussion/appendix) ✓\n- VerbConf mean 8.58/10 SciERC (discussion 8.6, limitations 8.58, appendix 8.58) ✓\n- ECE 0.069-0.096 NER (experiments/appendix) ✓\n- Entity-token LP 4× variance (discussion/limitations) ✓\n\n### Rounding conventions used:\n- 0.379 → \"0.38\" in prose ✓\n- 0.451 → \"0.45\" in prose ✓\n- 8.58 → \"8.6\" in discussion prose ✓\n- 0.524 → \"0.52\" in abstract/intro ✓\n\n---\n\n## Recommendations (Priority Order)\n\n1. **Fix #1 immediately** (reviewer-flagged): Resolve the \"+0.1pp over single\" vs \"+0.4pp over greedy\" contradiction in limitations.tex\n2. **Fix #2**: Reconcile Table 1 AUROC values with multi-seed table — either add a note about different eval protocols or correct one table\n3. **Rebuild provenance**: Multiple provenance entries reference superseded experiments. Full provenance rebuild needed against final Table 1/2 values.\n4. **Standardize SciERC F1 reference**: Pick \"≈65%\" (single-sample) or \"≈66%\" (greedy) and use consistently. Given the \"Single=greedy\" issue, this needs resolution first.\n5. **Minor fixes**: WNUT zero-F1 percentage (52% vs 53.7%), N-scaling gain reporting.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "641293f5-bfce-4261-b5a9-e8eb008d8d7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqdSwmFX7Xdb7ij5XdMn9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15996,
      "cache_read_input_tokens": 79102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15996
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

_source line 41 · 2026-05-16T09:51:57.680Z_

<details><summary>↩ Tool result · `toolu_012Ft1V8419crGMeVBnChafX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "43438a62-8cf3-4c69-a132-8bae9295840c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
    "content": "# Claim Audit Report: Numerical Consistency Check\n\n**Paper**: Strong Predictors, Weak Selectors  \n**Date**: 2026-05-16  \n**Scope**: All sections in `docs/paper/sections/` + `paper_provenance.yaml`\n\n---\n\n## Inconsistency List\n\n| # | Location 1 | Value 1 | Location 2 | Value 2 | Severity | Issue | Suggested Fix |\n|---|-----------|---------|-----------|---------|----------|-------|---------------|\n| 1 | discussion.tex:L43 | LP×VC best: +0.1pp over single-sample | limitations.tex:L10 | LP×VC: +0.4pp over greedy | **HIGH** | Mathematically contradictory. If best=single+0.1pp=0.646, then vs greedy (0.663)=-1.7pp, not +0.4pp. | Limitations should read \"+0.4pp over single-sample\" OR discussion value needs correction. Verify from exp data which is correct. |\n| 2 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | appendix.tex tab:multiseed (L419) | VC NER AUROC mean = .697±.010 | **HIGH** | Mathematically impossible: if seed=42 gives .663, population σ over 3 seeds cannot be .010 with mean .697 (seed=42 deviation alone = .034 > 3×σ). | Either Table 1 AUROC is not from seed=42, or multi-seed AUROC values are from a different eval protocol. Reconcile. |\n| 3 | paper_provenance.yaml c002 | EM NER AUROC = 0.749 | experiments.tex Table 1 (L37) | EM SciERC AUROC = .614 | **HIGH** | Provenance claims EM leads AUROC at 0.749; published Table 1 shows EM=.614, VC leads at .663. Provenance narrative contradicts paper. | Update provenance to match final Table 1 values. |\n| 4 | paper_provenance.yaml c013 | greedy F1 = 0.644 | experiments.tex Table 2 (L67) | Greedy (T=0) F1 = 0.663 | **HIGH** | 1.9pp discrepancy in greedy baseline between provenance (exp_016_rerun_1024_bootstrap) and paper Table 2 (exp_016_signal_ensemble). | Clarify which experiment sources Table 2. If different experiments, provenance should reference the correct one. |\n| 5 | paper_provenance.yaml c013 | oracle = 0.776 | experiments.tex Table 2 (L66) | Oracle = 0.778±0.003 | MEDIUM | Minor discrepancy (0.002). Different source experiments. | Align provenance to published value. |\n| 6 | experiments.tex:L9 | SciERC: ≈65% F1 | discussion.tex:L13 | SciERC (66%) | MEDIUM | \"≈65%\" refers to single-sample (0.645), \"66%\" refers to greedy (0.663). With the \"Single=greedy\" issue, these become entangled. | Standardize: if \"Single\" is the reference, use \"65%\"; if greedy, use \"66%\". Pick one. |\n| 7 | experiments.tex:L11 | WNUT-17: 52% zero F1 | paper_provenance.yaml c021 | 54% zero F1 (evidence: 53.7%) | MEDIUM | Paper says 52%, provenance says 54%/53.7%. Different filtering or rounding. | Verify exact number from exp_003 data and standardize. |\n| 8 | experiments.tex:L89 | LP Δ=+0.2pp (LP 0.647 - Single 0.645) | paper_provenance.yaml c011 | logprob +0.6pp (LP 0.650 - greedy 0.644) | MEDIUM | Different source experiments produce different LP values (0.647 vs 0.650) and different baselines. | Provenance should reference the same experiment as Table 2. |\n| 9 | appendix.tex:L81 | SJ N=8→N=16 gain = +0.047 | appendix.tex tab:n-scaling (L861) | SJ N=8→N=16 Δ = +0.0464 | LOW | Appendix text uses different baseline (single-seed 0.360) vs N-scaling table (3-seed mean 0.3641). Reported as +0.047 but actual calculation from text values: 0.411-0.360=0.051. | Use consistent baselines; if comparing 3-seed means, use both from N-scaling table (+0.046). |\n| 10 | paper_provenance.yaml c025 | SJ T=0.7 ρ = 0.388 | appendix.tex tab:robustness (L44) | SJ T=0.7 ρ = 0.364 | MEDIUM | Provenance cites exp_005 value (0.388); published table uses different value (0.364). Provenance is stale. | Update provenance to match published appendix table. |\n| 11 | paper_provenance.yaml c002 | VC AUROC (corrected) = 0.684 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | **HIGH** | Provenance note says \"Corrected to .684 via exp_012_rerun_1024\" but Table 1 shows .663. | Provenance values don't match final paper. Update provenance. |\n| 12 | introduction.tex:L35 | \"13-18 pp oracle headroom\" (context: greedy surpasses) | experiments.tex Table 2 | Oracle-Greedy = 0.778-0.663 = 11.5pp | MEDIUM | \"13-18pp\" is oracle vs single-sample (13.3 NER, 18.1 RE), not oracle vs greedy. The sentence juxtaposes greedy performance with headroom measured from a different baseline. Technically correct but misleading in context. | Consider rephrasing: \"despite 13pp oracle headroom above single-sample\" to avoid conflation with the greedy baseline in the same sentence. |\n| 13 | paper_provenance.yaml c004 | Voting RE ρ=0.350 (corrected) | appendix.tex tab:multiseed (L417) | RE VC mean ρ=0.309±0.024 | LOW | Provenance (single seed=42) vs appendix (3-seed mean). Both can be correct for their context but provenance should note this is single-seed. | Add note to provenance that 0.350 is seed=42 only; 3-seed mean is 0.309. |\n\n---\n\n## Provenance-Paper Alignment Summary\n\nThe provenance yaml (version 100, built 2026-05-16) has multiple values that don't match the final published tables. Key mismatches:\n\n| Provenance Claim | Provenance Value | Paper Value | Status |\n|-----------------|-----------------|-------------|--------|\n| c002: EM NER AUROC | 0.749 | 0.614 | **STALE** |\n| c002: VC NER AUROC | 0.684 | 0.663 | **STALE** |\n| c013: greedy NER F1 | 0.644 | 0.663 | **STALE** |\n| c013: oracle NER F1 | 0.776 | 0.778 | Minor |\n| c011: LP F1 | 0.650 | 0.647 | **STALE** |\n| c025: SJ T=0.7 ρ | 0.388 | 0.364 | **STALE** |\n\n**Root cause**: Provenance references experiments (exp_012_rerun_1024, exp_016_rerun_1024_bootstrap) that differ from the experiment sourcing Table 2 (exp_016_signal_ensemble). The provenance was not updated after the final table values were finalized.\n\n---\n\n## Cross-Section Consistency for Key Numbers\n\n### Consistent across sections (verified):\n- ρ up to 0.38 (abstract/intro/conclusion) ← VC 0.379 rounds to 0.38 ✓\n- 0.45 on ceiling control (abstract/intro/conclusion) ← EM CoNLL 0.451 ✓\n- 21-58% instance degeneracy (abstract/intro/discussion/conclusion) ← Table 3 ✓\n- median ρ=0.52 within-instance (abstract/intro/discussion) ← Table 3: 0.524 ✓\n- 0.041 nats LP range (abstract/intro/discussion/conclusion/appendix) ✓\n- MBR closes 23-41% (intro/discussion/Table 3) ✓\n- Greedy F1=0.663 (intro/experiments/discussion) ✓\n- Non-tied LP: +2.9pp, p=0.004 (experiments/discussion/appendix) ✓\n- VerbConf mean 8.58/10 SciERC (discussion 8.6, limitations 8.58, appendix 8.58) ✓\n- ECE 0.069-0.096 NER (experiments/appendix) ✓\n- Entity-token LP 4× variance (discussion/limitations) ✓\n\n### Rounding conventions used:\n- 0.379 → \"0.38\" in prose ✓\n- 0.451 → \"0.45\" in prose ✓\n- 8.58 → \"8.6\" in discussion prose ✓\n- 0.524 → \"0.52\" in abstract/intro ✓\n\n---\n\n## Recommendations (Priority Order)\n\n1. **Fix #1 immediately** (reviewer-flagged): Resolve the \"+0.1pp over single\" vs \"+0.4pp over greedy\" contradiction in limitations.tex\n2. **Fix #2**: Reconcile Table 1 AUROC values with multi-seed table — either add a note about different eval protocols or correct one table\n3. **Rebuild provenance**: Multiple provenance entries reference superseded experiments. Full provenance rebuild needed against final Table 1/2 values.\n4. **Standardize SciERC F1 reference**: Pick \"≈65%\" (single-sample) or \"≈66%\" (greedy) and use consistently. Given the \"Single=greedy\" issue, this needs resolution first.\n5. **Minor fixes**: WNUT zero-F1 percentage (52% vs 53.7%), N-scaling gain reporting.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Write · `toolu_01LfRj4nmLXNwfiHcSc4Wdw2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
  "content": "# \"Single\" Label Issues\n\n**Background**: Discovery that Table 2's \"Single\" row may actually be T=0 greedy decoding, mislabeled as \"one T=1.0 draw.\"\n\n---\n\n## Evidence For/Against \"Single = T=0 Greedy\"\n\n### Arguments supporting the mislabeling theory:\n1. Provenance c013 lists `greedy=0.644` — very close to paper's `Single=0.645`\n2. The provenance selection data (c011) has no explicit \"single\" field — only `greedy: 0.644, logprob: 0.650, sj: 0.645...`\n3. Provenance c011 computes LP gain as \"+0.6pp\" — this is `0.650-0.644=+0.6pp`, treating the 0.644 value as the single-sample baseline\n\n### Arguments against the mislabeling theory:\n1. Table 2 shows `Single: 0.645 ± 0.001` — the ±0.001 variance implies stochasticity, inconsistent with deterministic T=0\n2. Paper has BOTH `Greedy (T=0) = 0.663` and `Single = 0.645` as separate rows — if both are T=0, they should be identical\n3. Method.tex L61 explicitly defines: \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\"\n4. Table 2 footnote: \"‡Single: one T=1.0 draw (expected performance of a single sample)\"\n\n### Possible resolution:\nThe numbers suggest the pipeline has TWO different evaluation protocols both labeled as \"greedy/T=0\":\n- `Greedy (T=0)` in Table 2 (F1=0.663): from one experiment/eval set\n- `greedy` in provenance c013 (F1=0.644): from a different experiment (exp_016_rerun_1024_bootstrap)\n\nThe 1.9pp gap between them (0.663 vs 0.644) is too large to be noise. Likely explanations:\n- Different instance filtering (full set vs gold-filtered)\n- Different seed\n- One is 2-seed averaged, the other single-seed\n\nIf \"Single\" (0.645) ≈ provenance \"greedy\" (0.644), the issue may be that the provenance experiment computed its \"greedy\" baseline differently from Table 2's \"Greedy\" row.\n\n---\n\n## Affected Claims (If Single IS T=0 Greedy)\n\n### Category A: \"Over single-sample\" comparisons become \"over greedy\"\n\n| Location | Claim | Current Interpretation | If Single=Greedy |\n|----------|-------|----------------------|------------------|\n| experiments.tex:L89 | \"LP achieves 0.647 (Δ=+0.2pp)\" | LP beats single T=1.0 draw | LP beats greedy by 0.2pp → greedy no longer best |\n| experiments.tex:L89 | \"oracle reveals 13.3pp headroom above single-sample\" | Headroom above T=1.0 draw | Headroom above greedy |\n| experiments.tex:L93 | \"Greedy (T=0) surpasses all N=8 selection strategies\" | Greedy > LP > Single | If Single=Greedy, contradiction: \"Greedy\"(0.663) ≠ \"Single\"(0.645) |\n| introduction.tex:L35 | \"Greedy decoding (F1=0.663) surpasses all N=8 selection strategies (best: 0.647) despite 13-18pp oracle headroom\" | Clean claim | The \"13-18pp\" is now headroom over greedy, not over a stochastic sample |\n| discussion.tex:L43 | \"All three fail to improve over single-sample (best: +0.1pp)\" | Combinations vs T=1.0 | Combinations vs greedy |\n\n### Category B: The \"correlation-selection gap\" framing\n\nThe gap is defined as: \"quality estimation works (ρ=0.38), but selection fails to beat single-sample.\"\n- If single-sample IS greedy, then the gap is: \"QE works, but selection fails to beat greedy.\"\n- This actually STRENGTHENS the argument (it's even harder to beat greedy than a random T=1.0 draw).\n- BUT: it removes the claim that \"multi-sample is worse than the trivial single-sample baseline\" because the baseline is no longer trivial (it's the best possible deterministic output).\n\n### Category C: Definition contradictions\n\n| Location | Text | Issue |\n|----------|------|-------|\n| method.tex:L61 | \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\" | Definition explicitly says NOT argmax |\n| experiments.tex:L60-61 | \"‡Single: one T=1.0 draw (expected performance of a single sample)\" | Footnote repeats the T=1.0 claim |\n| experiments.tex:L78 | `Single‡ & 0.645 ± 0.001` | ±0.001 would be expected for T=1.0 across seeds |\n\n### Category D: If there are TWO greedy values in the paper\n\n| Row | F1 | Claimed Identity | Actual |\n|-----|-----|-----------------|--------|\n| Greedy (T=0)† | 0.663 | argmax decoding | ??? |\n| Single‡ | 0.645±0.001 | one T=1.0 draw | ??? |\n\nIf both are T=0, they MUST give identical F1 (deterministic). The 1.8pp difference proves they cannot both be T=0 under the same evaluation protocol. Therefore EITHER:\n1. Single IS T=1.0 (as stated) — no mislabeling, just confusing provenance\n2. They use different eval sets (e.g., Greedy on n=551, Single on n=529 gold-filtered)\n3. One is averaged over seeds differently\n\n---\n\n## Recommended Investigation\n\n1. **Check the experiment code**: Verify the temperature parameter used when computing the \"single\" baseline in exp_016_signal_ensemble\n2. **Check instance counts**: If Greedy uses n=551 (full) and Single uses n=529 (gold-filtered), the 1.8pp difference could be explained by the 22 excluded instances\n3. **Reconcile provenance \"greedy=0.644\" with paper \"Greedy=0.663\"**: Identify which experiment/filtering produces each\n4. **If Single is confirmed T=1.0**: Update provenance to stop conflating \"single\" with \"greedy\"\n5. **If Single is confirmed T=0**: \n   - Correct method.tex definition\n   - Correct table footnotes\n   - Reframe all \"vs single-sample\" claims\n   - Address why Greedy(0.663)≠Single(0.645) if both are T=0\n\n---\n\n## Impact Assessment\n\n| Scenario | Impact on Paper Claims | Severity |\n|----------|----------------------|----------|\n| Single is actually T=1.0 (no bug) | No impact; provenance needs cleanup only | Low |\n| Single is T=0 but from different eval set | Need to clarify eval protocol; minor text fixes | Medium |\n| Single is truly mislabeled T=0 with same eval set | Major rewrite of framing; \"Greedy=0.663\" row becomes unexplained | **Critical** |\n\nThe ±0.001 variance in the Single row and the 1.8pp gap from Greedy argue strongly that **Single is genuinely T=1.0** and the confusion stems from provenance using a different experiment's \"greedy\" value (0.644) that happens to be close to Single (0.645). The real issue is the provenance-paper misalignment documented in the main audit report.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "d4ed696a-c57c-42c8-8b6e-2493bf53bde6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iD7TrzpcY642tU3CtjS3r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 95098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2860
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

_source line 43 · 2026-05-16T09:52:43.303Z_

<details><summary>↩ Tool result · `toolu_01LfRj4nmLXNwfiHcSc4Wdw2`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "4859832e-15fc-4efb-b38f-e6d886dc9e00",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
    "content": "# \"Single\" Label Issues\n\n**Background**: Discovery that Table 2's \"Single\" row may actually be T=0 greedy decoding, mislabeled as \"one T=1.0 draw.\"\n\n---\n\n## Evidence For/Against \"Single = T=0 Greedy\"\n\n### Arguments supporting the mislabeling theory:\n1. Provenance c013 lists `greedy=0.644` — very close to paper's `Single=0.645`\n2. The provenance selection data (c011) has no explicit \"single\" field — only `greedy: 0.644, logprob: 0.650, sj: 0.645...`\n3. Provenance c011 computes LP gain as \"+0.6pp\" — this is `0.650-0.644=+0.6pp`, treating the 0.644 value as the single-sample baseline\n\n### Arguments against the mislabeling theory:\n1. Table 2 shows `Single: 0.645 ± 0.001` — the ±0.001 variance implies stochasticity, inconsistent with deterministic T=0\n2. Paper has BOTH `Greedy (T=0) = 0.663` and `Single = 0.645` as separate rows — if both are T=0, they should be identical\n3. Method.tex L61 explicitly defines: \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\"\n4. Table 2 footnote: \"‡Single: one T=1.0 draw (expected performance of a single sample)\"\n\n### Possible resolution:\nThe numbers suggest the pipeline has TWO different evaluation protocols both labeled as \"greedy/T=0\":\n- `Greedy (T=0)` in Table 2 (F1=0.663): from one experiment/eval set\n- `greedy` in provenance c013 (F1=0.644): from a different experiment (exp_016_rerun_1024_bootstrap)\n\nThe 1.9pp gap between them (0.663 vs 0.644) is too large to be noise. Likely explanations:\n- Different instance filtering (full set vs gold-filtered)\n- Different seed\n- One is 2-seed averaged, the other single-seed\n\nIf \"Single\" (0.645) ≈ provenance \"greedy\" (0.644), the issue may be that the provenance experiment computed its \"greedy\" baseline differently from Table 2's \"Greedy\" row.\n\n---\n\n## Affected Claims (If Single IS T=0 Greedy)\n\n### Category A: \"Over single-sample\" comparisons become \"over greedy\"\n\n| Location | Claim | Current Interpretation | If Single=Greedy |\n|----------|-------|----------------------|------------------|\n| experiments.tex:L89 | \"LP achieves 0.647 (Δ=+0.2pp)\" | LP beats single T=1.0 draw | LP beats greedy by 0.2pp → greedy no longer best |\n| experiments.tex:L89 | \"oracle reveals 13.3pp headroom above single-sample\" | Headroom above T=1.0 draw | Headroom above greedy |\n| experiments.tex:L93 | \"Greedy (T=0) surpasses all N=8 selection strategies\" | Greedy > LP > Single | If Single=Greedy, contradiction: \"Greedy\"(0.663) ≠ \"Single\"(0.645) |\n| introduction.tex:L35 | \"Greedy decoding (F1=0.663) surpasses all N=8 selection strategies (best: 0.647) despite 13-18pp oracle headroom\" | Clean claim | The \"13-18pp\" is now headroom over greedy, not over a stochastic sample |\n| discussion.tex:L43 | \"All three fail to improve over single-sample (best: +0.1pp)\" | Combinations vs T=1.0 | Combinations vs greedy |\n\n### Category B: The \"correlation-selection gap\" framing\n\nThe gap is defined as: \"quality estimation works (ρ=0.38), but selection fails to beat single-sample.\"\n- If single-sample IS greedy, then the gap is: \"QE works, but selection fails to beat greedy.\"\n- This actually STRENGTHENS the argument (it's even harder to beat greedy than a random T=1.0 draw).\n- BUT: it removes the claim that \"multi-sample is worse than the trivial single-sample baseline\" because the baseline is no longer trivial (it's the best possible deterministic output).\n\n### Category C: Definition contradictions\n\n| Location | Text | Issue |\n|----------|------|-------|\n| method.tex:L61 | \"single-sample (one T=1.0 draw, not argmax decoding; labeled 'Single' in tables)\" | Definition explicitly says NOT argmax |\n| experiments.tex:L60-61 | \"‡Single: one T=1.0 draw (expected performance of a single sample)\" | Footnote repeats the T=1.0 claim |\n| experiments.tex:L78 | `Single‡ & 0.645 ± 0.001` | ±0.001 would be expected for T=1.0 across seeds |\n\n### Category D: If there are TWO greedy values in the paper\n\n| Row | F1 | Claimed Identity | Actual |\n|-----|-----|-----------------|--------|\n| Greedy (T=0)† | 0.663 | argmax decoding | ??? |\n| Single‡ | 0.645±0.001 | one T=1.0 draw | ??? |\n\nIf both are T=0, they MUST give identical F1 (deterministic). The 1.8pp difference proves they cannot both be T=0 under the same evaluation protocol. Therefore EITHER:\n1. Single IS T=1.0 (as stated) — no mislabeling, just confusing provenance\n2. They use different eval sets (e.g., Greedy on n=551, Single on n=529 gold-filtered)\n3. One is averaged over seeds differently\n\n---\n\n## Recommended Investigation\n\n1. **Check the experiment code**: Verify the temperature parameter used when computing the \"single\" baseline in exp_016_signal_ensemble\n2. **Check instance counts**: If Greedy uses n=551 (full) and Single uses n=529 (gold-filtered), the 1.8pp difference could be explained by the 22 excluded instances\n3. **Reconcile provenance \"greedy=0.644\" with paper \"Greedy=0.663\"**: Identify which experiment/filtering produces each\n4. **If Single is confirmed T=1.0**: Update provenance to stop conflating \"single\" with \"greedy\"\n5. **If Single is confirmed T=0**: \n   - Correct method.tex definition\n   - Correct table footnotes\n   - Reframe all \"vs single-sample\" claims\n   - Address why Greedy(0.663)≠Single(0.645) if both are T=0\n\n---\n\n## Impact Assessment\n\n| Scenario | Impact on Paper Claims | Severity |\n|----------|----------------------|----------|\n| Single is actually T=1.0 (no bug) | No impact; provenance needs cleanup only | Low |\n| Single is T=0 but from different eval set | Need to clarify eval protocol; minor text fixes | Medium |\n| Single is truly mislabeled T=0 with same eval set | Major rewrite of framing; \"Greedy=0.663\" row becomes unexplained | **Critical** |\n\nThe ±0.001 variance in the Single row and the 1.8pp gap from Greedy argue strongly that **Single is genuinely T=1.0** and the confusion stems from provenance using a different experiment's \"greedy\" value (0.644) that happens to be close to Single (0.645). The real issue is the provenance-paper misalignment documented in the main audit report.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 44_

Now let me register the artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "05969a5e-e0ff-40e4-b783-e60280f003ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTRg5yHHEHBXMFt75tUx4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2099,
      "cache_read_input_tokens": 97958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2099
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

_source line 45_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M7EC6KfoCru3tEyy8MQ21F`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "c112a68c-aecb-4b05-850a-9b734d46b2db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTRg5yHHEHBXMFt75tUx4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2099,
      "cache_read_input_tokens": 97958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2099
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

_source line 46 · 2026-05-16T09:52:47.799Z_

<details><summary>↩ Tool result · `toolu_01M7EC6KfoCru3tEyy8MQ21F`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "142c9c47-38b1-44e0-9873-748d2b52ec92",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me register both artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "16f0aaff-3e44-473d-b13c-e099c58d95a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GY5cn2rg3obUSsT25T1P9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 100057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01RaSfTo1mvBSCoKH7PZ4tTV`</summary>

```json
{
  "name": "d112_claim_audit_report",
  "type": "report",
  "description": "Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/audit_report.md",
  "tags": [
    "paper",
    "audit",
    "round15",
    "numerical-consistency"
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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "74302f2e-a04a-41d7-a94b-c2a6a698f930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GY5cn2rg3obUSsT25T1P9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 100057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 49 · 2026-05-16T09:52:54.820Z_

<details><summary>↩ Tool result · `toolu_01RaSfTo1mvBSCoKH7PZ4tTV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_736eaa\", \"name\": \"d112_claim_audit_report\", \"type\": \"report\", \"description\": \"Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/audit_report_736eaa.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T09:52:54.496903+00:00\", \"tags\": [\"paper\", \"audit\", \"round15\", \"numerical-consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "8eae2308-c356-4928-871b-2ff0605defd8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_736eaa\\\", \\\"name\\\": \\\"d112_claim_audit_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/_project/report/audit_report_736eaa.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T09:52:54.496903+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"audit\\\", \\\"round15\\\", \\\"numerical-consistency\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_736eaa\", \"name\": \"d112_claim_audit_report\", \"type\": \"report\", \"description\": \"Systematic numerical consistency audit of all paper sections. Found 13 inconsistencies (5 HIGH, 5 MEDIUM, 3 LOW) including reviewer-flagged +0.1pp/+0.4pp contradiction, Table 1 vs multi-seed AUROC mathematical impossibility, and 6 stale provenance entries.\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/audit_report_736eaa.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T09:52:54.496903+00:00\", \"tags\": [\"paper\", \"audit\", \"round15\", \"numerical-consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01HyYpDdhJXLMBXPQwheybFR`</summary>

```json
{
  "name": "d112_single_label_issues",
  "type": "report",
  "description": "Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d112_claim_audit/single_label_issues.md",
  "tags": [
    "paper",
    "audit",
    "round15",
    "single-label",
    "table2"
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
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "200647ba-0129-4972-9685-3182fefadec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GY5cn2rg3obUSsT25T1P9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 100057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 51 · 2026-05-16T09:52:57.817Z_

<details><summary>↩ Tool result · `toolu_01HyYpDdhJXLMBXPQwheybFR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e0eca0\", \"name\": \"d112_single_label_issues\", \"type\": \"report\", \"description\": \"Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/single_label_issues.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T09:52:57.463770+00:00\", \"tags\": [\"paper\", \"audit\", \"round15\", \"single-label\", \"table2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "bcaf73d7-377b-47c4-9ccd-c18e05754d6c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_e0eca0\\\", \\\"name\\\": \\\"d112_single_label_issues\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/_project/report/single_label_issues.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T09:52:57.463770+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"audit\\\", \\\"round15\\\", \\\"single-label\\\", \\\"table2\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e0eca0\", \"name\": \"d112_single_label_issues\", \"type\": \"report\", \"description\": \"Analysis of the 'Single' row mislabeling issue in Table 2. Concludes that Single is likely genuinely T=1.0 (±0.001 variance and 1.8pp gap from Greedy prove they cannot both be T=0). The confusion stems from provenance using a different experiment's greedy value (0.644) that coincidentally approximates Single (0.645).\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/single_label_issues.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T09:52:57.463770+00:00\", \"tags\": [\"paper\", \"audit\", \"round15\", \"single-label\", \"table2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

审计完成。主要发现：

**5个HIGH严重度问题：**
1. Discussion "+0.1pp over single-sample" vs Limitations "+0.4pp over greedy" — 数学上矛盾（审稿人已指出）
2. Table 1 VC AUROC (.663) vs multi-seed table (.697±.010) — seed=42 数学上不可能产生这个均值/σ组合
3. Provenance c002 "EM AUROC=0.749" vs Table 1 实际值 .614 — provenance 严重过时
4. Provenance greedy=0.644 vs paper greedy=0.663 — 来源实验不同，1.9pp差距
5. Provenance VC AUROC=0.684 vs Table 1 VC AUROC=.663 — provenance 过时

**关于 "Single=T=0 greedy" 的结论：**
Single 行大概率确实是 T=1.0。证据：±0.001 方差（T=0 应为零方差）+ 与 Greedy 行差 1.8pp（如果都是 T=0 应完全相同）。混淆来源是 provenance 引用了不同实验的 greedy 值 (0.644) 恰好接近 Single (0.645)。

**最优先修复：** limitations.tex L10 的 "+0.4pp over greedy" 需改为 "+0.1pp over single-sample"（或从实验数据确认正确值）。

产出已保存到 `artifacts/d112_claim_audit/` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "uuid": "17de829f-16bd-4049-a502-af3aa66796d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRWB3DkKWGNnGCUdBftAG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1344,
      "cache_read_input_tokens": 100879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1344
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

_source line 53_

审计完成。主要发现：

**5个HIGH严重度问题：**
1. Discussion "+0.1pp over single-sample" vs Limitations "+0.4pp over greedy" — 数学上矛盾（审稿人已指出）
2. Table 1 VC AUROC (.663) vs multi-seed table (.697±.010) — seed=42 数学上不可能产生这个均值/σ组合
3. Provenance c002 "EM AUROC=0.749" vs Table 1 实际值 .614 — provenance 严重过时
4. Provenance greedy=0.644 vs paper greedy=0.663 — 来源实验不同，1.9pp差距
5. Provenance VC AUROC=0.684 vs Table 1 VC AUROC=.663 — provenance 过时

**关于 "Single=T=0 greedy" 的结论：**
Single 行大概率确实是 T=1.0。证据：±0.001 方差（T=0 应为零方差）+ 与 Greedy 行差 1.8pp（如果都是 T=0 应完全相同）。混淆来源是 provenance 引用了不同实验的 greedy 值 (0.644) 恰好接近 Single (0.645)。

**最优先修复：** limitations.tex L10 的 "+0.4pp over greedy" 需改为 "+0.1pp over single-sample"（或从实验数据确认正确值）。

产出已保存到 `artifacts/d112_claim_audit/` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 480429,
  "duration_api_ms": 480267,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "eb3aaa1b-b631-4567-9f6c-582a266346aa",
  "total_cost_usd": 1.4712859999999999,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 90382,
    "cache_read_input_tokens": 646967,
    "output_tokens": 23242,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 90382,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 443,
        "cache_read_input_tokens": 100879,
        "cache_creation_input_tokens": 1344,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1344
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1720,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001795,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 23242,
      "cacheReadInputTokens": 646967,
      "cacheCreationInputTokens": 90382,
      "webSearchRequests": 0,
      "costUSD": 1.4694909999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "448272ac-f3b1-47c0-abff-1fd68a12c47d"
}
```

</details>

---
