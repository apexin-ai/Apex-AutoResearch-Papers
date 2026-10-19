# review ai writing audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/workers/worker_review_ai_writing_audit_20260518T221534.log`
- **Structured JSON:** [`86d6242d364146e2d882.json`](../../sessions/86/86d6242d364146e2d882.json)

## Before a recorded user message

93 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
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
  "uuid": "7de0c249-8574-4aa2-a74d-c6953c183c11",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/memory/"
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
    "resetsAt": 1779160200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b24fd753-16ff-408f-94ac-3416c99594aa",
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by listing the .tex files in the paper directories, then systematically check each one for AI writing style issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "64b81773-c192-4ccc-b03a-5a85d1386757",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01411mjvvjNw7eYA3QLaFUcX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14105,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14105
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

开始对论文全文做 AI 写作风格审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "a26e26ff-f77c-4116-824b-6c67e49a0584",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01411mjvvjNw7eYA3QLaFUcX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14105,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14105
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01XjUwXgtk1EcaeukvE52tNw`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/",
  "description": "List .tex files in sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "360b708d-73cc-41ba-bb3b-5e46fc89b403",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01411mjvvjNw7eYA3QLaFUcX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14105,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14105
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 7 · 2026-05-18T22:15:48.129Z_

<details><summary>↩ Tool result · `toolu_01XjUwXgtk1EcaeukvE52tNw`</summary>

```text
abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "260c98d7-5a14-423f-b901-d12e76dc2037",
  "tool_use_result": {
    "stdout": "abstract.tex\nappendix.tex\nconclusion.tex\ndiscussion.tex\nexperiments.tex\nintroduction.tex\nlimitations.tex\nmethod.tex\nrelated_work.tex",
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

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q3wechAZC1FjBUzxJeLVuT`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/*.tex",
  "description": "List .tex files in paper root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "5dbde300-5e2c-47c8-be6e-84e97a259c71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01411mjvvjNw7eYA3QLaFUcX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14105,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14105
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 9 · 2026-05-18T22:15:48.666Z_

<details><summary>↩ Tool result · `toolu_01Q3wechAZC1FjBUzxJeLVuT`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "bee54d19-35ae-432c-b730-98e6c0a5254a",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
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

_source line 10_

10 files to check. Let me read them all and run grep checks in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "014336bc-5e88-496d-a325-5bb1185f60ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01GenR9nk5iTjS6srs4XKtev`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "0844dad8-bc88-449a-a326-b8a1da24f8fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 12 · 2026-05-18T22:15:52.145Z_

<details><summary>↩ Tool result · `toolu_01GenR9nk5iTjS6srs4XKtev`</summary>

```text
1	Reasoning models with chain-of-thought (CoT) can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. Detecting this safety commitment point requires monitoring, but a prior question remains unanswered: should a monitoring system read the model's hidden states or its generated text? We show that this comparison's outcome depends critically on an underexamined researcher degree of freedom: which transformer layer to monitor. Through systematic evaluation of hidden-state (HS) and text-based probes across four reasoning models, five selection metrics, and seven alternative methods, we find that a biased composite metric masks the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. Principled selection recovers significant HS precision gains (+15.4 to +21.9pp, Holm-Bonferroni corrected), with evidence from strong (OT-7B, 5/5 seeds) to qualified (R1-32B, position-mediated). Encoder quality bounds the advantage: against a stronger 1024d text encoder, only 1/4 models survives correction. Layer selection sensitivity is the robust methodological finding; the empirical HS advantage is conditional, and current probes characterize the commitment phenomenon (FPR 39--52\%) rather than constitute production detectors.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "7dc78150-7c69-4ba9-84ff-c141618116a6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex",
      "content": "Reasoning models with chain-of-thought (CoT) can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. Detecting this safety commitment point requires monitoring, but a prior question remains unanswered: should a monitoring system read the model's hidden states or its generated text? We show that this comparison's outcome depends critically on an underexamined researcher degree of freedom: which transformer layer to monitor. Through systematic evaluation of hidden-state (HS) and text-based probes across four reasoning models, five selection metrics, and seven alternative methods, we find that a biased composite metric masks the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. Principled selection recovers significant HS precision gains (+15.4 to +21.9pp, Holm-Bonferroni corrected), with evidence from strong (OT-7B, 5/5 seeds) to qualified (R1-32B, position-mediated). Encoder quality bounds the advantage: against a stronger 1024d text encoder, only 1/4 models survives correction. Layer selection sensitivity is the robust methodological finding; the empirical HS advantage is conditional, and current probes characterize the commitment phenomenon (FPR 39--52\\%) rather than constitute production detectors.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01YbqcSF5oFFBPAJxEdUH9SR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "6dbe7706-4da4-4e7c-a5f5-ccf77598e71b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 14 · 2026-05-18T22:15:52.462Z_

<details><summary>↩ Tool result · `toolu_01YbqcSF5oFFBPAJxEdUH9SR`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Before building production detectors, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides a systematic characterization of what hidden-state and text-based probes can and cannot detect.
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions, and a further complication is that HS probes require selecting which transformer layer to monitor. Layer selection is a researcher degree of freedom that has received almost no scrutiny in the probing literature, yet we show it can reverse a study's central conclusion.
6	
7	We present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\times$ crossing rate) selects shallow layers for 32B models because shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage. Threshold-dependent metrics excluding crossing rate consistently select deep layers (\cref{tab:layer_selection}), where all four models show significant HS advantage$^\dagger$ (Holm-Bonferroni corrected; precision +15.4 to +21.9pp; \cref{tab:hs_vs_text}), with evidence from strong (OT-7B: 5/5 seeds HB, $+21.9$pp) to qualified (R1-32B$^\dagger$: position-mediated; \cref{sec:experiments}).
8	
9	Our contributions are:
10	\begin{itemize}
11	    \item \textbf{Layer selection sensitivity.} We identify a systematic bias in composite metrics that reverses HS probe conclusions at 32B scale. A five-metric ablation establishes principled selection criteria (\cref{sec:layer-results}).
12	
13	    \item \textbf{Encoder-quality boundary with evidence gradient.} The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\dagger$ (+15.4 to +21.9pp precision, Holm-Bonferroni corrected) but attenuated against 1024d BGE-large (1/4 HB-significant). This boundary suggests the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference (\cref{fig:forest_precision}). PCA capacity matching to 384d preserves significance (+16.8 to +23.1pp, 79--92\% variance retained), providing partial evidence against a pure capacity explanation. Evidence strength varies by model: strong for OT-7B (5/5 seeds HB, $+21.9$pp, no caveats), moderate for R1-8B (FPR seed-fragile, 3/5 HB) and QwQ-32B$^\dagger$ (5/5 HB, negative lead time), and qualified for R1-32B$^\dagger$ (5/5 HB but position-mediated, residualized gap NS; \cref{sec:32b-analysis}).
14	
15	    \item \textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing at any evidence tier (\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE achieves competitive balanced accuracy on QwQ-32B (0.756 vs.\ supervised 0.778) but at substantially lower precision (0.512 vs.\ 0.700); cross-model transfer fails under PCA alignment. Control task selectivity (11.1--16.8pp above chance; \cref{app:control}) confirms genuine safety structure.
16	\end{itemize}
17	
18	\noindent Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\%, and the 76.7\% oracle gap (R1-8B; \cref{sec:oracle}) underscores how much room remains for improvement.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "fdb103e8-31fd-4929-ab4a-bd15f9681873",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nReasoning models such as DeepSeek-R1~\\cite{deepseekr1} and QwQ~\\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \\textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Before building production detectors, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides a systematic characterization of what hidden-state and text-based probes can and cannot detect.\n\nExisting safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\\cite{trajguard} and SafeSwitch~\\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions, and a further complication is that HS probes require selecting which transformer layer to monitor. Layer selection is a researcher degree of freedom that has received almost no scrutiny in the probing literature, yet we show it can reverse a study's central conclusion.\n\nWe present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\\times$ crossing rate) selects shallow layers for 32B models because shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage. Threshold-dependent metrics excluding crossing rate consistently select deep layers (\\cref{tab:layer_selection}), where all four models show significant HS advantage$^\\dagger$ (Holm-Bonferroni corrected; precision +15.4 to +21.9pp; \\cref{tab:hs_vs_text}), with evidence from strong (OT-7B: 5/5 seeds HB, $+21.9$pp) to qualified (R1-32B$^\\dagger$: position-mediated; \\cref{sec:experiments}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{Layer selection sensitivity.} We identify a systematic bias in composite metrics that reverses HS probe conclusions at 32B scale. A five-metric ablation establishes principled selection criteria (\\cref{sec:layer-results}).\n\n    \\item \\textbf{Encoder-quality boundary with evidence gradient.} The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\\dagger$ (+15.4 to +21.9pp precision, Holm-Bonferroni corrected) but attenuated against 1024d BGE-large (1/4 HB-significant). This boundary suggests the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference (\\cref{fig:forest_precision}). PCA capacity matching to 384d preserves significance (+16.8 to +23.1pp, 79--92\\% variance retained), providing partial evidence against a pure capacity explanation. Evidence strength varies by model: strong for OT-7B (5/5 seeds HB, $+21.9$pp, no caveats), moderate for R1-8B (FPR seed-fragile, 3/5 HB) and QwQ-32B$^\\dagger$ (5/5 HB, negative lead time), and qualified for R1-32B$^\\dagger$ (5/5 HB but position-mediated, residualized gap NS; \\cref{sec:32b-analysis}).\n\n    \\item \\textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing at any evidence tier (\\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE achieves competitive balanced accuracy on QwQ-32B (0.756 vs.\\ supervised 0.778) but at substantially lower precision (0.512 vs.\\ 0.700); cross-model transfer fails under PCA alignment. Control task selectivity (11.1--16.8pp above chance; \\cref{app:control}) confirms genuine safety structure.\n\\end{itemize}\n\n\\noindent Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\\%, and the 76.7\\% oracle gap (R1-8B; \\cref{sec:oracle}) underscores how much room remains for improvement.\n",
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_012spab9WrUexBhLMTn6QBgq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "636722d9-4a55-416d-83af-a928dbce2a18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 16 · 2026-05-18T22:15:53.524Z_

<details><summary>↩ Tool result · `toolu_012spab9WrUexBhLMTn6QBgq`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\cite{wang2025lrmsafety}.
5	
6	\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts}, with longer chains increasing circumvention probability~\cite{selfjailbreak}. Reasoning models can autonomously jailbreak other LLMs with 97\% success~\cite{hagendorff2026lrm_jailbreak}. H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\cite{yin2025refusal_cliff}, a phenomenon our temporal probes target. Refusal dynamics in standard LLMs~\cite{hu2026refusal_dynamics} and information leakage in traces~\cite{ahrend2026safer_traces} provide additional context.
7	
8	\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\cite{korbak2025cot_monitorability}. GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model.
9	
10	\textit{Mitigation.} SafeThink~\cite{safethink} steers early reasoning toward safety, SafeRemind~\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.
11	
12	\paragraph{Hidden-State Safety Detection.}
13	Internal activations can detect safety violations in standard LLMs. \citet{zhou2024alignment} show safety-relevant information distributes across layers, while \citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \citet{arditi2024refusal} identify a single refusal direction, but \citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones, consistent with our finding that single-direction methods are insufficient. TrajGuard~\cite{trajguard} uses Mahalanobis distance from safe trajectories; SafeSwitch~\cite{safeswitch} trains hidden-state classifiers; SIREN~\cite{siren} monitors internal representations during generation; SafeDream~\cite{safedream2026} proposes proactive world models for detection. These methods assume threats from external input manipulation and operate at the token level on instruction-tuned models. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \citet{kadali2025internal} decompose internal layer representations to separate jailbreak from benign prompts; their results confirm that layer-wise structure carries safety-relevant signal. We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.
14	
15	\paragraph{Probing Methodology and Layer Selection.}
16	Causal abstraction~\cite{geiger2025causal} provides a theoretical foundation for mechanistic interpretability by formalizing when high-level causal models faithfully describe neural computation, grounding the use of internal representations for behavioral prediction. Linear probing has a long history from layer-wise classifiers~\cite{alain2017understanding} through sentence probing~\cite{conneau2018probing} to comprehensive surveys~\cite{belinkov2019analysis,belinkov2022probing,rogers2020primer}. Layer-wise analyses reveal hierarchical linguistic structure across depth~\cite{jawahar2019bert,liu2019linguistic}, and information-theoretic formulations address probe complexity~\cite{voita2020information,pimentel2020information}. \citet{hewitt2019control} introduce control tasks to distinguish structure from memorization, which we adopt (\cref{app:control}). \citet{ravfogel2020null} introduce iterative nullspace projection (INLP) for concept removal; \citet{ravfogel2022rlace} extend this to closed-form linear adversarial concept erasure. \citet{belrose2023leace} establish theoretical limits on linear probe extraction; \citet{elazar2021amnesic} test whether probed information is causally used. \citet{tenney2019bert} show syntactic information in middle layers and semantics in deeper layers. \citet{marks2024geometry} find emergent linear structure in LLM truth representations, consistent with the linear separability we observe for safety commitment. \citet{zhang2025probing_selfverify} apply hidden-state probing to self-verification in reasoning models, a complementary perspective on what reasoning-model representations encode. Concurrent work by \citet{alvarez2026transport_geometry} uses hidden-state geometry for step-level hallucination detection; the approach shares our temporal probing framework but targets a different phenomenon. \citet{boxo2025linear_probes} show that linear probes can rely on textual evidence rather than deeper representations, which motivates our comparison of hidden-state probes against text-based monitors. Despite this foundation, layer selection remains underexamined: most studies select by a single metric without sensitivity analysis. We demonstrate that this practice can reverse a study's central conclusion (\cref{sec:layer-results}). Our probing approach establishes correlational evidence; causal validation via distributed alignment search~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or inference-time intervention~\citep{li2024iti} would be needed to confirm that probed directions are causally active in safety reasoning. We focus on establishing the observational foundation and identifying the layer selection confound before pursuing causal follow-ups.
17	
18	\paragraph{Change-Point Detection.}
19	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "ae1a4e32-6239-430e-a863-83e53529b650",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related-work}\n\n\\paragraph{Safety in Reasoning Models.}\nReasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\\cite{wang2025lrmsafety}.\n\n\\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\\cite{harmthoughts}, with longer chains increasing circumvention probability~\\cite{selfjailbreak}. Reasoning models can autonomously jailbreak other LLMs with 97\\% success~\\cite{hagendorff2026lrm_jailbreak}. H-CoT~\\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\\cite{yin2025refusal_cliff}, a phenomenon our temporal probes target. Refusal dynamics in standard LLMs~\\cite{hu2026refusal_dynamics} and information leakage in traces~\\cite{ahrend2026safer_traces} provide additional context.\n\n\\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\\cite{korbak2025cot_monitorability}. GuardReasoner~\\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model.\n\n\\textit{Mitigation.} SafeThink~\\cite{safethink} steers early reasoning toward safety, SafeRemind~\\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.\n\n\\paragraph{Hidden-State Safety Detection.}\nInternal activations can detect safety violations in standard LLMs. \\citet{zhou2024alignment} show safety-relevant information distributes across layers, while \\citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \\citet{arditi2024refusal} identify a single refusal direction, but \\citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \\citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \\citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones, consistent with our finding that single-direction methods are insufficient. TrajGuard~\\cite{trajguard} uses Mahalanobis distance from safe trajectories; SafeSwitch~\\cite{safeswitch} trains hidden-state classifiers; SIREN~\\cite{siren} monitors internal representations during generation; SafeDream~\\cite{safedream2026} proposes proactive world models for detection. These methods assume threats from external input manipulation and operate at the token level on instruction-tuned models. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \\citet{kadali2025internal} decompose internal layer representations to separate jailbreak from benign prompts; their results confirm that layer-wise structure carries safety-relevant signal. We reproduce TrajGuard (\\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.\n\n\\paragraph{Probing Methodology and Layer Selection.}\nCausal abstraction~\\cite{geiger2025causal} provides a theoretical foundation for mechanistic interpretability by formalizing when high-level causal models faithfully describe neural computation, grounding the use of internal representations for behavioral prediction. Linear probing has a long history from layer-wise classifiers~\\cite{alain2017understanding} through sentence probing~\\cite{conneau2018probing} to comprehensive surveys~\\cite{belinkov2019analysis,belinkov2022probing,rogers2020primer}. Layer-wise analyses reveal hierarchical linguistic structure across depth~\\cite{jawahar2019bert,liu2019linguistic}, and information-theoretic formulations address probe complexity~\\cite{voita2020information,pimentel2020information}. \\citet{hewitt2019control} introduce control tasks to distinguish structure from memorization, which we adopt (\\cref{app:control}). \\citet{ravfogel2020null} introduce iterative nullspace projection (INLP) for concept removal; \\citet{ravfogel2022rlace} extend this to closed-form linear adversarial concept erasure. \\citet{belrose2023leace} establish theoretical limits on linear probe extraction; \\citet{elazar2021amnesic} test whether probed information is causally used. \\citet{tenney2019bert} show syntactic information in middle layers and semantics in deeper layers. \\citet{marks2024geometry} find emergent linear structure in LLM truth representations, consistent with the linear separability we observe for safety commitment. \\citet{zhang2025probing_selfverify} apply hidden-state probing to self-verification in reasoning models, a complementary perspective on what reasoning-model representations encode. Concurrent work by \\citet{alvarez2026transport_geometry} uses hidden-state geometry for step-level hallucination detection; the approach shares our temporal probing framework but targets a different phenomenon. \\citet{boxo2025linear_probes} show that linear probes can rely on textual evidence rather than deeper representations, which motivates our comparison of hidden-state probes against text-based monitors. Despite this foundation, layer selection remains underexamined: most studies select by a single metric without sensitivity analysis. We demonstrate that this practice can reverse a study's central conclusion (\\cref{sec:layer-results}). Our probing approach establishes correlational evidence; causal validation via distributed alignment search~\\citep{geiger2025causal}, LEACE~\\citep{belrose2023leace}, or inference-time intervention~\\citep{li2024iti} would be needed to confirm that probed directions are causally active in safety reasoning. We focus on establishing the observational foundation and identifying the layer selection confound before pursuing causal follow-ups.\n\n\\paragraph{Change-Point Detection.}\nBOCPD~\\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_016P6DsUX3Q51SvkgJbZ2Wew`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "bbea749d-b0c9-4ea4-b311-4dfc6e2ea843",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 18 · 2026-05-18T22:15:53.877Z_

<details><summary>↩ Tool result · `toolu_016P6DsUX3Q51SvkgJbZ2Wew`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$.
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\begin{table}[t]
12	\centering
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
17	\midrule
18	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
19	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
20	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
21	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
25	\label{tab:models}
26	\end{table}
27	
28	\subsection{Probe Architecture}
29	\label{sec:probe-architecture}
30	
31	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \cref{sec:layer-sensitivity}.
32	
33	\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\citep{wang2020minilm} ($\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.
34	
35	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated under two protocols: a 70/30 train/test split (primary) and the same 60/20/20 split used for LR experiments (for fair comparison; \cref{tab:gru_multi_seeds,app:gru_details}).
36	
37	\subsection{Layer Selection Sensitivity}
38	\label{sec:layer-sensitivity}
39	
40	Layer selection is a researcher degree of freedom that can reverse modality comparison conclusions. A composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B, L10 (16\%) for R1-32B. Shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings are noise-driven (\cref{app:cosine_volatility}).
41	
42	A five-metric ablation reveals that threshold-dependent metrics (precision, inverse FPR, additive composite) consistently select deep layers: L63 (98\%) for both QwQ-32B and R1-32B. Pure balanced accuracy selects layers whose depth varies across data splits and models (7--98\% under 60/20/20; \cref{tab:ba_layer_comparison}). At these layers, all four models show significant HS advantage$^\dagger$ (Holm-Bonferroni corrected; strong for OT-7B, moderate for R1-8B and QwQ-32B$^\dagger$, qualified for R1-32B$^\dagger$; \cref{sec:evaluation}); at biased layers, only the two 7--8B models survive. While we report five metrics, their information content is not independent: BA, precision, and FPR share a confusion matrix with 2 degrees of freedom (given class marginals); crossing rate and the additive composite are derived from these. The effective number of independent statistical tests is four (one per model), as reflected in our HB correction. The five-metric ablation diagnoses which \emph{aspect} of classification performance drives layer selection bias, not five independent pieces of evidence. Holm-Bonferroni step-down on four model-level tests yields the same result (all pass, with R1-8B FPR $p{=}0.044$ at rank-4 threshold $\alpha/1{=}0.050$). A joint (layer, $W$) grid search over 192 configurations confirms that L63 is near-optimal for QwQ-32B at recommended windows ($W{=}3$--$5$; \cref{app:layer_sweep}). Full per-layer results appear in the same appendix.
43	
44	\subsection{Baseline Methods}
45	\label{sec:baselines}
46	
47	We evaluate seven alternatives to contextualize probe performance (\cref{tab:negative}): BOCPD~\citep{adams2007bayesian} and CUSUM~\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\citep{trajguard}; RepE mean-difference directions~\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \cref{app:bocpd_config,app:transfer_details}.
48	
49	\subsection{Evaluation Protocol}
50	\label{sec:evaluation}
51	
52	We report balanced accuracy, precision, pre-CP FPR, coverage, and lead time (steps between first detection and true CP). Step-level metrics evaluate per-step classification; trace-level metrics aggregate across an entire reasoning trace (e.g., trace-level FPR is the fraction of safe traces with any false alarm exceeding $K$ consecutive crossings). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance; sensitivity analysis (\cref{app:k_ablation}) confirms that $K \in \{3, 5, 7\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison, though a post-hoc rationale for $K{=}5$ is that it corresponds to a sustained commitment signal rather than transient fluctuation. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine representational structure (\cref{app:control}). Throughout, $\dagger$ marks conclusions drawn from sample-limited test sets ($n \leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "0342f3e3-2f14-446a-b93f-6334d5e986de",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex",
      "content": "\\section{Problem Setup and Methods}\n\\label{sec:method}\n\n\\subsection{Safety Commitment Point}\n\\label{sec:commitment-point}\n\nWhen a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \\textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \\emph{pre-commitment} ($y_t = 0$); steps at or after CP are \\emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \\in [0, 1]$ estimating whether the model has passed its CP by step $t$.\n\nWe study four reasoning models spanning two architectures and two scales (\\cref{tab:models}).\n\n\\begin{table}[t]\n\\centering\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Arch.} & \\textbf{Params} & \\textbf{Layers} & \\textbf{Hidden} & \\textbf{$n$ (total\\,/\\,test)} \\\\\n\\midrule\nR1-8B & Llama & 8B & 32 & 4096 & 209\\,/\\,43 \\\\\nOT-7B & Qwen & 7B & 28 & 3584 & 228\\,/\\,47 \\\\\nR1-32B & Qwen & 32B & 64 & 5120 & 100\\,/\\,20 \\\\\nQwQ-32B & Qwen & 32B & 64 & 5120 & 95\\,/\\,19 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\\citep{deepseekr1}; QwQ-32B~\\citep{qwq} is a native reasoning model; OT-7B~\\citep{openthinker} is trained with STILL~\\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}\n\\label{tab:models}\n\\end{table}\n\n\\subsection{Probe Architecture}\n\\label{sec:probe-architecture}\n\n\\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\\mathbf{h}_t^{(\\ell)} \\in \\mathbb{R}^d$ from layer $\\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \\cref{sec:layer-sensitivity}.\n\n\\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\\citep{wang2020minilm} ($\\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.\n\n\\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \\ldots, t]$. We evaluate $W \\in \\{1, 3, 5, 10, 15, 20, 25\\}$ and select per-model on validation. GRU sequence models are also evaluated under two protocols: a 70/30 train/test split (primary) and the same 60/20/20 split used for LR experiments (for fair comparison; \\cref{tab:gru_multi_seeds,app:gru_details}).\n\n\\subsection{Layer Selection Sensitivity}\n\\label{sec:layer-sensitivity}\n\nLayer selection is a researcher degree of freedom that can reverse modality comparison conclusions. A composite metric (balanced accuracy $\\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\\% depth) for QwQ-32B, L10 (16\\%) for R1-32B. Shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings are noise-driven (\\cref{app:cosine_volatility}).\n\nA five-metric ablation reveals that threshold-dependent metrics (precision, inverse FPR, additive composite) consistently select deep layers: L63 (98\\%) for both QwQ-32B and R1-32B. Pure balanced accuracy selects layers whose depth varies across data splits and models (7--98\\% under 60/20/20; \\cref{tab:ba_layer_comparison}). At these layers, all four models show significant HS advantage$^\\dagger$ (Holm-Bonferroni corrected; strong for OT-7B, moderate for R1-8B and QwQ-32B$^\\dagger$, qualified for R1-32B$^\\dagger$; \\cref{sec:evaluation}); at biased layers, only the two 7--8B models survive. While we report five metrics, their information content is not independent: BA, precision, and FPR share a confusion matrix with 2 degrees of freedom (given class marginals); crossing rate and the additive composite are derived from these. The effective number of independent statistical tests is four (one per model), as reflected in our HB correction. The five-metric ablation diagnoses which \\emph{aspect} of classification performance drives layer selection bias, not five independent pieces of evidence. Holm-Bonferroni step-down on four model-level tests yields the same result (all pass, with R1-8B FPR $p{=}0.044$ at rank-4 threshold $\\alpha/1{=}0.050$). A joint (layer, $W$) grid search over 192 configurations confirms that L63 is near-optimal for QwQ-32B at recommended windows ($W{=}3$--$5$; \\cref{app:layer_sweep}). Full per-layer results appear in the same appendix.\n\n\\subsection{Baseline Methods}\n\\label{sec:baselines}\n\nWe evaluate seven alternatives to contextualize probe performance (\\cref{tab:negative}): BOCPD~\\citep{adams2007bayesian} and CUSUM~\\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\\citep{trajguard}; RepE mean-difference directions~\\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \\cref{app:bocpd_config,app:transfer_details}.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\nWe report balanced accuracy, precision, pre-CP FPR, coverage, and lead time (steps between first detection and true CP). Step-level metrics evaluate per-step classification; trace-level metrics aggregate across an entire reasoning trace (e.g., trace-level FPR is the fraction of safe traces with any false alarm exceeding $K$ consecutive crossings). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance; sensitivity analysis (\\cref{app:k_ablation}) confirms that $K \\in \\{3, 5, 7\\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison, though a post-hoc rationale for $K{=}5$ is that it corresponds to a sustained commitment signal rather than transient fluctuation. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\\times$ 4 models $= 12$ tests, $\\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\\citep{hewitt2019control} validates genuine representational structure (\\cref{app:control}). Throughout, $\\dagger$ marks conclusions drawn from sample-limited test sets ($n \\leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_0145owcADHcHgQYKHa29j9HM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "065c1a0d-e22d-42b2-850d-b344e110a965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 20 · 2026-05-18T22:15:54.349Z_

<details><summary>↩ Tool result · `toolu_0145owcADHcHgQYKHa29j9HM`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\paragraph{Evidence gradient.} The strength of HS advantage evidence varies by model, not scale. We classify evidence into three tiers based on seed robustness, position independence, and sample size: \textbf{strong} (OT-7B: 5/5 seeds HB, $\Delta$Prec $+21.9$pp, no position confound, selectivity 11.1pp, $n{=}47$); \textbf{moderate} (R1-8B: precision-robust but FPR seed-fragile at 3/5 HB, $n{=}43$; QwQ-32B$^\dagger$: 5/5 HB, $\Delta$Prec $+19.2$pp, negative lead time, position-competitive BA, $n{=}19$); and \textbf{qualified} (R1-32B$^\dagger$: 5/5 HB, $\Delta$Prec std${=}2.0$pp, but position-mediated with residualized gap NS, $W{=}1$ only, $n{=}20$).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\citep{openthinker}; Qwen-7B backbone, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Statistical testing follows \cref{sec:evaluation}.
10	
11	\subsection{Layer Selection Results}\label{sec:layer-results}
12	
13	\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B and L10 (16\%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers at L63 (98\%) for both 32B models. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7--98\% depth under 60/20/20; \cref{tab:ba_layer_comparison}), itself demonstrating that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\times$ smaller than at deep layers across all models (\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\begin{tabular}{lccc}
19	\toprule
20	\textbf{Model} & \textbf{Biased}$^a$ & \textbf{Corrected}$^b$ & $p$ \textbf{(corr.)} \\
21	\midrule
22	R1-8B & L14 (44\%) & L14 (44\%) & ${<}0.001$ \\
23	OT-7B & L0 (0\%) & L16 (57\%) & ${<}0.001$ \\
24	QwQ-32B & L2 (3\%) & L63 (98\%) & ${<}0.005$ \\
25	R1-32B & L10 (16\%) & L63 (98\%) & ${<}0.001$ \\
26	\bottomrule
27	\end{tabular}
28	\caption{Layer selection sensitivity. $^a$\,bal\_acc $\times$ crossing\_rate. $^b$\,Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs.\ text precision $p$-value at corrected layer (e.g., QwQ-32B biased-layer: bal\_acc $p{=}0.35$, precision $p{=}0.83$, both non-significant).}
29	\label{tab:layer_selection}
30	\end{table}
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig_layer_heatmap.pdf}
35	\caption{Per-layer metric heatmap (2$\times$2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal\_acc $\times$ crossing\_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.}
36	\label{fig:layer_heatmap}
37	\end{figure}
38	
39	The downstream impact is severe: at biased layers, only the two 7--8B models show significant HS advantage; both 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction$^\dagger$ (\cref{sec:evaluation}): strong (OT-7B), moderate (R1-8B, QwQ-32B$^\dagger$), and qualified (R1-32B$^\dagger$). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.
40	
41	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
42	
43	\begin{table}[t]
44	\centering
45	\small
46	\resizebox{\columnwidth}{!}{%
47	\begin{tabular}{llclrrlrc}
48	\toprule
49	\textbf{Model} & \textbf{Layer} & \textbf{Enc.} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & \textbf{95\% CI} & $\Delta$\textbf{FPR} & \textbf{HB} \\
50	\midrule
51	R1-8B & L14 & 384d & 3 & +17.5 & +20.1 & [+12.4, +28.3] & $-$7.9 & \checkmark \\
52	 & & 1024d & & \multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \multicolumn{1}{c}{--} & \\[2pt]
53	OT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \checkmark \\
54	 & & 1024d & & \multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \multicolumn{1}{c}{--} & \checkmark \\[2pt]
55	QwQ & L63 & 384d & 5 & +13.0 & +19.2 & [+9.3, +33.5] & $-$15.0 & \checkmark \\
56	 & & 1024d & & \multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \multicolumn{1}{c}{--} & \\[2pt]
57	R1-32B & L63 & 384d & 1 & \textbf{+18.7} & +15.4 & [+8.7, +22.6] & \textbf{$-$14.6} & \checkmark \\
58	 & & 1024d & & \multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \multicolumn{1}{c}{--} & \\
59	\bottomrule
60	\end{tabular}}
61	\caption{HS vs.\ text at corrected layers (LR probes, 60/20/20 split, 10{,}000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS$-$text difference (pp); ``--'' = metric not computed for that encoder comparison. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$); all 384d model-level tests pass$^\dagger$. 1024d: HB over 4 model-level precision tests. Multi-seed stability in \cref{app:multi_seed}. BGE $\Delta$BA/$\Delta$FPR in \cref{app:encoder_robustness}.}
62	\label{tab:hs_vs_text}
63	\end{table}
64	
65	Against the 384d baseline, HS probes significantly outperform text probes across all four models$^\dagger$ (\cref{tab:hs_vs_text}), with evidence from strong (OT-7B: +21.9pp precision) to qualified (R1-32B$^\dagger$: +15.4pp, position-mediated). R1-8B FPR significance is fragile across seeds (2/5 uncorrected, 1/5 Bonferroni-corrected; \cref{tab:r18b_fpr_seeds}). R1-8B FPR advantage is directionally consistent across seeds (5/5) but not robust to data split (2/5 reach $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds, 1/5 remains significant; \cref{app:multi_seed}). At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces), and QwQ-32B's position baseline is competitive (\cref{sec:32b-analysis}). R1-32B passes 5/5 seeds (paired $\Delta$Prec std${=}2.0$pp, despite absolute precision std${=}12.8$pp) but its advantage is position-mediated (residualized gap NS; \cref{app:position_residual}). Overall, 18/20 model-seed combinations pass full HB; R1-8B FPR instability accounts for both failures (\cref{app:multi_seed}). Control task selectivity confirms genuine safety signal: 11.1--16.8pp above chance (\cref{app:control}).
66	
67	\paragraph{Capacity control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\% variance retained) preserves the precision advantage across all four models$^\dagger$ (+16.8 to +23.1pp, all $p{<}0.012$; all model-level precision tests pass Holm-Bonferroni). Two individual metric comparisons are non-significant: R1-8B balanced accuracy (+1.3pp, $p{=}0.731$, effect too small at $n{=}43$) and QwQ-32B FPR ($-$11.4pp, $p{=}0.038$, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder; the control provides partial evidence against a pure capacity explanation but does not rule out representation quality differences between PCA-compressed HS and trained text encoders. Random projection to 384d (structure-destroying, unlike PCA) yields similar results ($\Delta$Prec +8.3 to +20.5pp, all $p{<}0.001$; \cref{app:random_projection}), further weakening the capacity explanation. An LLM-based encoder (E5-Mistral-7B, 4096d$\rightarrow$PCA 384d) yields intermediate results (2/4 HB; \cref{app:e5_mistral}), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4).
68	
69	\paragraph{Encoder robustness.} The 1024d rows in \cref{tab:hs_vs_text} replace MiniLM (384d) with BGE-large~\citep{xiao2023cpack} (1024d, a 2.7$\times$ stronger encoder). The HS precision advantage persists directionally across all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). HS balanced accuracy advantage is also directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni; FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, $p{=}0.564$). The advantage is encoder-conditional rather than absolute (\cref{fig:forest_precision}). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline.
70	
71	\paragraph{Position mediation.} Position ($t/T$) accounts for 9--20pp of balanced accuracy depending on model and window size,\footnote{R1-32B's 20.4pp drop reflects $W{=}1$ (no temporal context); at $W{\geq}3$ with temporal windowing, drops are 9--17pp.} but all models retain non-positional signal above chance (all $p{<}0.001$; \cref{app:position_residual}). Three of four models retain significant non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp ($p{=}0.914$, $n{=}20$), consistent with a position-mediated advantage. Temporal windowing reduces position dependence (R1-8B: 24.3pp drop at $W{=}3$ vs.\ 16.5pp at $W{=}15$).
72	
73	\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces); at $W{\geq}3$, dimensionality ($51200 \times W$ for $n{=}20$) prevents significance. Sweeping regularization $C$ over $[0.01, 100]$ yields ${<}2$pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation ${<}1.5$pp across $\tau \in [0.3, 0.7]$; \cref{app:threshold_sensitivity}). QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \cref{sec:32b-analysis}.
74	
75	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
76	
77	R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\cref{tab:32b_divergence}); training method is the likely differentiator.
78	
79	\begin{table}[t]
80	\centering
81	\small
82	\begin{tabular}{lcccc}
83	\toprule
84	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
85	\midrule
86	R1-32B & 25\% & +11.7 to +13.3 & \checkmark{} ($W{=}1$) & +14.2pp \\
87	QwQ-32B & 74\% & $-$1.2 to +1.9 & \checkmark{} (all $W$) & $-$3.6pp \\
88	\bottomrule
89	\end{tabular}
90	\caption{32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS balanced accuracy minus position-only baseline.}
91	\label{tab:32b_divergence}
92	\end{table}
93	
94	R1-32B detects commitment 11--13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25\% of traces at the single significant window ($W{=}1$). QwQ-32B achieves statistical significance at all window sizes with 74\% coverage, but HS probes fire later than text probes (negative lead time). Consistent with the universal position analysis (\cref{sec:hs-text}), QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\ 0.796). HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are directionally positive but not statistically significant at $n{=}19$. The divergence implies that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale, and a system validated on one 32B model would fail on the other.
95	
96	\subsection{Temporal Context}\label{sec:temporal}
97	
98	Temporal windowing ($W{>}1$) improves both modalities on all models (\cref{fig:window_ablation}). Text precision improves +8 to +23pp from $W{=}1$ to $W{=}25$; HS precision improves +1.7 to +12.9pp. At 7--8B, the modality advantage (+20.1 to +21.9pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing ($W{=}3$--$15$) combined with principled layer selection yields the most consistent gains. Full per-model temporal ablations appear in \cref{app:temporal_details}; GRU sequence models under a matched 60/20/20 split achieve comparable accuracy but higher FPR than LR probes (\cref{tab:gru_multi_seeds}).
99	
100	\begin{figure}[t]
101	\centering
102	\includegraphics[width=\columnwidth]{figures/fig_forest_precision.pdf}
103	\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\ MiniLM-384d; orange: vs.\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction.}
104	\label{fig:forest_precision}
105	\end{figure}
106	
107	\subsection{Negative Results}\label{sec:negative}
108	
109	No alternative method consistently matches supervised probing across the four models at any evidence tier (\cref{tab:negative}). Each failure is diagnostic: BOCPD~\citep{adams2007bayesian}/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation (signal in minor PCA components, $<$5\% variance); RepE~\citep{zou2023representation} is model-dependent (QwQ-32B BA 0.756 but precision 0.512 vs.\ R1-32B BA 0.559); MLP probes overfit (3/4 worse than LR); CCS misaligns with temporal structure; cross-model transfer fails across 17 configurations. Detailed analysis and the full comparison table in \cref{app:negative_details}.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "0a39b3df-64ed-46a9-ab7b-fd85955a72d7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\\label{sec:experiments}\n\nWe evaluate temporal probes across four reasoning models (\\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.\n\n\\paragraph{Evidence gradient.} The strength of HS advantage evidence varies by model, not scale. We classify evidence into three tiers based on seed robustness, position independence, and sample size: \\textbf{strong} (OT-7B: 5/5 seeds HB, $\\Delta$Prec $+21.9$pp, no position confound, selectivity 11.1pp, $n{=}47$); \\textbf{moderate} (R1-8B: precision-robust but FPR seed-fragile at 3/5 HB, $n{=}43$; QwQ-32B$^\\dagger$: 5/5 HB, $\\Delta$Prec $+19.2$pp, negative lead time, position-competitive BA, $n{=}19$); and \\textbf{qualified} (R1-32B$^\\dagger$: 5/5 HB, $\\Delta$Prec std${=}2.0$pp, but position-mediated with residualized gap NS, $W{=}1$ only, $n{=}20$).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\\citep{openthinker}; Qwen-7B backbone, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \\in \\{1, 3, 5, 10, 15, 20, 25\\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Statistical testing follows \\cref{sec:evaluation}.\n\n\\subsection{Layer Selection Results}\\label{sec:layer-results}\n\n\\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\\% depth) for QwQ-32B and L10 (16\\%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers at L63 (98\\%) for both 32B models. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7--98\\% depth under 60/20/20; \\cref{tab:ba_layer_comparison}), itself demonstrating that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\\times$ smaller than at deep layers across all models (\\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\\cref{sec:layer-sensitivity}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Biased}$^a$ & \\textbf{Corrected}$^b$ & $p$ \\textbf{(corr.)} \\\\\n\\midrule\nR1-8B & L14 (44\\%) & L14 (44\\%) & ${<}0.001$ \\\\\nOT-7B & L0 (0\\%) & L16 (57\\%) & ${<}0.001$ \\\\\nQwQ-32B & L2 (3\\%) & L63 (98\\%) & ${<}0.005$ \\\\\nR1-32B & L10 (16\\%) & L63 (98\\%) & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer selection sensitivity. $^a$\\,bal\\_acc $\\times$ crossing\\_rate. $^b$\\,Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs.\\ text precision $p$-value at corrected layer (e.g., QwQ-32B biased-layer: bal\\_acc $p{=}0.35$, precision $p{=}0.83$, both non-significant).}\n\\label{tab:layer_selection}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_layer_heatmap.pdf}\n\\caption{Per-layer metric heatmap (2$\\times$2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal\\_acc $\\times$ crossing\\_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.}\n\\label{fig:layer_heatmap}\n\\end{figure}\n\nThe downstream impact is severe: at biased layers, only the two 7--8B models show significant HS advantage; both 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction$^\\dagger$ (\\cref{sec:evaluation}): strong (OT-7B), moderate (R1-8B, QwQ-32B$^\\dagger$), and qualified (R1-32B$^\\dagger$). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.\n\n\\subsection{HS vs.\\ Text Comparison}\\label{sec:hs-text}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llclrrlrc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{Enc.} & $W$ & $\\Delta$\\textbf{BA} & $\\Delta$\\textbf{Prec} & \\textbf{95\\% CI} & $\\Delta$\\textbf{FPR} & \\textbf{HB} \\\\\n\\midrule\nR1-8B & L14 & 384d & 3 & +17.5 & +20.1 & [+12.4, +28.3] & $-$7.9 & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \\multicolumn{1}{c}{--} & \\\\[2pt]\nOT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \\multicolumn{1}{c}{--} & \\checkmark \\\\[2pt]\nQwQ & L63 & 384d & 5 & +13.0 & +19.2 & [+9.3, +33.5] & $-$15.0 & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \\multicolumn{1}{c}{--} & \\\\[2pt]\nR1-32B & L63 & 384d & 1 & \\textbf{+18.7} & +15.4 & [+8.7, +22.6] & \\textbf{$-$14.6} & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \\multicolumn{1}{c}{--} & \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{HS vs.\\ text at corrected layers (LR probes, 60/20/20 split, 10{,}000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\\Delta$: HS$-$text difference (pp); ``--'' = metric not computed for that encoder comparison. HB: \\checkmark{} = model-level test passes Holm-Bonferroni ($\\alpha{=}0.05$); all 384d model-level tests pass$^\\dagger$. 1024d: HB over 4 model-level precision tests. Multi-seed stability in \\cref{app:multi_seed}. BGE $\\Delta$BA/$\\Delta$FPR in \\cref{app:encoder_robustness}.}\n\\label{tab:hs_vs_text}\n\\end{table}\n\nAgainst the 384d baseline, HS probes significantly outperform text probes across all four models$^\\dagger$ (\\cref{tab:hs_vs_text}), with evidence from strong (OT-7B: +21.9pp precision) to qualified (R1-32B$^\\dagger$: +15.4pp, position-mediated). R1-8B FPR significance is fragile across seeds (2/5 uncorrected, 1/5 Bonferroni-corrected; \\cref{tab:r18b_fpr_seeds}). R1-8B FPR advantage is directionally consistent across seeds (5/5) but not robust to data split (2/5 reach $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds, 1/5 remains significant; \\cref{app:multi_seed}). At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at $W{=}1$ with 25\\% coverage (5/20 traces), and QwQ-32B's position baseline is competitive (\\cref{sec:32b-analysis}). R1-32B passes 5/5 seeds (paired $\\Delta$Prec std${=}2.0$pp, despite absolute precision std${=}12.8$pp) but its advantage is position-mediated (residualized gap NS; \\cref{app:position_residual}). Overall, 18/20 model-seed combinations pass full HB; R1-8B FPR instability accounts for both failures (\\cref{app:multi_seed}). Control task selectivity confirms genuine safety signal: 11.1--16.8pp above chance (\\cref{app:control}).\n\n\\paragraph{Capacity control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\\% variance retained) preserves the precision advantage across all four models$^\\dagger$ (+16.8 to +23.1pp, all $p{<}0.012$; all model-level precision tests pass Holm-Bonferroni). Two individual metric comparisons are non-significant: R1-8B balanced accuracy (+1.3pp, $p{=}0.731$, effect too small at $n{=}43$) and QwQ-32B FPR ($-$11.4pp, $p{=}0.038$, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder; the control provides partial evidence against a pure capacity explanation but does not rule out representation quality differences between PCA-compressed HS and trained text encoders. Random projection to 384d (structure-destroying, unlike PCA) yields similar results ($\\Delta$Prec +8.3 to +20.5pp, all $p{<}0.001$; \\cref{app:random_projection}), further weakening the capacity explanation. An LLM-based encoder (E5-Mistral-7B, 4096d$\\rightarrow$PCA 384d) yields intermediate results (2/4 HB; \\cref{app:e5_mistral}), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4).\n\n\\paragraph{Encoder robustness.} The 1024d rows in \\cref{tab:hs_vs_text} replace MiniLM (384d) with BGE-large~\\citep{xiao2023cpack} (1024d, a 2.7$\\times$ stronger encoder). The HS precision advantage persists directionally across all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). HS balanced accuracy advantage is also directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni; FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, $p{=}0.564$). The advantage is encoder-conditional rather than absolute (\\cref{fig:forest_precision}). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline.\n\n\\paragraph{Position mediation.} Position ($t/T$) accounts for 9--20pp of balanced accuracy depending on model and window size,\\footnote{R1-32B's 20.4pp drop reflects $W{=}1$ (no temporal context); at $W{\\geq}3$ with temporal windowing, drops are 9--17pp.} but all models retain non-positional signal above chance (all $p{<}0.001$; \\cref{app:position_residual}). Three of four models retain significant non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp ($p{=}0.914$, $n{=}20$), consistent with a position-mediated advantage. Temporal windowing reduces position dependence (R1-8B: 24.3pp drop at $W{=}3$ vs.\\ 16.5pp at $W{=}15$).\n\n\\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\\% coverage (5/20 traces); at $W{\\geq}3$, dimensionality ($51200 \\times W$ for $n{=}20$) prevents significance. Sweeping regularization $C$ over $[0.01, 100]$ yields ${<}2$pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation ${<}1.5$pp across $\\tau \\in [0.3, 0.7]$; \\cref{app:threshold_sensitivity}). QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\\% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \\cref{sec:32b-analysis}.\n\n\\subsection{32B Model-Specific Analysis}\\label{sec:32b-analysis}\n\nR1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\\cref{tab:32b_divergence}); training method is the likely differentiator.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Cov.} & \\textbf{Lead (steps)} & \\textbf{HB} & \\textbf{Pos.\\ margin} \\\\\n\\midrule\nR1-32B & 25\\% & +11.7 to +13.3 & \\checkmark{} ($W{=}1$) & +14.2pp \\\\\nQwQ-32B & 74\\% & $-$1.2 to +1.9 & \\checkmark{} (all $W$) & $-$3.6pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \\checkmark{} = model-level test passes Holm-Bonferroni ($\\alpha{=}0.05$). Pos.\\ margin: HS balanced accuracy minus position-only baseline.}\n\\label{tab:32b_divergence}\n\\end{table}\n\nR1-32B detects commitment 11--13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25\\% of traces at the single significant window ($W{=}1$). QwQ-32B achieves statistical significance at all window sizes with 74\\% coverage, but HS probes fire later than text probes (negative lead time). Consistent with the universal position analysis (\\cref{sec:hs-text}), QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\\ 0.796). HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are directionally positive but not statistically significant at $n{=}19$. The divergence implies that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale, and a system validated on one 32B model would fail on the other.\n\n\\subsection{Temporal Context}\\label{sec:temporal}\n\nTemporal windowing ($W{>}1$) improves both modalities on all models (\\cref{fig:window_ablation}). Text precision improves +8 to +23pp from $W{=}1$ to $W{=}25$; HS precision improves +1.7 to +12.9pp. At 7--8B, the modality advantage (+20.1 to +21.9pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing ($W{=}3$--$15$) combined with principled layer selection yields the most consistent gains. Full per-model temporal ablations appear in \\cref{app:temporal_details}; GRU sequence models under a matched 60/20/20 split achieve comparable accuracy but higher FPR than LR probes (\\cref{tab:gru_multi_seeds}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_forest_precision.pdf}\n\\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\\ MiniLM-384d; orange: vs.\\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction.}\n\\label{fig:forest_precision}\n\\end{figure}\n\n\\subsection{Negative Results}\\label{sec:negative}\n\nNo alternative method consistently matches supervised probing across the four models at any evidence tier (\\cref{tab:negative}). Each failure is diagnostic: BOCPD~\\citep{adams2007bayesian}/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation (signal in minor PCA components, $<$5\\% variance); RepE~\\citep{zou2023representation} is model-dependent (QwQ-32B BA 0.756 but precision 0.512 vs.\\ R1-32B BA 0.559); MLP probes overfit (3/4 worse than LR); CCS misaligns with temporal structure; cross-model transfer fails across 17 configurations. Detailed analysis and the full comparison table in \\cref{app:negative_details}.\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Smnjquqsgkj4WXEM2161Y6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "080e426c-67b1-43dd-ae26-9e8701004ec5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 22 · 2026-05-18T22:15:54.814Z_

