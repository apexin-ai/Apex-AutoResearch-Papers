# paper arr checklist draft

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_arr_checklist_draft_20260522T223403.log`
- **Structured JSON:** [`3f4036d9658dd0f67886.json`](../../sessions/3f/3f4036d9658dd0f67886.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
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
  "uuid": "a681d25c-4730-453b-98d7-e8386b976986",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779499800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "469cdc82-0b57-41eb-b94f-3305e1a6c5d1",
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to draft an ARR Responsible NLP Checklist response for their paper submission. Let me:

1. Search for the latest ARR checklist
2. Read the relevant paper sections
3. Draft the checklist answers

Let me start by doing the web search and reading the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "e80c2a12-9ca3-43cc-b9bf-bce80ca6abe2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uzibEmGLPye1osxARpP6R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12925,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12925
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014iyfDifcmGApq7MDjFG1TY`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "4af02df2-836f-41e0-828c-fe0843f33794",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uzibEmGLPye1osxARpP6R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12925,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12925
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

_source line 6 · 2026-05-22T22:34:19.805Z_

<details><summary>↩ Tool result · `toolu_014iyfDifcmGApq7MDjFG1TY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "19190491-9dcf-458e-bf93-2536c63ca8a8",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the ARR checklist and read the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "82a6f119-13c0-459a-91c3-8eb97c3b739a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FngTxfKvxbG1uSkSw19UY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 24766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VEfSPJyuvuF3Dn7T8q9VtC`</summary>

```json
{
  "query": "ARR Responsible NLP Research Checklist 2025 2026 questions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "d0896b9a-242f-4521-8da6-ea615292f95f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FngTxfKvxbG1uSkSw19UY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 24766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01XkE2xZgo2n9BtJps4WfujV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "434d2a05-0c51-4b39-a922-83d03652e3c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FngTxfKvxbG1uSkSw19UY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 24766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 10 · 2026-05-22T22:34:27.761Z_

<details><summary>↩ Tool result · `toolu_01XkE2xZgo2n9BtJps4WfujV`</summary>

```text
1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a worst-case injection model; reported $\Delta\mathrm{TPR}$ values are upper-bound estimates, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "26c6aeec-e464-4918-81e7-a11b408adc57",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex",
      "content": "\\section*{Limitations}\n\n\\looseness=-1\nThree primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a worst-case injection model; reported $\\Delta\\mathrm{TPR}$ values are upper-bound estimates, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. More fundamentally, DIF detects \\emph{that} items function differently but cannot determine \\emph{why}. (2)~The MH $\\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\\approx}$27--29\\%) and family-level cluster bootstrap (95\\% CI: $[26.7\\%, 53.2\\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\\Delta\\mathrm{FPR}$ rises to 0.069 when contamination spans ${\\geq}20$ subjects. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01H6v6BnNbNBw978CFzTWiJQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "c952492b-3b9e-44dd-9973-e4783e1feb73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FngTxfKvxbG1uSkSw19UY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 24766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 12 · 2026-05-22T22:34:28.786Z_

<details><summary>↩ Tool result · `toolu_01H6v6BnNbNBw978CFzTWiJQ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal measurement instability} as the empirical phenomenon when DIF is detected across time-defined cohorts---a descriptive term denoting systematic changes in measurement properties, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. This instability does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings); it is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Contamination detectors---from membership inference~\citep{shi2024mink} to performance-based methods~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}---validate primarily against web-overlap labels~\citep{li2024contamination} that measure \emph{global exposure}: whether an item exists in publicly accessible training corpora. Such labels do not capture \emph{differential item functioning}: whether an item behaves differently across cohorts with varying exposure or training methodology (\Cref{fig:global_vs_differential}). Direct comparison confirms near-independence (Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Schematic illustration of global vs.\ differential contamination via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply a temporal DIF audit framework to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge the largest-scale DIF analysis on LLM benchmarks, complementing concurrent work on anchor-item calibration~\citep{habba2026growingpains} and addressing the fragility of existing detectors under post-training perturbation~\citep{wang2026fragility}. Two structural controls, a sensitivity check, and replication across all six METABENCH benchmarks confirm that the temporal DIF rate (${\approx}$27--29\% after non-independence corrections) is not a methodological artifact (\Cref{sec:temporal,sec:structural,sec:gsm8k}).
16	
17	DIF should be understood as a diagnostic lens rather than a quality filter: DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\ random removal; \Cref{sec:downstream}), and model families show distinctive DIF profiles.
18	
19	Our contributions are methodological and empirical, not algorithmic:
20	
21	\begin{enumerate}
22	\item \textbf{Orthogonal constructs}: We empirically demonstrate that web-overlap labels~\citep{li2024contamination}, which index global exposure, are near-independent of DIF flags, which index differential functioning (Jaccard $= 0.206$, $\phi = 0.012$ on 9,229 items); the two capture fundamentally different signals (\Cref{sec:groundtruth}).
23	
24	\item \textbf{Temporal DIF audit framework}: We develop and validate a general-purpose audit framework for multi-domain benchmarks, comprising cross-subject matching ($\Delta\mathrm{FPR} = 0$ guarantee), family-level clustering, per-item design-effect correction, and base-vs-instruct mechanism decomposition; validated semi-synthetically and replicated on GSM8K (\Cref{sec:semisynthetic,sec:gsm8k}).
25	
26	\item \textbf{Temporal measurement instability at scale}: We establish that ${\approx}$27--29\% of MMLU items exhibit temporal DIF after non-independence corrections; replication across six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$. Base-vs-instruct stratification reveals mechanistically distinct patterns ($\chi^2 = 562.7$), providing positive evidence for mechanism separation (\Cref{sec:temporal,sec:gsm8k,sec:disc_temporal}).
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "d96caa91-5f8c-458e-9aae-daaad3714267",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \\emph{measurement invariance} to denote the property that test items function identically across groups~\\citep{meredith1993invariance}, \\emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \\emph{temporal measurement instability} as the empirical phenomenon when DIF is detected across time-defined cohorts---a descriptive term denoting systematic changes in measurement properties, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\\citep{kipnis2024metabench},\\footnote{Analysis code and DIF audit scripts are available at \\url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\\% of MMLU~\\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\\% under a random-split control. This instability does not threaten benchmark validity ($\\rho \\approx 0.997$ between full and stable-item rankings); it is diagnostic, revealing which capability dimensions shift across model generations.\n\nContamination detectors---from membership inference~\\citep{shi2024mink} to performance-based methods~\\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}---validate primarily against web-overlap labels~\\citep{li2024contamination} that measure \\emph{global exposure}: whether an item exists in publicly accessible training corpora. Such labels do not capture \\emph{differential item functioning}: whether an item behaves differently across cohorts with varying exposure or training methodology (\\Cref{fig:global_vs_differential}). Direct comparison confirms near-independence (Jaccard $= 0.206$, $\\phi = 0.012$), consistent across contamination subtypes.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_1_global_vs_differential.pdf}\n\\caption{Schematic illustration of global vs.\\ differential contamination via Item Characteristic Curves (ICCs). \\textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \\textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}\n\\label{fig:global_vs_differential}\n\\end{figure}\n\nWe apply a temporal DIF audit framework to the full METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), to our knowledge the largest-scale DIF analysis on LLM benchmarks, complementing concurrent work on anchor-item calibration~\\citep{habba2026growingpains} and addressing the fragility of existing detectors under post-training perturbation~\\citep{wang2026fragility}. Two structural controls, a sensitivity check, and replication across all six METABENCH benchmarks confirm that the temporal DIF rate (${\\approx}$27--29\\% after non-independence corrections) is not a methodological artifact (\\Cref{sec:temporal,sec:structural,sec:gsm8k}).\n\nDIF should be understood as a diagnostic lens rather than a quality filter: DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\\ random removal; \\Cref{sec:downstream}), and model families show distinctive DIF profiles.\n\nOur contributions are methodological and empirical, not algorithmic:\n\n\\begin{enumerate}\n\\item \\textbf{Orthogonal constructs}: We empirically demonstrate that web-overlap labels~\\citep{li2024contamination}, which index global exposure, are near-independent of DIF flags, which index differential functioning (Jaccard $= 0.206$, $\\phi = 0.012$ on 9,229 items); the two capture fundamentally different signals (\\Cref{sec:groundtruth}).\n\n\\item \\textbf{Temporal DIF audit framework}: We develop and validate a general-purpose audit framework for multi-domain benchmarks, comprising cross-subject matching ($\\Delta\\mathrm{FPR} = 0$ guarantee), family-level clustering, per-item design-effect correction, and base-vs-instruct mechanism decomposition; validated semi-synthetically and replicated on GSM8K (\\Cref{sec:semisynthetic,sec:gsm8k}).\n\n\\item \\textbf{Temporal measurement instability at scale}: We establish that ${\\approx}$27--29\\% of MMLU items exhibit temporal DIF after non-independence corrections; replication across six METABENCH benchmarks yields C\\% $= 17.9$--$31.3\\%$. Base-vs-instruct stratification reveals mechanistically distinct patterns ($\\chi^2 = 562.7$), providing positive evidence for mechanism separation (\\Cref{sec:temporal,sec:gsm8k,sec:disc_temporal}).\n\\end{enumerate}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01D6dcNaVc3c3KnEfJRvb9Rc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "4ed4faa4-9a95-43b3-9342-b1c41d34a91e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FngTxfKvxbG1uSkSw19UY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 24766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 14 · 2026-05-22T22:34:28.990Z_

<details><summary>↩ Tool result · `toolu_01D6dcNaVc3c3KnEfJRvb9Rc`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%]; family-level cluster bootstrap CI $[26.7\%, 53.2\%]$). Two independent non-independence corrections converge on approximately 27--29\%: simple-mean DEFF correction (29.2\%) and family-level cluster bootstrap lower bound (26.7\%). The weighted-mean DEFF variant yields 13.5\%, but its effective cluster size ($\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\rho_s = -0.009$, $p = 0.96$; \Cref{app:icc_family}), so the weighted variant over-corrects (size-stratified analysis confirms: tier-level ICC decreases from 0.25 to 0.08 as family size grows, violating the homogeneity assumption that drives the weighted estimate; \Cref{tab:deff_stratified}). The $[13.5\%, 29.2\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\Delta_{\mathrm{MH}}| \geq 1.5$ unchanged). We adopt ${\approx}$27--29\% as our primary estimate, with 13.5\% as a lower bound under weighted-mean DEFF (\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\Delta\mathrm{C\%}| \leq 2.93$\,pp). Graduated de-duplication independently confirms C\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\,pp across random draws (\Cref{app:dedup_k}). C\% is stable across $K \geq 5$ (31.3\%--35.9\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, which may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation, while $K{=}3$ inflates to 39.4\% from under-stratification.
17	
18	\looseness=-1
19	Three controls confirm genuine temporal change (\Cref{tab:temporal_landscape}): random splits yield C\% of 0.18\% (2023) and 1.3\% (2024), both ${\geq}23\times$ below temporal C\%; ability-quintile comparison yields 2.9\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\% $= 28.9\% \pm 0.1\%$, confirming at most ${\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \Cref{app:method_details}).
20	
21	\looseness=-1
22	Across all 57 subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$; \Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\%), Humanities favor 2023 (64.4\%). Domain-level accuracy gains explain ${<}0.1\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is associated with item properties rather than aggregate gains (OR reverses from 1.55 to 0.73 after controlling for difficulty; \Cref{app:structural}). A difficulty--direction interaction emerges ($\rho = -0.597$): 2024 models gain on hard items while eroding on easy ones. The conclusion is robust across thresholds ($18.3\%$ at $|\Delta_{\mathrm{MH}}| \geq 2.0$, $10.2\%$ at $\geq 2.5$).
23	
24	\begin{table}[t]
25	\centering
26	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. C\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\ labels are not applicable.}
27	\label{tab:temporal_landscape}
28	\small
29	\resizebox{\columnwidth}{!}{%
30	\begin{tabular}{lcccc}
31	\toprule
32	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & C\% (web-clean) & Enrich. \\
33	\midrule
34	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
35	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
36	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
37	Random split 2023 (sanity) & 540 / 540 & 0.18 & -- & -- \\
38	Random split 2024 (sanity) & ${\sim}$400 / ${\sim}$400 & 1.3 & -- & -- \\
39	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
40	\bottomrule
41	\end{tabular}}
42	\end{table}
43	
44	\subsection{Ground Truth Mismatch}
45	\label{sec:groundtruth}
46	
47	\looseness=-1
48	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (bootstrap 95\% CI: $[0.94, 1.02]$; \Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests confirm near-independence ($\phi = 0.012$, OR $= 1.05$ [0.96, 1.15], Jaccard $= 0.206$, within permutation null $[0.203, 0.222]$; $p = 0.88$). This near-independence holds across contamination subtypes. The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The two constructs---global exposure and differential functioning---are empirically orthogonal.
49	\begin{figure}[t]
50	\centering
51	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
52	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
53	\label{fig:dose_response}
54	\end{figure}
55	
56	\subsection{Structural Analysis}
57	\label{sec:structural}
58	
59	\looseness=-1
60	Two structural controls and a sensitivity check fail to reduce temporal C\% below 31\% (\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\% $= 38.1\%$; cross-subject C\% is more conservative due to lower local dependence), and IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$). Logistic regression on nine subjects (1{,}787 items; 9/57---full-benchmark rates require further analysis) detects an additional 17.7\% with non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$; effect-size criterion; LR $p$-values not adjusted for clustering); the union reaches 47\% (Jaccard $= 0.28$): ${\approx}$27--29\% uniform (MH) plus 17.7\% non-uniform (interaction-only), mutually exclusive by construction. Ability-matched analysis yields C\% $= 28.9\%$ (temporal) and $28.3\%$ (Llama-2 vs.\ 3)---consistent matched values (${\sim}$28--29\%) despite vastly different unmatched rates (\Cref{app:structural}).
61	
62	\begin{table}[t]
63	\centering
64	\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\% below 31\%; $\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}
65	\label{tab:structural_comparison}
66	\small
67	\resizebox{\columnwidth}{!}{%
68	\begin{tabular}{lcccc}
69	\toprule
70	Approach & Mechanism & Temp.\ C\% & TPR ($p{=}0.5$) & Outcome \\
71	\midrule
72	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
73	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
74	$\theta$-cond.\ (sens.) & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
75	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
76	\bottomrule
77	\end{tabular}}
78	\end{table}
79	
80	\subsection{Semi-Synthetic Framework Validation}
81	\label{sec:semisynthetic}
82	
83	\looseness=-1
84	Cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$, upper-bound estimate under uniform binary flipping; \Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ on average. The $\Delta\mathrm{FPR} = 0$ guarantee holds for single-subject contamination ($k \leq 5$, $\Delta\mathrm{FPR} < 0.007$). Under broader contamination spanning $k = 10$ subjects (18\% of domains), $\Delta\mathrm{FPR}$ rises to $0.047 \pm 0.022$; at $k = 20$, to $0.069 \pm 0.018$ (\Cref{tab:multi_subject_injection,app:fig_matching}). Even worst-case multi-subject inflation ($\sim$7~pp) cannot account for the observed 31\% C\% rate, which exceeds the 0.18\% random baseline by ${>}170\times$. Under DEFF adjustment, worst-case $\Delta\mathrm{FPR}$ at $k{=}20$ (0.069) represents up to 50\% of the 13.5\% lower bound, underscoring $k \leq 5$ in practice. Difficulty-dependent injection produces distinguishable $\rho$ signatures (capability-like: $+0.77$ vs.\ contamination-like: $-0.52$; zero seed overlap), though mapping to real-data mechanisms requires further work.
85	
86	\subsection{Downstream Impact}
87	\label{sec:downstream}
88	
89	\looseness=-1
90	Stable-item ranks are preserved across all six benchmarks ($\rho = 0.997$, $\tau = 0.958$; flip rate $\leq 2.8\%$; \Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\ random removal; \Cref{app:fig_downstream}). Among the 200 most displaced models (top 3.8\%), 33.6\% of pairwise rankings reverse, concentrating among closely-ranked pairs (35.2\% at $\Delta\mathrm{rank} < 50$ vs.\ 0.0\% above 1000; \Cref{app:rank_reversal}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\times$ random; $p < 0.001$).
91	
92	\subsection{Cross-Benchmark Validation}
93	\label{sec:gsm8k}
94	
95	\looseness=-1
96	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}): C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU), with knowledge/reasoning benchmarks consistently higher than procedural ones (C\% $= 26.9$--$31.3\%$ vs.\ $17.9$--$18.9\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.
97	
98	\begin{table}[t]
99	\centering
100	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts; $\rho$/$\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\%/Rand.\ C\%, with baseline varying by benchmark. All six show substantial DIF (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
101	\label{tab:cross_benchmark}
102	\small
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{lrrrrrrl}
105	\toprule
106	Benchmark & Items & C\% & $\rho$ & $\tau$ & Flip\% & Rand.\ C\% & Ratio \\
107	\midrule
108	MMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.18 & 174$\times$ \\
109	WinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\times$ \\
110	TruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\times$ \\
111	ARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\times$ \\
112	GSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\times$ \\
113	HellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\times$ \\
114	\bottomrule
115	\end{tabular}}
116	\end{table}
117	
118	Semi-synthetic injection on GSM8K confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$; \Cref{app:gsm8k_details}). As an exploratory cross-benchmark signal, GSM1K contamination gaps correlate with DIF-C item accuracy ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{app:fig_gsm1k}), but the small sample requires replication.
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "0515d78a-627e-464b-b3db-14b0f127fe06",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH response matrix~\\citep{kipnis2024metabench} (5,227 models $\\times$ 12,508 MMLU items~\\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\n\\looseness=-1\nAs approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\\citep{zhou2026psnirt} ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \\geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ (details in \\Cref{app:method_details}). Our temporal cohorts ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\\Cref{app:power_sensitivity}).\n\n\\subsection{Temporal Comparability: 31\\% Measurement Instability}\n\\label{sec:temporal}\n\n\\looseness=-1\nWe compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 95\\% bootstrap CI: [29.4\\%, 38.1\\%]; family-level cluster bootstrap CI $[26.7\\%, 53.2\\%]$). Two independent non-independence corrections converge on approximately 27--29\\%: simple-mean DEFF correction (29.2\\%) and family-level cluster bootstrap lower bound (26.7\\%). The weighted-mean DEFF variant yields 13.5\\%, but its effective cluster size ($\\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\\rho_s = -0.009$, $p = 0.96$; \\Cref{app:icc_family}), so the weighted variant over-corrects (size-stratified analysis confirms: tier-level ICC decreases from 0.25 to 0.08 as family size grows, violating the homogeneity assumption that drives the weighted estimate; \\Cref{tab:deff_stratified}). The $[13.5\\%, 29.2\\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ unchanged). We adopt ${\\approx}$27--29\\% as our primary estimate, with 13.5\\% as a lower bound under weighted-mean DEFF (\\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp). Graduated de-duplication independently confirms C\\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\\,pp across random draws (\\Cref{app:dedup_k}). C\\% is stable across $K \\geq 5$ (31.3\\%--35.9\\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, which may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation, while $K{=}3$ inflates to 39.4\\% from under-stratification.\n\n\\looseness=-1\nThree controls confirm genuine temporal change (\\Cref{tab:temporal_landscape}): random splits yield C\\% of 0.18\\% (2023) and 1.3\\% (2024), both ${\\geq}23\\times$ below temporal C\\%; ability-quintile comparison yields 2.9\\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\\% $= 28.9\\% \\pm 0.1\\%$, confirming at most ${\\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \\Cref{app:method_details}).\n\n\\looseness=-1\nAcross all 57 subjects, C\\% ranges from 20.7\\% to 48.4\\% (mean $\\approx 30\\%$; \\Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \\emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\\%), Humanities favor 2023 (64.4\\%). Domain-level accuracy gains explain ${<}0.1\\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is associated with item properties rather than aggregate gains (OR reverses from 1.55 to 0.73 after controlling for difficulty; \\Cref{app:structural}). A difficulty--direction interaction emerges ($\\rho = -0.597$): 2024 models gain on hard items while eroding on easy ones. The conclusion is robust across thresholds ($18.3\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 2.0$, $10.2\\%$ at $\\geq 2.5$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. C\\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \\citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\\ labels are not applicable.}\n\\label{tab:temporal_landscape}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & C\\% & C\\% (web-clean) & Enrich. \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split 2023 (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nRandom split 2024 (sanity) & ${\\sim}$400 / ${\\sim}$400 & 1.3 & -- & -- \\\\\nWithin-subject (avg, 5 subj.) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\n\\looseness=-1\nDirect comparison of DIF flags against the web-overlap labels of \\citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (bootstrap 95\\% CI: $[0.94, 1.02]$; \\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\\% among web-contaminated items and 31.8\\% among clean items. Association tests confirm near-independence ($\\phi = 0.012$, OR $= 1.05$ [0.96, 1.15], Jaccard $= 0.206$, within permutation null $[0.203, 0.222]$; $p = 0.88$). This near-independence holds across contamination subtypes. The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \\emph{global exposure} (whether an item exists in training corpora), while DIF measures \\emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The two constructs---global exposure and differential functioning---are empirically orthogonal.\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\n\\looseness=-1\nTwo structural controls and a sensitivity check fail to reduce temporal C\\% below 31\\% (\\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\\% $= 38.1\\%$; cross-subject C\\% is more conservative due to lower local dependence), and IRT $\\theta$-conditioning ($r(\\theta, \\mathrm{total\\ score}) = 0.9986$). Logistic regression on nine subjects (1{,}787 items; 9/57---full-benchmark rates require further analysis) detects an additional 17.7\\% with non-uniform DIF ($|\\beta_{\\mathrm{interaction}}| \\geq 0.5$; effect-size criterion; LR $p$-values not adjusted for clustering); the union reaches 47\\% (Jaccard $= 0.28$): ${\\approx}$27--29\\% uniform (MH) plus 17.7\\% non-uniform (interaction-only), mutually exclusive by construction. Ability-matched analysis yields C\\% $= 28.9\\%$ (temporal) and $28.3\\%$ (Llama-2 vs.\\ 3)---consistent matched values (${\\sim}$28--29\\%) despite vastly different unmatched rates (\\Cref{app:structural}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\\% below 31\\%; $\\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}\n\\label{tab:structural_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temp.\\ C\\% & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (ext.) & Cross-bench.\\ total score & $0.314_{\\pm.009}$ & $0.834_{\\pm.027}$ & Reference \\\\\nMatched-ability & Within-quintile temp.\\ DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-cond.\\ (sens.) & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\n\\looseness=-1\nCross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$, upper-bound estimate under uniform binary flipping; \\Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ on average. The $\\Delta\\mathrm{FPR} = 0$ guarantee holds for single-subject contamination ($k \\leq 5$, $\\Delta\\mathrm{FPR} < 0.007$). Under broader contamination spanning $k = 10$ subjects (18\\% of domains), $\\Delta\\mathrm{FPR}$ rises to $0.047 \\pm 0.022$; at $k = 20$, to $0.069 \\pm 0.018$ (\\Cref{tab:multi_subject_injection,app:fig_matching}). Even worst-case multi-subject inflation ($\\sim$7~pp) cannot account for the observed 31\\% C\\% rate, which exceeds the 0.18\\% random baseline by ${>}170\\times$. Under DEFF adjustment, worst-case $\\Delta\\mathrm{FPR}$ at $k{=}20$ (0.069) represents up to 50\\% of the 13.5\\% lower bound, underscoring $k \\leq 5$ in practice. Difficulty-dependent injection produces distinguishable $\\rho$ signatures (capability-like: $+0.77$ vs.\\ contamination-like: $-0.52$; zero seed overlap), though mapping to real-data mechanisms requires further work.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\n\\looseness=-1\nStable-item ranks are preserved across all six benchmarks ($\\rho = 0.997$, $\\tau = 0.958$; flip rate $\\leq 2.8\\%$; \\Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\\ random removal; \\Cref{app:fig_downstream}). Among the 200 most displaced models (top 3.8\\%), 33.6\\% of pairwise rankings reverse, concentrating among closely-ranked pairs (35.2\\% at $\\Delta\\mathrm{rank} < 50$ vs.\\ 0.0\\% above 1000; \\Cref{app:rank_reversal}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\\times$ random; $p < 0.001$).\n\n\\subsection{Cross-Benchmark Validation}\n\\label{sec:gsm8k}\n\n\\looseness=-1\nTemporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six METABENCH benchmarks. C\\% = ETS~C items ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) between 2023 and 2024 cohorts; $\\rho$/$\\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\\%/Rand.\\ C\\%, with baseline varying by benchmark. All six show substantial DIF (45--174$\\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\\% than procedural ones.}\n\\label{tab:cross_benchmark}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrl}\n\\toprule\nBenchmark & Items & C\\% & $\\rho$ & $\\tau$ & Flip\\% & Rand.\\ C\\% & Ratio \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.18 & 174$\\times$ \\\\\nWinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\\times$ \\\\\nARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSemi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}). As an exploratory cross-benchmark signal, GSM1K contamination gaps correlate with DIF-C item accuracy ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{app:fig_gsm1k}), but the small sample requires replication.\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T22:34:31.754Z_

<details><summary>↩ Tool result · `toolu_01VEfSPJyuvuF3Dn7T8q9VtC`</summary>

```text
Web search results for query: "ARR Responsible NLP Research Checklist 2025 2026 questions"