<details><summary>↩ Tool result · `toolu_01Smnjquqsgkj4WXEM2161Y6`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Our five-metric ablation (\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers, it is significant across all four models$^\dagger$, from strong (OT-7B) to qualified (R1-32B$^\dagger$; \cref{sec:evaluation}). The mechanism is representation compression at shallow layers (\cref{app:cosine_volatility}), which inflates crossing rate independently of discriminative power. The effect likely generalizes to any threshold-based detection study. The HS advantage holds at both BA-optimal and precision-optimal layers regardless of depth: BA-optimal layers span 7--98\% depth across models and splits, yet 14/16 per-model tests pass HB (precision +12.8 to +18.6pp; \cref{tab:ba_layer_comparison}); the two FPR failures come from underpowered 32B test sets ($n{\leq}20$). That BA selection itself produces such depth variation reinforces the methodological finding. For R1-32B, layers L55--L63 at $W{=}1$ form a robust band where all 3/3 metrics pass HB (\cref{app:layer_sweep}).
5	
6	\paragraph{Encoder-quality boundary.}
7	The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\dagger$ (4/4 HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at 7--8B, the modality advantage exceeds temporal improvement; temporal windowing ($W{=}3$ to $15$) provides consistent gains regardless of modality.
8	
9	\paragraph{Guidance for future research.}
10	The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\% early detection with 50-step lead time, while R1-32B reaches only 50\% early detection (\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or ITI~\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "ff89a3c5-4b60-40c6-98a4-e7ce571c8aac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Layer selection as researcher degree of freedom.}\nOur five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers, it is significant across all four models$^\\dagger$, from strong (OT-7B) to qualified (R1-32B$^\\dagger$; \\cref{sec:evaluation}). The mechanism is representation compression at shallow layers (\\cref{app:cosine_volatility}), which inflates crossing rate independently of discriminative power. The effect likely generalizes to any threshold-based detection study. The HS advantage holds at both BA-optimal and precision-optimal layers regardless of depth: BA-optimal layers span 7--98\\% depth across models and splits, yet 14/16 per-model tests pass HB (precision +12.8 to +18.6pp; \\cref{tab:ba_layer_comparison}); the two FPR failures come from underpowered 32B test sets ($n{\\leq}20$). That BA selection itself produces such depth variation reinforces the methodological finding. For R1-32B, layers L55--L63 at $W{=}1$ form a robust band where all 3/3 metrics pass HB (\\cref{app:layer_sweep}).\n\n\\paragraph{Encoder-quality boundary.}\nThe HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\\dagger$ (4/4 HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at 7--8B, the modality advantage exceeds temporal improvement; temporal windowing ($W{=}3$ to $15$) provides consistent gains regardless of modality.\n\n\\paragraph{Guidance for future research.}\nThe evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\\% early detection with 50-step lead time, while R1-32B reaches only 50\\% early detection (\\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \\cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\\citep{geiger2025causal}, LEACE~\\citep{belrose2023leace}, or ITI~\\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01X8rUuDaeWgowc29gSGhNMz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "234874f7-93b4-4bd4-9843-489920c04b14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 24 · 2026-05-18T22:15:55.287Z_

<details><summary>↩ Tool result · `toolu_01X8rUuDaeWgowc29gSGhNMz`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Layer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (\cref{sec:discussion}) would have prevented our initial spurious scale-dependent conclusion and generalizes to any threshold-dependent detection study. The empirical HS advantage is conditional: robust at 7--8B (strong for OT-7B, moderate for R1-8B), position-mediated at 32B (moderate for QwQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 1024d). The methodological contribution is robust; the empirical contribution narrows as encoders improve. Current probes characterize commitment (FPR 39--52\%, oracle gap 76.7\%) rather than constitute production detectors; causal interventions~\citep{meng2022rome,li2024iti} and LLM-based encoders~\citep{wang2024e5mistral} are next steps.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "778dc080-7583-4c4e-af71-fa70ed10cf5f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nLayer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (\\cref{sec:discussion}) would have prevented our initial spurious scale-dependent conclusion and generalizes to any threshold-dependent detection study. The empirical HS advantage is conditional: robust at 7--8B (strong for OT-7B, moderate for R1-8B), position-mediated at 32B (moderate for QwQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 1024d). The methodological contribution is robust; the empirical contribution narrows as encoders improve. Current probes characterize commitment (FPR 39--52\\%, oracle gap 76.7\\%) rather than constitute production detectors; causal interventions~\\citep{meng2022rome,li2024iti} and LLM-based encoders~\\citep{wang2024e5mistral} are next steps.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01Rnv76DJ6kdwQJ1ztSxn2fc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "e0672a31-2b02-4d6c-87a8-da9536f5c4c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 26 · 2026-05-18T22:15:55.755Z_

<details><summary>↩ Tool result · `toolu_01Rnv76DJ6kdwQJ1ztSxn2fc`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{Model-specific caveats and statistical power.}
4	R1-32B achieves significance only at $W{=}1$ (25\% coverage, 5/20 traces) and its HS advantage is position-mediated (residualized gap +1.9pp, $p{=}0.914$; \cref{app:position_residual}). QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\ 0.796) with negative HS lead time. R1-8B FPR significance is seed-fragile (3/5 HB). At $n{=}19$--$20$, the minimum detectable effect at 80\% power is 8.6--9.5pp (\cref{app:power_analysis}); all 32B conclusions marked $\dagger$ should be interpreted with this constraint. Safe-trace FPR is 39--52\%, so current probes characterize the phenomenon rather than constitute production detectors; the 76.7\% oracle gap (\cref{sec:oracle}) confirms that passive probing captures only a fraction of available signal.
5	
6	\paragraph{Hyperparameter selection and scope.}
7	Layer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class at 32B), yielding up to $2{,}240$ configurations; cumulative degrees of freedom are substantial (\cref{app:hyperparameter_robustness} provides convergence, cross-validation, and bootstrap analyses addressing this concern). BA-optimal layer indices are sensitive to the train/validation split, spanning 7--98\% depth across models and splits (\cref{tab:ba_layer_comparison}); for example, OT-7B shifts from L16 to L2 and QwQ-32B from L60 to L63 between 70/30 and 60/20/20 splits, a direct manifestation of the layer selection sensitivity that constitutes our primary finding. Threshold-dependent metrics are more stable but still vary by up to 4 layers. $K$ was pre-selected (\cref{app:k_ablation}); joint (layer, $W$) stability was verified for QwQ-32B (\cref{app:layer_sweep}) but not R1-32B. CP annotations follow HarmThoughts~\citep{harmthoughts} without independent IAA evaluation; if annotation error is ${\geq}2$ steps, QwQ-32B's lead time ($-$1.2 to +1.9) falls within noise, though perturbation analysis shows smooth degradation with no cliff effects (\cref{app:cp_perturbation}). We cover 2 architectures and 2 scales; intermediate scales, proprietary models, and multilingual settings are untested. Results are correlational; causal intervention is needed to confirm mechanistic involvement.
8	
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "1ce06f75-95cf-4706-a51b-2907f3e9e468",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex",
      "content": "\\section{Limitations}\\label{sec:limitations}\n\n\\paragraph{Model-specific caveats and statistical power.}\nR1-32B achieves significance only at $W{=}1$ (25\\% coverage, 5/20 traces) and its HS advantage is position-mediated (residualized gap +1.9pp, $p{=}0.914$; \\cref{app:position_residual}). QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\\ 0.796) with negative HS lead time. R1-8B FPR significance is seed-fragile (3/5 HB). At $n{=}19$--$20$, the minimum detectable effect at 80\\% power is 8.6--9.5pp (\\cref{app:power_analysis}); all 32B conclusions marked $\\dagger$ should be interpreted with this constraint. Safe-trace FPR is 39--52\\%, so current probes characterize the phenomenon rather than constitute production detectors; the 76.7\\% oracle gap (\\cref{sec:oracle}) confirms that passive probing captures only a fraction of available signal.\n\n\\paragraph{Hyperparameter selection and scope.}\nLayer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class at 32B), yielding up to $2{,}240$ configurations; cumulative degrees of freedom are substantial (\\cref{app:hyperparameter_robustness} provides convergence, cross-validation, and bootstrap analyses addressing this concern). BA-optimal layer indices are sensitive to the train/validation split, spanning 7--98\\% depth across models and splits (\\cref{tab:ba_layer_comparison}); for example, OT-7B shifts from L16 to L2 and QwQ-32B from L60 to L63 between 70/30 and 60/20/20 splits, a direct manifestation of the layer selection sensitivity that constitutes our primary finding. Threshold-dependent metrics are more stable but still vary by up to 4 layers. $K$ was pre-selected (\\cref{app:k_ablation}); joint (layer, $W$) stability was verified for QwQ-32B (\\cref{app:layer_sweep}) but not R1-32B. CP annotations follow HarmThoughts~\\citep{harmthoughts} without independent IAA evaluation; if annotation error is ${\\geq}2$ steps, QwQ-32B's lead time ($-$1.2 to +1.9) falls within noise, though perturbation analysis shows smooth degradation with no cliff effects (\\cref{app:cp_perturbation}). We cover 2 architectures and 2 scales; intermediate scales, proprietary models, and multilingual settings are untested. Results are correlational; causal intervention is needed to confirm mechanistic involvement.\n\n",
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01QDTiakRXmPW5X9ejV9b3ct`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "8befe321-38bf-44b2-8c58-8b8ab83bc497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01DNHzZSxPcLWF22ChMcQgU4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "cbcb05ca-c6b9-47f8-bdc1-ca9ddbae06ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZHB14ysNGK7EtdGCSAYG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 29 · 2026-05-18T22:15:56.887Z_

<details><summary>↩ Tool result · `toolu_01DNHzZSxPcLWF22ChMcQgU4`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/discussion}
36	
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\input{sections/appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "241ea55a-ffff-479c-91c8-cd3b986fc0e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}\n\n\\author{Anonymous ARR Submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{sections/abstract}\n\\end{abstract}\n\n\\input{sections/introduction}\n\n\\input{sections/related_work}\n\n\\input{sections/method}\n\n\\input{sections/experiments}\n\n\\input{sections/discussion}\n\n\\input{sections/conclusion}\n\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T22:15:57.031Z_

<details><summary>↩ Tool result · reported error · `toolu_01QDTiakRXmPW5X9ejV9b3ct`</summary>

```text
File content (27439 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "721f2e3b-f7be-458c-b4bd-68a1310e27ad",
  "tool_use_result": "Error: File content (27439 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Assistant

_source line 31_

Now let me read the appendix in parts and run the grep-based checks in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "3ebb510e-3c6c-42d8-9b8f-63f95612d35a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01RpbLpcXVvZucX3PqDzeEhs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "06c9a40d-3b40-4663-b527-ed98cfa35279",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 33 · 2026-05-18T22:16:02.064Z_

<details><summary>↩ Tool result · `toolu_01RpbLpcXVvZucX3PqDzeEhs`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix Contents:}
4	\cref{app:checklist}~Responsible NLP Research Checklist;
5	\cref{app:layer_sweep}~Layer Sweep Results;
6	\cref{app:cosine_volatility}~Representation Compression Analysis;
7	\cref{app:holm_bonferroni}~Holm-Bonferroni Correction;
8	\cref{app:window_ablation}~Window Size Ablation;
9	\cref{app:ot7b_details}~OpenThinker-7B Details;
10	\cref{app:gru_details}~GRU Training Details;
11	\cref{app:control}~Control Task Methodology;
12	\cref{sec:oracle}~Oracle Upper Bound;
13	\cref{app:bocpd_config}~BOCPD/CUSUM Configuration;
14	\cref{app:k_ablation}~Detection Threshold Ablation;
15	\cref{app:threshold_sensitivity}~Decision Threshold Sensitivity;
16	\cref{app:bug}~M002 Bug Disclosure;
17	\cref{app:two_stage}~Adaptive Two-Stage Detection;
18	\cref{app:temporal_details}~Temporal Ablation Details;
19	\cref{app:negative_details}~Negative Results Details (incl.\ \cref{tab:negative});
20	\cref{app:transfer_details}~Cross-Model Transfer Details;
21	\cref{app:encoder_robustness}~Encoder Robustness;
22	\cref{app:position_residual}~Position-Residualized Probing;
23	\cref{app:multi_seed}~Multi-Seed Stability;
24	\cref{tab:ba_layer_comparison}~BA-Layer Modality Comparison;
25	\cref{app:power_analysis}~Post-Hoc Power Analysis.
26	
27	\section{Responsible NLP Research Checklist}
28	\label{app:checklist}
29	
30	We address the ARR Responsible NLP Research requirements below.
31	
32	\begin{itemize}
33	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
34	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.
35	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
36	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
37	    \item \textbf{Human subjects:} No human subjects research was conducted.
38	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
39	\end{itemize}
40	
41	
42	\section{Layer Sweep Results}
43	\label{app:layer_sweep}
44	
45	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-dependent metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects layers whose depth varies with the data split (under 70/30: L30 for QwQ-32B, L47 for R1-32B; under the canonical 60/20/20: L63 and L46 respectively; \cref{tab:ba_layer_results}).
46	
47	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased metric selects L0 (0\%), unbiased consensus selects L16 (57\%). QwQ-32B: biased metric selects L2 (3\%), unbiased consensus selects L63 (98\%). R1-32B: biased metric selects L10 (16\%), unbiased consensus selects L63 (98\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\% of the network while threshold-dependent metrics select layers at 98\% depth. Under 70/30, pure balanced accuracy selects L30 (47\%) for QwQ-32B and L47 (73\%) for R1-32B; under the canonical 60/20/20, it selects L63 (98\%) and L46 (72\%), demonstrating sensitivity to the data split.
48	
49	\paragraph{Impact on modality comparison.} At the biased layers, HS vs.\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the corrected deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\cref{sec:layer-results}).
50	
51	\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition regardless of metric. Under pure balanced accuracy, the dominant layer is selected in 68\% (QwQ-32B: L30, 13/19 folds) and 65\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections cluster in neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L63 for both 32B models) are similarly dominant under threshold-dependent selection.
52	
53	\paragraph{Joint (layer, $W$) sensitivity.} Under the original 70/30 validation protocol, we evaluate QwQ-32B across 64 layers $\times$ 3 windows ($W \in \{1, 3, 5\}$), yielding 192 configurations (\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. (Under 60/20/20, threshold-dependent metrics select L63; the shift from L60 to L63 across splits itself illustrates layer selection sensitivity.) The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \in \{1, 3, 5\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.
54	
55	\begin{table}[h]
56	\centering
57	\small
58	\caption{QwQ-32B joint (layer, $W$) grid search under 70/30 validation. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows. Under the canonical 60/20/20 split, threshold-dependent metrics select L63.}
59	\label{tab:joint_layer_w}
60	\begin{tabular}{clccc}
61	\toprule
62	$W$ & \textbf{Best layer} & \textbf{Best BA} & \textbf{L60 BA} & \textbf{L60 rank} \\
63	\midrule
64	1 & L47 & 0.798 & 0.783 & $\sim$15th \\
65	3 & L46 & 0.817 & 0.796 & $\sim$6th \\
66	5 & L60 & 0.808 & 0.808 & 1st \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	
72	\section{Representation Compression Analysis}
73	\label{app:cosine_volatility}
74	
75	We measure step-to-step cosine distance at biased (shallow) vs.\ corrected (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (\cref{tab:cosine_volatility}).
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\times$ smaller inter-step distances).}
81	\label{tab:cosine_volatility}
82	\begin{tabular}{llcc}
83	\toprule
84	\textbf{Model} & \textbf{Layer (type)} & \textbf{Mean} & \textbf{Std} \\
85	\midrule
86	R1-8B & L2 (biased) & 0.186 & 0.097 \\
87	 & L14 (corrected) & 0.411 & 0.143 \\[2pt]
88	OT-7B & L2 (biased) & 0.077 & 0.080 \\
89	 & L16 (corrected) & 0.206 & 0.091 \\[2pt]
90	QwQ-32B & L2 (biased) & 0.037 & 0.064 \\
91	 & L63 (corrected) & 0.084 & 0.056 \\[2pt]
92	R1-32B & L10 (biased) & 0.067 & 0.050 \\
93	 & L63 (corrected) & 0.092 & 0.076 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	Shallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\times$ smaller than at deep layers across all models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.
99	
100	
101	\section{Holm-Bonferroni Step-Down Correction}
102	\label{app:holm_bonferroni}
103	
104	\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \alpha / (m - i + 1)$ under the step-down procedure.
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
110	\label{tab:holm_bonferroni}
111	\setlength{\tabcolsep}{4pt}
112	\begin{tabular}{clllcc}
113	\toprule
114	\textbf{Rank} & \textbf{Model} & \textbf{Metric} & \textbf{$p$-val} & \textbf{Thresh.} & \textbf{Pass} \\
115	\midrule
116	1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
117	2  & OT-7B  & Bal.\ Acc. & $<$0.001 & 0.0045 & \checkmark \\
118	3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \checkmark \\
119	4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \checkmark \\
120	5  & QwQ-32B & Bal.\ Acc. & $<$0.001 & 0.0063 & \checkmark \\
121	6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \checkmark \\
122	7  & R1-32B & Bal.\ Acc. & $<$0.001 & 0.0083 & \checkmark \\
123	8  & R1-32B & Precision & $<$0.001 & 0.0100 & \checkmark \\
124	9  & QwQ-32B & FPR & 0.004 & 0.0125 & \checkmark \\
125	10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
126	11 & R1-32B & FPR & 0.007 & 0.0250 & \checkmark \\
127	12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
133	
134	\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\alpha{=}0.05$: QwQ-32B (bal\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of distributional assumptions at small $n$.
135	
136	
137	\section{Window Size Ablation Details}
138	\label{app:window_ablation}
139	
140	\cref{tab:window_full} reports the complete window size ablation across all models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) while FPR drops from 9.65\% to 4.8\%.
141	
142	\begin{figure}[h]
143	\centering
144	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
145	\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
146	\label{fig:window_ablation}
147	\end{figure}
148	
149	\begin{table}[h]
150	\centering
151	\small
152	\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
153	\label{tab:window_full}
154	\resizebox{\columnwidth}{!}{%
155	\begin{tabular}{llccccc}
156	\toprule
157	Model & $W$ & Bal.\ Acc. & Precision & FPR$_{\text{step}}$ & Coverage & Lead \\
158	\midrule
159	\multirow{7}{*}{R1-8B}
160	 & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\
161	 & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\
162	 & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\
163	 & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\
164	 & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\
165	 & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\
166	 & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\
167	\midrule
168	\multirow{7}{*}{OT-7B}
169	 & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\
170	 & 3  & \textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\
171	 & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\
172	 & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\
173	 & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\
174	 & 20 & 66.0 & \textbf{49.4} & \textbf{7.5} & 48.9 & 17.9 \\
175	 & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\
176	\midrule
177	\multirow{7}{*}{R1-32B}
178	 & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\
179	 & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\
180	 & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\
181	 & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\
182	 & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\
183	 & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\
184	 & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\
185	\midrule
186	\multirow{7}{*}{QwQ-32B}
187	 & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\
188	 & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\
189	 & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\
190	 & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\
191	 & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\
192	 & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\
193	 & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\
194	\bottomrule
195	\end{tabular}}%
196	\end{table}
197	
198	Key cross-model patterns emerge from the window ablation:
199	
200	\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
201	
202	\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}20$), and FPR drops from 12.0\% to 7.5\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the corrected layer selection (\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.
203	
204	\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
205	
206	\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
207	
208	\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
209	
210	\subsection{Text Probe Window Ablation}
211	\label{app:text_window}
212	
213	\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
214	
215	\begin{table}[h]
216	\centering
217	\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
218	\label{tab:text_window}
219	\begin{tabular}{lcccc}
220	\toprule
221	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
222	\midrule
223	 1  & 64.7 & 41.6 & 25.8 & 95.4 \\
224	 3  & 66.9 & 44.8 & 23.1 & 90.7 \\
225	 5  & 69.2 & 48.5 & 20.4 & 84.9 \\
226	 10 & 72.1 & 54.3 & 16.7 & 74.4 \\
227	 15 & 74.3 & 58.9 & 14.2 & 67.4 \\
228	 20 & 75.8 & 62.1 & 12.5 & 62.8 \\
229	 25 & 76.7 & 64.8 & 11.8 & 58.1 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	Text probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.
235	
236	
237	\section{OpenThinker-7B Detailed Results}
238	\label{app:ot7b_details}
239	
240	OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
241	
242	\paragraph{Layer sweep.}
243	
244	\begin{table}[h]
245	\centering
246	\small
247	\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
248	\label{tab:ot7b_layer_sweep}
249	\setlength{\tabcolsep}{4pt}
250	\begin{tabular}{lcccc}
251	\toprule
252	Layer & Depth & Bal.\ Acc. & Cross.\ Rate & Score \\
253	\midrule
254	0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\
255	4 & 14 & 66.3 & 40.4 & 26.8 \\
256	8 & 29 & 66.4 & 25.5 & 17.0 \\
257	12 & 43 & 67.5 & 31.9 & 21.6 \\
258	16 & 57 & 68.2 & 31.9 & 21.8 \\
259	20 & 71 & 65.5 & 31.9 & 20.9 \\
260	24 & 86 & 66.9 & 29.8 & 19.9 \\
261	27 & 96 & 63.0 & 31.9 & 20.1 \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers under the 70/30 split used here; under the canonical 60/20/20 split, BA selects L2 (7\% depth; \cref{tab:ba_layer_results}). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
267	
268	\paragraph{Text probe window ablation.}
269	
270	\begin{table}[h]
271	\centering
272	\small
273	\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
274	\label{tab:ot7b_text_window}
275	\begin{tabular}{lcccc}
276	\toprule
277	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
278	\midrule
279	 1  & 58.1 & 24.5 & 34.5 & 63.8 \\
280	 3  & 57.9 & 25.4 & 27.1 & 74.5 \\
281	 5  & 56.9 & 24.7 & 25.5 & 70.2 \\
282	 10 & 58.3 & 27.0 & 22.2 & 70.2 \\
283	 15 & 58.9 & 28.3 & 20.0 & 66.0 \\
284	 20 & 60.9 & 31.6 & 17.6 & 66.0 \\
285	 25 & 61.4 & 32.9 & 16.1 & 66.0 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
291	
292	\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\% trace-level balanced accuracy vs.\ 65.6\% for text (bootstrap $\Delta{=}$+10.7pp, 95\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\% vs.\ 34.6\% (bootstrap $\Delta{=}$+21.9pp, 95\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\% vs.\ 27.1\% (bootstrap $\Delta{=}{-}17.1$pp, 95\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\times$ more temporal context.
293	
294	
295	\section{GRU Training Details}
296	\label{app:gru_details}
297	
298	\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
299	
300	\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
301	
302	\paragraph{Training procedure.} We train with Adam (learning rate $1 \times 10^{-3}$, default $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.
303	
304	\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\pm$ standard deviation.
305	
306	\paragraph{Per-seed results for R1-8B (single-layer GRU).}
307	
308	\begin{table}[h]
309	\centering
310	\small
311	\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
312	\label{tab:gru_seeds}
313	\setlength{\tabcolsep}{4pt}
314	\begin{tabular}{lccc}
315	\toprule
316	Seed & Peak Acc. & Crossing Acc. & Lead (steps) \\
317	\midrule
318	1 & 85.2 & 74.3 & +4.8 \\
319	2 & 83.1 & 71.6 & +4.8 \\
320	3 & 83.4 & 70.4 & +0.9 \\
321	\midrule
322	Mean $\pm$ std & 83.9 $\pm$ 1.1 & 72.1 $\pm$ 2.0 & +3.5 $\pm$ 2.3 \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.
328	
329	\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}
330	
331	\begin{table}[h]
332	\centering
333	\scriptsize
334	\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
335	\label{tab:gru_multi_seeds}
336	\resizebox{\columnwidth}{!}{%
337	\begin{tabular}{llccccc}
338	\toprule
339	Model & Seed & Acc & Prec & FPR & Cross.\% & Lead \\
340	\midrule
341	GRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\% & 3.55 \\
342	GRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\% & 7.39 \\
343	GRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\% & 8.45 \\
344	\rowcolor{gray!10}
345	GRU-single & \textit{mean} & 0.799$\pm$0.035 & 0.528$\pm$0.091 & 0.178$\pm$0.028 & 68.2$\pm$2.9\% & 6.46$\pm$2.10 \\
346	\midrule
347	GRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\% & 5.66 \\
348	GRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\% & 6.43 \\
349	GRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\% & 8.93 \\
350	\rowcolor{gray!10}
351	GRU-multi  & \textit{mean} & 0.789$\pm$0.027 & 0.510$\pm$0.075 & 0.189$\pm$0.018 & 68.2$\pm$4.4\% & 7.01$\pm$1.40 \\
352	\midrule
353	LR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\% & $-$2.00 \\
354	LR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\% & 5.26 \\
355	LR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\% & 3.94 \\
356	\rowcolor{gray!10}
357	LR-single  & \textit{mean} & 0.803$\pm$0.037 & 0.547$\pm$0.108 & 0.141$\pm$0.035 & 47.3$\pm$4.8\% & 2.40$\pm$3.16 \\
358	\midrule
359	LR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\% & 1.06 \\
360	LR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\% & 7.30 \\
361	LR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\% & 4.00 \\
362	\rowcolor{gray!10}
363	LR-multi   & \textit{mean} & 0.800$\pm$0.032 & 0.547$\pm$0.099 & 0.134$\pm$0.036 & 40.3$\pm$4.8\% & 4.12$\pm$2.55 \\
364	\bottomrule
365	\end{tabular}}%
366	\end{table}
367	
368	Under this protocol, multi-layer GRU achieves the highest mean lead (7.01$\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.
369	
370	\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}
371	OT-7B GRU achieves 74.6$\pm$1.3\% balanced accuracy, 64.5$\pm$7.0\% coverage, +33.6$\pm$4.8 steps lead, and 27.4$\pm$6.1\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\sim}$80 reasoning steps (vs.\ ${\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), confirming that GRUs gain lead time at the cost of more false alarms across both 7-8B models.
372	
373	
374	\section{Control Task Methodology}
375	\label{app:control}
376	
377	We follow the selectivity framework of \cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.
378	
379	\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:
380	\begin{equation}
381	    \text{Selectivity} = \text{Acc}_{\text{linguistic}} - \text{Acc}_{\text{control}}
382	\end{equation}
383	where $\text{Acc}_{\text{linguistic}}$ is the probe accuracy on true labels and $\text{Acc}_{\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.
384	
385	\paragraph{Results.} We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers (60/20/20 split) are: R1-32B 16.8pp (layer 63), QwQ-32B 16.1pp (layer 63), R1-8B 14.1pp (layer 14), OT-7B 11.1pp (layer 16). All values exceed the 5pp threshold recommended by \cite{hewitt2019control}. R1-32B and QwQ-32B achieve the strongest selectivity ($>$16pp) at corrected layers. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
386	
387	\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
388	
389	\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\% FPR compared to 8.1\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.
390	
391	\paragraph{Residualized selectivity.} To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in \cref{app:position_residual}). Residualized selectivity: R1-8B 22.9pp, OT-7B 10.4pp, QwQ-32B 11.3pp (all ${>}5$pp), R1-32B 3.0pp (${<}5$pp, consistent with the position-mediated advantage reported in \cref{sec:hs-text}). Three of four models retain selectivity well above the \citet{hewitt2019control} threshold after position removal; R1-32B's drop confirms that its safety signal is largely positional.
392	
393	
394	\section{Oracle Upper Bound Analysis}
395	\label{sec:oracle}
396	
397	We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.
398	
399	\cref{tab:oracle} reports oracle performance across all four models. Oracle analysis confirms the evidence gradient: OT-7B (strong) shows the highest early detection rate (93.6\%) and longest lead time (50 steps), while R1-32B (qualified) achieves only 50\% early detection even with oracle labels, suggesting that its commitment signal is inherently weaker. On R1-8B, the oracle early detection rate is 76.7\% (33/43 traces detected before CP, with +31 steps mean lead time), compared to +4.5 steps for the best learned probe (GRU). This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.
400	
401	\begin{table}[h]
402	\centering
403	\small
404	\caption{Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. Mean lead: average steps before CP at first detection.}
405	\label{tab:oracle}
406	\begin{tabular}{lcccc}
407	\toprule
408	\textbf{Model} & \textbf{Det.\ Rate} & \textbf{Early Det.} & \textbf{Mean Lead} & $n_{\text{test}}$ \\
409	\midrule
410	R1-8B & 100\% & 76.7\% & 31.0 & 43 \\
411	OT-7B & 100\% & 93.6\% & 50.0 & 47 \\
412	R1-32B$^\dagger$ & 95.0\% & 50.0\% & 32.4 & 20 \\
413	QwQ-32B$^\dagger$ & 100\% & 84.2\% & 24.4 & 19 \\
414	\bottomrule
415	\end{tabular}
416	\end{table}
417	
418	
419	\section{CP Annotation Perturbation}
420	\label{app:cp_perturbation}
421	
422	To assess sensitivity to annotation noise, we shift all ground-truth CP labels by $\delta \in \{-3, \ldots, +3\}$ steps and retrain the HS probe (\cref{tab:cp_perturbation}). Precision degrades smoothly with no cliff effect: within $\pm 2$ steps, BA changes by ${<}2.5$pp for all models (7--8B: ${<}1.0$pp). At the $\pm 3$-step worst case, all models retain precision well above their respective text baselines. These results support the annotation robustness assumption discussed in \cref{sec:limitations}.
423	
424	\begin{table}[h]
425	\centering
426	\small
427	\caption{HS probe sensitivity to CP annotation shift ($\delta$ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects.}
428	\label{tab:cp_perturbation}
429	\begin{tabular}{llccc}
430	\toprule
431	\textbf{Model} & $\delta$ & \textbf{Prec} & \textbf{BA} & \textbf{FPR} \\
432	\midrule
433	R1-8B & $-3$ & .652 & .773 & .177 \\
434	 & $0$ & .596 & .784 & .165 \\
435	 & $+3$ & .530 & .771 & .143 \\[2pt]
436	OT-7B & $-3$ & .404 & .714 & .298 \\
437	 & $0$ & .351 & .707 & .286 \\
438	 & $+3$ & .300 & .702 & .276 \\[2pt]
439	QwQ-32B & $-3$ & .661 & .728 & .158 \\
440	 & $0$ & .609 & .690 & .129 \\
441	 & $+3$ & .550 & .676 & .114 \\[2pt]
442	R1-32B & $-3$ & .625 & .698 & .360 \\
443	 & $0$ & .570 & .722 & .281 \\
444	 & $+3$ & .503 & .750 & .236 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	
450	\section{BOCPD/CUSUM Configuration Sweep}
451	\label{app:bocpd_config}
452	
453	We sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.
454	
455	\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\lambda$ controls the prior probability of a change-point at each step ($P(\text{change}) = 1/\lambda$).
456	
457	\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.
458	
459	\begin{table}[h]
460	\centering
461	\small
462	\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
463	\label{tab:cpd_sweep}
464	\setlength{\tabcolsep}{4pt}
465	\begin{tabular}{llcc}
466	\toprule
467	Method & Configuration & Det.\ Rate & Lead \\
468	\midrule
469	\multirow{5}{*}{BOCPD}
470	 & $\lambda = 5$   & 97 & +2.1 \\
471	 & $\lambda = 10$  & 93 & +3.5 \\
472	 & $\lambda = 20$  & 87 & +4.2 \\
473	 & $\lambda = 50$  & 72 & +5.8 \\
474	 & $\lambda = 100$ & 67.4 & +1.03 \\
475	\midrule
476	\multirow{10}{*}{CUSUM}
477	 & $\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\
478	 & $\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\
479	 & $\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\
480	 & $\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\
481	 & $\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\
482	 & $\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\
483	 & $\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\
484	 & $\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\
485	 & $\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\
486	 & $\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\
487	\midrule
488	Simple threshold & FCP baseline & 65.1 & +4.89 \\
489	\bottomrule
490	\end{tabular}
491	\end{table}
492	
493	The best BOCPD configuration ($\lambda{=}10$) achieves 93.0\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.
494	
495	These results reveal a coverage-timing tradeoff. BOCPD ($\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\% vs.\ 65.1\%), but with lower lead (+3.45 vs.\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.
496	
497	\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.
498	
499	
500	\section{Detection Threshold ($K$) Ablation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "2edc85a8-472d-4c88-9806-7ca145870266",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
      "content": "\\appendix\n\n\\noindent\\textbf{Appendix Contents:}\n\\cref{app:checklist}~Responsible NLP Research Checklist;\n\\cref{app:layer_sweep}~Layer Sweep Results;\n\\cref{app:cosine_volatility}~Representation Compression Analysis;\n\\cref{app:holm_bonferroni}~Holm-Bonferroni Correction;\n\\cref{app:window_ablation}~Window Size Ablation;\n\\cref{app:ot7b_details}~OpenThinker-7B Details;\n\\cref{app:gru_details}~GRU Training Details;\n\\cref{app:control}~Control Task Methodology;\n\\cref{sec:oracle}~Oracle Upper Bound;\n\\cref{app:bocpd_config}~BOCPD/CUSUM Configuration;\n\\cref{app:k_ablation}~Detection Threshold Ablation;\n\\cref{app:threshold_sensitivity}~Decision Threshold Sensitivity;\n\\cref{app:bug}~M002 Bug Disclosure;\n\\cref{app:two_stage}~Adaptive Two-Stage Detection;\n\\cref{app:temporal_details}~Temporal Ablation Details;\n\\cref{app:negative_details}~Negative Results Details (incl.\\ \\cref{tab:negative});\n\\cref{app:transfer_details}~Cross-Model Transfer Details;\n\\cref{app:encoder_robustness}~Encoder Robustness;\n\\cref{app:position_residual}~Position-Residualized Probing;\n\\cref{app:multi_seed}~Multi-Seed Stability;\n\\cref{tab:ba_layer_comparison}~BA-Layer Modality Comparison;\n\\cref{app:power_analysis}~Post-Hoc Power Analysis.\n\n\\section{Responsible NLP Research Checklist}\n\\label{app:checklist}\n\nWe address the ARR Responsible NLP Research requirements below.\n\n\\begin{itemize}\n    \\item \\textbf{Limitations discussed:} Yes (\\cref{sec:limitations}).\n    \\item \\textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.\n    \\item \\textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.\n    \\item \\textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.\n    \\item \\textbf{Human subjects:} No human subjects research was conducted.\n    \\item \\textbf{Reproducibility:} All hyperparameters are reported in \\cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.\n\\end{itemize}\n\n\n\\section{Layer Sweep Results}\n\\label{app:layer_sweep}\n\nFor each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-dependent metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects layers whose depth varies with the data split (under 70/30: L30 for QwQ-32B, L47 for R1-32B; under the canonical 60/20/20: L63 and L46 respectively; \\cref{tab:ba_layer_results}).\n\n\\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\\% depth). OT-7B: biased metric selects L0 (0\\%), unbiased consensus selects L16 (57\\%). QwQ-32B: biased metric selects L2 (3\\%), unbiased consensus selects L63 (98\\%). R1-32B: biased metric selects L10 (16\\%), unbiased consensus selects L63 (98\\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\\% of the network while threshold-dependent metrics select layers at 98\\% depth. Under 70/30, pure balanced accuracy selects L30 (47\\%) for QwQ-32B and L47 (73\\%) for R1-32B; under the canonical 60/20/20, it selects L63 (98\\%) and L46 (72\\%), demonstrating sensitivity to the data split.\n\n\\paragraph{Impact on modality comparison.} At the biased layers, HS vs.\\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the corrected deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\\cref{sec:layer-results}).\n\n\\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition regardless of metric. Under pure balanced accuracy, the dominant layer is selected in 68\\% (QwQ-32B: L30, 13/19 folds) and 65\\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections cluster in neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L63 for both 32B models) are similarly dominant under threshold-dependent selection.\n\n\\paragraph{Joint (layer, $W$) sensitivity.} Under the original 70/30 validation protocol, we evaluate QwQ-32B across 64 layers $\\times$ 3 windows ($W \\in \\{1, 3, 5\\}$), yielding 192 configurations (\\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. (Under 60/20/20, threshold-dependent metrics select L63; the shift from L60 to L63 across splits itself illustrates layer selection sensitivity.) The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \\in \\{1, 3, 5\\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{QwQ-32B joint (layer, $W$) grid search under 70/30 validation. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows. Under the canonical 60/20/20 split, threshold-dependent metrics select L63.}\n\\label{tab:joint_layer_w}\n\\begin{tabular}{clccc}\n\\toprule\n$W$ & \\textbf{Best layer} & \\textbf{Best BA} & \\textbf{L60 BA} & \\textbf{L60 rank} \\\\\n\\midrule\n1 & L47 & 0.798 & 0.783 & $\\sim$15th \\\\\n3 & L46 & 0.817 & 0.796 & $\\sim$6th \\\\\n5 & L60 & 0.808 & 0.808 & 1st \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Representation Compression Analysis}\n\\label{app:cosine_volatility}\n\nWe measure step-to-step cosine distance at biased (shallow) vs.\\ corrected (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (\\cref{tab:cosine_volatility}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\\times$ smaller inter-step distances).}\n\\label{tab:cosine_volatility}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer (type)} & \\textbf{Mean} & \\textbf{Std} \\\\\n\\midrule\nR1-8B & L2 (biased) & 0.186 & 0.097 \\\\\n & L14 (corrected) & 0.411 & 0.143 \\\\[2pt]\nOT-7B & L2 (biased) & 0.077 & 0.080 \\\\\n & L16 (corrected) & 0.206 & 0.091 \\\\[2pt]\nQwQ-32B & L2 (biased) & 0.037 & 0.064 \\\\\n & L63 (corrected) & 0.084 & 0.056 \\\\[2pt]\nR1-32B & L10 (biased) & 0.067 & 0.050 \\\\\n & L63 (corrected) & 0.092 & 0.076 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nShallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\\times$ smaller than at deep layers across all models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.\n\n\n\\section{Holm-Bonferroni Step-Down Correction}\n\\label{app:holm_bonferroni}\n\n\\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \\alpha / (m - i + 1)$ under the step-down procedure.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}\n\\label{tab:holm_bonferroni}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{clllcc}\n\\toprule\n\\textbf{Rank} & \\textbf{Model} & \\textbf{Metric} & \\textbf{$p$-val} & \\textbf{Thresh.} & \\textbf{Pass} \\\\\n\\midrule\n1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \\checkmark \\\\\n2  & OT-7B  & Bal.\\ Acc. & $<$0.001 & 0.0045 & \\checkmark \\\\\n3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \\checkmark \\\\\n4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \\checkmark \\\\\n5  & QwQ-32B & Bal.\\ Acc. & $<$0.001 & 0.0063 & \\checkmark \\\\\n6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \\checkmark \\\\\n7  & R1-32B & Bal.\\ Acc. & $<$0.001 & 0.0083 & \\checkmark \\\\\n8  & R1-32B & Precision & $<$0.001 & 0.0100 & \\checkmark \\\\\n9  & QwQ-32B & FPR & 0.004 & 0.0125 & \\checkmark \\\\\n10 & R1-8B  & Bal.\\ Acc. & 0.005 & 0.0167 & \\checkmark \\\\\n11 & R1-32B & FPR & 0.007 & 0.0250 & \\checkmark \\\\\n12 & R1-8B  & FPR & 0.044 & 0.0500 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\\%), which leaves less room for HS improvement on this metric.\n\n\\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\\alpha{=}0.05$: QwQ-32B (bal\\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \\cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of distributional assumptions at small $n$.\n\n\n\\section{Window Size Ablation Details}\n\\label{app:window_ablation}\n\n\\cref{tab:window_full} reports the complete window size ablation across all models and seven window sizes. The main text (\\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \\cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$) while FPR drops from 9.65\\% to 4.8\\%.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_temporal_improvement.pdf}\n\\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$); FPR: 9.65\\% to 4.8\\%.}\n\\label{fig:window_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}\n\\label{tab:window_full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\nModel & $W$ & Bal.\\ Acc. & Precision & FPR$_{\\text{step}}$ & Coverage & Lead \\\\\n\\midrule\n\\multirow{7}{*}{R1-8B}\n & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\\\\n & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\\\\n & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\\\\n & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\\\\n & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\\\\n & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\\\\n & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\\\\n\\midrule\n\\multirow{7}{*}{OT-7B}\n & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\\\\n & 3  & \\textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\\\\n & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\\\\n & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\\\\n & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\\\\n & 20 & 66.0 & \\textbf{49.4} & \\textbf{7.5} & 48.9 & 17.9 \\\\\n & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\\\\n\\midrule\n\\multirow{7}{*}{R1-32B}\n & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\\\\n & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\\\\n & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\\\\n & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\\\\n & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\\\\n & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\\\\n & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\\\\n\\midrule\n\\multirow{7}{*}{QwQ-32B}\n & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\\\\n & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\\\\n & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\\\\n & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\\\\n & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\\\\n & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\\\\n & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\end{table}\n\nKey cross-model patterns emerge from the window ablation:\n\n\\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\\% ($W{=}1$) to 81.0\\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\\% to 4.83\\%). Coverage trades off against quality, dropping from 72.1\\% to 48.8\\%.\n\n\\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\\% ($W{=}1$) to 49.4\\% ($W{=}20$), and FPR drops from 12.0\\% to 7.5\\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the corrected layer selection (\\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.\n\n\\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\\%) and highest precision (60.9\\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).\n\n\\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\\%), dips at $W{=}10$--$15$, then recovers to 76.2\\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\\% to 61.8\\% precision; 22.76\\% to 16.94\\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.\n\n\\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.\n\n\\subsection{Text Probe Window Ablation}\n\\label{app:text_window}\n\n\\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}\n\\label{tab:text_window}\n\\begin{tabular}{lcccc}\n\\toprule\n$W$ & Bal. Acc. & Precision & FPR & Coverage \\\\\n\\midrule\n 1  & 64.7 & 41.6 & 25.8 & 95.4 \\\\\n 3  & 66.9 & 44.8 & 23.1 & 90.7 \\\\\n 5  & 69.2 & 48.5 & 20.4 & 84.9 \\\\\n 10 & 72.1 & 54.3 & 16.7 & 74.4 \\\\\n 15 & 74.3 & 58.9 & 14.2 & 67.4 \\\\\n 20 & 75.8 & 62.1 & 12.5 & 62.8 \\\\\n 25 & 76.7 & 64.8 & 11.8 & 58.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nText probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.\n\n\n\\section{OpenThinker-7B Detailed Results}\n\\label{app:ot7b_details}\n\nOpenThinker-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.\n\n\\paragraph{Layer sweep.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{OT-7B layer sweep. Score = balanced accuracy $\\times$ crossing rate. Layer 16 (57\\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}\n\\label{tab:ot7b_layer_sweep}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Depth & Bal.\\ Acc. & Cross.\\ Rate & Score \\\\\n\\midrule\n0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\\\\n4 & 14 & 66.3 & 40.4 & 26.8 \\\\\n8 & 29 & 66.4 & 25.5 & 17.0 \\\\\n12 & 43 & 67.5 & 31.9 & 21.6 \\\\\n16 & 57 & 68.2 & 31.9 & 21.8 \\\\\n20 & 71 & 65.5 & 31.9 & 20.9 \\\\\n24 & 86 & 66.9 & 29.8 & 19.9 \\\\\n27 & 96 & 63.0 & 31.9 & 20.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter correction of a layer selection bug, layer 16 (57\\% depth) is selected. It achieves the highest balanced accuracy (68.2\\%) among transformer layers under the 70/30 split used here; under the canonical 60/20/20 split, BA selects L2 (7\\% depth; \\cref{tab:ba_layer_results}). Layer 0 (embedding) has a higher crossing rate (53.2\\% vs.\\ 31.9\\%) but lower accuracy.\n\n\\paragraph{Text probe window ablation.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}\n\\label{tab:ot7b_text_window}\n\\begin{tabular}{lcccc}\n\\toprule\n$W$ & Bal. Acc. & Precision & FPR & Coverage \\\\\n\\midrule\n 1  & 58.1 & 24.5 & 34.5 & 63.8 \\\\\n 3  & 57.9 & 25.4 & 27.1 & 74.5 \\\\\n 5  & 56.9 & 24.7 & 25.5 & 70.2 \\\\\n 10 & 58.3 & 27.0 & 22.2 & 70.2 \\\\\n 15 & 58.9 & 28.3 & 20.0 & 66.0 \\\\\n 20 & 60.9 & 31.6 & 17.6 & 66.0 \\\\\n 25 & 61.4 & 32.9 & 16.1 & 66.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.\n\n\\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\\% trace-level balanced accuracy vs.\\ 65.6\\% for text (bootstrap $\\Delta{=}$+10.7pp, 95\\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\\% vs.\\ 34.6\\% (bootstrap $\\Delta{=}$+21.9pp, 95\\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\\% vs.\\ 27.1\\% (bootstrap $\\Delta{=}{-}17.1$pp, 95\\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\\times$ more temporal context.\n\n\n\\section{GRU Training Details}\n\\label{app:gru_details}\n\n\\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\\% training portion, we hold out 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\n\n\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\n\n\\paragraph{Training procedure.} We train with Adam (learning rate $1 \\times 10^{-3}$, default $\\beta_1{=}0.9$, $\\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\n\n\\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\\pm$ standard deviation.\n\n\\paragraph{Per-seed results for R1-8B (single-layer GRU).}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}\n\\label{tab:gru_seeds}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Peak Acc. & Crossing Acc. & Lead (steps) \\\\\n\\midrule\n1 & 85.2 & 74.3 & +4.8 \\\\\n2 & 83.1 & 71.6 & +4.8 \\\\\n3 & 83.4 & 70.4 & +0.9 \\\\\n\\midrule\nMean $\\pm$ std & 83.9 $\\pm$ 1.1 & 72.1 $\\pm$ 2.0 & +3.5 $\\pm$ 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.\n\n\\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}\n\\label{tab:gru_multi_seeds}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Seed & Acc & Prec & FPR & Cross.\\% & Lead \\\\\n\\midrule\nGRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\\% & 3.55 \\\\\nGRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\\% & 7.39 \\\\\nGRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\\% & 8.45 \\\\\n\\rowcolor{gray!10}\nGRU-single & \\textit{mean} & 0.799$\\pm$0.035 & 0.528$\\pm$0.091 & 0.178$\\pm$0.028 & 68.2$\\pm$2.9\\% & 6.46$\\pm$2.10 \\\\\n\\midrule\nGRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\\% & 5.66 \\\\\nGRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\\% & 6.43 \\\\\nGRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\\% & 8.93 \\\\\n\\rowcolor{gray!10}\nGRU-multi  & \\textit{mean} & 0.789$\\pm$0.027 & 0.510$\\pm$0.075 & 0.189$\\pm$0.018 & 68.2$\\pm$4.4\\% & 7.01$\\pm$1.40 \\\\\n\\midrule\nLR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\\% & $-$2.00 \\\\\nLR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\\% & 5.26 \\\\\nLR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\\% & 3.94 \\\\\n\\rowcolor{gray!10}\nLR-single  & \\textit{mean} & 0.803$\\pm$0.037 & 0.547$\\pm$0.108 & 0.141$\\pm$0.035 & 47.3$\\pm$4.8\\% & 2.40$\\pm$3.16 \\\\\n\\midrule\nLR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\\% & 1.06 \\\\\nLR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\\% & 7.30 \\\\\nLR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\\% & 4.00 \\\\\n\\rowcolor{gray!10}\nLR-multi   & \\textit{mean} & 0.800$\\pm$0.032 & 0.547$\\pm$0.099 & 0.134$\\pm$0.036 & 40.3$\\pm$4.8\\% & 4.12$\\pm$2.55 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\end{table}\n\nUnder this protocol, multi-layer GRU achieves the highest mean lead (7.01$\\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.\n\n\\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}\nOT-7B GRU achieves 74.6$\\pm$1.3\\% balanced accuracy, 64.5$\\pm$7.0\\% coverage, +33.6$\\pm$4.8 steps lead, and 27.4$\\pm$6.1\\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\\sim}$80 reasoning steps (vs.\\ ${\\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\\%) is far above the LR probe at layer 16 (10.0\\%), confirming that GRUs gain lead time at the cost of more false alarms across both 7-8B models.\n\n\n\\section{Control Task Methodology}\n\\label{app:control}\n\nWe follow the selectivity framework of \\cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.\n\n\\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:\n\\begin{equation}\n    \\text{Selectivity} = \\text{Acc}_{\\text{linguistic}} - \\text{Acc}_{\\text{control}}\n\\end{equation}\nwhere $\\text{Acc}_{\\text{linguistic}}$ is the probe accuracy on true labels and $\\text{Acc}_{\\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.\n\n\\paragraph{Results.} We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers (60/20/20 split) are: R1-32B 16.8pp (layer 63), QwQ-32B 16.1pp (layer 63), R1-8B 14.1pp (layer 14), OT-7B 11.1pp (layer 16). All values exceed the 5pp threshold recommended by \\cite{hewitt2019control}. R1-32B and QwQ-32B achieve the strongest selectivity ($>$16pp) at corrected layers. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.\n\n\\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.\n\n\\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\\% FPR compared to 8.1\\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.\n\n\\paragraph{Residualized selectivity.} To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in \\cref{app:position_residual}). Residualized selectivity: R1-8B 22.9pp, OT-7B 10.4pp, QwQ-32B 11.3pp (all ${>}5$pp), R1-32B 3.0pp (${<}5$pp, consistent with the position-mediated advantage reported in \\cref{sec:hs-text}). Three of four models retain selectivity well above the \\citet{hewitt2019control} threshold after position removal; R1-32B's drop confirms that its safety signal is largely positional.\n\n\n\\section{Oracle Upper Bound Analysis}\n\\label{sec:oracle}\n\nWe compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.\n\n\\cref{tab:oracle} reports oracle performance across all four models. Oracle analysis confirms the evidence gradient: OT-7B (strong) shows the highest early detection rate (93.6\\%) and longest lead time (50 steps), while R1-32B (qualified) achieves only 50\\% early detection even with oracle labels, suggesting that its commitment signal is inherently weaker. On R1-8B, the oracle early detection rate is 76.7\\% (33/43 traces detected before CP, with +31 steps mean lead time), compared to +4.5 steps for the best learned probe (GRU). This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. Mean lead: average steps before CP at first detection.}\n\\label{tab:oracle}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Det.\\ Rate} & \\textbf{Early Det.} & \\textbf{Mean Lead} & $n_{\\text{test}}$ \\\\\n\\midrule\nR1-8B & 100\\% & 76.7\\% & 31.0 & 43 \\\\\nOT-7B & 100\\% & 93.6\\% & 50.0 & 47 \\\\\nR1-32B$^\\dagger$ & 95.0\\% & 50.0\\% & 32.4 & 20 \\\\\nQwQ-32B$^\\dagger$ & 100\\% & 84.2\\% & 24.4 & 19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{CP Annotation Perturbation}\n\\label{app:cp_perturbation}\n\nTo assess sensitivity to annotation noise, we shift all ground-truth CP labels by $\\delta \\in \\{-3, \\ldots, +3\\}$ steps and retrain the HS probe (\\cref{tab:cp_perturbation}). Precision degrades smoothly with no cliff effect: within $\\pm 2$ steps, BA changes by ${<}2.5$pp for all models (7--8B: ${<}1.0$pp). At the $\\pm 3$-step worst case, all models retain precision well above their respective text baselines. These results support the annotation robustness assumption discussed in \\cref{sec:limitations}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS probe sensitivity to CP annotation shift ($\\delta$ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects.}\n\\label{tab:cp_perturbation}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & $\\delta$ & \\textbf{Prec} & \\textbf{BA} & \\textbf{FPR} \\\\\n\\midrule\nR1-8B & $-3$ & .652 & .773 & .177 \\\\\n & $0$ & .596 & .784 & .165 \\\\\n & $+3$ & .530 & .771 & .143 \\\\[2pt]\nOT-7B & $-3$ & .404 & .714 & .298 \\\\\n & $0$ & .351 & .707 & .286 \\\\\n & $+3$ & .300 & .702 & .276 \\\\[2pt]\nQwQ-32B & $-3$ & .661 & .728 & .158 \\\\\n & $0$ & .609 & .690 & .129 \\\\\n & $+3$ & .550 & .676 & .114 \\\\[2pt]\nR1-32B & $-3$ & .625 & .698 & .360 \\\\\n & $0$ & .570 & .722 & .281 \\\\\n & $+3$ & .503 & .750 & .236 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{BOCPD/CUSUM Configuration Sweep}\n\\label{app:bocpd_config}\n\nWe sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.\n\n\\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\\lambda$ controls the prior probability of a change-point at each step ($P(\\text{change}) = 1/\\lambda$).\n\n\\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}\n\\label{tab:cpd_sweep}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\nMethod & Configuration & Det.\\ Rate & Lead \\\\\n\\midrule\n\\multirow{5}{*}{BOCPD}\n & $\\lambda = 5$   & 97 & +2.1 \\\\\n & $\\lambda = 10$  & 93 & +3.5 \\\\\n & $\\lambda = 20$  & 87 & +4.2 \\\\\n & $\\lambda = 50$  & 72 & +5.8 \\\\\n & $\\lambda = 100$ & 67.4 & +1.03 \\\\\n\\midrule\n\\multirow{10}{*}{CUSUM}\n & $\\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\\\\n & $\\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\\\\n & $\\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\\\\n & $\\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\\\\n & $\\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\\\\n & $\\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\\\\n & $\\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\\\\n & $\\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\\\\n & $\\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\\\\n & $\\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\\\\n\\midrule\nSimple threshold & FCP baseline & 65.1 & +4.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe best BOCPD configuration ($\\lambda{=}10$) achieves 93.0\\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.\n\nThese results reveal a coverage-timing tradeoff. BOCPD ($\\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\\% vs.\\ 65.1\\%), but with lower lead (+3.45 vs.\\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.\n\n\\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\\% detection rate across all tested configurations ($\\lambda \\in \\{5, 10, 50, 100, 200\\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.\n\n\n\\section{Detection Threshold ($K$) Ablation}",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 961
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_012b9FrAt8d3UBjTugypRNP6`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "5a093f74-36b9-4ad5-af49-9930c7c3eca1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 35 · 2026-05-18T22:16:02.767Z_

<details><summary>↩ Tool result · `toolu_012b9FrAt8d3UBjTugypRNP6`</summary>

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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "8208f8a9-4818-44d5-993e-1a1f9e4f81fb",
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

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_018deJsghKyjRx5JHFYoYFkG`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "65c38355-3b29-4e1f-a0a3-c44ddaa114fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 37 · 2026-05-18T22:16:03.717Z_

<details><summary>↩ Tool result · `toolu_018deJsghKyjRx5JHFYoYFkG`</summary>

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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "0d296e7e-69f1-47a0-882e-1d1e7af7d91c",
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

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01WyShfHEBYszCVD9eWigeQU`</summary>

```json
{
  "pattern": ", [a-z]+ing (the|a|an|that|this|our|its|their|how|what|which|more|each|all) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "43491f66-ea44-429e-b4b7-266455da04a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 39 · 2026-05-18T22:16:06.200Z_

<details><summary>↩ Tool result · `toolu_01WyShfHEBYszCVD9eWigeQU`</summary>

```text
docs/paper/sections/related_work.tex:16:[Omitted long matching line]
docs/paper/sections/experiments.tex:67:[Omitted long matching line]
docs/paper/sections/discussion.tex:10:[Omitted long matching line]
docs/paper/sections/method.tex:52:[Omitted long matching line]
docs/paper/sections/appendix.tex:53:[Omitted long matching line]
docs/paper/sections/appendix.tex:109:\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
docs/paper/sections/appendix.tex:134:[Omitted long matching line]
docs/paper/sections/appendix.tex:213:\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
docs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
docs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
docs/paper/sections/appendix.tex:298:\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
docs/paper/sections/appendix.tex:300:\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
docs/paper/sections/appendix.tex:368:[Omitted long matching line]
docs/paper/sections/appendix.tex:371:[Omitted long matching line]
docs/paper/sections/appendix.tex:387:\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
docs/paper/sections/appendix.tex:399:[Omitted long matching line]
docs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\tau{=}0.5$.
docs/paper/sections/appendix.tex:562:[Omitted long matching line]
docs/paper/sections/appendix.tex:636:[Omitted long matching line]
docs/paper/sections/appendix.tex:689:PCA capacity matching (\cref{app:encoder_robustness}) preserves 79--92\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\cref{tab:random_projection}).
docs/paper/sections/appendix.tex:708:[Omitted long matching line]
docs/paper/sections/appendix.tex:733:[Omitted long matching line]
docs/paper/sections/appendix.tex:759:[Omitted long matching line]
docs/paper/sections/appendix.tex:767:The joint search space for layer (${\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.
docs/paper/sections/appendix.tex:932:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "68fd42f9-ade4-4820-b089-8d1b05952570",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:16:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:67:[Omitted long matching line]\ndocs/paper/sections/discussion.tex:10:[Omitted long matching line]\ndocs/paper/sections/method.tex:52:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:53:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:109:\\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}\ndocs/paper/sections/appendix.tex:134:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:213:\\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.\ndocs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.\ndocs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.\ndocs/paper/sections/appendix.tex:298:\\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\\% training portion, we hold out 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\ndocs/paper/sections/appendix.tex:300:\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\ndocs/paper/sections/appendix.tex:368:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:371:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:387:\\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.\ndocs/paper/sections/appendix.tex:399:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\\Delta$BA $= +0.109$ to $+0.126$, $\\Delta$Prec $= +0.113$ to $+0.143$, $\\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\tau{=}0.5$.\ndocs/paper/sections/appendix.tex:562:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:636:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:689:PCA capacity matching (\\cref{app:encoder_robustness}) preserves 79--92\\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\\cref{tab:random_projection}).\ndocs/paper/sections/appendix.tex:708:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:733:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:759:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:767:The joint search space for layer (${\\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.\ndocs/paper/sections/appendix.tex:932:[Omitted long matching line]",
    "numLines": 25
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_0153GjLGa8THizA38EpEkGRX`</summary>

```json
{
  "pattern": "(?i)(Furthermore|Moreover|Additionally|In addition)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "17ea1ce1-5e1d-47c0-96c1-5a7df53eeb99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 41 · 2026-05-18T22:16:07.491Z_

<details><summary>↩ Tool result · `toolu_0153GjLGa8THizA38EpEkGRX`</summary>

```text
docs/paper/sections/appendix.tex:634:\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "735269c5-c5c8-4bcc-9c4d-7c7193632626",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/appendix.tex:634:\\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_01PYxJez2vfjKaxeUhe2AUGr`</summary>

```json
{
  "pattern": "(?i)(It is worth noting|Notably|delve into|leverage|utilize|facilitate|a myriad of|a plethora of|in the realm of|paradigm shift)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "347784a7-aa32-4063-913c-35ec98cceb14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrjiTRVZrU9QEMf5tXV4X3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 415,
      "cache_creation_input_tokens": 14124,
      "cache_read_input_tokens": 25953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14124
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

_source line 43 · 2026-05-18T22:16:09.701Z_

<details><summary>↩ Tool result · `toolu_01PYxJez2vfjKaxeUhe2AUGr`</summary>

```text
docs/paper/sections/appendix.tex:206:\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "5e10ce71-ab3e-42ac-b122-bcbe67ad9b87",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/appendix.tex:206:\\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\\%), dips at $W{=}10$--$15$, then recovers to 76.2\\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\\% to 61.8\\% precision; 22.76\\% to 16.94\\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Let me now look at the -ing phrases more carefully, check for transition words in same paragraphs, and read the rest of the appendix. Let me also get more detail on the -ing phrase matches and the "notably" match.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "91b9f88a-066e-44aa-9bbd-1a6da8abaeb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsHWJnKhjjAcwMfKVwLr2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18437,
      "cache_read_input_tokens": 40077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18437
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

_source line 45_

Let me get more detail on the flagged items and continue reading the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "2f1d62b8-7f27-41ce-9dc1-b28a84f9d31e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsHWJnKhjjAcwMfKVwLr2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18437,
      "cache_read_input_tokens": 40077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18437
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

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_014PuyubuxHiGDvmDKFiGrXd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": 500,
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "6feb50b1-6ca3-4eb2-8919-7e332f0c5181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsHWJnKhjjAcwMfKVwLr2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18437,
      "cache_read_input_tokens": 40077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18437
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

_source line 47 · 2026-05-18T22:16:16.223Z_

<details><summary>↩ Tool result · `toolu_014PuyubuxHiGDvmDKFiGrXd`</summary>

```text
500	\section{Detection Threshold ($K$) Ablation}
501	\label{app:k_ablation}
502	
503	The consecutive-crossings threshold $K$ controls the trade-off between detection coverage and false positive rate. We evaluate $K \in \{1, 3, 5, 7, 10\}$ at $W{=}1$ on all models using HS probes at corrected layers (\cref{tab:k_ablation}).
504	
505	\begin{table}[h]
506	\centering
507	\small
508	\caption{Detection threshold ablation ($W{=}1$, HS probes at corrected layers). Coverage: fraction of jailbreak traces with $\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\geq K$ consecutive false alarms.}
509	\label{tab:k_ablation}
510	\setlength{\tabcolsep}{3pt}
511	\begin{tabular}{lccccccccc}
512	\toprule
513	& \multicolumn{4}{c}{\textbf{Coverage}} & & \multicolumn{4}{c}{\textbf{Safe FPR}} \\
514	\cmidrule{2-5} \cmidrule{7-10}
515	$K$ & R1-8B & OT-7B & QwQ & R1-32B & & R1-8B & OT-7B & QwQ & R1-32B \\
516	\midrule
517	1  & 1.00 & 1.00 & 1.00 & 1.00 & & 1.00 & 0.92 & 1.00 & 0.99 \\
518	3  & 0.74 & 0.79 & 0.95 & 0.90 & & 0.81 & 0.41 & 0.78 & 0.78 \\
519	5  & 0.47 & 0.51 & 0.79 & 0.65 & & 0.63 & 0.19 & 0.65 & 0.47 \\
520	7  & 0.35 & 0.30 & 0.58 & 0.45 & & 0.39 & 0.16 & 0.35 & 0.31 \\
521	10 & 0.14 & 0.21 & 0.32 & 0.35 & & 0.22 & 0.08 & 0.25 & 0.17 \\
522	\bottomrule
523	\end{tabular}
524	\end{table}
525	
526	$K{=}1$ yields perfect coverage but near-perfect safe FPR (0.92--1.00), offering no discrimination. $K{=}5$ is empirically selected as a middle-ground tradeoff: average coverage 0.60 with average safe FPR 0.48 across models. OT-7B benefits most from increasing $K$, reaching 0.19 safe FPR at $K{=}5$ (vs.\ 0.92 at $K{=}1$) while retaining 51\% coverage. Higher $K$ values ($\geq$7) reduce safe FPR further but at steep coverage cost. $K{=}5$ vs.\ $K{=}7$ is the key decision: $K{=}7$ reduces mean safe FPR from 0.48 to 0.30 but drops mean coverage from 0.60 to 0.42.
527	
528	$K$ was set as a design pre-selection before evaluation, not tuned on the validation set; all main-text results use $K{=}5$ without per-model optimization. The $K \times W$ interaction is not fully explored: this ablation uses $W{=}1$ to isolate $K$'s effect, and the joint $K \times W$ surface remains a limitation. At optimal $W$, coverage at $K{=}5$ improves (e.g., R1-8B: 0.47 at $W{=}1$ vs.\ 0.60 at $W{=}15$).
529	
530	
531	\section{Decision Threshold Sensitivity}
532	\label{app:threshold_sensitivity}
533	
534	We evaluate whether the HS advantage depends on the logistic regression decision threshold by sweeping $\tau \in \{0.3, 0.4, 0.5, 0.6, 0.7\}$ for both 32B models at their corrected layers. Results below were conducted at L60 under the 70/30 protocol; main-text results use L63 under 60/20/20. QwQ-32B (L60, $W{=}3$) HS balanced accuracy varies by only 0.53pp across all thresholds, with $\Delta$(HS$-$Text) stable at +8.5 to +9.3pp. \cref{tab:threshold_r132b} reports R1-32B results.
535	
536	\begin{table}[h]
537	\centering
538	\small
539	\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}
540	\label{tab:threshold_r132b}
541	\begin{tabular}{ccccccc}
542	\toprule
543	$\tau$ & HS BA & $\Delta$BA & HS Prec & $\Delta$Prec & HS FPR & $\Delta$FPR \\
544	\midrule
545	0.3 & 0.752 & +0.126 & 0.583 & +0.126 & 0.295 & $-$0.106 \\
546	0.4 & 0.746 & +0.116 & 0.586 & +0.120 & 0.281 & $-$0.092 \\
547	\textbf{0.5} & \textbf{0.742} & \textbf{+0.109} & \textbf{0.588} & \textbf{+0.113} & \textbf{0.273} & $\mathbf{-}$\textbf{0.078} \\
548	0.6 & 0.741 & +0.112 & 0.599 & +0.119 & 0.254 & $-$0.072 \\
549	0.7 & 0.743 & +0.126 & 0.617 & +0.143 & 0.228 & $-$0.084 \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\tau{=}0.5$.
555	
556	
557	\section{M002 Bug Disclosure}
558	\label{app:bug}
559	
560	We disclose a bug discovered during development that affected intermediate results for QwQ-32B.
561	
562	\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).
563	
564	\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the biased composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\cref{sec:layer-results}) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage$^\dagger$ at corrected deep layers, from strong (OT-7B) to qualified (R1-32B) (\cref{tab:hs_vs_text}).
565	
566	\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection correction (\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and biased layer selection. Both are fully resolved in the final analysis.
567	
568	\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. Code and data will be released upon publication.
569	
570	\section{Adaptive Two-Stage Detection}
571	\label{app:two_stage}
572	
573	We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.
574	
575	We merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\text{screen}} \in \{1, 3, 5\}$, $W_{\text{confirm}} \in \{10, 15, 20, 25\}$, and $k \in \{1, 3, 5\}$ on these R1-8B traces. \cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\% precision at 76.9\% coverage, compared to 70.9\% precision at 76.9\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\% precision at 38.5\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.
576	
577	\begin{figure}[h]
578	\centering
579	\includegraphics[width=0.85\columnwidth]{figures/pareto_two_stage.pdf}
580	\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
581	\label{fig:pareto_two_stage}
582	\end{figure}
583	
584	The marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.
585	
586	
587	\section{Temporal Ablation Details}
588	\label{app:temporal_details}
589	
590	Full per-model temporal ablations are reported in \cref{tab:window_full} (\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) with FPR halving (9.65\% to 4.83\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.
591	
592	\section{Negative Results Details}
593	\label{app:negative_details}
594	
595	\begin{table}[h]
596	\centering
597	\small
598	\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}
599	\toprule
600	\textbf{Method} & \textbf{Result} & \textbf{Limitation} \\
601	\midrule
602	BOCPD & 0\% det.\ on 3/4 models & Commitment gradual \\
603	CUSUM & $<$ threshold, all models & Same as BOCPD \\
604	Mahalanobis & $\Delta d \approx 0$ & Signal in minor PCs \\
605	RepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent \\
606	MLP & 3/4 worse than LR & Overfitting \\
607	CCS & No gain over supervised$^b$ & Alignment mismatch \\
608	Transfer & Best 59.5\% (PCA)$^c$ & Model-specific repr. \\
609	\bottomrule
610	\end{tabular}
611	\caption{Seven alternative approaches. $^a$\,RepE QwQ approaches supervised bal\_acc but precision is 0.512 vs.\ LR 0.700. $^b$\,Semi-supervised (requires CP labels). $^c$\,Best direct transfer 67.3\% but 1\% crossing rate.}
612	\label{tab:negative}
613	\end{table}
614	
615	\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). Only R1-8B produces non-zero detection (best: $\lambda{=}10$, 93\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\cref{app:bocpd_config}).
616	
617	\paragraph{Mahalanobis distance.} Following TrajGuard~\cite{trajguard}, Mahalanobis distance from the pre-CP centroid produces $\Delta d \approx 0$ between pre-CP and post-CP steps. The discriminative signal resides in minor PCA components (explaining $<$5\% of total variance) rather than the principal directions that dominate the distance computation.
618	
619	\paragraph{RepE.} Mean-difference directions~\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\ LR 0.700) and FPR (0.309 vs.\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.
620	
621	\paragraph{MLP probes.} Two-layer MLPs ($d \rightarrow 128 \rightarrow 1$, ReLU) underperform logistic regression on 3/4 models. The commitment boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small training sets.
622	
623	\paragraph{CCS.} Contrast-Consistent Search~\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.
624	
625	\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\rightarrow$ QwQ-32B at 59.5\% (PCA-2048). Best direct: QwQ-32B $\rightarrow$ R1-32B at 67.3\% but 1\% crossing rate. Implementation details in \cref{app:transfer_details}.
626	
627	\section{Cross-Model Transfer Implementation Details}
628	\label{app:transfer_details}
629	
630	We test whether safety probes transfer across models by projecting hidden states into a shared dimensionality space and applying cross-model classification.
631	
632	\paragraph{Method.} For each source-target model pair, we apply PCA independently to each model's hidden states, reducing to a shared dimensionality $d \in \{512, 1024, 2048\}$. PCA is fitted on the full dataset (including test traces) for each model separately, a setting favorable to transfer since it maximizes the quality of the projection. A logistic regression classifier (C=1.0, class\_weight=`balanced', max\_iter=2000, random\_state=42) trained on the source model's PCA-projected training data is then applied directly to the target model's PCA-projected test data. No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied; PCA serves as a standard linear dimensionality reduction baseline.
633	
634	\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.
635	
636	\paragraph{Results.} All 17 transfer configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers for same-dimension pairs) fail to produce practically useful transfer. The best PCA result is R1-8B $\rightarrow$ QwQ-32B at 59.5\% balanced accuracy (PCA-2048). The best direct transfer (QwQ-32B $\rightarrow$ R1-32B) reaches 67.3\% balanced accuracy, which exceeds the within-model baseline of 65.2\%. However, this transfer direction achieves only 1\% crossing rate, meaning the transferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. The complete failure under maximally favorable conditions (PCA fitted on full data, no train/test separation for projection) strengthens the conclusion that safety commitment is encoded in model-specific geometric configurations. PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.
637	
638	
639	\section{Encoder Robustness Analysis}
640	\label{app:encoder_robustness}
641	
642	To test whether the HS advantage over text probes depends on the specific text encoder, we replace all-MiniLM-L6-v2 (384d) with BGE-large-en-v1.5 (1024d), a 2.7$\times$ higher-dimensional encoder with stronger semantic representations. \cref{tab:encoder_robustness} reports precision comparisons at each model's corrected layer; \cref{fig:forest_precision} provides a visual summary.
643	
644	\begin{table}[h]
645	\centering
646	\small
647	\caption{HS vs.\ BGE-large (1024d) text probe precision. $\Delta$: HS minus BGE-large. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha{=}0.05$).}
648	\label{tab:encoder_robustness}
649	\begin{tabular}{lcccccc}
650	\toprule
651	\textbf{Model} & \textbf{HS Prec} & \textbf{BGE Prec} & $\Delta$ & \textbf{95\% CI} & $p$ & \textbf{HB} \\
652	\midrule
653	R1-8B & 0.497 & 0.436 & +0.058 & [$-$0.07, +0.20] & 0.185 & No \\
654	OT-7B & 0.446 & 0.263 & +0.181 & [+0.08, +0.29] & ${<}0.001$ & Yes \\
655	R1-32B & 0.588 & 0.475 & +0.117 & [$-$0.00, +0.24] & 0.042 & No \\
656	QwQ-32B & 0.545 & 0.454 & +0.094 & [$-$0.07, +0.28] & 0.132 & No \\
657	\bottomrule
658	\end{tabular}
659	\end{table}
660	
661	The HS precision advantage is directionally consistent across all four models (positive $\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.
662	
663	\paragraph{Balanced accuracy and FPR.} \cref{tab:bge_ba_fpr} reports BGE-large comparisons on balanced accuracy and FPR. HS balanced accuracy advantage is directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni. FPR advantage is significant only for OT-7B. R1-8B shows an adverse FPR direction: HS FPR is 1.2pp higher (worse) than BGE ($p{=}0.564$), the only model where HS does not improve over the stronger encoder on this metric.
664	
665	\begin{table}[h]
666	\centering
667	\small
668	\caption{HS vs.\ BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction (4 tests per metric, $\alpha{=}0.05$).}
669	\label{tab:bge_ba_fpr}
670	\begin{tabular}{lcccccc}
671	\toprule
672	\textbf{Model} & $\Delta$\textbf{BA} & $p$ (BA) & \textbf{HB} & $\Delta$\textbf{FPR} & $p$ (FPR) & \textbf{HB} \\
673	\midrule
674	R1-8B & +8.4 & 0.029 & No & $-$1.2$^\dagger$ & 0.564 & No \\
675	OT-7B & +10.8 & 0.002 & Yes & +10.5 & ${<}0.001$ & Yes \\
676	QwQ-32B & +9.3 & 0.067 & No & +2.7 & 0.368 & No \\
677	R1-32B & +10.9 & 0.008 & Yes & +7.8 & 0.165 & No \\
678	\bottomrule
679	\end{tabular}
680	\begin{flushleft}
681	\scriptsize $^\dagger$Adverse direction: HS FPR higher (worse) than BGE.
682	\end{flushleft}
683	\end{table}
684	
685	
686	\section{Random Projection Baseline}
687	\label{app:random_projection}
688	
689	PCA capacity matching (\cref{app:encoder_robustness}) preserves 79--92\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\cref{tab:random_projection}).
690	
691	\begin{table}[h]
692	\centering
693	\small
694	\caption{Random projection (RP, 384d) vs.\ text (384d MiniLM). All $p < 0.001$ (1{,}000 bootstrap resamples). R1-8B uses $W{=}15$ (Table~3: $W{=}3$); QwQ-32B evaluated at L60 (Table~3: L63). 60/20/20 split.}
695	\label{tab:random_projection}
696	\begin{tabular}{lcccc}
697	\toprule
698	\textbf{Model} & \textbf{RP Prec} & \textbf{Text Prec} & $\Delta$\textbf{Prec} & $\Delta$\textbf{BA} \\
699	\midrule
700	R1-8B & .621 & .416 & +.205 & +.140 \\
701	OT-7B & .371 & .244 & +.127 & +.128 \\
702	QwQ-32B & .563 & .391 & +.172 & +.132 \\
703	R1-32B & .524 & .441 & +.083 & +.085 \\
704	\bottomrule
705	\end{tabular}
706	\end{table}
707	
708	All four models retain significant HS advantage under random projection ($\Delta$Prec +8.3 to +20.5pp), with cross-seed standard deviations below 1.7pp. RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. This weakens a pure capacity explanation: even a structure-destroying projection preserves the HS advantage, suggesting the safety signal is broadly distributed across hidden-state dimensions rather than concentrated in top principal components.
709	
710	
711	\section{LLM-Based Text Encoder Comparison}
712	\label{app:e5_mistral}
713	
714	To test whether an LLM-based text encoder closes the HS advantage gap, we encode each reasoning step with E5-Mistral-7B-Instruct~\citep{wang2024e5mistral} (4096d, reduced to 384d via PCA to match the MiniLM dimensionality). \cref{tab:e5_mistral} reports precision comparisons against HS probes at corrected layers.
715	
716	\begin{table}[h]
717	\centering
718	\small
719	\caption{HS vs.\ E5-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, $\alpha{=}0.05$). MiniLM precision from \cref{tab:hs_vs_text} for reference. 60/20/20 split.}
720	\label{tab:e5_mistral}
721	\begin{tabular}{llccccccc}
722	\toprule
723	\textbf{Model} & \textbf{Layer} & $W$ & \textbf{HS} & \textbf{E5} & \textbf{MiniLM} & $\Delta$(HS$-$E5) & $p$ & \textbf{HB} \\
724	\midrule
725	R1-8B & L14 & 3 & .630 & .480 & .416 & +15.0 & 0.001 & \checkmark \\
726	OT-7B & L16 & 3 & .446 & .321 & .244 & +12.5 & 0.009 & \checkmark \\
727	R1-32B & L63 & 1 & .588 & .506 & .441 & +8.2 & 0.235 & \\
728	QwQ-32B & L63 & 5 & .515 & .447 & .391 & +6.8 & 0.368 & \\
729	\bottomrule
730	\end{tabular}
731	\end{table}
732	
733	The HS advantage partially survives against the LLM encoder: 2/4 models (both 7--8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (22M params, 384d): 4/4 HB; E5-Mistral (7B, PCA 384d): 2/4 HB; BGE-large (335M, 1024d): 1/4 HB (\cref{app:encoder_robustness}). E5 precision consistently falls between MiniLM and HS across all models, confirming that encoder quality progressively narrows the gap. PCA to 384d discards information from the 4096d E5 representation; the comparison controls dimensionality but not representation quality, so the true E5 advantage may be larger than reported here.
734	
735	
736	\section{Position-Residualized Probing}
737	\label{app:position_residual}
738	
739	To quantify non-positional safety signal, we regress out the normalized position $t/T$ from each hidden-state (or text-embedding) vector before training the logistic regression probe. \cref{tab:position_residual} summarizes results across all models at their optimal $W$.
740	
741	\begin{table}[h]
742	\centering
743	\small
744	\begin{tabular}{lcrrrr}
745	\toprule
746	\textbf{Model} & $W$ & \textbf{HS BA} & \textbf{Resid.\ HS BA} & \textbf{Drop} & \textbf{Resid.\ Text BA} \\
747	\midrule
748	R1-8B & 15 & 0.834 & 0.669 & 16.5pp & 0.605 \\
749	R1-8B & 3 & 0.813 & 0.571 & 24.3pp & 0.534 \\
750	OT-7B & 3 & 0.732 & 0.609 & 12.3pp & 0.540 \\
751	QwQ-32B & 3 & 0.796 & 0.619 & 17.7pp & 0.582 \\
752	R1-32B & 1 & 0.756 & 0.552 & 20.4pp & 0.532 \\
753	\bottomrule
754	\end{tabular}
755	\caption{Position-residualized probe balanced accuracy. All residualized HS probes are above chance ($p{<}0.001$). 3/4 models retain significant non-positional HS advantage over text (gap +3.7 to +6.9pp, HB corrected); R1-32B is the exception (+1.9pp, $p{=}0.914$).}
756	\label{tab:position_residual}
757	\end{table}
758	
759	Position accounts for 9--20pp of balanced accuracy depending on model and window size (R1-32B's 20.4pp drop at $W{=}1$ reflects the absence of temporal context), and all models retain non-positional signal above chance ($p{<}0.001$). Three of four models retain significant non-positional HS advantage over text after residualization (OT-7B +6.9pp, R1-8B +6.4pp at $W{=}15$, QwQ-32B +3.7pp; all HB corrected). R1-32B is the exception: residualized HS-text gap is +1.9pp ($p{=}0.914$), indicating its HS advantage is position-mediated. Larger temporal windows reduce position dependence: R1-8B drops 24.3pp at $W{=}3$ but only 16.5pp at $W{=}15$.
760	
761	For QwQ-32B specifically, three complementary significance tests confirm the residualized probe performs above chance: Wilcoxon signed-rank $p{=}0.0024$, paired $t$-test $p{=}0.0008$, permutation test $p{<}0.001$ (bootstrap 95\% CI for per-trace BA: $[0.575, 0.744]$). The position baseline achieves higher balanced accuracy (0.832 vs.\ HS 0.796), and HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are not statistically significant at $n{=}19$.
762	
763	
764	\section{Hyperparameter Robustness}
765	\label{app:hyperparameter_robustness}
766	
767	The joint search space for layer (${\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.
768	
769	\paragraph{Threshold-dependent metrics converge to a deep-layer band.}
770	Despite the large search space, three of four threshold-dependent metrics (precision, inverse FPR, additive composite) independently select L63 (98\% depth) for both 32B models (\cref{tab:layer_selection}). A joint (layer, $W$) grid search over 192 configurations confirms that L63 is near-optimal for QwQ-32B at recommended windows (\cref{tab:joint_layer_w}). For R1-32B, layers L55--L63 at $W{=}1$ form a robust band where all 3/3 metrics pass Holm-Bonferroni (\cref{app:layer_sweep}). The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.
771	
772	\paragraph{BA-optimal layer instability is the finding, not a confound.}
773	Five-fold cross-validation on 32B validation sets reveals that balanced-accuracy-optimal layers are highly unstable across folds (\cref{tab:fold_ba_layers}). This instability is not a limitation of the study but the central methodological finding: BA-layer selection is sensitive to data composition, and conclusions drawn from any single BA-optimal layer are unreliable. Despite per-fold instability, mean BA across folds peaks near L47--L50 for both models, consistent with the LOO-CV dominant layers (\cref{app:layer_sweep}). The HS advantage holds at both BA-optimal and precision-optimal layers regardless of depth (14/16 per-model tests pass HB; \cref{tab:ba_layer_comparison}).
774	
775	\begin{table}[h]
776	\centering
777	\small
778	\caption{BA-optimal layer per fold (5-fold CV, 32B models). Per-fold selections span 24 layers, but mean-BA landscape peaks are stable.}
779	\label{tab:fold_ba_layers}
780	\begin{tabular}{lccccccc}
781	\toprule
782	\textbf{Model} & \textbf{F1} & \textbf{F2} & \textbf{F3} & \textbf{F4} & \textbf{F5} & \textbf{Spread} & \textbf{Mean-BA best} \\
783	\midrule
784	QwQ-32B & L63 & L51 & L39 & L44 & L44 & 24 layers & L50 \\
785	R1-32B & L53 & L45 & L40 & L63 & L39 & 24 layers & L47 \\
786	\bottomrule
787	\end{tabular}
788	\end{table}
789	
790	\paragraph{Bootstrap CIs quantify statistical uncertainty.}
791	For the most fragile result (R1-8B FPR), bias-corrected accelerated (BCa) bootstrap yields a 95\% CI of [0.006, 0.159] ($p{=}0.033$), with 12\% leave-one-out instability (\cref{app:multi_seed}). The CI excludes zero, confirming significance despite seed fragility. CP annotation perturbation (\cref{tab:cp_perturbation}) further shows that $\pm 2$-step label noise changes BA by ${<}2.5$pp, so annotation uncertainty does not compound with hyperparameter selection.
792	
793	
794	\section{Multi-Seed Stability}
795	\label{app:multi_seed}
796	
797	\cref{tab:multi_seed} reports LR probe performance across 5 random seeds at each model's corrected layer and optimal $W$.
798	
799	\begin{table}[h]
800	\centering
801	\small
802	\caption{LR probe stability across 5 random seeds (corrected layers, optimal $W$). 7--8B models are stable; R1-32B shows high variance due to small sample ($n{=}20$).}
803	\label{tab:multi_seed}
804	\begin{tabular}{lccc}
805	\toprule
806	\textbf{Model} & \textbf{Precision} & \textbf{Bal.\ Acc} & \textbf{FPR} \\
807	\midrule
808	R1-8B & $0.590 \pm 0.072$ & $0.756 \pm 0.028$ & $0.154 \pm 0.026$ \\
809	OT-7B & $0.421 \pm 0.034$ & $0.633 \pm 0.023$ & $0.157 \pm 0.021$ \\
810	QwQ-32B & $0.651 \pm 0.099$ & $0.731 \pm 0.028$ & $0.133 \pm 0.032$ \\
811	R1-32B & $0.594 \pm 0.128$ & $0.692 \pm 0.056$ & $0.207 \pm 0.145$ \\
812	\bottomrule
813	\end{tabular}
814	\end{table}
815	
816	R1-32B's high FPR variance (std $= 0.145$) reflects a single outlier seed (FPR $= 0.48$), amplified by the small test set ($n{=}20$). Note that R1-32B's absolute precision std (12.8pp) differs markedly from its paired $\Delta$Prec std (2.0pp): HS and text precision covary across seeds.
817	
818	\paragraph{5-seed Holm-Bonferroni pass rates.} \cref{tab:seed_hb} reports HB pass rates per model across 5 seeds. Overall, 18/20 (90\%) model-seed combinations pass full HB (3/3 metrics).
819	
820	\begin{table}[h]
821	\centering
822	\small
823	\caption{5-seed HB pass rates (3/3 metrics per seed). R1-8B failures are FPR-specific.}
824	\label{tab:seed_hb}
825	\begin{tabular}{lccc}
826	\toprule
827	\textbf{Model} & \textbf{HB Pass} & \textbf{Mean $\Delta$Prec $\pm$ std} & \textbf{Note} \\
828	\midrule
829	OT-7B & 5/5 & $+20.9 \pm 1.3$pp & Cleanest evidence \\
830	R1-32B & 5/5 & $+13.7 \pm 2.0$pp & Position-mediated \\
831	QwQ-32B & 5/5 & $+19.9 \pm 2.5$pp & Robust \\
832	R1-8B & 3/5 & $+14.6 \pm 4.5$pp & FPR seed-fragile \\
833	\bottomrule
834	\end{tabular}
835	\end{table}
836	
837	\paragraph{R1-8B FPR per-seed breakdown.} \cref{tab:r18b_fpr_seeds} reports per-seed HS vs.\ text FPR comparisons for R1-8B. The HS advantage is directionally consistent (5/5 seeds), with 2/5 reaching $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds ($\alpha{=}0.01$), 1/5 remains significant. Text FPR is highly stable (std $= 0.007$) while HS FPR is split-sensitive (std $= 0.040$), which explains why the canonical-split FPR advantage ($-7.4$pp) does not generalize robustly across seeds.
838	
839	\begin{table}[h]
840	\centering
841	\small
842	\caption{R1-8B FPR per-seed comparison (L14, $W{=}15$; main text \cref{tab:hs_vs_text} reports $W{=}3$ after 5-seed validation). Direction is consistent (5/5 HS $\leq$ Text); 2/5 reach $p{<}0.05$ uncorrected, 1/5 after Bonferroni correction (5 seeds, $\alpha{=}0.01$).}
843	\label{tab:r18b_fpr_seeds}
844	\begin{tabular}{ccccc}
845	\toprule
846	\textbf{Seed} & \textbf{HS FPR} & \textbf{Text FPR} & $\Delta$\textbf{FPR} & $p$ \\
847	\midrule
848	0 & 0.161 & 0.165 & $-$0.004 & 0.440 \\
849	1 & 0.061 & 0.166 & $-$0.105 & ${<}0.001$ \\
850	2 & 0.123 & 0.176 & $-$0.053 & 0.093 \\
851	3 & 0.148 & 0.167 & $-$0.018 & 0.293 \\
852	4 & 0.100 & 0.176 & $-$0.076 & 0.021 \\
853	\midrule
854	mean$\pm$std & $0.119 \pm 0.040$ & $0.170 \pm 0.007$ & $-$0.051 & -- \\
855	\bottomrule
856	\end{tabular}
857	\end{table}
858	
859	\paragraph{R1-8B per-metric HB pass rates.} \cref{tab:r18b_metric_hb} reports Holm-Bonferroni pass rates per metric across 5 seeds for R1-8B, the model classified as ``moderate'' evidence due to FPR instability.
860	
861	\begin{table}[h]
862	\centering
863	\small
864	\caption{R1-8B per-metric$\times$seed HB pass rates. Precision is robust (5/5); FPR is fragile (3/5). FPR std across seeds is 0.040 vs.\ text FPR std 0.007, consistent with a proportion near boundary (${\sim}$12\%) amplified at $n{=}43$.}
865	\label{tab:r18b_metric_hb}
866	\begin{tabular}{lccc}
867	\toprule
868	\textbf{Seed} & $\Delta$\textbf{Prec HB} & $\Delta$\textbf{BA HB} & $\Delta$\textbf{FPR HB} \\
869	\midrule
870	0 & \checkmark & \checkmark & $\times$ \\
871	1 & \checkmark & \checkmark & \checkmark \\
872	2 & \checkmark & \checkmark & $\times$ \\
873	3 & \checkmark & \checkmark & \checkmark \\
874	4 & \checkmark & \checkmark & \checkmark \\
875	\midrule
876	Pass rate & 5/5 & 5/5 & 3/5 \\
877	\bottomrule
878	\end{tabular}
879	\end{table}
880	
881	The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17\% (std${=}0.7$pp) while HS FPR ranges from 6.1\% to 16.1\% (std${=}4.0$pp). Seeds where HS FPR happens to be high ($>$14\%) lose significance because the gap against text narrows below the detection threshold at $n{=}43$. This instability is metric-specific and does not affect the precision or balanced accuracy advantage, which passes all 5 seeds.
882	
883	\paragraph{R1-32B per-seed breakdown.} \cref{tab:r132b_seeds} reports the full per-seed breakdown for R1-32B. Seed 0 is an outlier (FPR $= 0.483$), driven by test-set trace allocation at $n{=}20$. Excluding seed 0, FPR std drops from 0.145 to 0.046.
884	
885	\begin{table}[h]
886	\centering
887	\small
888	\caption{R1-32B per-seed performance (L63, $W{=}1$). Seed 0 is an outlier driven by test-set trace allocation.}
889	\label{tab:r132b_seeds}
890	\begin{tabular}{cccc}
891	\toprule
892	\textbf{Seed} & \textbf{Precision} & \textbf{Bal.\ Acc} & \textbf{FPR} \\
893	\midrule
894	0 & 0.441 & 0.594 & 0.483 \\
895	1 & 0.750 & 0.748 & 0.109 \\
896	2 & 0.685 & 0.670 & 0.111 \\
897	3 & 0.652 & 0.733 & 0.111 \\
898	4 & 0.444 & 0.715 & 0.221 \\
899	\midrule
900	mean$\pm$std & $0.594 \pm 0.128$ & $0.692 \pm 0.056$ & $0.207 \pm 0.145$ \\
901	\bottomrule
902	\end{tabular}
903	\end{table}
904	
905	
906	\section{BA-Layer Modality Comparison}
907	\label{tab:ba_layer_comparison}
908	
909	To address the concern that threshold-dependent layer selection may circularly favor HS probes, we repeat the modality comparison at layers selected by pure balanced accuracy, a threshold-free metric (\cref{tab:ba_layer_results}). BA-optimal layers vary widely across models (7--98\% depth), itself demonstrating that layer selection is a consequential methodological choice. The HS advantage is significant at whichever layer BA selects (14/16 per-model HB, two FPR failures from underpowered 32B test sets $n{\leq}20$).
910	
911	\begin{table}[h]
912	\centering
913	\small
914	\caption{HS vs.\ text at BA-selected layers (60/20/20 split, same as main results). 14/16 per-model tests pass Holm-Bonferroni ($\alpha{=}0.05$); two FPR failures from underpowered 32B sets. BA-L: layer selected by pure balanced accuracy. Depth varies from 7\% to 98\%.}
915	\label{tab:ba_layer_results}
916	\setlength{\tabcolsep}{3pt}
917	\begin{tabular}{lccccc}
918	\toprule
919	\textbf{Model} & \textbf{BA-L} & $\Delta$\textbf{Prec} & $\Delta$\textbf{BA} & $\Delta$\textbf{FPR} & $\Delta$\textbf{AUROC} \\
920	\midrule
921	R1-8B & L17 & +18.6 ({<}.001) & +8.4 (.006) & $-$7.0 (.043) & +12.1 (.009) \\
922	OT-7B & L2 & +18.5 ({<}.001) & +8.0 (.006) & $-$13.3 ({<}.001) & +12.8 (.003) \\
923	QwQ-32B$^\dagger$ & L63 & +18.1 (.001) & +13.5 ({<}.001) & $-$6.4 (.088) & +15.1 (.001) \\
924	R1-32B$^\dagger$ & L46 & +12.8 (.014) & +17.6 ({<}.001) & $-$12.2 (.083) & +15.1 (.009) \\
925	\bottomrule
926	\end{tabular}
927	\begin{flushleft}
928	\scriptsize Values: difference in pp ($p$-value, bootstrap, 10{,}000 resamples). $\dagger$\,Sample-limited ($n \leq 20$).
929	\end{flushleft}
930	\end{table}
931	
932	Of 16 per-model tests (4 models $\times$ 4 metrics), 14 pass Holm-Bonferroni correction. The precision gains (+12.8 to +18.6pp) are comparable to those at threshold-dependent layers (+15.4 to +21.9pp; \cref{tab:hs_vs_text}), confirming that the HS advantage is robust to the choice of layer selection criterion. The two failures are both FPR at 32B: R1-32B ($p{=}0.083$) and QwQ-32B ($p{=}0.088$), consistent with the underpowered test sets ($n{\leq}20$) noted throughout. BA-optimal depths span 7\% (OT-7B L2) to 98\% (QwQ-32B L63), in contrast to threshold-dependent layers that consistently select deep layers (94--98\%). That BA selection produces such depth variation while preserving significant HS advantage reinforces the core methodological finding: the advantage is genuine rather than an artifact of any particular layer selection criterion.
933	
934	
935	\section{Post-Hoc Power Analysis}
936	\label{app:power_analysis}
937	
938	We compute post-hoc minimum detectable effects (MDEs) at 80\% power for each model's test set to contextualize non-significant results, particularly at 32B scale where sample sizes are small (\cref{tab:power_analysis}).
939	
940	\begin{table}[h]
941	\centering
942	\small
943	\caption{Post-hoc power analysis. MDE: minimum detectable effect (balanced accuracy, pp) at 80\% power given each model's test-set size and observed variance. Effects smaller than the MDE cannot be reliably detected.}
944	\label{tab:power_analysis}
945	\begin{tabular}{lccc}
946	\toprule
947	\textbf{Model} & $n_{\text{test}}$ & \textbf{Obs.\ std (BA)} & \textbf{MDE (80\%)} \\
948	\midrule
949	R1-8B & 43 & 0.028 & 4.2pp \\
950	OT-7B & 47 & 0.023 & 3.3pp \\
951	QwQ-32B$^\dagger$ & 19 & 0.028 & 8.6pp \\
952	R1-32B$^\dagger$ & 20 & 0.056 & 9.5pp \\
953	\bottomrule
954	\end{tabular}
955	\begin{flushleft}
956	\scriptsize $\dagger$\,Sample-limited. MDE computed from 5-seed observed standard deviation via two-sided paired $t$-test formula.
957	\end{flushleft}
958	\end{table}
959	
960	At 32B scale, the MDE is 8.6--9.5pp, meaning effects below this magnitude cannot be reliably distinguished from noise. R1-32B's residualized HS-text gap (+1.9pp) falls well below the MDE (9.5pp), so the non-significant result (\cref{app:position_residual}) is consistent with either a true null or an underpowered test. The 7--8B MDEs (3.3--4.2pp) are substantially lower, explaining why smaller effects reach significance at these scales.
961	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "f31041a1-6437-4749-be58-4e0c33037bf8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
      "content": "\\section{Detection Threshold ($K$) Ablation}\n\\label{app:k_ablation}\n\nThe consecutive-crossings threshold $K$ controls the trade-off between detection coverage and false positive rate. We evaluate $K \\in \\{1, 3, 5, 7, 10\\}$ at $W{=}1$ on all models using HS probes at corrected layers (\\cref{tab:k_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Detection threshold ablation ($W{=}1$, HS probes at corrected layers). Coverage: fraction of jailbreak traces with $\\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\\geq K$ consecutive false alarms.}\n\\label{tab:k_ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Coverage}} & & \\multicolumn{4}{c}{\\textbf{Safe FPR}} \\\\\n\\cmidrule{2-5} \\cmidrule{7-10}\n$K$ & R1-8B & OT-7B & QwQ & R1-32B & & R1-8B & OT-7B & QwQ & R1-32B \\\\\n\\midrule\n1  & 1.00 & 1.00 & 1.00 & 1.00 & & 1.00 & 0.92 & 1.00 & 0.99 \\\\\n3  & 0.74 & 0.79 & 0.95 & 0.90 & & 0.81 & 0.41 & 0.78 & 0.78 \\\\\n5  & 0.47 & 0.51 & 0.79 & 0.65 & & 0.63 & 0.19 & 0.65 & 0.47 \\\\\n7  & 0.35 & 0.30 & 0.58 & 0.45 & & 0.39 & 0.16 & 0.35 & 0.31 \\\\\n10 & 0.14 & 0.21 & 0.32 & 0.35 & & 0.22 & 0.08 & 0.25 & 0.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$K{=}1$ yields perfect coverage but near-perfect safe FPR (0.92--1.00), offering no discrimination. $K{=}5$ is empirically selected as a middle-ground tradeoff: average coverage 0.60 with average safe FPR 0.48 across models. OT-7B benefits most from increasing $K$, reaching 0.19 safe FPR at $K{=}5$ (vs.\\ 0.92 at $K{=}1$) while retaining 51\\% coverage. Higher $K$ values ($\\geq$7) reduce safe FPR further but at steep coverage cost. $K{=}5$ vs.\\ $K{=}7$ is the key decision: $K{=}7$ reduces mean safe FPR from 0.48 to 0.30 but drops mean coverage from 0.60 to 0.42.\n\n$K$ was set as a design pre-selection before evaluation, not tuned on the validation set; all main-text results use $K{=}5$ without per-model optimization. The $K \\times W$ interaction is not fully explored: this ablation uses $W{=}1$ to isolate $K$'s effect, and the joint $K \\times W$ surface remains a limitation. At optimal $W$, coverage at $K{=}5$ improves (e.g., R1-8B: 0.47 at $W{=}1$ vs.\\ 0.60 at $W{=}15$).\n\n\n\\section{Decision Threshold Sensitivity}\n\\label{app:threshold_sensitivity}\n\nWe evaluate whether the HS advantage depends on the logistic regression decision threshold by sweeping $\\tau \\in \\{0.3, 0.4, 0.5, 0.6, 0.7\\}$ for both 32B models at their corrected layers. Results below were conducted at L60 under the 70/30 protocol; main-text results use L63 under 60/20/20. QwQ-32B (L60, $W{=}3$) HS balanced accuracy varies by only 0.53pp across all thresholds, with $\\Delta$(HS$-$Text) stable at +8.5 to +9.3pp. \\cref{tab:threshold_r132b} reports R1-32B results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}\n\\label{tab:threshold_r132b}\n\\begin{tabular}{ccccccc}\n\\toprule\n$\\tau$ & HS BA & $\\Delta$BA & HS Prec & $\\Delta$Prec & HS FPR & $\\Delta$FPR \\\\\n\\midrule\n0.3 & 0.752 & +0.126 & 0.583 & +0.126 & 0.295 & $-$0.106 \\\\\n0.4 & 0.746 & +0.116 & 0.586 & +0.120 & 0.281 & $-$0.092 \\\\\n\\textbf{0.5} & \\textbf{0.742} & \\textbf{+0.109} & \\textbf{0.588} & \\textbf{+0.113} & \\textbf{0.273} & $\\mathbf{-}$\\textbf{0.078} \\\\\n0.6 & 0.741 & +0.112 & 0.599 & +0.119 & 0.254 & $-$0.072 \\\\\n0.7 & 0.743 & +0.126 & 0.617 & +0.143 & 0.228 & $-$0.084 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nR1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\\Delta$BA $= +0.109$ to $+0.126$, $\\Delta$Prec $= +0.113$ to $+0.143$, $\\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\tau{=}0.5$.\n\n\n\\section{M002 Bug Disclosure}\n\\label{app:bug}\n\nWe disclose a bug discovered during development that affected intermediate results for QwQ-32B.\n\n\\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).\n\n\\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the biased composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\\cref{sec:layer-results}) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage$^\\dagger$ at corrected deep layers, from strong (OT-7B) to qualified (R1-32B) (\\cref{tab:hs_vs_text}).\n\n\\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection correction (\\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and biased layer selection. Both are fully resolved in the final analysis.\n\n\\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. Code and data will be released upon publication.\n\n\\section{Adaptive Two-Stage Detection}\n\\label{app:two_stage}\n\nWe explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.\n\nWe merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\\text{screen}} \\in \\{1, 3, 5\\}$, $W_{\\text{confirm}} \\in \\{10, 15, 20, 25\\}$, and $k \\in \\{1, 3, 5\\}$ on these R1-8B traces. \\cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\\text{screen}}{=}3$, $W_{\\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\\% precision at 76.9\\% coverage, compared to 70.9\\% precision at 76.9\\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\\% precision at 38.5\\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/pareto_two_stage.pdf}\n\\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\\text{screen}}{=}3$, $W_{\\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}\n\\label{fig:pareto_two_stage}\n\\end{figure}\n\nThe marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.\n\n\n\\section{Temporal Ablation Details}\n\\label{app:temporal_details}\n\nFull per-model temporal ablations are reported in \\cref{tab:window_full} (\\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$) with FPR halving (9.65\\% to 4.83\\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.\n\n\\section{Negative Results Details}\n\\label{app:negative_details}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}\n\\toprule\n\\textbf{Method} & \\textbf{Result} & \\textbf{Limitation} \\\\\n\\midrule\nBOCPD & 0\\% det.\\ on 3/4 models & Commitment gradual \\\\\nCUSUM & $<$ threshold, all models & Same as BOCPD \\\\\nMahalanobis & $\\Delta d \\approx 0$ & Signal in minor PCs \\\\\nRepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent \\\\\nMLP & 3/4 worse than LR & Overfitting \\\\\nCCS & No gain over supervised$^b$ & Alignment mismatch \\\\\nTransfer & Best 59.5\\% (PCA)$^c$ & Model-specific repr. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seven alternative approaches. $^a$\\,RepE QwQ approaches supervised bal\\_acc but precision is 0.512 vs.\\ LR 0.700. $^b$\\,Semi-supervised (requires CP labels). $^c$\\,Best direct transfer 67.3\\% but 1\\% crossing rate.}\n\\label{tab:negative}\n\\end{table}\n\n\\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\\% detection rate across all tested configurations ($\\lambda \\in \\{5, 10, 50, 100, 200\\}$). Only R1-8B produces non-zero detection (best: $\\lambda{=}10$, 93\\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\\cref{app:bocpd_config}).\n\n\\paragraph{Mahalanobis distance.} Following TrajGuard~\\cite{trajguard}, Mahalanobis distance from the pre-CP centroid produces $\\Delta d \\approx 0$ between pre-CP and post-CP steps. The discriminative signal resides in minor PCA components (explaining $<$5\\% of total variance) rather than the principal directions that dominate the distance computation.\n\n\\paragraph{RepE.} Mean-difference directions~\\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\\ LR 0.700) and FPR (0.309 vs.\\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.\n\n\\paragraph{MLP probes.} Two-layer MLPs ($d \\rightarrow 128 \\rightarrow 1$, ReLU) underperform logistic regression on 3/4 models. The commitment boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small training sets.\n\n\\paragraph{CCS.} Contrast-Consistent Search~\\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.\n\n\\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\\rightarrow$ QwQ-32B at 59.5\\% (PCA-2048). Best direct: QwQ-32B $\\rightarrow$ R1-32B at 67.3\\% but 1\\% crossing rate. Implementation details in \\cref{app:transfer_details}.\n\n\\section{Cross-Model Transfer Implementation Details}\n\\label{app:transfer_details}\n\nWe test whether safety probes transfer across models by projecting hidden states into a shared dimensionality space and applying cross-model classification.\n\n\\paragraph{Method.} For each source-target model pair, we apply PCA independently to each model's hidden states, reducing to a shared dimensionality $d \\in \\{512, 1024, 2048\\}$. PCA is fitted on the full dataset (including test traces) for each model separately, a setting favorable to transfer since it maximizes the quality of the projection. A logistic regression classifier (C=1.0, class\\_weight=`balanced', max\\_iter=2000, random\\_state=42) trained on the source model's PCA-projected training data is then applied directly to the target model's PCA-projected test data. No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied; PCA serves as a standard linear dimensionality reduction baseline.\n\n\\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.\n\n\\paragraph{Results.} All 17 transfer configurations (5 directional pairs $\\times$ 3 PCA dimensionalities, plus 2 direct transfers for same-dimension pairs) fail to produce practically useful transfer. The best PCA result is R1-8B $\\rightarrow$ QwQ-32B at 59.5\\% balanced accuracy (PCA-2048). The best direct transfer (QwQ-32B $\\rightarrow$ R1-32B) reaches 67.3\\% balanced accuracy, which exceeds the within-model baseline of 65.2\\%. However, this transfer direction achieves only 1\\% crossing rate, meaning the transferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. The complete failure under maximally favorable conditions (PCA fitted on full data, no train/test separation for projection) strengthens the conclusion that safety commitment is encoded in model-specific geometric configurations. PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.\n\n\n\\section{Encoder Robustness Analysis}\n\\label{app:encoder_robustness}\n\nTo test whether the HS advantage over text probes depends on the specific text encoder, we replace all-MiniLM-L6-v2 (384d) with BGE-large-en-v1.5 (1024d), a 2.7$\\times$ higher-dimensional encoder with stronger semantic representations. \\cref{tab:encoder_robustness} reports precision comparisons at each model's corrected layer; \\cref{fig:forest_precision} provides a visual summary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS vs.\\ BGE-large (1024d) text probe precision. $\\Delta$: HS minus BGE-large. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\\alpha{=}0.05$).}\n\\label{tab:encoder_robustness}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{HS Prec} & \\textbf{BGE Prec} & $\\Delta$ & \\textbf{95\\% CI} & $p$ & \\textbf{HB} \\\\\n\\midrule\nR1-8B & 0.497 & 0.436 & +0.058 & [$-$0.07, +0.20] & 0.185 & No \\\\\nOT-7B & 0.446 & 0.263 & +0.181 & [+0.08, +0.29] & ${<}0.001$ & Yes \\\\\nR1-32B & 0.588 & 0.475 & +0.117 & [$-$0.00, +0.24] & 0.042 & No \\\\\nQwQ-32B & 0.545 & 0.454 & +0.094 & [$-$0.07, +0.28] & 0.132 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe HS precision advantage is directionally consistent across all four models (positive $\\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \\cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.\n\n\\paragraph{Balanced accuracy and FPR.} \\cref{tab:bge_ba_fpr} reports BGE-large comparisons on balanced accuracy and FPR. HS balanced accuracy advantage is directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni. FPR advantage is significant only for OT-7B. R1-8B shows an adverse FPR direction: HS FPR is 1.2pp higher (worse) than BGE ($p{=}0.564$), the only model where HS does not improve over the stronger encoder on this metric.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS vs.\\ BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction (4 tests per metric, $\\alpha{=}0.05$).}\n\\label{tab:bge_ba_fpr}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & $\\Delta$\\textbf{BA} & $p$ (BA) & \\textbf{HB} & $\\Delta$\\textbf{FPR} & $p$ (FPR) & \\textbf{HB} \\\\\n\\midrule\nR1-8B & +8.4 & 0.029 & No & $-$1.2$^\\dagger$ & 0.564 & No \\\\\nOT-7B & +10.8 & 0.002 & Yes & +10.5 & ${<}0.001$ & Yes \\\\\nQwQ-32B & +9.3 & 0.067 & No & +2.7 & 0.368 & No \\\\\nR1-32B & +10.9 & 0.008 & Yes & +7.8 & 0.165 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\scriptsize $^\\dagger$Adverse direction: HS FPR higher (worse) than BGE.\n\\end{flushleft}\n\\end{table}\n\n\n\\section{Random Projection Baseline}\n\\label{app:random_projection}\n\nPCA capacity matching (\\cref{app:encoder_robustness}) preserves 79--92\\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\\cref{tab:random_projection}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Random projection (RP, 384d) vs.\\ text (384d MiniLM). All $p < 0.001$ (1{,}000 bootstrap resamples). R1-8B uses $W{=}15$ (Table~3: $W{=}3$); QwQ-32B evaluated at L60 (Table~3: L63). 60/20/20 split.}\n\\label{tab:random_projection}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{RP Prec} & \\textbf{Text Prec} & $\\Delta$\\textbf{Prec} & $\\Delta$\\textbf{BA} \\\\\n\\midrule\nR1-8B & .621 & .416 & +.205 & +.140 \\\\\nOT-7B & .371 & .244 & +.127 & +.128 \\\\\nQwQ-32B & .563 & .391 & +.172 & +.132 \\\\\nR1-32B & .524 & .441 & +.083 & +.085 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four models retain significant HS advantage under random projection ($\\Delta$Prec +8.3 to +20.5pp), with cross-seed standard deviations below 1.7pp. RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. This weakens a pure capacity explanation: even a structure-destroying projection preserves the HS advantage, suggesting the safety signal is broadly distributed across hidden-state dimensions rather than concentrated in top principal components.\n\n\n\\section{LLM-Based Text Encoder Comparison}\n\\label{app:e5_mistral}\n\nTo test whether an LLM-based text encoder closes the HS advantage gap, we encode each reasoning step with E5-Mistral-7B-Instruct~\\citep{wang2024e5mistral} (4096d, reduced to 384d via PCA to match the MiniLM dimensionality). \\cref{tab:e5_mistral} reports precision comparisons against HS probes at corrected layers.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS vs.\\ E5-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, $\\alpha{=}0.05$). MiniLM precision from \\cref{tab:hs_vs_text} for reference. 60/20/20 split.}\n\\label{tab:e5_mistral}\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & $W$ & \\textbf{HS} & \\textbf{E5} & \\textbf{MiniLM} & $\\Delta$(HS$-$E5) & $p$ & \\textbf{HB} \\\\\n\\midrule\nR1-8B & L14 & 3 & .630 & .480 & .416 & +15.0 & 0.001 & \\checkmark \\\\\nOT-7B & L16 & 3 & .446 & .321 & .244 & +12.5 & 0.009 & \\checkmark \\\\\nR1-32B & L63 & 1 & .588 & .506 & .441 & +8.2 & 0.235 & \\\\\nQwQ-32B & L63 & 5 & .515 & .447 & .391 & +6.8 & 0.368 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe HS advantage partially survives against the LLM encoder: 2/4 models (both 7--8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (22M params, 384d): 4/4 HB; E5-Mistral (7B, PCA 384d): 2/4 HB; BGE-large (335M, 1024d): 1/4 HB (\\cref{app:encoder_robustness}). E5 precision consistently falls between MiniLM and HS across all models, confirming that encoder quality progressively narrows the gap. PCA to 384d discards information from the 4096d E5 representation; the comparison controls dimensionality but not representation quality, so the true E5 advantage may be larger than reported here.\n\n\n\\section{Position-Residualized Probing}\n\\label{app:position_residual}\n\nTo quantify non-positional safety signal, we regress out the normalized position $t/T$ from each hidden-state (or text-embedding) vector before training the logistic regression probe. \\cref{tab:position_residual} summarizes results across all models at their optimal $W$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Model} & $W$ & \\textbf{HS BA} & \\textbf{Resid.\\ HS BA} & \\textbf{Drop} & \\textbf{Resid.\\ Text BA} \\\\\n\\midrule\nR1-8B & 15 & 0.834 & 0.669 & 16.5pp & 0.605 \\\\\nR1-8B & 3 & 0.813 & 0.571 & 24.3pp & 0.534 \\\\\nOT-7B & 3 & 0.732 & 0.609 & 12.3pp & 0.540 \\\\\nQwQ-32B & 3 & 0.796 & 0.619 & 17.7pp & 0.582 \\\\\nR1-32B & 1 & 0.756 & 0.552 & 20.4pp & 0.532 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Position-residualized probe balanced accuracy. All residualized HS probes are above chance ($p{<}0.001$). 3/4 models retain significant non-positional HS advantage over text (gap +3.7 to +6.9pp, HB corrected); R1-32B is the exception (+1.9pp, $p{=}0.914$).}\n\\label{tab:position_residual}\n\\end{table}\n\nPosition accounts for 9--20pp of balanced accuracy depending on model and window size (R1-32B's 20.4pp drop at $W{=}1$ reflects the absence of temporal context), and all models retain non-positional signal above chance ($p{<}0.001$). Three of four models retain significant non-positional HS advantage over text after residualization (OT-7B +6.9pp, R1-8B +6.4pp at $W{=}15$, QwQ-32B +3.7pp; all HB corrected). R1-32B is the exception: residualized HS-text gap is +1.9pp ($p{=}0.914$), indicating its HS advantage is position-mediated. Larger temporal windows reduce position dependence: R1-8B drops 24.3pp at $W{=}3$ but only 16.5pp at $W{=}15$.\n\nFor QwQ-32B specifically, three complementary significance tests confirm the residualized probe performs above chance: Wilcoxon signed-rank $p{=}0.0024$, paired $t$-test $p{=}0.0008$, permutation test $p{<}0.001$ (bootstrap 95\\% CI for per-trace BA: $[0.575, 0.744]$). The position baseline achieves higher balanced accuracy (0.832 vs.\\ HS 0.796), and HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are not statistically significant at $n{=}19$.\n\n\n\\section{Hyperparameter Robustness}\n\\label{app:hyperparameter_robustness}\n\nThe joint search space for layer (${\\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.\n\n\\paragraph{Threshold-dependent metrics converge to a deep-layer band.}\nDespite the large search space, three of four threshold-dependent metrics (precision, inverse FPR, additive composite) independently select L63 (98\\% depth) for both 32B models (\\cref{tab:layer_selection}). A joint (layer, $W$) grid search over 192 configurations confirms that L63 is near-optimal for QwQ-32B at recommended windows (\\cref{tab:joint_layer_w}). For R1-32B, layers L55--L63 at $W{=}1$ form a robust band where all 3/3 metrics pass Holm-Bonferroni (\\cref{app:layer_sweep}). The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\n\n\\paragraph{BA-optimal layer instability is the finding, not a confound.}\nFive-fold cross-validation on 32B validation sets reveals that balanced-accuracy-optimal layers are highly unstable across folds (\\cref{tab:fold_ba_layers}). This instability is not a limitation of the study but the central methodological finding: BA-layer selection is sensitive to data composition, and conclusions drawn from any single BA-optimal layer are unreliable. Despite per-fold instability, mean BA across folds peaks near L47--L50 for both models, consistent with the LOO-CV dominant layers (\\cref{app:layer_sweep}). The HS advantage holds at both BA-optimal and precision-optimal layers regardless of depth (14/16 per-model tests pass HB; \\cref{tab:ba_layer_comparison}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BA-optimal layer per fold (5-fold CV, 32B models). Per-fold selections span 24 layers, but mean-BA landscape peaks are stable.}\n\\label{tab:fold_ba_layers}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{F1} & \\textbf{F2} & \\textbf{F3} & \\textbf{F4} & \\textbf{F5} & \\textbf{Spread} & \\textbf{Mean-BA best} \\\\\n\\midrule\nQwQ-32B & L63 & L51 & L39 & L44 & L44 & 24 layers & L50 \\\\\nR1-32B & L53 & L45 & L40 & L63 & L39 & 24 layers & L47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Bootstrap CIs quantify statistical uncertainty.}\nFor the most fragile result (R1-8B FPR), bias-corrected accelerated (BCa) bootstrap yields a 95\\% CI of [0.006, 0.159] ($p{=}0.033$), with 12\\% leave-one-out instability (\\cref{app:multi_seed}). The CI excludes zero, confirming significance despite seed fragility. CP annotation perturbation (\\cref{tab:cp_perturbation}) further shows that $\\pm 2$-step label noise changes BA by ${<}2.5$pp, so annotation uncertainty does not compound with hyperparameter selection.\n\n\n\\section{Multi-Seed Stability}\n\\label{app:multi_seed}\n\n\\cref{tab:multi_seed} reports LR probe performance across 5 random seeds at each model's corrected layer and optimal $W$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LR probe stability across 5 random seeds (corrected layers, optimal $W$). 7--8B models are stable; R1-32B shows high variance due to small sample ($n{=}20$).}\n\\label{tab:multi_seed}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Precision} & \\textbf{Bal.\\ Acc} & \\textbf{FPR} \\\\\n\\midrule\nR1-8B & $0.590 \\pm 0.072$ & $0.756 \\pm 0.028$ & $0.154 \\pm 0.026$ \\\\\nOT-7B & $0.421 \\pm 0.034$ & $0.633 \\pm 0.023$ & $0.157 \\pm 0.021$ \\\\\nQwQ-32B & $0.651 \\pm 0.099$ & $0.731 \\pm 0.028$ & $0.133 \\pm 0.032$ \\\\\nR1-32B & $0.594 \\pm 0.128$ & $0.692 \\pm 0.056$ & $0.207 \\pm 0.145$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nR1-32B's high FPR variance (std $= 0.145$) reflects a single outlier seed (FPR $= 0.48$), amplified by the small test set ($n{=}20$). Note that R1-32B's absolute precision std (12.8pp) differs markedly from its paired $\\Delta$Prec std (2.0pp): HS and text precision covary across seeds.\n\n\\paragraph{5-seed Holm-Bonferroni pass rates.} \\cref{tab:seed_hb} reports HB pass rates per model across 5 seeds. Overall, 18/20 (90\\%) model-seed combinations pass full HB (3/3 metrics).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{5-seed HB pass rates (3/3 metrics per seed). R1-8B failures are FPR-specific.}\n\\label{tab:seed_hb}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{HB Pass} & \\textbf{Mean $\\Delta$Prec $\\pm$ std} & \\textbf{Note} \\\\\n\\midrule\nOT-7B & 5/5 & $+20.9 \\pm 1.3$pp & Cleanest evidence \\\\\nR1-32B & 5/5 & $+13.7 \\pm 2.0$pp & Position-mediated \\\\\nQwQ-32B & 5/5 & $+19.9 \\pm 2.5$pp & Robust \\\\\nR1-8B & 3/5 & $+14.6 \\pm 4.5$pp & FPR seed-fragile \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{R1-8B FPR per-seed breakdown.} \\cref{tab:r18b_fpr_seeds} reports per-seed HS vs.\\ text FPR comparisons for R1-8B. The HS advantage is directionally consistent (5/5 seeds), with 2/5 reaching $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds ($\\alpha{=}0.01$), 1/5 remains significant. Text FPR is highly stable (std $= 0.007$) while HS FPR is split-sensitive (std $= 0.040$), which explains why the canonical-split FPR advantage ($-7.4$pp) does not generalize robustly across seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B FPR per-seed comparison (L14, $W{=}15$; main text \\cref{tab:hs_vs_text} reports $W{=}3$ after 5-seed validation). Direction is consistent (5/5 HS $\\leq$ Text); 2/5 reach $p{<}0.05$ uncorrected, 1/5 after Bonferroni correction (5 seeds, $\\alpha{=}0.01$).}\n\\label{tab:r18b_fpr_seeds}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{HS FPR} & \\textbf{Text FPR} & $\\Delta$\\textbf{FPR} & $p$ \\\\\n\\midrule\n0 & 0.161 & 0.165 & $-$0.004 & 0.440 \\\\\n1 & 0.061 & 0.166 & $-$0.105 & ${<}0.001$ \\\\\n2 & 0.123 & 0.176 & $-$0.053 & 0.093 \\\\\n3 & 0.148 & 0.167 & $-$0.018 & 0.293 \\\\\n4 & 0.100 & 0.176 & $-$0.076 & 0.021 \\\\\n\\midrule\nmean$\\pm$std & $0.119 \\pm 0.040$ & $0.170 \\pm 0.007$ & $-$0.051 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{R1-8B per-metric HB pass rates.} \\cref{tab:r18b_metric_hb} reports Holm-Bonferroni pass rates per metric across 5 seeds for R1-8B, the model classified as ``moderate'' evidence due to FPR instability.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B per-metric$\\times$seed HB pass rates. Precision is robust (5/5); FPR is fragile (3/5). FPR std across seeds is 0.040 vs.\\ text FPR std 0.007, consistent with a proportion near boundary (${\\sim}$12\\%) amplified at $n{=}43$.}\n\\label{tab:r18b_metric_hb}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Seed} & $\\Delta$\\textbf{Prec HB} & $\\Delta$\\textbf{BA HB} & $\\Delta$\\textbf{FPR HB} \\\\\n\\midrule\n0 & \\checkmark & \\checkmark & $\\times$ \\\\\n1 & \\checkmark & \\checkmark & \\checkmark \\\\\n2 & \\checkmark & \\checkmark & $\\times$ \\\\\n3 & \\checkmark & \\checkmark & \\checkmark \\\\\n4 & \\checkmark & \\checkmark & \\checkmark \\\\\n\\midrule\nPass rate & 5/5 & 5/5 & 3/5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe FPR instability has a clear source: R1-8B text FPR clusters tightly around 17\\% (std${=}0.7$pp) while HS FPR ranges from 6.1\\% to 16.1\\% (std${=}4.0$pp). Seeds where HS FPR happens to be high ($>$14\\%) lose significance because the gap against text narrows below the detection threshold at $n{=}43$. This instability is metric-specific and does not affect the precision or balanced accuracy advantage, which passes all 5 seeds.\n\n\\paragraph{R1-32B per-seed breakdown.} \\cref{tab:r132b_seeds} reports the full per-seed breakdown for R1-32B. Seed 0 is an outlier (FPR $= 0.483$), driven by test-set trace allocation at $n{=}20$. Excluding seed 0, FPR std drops from 0.145 to 0.046.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-32B per-seed performance (L63, $W{=}1$). Seed 0 is an outlier driven by test-set trace allocation.}\n\\label{tab:r132b_seeds}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Precision} & \\textbf{Bal.\\ Acc} & \\textbf{FPR} \\\\\n\\midrule\n0 & 0.441 & 0.594 & 0.483 \\\\\n1 & 0.750 & 0.748 & 0.109 \\\\\n2 & 0.685 & 0.670 & 0.111 \\\\\n3 & 0.652 & 0.733 & 0.111 \\\\\n4 & 0.444 & 0.715 & 0.221 \\\\\n\\midrule\nmean$\\pm$std & $0.594 \\pm 0.128$ & $0.692 \\pm 0.056$ & $0.207 \\pm 0.145$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{BA-Layer Modality Comparison}\n\\label{tab:ba_layer_comparison}\n\nTo address the concern that threshold-dependent layer selection may circularly favor HS probes, we repeat the modality comparison at layers selected by pure balanced accuracy, a threshold-free metric (\\cref{tab:ba_layer_results}). BA-optimal layers vary widely across models (7--98\\% depth), itself demonstrating that layer selection is a consequential methodological choice. The HS advantage is significant at whichever layer BA selects (14/16 per-model HB, two FPR failures from underpowered 32B test sets $n{\\leq}20$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS vs.\\ text at BA-selected layers (60/20/20 split, same as main results). 14/16 per-model tests pass Holm-Bonferroni ($\\alpha{=}0.05$); two FPR failures from underpowered 32B sets. BA-L: layer selected by pure balanced accuracy. Depth varies from 7\\% to 98\\%.}\n\\label{tab:ba_layer_results}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{BA-L} & $\\Delta$\\textbf{Prec} & $\\Delta$\\textbf{BA} & $\\Delta$\\textbf{FPR} & $\\Delta$\\textbf{AUROC} \\\\\n\\midrule\nR1-8B & L17 & +18.6 ({<}.001) & +8.4 (.006) & $-$7.0 (.043) & +12.1 (.009) \\\\\nOT-7B & L2 & +18.5 ({<}.001) & +8.0 (.006) & $-$13.3 ({<}.001) & +12.8 (.003) \\\\\nQwQ-32B$^\\dagger$ & L63 & +18.1 (.001) & +13.5 ({<}.001) & $-$6.4 (.088) & +15.1 (.001) \\\\\nR1-32B$^\\dagger$ & L46 & +12.8 (.014) & +17.6 ({<}.001) & $-$12.2 (.083) & +15.1 (.009) \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\scriptsize Values: difference in pp ($p$-value, bootstrap, 10{,}000 resamples). $\\dagger$\\,Sample-limited ($n \\leq 20$).\n\\end{flushleft}\n\\end{table}\n\nOf 16 per-model tests (4 models $\\times$ 4 metrics), 14 pass Holm-Bonferroni correction. The precision gains (+12.8 to +18.6pp) are comparable to those at threshold-dependent layers (+15.4 to +21.9pp; \\cref{tab:hs_vs_text}), confirming that the HS advantage is robust to the choice of layer selection criterion. The two failures are both FPR at 32B: R1-32B ($p{=}0.083$) and QwQ-32B ($p{=}0.088$), consistent with the underpowered test sets ($n{\\leq}20$) noted throughout. BA-optimal depths span 7\\% (OT-7B L2) to 98\\% (QwQ-32B L63), in contrast to threshold-dependent layers that consistently select deep layers (94--98\\%). That BA selection produces such depth variation while preserving significant HS advantage reinforces the core methodological finding: the advantage is genuine rather than an artifact of any particular layer selection criterion.\n\n\n\\section{Post-Hoc Power Analysis}\n\\label{app:power_analysis}\n\nWe compute post-hoc minimum detectable effects (MDEs) at 80\\% power for each model's test set to contextualize non-significant results, particularly at 32B scale where sample sizes are small (\\cref{tab:power_analysis}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Post-hoc power analysis. MDE: minimum detectable effect (balanced accuracy, pp) at 80\\% power given each model's test-set size and observed variance. Effects smaller than the MDE cannot be reliably detected.}\n\\label{tab:power_analysis}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & $n_{\\text{test}}$ & \\textbf{Obs.\\ std (BA)} & \\textbf{MDE (80\\%)} \\\\\n\\midrule\nR1-8B & 43 & 0.028 & 4.2pp \\\\\nOT-7B & 47 & 0.023 & 3.3pp \\\\\nQwQ-32B$^\\dagger$ & 19 & 0.028 & 8.6pp \\\\\nR1-32B$^\\dagger$ & 20 & 0.056 & 9.5pp \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\scriptsize $\\dagger$\\,Sample-limited. MDE computed from 5-seed observed standard deviation via two-sided paired $t$-test formula.\n\\end{flushleft}\n\\end{table}\n\nAt 32B scale, the MDE is 8.6--9.5pp, meaning effects below this magnitude cannot be reliably distinguished from noise. R1-32B's residualized HS-text gap (+1.9pp) falls well below the MDE (9.5pp), so the non-significant result (\\cref{app:position_residual}) is consistent with either a true null or an underpowered test. The 7--8B MDEs (3.3--4.2pp) are substantially lower, explaining why smaller effects reach significance at these scales.\n",
      "numLines": 462,
      "startLine": 500,
      "totalLines": 961
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01MiNA1tB7HUbRYw6yeRhnLL`</summary>

```json
{
  "pattern": ", [a-z]+ing (the|a|an|that|this|our|its|their|how|what|which|more|each|all) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "66b8b554-021e-40e5-adf3-9c33d0ddff7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsHWJnKhjjAcwMfKVwLr2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18437,
      "cache_read_input_tokens": 40077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18437
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

_source line 49 · 2026-05-18T22:16:17.858Z_

<details><summary>↩ Tool result · `toolu_01MiNA1tB7HUbRYw6yeRhnLL`</summary>

```text
docs/paper/sections/related_work.tex:16:[Omitted long matching line]
docs/paper/sections/experiments.tex:67:[Omitted long matching line]
docs/paper/sections/discussion.tex:10:[Omitted long matching line]
docs/paper/sections/method.tex:52:[Omitted long matching line]
docs/paper/sections/appendix.tex:53:[Omitted long matching line]
docs/paper/sections/appendix.tex:109:\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
docs/paper/sections/appendix.tex:134:[Omitted long matching line]
docs/paper/sections/appendix.tex:213:\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
docs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
docs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
docs/paper/sections/appendix.tex:298:\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
docs/paper/sections/appendix.tex:300:\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
docs/paper/sections/appendix.tex:368:[Omitted long matching line]
docs/paper/sections/appendix.tex:371:[Omitted long matching line]
docs/paper/sections/appendix.tex:387:\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
docs/paper/sections/appendix.tex:399:[Omitted long matching line]
docs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\tau{=}0.5$.
docs/paper/sections/appendix.tex:562:[Omitted long matching line]
docs/paper/sections/appendix.tex:636:[Omitted long matching line]
docs/paper/sections/appendix.tex:689:PCA capacity matching (\cref{app:encoder_robustness}) preserves 79--92\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\cref{tab:random_projection}).
docs/paper/sections/appendix.tex:708:[Omitted long matching line]
docs/paper/sections/appendix.tex:733:[Omitted long matching line]
docs/paper/sections/appendix.tex:759:[Omitted long matching line]
docs/paper/sections/appendix.tex:767:The joint search space for layer (${\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.
docs/paper/sections/appendix.tex:932:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "df065587-a62d-442a-a14a-5844e118f3a7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:16:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:67:[Omitted long matching line]\ndocs/paper/sections/discussion.tex:10:[Omitted long matching line]\ndocs/paper/sections/method.tex:52:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:53:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:109:\\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}\ndocs/paper/sections/appendix.tex:134:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:213:\\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.\ndocs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.\ndocs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.\ndocs/paper/sections/appendix.tex:298:\\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\\% training portion, we hold out 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\ndocs/paper/sections/appendix.tex:300:\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\ndocs/paper/sections/appendix.tex:368:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:371:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:387:\\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.\ndocs/paper/sections/appendix.tex:399:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\\Delta$BA $= +0.109$ to $+0.126$, $\\Delta$Prec $= +0.113$ to $+0.143$, $\\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\tau{=}0.5$.\ndocs/paper/sections/appendix.tex:562:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:636:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:689:PCA capacity matching (\\cref{app:encoder_robustness}) preserves 79--92\\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\\cref{tab:random_projection}).\ndocs/paper/sections/appendix.tex:708:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:733:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:759:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:767:The joint search space for layer (${\\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.\ndocs/paper/sections/appendix.tex:932:[Omitted long matching line]",
    "numLines": 25
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_01HZUGYmZhemvnsGdsLHPtFf`</summary>

```json
{
  "pattern": "(?i)notably",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "2f6b2d81-7ae2-4141-a1ed-a2958dc08ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsHWJnKhjjAcwMfKVwLr2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18437,
      "cache_read_input_tokens": 40077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18437
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

_source line 51 · 2026-05-18T22:16:19.273Z_

<details><summary>↩ Tool result · `toolu_01HZUGYmZhemvnsGdsLHPtFf`</summary>

```text
docs/paper/sections/appendix.tex:206:\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "83de620b-3b4d-4333-9e25-615c47b58c41",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/appendix.tex:206:\\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\\%), dips at $W{=}10$--$15$, then recovers to 76.2\\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\\% to 61.8\\% precision; 22.76\\% to 16.94\\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Grep · `toolu_01YZNF87NX2rTnRJtkqdHbfw`</summary>

```json
{
  "pattern": "(?i)(Additionally|In addition)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "81a984c4-55fc-4752-b460-d072c70233d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsHWJnKhjjAcwMfKVwLr2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18437,
      "cache_read_input_tokens": 40077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18437
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

_source line 53 · 2026-05-18T22:16:20.264Z_

<details><summary>↩ Tool result · `toolu_01YZNF87NX2rTnRJtkqdHbfw`</summary>

```text
docs/paper/sections/appendix.tex:634:\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "d6257c9f-db46-4d61-80b9-beada44c5f85",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/appendix.tex:634:\\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now let me carefully analyze the -ing phrase matches. The grep returned many lines but they were "omitted long matching line". Let me get the actual content with more context, specifically looking at the -ing phrase patterns to determine which are actually problematic.

Let me also look more carefully at the `-ing` endings. The grep pattern `, [a-z]+ing (the|a|an|...)` will catch many lines. Let me look at specific ones that are likely issues.

Let me search with a more specific pattern for sentence-ending -ing phrases - those that come at the end of a sentence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "e2168119-b45a-4aa4-9dda-1d978af958c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgxa9Ns1NPwReGmivvT1mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16889,
      "cache_read_input_tokens": 58514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16889
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

_source line 55_

Let me get the specific -ing phrase matches with surrounding context, and check for more specific patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "ff8714e8-e50b-48c8-b859-0f30462b53a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgxa9Ns1NPwReGmivvT1mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16889,
      "cache_read_input_tokens": 58514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16889
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

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_01YSLrhmDzymmch9CJsZPJGq`</summary>

```json
{
  "pattern": ", [a-z]+ing (the|a|an|that|this|our|its|their|how|what|which|more|each|all) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "b5715a24-8289-499c-8963-5fb26e6fc628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgxa9Ns1NPwReGmivvT1mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16889,
      "cache_read_input_tokens": 58514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16889
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

_source line 57 · 2026-05-18T22:16:29.689Z_

<details><summary>↩ Tool result · `toolu_01YSLrhmDzymmch9CJsZPJGq`</summary>

```text
docs/paper/sections/related_work.tex:16:[Omitted long matching line]
docs/paper/sections/experiments.tex:67:[Omitted long matching line]
docs/paper/sections/discussion.tex:10:[Omitted long matching line]
docs/paper/sections/method.tex:52:[Omitted long matching line]
docs/paper/sections/appendix.tex:53:[Omitted long matching line]
docs/paper/sections/appendix.tex:109:\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
docs/paper/sections/appendix.tex:134:[Omitted long matching line]
docs/paper/sections/appendix.tex:213:\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
docs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
docs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
docs/paper/sections/appendix.tex:298:\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
docs/paper/sections/appendix.tex:300:\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
docs/paper/sections/appendix.tex:368:[Omitted long matching line]
docs/paper/sections/appendix.tex:371:[Omitted long matching line]
docs/paper/sections/appendix.tex:387:\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
docs/paper/sections/appendix.tex:399:[Omitted long matching line]
docs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\tau{=}0.5$.
docs/paper/sections/appendix.tex:562:[Omitted long matching line]
docs/paper/sections/appendix.tex:636:[Omitted long matching line]
docs/paper/sections/appendix.tex:689:PCA capacity matching (\cref{app:encoder_robustness}) preserves 79--92\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\cref{tab:random_projection}).
docs/paper/sections/appendix.tex:708:[Omitted long matching line]
docs/paper/sections/appendix.tex:733:[Omitted long matching line]
docs/paper/sections/appendix.tex:759:[Omitted long matching line]
docs/paper/sections/appendix.tex:767:The joint search space for layer (${\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.
docs/paper/sections/appendix.tex:932:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "42b38676-1b91-4adb-a18f-c71c3f6efd51",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:16:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:67:[Omitted long matching line]\ndocs/paper/sections/discussion.tex:10:[Omitted long matching line]\ndocs/paper/sections/method.tex:52:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:53:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:109:\\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}\ndocs/paper/sections/appendix.tex:134:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:213:\\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.\ndocs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.\ndocs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.\ndocs/paper/sections/appendix.tex:298:\\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\\% training portion, we hold out 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\ndocs/paper/sections/appendix.tex:300:\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\ndocs/paper/sections/appendix.tex:368:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:371:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:387:\\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.\ndocs/paper/sections/appendix.tex:399:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\\Delta$BA $= +0.109$ to $+0.126$, $\\Delta$Prec $= +0.113$ to $+0.143$, $\\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\tau{=}0.5$.\ndocs/paper/sections/appendix.tex:562:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:636:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:689:PCA capacity matching (\\cref{app:encoder_robustness}) preserves 79--92\\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\\cref{tab:random_projection}).\ndocs/paper/sections/appendix.tex:708:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:733:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:759:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:767:The joint search space for layer (${\\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.\ndocs/paper/sections/appendix.tex:932:[Omitted long matching line]",
    "numLines": 25
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Grep · `toolu_01GuyoBukdMmvsM54N9vut7X`</summary>

```json
{
  "pattern": "(?i)(Furthermore|Moreover)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "33859fde-993e-4897-abaa-085be1d09590",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgxa9Ns1NPwReGmivvT1mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16889,
      "cache_read_input_tokens": 58514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16889
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

_source line 59 · 2026-05-18T22:16:31.176Z_

<details><summary>↩ Tool result · `toolu_01GuyoBukdMmvsM54N9vut7X`</summary>

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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "7f349df3-7f44-4600-bc8c-b7a0dab46117",
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

_source line 60_

<details open><summary>🔧 Tool call — Grep · `toolu_012RT2yU5QRHPYSA1Yihu2iu`</summary>

```json
{
  "pattern": ", (suggesting|confirming|indicating|demonstrating|highlighting|showing|making|rendering|strengthening|weakening|providing|following|raising|producing|yielding) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "glob": "*.tex",
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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "db4b15fa-289b-4bb5-9efa-ee60af98a7d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgxa9Ns1NPwReGmivvT1mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16889,
      "cache_read_input_tokens": 58514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16889
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

_source line 61 · 2026-05-18T22:16:33.121Z_

<details><summary>↩ Tool result · `toolu_012RT2yU5QRHPYSA1Yihu2iu`</summary>

```text
docs/paper/sections/discussion.tex:7:[Omitted long matching line]
docs/paper/sections/discussion.tex:10:[Omitted long matching line]
docs/paper/sections/method.tex:52:[Omitted long matching line]
docs/paper/sections/limitations.tex:7:[Omitted long matching line]
docs/paper/sections/appendix.tex:47:[Omitted long matching line]
docs/paper/sections/appendix.tex:53:[Omitted long matching line]
docs/paper/sections/appendix.tex:134:[Omitted long matching line]
docs/paper/sections/appendix.tex:213:\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
docs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
docs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
docs/paper/sections/appendix.tex:298:\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
docs/paper/sections/appendix.tex:300:\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
docs/paper/sections/appendix.tex:371:[Omitted long matching line]
docs/paper/sections/appendix.tex:387:\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
docs/paper/sections/appendix.tex:399:[Omitted long matching line]
docs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\tau{=}0.5$.
docs/paper/sections/appendix.tex:562:[Omitted long matching line]
docs/paper/sections/appendix.tex:619:\paragraph{RepE.} Mean-difference directions~\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\ LR 0.700) and FPR (0.309 vs.\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.
docs/paper/sections/appendix.tex:623:\paragraph{CCS.} Contrast-Consistent Search~\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.
docs/paper/sections/appendix.tex:636:[Omitted long matching line]
docs/paper/sections/appendix.tex:689:PCA capacity matching (\cref{app:encoder_robustness}) preserves 79--92\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\cref{tab:random_projection}).
docs/paper/sections/appendix.tex:708:[Omitted long matching line]
docs/paper/sections/appendix.tex:733:[Omitted long matching line]
docs/paper/sections/appendix.tex:759:[Omitted long matching line]
docs/paper/sections/appendix.tex:767:The joint search space for layer (${\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.
docs/paper/sections/appendix.tex:791:For the most fragile result (R1-8B FPR), bias-corrected accelerated (BCa) bootstrap yields a 95\% CI of [0.006, 0.159] ($p{=}0.033$), with 12\% leave-one-out instability (\cref{app:multi_seed}). The CI excludes zero, confirming significance despite seed fragility. CP annotation perturbation (\cref{tab:cp_perturbation}) further shows that $\pm 2$-step label noise changes BA by ${<}2.5$pp, so annotation uncertainty does not compound with hyperparameter selection.
docs/paper/sections/appendix.tex:932:[Omitted long matching line]
docs/paper/sections/introduction.tex:13:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "2282fc3e-3fd0-4879-9ca6-cdd59fed7fd7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/discussion.tex:7:[Omitted long matching line]\ndocs/paper/sections/discussion.tex:10:[Omitted long matching line]\ndocs/paper/sections/method.tex:52:[Omitted long matching line]\ndocs/paper/sections/limitations.tex:7:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:47:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:53:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:134:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:213:\\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.\ndocs/paper/sections/appendix.tex:240:OpenThinker-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.\ndocs/paper/sections/appendix.tex:290:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.\ndocs/paper/sections/appendix.tex:298:\\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\\% training portion, we hold out 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\ndocs/paper/sections/appendix.tex:300:\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\ndocs/paper/sections/appendix.tex:371:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:387:\\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.\ndocs/paper/sections/appendix.tex:399:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:554:R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\\Delta$BA $= +0.109$ to $+0.126$, $\\Delta$Prec $= +0.113$ to $+0.143$, $\\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\tau{=}0.5$.\ndocs/paper/sections/appendix.tex:562:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:619:\\paragraph{RepE.} Mean-difference directions~\\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\\ LR 0.700) and FPR (0.309 vs.\\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.\ndocs/paper/sections/appendix.tex:623:\\paragraph{CCS.} Contrast-Consistent Search~\\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.\ndocs/paper/sections/appendix.tex:636:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:689:PCA capacity matching (\\cref{app:encoder_robustness}) preserves 79--92\\% of variance, raising the question of whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projection (3 seeds, averaged) and compare with text embeddings at the same dimensionality (\\cref{tab:random_projection}).\ndocs/paper/sections/appendix.tex:708:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:733:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:759:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:767:The joint search space for layer (${\\leq}64$), window $W$ (7 values), consecutive-crossing threshold $K$ (5 values), and decision threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting to small validation sets ($n{=}4$--$9$ per class at 32B). Three analyses address this concern.\ndocs/paper/sections/appendix.tex:791:For the most fragile result (R1-8B FPR), bias-corrected accelerated (BCa) bootstrap yields a 95\\% CI of [0.006, 0.159] ($p{=}0.033$), with 12\\% leave-one-out instability (\\cref{app:multi_seed}). The CI excludes zero, confirming significance despite seed fragility. CP annotation perturbation (\\cref{tab:cp_perturbation}) further shows that $\\pm 2$-step label noise changes BA by ${<}2.5$pp, so annotation uncertainty does not compound with hyperparameter selection.\ndocs/paper/sections/appendix.tex:932:[Omitted long matching line]\ndocs/paper/sections/introduction.tex:13:[Omitted long matching line]",
    "numLines": 28
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
The grep results have many "[Omitted long matching line]" entries. Let me use bash to grep with actual text output so I can see the full lines and evaluate each match properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "2b07266f-d6f0-451f-855f-9ae00f1f3024",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeUvTiWfwZzcy4wGAS9BJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 75403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3909
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

_source line 63_

The grep output is truncating long lines. Let me use bash for more precise analysis of the specific patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "ea6d6245-ee28-4116-a4e7-7c11d9bb4bf7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeUvTiWfwZzcy4wGAS9BJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 75403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3909
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

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01EgyqNZVxzoevR85qawSVtX`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper && grep -n '—' sections/*.tex main.tex 2>/dev/null | head -20",
  "description": "Check for em-dash in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "554f1f98-f1db-46d1-8971-b37ad18bd3cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeUvTiWfwZzcy4wGAS9BJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 75403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3909
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

_source line 65 · 2026-05-18T22:16:38.540Z_

<details><summary>↩ Tool result · `toolu_01EgyqNZVxzoevR85qawSVtX`</summary>

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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "cc367327-490e-475e-af45-14dc9541e19d",
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

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_019cTdhXthnBpqDUscvmiBjC`</summary>

```json
{
  "command": "grep -n ' – ' sections/*.tex main.tex 2>/dev/null | head -20",
  "description": "Check for explanatory en-dash in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "5090a94b-2704-413c-8ea4-e3a21f685061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeUvTiWfwZzcy4wGAS9BJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 75403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3909
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

_source line 67 · 2026-05-18T22:16:39.608Z_

<details><summary>↩ Tool result · `toolu_019cTdhXthnBpqDUscvmiBjC`</summary>

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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "5a7048cd-e2f7-45b8-819e-75495f9082f8",
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01X93znPRRupbRm2nwKYTGRG`</summary>

```json
{
  "command": "grep -rnoP ', (suggesting|confirming|indicating|demonstrating|highlighting|showing|making|rendering|strengthening|weakening|providing|yielding|raising|producing|following|motivating) ' sections/*.tex main.tex 2>/dev/null",
  "description": "Search for -ing participial phrases after commas"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "f96e953e-c59c-496f-bf9e-cb8fd7ee9231",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeUvTiWfwZzcy4wGAS9BJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 75403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3909
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

_source line 69 · 2026-05-18T22:16:41.242Z_

<details><summary>↩ Tool result · `toolu_01X93znPRRupbRm2nwKYTGRG`</summary>

```text
sections/appendix.tex:47:, demonstrating 
sections/appendix.tex:53:, yielding 
sections/appendix.tex:53:, confirming 
sections/appendix.tex:134:, confirming 
sections/appendix.tex:213:, confirming 
sections/appendix.tex:240:, producing 
sections/appendix.tex:290:, following 
sections/appendix.tex:298:, yielding 
sections/appendix.tex:300:, producing 
sections/appendix.tex:371:, confirming 
sections/appendix.tex:387:, confirming 
sections/appendix.tex:399:, suggesting 
sections/appendix.tex:554:, confirming 
sections/appendix.tex:562:, producing 
sections/appendix.tex:619:, making 
sections/appendix.tex:623:, making 
sections/appendix.tex:636:, rendering 
sections/appendix.tex:689:, raising 
sections/appendix.tex:708:, suggesting 
sections/appendix.tex:733:, confirming 
sections/appendix.tex:759:, indicating 
sections/appendix.tex:767:, raising 
sections/appendix.tex:791:, confirming 
sections/appendix.tex:932:, confirming 
sections/discussion.tex:7:, providing 
sections/discussion.tex:10:, suggesting 
sections/introduction.tex:13:, providing 
sections/limitations.tex:7:, yielding 
sections/method.tex:52:, making
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "d93dbaa6-ae8d-4bf6-83d6-0184594e1bf6",
  "tool_use_result": {
    "stdout": "sections/appendix.tex:47:, demonstrating \nsections/appendix.tex:53:, yielding \nsections/appendix.tex:53:, confirming \nsections/appendix.tex:134:, confirming \nsections/appendix.tex:213:, confirming \nsections/appendix.tex:240:, producing \nsections/appendix.tex:290:, following \nsections/appendix.tex:298:, yielding \nsections/appendix.tex:300:, producing \nsections/appendix.tex:371:, confirming \nsections/appendix.tex:387:, confirming \nsections/appendix.tex:399:, suggesting \nsections/appendix.tex:554:, confirming \nsections/appendix.tex:562:, producing \nsections/appendix.tex:619:, making \nsections/appendix.tex:623:, making \nsections/appendix.tex:636:, rendering \nsections/appendix.tex:689:, raising \nsections/appendix.tex:708:, suggesting \nsections/appendix.tex:733:, confirming \nsections/appendix.tex:759:, indicating \nsections/appendix.tex:767:, raising \nsections/appendix.tex:791:, confirming \nsections/appendix.tex:932:, confirming \nsections/discussion.tex:7:, providing \nsections/discussion.tex:10:, suggesting \nsections/introduction.tex:13:, providing \nsections/limitations.tex:7:, yielding \nsections/method.tex:52:, making",
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

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01XMHSzasPWNhTpYTPwipaPm`</summary>

```json
{
  "command": "grep -noP 'notably' sections/*.tex main.tex 2>/dev/null",
  "description": "Check for \"notably\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "e23826db-4849-40e1-912d-059c6eee0ef5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXjYB1gYBLFmjMBf9m4TmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 79312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 889
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 71 · 2026-05-18T22:16:44.613Z_

<details><summary>↩ Tool result · `toolu_01XMHSzasPWNhTpYTPwipaPm`</summary>

```text
sections/appendix.tex:206:notably
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "169f72aa-7578-45de-b192-8c7003b1dc70",
  "tool_use_result": {
    "stdout": "sections/appendix.tex:206:notably",
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

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_019ma8jtGty6edDJznNyaWNm`</summary>

```json
{
  "command": "grep -noP '(?i)(Additionally|In addition)' sections/*.tex main.tex 2>/dev/null",
  "description": "Check for Additionally / In addition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "e2f7b21e-300f-48e0-9ada-dad6e5991db7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXjYB1gYBLFmjMBf9m4TmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 79312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 889
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 73 · 2026-05-18T22:16:46.015Z_

<details><summary>↩ Tool result · `toolu_019ma8jtGty6edDJznNyaWNm`</summary>

```text
sections/appendix.tex:634:additionally
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "96edb14f-c563-443c-b969-ea5949481fcc",
  "tool_use_result": {
    "stdout": "sections/appendix.tex:634:additionally",
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

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_01KKxCDBuss5EtPg2CeAbp8r`</summary>

```json
{
  "command": "grep -noP '(?i)(delve|leverage|utilize|facilitate|myriad|plethora|in the realm|paradigm shift|It is worth noting)' sections/*.tex main.tex 2>/dev/null",
  "description": "Check for AI blacklist words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "31b6bc7d-cfe1-4384-acd6-50b1aac09e94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXjYB1gYBLFmjMBf9m4TmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 79312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 889
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 75 · 2026-05-18T22:16:47.594Z_

<details><summary>↩ Tool result · `toolu_01KKxCDBuss5EtPg2CeAbp8r`</summary>

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
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "02794418-43e0-4d52-b87e-1754398d1092",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01E3mm9mqVtz4fhHSyUHd7zF`</summary>

```json
{
  "command": "for f in sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/discussion.tex sections/conclusion.tex sections/limitations.tex; do echo \"=== $f ===\" && grep -nP ', (suggesting|confirming|indicating|demonstrating|highlighting|showing|making|rendering|strengthening|weakening|providing|yielding|raising|producing|following|motivating) ' \"$f\" 2>/dev/null; done",
  "description": "-ing phrases in main sections with context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "bef4b4dc-373f-4de0-a165-e91b0479125d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAyn5V3txJtaQ4DJS2hcvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 80201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 77 · 2026-05-18T22:16:51.669Z_

<details><summary>↩ Tool result · `toolu_01E3mm9mqVtz4fhHSyUHd7zF`</summary>

```text
=== sections/abstract.tex ===
=== sections/introduction.tex ===
13:    \item \textbf{Encoder-quality boundary with evidence gradient.} The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\dagger$ (+15.4 to +21.9pp precision, Holm-Bonferroni corrected) but attenuated against 1024d BGE-large (1/4 HB-significant). This boundary suggests the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference (\cref{fig:forest_precision}). PCA capacity matching to 384d preserves significance (+16.8 to +23.1pp, 79--92\% variance retained), providing partial evidence against a pure capacity explanation. Evidence strength varies by model: strong for OT-7B (5/5 seeds HB, $+21.9$pp, no caveats), moderate for R1-8B (FPR seed-fragile, 3/5 HB) and QwQ-32B$^\dagger$ (5/5 HB, negative lead time), and qualified for R1-32B$^\dagger$ (5/5 HB but position-mediated, residualized gap NS; \cref{sec:32b-analysis}).
=== sections/related_work.tex ===
=== sections/method.tex ===
52:We report balanced accuracy, precision, pre-CP FPR, coverage, and lead time (steps between first detection and true CP). Step-level metrics evaluate per-step classification; trace-level metrics aggregate across an entire reasoning trace (e.g., trace-level FPR is the fraction of safe traces with any false alarm exceeding $K$ consecutive crossings). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance; sensitivity analysis (\cref{app:k_ablation}) confirms that $K \in \{3, 5, 7\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison, though a post-hoc rationale for $K{=}5$ is that it corresponds to a sustained commitment signal rather than transient fluctuation. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine representational structure (\cref{app:control}). Throughout, $\dagger$ marks conclusions drawn from sample-limited test sets ($n \leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).
=== sections/experiments.tex ===
=== sections/discussion.tex ===
7:The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\dagger$ (4/4 HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at 7--8B, the modality advantage exceeds temporal improvement; temporal windowing ($W{=}3$ to $15$) provides consistent gains regardless of modality.
10:The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\% early detection with 50-step lead time, while R1-32B reaches only 50\% early detection (\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or ITI~\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.
=== sections/conclusion.tex ===
=== sections/limitations.tex ===
7:Layer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class at 32B), yielding up to $2{,}240$ configurations; cumulative degrees of freedom are substantial (\cref{app:hyperparameter_robustness} provides convergence, cross-validation, and bootstrap analyses addressing this concern). BA-optimal layer indices are sensitive to the train/validation split, spanning 7--98\% depth across models and splits (\cref{tab:ba_layer_comparison}); for example, OT-7B shifts from L16 to L2 and QwQ-32B from L60 to L63 between 70/30 and 60/20/20 splits, a direct manifestation of the layer selection sensitivity that constitutes our primary finding. Threshold-dependent metrics are more stable but still vary by up to 4 layers. $K$ was pre-selected (\cref{app:k_ablation}); joint (layer, $W$) stability was verified for QwQ-32B (\cref{app:layer_sweep}) but not R1-32B. CP annotations follow HarmThoughts~\citep{harmthoughts} without independent IAA evaluation; if annotation error is ${\geq}2$ steps, QwQ-32B's lead time ($-$1.2 to +1.9) falls within noise, though perturbation analysis shows smooth degradation with no cliff effects (\cref{app:cp_perturbation}). We cover 2 architectures and 2 scales; intermediate scales, proprietary models, and multilingual settings are untested. Results are correlational; causal intervention is needed to confirm mechanistic involvement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "cbd03a67-9960-4207-ba18-0a1de29d44e5",
  "tool_use_result": {
    "stdout": "=== sections/abstract.tex ===\n=== sections/introduction.tex ===\n13:    \\item \\textbf{Encoder-quality boundary with evidence gradient.} The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\\dagger$ (+15.4 to +21.9pp precision, Holm-Bonferroni corrected) but attenuated against 1024d BGE-large (1/4 HB-significant). This boundary suggests the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference (\\cref{fig:forest_precision}). PCA capacity matching to 384d preserves significance (+16.8 to +23.1pp, 79--92\\% variance retained), providing partial evidence against a pure capacity explanation. Evidence strength varies by model: strong for OT-7B (5/5 seeds HB, $+21.9$pp, no caveats), moderate for R1-8B (FPR seed-fragile, 3/5 HB) and QwQ-32B$^\\dagger$ (5/5 HB, negative lead time), and qualified for R1-32B$^\\dagger$ (5/5 HB but position-mediated, residualized gap NS; \\cref{sec:32b-analysis}).\n=== sections/related_work.tex ===\n=== sections/method.tex ===\n52:We report balanced accuracy, precision, pre-CP FPR, coverage, and lead time (steps between first detection and true CP). Step-level metrics evaluate per-step classification; trace-level metrics aggregate across an entire reasoning trace (e.g., trace-level FPR is the fraction of safe traces with any false alarm exceeding $K$ consecutive crossings). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance; sensitivity analysis (\\cref{app:k_ablation}) confirms that $K \\in \\{3, 5, 7\\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison, though a post-hoc rationale for $K{=}5$ is that it corresponds to a sustained commitment signal rather than transient fluctuation. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\\times$ 4 models $= 12$ tests, $\\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\\citep{hewitt2019control} validates genuine representational structure (\\cref{app:control}). Throughout, $\\dagger$ marks conclusions drawn from sample-limited test sets ($n \\leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).\n=== sections/experiments.tex ===\n=== sections/discussion.tex ===\n7:The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\\dagger$ (4/4 HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at 7--8B, the modality advantage exceeds temporal improvement; temporal windowing ($W{=}3$ to $15$) provides consistent gains regardless of modality.\n10:The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\\% early detection with 50-step lead time, while R1-32B reaches only 50\\% early detection (\\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \\cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\\citep{geiger2025causal}, LEACE~\\citep{belrose2023leace}, or ITI~\\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.\n=== sections/conclusion.tex ===\n=== sections/limitations.tex ===\n7:Layer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class at 32B), yielding up to $2{,}240$ configurations; cumulative degrees of freedom are substantial (\\cref{app:hyperparameter_robustness} provides convergence, cross-validation, and bootstrap analyses addressing this concern). BA-optimal layer indices are sensitive to the train/validation split, spanning 7--98\\% depth across models and splits (\\cref{tab:ba_layer_comparison}); for example, OT-7B shifts from L16 to L2 and QwQ-32B from L60 to L63 between 70/30 and 60/20/20 splits, a direct manifestation of the layer selection sensitivity that constitutes our primary finding. Threshold-dependent metrics are more stable but still vary by up to 4 layers. $K$ was pre-selected (\\cref{app:k_ablation}); joint (layer, $W$) stability was verified for QwQ-32B (\\cref{app:layer_sweep}) but not R1-32B. CP annotations follow HarmThoughts~\\citep{harmthoughts} without independent IAA evaluation; if annotation error is ${\\geq}2$ steps, QwQ-32B's lead time ($-$1.2 to +1.9) falls within noise, though perturbation analysis shows smooth degradation with no cliff effects (\\cref{app:cp_perturbation}). We cover 2 architectures and 2 scales; intermediate scales, proprietary models, and multilingual settings are untested. Results are correlational; causal intervention is needed to confirm mechanistic involvement.",
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

_source line 78_

Now let me check for over-segmented paragraphs and unclear pronoun references by examining the content I've already read. Let me also get the specific line content for the appendix -ing phrases.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "6b8ef3ff-ff36-4da4-9c96-4d9b20408653",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5uBoWG7rtobMfAqn7uQNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 80697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_017M6LcSJ1fNvxYduX7fmr9P`</summary>

```json
{
  "command": "for line in 47 53 134 213 240 290 298 300 371 387 399 554 562 619 623 636 689 708 733 759 767 791 932; do echo \"=== appendix.tex:$line ===\" && sed -n \"${line}p\" sections/appendix.tex | grep -oP '.{0,60}, (suggesting|confirming|indicating|demonstrating|highlighting|showing|making|rendering|strengthening|weakening|providing|yielding|raising|producing|following|motivating) .{0,60}'; done",
  "description": "Extract -ing phrase context from appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "94c8896d-f53b-4e02-a9ba-f99e9a07af5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5uBoWG7rtobMfAqn7uQNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 80697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 80 · 2026-05-18T22:16:57.438Z_

<details><summary>↩ Tool result · `toolu_017M6LcSJ1fNvxYduX7fmr9P`</summary>

```text
=== appendix.tex:47 ===
the canonical 60/20/20, it selects L63 (98\%) and L46 (72\%), demonstrating sensitivity to the data split.
=== appendix.tex:53 ===
2B across 64 layers $\times$ 3 windows ($W \in \{1, 3, 5\}$), yielding 192 configurations (\cref{tab:joint_layer_w}). L60 is near-o
om middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV
=== appendix.tex:134 ===
tent with the bootstrap values in \cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of di
=== appendix.tex:213 ===
indow} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongl
=== appendix.tex:240 ===
-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from
=== appendix.tex:290 ===
 $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show 
=== appendix.tex:298 ===
 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The valid
=== appendix.tex:300 ===
om 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
=== appendix.tex:371 ===
 FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), confirming that GRUs gain lead time at the cost of more false alarms ac
=== appendix.tex:387 ===
rected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
=== appendix.tex:399 ===
) achieves only 50\% early detection even with oracle labels, suggesting that its commitment signal is inherently weaker. On R1-8B, t
=== appendix.tex:554 ===
onsistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\ta
=== appendix.tex:562 ===
n noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text
=== appendix.tex:619 ===
 captures commitment structure in some models but not others, making it unreliable as a general-purpose method.
=== appendix.tex:623 ===
tructure. CCS still requires CP labels for pair construction, making it semi-supervised.
=== appendix.tex:636 ===
ransferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. T
=== appendix.tex:689 ===
cref{app:encoder_robustness}) preserves 79--92\% of variance, raising the question of whether the HS advantage depends on PCA's st
=== appendix.tex:708 ===
a structure-destroying projection preserves the HS advantage, suggesting the safety signal is broadly distributed across hidden-state
=== appendix.tex:733 ===
n consistently falls between MiniLM and HS across all models, confirming that encoder quality progressively narrows the gap. PCA to 3
=== appendix.tex:759 ===
 exception: residualized HS-text gap is +1.9pp ($p{=}0.914$), indicating its HS advantage is position-mediated. Larger temporal windo
=== appendix.tex:767 ===
 threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting t
=== appendix.tex:791 ===
ut instability (\cref{app:multi_seed}). The CI excludes zero, confirming significance despite seed fragility. CP annotation perturbat
=== appendix.tex:932 ===
d-dependent layers (+15.4 to +21.9pp; \cref{tab:hs_vs_text}), confirming that the HS advantage is robust to the choice of layer selec
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "cb292ac4-753a-47e6-b643-050cb749d6b1",
  "tool_use_result": {
    "stdout": "=== appendix.tex:47 ===\nthe canonical 60/20/20, it selects L63 (98\\%) and L46 (72\\%), demonstrating sensitivity to the data split.\n=== appendix.tex:53 ===\n2B across 64 layers $\\times$ 3 windows ($W \\in \\{1, 3, 5\\}$), yielding 192 configurations (\\cref{tab:joint_layer_w}). L60 is near-o\nom middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV\n=== appendix.tex:134 ===\ntent with the bootstrap values in \\cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of di\n=== appendix.tex:213 ===\nindow} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongl\n=== appendix.tex:240 ===\n-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from\n=== appendix.tex:290 ===\n $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show \n=== appendix.tex:298 ===\n 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The valid\n=== appendix.tex:300 ===\nom 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\n=== appendix.tex:371 ===\n FPR (27.4\\%) is far above the LR probe at layer 16 (10.0\\%), confirming that GRUs gain lead time at the cost of more false alarms ac\n=== appendix.tex:387 ===\nrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.\n=== appendix.tex:399 ===\n) achieves only 50\\% early detection even with oracle labels, suggesting that its commitment signal is inherently weaker. On R1-8B, t\n=== appendix.tex:554 ===\nonsistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\ta\n=== appendix.tex:562 ===\nn noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text\n=== appendix.tex:619 ===\n captures commitment structure in some models but not others, making it unreliable as a general-purpose method.\n=== appendix.tex:623 ===\ntructure. CCS still requires CP labels for pair construction, making it semi-supervised.\n=== appendix.tex:636 ===\nransferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. T\n=== appendix.tex:689 ===\ncref{app:encoder_robustness}) preserves 79--92\\% of variance, raising the question of whether the HS advantage depends on PCA's st\n=== appendix.tex:708 ===\na structure-destroying projection preserves the HS advantage, suggesting the safety signal is broadly distributed across hidden-state\n=== appendix.tex:733 ===\nn consistently falls between MiniLM and HS across all models, confirming that encoder quality progressively narrows the gap. PCA to 3\n=== appendix.tex:759 ===\n exception: residualized HS-text gap is +1.9pp ($p{=}0.914$), indicating its HS advantage is position-mediated. Larger temporal windo\n=== appendix.tex:767 ===\n threshold is large (up to 2{,}240 configurations per model), raising the concern that reported performance reflects overfitting t\n=== appendix.tex:791 ===\nut instability (\\cref{app:multi_seed}). The CI excludes zero, confirming significance despite seed fragility. CP annotation perturbat\n=== appendix.tex:932 ===\nd-dependent layers (+15.4 to +21.9pp; \\cref{tab:hs_vs_text}), confirming that the HS advantage is robust to the choice of layer selec",
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

_source line 81_

Now let me check for unclear pronoun references (This/That/It at sentence starts) and over-segmented paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "d44991d0-82c6-4936-8d2c-30f4ff6521b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7vdjiqBeY7H5MsxqzJFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1437,
      "cache_read_input_tokens": 82580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1437
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 82_

<details open><summary>🔧 Tool call — Bash · `toolu_01VvTr6SZX57MaDKFzbs9cKp`</summary>

```json
{
  "command": "grep -nP '(^|\\. )This (demonstrates|suggests|indicates|shows|implies|confirms|reveals|means|highlights|underscores|ensures|makes|is)[^a-z]' sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/discussion.tex sections/conclusion.tex sections/limitations.tex 2>/dev/null",
  "description": "Check for \"This + verb\" unclear pronoun in main sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "6c318106-03a1-4f71-b1a5-88440ed49cb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7vdjiqBeY7H5MsxqzJFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1437,
      "cache_read_input_tokens": 82580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1437
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 83 · 2026-05-18T22:17:04.012Z_

<details><summary>↩ Tool result · `toolu_01VvTr6SZX57MaDKFzbs9cKp`</summary>

```text
sections/discussion.tex:10:The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\% early detection with 50-step lead time, while R1-32B reaches only 50\% early detection (\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or ITI~\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "c7e83c6a-6941-46bf-bd30-c21008990c42",
  "tool_use_result": {
    "stdout": "sections/discussion.tex:10:The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\\% early detection with 50-step lead time, while R1-32B reaches only 50\\% early detection (\\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \\cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\\citep{geiger2025causal}, LEACE~\\citep{belrose2023leace}, or ITI~\\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.",
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

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01N3VFHYkXna424kzqUxBNGu`</summary>

```json
{
  "command": "grep -nP '(^|\\. )This (demonstrates|suggests|indicates|shows|implies|confirms|reveals|means|highlights|underscores|ensures|makes|is)[^a-z]' sections/appendix.tex 2>/dev/null",
  "description": "Check for \"This + verb\" in appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "37eae1d4-b7a8-4180-8438-884e1137cc4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7vdjiqBeY7H5MsxqzJFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1437,
      "cache_read_input_tokens": 82580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1437
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 85 · 2026-05-18T22:17:05.098Z_

<details><summary>↩ Tool result · `toolu_01N3VFHYkXna424kzqUxBNGu`</summary>

```text
661:The HS precision advantage is directionally consistent across all four models (positive $\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "fa9e4eda-4f2a-450d-85a4-5d1314df23be",
  "tool_use_result": {
    "stdout": "661:The HS precision advantage is directionally consistent across all four models (positive $\\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \\cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.",
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

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_014Nh7XM3uCmQeVDvUEjpqTN`</summary>

```json
{
  "command": "grep -nP '\\. This [a-z]' sections/*.tex | grep -vP '\\. This (failure|boundary|failure|paper|comparison|finding|probe|baseline|pattern|loss|setting|bug|control|value|instability|asymmetry|variance|approach|advantage|gap|transition|divergence|limitation|mechanism|metric|section|paragraph|table|figure|analysis|result|test|effect|report|split|step|work|improvement|evaluation|correction|configuration)' | head -30",
  "description": "Find \"This\" + verb (potential unclear pronoun)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "4ace7727-4726-4aca-b1bb-9126dbd1b06c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7vdjiqBeY7H5MsxqzJFb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1437,
      "cache_read_input_tokens": 82580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1437
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 87 · 2026-05-18T22:17:08.885Z_

<details><summary>↩ Tool result · `toolu_014Nh7XM3uCmQeVDvUEjpqTN`</summary>

```text
sections/appendix.tex:132:The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
sections/appendix.tex:397:We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.
sections/appendix.tex:562:\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).
sections/appendix.tex:661:The HS precision advantage is directionally consistent across all four models (positive $\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.
sections/appendix.tex:708:All four models retain significant HS advantage under random projection ($\Delta$Prec +8.3 to +20.5pp), with cross-seed standard deviations below 1.7pp. RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. This weakens a pure capacity explanation: even a structure-destroying projection preserves the HS advantage, suggesting the safety signal is broadly distributed across hidden-state dimensions rather than concentrated in top principal components.
sections/discussion.tex:10:The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\% early detection with 50-step lead time, while R1-32B reaches only 50\% early detection (\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or ITI~\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "c4971724-c90a-48ea-bd1f-98728bf77d0c",
  "tool_use_result": {
    "stdout": "sections/appendix.tex:132:The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\\%), which leaves less room for HS improvement on this metric.\nsections/appendix.tex:397:We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.\nsections/appendix.tex:562:\\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).\nsections/appendix.tex:661:The HS precision advantage is directionally consistent across all four models (positive $\\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \\cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.\nsections/appendix.tex:708:All four models retain significant HS advantage under random projection ($\\Delta$Prec +8.3 to +20.5pp), with cross-seed standard deviations below 1.7pp. RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. This weakens a pure capacity explanation: even a structure-destroying projection preserves the HS advantage, suggesting the safety signal is broadly distributed across hidden-state dimensions rather than concentrated in top principal components.\nsections/discussion.tex:10:The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\\% early detection with 50-step lead time, while R1-32B reaches only 50\\% early detection (\\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \\cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\\citep{geiger2025causal}, LEACE~\\citep{belrose2023leace}, or ITI~\\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.",
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

_source line 88_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of all the issues. Let me compile the audit report. Let me also quickly check for over-segmented paragraphs. I need to look at each section's paragraph structure.

Let me check over-segmentation by looking at paragraph boundaries (blank lines between non-empty, non-command lines).

Actually, looking at the files I've already read, I can determine this. Let me review:

- abstract.tex: 1 paragraph, fine
- introduction.tex: well-structured paragraphs, not over-segmented
- related_work.tex: uses \paragraph{} headers, typical for related work


- method.tex: uses subsections and \paragraph{}, reasonable
- experiments.tex: uses subsections and \paragraph{}, reasonable
- discussion.tex: uses \paragraph{}, 3 paragraphs - each seems substantive
- conclusion.tex: 1 paragraph, fine
- limitations.tex: 2 \paragraph{} sections, each substantial

The main text doesn't seem to have over-segmentation issues. The appendix is a collection of many sections which is normal. From my reading of the files, the writing is quite dense with substantial paragraphs throughout, so I don't see obvious over-segmentation problems.

Now I'm compiling the audit findings. The em-dash and en-dash usage is clean with none found. For -ing phrases, I'm seeing a handful scattered through the main body—introduction, methods, discussion, and limitations sections—with several more instances in the appendix. Let me document these findings for the report. I'm continuing through the appendix to identify all the problematic -ing phrases that end sentences. Looking at this next batch, I see patterns like "making it unreliable," "rendering it useless," "raising the question," "suggesting the safety signal," and so on—each one ending a sentence with a participle phrase. Counting these up alongside the ones I already found, I'm getting to around 28 total instances across the main body and appendix combined, though I need to be careful to only count the actual sentence-ending -ing constructions rather than all gerunds. I'm narrowing down the problematic patterns here. The rule targets sentence-ending participial phrases with commas, so I need to distinguish between mid-sentence clauses and actual sentence-final ones. Looking at the instances more carefully, some like "producing a 7B reasoning model" are embedded in the middle of sentences, while others like "making the correction stricter than under independence" genuinely end clauses. I should flag the sentence-final ones as violations but recognize that mid-sentence participial phrases are acceptable. For the blacklist words, I found "notably" once and "additionally" once, neither of which represents a pattern issue.

Now checking for other structural problems—the paragraphs seem appropriately dense without over-segmentation, and while there are several instances of "This" as a pronoun, most have reasonably clear antecedents from the immediately preceding sentence, though a couple like the one in discussion.tex:10 are slightly ambiguous.

I'm noticing a pattern of trailing -ing phrases that feel characteristic of AI writing—constructions like "confirming that," "suggesting that," "demonstrating," and "indicating" appear repeatedly throughout. Some of these are natural English, but the frequency and consistency suggest I should flag the clearest cases where these connective phrases dominate the style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "6154fdd4-9aa4-4473-acdc-35a1a0f52b93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNtqP3z8f3VsHtBaCP144n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 84017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2144
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

_source line 89_

Now I have all the data. Let me compile the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "afe290f7-1285-4cb3-bdd7-9b6360eb7ca4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNtqP3z8f3VsHtBaCP144n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 84017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2144
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

_source line 90_

<details open><summary>🔧 Tool call — Write · `toolu_01Q66tuocd97ZuPMVysM2GDm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/ai_writing_audit.md",
  "content": "# AI Writing Style Audit\n\n## Summary\n- Total issues: 33\n- Files checked: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex\n\n## Issues by Category\n\n### Em-dash / En-dash (0 issues)\n0 issues found ✓\n\nNo Unicode em-dash (—) or explanatory en-dash ( – ) detected in any file.\n\n### -ing Phrases (29 issues)\n\n**Main body (6):**\n\n- `sections/introduction.tex:13` — \"...79--92\\% variance retained), **providing** partial evidence against a pure capacity explanation.\" → 拆分：\"...79--92\\% variance retained); this provides partial evidence against...\"\n- `sections/method.tex:52` — \"...the three metrics are positively correlated by construction, **making** the correction stricter than under independence.\" → 改为：\"...by construction, so the correction is stricter than under independence.\"\n- `sections/discussion.tex:7` — \"PCA capacity matching preserves significance (+16.8 to +23.1pp), **providing** partial evidence against a pure capacity explanation.\" → 改为：\"PCA capacity matching preserves significance (+16.8 to +23.1pp) and provides partial evidence against...\"\n- `sections/discussion.tex:10` — \"...while R1-32B reaches only 50\\% early detection, **suggesting** that the commitment signal strength itself varies across models.\" → 改为：\"...only 50\\% early detection. The gap suggests that the commitment signal strength varies across models.\"\n- `sections/limitations.tex:7` — \"...are selected on the same validation set, **yielding** up to 2,240 configurations\" → 改为：\"...are selected on the same validation set (up to 2,240 configurations);\"\n\n**Appendix (23):**\n\n- `sections/appendix.tex:47` — \"...it selects L63 (98\\%) and L46 (72\\%), **demonstrating** sensitivity to the data split.\" → \"...L46 (72\\%), which demonstrates sensitivity to the data split.\"\n- `sections/appendix.tex:53` — \"...3 windows, **yielding** 192 configurations\" → \"...3 windows (192 configurations)\"\n- `sections/appendix.tex:53` — \"...to deep (L60 at $W{=}5$), **confirming** a layer-window interaction.\" → \"...at $W{=}5$), which confirms a layer-window interaction.\"\n- `sections/appendix.tex:134` — \"...consistent with the bootstrap values, **confirming** that the bootstrap-based conclusions are not artifacts\" → \"...consistent with the bootstrap values and confirm that the conclusions are not artifacts\"\n- `sections/appendix.tex:213` — \"...window sweep on R1-8B, **confirming** that temporal context benefits text probes\" → \"...sweep on R1-8B and confirms that temporal context benefits text probes\"\n- `sections/appendix.tex:240` — \"...trained with STILL on Qwen2.5-7B, **producing** a 7B reasoning model\" → \"...STILL on Qwen2.5-7B to produce a 7B reasoning model\"\n- `sections/appendix.tex:290` — \"...+8.5pp precision, $-$18.4pp FPR), **following** the same pattern as R1-8B\" → \"...$-$18.4pp FPR), consistent with the R1-8B pattern.\"\n- `sections/appendix.tex:298` — \"...as a validation set for early stopping, **yielding** an effective 60/10/30 split.\" → \"...for early stopping (effective 60/10/30 split).\"\n- `sections/appendix.tex:300` — \"...through the network) at each step, **producing** a higher-dimensional input\" → \"...at each step to produce a higher-dimensional input\"\n- `sections/appendix.tex:371` — \"...LR probe at layer 16 (10.0\\%), **confirming** that GRUs gain lead time at the cost of more false alarms\" → \"...at layer 16 (10.0\\%), which confirms that GRUs gain lead time...\"\n- `sections/appendix.tex:387` — \"...selectivity is 16.1pp at L63, **confirming** that safety-specific signal persists at deep layers.\" → \"...at L63, which confirms that safety-specific signal persists...\"\n- `sections/appendix.tex:399` — \"...only 50\\% early detection even with oracle labels, **suggesting** that its commitment signal is inherently weaker.\" → \"...even with oracle labels, consistent with an inherently weaker commitment signal.\"\n- `sections/appendix.tex:554` — \"...consistent in both magnitude and direction, **confirming** that the HS advantage is not an artifact\" → \"...in both magnitude and direction, so the HS advantage is not an artifact\"\n- `sections/appendix.tex:562` — \"...trivially predictive, **producing** a spuriously significant result\" → \"...trivially predictive and produced a spuriously significant result\"\n- `sections/appendix.tex:619` — \"...in some models but not others, **making** it unreliable as a general-purpose method.\" → \"...in some models but not others, so it is unreliable as a general-purpose method.\"\n- `sections/appendix.tex:623` — \"...CCS still requires CP labels for pair construction, **making** it semi-supervised.\" → \"...still requires CP labels for pair construction and is therefore semi-supervised.\"\n- `sections/appendix.tex:636` — \"...almost never triggers detection in practice, **rendering** it useless for deployment\" → \"...almost never triggers detection in practice and is useless for deployment\"\n- `sections/appendix.tex:689` — \"...preserves 79--92\\% of variance, **raising** the question of whether the HS advantage depends on PCA's structure\" → \"...preserves 79--92\\% of variance. A natural question is whether the HS advantage depends on PCA's structure\"\n- `sections/appendix.tex:708` — \"...projection preserves the HS advantage, **suggesting** the safety signal is broadly distributed\" → \"...preserves the HS advantage. The safety signal appears broadly distributed\"\n- `sections/appendix.tex:733` — \"...falls between MiniLM and HS across all models, **confirming** that encoder quality progressively narrows the gap.\" → \"...across all models, consistent with encoder quality progressively narrowing the gap.\"\n- `sections/appendix.tex:759` — \"...residualized HS-text gap is +1.9pp ($p{=}0.914$), **indicating** its HS advantage is position-mediated.\" → \"...is +1.9pp ($p{=}0.914$), so its HS advantage is position-mediated.\"\n- `sections/appendix.tex:767` — \"...is large (up to 2,240 configurations per model), **raising** the concern that reported performance reflects overfitting\" → \"...is large (up to 2,240 configurations per model). This raises the concern that reported performance reflects overfitting\"\n- `sections/appendix.tex:791` — \"The CI excludes zero, **confirming** significance despite seed fragility.\" → \"The CI excludes zero and confirms significance despite seed fragility.\"\n- `sections/appendix.tex:932` — \"...comparable to those at threshold-dependent layers, **confirming** that the HS advantage is robust to the choice\" → \"...comparable to those at threshold-dependent layers, so the HS advantage is robust to the choice\"\n\n### Consecutive Transition Words (0 issues)\n0 issues found ✓\n\nNo \"Furthermore\", \"Moreover\", or consecutive transition words in same paragraphs.\n\n### AI Blacklist Words (1 issue)\n\n- `sections/appendix.tex:206` — \"QwQ-32B produces **notably** longer lead times than R1-8B\" → \"QwQ-32B produces longer lead times than R1-8B\" (或 \"substantially longer\")\n\n### Over-segmented Paragraphs (0 issues)\n0 issues found ✓\n\nAll paragraphs are substantive (5+ sentences or dense technical content). No 2-sentence paragraph splitting detected.\n\n### Unclear Pronouns (3 issues)\n\n- `sections/discussion.tex:10` — \"...only 50\\% early detection, suggesting that the commitment signal strength itself varies across models. **This indicates** that distillation and native reasoning produce qualitatively different safety representation geometry.\" → \"This\" 的先行词是前一个从句的整体含义，但读起来指代不够清晰。建议：\"The cross-model variation indicates that distillation and native reasoning produce qualitatively different safety representation geometry.\"\n- `sections/appendix.tex:397` — \"The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. **This provides** a theoretical ceiling on early detection performance.\" → \"This\" 指代整个 oracle detector 的计算过程。建议：\"The resulting bound provides a theoretical ceiling...\"\n- `sections/appendix.tex:708` — \"RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. **This weakens** a pure capacity explanation: even a structure-destroying projection preserves the HS advantage\" → \"This\" 指代 RP 和 PCA 结果接近这一事实。建议：\"The small gap weakens a pure capacity explanation...\"\n\n---\n\n## Priority\n\n1. **-ing phrases (29)** — 这是最显著的 AI 写作标志，数量较多，尤其 appendix 中 \"confirming that...\" 出现 10+ 次，重复度高。建议：全文替换 `, confirming` → 改为 \"which confirms\" / \"and confirms\" / \"so\" / \"consistent with\"。\n2. **Blacklist words (1)** — \"notably\" 只出现一次，容易修。\n3. **Unclear pronouns (3)** — 修复成本低。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "f814ba74-7ad7-4b3f-b64c-2aaee97e6f39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNtqP3z8f3VsHtBaCP144n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 84017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2144
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

_source line 91 · 2026-05-18T22:18:23.056Z_

<details><summary>↩ Tool result · `toolu_01Q66tuocd97ZuPMVysM2GDm`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/ai_writing_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "136ef5c0-fd57-4bee-b3ba-ce898ec62db2",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/ai_writing_audit.md",
    "content": "# AI Writing Style Audit\n\n## Summary\n- Total issues: 33\n- Files checked: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex\n\n## Issues by Category\n\n### Em-dash / En-dash (0 issues)\n0 issues found ✓\n\nNo Unicode em-dash (—) or explanatory en-dash ( – ) detected in any file.\n\n### -ing Phrases (29 issues)\n\n**Main body (6):**\n\n- `sections/introduction.tex:13` — \"...79--92\\% variance retained), **providing** partial evidence against a pure capacity explanation.\" → 拆分：\"...79--92\\% variance retained); this provides partial evidence against...\"\n- `sections/method.tex:52` — \"...the three metrics are positively correlated by construction, **making** the correction stricter than under independence.\" → 改为：\"...by construction, so the correction is stricter than under independence.\"\n- `sections/discussion.tex:7` — \"PCA capacity matching preserves significance (+16.8 to +23.1pp), **providing** partial evidence against a pure capacity explanation.\" → 改为：\"PCA capacity matching preserves significance (+16.8 to +23.1pp) and provides partial evidence against...\"\n- `sections/discussion.tex:10` — \"...while R1-32B reaches only 50\\% early detection, **suggesting** that the commitment signal strength itself varies across models.\" → 改为：\"...only 50\\% early detection. The gap suggests that the commitment signal strength varies across models.\"\n- `sections/limitations.tex:7` — \"...are selected on the same validation set, **yielding** up to 2,240 configurations\" → 改为：\"...are selected on the same validation set (up to 2,240 configurations);\"\n\n**Appendix (23):**\n\n- `sections/appendix.tex:47` — \"...it selects L63 (98\\%) and L46 (72\\%), **demonstrating** sensitivity to the data split.\" → \"...L46 (72\\%), which demonstrates sensitivity to the data split.\"\n- `sections/appendix.tex:53` — \"...3 windows, **yielding** 192 configurations\" → \"...3 windows (192 configurations)\"\n- `sections/appendix.tex:53` — \"...to deep (L60 at $W{=}5$), **confirming** a layer-window interaction.\" → \"...at $W{=}5$), which confirms a layer-window interaction.\"\n- `sections/appendix.tex:134` — \"...consistent with the bootstrap values, **confirming** that the bootstrap-based conclusions are not artifacts\" → \"...consistent with the bootstrap values and confirm that the conclusions are not artifacts\"\n- `sections/appendix.tex:213` — \"...window sweep on R1-8B, **confirming** that temporal context benefits text probes\" → \"...sweep on R1-8B and confirms that temporal context benefits text probes\"\n- `sections/appendix.tex:240` — \"...trained with STILL on Qwen2.5-7B, **producing** a 7B reasoning model\" → \"...STILL on Qwen2.5-7B to produce a 7B reasoning model\"\n- `sections/appendix.tex:290` — \"...+8.5pp precision, $-$18.4pp FPR), **following** the same pattern as R1-8B\" → \"...$-$18.4pp FPR), consistent with the R1-8B pattern.\"\n- `sections/appendix.tex:298` — \"...as a validation set for early stopping, **yielding** an effective 60/10/30 split.\" → \"...for early stopping (effective 60/10/30 split).\"\n- `sections/appendix.tex:300` — \"...through the network) at each step, **producing** a higher-dimensional input\" → \"...at each step to produce a higher-dimensional input\"\n- `sections/appendix.tex:371` — \"...LR probe at layer 16 (10.0\\%), **confirming** that GRUs gain lead time at the cost of more false alarms\" → \"...at layer 16 (10.0\\%), which confirms that GRUs gain lead time...\"\n- `sections/appendix.tex:387` — \"...selectivity is 16.1pp at L63, **confirming** that safety-specific signal persists at deep layers.\" → \"...at L63, which confirms that safety-specific signal persists...\"\n- `sections/appendix.tex:399` — \"...only 50\\% early detection even with oracle labels, **suggesting** that its commitment signal is inherently weaker.\" → \"...even with oracle labels, consistent with an inherently weaker commitment signal.\"\n- `sections/appendix.tex:554` — \"...consistent in both magnitude and direction, **confirming** that the HS advantage is not an artifact\" → \"...in both magnitude and direction, so the HS advantage is not an artifact\"\n- `sections/appendix.tex:562` — \"...trivially predictive, **producing** a spuriously significant result\" → \"...trivially predictive and produced a spuriously significant result\"\n- `sections/appendix.tex:619` — \"...in some models but not others, **making** it unreliable as a general-purpose method.\" → \"...in some models but not others, so it is unreliable as a general-purpose method.\"\n- `sections/appendix.tex:623` — \"...CCS still requires CP labels for pair construction, **making** it semi-supervised.\" → \"...still requires CP labels for pair construction and is therefore semi-supervised.\"\n- `sections/appendix.tex:636` — \"...almost never triggers detection in practice, **rendering** it useless for deployment\" → \"...almost never triggers detection in practice and is useless for deployment\"\n- `sections/appendix.tex:689` — \"...preserves 79--92\\% of variance, **raising** the question of whether the HS advantage depends on PCA's structure\" → \"...preserves 79--92\\% of variance. A natural question is whether the HS advantage depends on PCA's structure\"\n- `sections/appendix.tex:708` — \"...projection preserves the HS advantage, **suggesting** the safety signal is broadly distributed\" → \"...preserves the HS advantage. The safety signal appears broadly distributed\"\n- `sections/appendix.tex:733` — \"...falls between MiniLM and HS across all models, **confirming** that encoder quality progressively narrows the gap.\" → \"...across all models, consistent with encoder quality progressively narrowing the gap.\"\n- `sections/appendix.tex:759` — \"...residualized HS-text gap is +1.9pp ($p{=}0.914$), **indicating** its HS advantage is position-mediated.\" → \"...is +1.9pp ($p{=}0.914$), so its HS advantage is position-mediated.\"\n- `sections/appendix.tex:767` — \"...is large (up to 2,240 configurations per model), **raising** the concern that reported performance reflects overfitting\" → \"...is large (up to 2,240 configurations per model). This raises the concern that reported performance reflects overfitting\"\n- `sections/appendix.tex:791` — \"The CI excludes zero, **confirming** significance despite seed fragility.\" → \"The CI excludes zero and confirms significance despite seed fragility.\"\n- `sections/appendix.tex:932` — \"...comparable to those at threshold-dependent layers, **confirming** that the HS advantage is robust to the choice\" → \"...comparable to those at threshold-dependent layers, so the HS advantage is robust to the choice\"\n\n### Consecutive Transition Words (0 issues)\n0 issues found ✓\n\nNo \"Furthermore\", \"Moreover\", or consecutive transition words in same paragraphs.\n\n### AI Blacklist Words (1 issue)\n\n- `sections/appendix.tex:206` — \"QwQ-32B produces **notably** longer lead times than R1-8B\" → \"QwQ-32B produces longer lead times than R1-8B\" (或 \"substantially longer\")\n\n### Over-segmented Paragraphs (0 issues)\n0 issues found ✓\n\nAll paragraphs are substantive (5+ sentences or dense technical content). No 2-sentence paragraph splitting detected.\n\n### Unclear Pronouns (3 issues)\n\n- `sections/discussion.tex:10` — \"...only 50\\% early detection, suggesting that the commitment signal strength itself varies across models. **This indicates** that distillation and native reasoning produce qualitatively different safety representation geometry.\" → \"This\" 的先行词是前一个从句的整体含义，但读起来指代不够清晰。建议：\"The cross-model variation indicates that distillation and native reasoning produce qualitatively different safety representation geometry.\"\n- `sections/appendix.tex:397` — \"The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. **This provides** a theoretical ceiling on early detection performance.\" → \"This\" 指代整个 oracle detector 的计算过程。建议：\"The resulting bound provides a theoretical ceiling...\"\n- `sections/appendix.tex:708` — \"RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. **This weakens** a pure capacity explanation: even a structure-destroying projection preserves the HS advantage\" → \"This\" 指代 RP 和 PCA 结果接近这一事实。建议：\"The small gap weakens a pure capacity explanation...\"\n\n---\n\n## Priority\n\n1. **-ing phrases (29)** — 这是最显著的 AI 写作标志，数量较多，尤其 appendix 中 \"confirming that...\" 出现 10+ 次，重复度高。建议：全文替换 `, confirming` → 改为 \"which confirms\" / \"and confirms\" / \"so\" / \"consistent with\"。\n2. **Blacklist words (1)** — \"notably\" 只出现一次，容易修。\n3. **Unclear pronouns (3)** — 修复成本低。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 92_

审计完成，结果保存在 `artifacts/ai_writing_audit.md`。

核心发现：
- **33 个问题**，集中在一个类别
- **Em-dash / En-dash**: 0（干净）
- **-ing 分词短语**: 29 个（最严重问题，主体 6 个 + 附录 23 个）。"`, confirming that...`" 模式出现 10+ 次，重复度高，是最显眼的 AI 痕迹
- **连续过渡词**: 0
- **AI 黑名单词**: 1 个（"notably"，附录中）
- **过度分段**: 0
- **代词指代不清**: 3 个

修复优先级：先批量处理 -ing 短语（尤其是 `, confirming` → `which confirms` / `and confirms` / `so`），这是审稿人最容易识别的模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "uuid": "e3e570a4-bf2c-46d4-b026-ad760cb89d27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVkLhNAAVjdwArVA7gB45a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 86161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4584
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

_source line 93_

审计完成，结果保存在 `artifacts/ai_writing_audit.md`。

核心发现：
- **33 个问题**，集中在一个类别
- **Em-dash / En-dash**: 0（干净）
- **-ing 分词短语**: 29 个（最严重问题，主体 6 个 + 附录 23 个）。"`, confirming that...`" 模式出现 10+ 次，重复度高，是最显眼的 AI 痕迹
- **连续过渡词**: 0
- **AI 黑名单词**: 1 个（"notably"，附录中）
- **过度分段**: 0
- **代词指代不清**: 3 个

修复优先级：先批量处理 -ing 短语（尤其是 `, confirming` → `which confirms` / `and confirms` / `so`），这是审稿人最容易识别的模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 166013,
  "duration_api_ms": 167279,
  "num_turns": 38,
  "stop_reason": "end_turn",
  "session_id": "13e47f3a-195f-4daa-a003-3ce60ed70222",
  "total_cost_usd": 1.1176055,
  "usage": {
    "input_tokens": 427,
    "cache_creation_input_tokens": 79298,
    "cache_read_input_tokens": 729914,
    "output_tokens": 10132,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 79298,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 261,
        "cache_read_input_tokens": 86161,
        "cache_creation_input_tokens": 4584,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4584
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1516,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001601,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 427,
      "outputTokens": 10132,
      "cacheReadInputTokens": 729914,
      "cacheCreationInputTokens": 79298,
      "webSearchRequests": 0,
      "costUSD": 1.1160045,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f56fbf0c-5e5f-475f-aeef-1a6227f6a33c"
}
```

</details>

---