Links: [{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Responsible NLP Research Checklist","url":"https://aclrollingreview.org/static/responsibleNLPresearch.pdf"},{"title":"Responsible NLP Research Checklist","url":"https://arxiv.org/html/2308.06385v2"},{"title":"Responsible NLP Checklist","url":"https://aclanthology.org/attachments/2025.findings-emnlp.877.checklist.pdf"},{"title":"ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses","url":"https://arxiv.org/pdf/2408.04675"}]

Based on the search results, I found information about the ARR Responsible NLP Research Checklist. Here's what I found:

The ARR Responsible NLP Research checklist is designed to encourage best practices for responsible research, addressing issues of research ethics, societal impact and reproducibility.

For each question, if you answer Yes, provide the section number; if you answer No, provide a justification. Note that not answering positively to a question is not grounds for rejection.

The checklist covers several key areas:
- **Computational Experiments:** Including reporting number of parameters, computational budget (GPU hours), computing infrastructure, experimental setup details, descriptive statistics, and implementation settings for packages used.
- **Human Annotators and Research Subjects:** Questions about using crowdworkers or research involving human subjects.
- **AI Writing Assistance:** Questions about the use of AI tools in writing the paper.

At EMNLP'25 the checklist will be published as an appendix to accepted papers, and starting from December 2024 inappropriately filled checklist can be considered grounds for desk rejection.

The official detailed explanation and full questions are available at the ACL Rolling Review (ARR) website and in their official documentation. If you need to see the complete list of specific questions, you can access the full checklist PDF from the aclrollingreview.org domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "8c699a34-c51f-4dff-a94a-1b2b8e5727e1",
  "tool_use_result": {
    "query": "ARR Responsible NLP Research Checklist 2025 2026 questions",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DSNonWzDmPzn6yEhpDy4Wk",
        "content": [
          {
            "title": "Authors Beware: Common Submission Problems",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "Responsible NLP Research Checklist",
            "url": "https://aclrollingreview.org/static/responsibleNLPresearch.pdf"
          },
          {
            "title": "Responsible NLP Research Checklist",
            "url": "https://arxiv.org/html/2308.06385v2"
          },
          {
            "title": "Responsible NLP Checklist",
            "url": "https://aclanthology.org/attachments/2025.findings-emnlp.877.checklist.pdf"
          },
          {
            "title": "ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses",
            "url": "https://arxiv.org/pdf/2408.04675"
          }
        ]
      },
      "Based on the search results, I found information about the ARR Responsible NLP Research Checklist. Here's what I found:\n\nThe ARR Responsible NLP Research checklist is designed to encourage best practices for responsible research, addressing issues of research ethics, societal impact and reproducibility.\n\nFor each question, if you answer Yes, provide the section number; if you answer No, provide a justification. Note that not answering positively to a question is not grounds for rejection.\n\nThe checklist covers several key areas:\n- **Computational Experiments:** Including reporting number of parameters, computational budget (GPU hours), computing infrastructure, experimental setup details, descriptive statistics, and implementation settings for packages used.\n- **Human Annotators and Research Subjects:** Questions about using crowdworkers or research involving human subjects.\n- **AI Writing Assistance:** Questions about the use of AI tools in writing the paper.\n\nAt EMNLP'25 the checklist will be published as an appendix to accepted papers, and starting from December 2024 inappropriately filled checklist can be considered grounds for desk rejection.\n\nThe official detailed explanation and full questions are available at the ACL Rolling Review (ARR) website and in their official documentation. If you need to see the complete list of specific questions, you can access the full checklist PDF from the aclrollingreview.org domain."
    ],
    "durationSeconds": 6.446805408
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the actual ARR checklist PDF to get the exact questions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "fec52a5f-8cc2-45e4-ac18-f2889c809f31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFDMVjySdQjHXrq1VAH3wg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7047,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 25949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 893
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

_source line 17_

Let me fetch the actual checklist document to get the exact questions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "0342986d-ce14-4a9d-bc5b-3dcc9d3d9b38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFDMVjySdQjHXrq1VAH3wg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7047,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 25949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 893
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

_source line 18_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MMPgrj3cUSZdavna9u2Cfv`</summary>

```json
{
  "url": "https://aclrollingreview.org/static/responsibleNLPresearch.pdf",
  "prompt": "Extract ALL questions from the ARR Responsible NLP Research Checklist. List every section (A, B, C, D, E, F) and every question with its exact number and text. Include any sub-questions. Be comprehensive - I need every single question."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "0bcf1904-0efe-49e6-a76b-23bdf8d15e92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFDMVjySdQjHXrq1VAH3wg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7047,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 25949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 893
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

_source line 19_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HZVpzHzUs7ZsKnwNZ1PMGN`</summary>

```json
{
  "url": "https://aclrollingreview.org/authorchecklist",
  "prompt": "Extract the complete list of ALL questions from the ARR Responsible NLP Research Checklist. Include section names, question numbers, exact question text, and any guidance notes. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "7216a736-d61d-4bba-abd5-cffb3efc04c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFDMVjySdQjHXrq1VAH3wg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7047,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 25949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 893
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

_source line 20 · 2026-05-22T22:34:41.535Z_

<details><summary>↩ Tool result · `toolu_01MMPgrj3cUSZdavna9u2Cfv`</summary>

```text
I appreciate your request, but I cannot complete this task as specified. The document provided appears to be a PDF file in raw binary format, not readable text. The content shown consists of PDF object streams with compressed/encoded data that would require proper decompilation to access the actual checklist questions.

To extract the ARR Responsible NLP Research Checklist questions accurately, I would need:

1. A properly rendered text version of the document, or
2. A PDF that can be parsed to readable text, or
3. Direct access to the checklist in a text-based format

If you have access to the original checklist document, I'd be happy to extract all section headers and questions from Sections A through F with their exact numbering, keeping within your 125-character quote limit and using proper attribution.

Would you be able to provide the content in a more accessible format?

[Binary content (application/pdf, 107KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/cd3367d5-3401-489b-aac6-a7bde6f12fd6/tool-results/webfetch-1779489278003-uluj4j.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "d6e5b109-b36a-4b7c-9273-8f3a0934799c",
  "tool_use_result": {
    "bytes": 109565,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I cannot complete this task as specified. The document provided appears to be a PDF file in raw binary format, not readable text. The content shown consists of PDF object streams with compressed/encoded data that would require proper decompilation to access the actual checklist questions.\n\nTo extract the ARR Responsible NLP Research Checklist questions accurately, I would need:\n\n1. A properly rendered text version of the document, or\n2. A PDF that can be parsed to readable text, or\n3. Direct access to the checklist in a text-based format\n\nIf you have access to the original checklist document, I'd be happy to extract all section headers and questions from Sections A through F with their exact numbering, keeping within your 125-character quote limit and using proper attribution.\n\nWould you be able to provide the content in a more accessible format?\n\n[Binary content (application/pdf, 107KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/cd3367d5-3401-489b-aac6-a7bde6f12fd6/tool-results/webfetch-1779489278003-uluj4j.pdf]",
    "durationMs": 4018,
    "url": "https://aclrollingreview.org/static/responsibleNLPresearch.pdf"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T22:34:42.611Z_

<details><summary>↩ Tool result · `toolu_01HZVpzHzUs7ZsKnwNZ1PMGN`</summary>

```text
I appreciate your detailed request, but I need to be transparent: **the webpage content provided does not contain the complete Responsible NLP Research Checklist itself.**

The page references the checklist and states: "Our submission form includes the responsible NLP research checklist (detailed explanation of all its questions is available [here](/responsibleNLPresearch))."

However, the actual checklist questions are located on a separate page (`/responsibleNLPresearch`) that wasn't included in the content you provided.

**What I can tell you from this page:**

The document mentions the checklist covers topics including:
- "ethics and reproducibility"
- Generative AI usage (with reference to ACL policy on authorship)
- Questions where authors sometimes inappropriately respond with just "yes" without relevant justification

**To get the complete checklist**, you would need to:
1. Visit the linked `/responsibleNLPresearch` page directly
2. Review the actual ARR submission form on OpenReview
3. Consult the ARR website's guidelines section

I can only extract and quote from content you provide, and the actual checklist questions aren't in your source material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "a4f182f2-28d5-4454-8dc9-e706d5ff1e82",
  "tool_use_result": {
    "bytes": 27619,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your detailed request, but I need to be transparent: **the webpage content provided does not contain the complete Responsible NLP Research Checklist itself.**\n\nThe page references the checklist and states: \"Our submission form includes the responsible NLP research checklist (detailed explanation of all its questions is available [here](/responsibleNLPresearch)).\"\n\nHowever, the actual checklist questions are located on a separate page (`/responsibleNLPresearch`) that wasn't included in the content you provided.\n\n**What I can tell you from this page:**\n\nThe document mentions the checklist covers topics including:\n- \"ethics and reproducibility\"\n- Generative AI usage (with reference to ACL policy on authorship)\n- Questions where authors sometimes inappropriately respond with just \"yes\" without relevant justification\n\n**To get the complete checklist**, you would need to:\n1. Visit the linked `/responsibleNLPresearch` page directly\n2. Review the actual ARR submission form on OpenReview\n3. Consult the ARR website's guidelines section\n\nI can only extract and quote from content you provide, and the actual checklist questions aren't in your source material.",
    "durationMs": 3833,
    "url": "https://aclrollingreview.org/authorchecklist"
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me try fetching the responsibleNLPresearch page and also the arxiv paper that describes the checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "266d77a5-6ac5-4d8c-b096-0602228f7280",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvUb8hj99iUCyRpL4anZHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7956,
      "cache_read_input_tokens": 26842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7956
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ub9SvnrrZQw9WZXt8NoPxN`</summary>

```json
{
  "url": "https://aclrollingreview.org/responsibleNLPresearch",
  "prompt": "Extract ALL questions from the ARR Responsible NLP Research Checklist. List every section (A, B, C, D, E, F) and every question number, exact text, and sub-questions. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "4bd4ae26-4396-4c74-94eb-716d0a586cc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvUb8hj99iUCyRpL4anZHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7956,
      "cache_read_input_tokens": 26842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7956
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

_source line 24_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W2eJJiaJoDMAQAQcmQDhMw`</summary>

```json
{
  "url": "https://arxiv.org/html/2308.06385v2",
  "prompt": "Extract ALL questions from the ARR Responsible NLP Research Checklist. List every section (A, B, C, D, E, F) and every question number, exact question text. Be comprehensive - I need every single question and its section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "ee3a7cb5-1454-44be-82a9-69dcda9c65c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvUb8hj99iUCyRpL4anZHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7956,
      "cache_read_input_tokens": 26842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7956
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

_source line 25 · 2026-05-22T22:34:54.248Z_

<details><summary>↩ Tool result · `toolu_01W2eJJiaJoDMAQAQcmQDhMw`</summary>

```text
# ARR Responsible NLP Research Checklist - All Questions

## Section A: For Every Submission

**A1:** "Did you discuss the limitations of your work?"

**A2:** "Did you discuss any potential risks of your work?"

**A3:** "Do the abstract and introduction summarize the paper's main claims?"

## Section B: Scientific Artifacts

**B1:** "Did you cite the creators of artifacts you used?"

**B2:** "Did you discuss the license or terms for use and/or distribution of any artifacts?"

**B3:** Did you discuss consistency of use with intended purposes and specify intended use for created artifacts?

**B4:** Did you discuss checks for personally identifiable information, offensive content, and anonymization steps?

**B5:** "Did you provide documentation of the artifacts, e.g., coverage of domains, languages, and linguistic phenomena, demographic groups represented, etc.?"

**B6:** "Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc. for the data that you used/created?"

## Section C: Computational Experiments

**C1:** Did you report model parameters, total computational budget (GPU hours), and infrastructure?

**C2:** "Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?"

**C3:** Did you report descriptive statistics (error bars, summaries) with transparency about max/mean reporting?

**C4:** "If you used existing packages (e.g., for preprocessing, for normalization, or for evaluation), did you report the implementation, model, and parameter settings used?"

## Section D: Human Annotators/Subjects

**D1:** "Did you report the full text of instructions given to participants, including e.g., screenshots, disclaimers of any risks to participants or annotators, etc.?"

**D2:** Did you report recruitment methods, participant payment, and adequacy discussion by demographics?

**D3:** "Did you discuss whether and how consent was obtained from people whose data you're using/curating?"

**D4:** "Was the data collection protocol approved (or determined exempt) by an ethics review board?"

**D5:** "Did you report the basic demographic and geographic characteristics of the annotator population?"

## Section E: AI Assistants

**E1:** "Did you include information about your use of AI assistants?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "eb929ab4-1b8e-4913-a73f-84ed5f59331a",
  "tool_use_result": {
    "bytes": 61560,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Responsible NLP Research Checklist - All Questions\n\n## Section A: For Every Submission\n\n**A1:** \"Did you discuss the limitations of your work?\"\n\n**A2:** \"Did you discuss any potential risks of your work?\"\n\n**A3:** \"Do the abstract and introduction summarize the paper's main claims?\"\n\n## Section B: Scientific Artifacts\n\n**B1:** \"Did you cite the creators of artifacts you used?\"\n\n**B2:** \"Did you discuss the license or terms for use and/or distribution of any artifacts?\"\n\n**B3:** Did you discuss consistency of use with intended purposes and specify intended use for created artifacts?\n\n**B4:** Did you discuss checks for personally identifiable information, offensive content, and anonymization steps?\n\n**B5:** \"Did you provide documentation of the artifacts, e.g., coverage of domains, languages, and linguistic phenomena, demographic groups represented, etc.?\"\n\n**B6:** \"Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc. for the data that you used/created?\"\n\n## Section C: Computational Experiments\n\n**C1:** Did you report model parameters, total computational budget (GPU hours), and infrastructure?\n\n**C2:** \"Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?\"\n\n**C3:** Did you report descriptive statistics (error bars, summaries) with transparency about max/mean reporting?\n\n**C4:** \"If you used existing packages (e.g., for preprocessing, for normalization, or for evaluation), did you report the implementation, model, and parameter settings used?\"\n\n## Section D: Human Annotators/Subjects\n\n**D1:** \"Did you report the full text of instructions given to participants, including e.g., screenshots, disclaimers of any risks to participants or annotators, etc.?\"\n\n**D2:** Did you report recruitment methods, participant payment, and adequacy discussion by demographics?\n\n**D3:** \"Did you discuss whether and how consent was obtained from people whose data you're using/curating?\"\n\n**D4:** \"Was the data collection protocol approved (or determined exempt) by an ethics review board?\"\n\n**D5:** \"Did you report the basic demographic and geographic characteristics of the annotator population?\"\n\n## Section E: AI Assistants\n\n**E1:** \"Did you include information about your use of AI assistants?\"",
    "durationMs": 7212,
    "url": "https://arxiv.org/html/2308.06385v2"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T22:34:58.677Z_

<details><summary>↩ Tool result · `toolu_01Ub9SvnrrZQw9WZXt8NoPxN`</summary>

```text
# ARR Responsible NLP Research Checklist - Complete Question Extraction

## Section A: For Every Submission

**A1. Did you describe the limitations of your work?**
- Point out strong assumptions and robustness to violations
- Reflect on scope of claims (datasets, languages, runs)
- Discuss model bias definitions explicitly if analyzed
- Acknowledge limitations transparently

**A2. Did you discuss any potential risks of your work?**
- Malicious/unintended harmful effects (disinformation, surveillance, etc.)
- Environmental impact from computational requirements
- Fairness and deployment considerations
- Privacy and security concerns
- Overgeneralization and bias confirmation
- Impact on different stakeholder groups
- Dual-use scenarios and mitigation strategies

---

## Section B: Scientific Artifacts

**B1. Did you cite the creators of artifacts you used?**
- Include all creators of composite artifacts
- Cite original papers for code/datasets
- State version numbers
- Provide URLs when possible

**B2. Did you discuss the license or terms for use/distribution of artifacts?**
- Name specific licenses (e.g., CC-BY 4.0)
- State copyright and terms of service for scraped data
- Clarify consent status
- Include license information for released assets
- Document original and derived licenses

**B3. Did you discuss if your use of existing artifacts was consistent with intended use?**
- Ensure license compatibility with access conditions
- Specify intended use for created artifacts
- Discuss anonymization adequacy
- Address harms from data collection limitations

**B4. Did you discuss steps to check for identifying information or offensive content?**
- Explain checking methodology
- Describe anonymization methods
- List privacy protection measures
- Address identifiability risks

**B5. Did you provide documentation of artifacts?**
- Report language of language data
- Describe domain and demographic information
- Use data statements, model cards, or datasheets

**B6. Did you report relevant statistics like example counts and splits?**
- Include train/validation/test split sizes
- Provide context for all benchmark datasets

---

## Section C: Computational Experiments

**C1. Did you report parameter counts, computational budget, and infrastructure?**
- State model parameter numbers
- Report GPU hours or equivalent metrics
- Describe computing hardware specifications
- Include all experiment runs, not just final results

**C2. Did you discuss experimental setup, hyperparameter search, and best values?**
- Explain model selection methodology
- Document hyperparameter tuning processes
- Report best-found hyperparameter values
- Clarify which dataset was used for tuning

**C3. Did you report descriptive statistics and result transparency?**
- Include error bars or confidence intervals
- Clarify if reporting max, mean, or single runs
- Report validation performance alongside test results

**C4. If using existing packages, did you report implementation details?**
- State version numbers or implementation references
- Cite original work or provide URLs
- Explain any library modifications

---

## Section D: Human Annotators/Participants

**D1. Did you report full text of instructions to participants?**
- Include screenshots and disclaimers
- Warn of risks to participants or annotators

**D2. Did you report recruitment methods, payment, and adequacy?**
- Specify crowdsourcing platforms or recruitment sources
- Report compensation amounts and fairness discussion
- Include wage determination methodology

**D3. Did you discuss consent from data sources?**
- Explain how consent was obtained or documented

**D4. Was data collection approved by ethics review board?**
- State IRB or equivalent board approval
- Note exemption determinations

**D5. Did you report demographic/geographic characteristics of annotators?**
- Describe annotator population characteristics
- Provide data statements per Bender and Friedman (2018)
- Clarify self-reported versus inferred characteristics

---

## Section E: AI Assistants

**E1. If you used AI assistants, did you include information about your use?**
- Disclose all AI assistant usage
- Ensure compliance with authorship criteria

---

**Note:** No Section F appears in this checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "66aef687-cccf-4b19-9a72-9d1997b15bc3",
  "tool_use_result": {
    "bytes": 36573,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Responsible NLP Research Checklist - Complete Question Extraction\n\n## Section A: For Every Submission\n\n**A1. Did you describe the limitations of your work?**\n- Point out strong assumptions and robustness to violations\n- Reflect on scope of claims (datasets, languages, runs)\n- Discuss model bias definitions explicitly if analyzed\n- Acknowledge limitations transparently\n\n**A2. Did you discuss any potential risks of your work?**\n- Malicious/unintended harmful effects (disinformation, surveillance, etc.)\n- Environmental impact from computational requirements\n- Fairness and deployment considerations\n- Privacy and security concerns\n- Overgeneralization and bias confirmation\n- Impact on different stakeholder groups\n- Dual-use scenarios and mitigation strategies\n\n---\n\n## Section B: Scientific Artifacts\n\n**B1. Did you cite the creators of artifacts you used?**\n- Include all creators of composite artifacts\n- Cite original papers for code/datasets\n- State version numbers\n- Provide URLs when possible\n\n**B2. Did you discuss the license or terms for use/distribution of artifacts?**\n- Name specific licenses (e.g., CC-BY 4.0)\n- State copyright and terms of service for scraped data\n- Clarify consent status\n- Include license information for released assets\n- Document original and derived licenses\n\n**B3. Did you discuss if your use of existing artifacts was consistent with intended use?**\n- Ensure license compatibility with access conditions\n- Specify intended use for created artifacts\n- Discuss anonymization adequacy\n- Address harms from data collection limitations\n\n**B4. Did you discuss steps to check for identifying information or offensive content?**\n- Explain checking methodology\n- Describe anonymization methods\n- List privacy protection measures\n- Address identifiability risks\n\n**B5. Did you provide documentation of artifacts?**\n- Report language of language data\n- Describe domain and demographic information\n- Use data statements, model cards, or datasheets\n\n**B6. Did you report relevant statistics like example counts and splits?**\n- Include train/validation/test split sizes\n- Provide context for all benchmark datasets\n\n---\n\n## Section C: Computational Experiments\n\n**C1. Did you report parameter counts, computational budget, and infrastructure?**\n- State model parameter numbers\n- Report GPU hours or equivalent metrics\n- Describe computing hardware specifications\n- Include all experiment runs, not just final results\n\n**C2. Did you discuss experimental setup, hyperparameter search, and best values?**\n- Explain model selection methodology\n- Document hyperparameter tuning processes\n- Report best-found hyperparameter values\n- Clarify which dataset was used for tuning\n\n**C3. Did you report descriptive statistics and result transparency?**\n- Include error bars or confidence intervals\n- Clarify if reporting max, mean, or single runs\n- Report validation performance alongside test results\n\n**C4. If using existing packages, did you report implementation details?**\n- State version numbers or implementation references\n- Cite original work or provide URLs\n- Explain any library modifications\n\n---\n\n## Section D: Human Annotators/Participants\n\n**D1. Did you report full text of instructions to participants?**\n- Include screenshots and disclaimers\n- Warn of risks to participants or annotators\n\n**D2. Did you report recruitment methods, payment, and adequacy?**\n- Specify crowdsourcing platforms or recruitment sources\n- Report compensation amounts and fairness discussion\n- Include wage determination methodology\n\n**D3. Did you discuss consent from data sources?**\n- Explain how consent was obtained or documented\n\n**D4. Was data collection approved by ethics review board?**\n- State IRB or equivalent board approval\n- Note exemption determinations\n\n**D5. Did you report demographic/geographic characteristics of annotators?**\n- Describe annotator population characteristics\n- Provide data statements per Bender and Friedman (2018)\n- Clarify self-reported versus inferred characteristics\n\n---\n\n## Section E: AI Assistants\n\n**E1. If you used AI assistants, did you include information about your use?**\n- Disclose all AI assistant usage\n- Ensure compliance with authorship criteria\n\n---\n\n**Note:** No Section F appears in this checklist.",
    "durationMs": 12318,
    "url": "https://aclrollingreview.org/responsibleNLPresearch"
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of both the checklist questions and the paper content. Let me also check if there's an A3 question that the arxiv source mentions but the main page doesn't. The arxiv version mentions A3: "Do the abstract and introduction summarize the paper's main claims?" Let me include this.

Now let me also check the paper's abstract to be complete.

Actually, I have enough information now to draft the checklist. Let me write it.

Key information about the paper:
- Pure statistical analysis work (MH-DIF analysis)
- Uses METABENCH public dataset (5227 models × 12508 items)


- Code available at anonymous.4open.science/r/dif-audit
- Computationally lightweight (under 100 CPU-hours, CPU-only)
- No human subjects or new data collection involved
- Already includes three documented limitations
- Low-risk analytical study

Now I'm ready to compose the checklist draft.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "bde40564-6209-499f-9cba-5cd3885855aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aceSFxboCa9F2BtwQqLH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 561,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 34798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1377
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

_source line 28_

Now I have all the information needed. Let me write the checklist draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "fcf4f1a4-b69b-4747-9f30-aede6804ecbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aceSFxboCa9F2BtwQqLH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 561,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 34798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1377
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

_source line 29_

<details open><summary>🔧 Tool call — Write · `toolu_01WDJ7q7G8jTKiP5GJ5u33tg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/arr_checklist_draft.md",
  "content": "# ARR Responsible NLP Research Checklist — Draft Answers\n\n> 基于论文内容拟定，供用户在 OpenReview submission form 中参考填写。\n> 论文：*Psychometric Auditing of LLM Benchmarks via Mantel-Haenszel Differential Item Functioning*\n\n---\n\n## Section A: For Every Submission\n\n### A1. Did you describe the limitations of your work?\n**Answer**: Yes\n**Justification**: The paper includes a dedicated Limitations section (unnumbered, after §5) covering three points: (1) the semi-synthetic framework uses uniform binary flipping as a worst-case injection model, so reported ΔTPR values are upper-bound estimates; (2) the MH χ² test assumes independent examinees, which LLM model families violate — three convergent corrections and family-level cluster bootstrap bound the impact; (3) cross-subject matching assumes contamination affects a minority of domains, with ΔFPR rising under broad contamination.\n\n### A2. Did you discuss any potential risks of your work?\n**Answer**: Yes\n**Justification**: This is a purely analytical/diagnostic study applying classical psychometric methods (MH-DIF) to publicly available benchmark response data. The work identifies measurement instability in existing benchmarks but does not produce models, generate text, or create tools that could be directly misused. The primary risk is misinterpretation of DIF flags as definitive contamination evidence; the paper explicitly states that \"DIF detects *that* items function differently but cannot determine *why*\" (Limitations) and frames DIF as \"a diagnostic lens rather than a quality filter\" (§1). No dual-use or harmful application risks identified.\n\n### A3. Do the abstract and introduction summarize the paper's main claims?\n**Answer**: Yes\n**Justification**: The introduction (§1) explicitly enumerates three contributions: (1) empirical demonstration that web-overlap labels and DIF flags are near-independent (orthogonal constructs), (2) a temporal DIF audit framework with cross-subject matching, clustering, and DEFF correction, and (3) temporal measurement instability at scale (~27–29% of MMLU items). The abstract summarizes these findings with key quantitative results.\n\n---\n\n## Section B: Scientific Artifacts\n\n### B1. Did you cite the creators of artifacts you used?\n**Answer**: Yes\n**Justification**: All artifacts are cited: METABENCH (Kipnis, 2024), MMLU (Hendrycks et al., 2021), GSM8K, HellaSwag (Zellers et al., 2019), ARC, WinoGrande, TruthfulQA, PSN-IRT (Zhou et al., 2026), and the web-overlap contamination labels (Li et al., 2024). The ETS classification system and MH method (Holland & Thayer, 1988) are also cited.\n\n### B2. Did you discuss the license or terms for use and/or distribution of any artifacts?\n**Answer**: No\n**Justification**: The paper does not explicitly discuss licenses of the datasets used. METABENCH is publicly available; MMLU uses MIT license. The analysis code is released at an anonymous repository. 建议：可以在 camera-ready 版的 Appendix 或 Ethics Statement 中补充数据集 license 信息（METABENCH: Apache 2.0, MMLU: MIT 等），但 checklist 中回答 No 并附理由即可，这不是 rejection ground。\n\n### B3. Did you discuss if your use of existing artifacts was consistent with their intended use?\n**Answer**: Yes\n**Justification**: METABENCH was created as a unified response matrix for cross-benchmark analysis of LLMs — our DIF analysis directly serves this purpose. MMLU and other benchmarks are used for their original evaluation purpose. Our use (psychometric auditing of item functioning) is a natural extension of benchmark evaluation.\n\n### B4. Did you discuss if the data contains personally identifiable information or offensive content?\n**Answer**: N/A\n**Justification**: The data consists entirely of binary (correct/incorrect) response matrices from LLM evaluations on public benchmarks. No human subjects, no personally identifiable information, and no user-generated content are involved. The benchmark items themselves are from established academic datasets.\n\n### B5. Did you provide documentation of the artifacts, e.g., coverage of domains, languages, and linguistic phenomena?\n**Answer**: Yes\n**Justification**: §2 and §4 describe the METABENCH dataset dimensions (5,227 models × 12,508 MMLU items), temporal cohort definitions (2023 vs. 2024 by release date, N_ref=1,080, N_focal=807), and cross-benchmark coverage (6 benchmarks with item counts in Table 5). MMLU's 57-subject domain structure is discussed with subject-level DIF rates.\n\n### B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?\n**Answer**: Yes\n**Justification**: Full dataset statistics are reported: total items per benchmark (Table 5), cohort sizes (§4.2), model family counts, and semi-synthetic validation parameters. There are no train/test/dev splits as this is a statistical analysis, not a machine learning training task.\n\n---\n\n## Section C: Computational Experiments\n\n### C1. Did you report the number of parameters in each model, the total computational budget, and computing infrastructure?\n**Answer**: Partial\n**Justification**: This work does not train or fine-tune any models; it performs statistical analysis (MH-DIF, bootstrap, permutation tests) on existing response matrices. No model parameters are relevant. The computational budget is modest (pure CPU computation; estimated <100 CPU-hours for all analyses including bootstrap CIs and permutation tests). 建议：在 camera-ready 中可在 Appendix 补充一句 \"All analyses were performed on CPU; total compute was approximately X CPU-hours on [hardware spec].\"\n\n### C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?\n**Answer**: Yes\n**Justification**: Key methodological parameters are specified: ETS C threshold (|Δ_MH| ≥ 1.5, p < 0.05), number of ability strata (K=5 as primary, with K=3,10 sensitivity), bootstrap replications, Monte Carlo power analysis parameters (1,000 replications), nearest-neighbor matching criteria, and semi-synthetic injection rates. No hyperparameter search was conducted as the method uses established psychometric thresholds.\n\n### C3. Did you report descriptive statistics about your results with transparency about max/mean reporting?\n**Answer**: Yes\n**Justification**: Results include bootstrap 95% CIs (e.g., C% CI [29.4%, 38.1%]), family-level cluster bootstrap CIs ([26.7%, 53.2%]), DEFF correction ranges (13.5%–29.2%), standard deviations for semi-synthetic results, permutation p-values, and effect sizes (Cohen's d, φ, Jaccard, OR with CIs). Multiple convergent estimates are reported rather than cherry-picked single values.\n\n### C4. If you used existing packages, did you report the implementation, model, and parameter settings used?\n**Answer**: Partial\n**Justification**: The MH-DIF method is fully described with equations and references (Holland & Thayer, 1988). ETS classification criteria are specified. PSN-IRT parameters are cited (Zhou et al., 2026). The analysis code is available at anonymous.4open.science/r/dif-audit. 建议：camera-ready 可在代码仓库的 README 或 requirements.txt 中列出 Python 包版本。\n\n---\n\n## Section D: Human Annotators/Participants\n\n### D1. Did you report the full text of instructions given to participants?\n**Answer**: N/A\n**Justification**: No human participants or annotators were involved in this study. The analysis uses only pre-existing LLM response data from METABENCH.\n\n### D2. Did you report annotator demographics and payment information?\n**Answer**: N/A\n**Justification**: No human annotators were used.\n\n### D3. Did you discuss whether and how consent was obtained from people whose data you're using/curating?\n**Answer**: N/A\n**Justification**: No human-subject data is used. The data consists entirely of LLM model outputs on public benchmarks.\n\n### D4. Was the data collection protocol approved (or determined exempt) by an ethics review board?\n**Answer**: N/A\n**Justification**: No new data collection involving human subjects was performed. The study analyzes publicly released model evaluation results.\n\n### D5. Did you report the basic demographic and geographic characteristics of the annotator population?\n**Answer**: N/A\n**Justification**: No human annotators involved.\n\n---\n\n## Section E: AI Assistants\n\n### E1. Did you include information about your use of AI assistants?\n**Answer**: Yes / No（根据实际情况选择）\n**Justification**: 如果使用了 AI 辅助写作（如 Claude、ChatGPT），需如实披露使用方式（e.g., \"AI assistants were used for editing and proofreading; all scientific content, analysis, and claims are the authors' own work.\"）。如果未使用，回答 No 即可。\n\n---\n\n## 填写提示\n\n1. **Checklist 在 OpenReview submission form 中填写**，不需要出现在论文 PDF 中。\n2. 回答 \"No\" 或 \"N/A\" **不构成拒稿理由**，但需要提供合理的 justification。\n3. 上述标注\"建议\"的条目可选择性补充，不影响审稿。\n4. Section E 关于 AI assistant 的回答需要根据实际使用情况如实填写。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "79cee8c1-6b05-47f4-9a1f-0ae9236124b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aceSFxboCa9F2BtwQqLH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 561,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 34798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1377
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

_source line 30 · 2026-05-22T22:36:04.279Z_

<details><summary>↩ Tool result · `toolu_01WDJ7q7G8jTKiP5GJ5u33tg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/arr_checklist_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "85774869-5e50-4c1d-92fd-e6c0121a286f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/arr_checklist_draft.md",
    "content": "# ARR Responsible NLP Research Checklist — Draft Answers\n\n> 基于论文内容拟定，供用户在 OpenReview submission form 中参考填写。\n> 论文：*Psychometric Auditing of LLM Benchmarks via Mantel-Haenszel Differential Item Functioning*\n\n---\n\n## Section A: For Every Submission\n\n### A1. Did you describe the limitations of your work?\n**Answer**: Yes\n**Justification**: The paper includes a dedicated Limitations section (unnumbered, after §5) covering three points: (1) the semi-synthetic framework uses uniform binary flipping as a worst-case injection model, so reported ΔTPR values are upper-bound estimates; (2) the MH χ² test assumes independent examinees, which LLM model families violate — three convergent corrections and family-level cluster bootstrap bound the impact; (3) cross-subject matching assumes contamination affects a minority of domains, with ΔFPR rising under broad contamination.\n\n### A2. Did you discuss any potential risks of your work?\n**Answer**: Yes\n**Justification**: This is a purely analytical/diagnostic study applying classical psychometric methods (MH-DIF) to publicly available benchmark response data. The work identifies measurement instability in existing benchmarks but does not produce models, generate text, or create tools that could be directly misused. The primary risk is misinterpretation of DIF flags as definitive contamination evidence; the paper explicitly states that \"DIF detects *that* items function differently but cannot determine *why*\" (Limitations) and frames DIF as \"a diagnostic lens rather than a quality filter\" (§1). No dual-use or harmful application risks identified.\n\n### A3. Do the abstract and introduction summarize the paper's main claims?\n**Answer**: Yes\n**Justification**: The introduction (§1) explicitly enumerates three contributions: (1) empirical demonstration that web-overlap labels and DIF flags are near-independent (orthogonal constructs), (2) a temporal DIF audit framework with cross-subject matching, clustering, and DEFF correction, and (3) temporal measurement instability at scale (~27–29% of MMLU items). The abstract summarizes these findings with key quantitative results.\n\n---\n\n## Section B: Scientific Artifacts\n\n### B1. Did you cite the creators of artifacts you used?\n**Answer**: Yes\n**Justification**: All artifacts are cited: METABENCH (Kipnis, 2024), MMLU (Hendrycks et al., 2021), GSM8K, HellaSwag (Zellers et al., 2019), ARC, WinoGrande, TruthfulQA, PSN-IRT (Zhou et al., 2026), and the web-overlap contamination labels (Li et al., 2024). The ETS classification system and MH method (Holland & Thayer, 1988) are also cited.\n\n### B2. Did you discuss the license or terms for use and/or distribution of any artifacts?\n**Answer**: No\n**Justification**: The paper does not explicitly discuss licenses of the datasets used. METABENCH is publicly available; MMLU uses MIT license. The analysis code is released at an anonymous repository. 建议：可以在 camera-ready 版的 Appendix 或 Ethics Statement 中补充数据集 license 信息（METABENCH: Apache 2.0, MMLU: MIT 等），但 checklist 中回答 No 并附理由即可，这不是 rejection ground。\n\n### B3. Did you discuss if your use of existing artifacts was consistent with their intended use?\n**Answer**: Yes\n**Justification**: METABENCH was created as a unified response matrix for cross-benchmark analysis of LLMs — our DIF analysis directly serves this purpose. MMLU and other benchmarks are used for their original evaluation purpose. Our use (psychometric auditing of item functioning) is a natural extension of benchmark evaluation.\n\n### B4. Did you discuss if the data contains personally identifiable information or offensive content?\n**Answer**: N/A\n**Justification**: The data consists entirely of binary (correct/incorrect) response matrices from LLM evaluations on public benchmarks. No human subjects, no personally identifiable information, and no user-generated content are involved. The benchmark items themselves are from established academic datasets.\n\n### B5. Did you provide documentation of the artifacts, e.g., coverage of domains, languages, and linguistic phenomena?\n**Answer**: Yes\n**Justification**: §2 and §4 describe the METABENCH dataset dimensions (5,227 models × 12,508 MMLU items), temporal cohort definitions (2023 vs. 2024 by release date, N_ref=1,080, N_focal=807), and cross-benchmark coverage (6 benchmarks with item counts in Table 5). MMLU's 57-subject domain structure is discussed with subject-level DIF rates.\n\n### B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?\n**Answer**: Yes\n**Justification**: Full dataset statistics are reported: total items per benchmark (Table 5), cohort sizes (§4.2), model family counts, and semi-synthetic validation parameters. There are no train/test/dev splits as this is a statistical analysis, not a machine learning training task.\n\n---\n\n## Section C: Computational Experiments\n\n### C1. Did you report the number of parameters in each model, the total computational budget, and computing infrastructure?\n**Answer**: Partial\n**Justification**: This work does not train or fine-tune any models; it performs statistical analysis (MH-DIF, bootstrap, permutation tests) on existing response matrices. No model parameters are relevant. The computational budget is modest (pure CPU computation; estimated <100 CPU-hours for all analyses including bootstrap CIs and permutation tests). 建议：在 camera-ready 中可在 Appendix 补充一句 \"All analyses were performed on CPU; total compute was approximately X CPU-hours on [hardware spec].\"\n\n### C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?\n**Answer**: Yes\n**Justification**: Key methodological parameters are specified: ETS C threshold (|Δ_MH| ≥ 1.5, p < 0.05), number of ability strata (K=5 as primary, with K=3,10 sensitivity), bootstrap replications, Monte Carlo power analysis parameters (1,000 replications), nearest-neighbor matching criteria, and semi-synthetic injection rates. No hyperparameter search was conducted as the method uses established psychometric thresholds.\n\n### C3. Did you report descriptive statistics about your results with transparency about max/mean reporting?\n**Answer**: Yes\n**Justification**: Results include bootstrap 95% CIs (e.g., C% CI [29.4%, 38.1%]), family-level cluster bootstrap CIs ([26.7%, 53.2%]), DEFF correction ranges (13.5%–29.2%), standard deviations for semi-synthetic results, permutation p-values, and effect sizes (Cohen's d, φ, Jaccard, OR with CIs). Multiple convergent estimates are reported rather than cherry-picked single values.\n\n### C4. If you used existing packages, did you report the implementation, model, and parameter settings used?\n**Answer**: Partial\n**Justification**: The MH-DIF method is fully described with equations and references (Holland & Thayer, 1988). ETS classification criteria are specified. PSN-IRT parameters are cited (Zhou et al., 2026). The analysis code is available at anonymous.4open.science/r/dif-audit. 建议：camera-ready 可在代码仓库的 README 或 requirements.txt 中列出 Python 包版本。\n\n---\n\n## Section D: Human Annotators/Participants\n\n### D1. Did you report the full text of instructions given to participants?\n**Answer**: N/A\n**Justification**: No human participants or annotators were involved in this study. The analysis uses only pre-existing LLM response data from METABENCH.\n\n### D2. Did you report annotator demographics and payment information?\n**Answer**: N/A\n**Justification**: No human annotators were used.\n\n### D3. Did you discuss whether and how consent was obtained from people whose data you're using/curating?\n**Answer**: N/A\n**Justification**: No human-subject data is used. The data consists entirely of LLM model outputs on public benchmarks.\n\n### D4. Was the data collection protocol approved (or determined exempt) by an ethics review board?\n**Answer**: N/A\n**Justification**: No new data collection involving human subjects was performed. The study analyzes publicly released model evaluation results.\n\n### D5. Did you report the basic demographic and geographic characteristics of the annotator population?\n**Answer**: N/A\n**Justification**: No human annotators involved.\n\n---\n\n## Section E: AI Assistants\n\n### E1. Did you include information about your use of AI assistants?\n**Answer**: Yes / No（根据实际情况选择）\n**Justification**: 如果使用了 AI 辅助写作（如 Claude、ChatGPT），需如实披露使用方式（e.g., \"AI assistants were used for editing and proofreading; all scientific content, analysis, and claims are the authors' own work.\"）。如果未使用，回答 No 即可。\n\n---\n\n## 填写提示\n\n1. **Checklist 在 OpenReview submission form 中填写**，不需要出现在论文 PDF 中。\n2. 回答 \"No\" 或 \"N/A\" **不构成拒稿理由**，但需要提供合理的 justification。\n3. 上述标注\"建议\"的条目可选择性补充，不影响审稿。\n4. Section E 关于 AI assistant 的回答需要根据实际使用情况如实填写。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 31_

已写入 `artifacts/arr_checklist_draft.md`，覆盖 A1–A3、B1–B6、C1–C4、D1–D5、E1 共 18 项。几个需要你确认的点：

- **B2 (License)**: 建议回答 No 并附理由——纯分析工作中不讨论 license 不是 rejection ground，camera-ready 可补。
- **C1 (Compute)**: 回答 Partial，因为论文未显式写 compute budget。建议 camera-ready 补一句。
- **E1 (AI Assistant)**: 留了占位，需要你根据实际使用情况填写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "uuid": "103881df-fc51-4ecb-a9e8-e4ff8ecfdca9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEnivF7iHkCXqCCti1G22A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3353,
      "cache_read_input_tokens": 36175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3353
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

_source line 32_

已写入 `artifacts/arr_checklist_draft.md`，覆盖 A1–A3、B1–B6、C1–C4、D1–D5、E1 共 18 项。几个需要你确认的点：

- **B2 (License)**: 建议回答 No 并附理由——纯分析工作中不讨论 license 不是 rejection ground，camera-ready 可补。
- **C1 (Compute)**: 回答 Partial，因为论文未显式写 compute budget。建议 camera-ready 补一句。
- **E1 (AI Assistant)**: 留了占位，需要你根据实际使用情况填写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 122294,
  "duration_api_ms": 137375,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "cd3367d5-3401-489b-aac6-a7bde6f12fd6",
  "total_cost_usd": 0.50828925,
  "usage": {
    "input_tokens": 7616,
    "cache_creation_input_tokens": 27687,
    "cache_read_input_tokens": 160371,
    "output_tokens": 4002,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27687,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 190,
        "cache_read_input_tokens": 36175,
        "cache_creation_input_tokens": 3353,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3353
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 95045,
      "outputTokens": 2377,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 1,
      "costUSD": 0.11693000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7616,
      "outputTokens": 4002,
      "cacheReadInputTokens": 160371,
      "cacheCreationInputTokens": 27687,
      "webSearchRequests": 0,
      "costUSD": 0.39135925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b196c76d-1799-4916-b571-6dea3108bacd"
}
```

</details>

---
