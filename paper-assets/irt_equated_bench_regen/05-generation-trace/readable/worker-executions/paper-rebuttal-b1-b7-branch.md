# paper rebuttal b1 b7 branch

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_paper_rebuttal_b1_b7_branch_20260522T204142.log`
- **Structured JSON:** [`f8c15f54f2c8c6878c31.json`](../../sessions/f8/f8c15f54f2c8c6878c31.json)

## Before a recorded user message

70 recorded events

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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_repo_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__search_repo",
    "mcp__agent-ml-research__sync_code_to_remote"
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
  "uuid": "93e2bbb3-f29b-4e06-8992-bcb111c93624",
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
  "uuid": "d9f5789b-e690-41f8-81cf-33be8e0eefa8",
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Create branch `rebuttal-b1-b7` from current HEAD
2. Make 7 independent commits (B1-B7) with specific changes
3. Verify everything at the end

Let me start by creating the branch and reading the necessary files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "1a70dba1-004c-48ea-a2ab-201e97f455ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

Creating the branch and reading all needed files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "2635b72b-3961-46f5-835d-616b5c940d65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_0151YWUmrwAfb6nBJfdks9VB`</summary>

```json
{
  "command": "git checkout -b rebuttal-b1-b7",
  "description": "Create rebuttal-b1-b7 branch from current HEAD"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "0f3e2cda-e9ba-430f-97a1-a1a0a944e490",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 7 · 2026-05-22T20:41:57.769Z_

<details><summary>↩ Tool result · `toolu_0151YWUmrwAfb6nBJfdks9VB`</summary>

```text
Switched to a new branch 'rebuttal-b1-b7'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "03086b28-1275-49e6-bec1-872c5023ae7a",
  "tool_use_result": {
    "stdout": "Switched to a new branch 'rebuttal-b1-b7'",
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

<details open><summary>🔧 Tool call — Read · `toolu_01WFARgACcyK9NVQUz4ZUrvr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "6addeb7c-7be2-4c32-904b-5281b8701323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 9 · 2026-05-22T20:41:58.176Z_

<details><summary>↩ Tool result · `toolu_01WFARgACcyK9NVQUz4ZUrvr`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{20\baselineskip}
4	
5	\subsection{What Drives Temporal DIF?}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}. Three non-exclusive mechanisms may drive the observed ${\approx}$27--29\% rate: (1)~differential contamination; (2)~capability evolution; (3)~training methodology shifts. The ETS baseline of 5--15\% C\%~\citep{clauser1998dif} is for concurrent demographic groups; the comparison to temporal LLM cohorts is illustrative, not normative.
10	
11	\looseness=-1
12	Four exclusion arguments constrain this ambiguity: ability confounds explain at most 2.4~pp (matched C\% $= 28.9\%$; \Cref{sec:temporal}); domain-level improvement explains ${<}0.1\%$ of item-level DIF variance ($R^2 = 0.0007$); no enrichment among expert-annotated errors~\citep{gema2024mmlu} ($= 1.10$, $p = 0.23$); web-overlap labels~\citep{li2024contamination} are near-independent (Jaccard $= 0.206$; \Cref{sec:groundtruth}).
13	
14	\looseness=-1
15	The aggregate difficulty--direction interaction ($\rho = -0.597$, robust at $[0.2, 0.8]$: $\rho = -0.447$, $p < 10^{-100}$; \Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\Cref{sec:semisynthetic}) shows uniform injection also produces $\rho \approx -0.52$ via ceiling effects, while difficulty-dependent injection yields $\rho \approx +0.77$ (zero overlap across seeds); the observed $\rho$ cannot alone distinguish contamination from capability evolution~\citep{suk2026rethinking}. The aggregate $\rho \approx 0.997$ masks subject-level instability (22/57 below 0.95; five below 0.90), motivating targeted replacement~\citep{zhao2025mmlucf,habba2026growingpains}.
16	
17	\looseness=-1
18	Stratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\% reference-favoring with a strong difficulty gradient ($\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\% focal-favoring with a near-zero gradient ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above.
19	
20	\subsection{Recommended DIF Audit Protocol}
21	\label{sec:disc_protocol}
22	
23	\looseness=-1
24	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\geq$500 models accumulate (ensuring $\geq$80 per stratum at $K{=}5$; \Cref{sec:validation}), with three action levels (calibrate via $\rho$-degradation; \Cref{app:fig_rho_degradation}): \emph{Monitor} (C\% $< 15\%$), \emph{Flag} ($15$--$25\%$: dual rankings), \emph{Act} ($\geq 25\%$: stable-item rankings). Difficulty--direction and model-type signals (\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\Cref{app:fig_downstream}), motivating equating~\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\rho = 0.95$).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "e4c3f3d6-133c-482f-88ee-128dbedc870a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\\enlargethispage*{20\\baselineskip}\n\n\\subsection{What Drives Temporal DIF?}\n\\label{sec:disc_temporal}\n\n\\looseness=-1\nTemporal DIF detects \\emph{that} items function differently across cohorts, not \\emph{why}. Three non-exclusive mechanisms may drive the observed ${\\approx}$27--29\\% rate: (1)~differential contamination; (2)~capability evolution; (3)~training methodology shifts. The ETS baseline of 5--15\\% C\\%~\\citep{clauser1998dif} is for concurrent demographic groups; the comparison to temporal LLM cohorts is illustrative, not normative.\n\n\\looseness=-1\nFour exclusion arguments constrain this ambiguity: ability confounds explain at most 2.4~pp (matched C\\% $= 28.9\\%$; \\Cref{sec:temporal}); domain-level improvement explains ${<}0.1\\%$ of item-level DIF variance ($R^2 = 0.0007$); no enrichment among expert-annotated errors~\\citep{gema2024mmlu} ($= 1.10$, $p = 0.23$); web-overlap labels~\\citep{li2024contamination} are near-independent (Jaccard $= 0.206$; \\Cref{sec:groundtruth}).\n\n\\looseness=-1\nThe aggregate difficulty--direction interaction ($\\rho = -0.597$, robust at $[0.2, 0.8]$: $\\rho = -0.447$, $p < 10^{-100}$; \\Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\\Cref{sec:semisynthetic}) shows uniform injection also produces $\\rho \\approx -0.52$ via ceiling effects, while difficulty-dependent injection yields $\\rho \\approx +0.77$ (zero overlap across seeds); the observed $\\rho$ cannot alone distinguish contamination from capability evolution~\\citep{suk2026rethinking}. The aggregate $\\rho \\approx 0.997$ masks subject-level instability (22/57 below 0.95; five below 0.90), motivating targeted replacement~\\citep{zhao2025mmlucf,habba2026growingpains}.\n\n\\looseness=-1\nStratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring with a strong difficulty gradient ($\\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\\% focal-favoring with a near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above.\n\n\\subsection{Recommended DIF Audit Protocol}\n\\label{sec:disc_protocol}\n\n\\looseness=-1\nItem-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \\Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation}), with three action levels (calibrate via $\\rho$-degradation; \\Cref{app:fig_rho_degradation}): \\emph{Monitor} (C\\% $< 15\\%$), \\emph{Flag} ($15$--$25\\%$: dual rankings), \\emph{Act} ($\\geq 25\\%$: stable-item rankings). Difficulty--direction and model-type signals (\\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\\Cref{app:fig_downstream}), motivating equating~\\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\\rho = 0.95$).\n",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01ELRzpXvgCMQqE3sxG5zd4y`</summary>

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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "7e9a0db5-4fba-4274-b551-cce1c5c44269",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 11 · 2026-05-22T20:41:58.766Z_

<details><summary>↩ Tool result · `toolu_01ELRzpXvgCMQqE3sxG5zd4y`</summary>

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
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%]; family-level cluster bootstrap CI $[26.7\%, 53.2\%]$). Two independent non-independence corrections converge on approximately 27--29\%: simple-mean DEFF correction (29.2\%) and family-level cluster bootstrap lower bound (26.7\%). The weighted-mean DEFF variant yields 13.5\%, but its effective cluster size ($\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\rho_s = -0.009$, $p = 0.96$; \Cref{app:icc_family}), so the weighted variant over-corrects. The $[13.5\%, 29.2\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\Delta_{\mathrm{MH}}| \geq 1.5$ unchanged). We adopt ${\approx}$27--29\% as our primary estimate, with 13.5\% as a lower bound under weighted-mean DEFF (\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\Delta\mathrm{C\%}| \leq 2.93$\,pp). Graduated de-duplication independently confirms C\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\,pp across random draws (\Cref{app:dedup_k}). C\% is stable across $K \geq 5$ (31.3\%--35.9\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, consistent with residual non-uniform DIF that MH does not capture, while $K{=}3$ inflates to 39.4\% from under-stratification.
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
118	Semi-synthetic injection on GSM8K confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$; \Cref{app:gsm8k_details}); GSM1K analysis ($r = -0.478$, $p = 0.005$; \Cref{app:fig_gsm1k}) suggests DIF captures beyond memorization.
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "ed95fdcf-fe22-473e-bdf7-9c6e3340ee20",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH response matrix~\\citep{kipnis2024metabench} (5,227 models $\\times$ 12,508 MMLU items~\\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\n\\looseness=-1\nAs approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\\citep{zhou2026psnirt} ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \\geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ (details in \\Cref{app:method_details}). Our temporal cohorts ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\\Cref{app:power_sensitivity}).\n\n\\subsection{Temporal Comparability: 31\\% Measurement Instability}\n\\label{sec:temporal}\n\n\\looseness=-1\nWe compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 95\\% bootstrap CI: [29.4\\%, 38.1\\%]; family-level cluster bootstrap CI $[26.7\\%, 53.2\\%]$). Two independent non-independence corrections converge on approximately 27--29\\%: simple-mean DEFF correction (29.2\\%) and family-level cluster bootstrap lower bound (26.7\\%). The weighted-mean DEFF variant yields 13.5\\%, but its effective cluster size ($\\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\\rho_s = -0.009$, $p = 0.96$; \\Cref{app:icc_family}), so the weighted variant over-corrects. The $[13.5\\%, 29.2\\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ unchanged). We adopt ${\\approx}$27--29\\% as our primary estimate, with 13.5\\% as a lower bound under weighted-mean DEFF (\\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp). Graduated de-duplication independently confirms C\\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\\,pp across random draws (\\Cref{app:dedup_k}). C\\% is stable across $K \\geq 5$ (31.3\\%--35.9\\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, consistent with residual non-uniform DIF that MH does not capture, while $K{=}3$ inflates to 39.4\\% from under-stratification.\n\n\\looseness=-1\nThree controls confirm genuine temporal change (\\Cref{tab:temporal_landscape}): random splits yield C\\% of 0.18\\% (2023) and 1.3\\% (2024), both ${\\geq}23\\times$ below temporal C\\%; ability-quintile comparison yields 2.9\\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\\% $= 28.9\\% \\pm 0.1\\%$, confirming at most ${\\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \\Cref{app:method_details}).\n\n\\looseness=-1\nAcross all 57 subjects, C\\% ranges from 20.7\\% to 48.4\\% (mean $\\approx 30\\%$; \\Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \\emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\\%), Humanities favor 2023 (64.4\\%). Domain-level accuracy gains explain ${<}0.1\\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is associated with item properties rather than aggregate gains (OR reverses from 1.55 to 0.73 after controlling for difficulty; \\Cref{app:structural}). A difficulty--direction interaction emerges ($\\rho = -0.597$): 2024 models gain on hard items while eroding on easy ones. The conclusion is robust across thresholds ($18.3\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 2.0$, $10.2\\%$ at $\\geq 2.5$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. C\\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \\citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\\ labels are not applicable.}\n\\label{tab:temporal_landscape}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & C\\% & C\\% (web-clean) & Enrich. \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split 2023 (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nRandom split 2024 (sanity) & ${\\sim}$400 / ${\\sim}$400 & 1.3 & -- & -- \\\\\nWithin-subject (avg, 5 subj.) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\n\\looseness=-1\nDirect comparison of DIF flags against the web-overlap labels of \\citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (bootstrap 95\\% CI: $[0.94, 1.02]$; \\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\\% among web-contaminated items and 31.8\\% among clean items. Association tests confirm near-independence ($\\phi = 0.012$, OR $= 1.05$ [0.96, 1.15], Jaccard $= 0.206$, within permutation null $[0.203, 0.222]$; $p = 0.88$). This near-independence holds across contamination subtypes. The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \\emph{global exposure} (whether an item exists in training corpora), while DIF measures \\emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The two constructs---global exposure and differential functioning---are empirically orthogonal.\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\n\\looseness=-1\nTwo structural controls and a sensitivity check fail to reduce temporal C\\% below 31\\% (\\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\\% $= 38.1\\%$; cross-subject C\\% is more conservative due to lower local dependence), and IRT $\\theta$-conditioning ($r(\\theta, \\mathrm{total\\ score}) = 0.9986$). Logistic regression on nine subjects (1{,}787 items; 9/57---full-benchmark rates require further analysis) detects an additional 17.7\\% with non-uniform DIF ($|\\beta_{\\mathrm{interaction}}| \\geq 0.5$; effect-size criterion; LR $p$-values not adjusted for clustering); the union reaches 47\\% (Jaccard $= 0.28$): ${\\approx}$27--29\\% uniform (MH) plus 17.7\\% non-uniform (interaction-only), mutually exclusive by construction. Ability-matched analysis yields C\\% $= 28.9\\%$ (temporal) and $28.3\\%$ (Llama-2 vs.\\ 3)---consistent matched values (${\\sim}$28--29\\%) despite vastly different unmatched rates (\\Cref{app:structural}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\\% below 31\\%; $\\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}\n\\label{tab:structural_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temp.\\ C\\% & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (ext.) & Cross-bench.\\ total score & $0.314_{\\pm.009}$ & $0.834_{\\pm.027}$ & Reference \\\\\nMatched-ability & Within-quintile temp.\\ DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-cond.\\ (sens.) & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\n\\looseness=-1\nCross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$, upper-bound estimate under uniform binary flipping; \\Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ on average. The $\\Delta\\mathrm{FPR} = 0$ guarantee holds for single-subject contamination ($k \\leq 5$, $\\Delta\\mathrm{FPR} < 0.007$). Under broader contamination spanning $k = 10$ subjects (18\\% of domains), $\\Delta\\mathrm{FPR}$ rises to $0.047 \\pm 0.022$; at $k = 20$, to $0.069 \\pm 0.018$ (\\Cref{tab:multi_subject_injection,app:fig_matching}). Even worst-case multi-subject inflation ($\\sim$7~pp) cannot account for the observed 31\\% C\\% rate, which exceeds the 0.18\\% random baseline by ${>}170\\times$. Under DEFF adjustment, worst-case $\\Delta\\mathrm{FPR}$ at $k{=}20$ (0.069) represents up to 50\\% of the 13.5\\% lower bound, underscoring $k \\leq 5$ in practice. Difficulty-dependent injection produces distinguishable $\\rho$ signatures (capability-like: $+0.77$ vs.\\ contamination-like: $-0.52$; zero seed overlap), though mapping to real-data mechanisms requires further work.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\n\\looseness=-1\nStable-item ranks are preserved across all six benchmarks ($\\rho = 0.997$, $\\tau = 0.958$; flip rate $\\leq 2.8\\%$; \\Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\\ random removal; \\Cref{app:fig_downstream}). Among the 200 most displaced models (top 3.8\\%), 33.6\\% of pairwise rankings reverse, concentrating among closely-ranked pairs (35.2\\% at $\\Delta\\mathrm{rank} < 50$ vs.\\ 0.0\\% above 1000; \\Cref{app:rank_reversal}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\\times$ random; $p < 0.001$).\n\n\\subsection{Cross-Benchmark Validation}\n\\label{sec:gsm8k}\n\n\\looseness=-1\nTemporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six METABENCH benchmarks. C\\% = ETS~C items ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) between 2023 and 2024 cohorts; $\\rho$/$\\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\\%/Rand.\\ C\\%, with baseline varying by benchmark. All six show substantial DIF (45--174$\\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\\% than procedural ones.}\n\\label{tab:cross_benchmark}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrl}\n\\toprule\nBenchmark & Items & C\\% & $\\rho$ & $\\tau$ & Flip\\% & Rand.\\ C\\% & Ratio \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.18 & 174$\\times$ \\\\\nWinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\\times$ \\\\\nARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSemi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}); GSM1K analysis ($r = -0.478$, $p = 0.005$; \\Cref{app:fig_gsm1k}) suggests DIF captures beyond memorization.\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01FyHpMq5CZr9XdCikU8uRG5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "4e880128-1200-42ee-8fe7-368a673980d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 13 · 2026-05-22T20:41:59.754Z_

<details><summary>↩ Tool result · `toolu_01FyHpMq5CZr9XdCikU8uRG5`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{IRT model fit.} For transparency, we report that the MMLU response matrix shows poor fit to a unidimensional 2PL model (expected for a 57-subject multidimensional benchmark). This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.
23	
24	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
25	
26	\paragraph{Power sensitivity to item discrimination.}
27	\label{app:power_sensitivity}
28	The Monte Carlo power analysis in \Cref{sec:validation} uses average 2PL parameters ($\bar{a} = 1.2$, $\bar{b} = -0.84$). \Cref{tab:power_sensitivity} reports TPR as a function of discrimination $a$ (other parameters at their means, $N = 80$ per cohort, $|\Delta_b| = 1.4$, 1,000 replications). TPR increases monotonically from 0.40 ($a = 0.5$) to 0.95 ($a = 2.0$); FPR remains below 0.04 throughout. The MMLU item pool shows substantial heterogeneity: $a$ ranges from 0.006 to 2.657 (SD $= 0.54$, IQR $= [0.75, 1.64]$). The aggregate TPR of 0.68 from Phase~2 reflects this full distribution, while TPR at mean $a \approx 1.2$ is 0.87---the gap is consistent with Jensen's inequality applied to the concave TPR($a$) function. Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation: parametric estimates (TPR $= 0.68$--$0.80$) are validated by empirical semi-synthetic injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{sec:semisynthetic}), confirming adequate detection power regardless of parametric assumptions.
29	
30	\begin{table}[h]
31	\centering
32	\caption{Power sensitivity to item discrimination. TPR = true positive rate for ETS~C detection ($|\Delta_{\mathrm{MH}}| \geq 1.5$) at $N = 80$ per cohort, $|\Delta_b| = 1.4$, 1,000 replications.}
33	\label{tab:power_sensitivity}
34	\small
35	\begin{tabular}{rccc}
36	\toprule
37	$a$ & TPR & 95\% CI & FPR \\
38	\midrule
39	0.5 & 0.398 & [0.20, 0.60] & 0.033 \\
40	0.8 & 0.683 & [0.45, 0.90] & 0.036 \\
41	1.0 & 0.808 & [0.60, 0.95] & 0.038 \\
42	1.2 ($\approx \bar{a}$) & 0.874 & [0.70, 1.00] & 0.038 \\
43	1.5 & 0.930 & [0.80, 1.00] & 0.038 \\
44	2.0 & 0.949 & [0.80, 1.00] & 0.037 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.
50	
51	\paragraph{Logistic regression specification.} The Simpson's paradox analysis (\Cref{sec:temporal}) uses binary logistic regression with DIF-C classification as the dependent variable, domain-level accuracy change (2024 minus 2023 mean accuracy) as the primary predictor, and item difficulty (proportion correct) and IRT discrimination (point-biserial correlation) as controls. The interaction between domain accuracy change and item difficulty is included. Non-uniform DIF detection (\Cref{sec:structural}) uses logistic regression with a group $\times$ ability interaction term; a significant interaction ($p < 0.05$) indicates non-uniform DIF.
52	
53	\section{Structural Analysis Details}
54	\label{app:structural}
55	
56	Two structural controls and a sensitivity check fail to reduce the temporal C\% below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal C\% unchanged at approximately 0.31. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. As a sensitivity check, IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and C\% $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. \Cref{tab:structural_comparison} summarizes these results.
57	
58	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions available in the supplementary material).
59	
60	\begin{table}[h]
61	\centering
62	\caption{Domain-level Cohen's $d$ between 2023 and 2024 cohorts. The narrow range ($0.12$) indicates nearly uniform improvement across domains, supporting total-score matching adequacy for DIF analysis (\Cref{sec:method}).}
63	\label{tab:domain_cohens_d}
64	\small
65	\begin{tabular}{lr}
66	\toprule
67	Domain & Cohen's $d$ \\
68	\midrule
69	STEM & 0.261 \\
70	Humanities & 0.159 \\
71	Social Science & 0.147 \\
72	Other & 0.146 \\
73	\bottomrule
74	\end{tabular}
75	\end{table}
76	
77	\begin{table}[h]
78	\centering
79	\caption{Multi-subject injection robustness. $k$ = number of simultaneously contaminated subjects (out of 57); values are mean $\pm$ SD across 5 random subject draws at exploitation rate $p = 0.5$.}
80	\label{tab:multi_subject_injection}
81	\small
82	\begin{tabular}{rcc}
83	\toprule
84	$k$ & $\Delta\mathrm{FPR}$ & $\Delta\mathrm{TPR}$ \\
85	\midrule
86	1 & $0.000_{\pm.000}$ & $0.371_{\pm.048}$ \\
87	3 & $0.003_{\pm.002}$ & $0.385_{\pm.031}$ \\
88	5 & $0.007_{\pm.003}$ & $0.392_{\pm.027}$ \\
89	10 & $0.047_{\pm.022}$ & $0.401_{\pm.024}$ \\
90	20 & $0.069_{\pm.018}$ & $0.410_{\pm.020}$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	\begin{table}[h]
96	\centering
97	\caption{Leave-one-family-out (LOFO) robustness on MMLU. Removing non-dominant families ($\leq$15\% of their cohort) changes C\% by at most 2.93\,pp. Larger shifts from removing Mistral or Llama-3 are driven almost entirely by family composition, not statistical power loss: Monte Carlo random-subsample calibration (200 replicates per scenario, matching the reduced sample size) shows the power effect is $\leq$1\,pp, while the composition effect accounts for 95--113\% of the observed C\% drop (Mistral: $-8.44$\,pp composition vs.\ $-0.41$\,pp power; Llama-3: $-8.17$\,pp vs.\ ${+}0.91$\,pp; observed C\% falls below the 95\% random-subsample range in both cases). Stratification uses total test score for computational efficiency; cross-subject matching yields identical baseline C\%.}
98	\label{tab:lofo}
99	\small
100	\begin{tabular}{lrrr}
101	\toprule
102	Family & $N$ removed & Cohort share & C\% (LOFO) \\
103	\midrule
104	\emph{Full sample} & --- & --- & 31.32 \\
105	Mistral & 547 & 51\% ref & 22.47 \\
106	Llama-3 & 315 & 39\% foc & 24.06 \\
107	Mixtral & 120 & 15\% foc & 34.26 \\
108	Llama-2 & 161 & 15\% ref & 31.48 \\
109	Solar & 91 & 11\% foc & 31.01 \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\section{Design Effect Estimation}
115	\label{app:deff}
116	
117	Model families (e.g., Mistral, Llama-3) induce intra-class correlation (ICC) that inflates Mantel-Haenszel $\chi^2$ statistics beyond the nominal $\chi^2_1$ reference distribution. We estimate the design effect (DEFF) per item following \citet{rao1992variance}: $\mathrm{DEFF}_i = 1 + (\bar{m} - 1) \cdot \mathrm{ICC}_i$, where $\bar{m}$ is the mean family size and $\mathrm{ICC}_i$ is the one-way random-effects ICC for item $i$ across 30 families (restricted to ref+foc cohort; 1,884 models with family$\geq$2).
118	
119	Two estimates of $\bar{m}$ bracket the adjustment: (1)~\emph{Simple mean} ($\bar{m} = 62.8$), treating all families equally, yields $\mathrm{DEFF} = 3.87$ and adjusted C\% $= 29.2\%$; (2)~\emph{Weighted mean} ($\bar{m} = \sum n_f^2 / \sum n_f = 254.5$; \citealp{kish1965survey}), reflecting the effective cluster size experienced by a randomly sampled model, yields $\mathrm{DEFF} = 12.79$ and adjusted C\% $= 13.5\%$.
120	
121	\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\% of items exceed $0.10$). After dividing each item's $\chi^2_{\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\% of items retain Category~C classification depending on the $\bar{m}$ variant---both far exceeding the 0.18\% random-split baseline (75--162$\times$).
122	
123	\paragraph{Size-stratified DEFF.} The aggregate ICC masks a size--ICC inverse relationship: smaller families exhibit higher within-family similarity (\Cref{tab:deff_stratified}). Tier-level ICC ranges from 0.246 (2--10 members) to 0.082 ({>}200 members), reflecting greater heterogeneity in mega-families. At small family sizes, DEFF correction has negligible impact (Adj.\ C\% $= 31.3\%$); the conservative 13.5\% bound is driven entirely by the two mega-families (Mistral, Llama-3). Family definition sensitivity is minimal: merging sub-generations (e.g., Llama-2 + Llama-3) into coarse families (22 families) changes C\% by $\leq$0.3~pp.
124	
125	\begin{table}[h]
126	\centering
127	\caption{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\ C\% applies tier-specific DEFF to all items.}
128	\label{tab:deff_stratified}
129	\small
130	\begin{tabular}{lrrrrc}
131	\toprule
132	Tier & Families & $\bar{m}$ & ICC & DEFF & Adj.\ C\% \\
133	\midrule
134	2--10 & 9 & 5.3 & 0.246 & 2.07 & 31.3\% \\
135	11--50 & 11 & 22.1 & 0.226 & 5.78 & 24.6\% \\
136	51--200 & 8 & 91.4 & 0.137 & 13.34 & 13.7\% \\
137	${>}200$ & 2 & 431.0 & 0.082 & 36.11 & 9.0\% \\
138	\midrule
139	Overall & 30 & 62.8 & 0.047 & 3.87 & 29.2\% \\
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	
144	\section{Uncertainty Quantification Comparison}
145	\label{app:uncertainty}
146	
147	\begin{table}[h]
148	\centering
149	\caption{Comparison of uncertainty quantification methods for the 31.3\% C\% estimate on MMLU.}
150	\small
151	\resizebox{\columnwidth}{!}{%
152	\begin{tabular}{llr}
153	\toprule
154	Method & Key assumption & Result \\
155	\midrule
156	Model-level bootstrap & Models independent & 95\% CI [29.4\%, 38.1\%] \\
157	Family-level cluster bootstrap & Family is clustering unit & 95\% CI [26.7\%, 53.2\%] \\
158	DEFF (simple $\bar{m}$) & Equal-weight families & Adjusted C\% = 29.2\% \\
159	DEFF (weighted $\bar{m}$) & Size-proportional weighting & Adjusted C\% = 13.5\% \\
160	Graduated de-dup.\ ($K{=}20$) & Remove within-family duplicates & C\% = 19.7\% $\pm$ 0.9\% \\
161	\bottomrule
162	\end{tabular}}
163	\label{tab:uncertainty}
164	\end{table}
165	
166	The cluster bootstrap upper bound (53.2\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\%) and simple-mean DEFF adjustment (29.2\%)---converge on $\sim$27--29\%, establishing a robust corrected estimate that remains $>$150$\times$ the random-split baseline (0.18\%). Graduated de-duplication at $K{=}20$ yields C\% $= 19.7\% \pm 0.9\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \approx 450$ vs.\ 1,887), but within-$K$ variance ${<}1.5$\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\%) represents a conservative extreme; even this lower bound exceeds the baseline by 75$\times$.
167	
168	\section{Cross-Benchmark Comparison}
169	\label{app:gsm8k_details}
170	
171	\begin{table}[h]
172	\centering
173	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal measurement instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
174	\label{tab:gsm8k_comparison}
175	\small
176	\begin{tabular}{lcc}
177	\toprule
178	Metric & MMLU & GSM8K \\
179	\midrule
180	Items & 12,508 & 1,319 \\
181	Models & 5,227 & 6,702 \\
182	Temporal C\% & 31.3\% & 18.9\% \\
183	Sanity C\% & 0.18\% & 0.3\% \\
184	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
185	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	\section{Additional Figures}
191	\label{app:figures}
192	
193	\begin{figure}[h]
194	\centering
195	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
196	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
197	\label{app:fig_matching}
198	\end{figure}
199	
200	\begin{figure}[h]
201	\centering
202	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
203	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
204	\label{app:fig_downstream}
205	\end{figure}
206	
207	\begin{figure}[h]
208	\centering
209	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
210	\caption{Exploratory: GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$; small sample, results should be interpreted cautiously). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items. Three of 33 models exceed the Cook's $D$ threshold ($4/N = 0.12$); leave-one-out analysis confirms all individual-removal correlations remain significant ($r \in [-0.54, -0.37]$, all $p < 0.05$), and removing all three outliers yields $r = -0.38$ ($p = 0.036$, $N = 30$).}
211	\label{app:fig_gsm1k}
212	\end{figure}
213	
214	\begin{figure}[h]
215	\centering
216	\includegraphics[width=\columnwidth]{fig_A3_rho_degradation.pdf}
217	\caption{Ranking degradation under DIF-ordered vs.\ random item removal across six benchmarks. DIF-ordered removal (orange) consistently degrades $\rho$ faster than random removal (blue band = mean $\pm$ 1 SD, 20 seeds). Vertical dashed lines mark the Monitor/Flag (15\%) and Flag/Act (25\%) thresholds from \Cref{sec:disc_protocol}.}
218	\label{app:fig_rho_degradation}
219	\end{figure}
220	
221	\section{Item-Property Predictive Analysis}
222	\label{app:predictive}
223	
224	To test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \pm 0.020$ (LR) and $0.599 \pm 0.026$ (LightGBM)---near chance. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.
225	
226	\section{Within-Family Similarity by Family Size}
227	\label{app:icc_family}
228	
229	Within-family similarity (mean pairwise Pearson $r$ over 12{,}508-item response vectors) shows no dependence on family size (Spearman $\rho = -0.009$, $p = 0.96$; 30 families with $\geq 2$ members, 1{,}884 models). Large families (Mistral, $m = 547$, $\bar{r} = 0.47$; Llama-3, $m = 315$, $\bar{r} = 0.53$) are no more homogeneous than small or mid-sized families. Of the 5{,}227 models, 3{,}343 lack family assignments; these are retained in DIF analysis but excluded from similarity estimation. Within the temporal DIF cohorts ($N_{\mathrm{ref}} + N_{\mathrm{foc}} = 1{,}887$), 1{,}884 (99.8\%) belong to identified families with $\geq 2$ members, so DEFF estimates are computed over nearly the full cohort. This indicates that the weighted-mean DEFF variant's effective cluster size ($\bar{m} = 254$) reflects an arithmetic artifact of mega-family dominance rather than genuine within-family homogeneity.
230	
231	\section{Graduated De-Duplication Sensitivity}
232	\label{app:dedup_k}
233	
234	For each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \text{all}$ is deterministic).
235	
236	C\% increases monotonically from 0.3\% ($K = 1$) to 31.3\% ($K = \text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\% $= 19.7\% \pm 0.9\%$ ($N \approx 450$); the gap from the full-sample 31.3\% reflects reduced power, not reduced bias.
237	
238	\section{Rank-Reversal by Distance}
239	\label{app:rank_reversal}
240	
241	Pairwise rank reversals between full-item and stable-item rankings concentrate among closely-ranked models. At $\Delta\mathrm{rank} < 50$ (mean $\Delta\mathrm{acc} = 0.003$, effectively statistical ties), the reversal rate is 35.2\%. It drops to 15.1\% for $\Delta\mathrm{rank} \in [50, 200)$, 4.0\% for $[200, 500)$, 0.6\% for $[500, 1000)$, and 0.0\% above 1000. Broad leaderboard structure is fully preserved; instability affects only models within each other's noise margin.
242	
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "af204380-5a44-4407-a4c9-0de32412bf9b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
      "content": "\\section{Method Details}\n\\label{app:method_details}\n\n\\subsection{Diagnostics}\n\\label{app:diagnostics}\n\nThree diagnostic procedures complement the primary DIF analysis.\n\n\\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\\theta$ captures, which could inflate within-subject DIF rates.\n\n\\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\\rho$ between subject-level C\\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.\n\n\\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\\% measures the contribution of domain-level improvement to the total instability.\n\n\\subsection{Statistical Considerations}\n\\label{app:statistical}\n\n\\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.\n\n\\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\\Delta_{\\mathrm{MH}}| \\in \\{1.0, 1.5, 2.0, 2.5\\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ corresponds to the ETS~C definition used throughout the paper.\n\n\\paragraph{IRT model fit.} For transparency, we report that the MMLU response matrix shows poor fit to a unidimensional 2PL model (expected for a 57-subject multidimensional benchmark). This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.\n\n\\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.\n\n\\paragraph{Power sensitivity to item discrimination.}\n\\label{app:power_sensitivity}\nThe Monte Carlo power analysis in \\Cref{sec:validation} uses average 2PL parameters ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$). \\Cref{tab:power_sensitivity} reports TPR as a function of discrimination $a$ (other parameters at their means, $N = 80$ per cohort, $|\\Delta_b| = 1.4$, 1,000 replications). TPR increases monotonically from 0.40 ($a = 0.5$) to 0.95 ($a = 2.0$); FPR remains below 0.04 throughout. The MMLU item pool shows substantial heterogeneity: $a$ ranges from 0.006 to 2.657 (SD $= 0.54$, IQR $= [0.75, 1.64]$). The aggregate TPR of 0.68 from Phase~2 reflects this full distribution, while TPR at mean $a \\approx 1.2$ is 0.87---the gap is consistent with Jensen's inequality applied to the concave TPR($a$) function. Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation: parametric estimates (TPR $= 0.68$--$0.80$) are validated by empirical semi-synthetic injection ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{sec:semisynthetic}), confirming adequate detection power regardless of parametric assumptions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Power sensitivity to item discrimination. TPR = true positive rate for ETS~C detection ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) at $N = 80$ per cohort, $|\\Delta_b| = 1.4$, 1,000 replications.}\n\\label{tab:power_sensitivity}\n\\small\n\\begin{tabular}{rccc}\n\\toprule\n$a$ & TPR & 95\\% CI & FPR \\\\\n\\midrule\n0.5 & 0.398 & [0.20, 0.60] & 0.033 \\\\\n0.8 & 0.683 & [0.45, 0.90] & 0.036 \\\\\n1.0 & 0.808 & [0.60, 0.95] & 0.038 \\\\\n1.2 ($\\approx \\bar{a}$) & 0.874 & [0.70, 1.00] & 0.038 \\\\\n1.5 & 0.930 & [0.80, 1.00] & 0.038 \\\\\n2.0 & 0.949 & [0.80, 1.00] & 0.037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.\n\n\\paragraph{Logistic regression specification.} The Simpson's paradox analysis (\\Cref{sec:temporal}) uses binary logistic regression with DIF-C classification as the dependent variable, domain-level accuracy change (2024 minus 2023 mean accuracy) as the primary predictor, and item difficulty (proportion correct) and IRT discrimination (point-biserial correlation) as controls. The interaction between domain accuracy change and item difficulty is included. Non-uniform DIF detection (\\Cref{sec:structural}) uses logistic regression with a group $\\times$ ability interaction term; a significant interaction ($p < 0.05$) indicates non-uniform DIF.\n\n\\section{Structural Analysis Details}\n\\label{app:structural}\n\nTwo structural controls and a sensitivity check fail to reduce the temporal C\\% below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal C\\% unchanged at approximately 0.31. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\\% $= 38.1\\%$, exceeding the 25\\% threshold that would indicate viable bifactor structure. As a sensitivity check, IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and C\\% $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. \\Cref{tab:structural_comparison} summarizes these results.\n\nThe temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\\ 2.2\\% cross-subject; $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\\% persists under external matching (full Q3 distributions available in the supplementary material).\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level Cohen's $d$ between 2023 and 2024 cohorts. The narrow range ($0.12$) indicates nearly uniform improvement across domains, supporting total-score matching adequacy for DIF analysis (\\Cref{sec:method}).}\n\\label{tab:domain_cohens_d}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nDomain & Cohen's $d$ \\\\\n\\midrule\nSTEM & 0.261 \\\\\nHumanities & 0.159 \\\\\nSocial Science & 0.147 \\\\\nOther & 0.146 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-subject injection robustness. $k$ = number of simultaneously contaminated subjects (out of 57); values are mean $\\pm$ SD across 5 random subject draws at exploitation rate $p = 0.5$.}\n\\label{tab:multi_subject_injection}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\n$k$ & $\\Delta\\mathrm{FPR}$ & $\\Delta\\mathrm{TPR}$ \\\\\n\\midrule\n1 & $0.000_{\\pm.000}$ & $0.371_{\\pm.048}$ \\\\\n3 & $0.003_{\\pm.002}$ & $0.385_{\\pm.031}$ \\\\\n5 & $0.007_{\\pm.003}$ & $0.392_{\\pm.027}$ \\\\\n10 & $0.047_{\\pm.022}$ & $0.401_{\\pm.024}$ \\\\\n20 & $0.069_{\\pm.018}$ & $0.410_{\\pm.020}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-family-out (LOFO) robustness on MMLU. Removing non-dominant families ($\\leq$15\\% of their cohort) changes C\\% by at most 2.93\\,pp. Larger shifts from removing Mistral or Llama-3 are driven almost entirely by family composition, not statistical power loss: Monte Carlo random-subsample calibration (200 replicates per scenario, matching the reduced sample size) shows the power effect is $\\leq$1\\,pp, while the composition effect accounts for 95--113\\% of the observed C\\% drop (Mistral: $-8.44$\\,pp composition vs.\\ $-0.41$\\,pp power; Llama-3: $-8.17$\\,pp vs.\\ ${+}0.91$\\,pp; observed C\\% falls below the 95\\% random-subsample range in both cases). Stratification uses total test score for computational efficiency; cross-subject matching yields identical baseline C\\%.}\n\\label{tab:lofo}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nFamily & $N$ removed & Cohort share & C\\% (LOFO) \\\\\n\\midrule\n\\emph{Full sample} & --- & --- & 31.32 \\\\\nMistral & 547 & 51\\% ref & 22.47 \\\\\nLlama-3 & 315 & 39\\% foc & 24.06 \\\\\nMixtral & 120 & 15\\% foc & 34.26 \\\\\nLlama-2 & 161 & 15\\% ref & 31.48 \\\\\nSolar & 91 & 11\\% foc & 31.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Design Effect Estimation}\n\\label{app:deff}\n\nModel families (e.g., Mistral, Llama-3) induce intra-class correlation (ICC) that inflates Mantel-Haenszel $\\chi^2$ statistics beyond the nominal $\\chi^2_1$ reference distribution. We estimate the design effect (DEFF) per item following \\citet{rao1992variance}: $\\mathrm{DEFF}_i = 1 + (\\bar{m} - 1) \\cdot \\mathrm{ICC}_i$, where $\\bar{m}$ is the mean family size and $\\mathrm{ICC}_i$ is the one-way random-effects ICC for item $i$ across 30 families (restricted to ref+foc cohort; 1,884 models with family$\\geq$2).\n\nTwo estimates of $\\bar{m}$ bracket the adjustment: (1)~\\emph{Simple mean} ($\\bar{m} = 62.8$), treating all families equally, yields $\\mathrm{DEFF} = 3.87$ and adjusted C\\% $= 29.2\\%$; (2)~\\emph{Weighted mean} ($\\bar{m} = \\sum n_f^2 / \\sum n_f = 254.5$; \\citealp{kish1965survey}), reflecting the effective cluster size experienced by a randomly sampled model, yields $\\mathrm{DEFF} = 12.79$ and adjusted C\\% $= 13.5\\%$.\n\n\\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\\% of items exceed $0.10$). After dividing each item's $\\chi^2_{\\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\\% of items retain Category~C classification depending on the $\\bar{m}$ variant---both far exceeding the 0.18\\% random-split baseline (75--162$\\times$).\n\n\\paragraph{Size-stratified DEFF.} The aggregate ICC masks a size--ICC inverse relationship: smaller families exhibit higher within-family similarity (\\Cref{tab:deff_stratified}). Tier-level ICC ranges from 0.246 (2--10 members) to 0.082 ({>}200 members), reflecting greater heterogeneity in mega-families. At small family sizes, DEFF correction has negligible impact (Adj.\\ C\\% $= 31.3\\%$); the conservative 13.5\\% bound is driven entirely by the two mega-families (Mistral, Llama-3). Family definition sensitivity is minimal: merging sub-generations (e.g., Llama-2 + Llama-3) into coarse families (22 families) changes C\\% by $\\leq$0.3~pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\\ C\\% applies tier-specific DEFF to all items.}\n\\label{tab:deff_stratified}\n\\small\n\\begin{tabular}{lrrrrc}\n\\toprule\nTier & Families & $\\bar{m}$ & ICC & DEFF & Adj.\\ C\\% \\\\\n\\midrule\n2--10 & 9 & 5.3 & 0.246 & 2.07 & 31.3\\% \\\\\n11--50 & 11 & 22.1 & 0.226 & 5.78 & 24.6\\% \\\\\n51--200 & 8 & 91.4 & 0.137 & 13.34 & 13.7\\% \\\\\n${>}200$ & 2 & 431.0 & 0.082 & 36.11 & 9.0\\% \\\\\n\\midrule\nOverall & 30 & 62.8 & 0.047 & 3.87 & 29.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Uncertainty Quantification Comparison}\n\\label{app:uncertainty}\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison of uncertainty quantification methods for the 31.3\\% C\\% estimate on MMLU.}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llr}\n\\toprule\nMethod & Key assumption & Result \\\\\n\\midrule\nModel-level bootstrap & Models independent & 95\\% CI [29.4\\%, 38.1\\%] \\\\\nFamily-level cluster bootstrap & Family is clustering unit & 95\\% CI [26.7\\%, 53.2\\%] \\\\\nDEFF (simple $\\bar{m}$) & Equal-weight families & Adjusted C\\% = 29.2\\% \\\\\nDEFF (weighted $\\bar{m}$) & Size-proportional weighting & Adjusted C\\% = 13.5\\% \\\\\nGraduated de-dup.\\ ($K{=}20$) & Remove within-family duplicates & C\\% = 19.7\\% $\\pm$ 0.9\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\label{tab:uncertainty}\n\\end{table}\n\nThe cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\\%) and simple-mean DEFF adjustment (29.2\\%)---converge on $\\sim$27--29\\%, establishing a robust corrected estimate that remains $>$150$\\times$ the random-split baseline (0.18\\%). Graduated de-duplication at $K{=}20$ yields C\\% $= 19.7\\% \\pm 0.9\\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \\approx 450$ vs.\\ 1,887), but within-$K$ variance ${<}1.5$\\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\\%) represents a conservative extreme; even this lower bound exceeds the baseline by 75$\\times$.\n\n\\section{Cross-Benchmark Comparison}\n\\label{app:gsm8k_details}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal measurement instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\\pm$ values denote standard deviations across 5 random injection seeds.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.18\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\\pm.006}$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\\pm.027}$ & $+0.514_{\\pm.028}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Figures}\n\\label{app:figures}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{app:fig_matching}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}\n\\label{app:fig_downstream}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{Exploratory: GSM1K contamination gap vs.\\ DIF ranking advantage ($N = 33$; small sample, results should be interpreted cautiously). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items. Three of 33 models exceed the Cook's $D$ threshold ($4/N = 0.12$); leave-one-out analysis confirms all individual-removal correlations remain significant ($r \\in [-0.54, -0.37]$, all $p < 0.05$), and removing all three outliers yields $r = -0.38$ ($p = 0.036$, $N = 30$).}\n\\label{app:fig_gsm1k}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_A3_rho_degradation.pdf}\n\\caption{Ranking degradation under DIF-ordered vs.\\ random item removal across six benchmarks. DIF-ordered removal (orange) consistently degrades $\\rho$ faster than random removal (blue band = mean $\\pm$ 1 SD, 20 seeds). Vertical dashed lines mark the Monitor/Flag (15\\%) and Flag/Act (25\\%) thresholds from \\Cref{sec:disc_protocol}.}\n\\label{app:fig_rho_degradation}\n\\end{figure}\n\n\\section{Item-Property Predictive Analysis}\n\\label{app:predictive}\n\nTo test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \\pm 0.020$ (LR) and $0.599 \\pm 0.026$ (LightGBM)---near chance. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \\Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.\n\n\\section{Within-Family Similarity by Family Size}\n\\label{app:icc_family}\n\nWithin-family similarity (mean pairwise Pearson $r$ over 12{,}508-item response vectors) shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; 30 families with $\\geq 2$ members, 1{,}884 models). Large families (Mistral, $m = 547$, $\\bar{r} = 0.47$; Llama-3, $m = 315$, $\\bar{r} = 0.53$) are no more homogeneous than small or mid-sized families. Of the 5{,}227 models, 3{,}343 lack family assignments; these are retained in DIF analysis but excluded from similarity estimation. Within the temporal DIF cohorts ($N_{\\mathrm{ref}} + N_{\\mathrm{foc}} = 1{,}887$), 1{,}884 (99.8\\%) belong to identified families with $\\geq 2$ members, so DEFF estimates are computed over nearly the full cohort. This indicates that the weighted-mean DEFF variant's effective cluster size ($\\bar{m} = 254$) reflects an arithmetic artifact of mega-family dominance rather than genuine within-family homogeneity.\n\n\\section{Graduated De-Duplication Sensitivity}\n\\label{app:dedup_k}\n\nFor each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC\\% increases monotonically from 0.3\\% ($K = 1$) to 31.3\\% ($K = \\text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\\% $= 19.7\\% \\pm 0.9\\%$ ($N \\approx 450$); the gap from the full-sample 31.3\\% reflects reduced power, not reduced bias.\n\n\\section{Rank-Reversal by Distance}\n\\label{app:rank_reversal}\n\nPairwise rank reversals between full-item and stable-item rankings concentrate among closely-ranked models. At $\\Delta\\mathrm{rank} < 50$ (mean $\\Delta\\mathrm{acc} = 0.003$, effectively statistical ties), the reversal rate is 35.2\\%. It drops to 15.1\\% for $\\Delta\\mathrm{rank} \\in [50, 200)$, 4.0\\% for $[200, 500)$, 0.6\\% for $[500, 1000)$, and 0.0\\% above 1000. Broad leaderboard structure is fully preserved; instability affects only models within each other's noise margin.\n\n",
      "numLines": 243,
      "startLine": 1,
      "totalLines": 243
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01DWtvoafvKTrJWMUqF2AinG`</summary>

```json
{
  "pattern": "\\\\enlargethispage",
  "output_mode": "content",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "0970c16b-df63-40ea-af82-e22d2c8c6c7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cpqgT1X99LPeFZFVXWdPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14605,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14605
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 15 · 2026-05-22T20:42:00.683Z_

<details><summary>↩ Tool result · `toolu_01DWtvoafvKTrJWMUqF2AinG`</summary>

```text
paper/sections/discussion.tex:3:\enlargethispage*{20\baselineskip}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "e78ea225-1a73-458f-8451-b6ad975019a0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/discussion.tex:3:\\enlargethispage*{20\\baselineskip}",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also search for temporal granularity / half-year content for B4, and NUDIF/non-uniform content for B7.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "f5e1173c-143e-4b2e-96a4-06788c818c8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wETJ1fV9yKmxhSmgYeaUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14277,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14277
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

Let me search for the half-year and NUDIF content before starting edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "99753b57-e019-4863-a298-101c97582449",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wETJ1fV9yKmxhSmgYeaUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14277,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14277
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

<details open><summary>🔧 Tool call — Grep · `toolu_018JK66TVpruY6pWCmXmoqgq`</summary>

```json
{
  "pattern": "half-year|half.year|temporal granularity|6.month|six.month",
  "output_mode": "content",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "0b96d336-1807-4895-af05-599ec04ee9b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wETJ1fV9yKmxhSmgYeaUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14277,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14277
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

_source line 19 · 2026-05-22T20:42:09.422Z_

<details><summary>↩ Tool result · `toolu_018JK66TVpruY6pWCmXmoqgq`</summary>

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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "7eea15c5-8a32-44f4-87c5-e0e5bf993e7e",
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

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_012UVRgs5HATa56fWXJ83ra8`</summary>

```json
{
  "pattern": "non-uniform|NUDIF|non.uniform DIF",
  "output_mode": "content",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "119097c1-ebda-4af0-860f-905cad81890a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wETJ1fV9yKmxhSmgYeaUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14277,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14277
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

_source line 21 · 2026-05-22T20:42:10.429Z_

<details><summary>↩ Tool result · `toolu_012UVRgs5HATa56fWXJ83ra8`</summary>

```text
paper/sections/experiments.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:60:[Omitted long matching line]
paper/sections/appendix.tex:51:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "e7a3b100-e1a3-49bb-b434-d21eec6726ee",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/experiments.tex:16:[Omitted long matching line]\npaper/sections/experiments.tex:60:[Omitted long matching line]\npaper/sections/appendix.tex:51:[Omitted long matching line]",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_01MdiYwmwcneELSiQNjSH5xY`</summary>

```json
{
  "pattern": "34\\.4|half-year|H1.*H2",
  "output_mode": "content",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "8fc95ed9-839b-4a11-8fab-fbc37bab07f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wETJ1fV9yKmxhSmgYeaUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14277,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14277
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

_source line 23 · 2026-05-22T20:42:11.927Z_

<details><summary>↩ Tool result · `toolu_01MdiYwmwcneELSiQNjSH5xY`</summary>

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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "a8f189b0-fa91-4091-ab51-a355c321f4a1",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
No half-year or 34.4% content exists in any .tex file. So for B4, I need to find where temporal granularity could be discussed. Since the half-year analysis isn't in the paper at all, I should add it to the appendix. Let me look for a logical place in the appendix - perhaps near the DEFF section or the uncertainty quantification section.

For B7, the non-uniform DIF content is in experiments.tex line 16: "consistent with residual non-uniform DIF that MH does not capture". I need to check the exact wording.

Let me now proceed with all the edits. I have all the information I need.


Now I'm mapping out the specific changes: B1 needs a couple sentences added to discussion.tex after line 18 about an alternative explanation, B2 requires replacing the last sentence in experiments.tex at line 118, B3 involves reducing the page enlargement command in discussion.tex line 3 to 8 or less, and B4 requires inserting the half-year explanation into the appendix since it doesn't appear anywhere in the current text. I need to search through the paper first to see if there's any existing mention of temporal granularity or half-year analysis before deciding where to add this content. Since neither appears to exist in the main text, the structural analysis section in the appendix seems like the most logical place to incorporate this temporal comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "f04ea772-0908-42f4-8930-2dc3deb59ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149uJdPpm6tdUBnbKwmQwqQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 40723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 784
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

_source line 25_

All files read. No half-year/34.4% content exists in any .tex file. The only `\enlargethispage` is in `discussion.tex` line 3 with value 20. NUDIF caveat is in `experiments.tex` line 16. Starting the 7 commits now.

**B1**: Adding alternative explanation to §5.1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "a2d39e05-ccf1-4333-b403-7c3403463634",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149uJdPpm6tdUBnbKwmQwqQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 40723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 784
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_015oxJMpEX3THyHgCseymPbB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "old_string": "This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above.",
  "new_string": "This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above. An alternative explanation---that easy items are uniformly contaminated ($\\to$ DIF-A) while hard items are differentially contaminated ($\\to$ DIF-C)---is partially addressed by this base-vs-instruct direction reversal: under a pure difficulty-dependent contamination account, both model types should exhibit the same DIF direction, yet we observe opposite patterns ($\\chi^2 = 562.7$, $p < 10^{-124}$; \\Cref{sec:temporal})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "39115e66-46d6-4339-874e-47c0aac9f98a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149uJdPpm6tdUBnbKwmQwqQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 40723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 784
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

_source line 27 · 2026-05-22T20:42:44.975Z_

<details><summary>↩ Tool result · `toolu_015oxJMpEX3THyHgCseymPbB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "14e44020-18c2-4ad2-9619-9bac4e65654f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "oldString": "This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above.",
    "newString": "This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above. An alternative explanation---that easy items are uniformly contaminated ($\\to$ DIF-A) while hard items are differentially contaminated ($\\to$ DIF-C)---is partially addressed by this base-vs-instruct direction reversal: under a pure difficulty-dependent contamination account, both model types should exhibit the same DIF direction, yet we observe opposite patterns ($\\chi^2 = 562.7$, $p < 10^{-124}$; \\Cref{sec:temporal}).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\\enlargethispage*{20\\baselineskip}\n\n\\subsection{What Drives Temporal DIF?}\n\\label{sec:disc_temporal}\n\n\\looseness=-1\nTemporal DIF detects \\emph{that} items function differently across cohorts, not \\emph{why}. Three non-exclusive mechanisms may drive the observed ${\\approx}$27--29\\% rate: (1)~differential contamination; (2)~capability evolution; (3)~training methodology shifts. The ETS baseline of 5--15\\% C\\%~\\citep{clauser1998dif} is for concurrent demographic groups; the comparison to temporal LLM cohorts is illustrative, not normative.\n\n\\looseness=-1\nFour exclusion arguments constrain this ambiguity: ability confounds explain at most 2.4~pp (matched C\\% $= 28.9\\%$; \\Cref{sec:temporal}); domain-level improvement explains ${<}0.1\\%$ of item-level DIF variance ($R^2 = 0.0007$); no enrichment among expert-annotated errors~\\citep{gema2024mmlu} ($= 1.10$, $p = 0.23$); web-overlap labels~\\citep{li2024contamination} are near-independent (Jaccard $= 0.206$; \\Cref{sec:groundtruth}).\n\n\\looseness=-1\nThe aggregate difficulty--direction interaction ($\\rho = -0.597$, robust at $[0.2, 0.8]$: $\\rho = -0.447$, $p < 10^{-100}$; \\Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\\Cref{sec:semisynthetic}) shows uniform injection also produces $\\rho \\approx -0.52$ via ceiling effects, while difficulty-dependent injection yields $\\rho \\approx +0.77$ (zero overlap across seeds); the observed $\\rho$ cannot alone distinguish contamination from capability evolution~\\citep{suk2026rethinking}. The aggregate $\\rho \\approx 0.997$ masks subject-level instability (22/57 below 0.95; five below 0.90), motivating targeted replacement~\\citep{zhao2025mmlucf,habba2026growingpains}.\n\n\\looseness=-1\nStratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring with a strong difficulty gradient ($\\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\\% focal-favoring with a near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above.\n\n\\subsection{Recommended DIF Audit Protocol}\n\\label{sec:disc_protocol}\n\n\\looseness=-1\nItem-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \\Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation}), with three action levels (calibrate via $\\rho$-degradation; \\Cref{app:fig_rho_degradation}): \\emph{Monitor} (C\\% $< 15\\%$), \\emph{Flag} ($15$--$25\\%$: dual rankings), \\emph{Act} ($\\geq 25\\%$: stable-item rankings). Difficulty--direction and model-type signals (\\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\\Cref{app:fig_downstream}), motivating equating~\\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\\rho = 0.95$).\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " The aggregate difficulty--direction interaction ($\\rho = -0.597$, robust at $[0.2, 0.8]$: $\\rho = -0.447$, $p < 10^{-100}$; \\Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\\Cref{sec:semisynthetic}) shows uniform injection also produces $\\rho \\approx -0.52$ via ceiling effects, while difficulty-dependent injection yields $\\rho \\approx +0.77$ (zero overlap across seeds); the observed $\\rho$ cannot alone distinguish contamination from capability evolution~\\citep{suk2026rethinking}. The aggregate $\\rho \\approx 0.997$ masks subject-level instability (22/57 below 0.95; five below 0.90), motivating targeted replacement~\\citep{zhao2025mmlucf,habba2026growingpains}.",
          " ",
          " \\looseness=-1",
          "-Stratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring with a strong difficulty gradient ($\\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\\% focal-favoring with a near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above.",
          "+Stratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring with a strong difficulty gradient ($\\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\\% focal-favoring with a near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above. An alternative explanation---that easy items are uniformly contaminated ($\\to$ DIF-A) while hard items are differentially contaminated ($\\to$ DIF-C)---is partially addressed by this base-vs-instruct direction reversal: under a pure difficulty-dependent contamination account, both model types should exhibit the same DIF direction, yet we observe opposite patterns ($\\chi^2 = 562.7$, $p < 10^{-124}$; \\Cref{sec:temporal}).",
          " ",
          " \\subsection{Recommended DIF Audit Protocol}",
          " \\label{sec:disc_protocol}"
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01PujKiL9zGTq3k3w4rCX6wb`</summary>

```json
{
  "command": "git add paper/sections/discussion.tex && git commit -m \"[paper] B1: Add difficulty-dependent contamination alternative explanation to §5.1\"",
  "description": "Commit B1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "b2c2bc72-9e1d-468f-8b02-dcf4881ad5eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3mj18qQgePgbQUaWjY9DQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 41507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 29 · 2026-05-22T20:42:48.924Z_

<details><summary>↩ Tool result · `toolu_01PujKiL9zGTq3k3w4rCX6wb`</summary>

```text
[rebuttal-b1-b7 7403f00] [paper] B1: Add difficulty-dependent contamination alternative explanation to §5.1
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "04d35ea8-b71a-441a-a017-422e2e147011",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 7403f00] [paper] B1: Add difficulty-dependent contamination alternative explanation to §5.1\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 1 insertion(+), 1 deletion(-)",
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

**B2**: Mark GSM1K as exploratory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "4ee1fa7a-bf58-4b34-839e-da693f8a0689",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6w1DFcozbGdv6eyTyfibb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 42817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 289
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01DhMLjJCqaHV9Zp6AajQXTg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "old_string": "Semi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}); GSM1K analysis ($r = -0.478$, $p = 0.005$; \\Cref{app:fig_gsm1k}) suggests DIF captures beyond memorization.",
  "new_string": "Semi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}). As an exploratory cross-benchmark signal, GSM1K contamination gaps correlate with DIF-C item accuracy ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{app:fig_gsm1k}), but the small sample requires replication."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "df90cd8a-0bd3-4728-8e99-d1998e65c138",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6w1DFcozbGdv6eyTyfibb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 42817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 289
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

### Tool result

_source line 32 · 2026-05-22T20:42:56.215Z_

<details><summary>↩ Tool result · `toolu_01DhMLjJCqaHV9Zp6AajQXTg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "9dda4ec1-deac-42c5-86bb-b82e9ddbcb02",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "oldString": "Semi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}); GSM1K analysis ($r = -0.478$, $p = 0.005$; \\Cref{app:fig_gsm1k}) suggests DIF captures beyond memorization.",
    "newString": "Semi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}). As an exploratory cross-benchmark signal, GSM1K contamination gaps correlate with DIF-C item accuracy ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{app:fig_gsm1k}), but the small sample requires replication.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH response matrix~\\citep{kipnis2024metabench} (5,227 models $\\times$ 12,508 MMLU items~\\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\n\\looseness=-1\nAs approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\\citep{zhou2026psnirt} ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \\geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ (details in \\Cref{app:method_details}). Our temporal cohorts ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\\Cref{app:power_sensitivity}).\n\n\\subsection{Temporal Comparability: 31\\% Measurement Instability}\n\\label{sec:temporal}\n\n\\looseness=-1\nWe compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 95\\% bootstrap CI: [29.4\\%, 38.1\\%]; family-level cluster bootstrap CI $[26.7\\%, 53.2\\%]$). Two independent non-independence corrections converge on approximately 27--29\\%: simple-mean DEFF correction (29.2\\%) and family-level cluster bootstrap lower bound (26.7\\%). The weighted-mean DEFF variant yields 13.5\\%, but its effective cluster size ($\\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\\rho_s = -0.009$, $p = 0.96$; \\Cref{app:icc_family}), so the weighted variant over-corrects. The $[13.5\\%, 29.2\\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ unchanged). We adopt ${\\approx}$27--29\\% as our primary estimate, with 13.5\\% as a lower bound under weighted-mean DEFF (\\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp). Graduated de-duplication independently confirms C\\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\\,pp across random draws (\\Cref{app:dedup_k}). C\\% is stable across $K \\geq 5$ (31.3\\%--35.9\\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, consistent with residual non-uniform DIF that MH does not capture, while $K{=}3$ inflates to 39.4\\% from under-stratification.\n\n\\looseness=-1\nThree controls confirm genuine temporal change (\\Cref{tab:temporal_landscape}): random splits yield C\\% of 0.18\\% (2023) and 1.3\\% (2024), both ${\\geq}23\\times$ below temporal C\\%; ability-quintile comparison yields 2.9\\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\\% $= 28.9\\% \\pm 0.1\\%$, confirming at most ${\\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \\Cref{app:method_details}).\n\n\\looseness=-1\nAcross all 57 subjects, C\\% ranges from 20.7\\% to 48.4\\% (mean $\\approx 30\\%$; \\Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \\emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\\%), Humanities favor 2023 (64.4\\%). Domain-level accuracy gains explain ${<}0.1\\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is associated with item properties rather than aggregate gains (OR reverses from 1.55 to 0.73 after controlling for difficulty; \\Cref{app:structural}). A difficulty--direction interaction emerges ($\\rho = -0.597$): 2024 models gain on hard items while eroding on easy ones. The conclusion is robust across thresholds ($18.3\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 2.0$, $10.2\\%$ at $\\geq 2.5$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. C\\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \\citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\\ labels are not applicable.}\n\\label{tab:temporal_landscape}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & C\\% & C\\% (web-clean) & Enrich. \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split 2023 (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nRandom split 2024 (sanity) & ${\\sim}$400 / ${\\sim}$400 & 1.3 & -- & -- \\\\\nWithin-subject (avg, 5 subj.) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\n\\looseness=-1\nDirect comparison of DIF flags against the web-overlap labels of \\citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (bootstrap 95\\% CI: $[0.94, 1.02]$; \\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\\% among web-contaminated items and 31.8\\% among clean items. Association tests confirm near-independence ($\\phi = 0.012$, OR $= 1.05$ [0.96, 1.15], Jaccard $= 0.206$, within permutation null $[0.203, 0.222]$; $p = 0.88$). This near-independence holds across contamination subtypes. The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \\emph{global exposure} (whether an item exists in training corpora), while DIF measures \\emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The two constructs---global exposure and differential functioning---are empirically orthogonal.\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\n\\looseness=-1\nTwo structural controls and a sensitivity check fail to reduce temporal C\\% below 31\\% (\\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\\% $= 38.1\\%$; cross-subject C\\% is more conservative due to lower local dependence), and IRT $\\theta$-conditioning ($r(\\theta, \\mathrm{total\\ score}) = 0.9986$). Logistic regression on nine subjects (1{,}787 items; 9/57---full-benchmark rates require further analysis) detects an additional 17.7\\% with non-uniform DIF ($|\\beta_{\\mathrm{interaction}}| \\geq 0.5$; effect-size criterion; LR $p$-values not adjusted for clustering); the union reaches 47\\% (Jaccard $= 0.28$): ${\\approx}$27--29\\% uniform (MH) plus 17.7\\% non-uniform (interaction-only), mutually exclusive by construction. Ability-matched analysis yields C\\% $= 28.9\\%$ (temporal) and $28.3\\%$ (Llama-2 vs.\\ 3)---consistent matched values (${\\sim}$28--29\\%) despite vastly different unmatched rates (\\Cref{app:structural}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\\% below 31\\%; $\\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}\n\\label{tab:structural_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temp.\\ C\\% & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (ext.) & Cross-bench.\\ total score & $0.314_{\\pm.009}$ & $0.834_{\\pm.027}$ & Reference \\\\\nMatched-ability & Within-quintile temp.\\ DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-cond.\\ (sens.) & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\n\\looseness=-1\nCross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$, upper-bound estimate under uniform binary flipping; \\Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ on average. The $\\Delta\\mathrm{FPR} = 0$ guarantee holds for single-subject contamination ($k \\leq 5$, $\\Delta\\mathrm{FPR} < 0.007$). Under broader contamination spanning $k = 10$ subjects (18\\% of domains), $\\Delta\\mathrm{FPR}$ rises to $0.047 \\pm 0.022$; at $k = 20$, to $0.069 \\pm 0.018$ (\\Cref{tab:multi_subject_injection,app:fig_matching}). Even worst-case multi-subject inflation ($\\sim$7~pp) cannot account for the observed 31\\% C\\% rate, which exceeds the 0.18\\% random baseline by ${>}170\\times$. Under DEFF adjustment, worst-case $\\Delta\\mathrm{FPR}$ at $k{=}20$ (0.069) represents up to 50\\% of the 13.5\\% lower bound, underscoring $k \\leq 5$ in practice. Difficulty-dependent injection produces distinguishable $\\rho$ signatures (capability-like: $+0.77$ vs.\\ contamination-like: $-0.52$; zero seed overlap), though mapping to real-data mechanisms requires further work.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\n\\looseness=-1\nStable-item ranks are preserved across all six benchmarks ($\\rho = 0.997$, $\\tau = 0.958$; flip rate $\\leq 2.8\\%$; \\Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\\ random removal; \\Cref{app:fig_downstream}). Among the 200 most displaced models (top 3.8\\%), 33.6\\% of pairwise rankings reverse, concentrating among closely-ranked pairs (35.2\\% at $\\Delta\\mathrm{rank} < 50$ vs.\\ 0.0\\% above 1000; \\Cref{app:rank_reversal}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\\times$ random; $p < 0.001$).\n\n\\subsection{Cross-Benchmark Validation}\n\\label{sec:gsm8k}\n\n\\looseness=-1\nTemporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six METABENCH benchmarks. C\\% = ETS~C items ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) between 2023 and 2024 cohorts; $\\rho$/$\\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\\%/Rand.\\ C\\%, with baseline varying by benchmark. All six show substantial DIF (45--174$\\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\\% than procedural ones.}\n\\label{tab:cross_benchmark}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrl}\n\\toprule\nBenchmark & Items & C\\% & $\\rho$ & $\\tau$ & Flip\\% & Rand.\\ C\\% & Ratio \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.18 & 174$\\times$ \\\\\nWinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\\times$ \\\\\nARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSemi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}); GSM1K analysis ($r = -0.478$, $p = 0.005$; \\Cref{app:fig_gsm1k}) suggests DIF captures beyond memorization.\n",
    "structuredPatch": [
      {
        "oldStart": 115,
        "oldLines": 4,
        "newStart": 115,
        "newLines": 4,
        "lines": [
          " \\end{tabular}}",
          " \\end{table}",
          " ",
          "-Semi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}); GSM1K analysis ($r = -0.478$, $p = 0.005$; \\Cref{app:fig_gsm1k}) suggests DIF captures beyond memorization.",
          "+Semi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}). As an exploratory cross-benchmark signal, GSM1K contamination gaps correlate with DIF-C item accuracy ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{app:fig_gsm1k}), but the small sample requires replication."
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

<details open><summary>🔧 Tool call — Bash · `toolu_018V83krPSwBQBct5q6u1MKd`</summary>

```json
{
  "command": "git add paper/sections/experiments.tex && git commit -m \"[paper] B2: Mark GSM1K analysis as exploratory with replication caveat\"",
  "description": "Commit B2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "a54c1554-be61-42b3-8f0f-a662294722e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9ha7asgFwbiuUJ48t739N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 43106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 34 · 2026-05-22T20:42:59.663Z_

<details><summary>↩ Tool result · `toolu_018V83krPSwBQBct5q6u1MKd`</summary>

```text
[rebuttal-b1-b7 55e0e23] [paper] B2: Mark GSM1K analysis as exploratory with replication caveat
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "fc739be4-7b81-45f6-8fdd-aac1f9fe2bd3",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 55e0e23] [paper] B2: Mark GSM1K analysis as exploratory with replication caveat\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 1 insertion(+), 1 deletion(-)",
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

_source line 35_

**B3**: Reduce `\enlargethispage*{20\baselineskip}` to 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "bda5b85c-2fa4-4d54-8339-f8d36cce6e61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsrFDMf1h8YU9swbDzYRpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 43535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01JHzt5XtbUC69NpYiE6unaJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "old_string": "\\enlargethispage*{20\\baselineskip}",
  "new_string": "\\enlargethispage*{4\\baselineskip}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "1e9c68f1-364a-4903-8628-94f2661f3bc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsrFDMf1h8YU9swbDzYRpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 43535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
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

### Tool result

_source line 37 · 2026-05-22T20:43:03.084Z_

<details><summary>↩ Tool result · `toolu_01JHzt5XtbUC69NpYiE6unaJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "a2a98521-d397-4d28-ad26-594eafb150f3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "oldString": "\\enlargethispage*{20\\baselineskip}",
    "newString": "\\enlargethispage*{4\\baselineskip}",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\\enlargethispage*{20\\baselineskip}\n\n\\subsection{What Drives Temporal DIF?}\n\\label{sec:disc_temporal}\n\n\\looseness=-1\nTemporal DIF detects \\emph{that} items function differently across cohorts, not \\emph{why}. Three non-exclusive mechanisms may drive the observed ${\\approx}$27--29\\% rate: (1)~differential contamination; (2)~capability evolution; (3)~training methodology shifts. The ETS baseline of 5--15\\% C\\%~\\citep{clauser1998dif} is for concurrent demographic groups; the comparison to temporal LLM cohorts is illustrative, not normative.\n\n\\looseness=-1\nFour exclusion arguments constrain this ambiguity: ability confounds explain at most 2.4~pp (matched C\\% $= 28.9\\%$; \\Cref{sec:temporal}); domain-level improvement explains ${<}0.1\\%$ of item-level DIF variance ($R^2 = 0.0007$); no enrichment among expert-annotated errors~\\citep{gema2024mmlu} ($= 1.10$, $p = 0.23$); web-overlap labels~\\citep{li2024contamination} are near-independent (Jaccard $= 0.206$; \\Cref{sec:groundtruth}).\n\n\\looseness=-1\nThe aggregate difficulty--direction interaction ($\\rho = -0.597$, robust at $[0.2, 0.8]$: $\\rho = -0.447$, $p < 10^{-100}$; \\Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\\Cref{sec:semisynthetic}) shows uniform injection also produces $\\rho \\approx -0.52$ via ceiling effects, while difficulty-dependent injection yields $\\rho \\approx +0.77$ (zero overlap across seeds); the observed $\\rho$ cannot alone distinguish contamination from capability evolution~\\citep{suk2026rethinking}. The aggregate $\\rho \\approx 0.997$ masks subject-level instability (22/57 below 0.95; five below 0.90), motivating targeted replacement~\\citep{zhao2025mmlucf,habba2026growingpains}.\n\n\\looseness=-1\nStratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring with a strong difficulty gradient ($\\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\\% focal-favoring with a near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above. An alternative explanation---that easy items are uniformly contaminated ($\\to$ DIF-A) while hard items are differentially contaminated ($\\to$ DIF-C)---is partially addressed by this base-vs-instruct direction reversal: under a pure difficulty-dependent contamination account, both model types should exhibit the same DIF direction, yet we observe opposite patterns ($\\chi^2 = 562.7$, $p < 10^{-124}$; \\Cref{sec:temporal}).\n\n\\subsection{Recommended DIF Audit Protocol}\n\\label{sec:disc_protocol}\n\n\\looseness=-1\nItem-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \\Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation}), with three action levels (calibrate via $\\rho$-degradation; \\Cref{app:fig_rho_degradation}): \\emph{Monitor} (C\\% $< 15\\%$), \\emph{Flag} ($15$--$25\\%$: dual rankings), \\emph{Act} ($\\geq 25\\%$: stable-item rankings). Difficulty--direction and model-type signals (\\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\\Cref{app:fig_downstream}), motivating equating~\\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\\rho = 0.95$).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\section{Discussion}",
          " \\label{sec:discussion}",
          "-\\enlargethispage*{20\\baselineskip}",
          "+\\enlargethispage*{4\\baselineskip}",
          " ",
          " \\subsection{What Drives Temporal DIF?}",
          " \\label{sec:disc_temporal}"
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_013guP1Tm2r6CLrqmiJ9ciap`</summary>

```json
{
  "command": "git add paper/sections/discussion.tex && git commit -m \"[paper] B3: Reduce excessive enlargethispage values\"",
  "description": "Commit B3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "b6a8d7a7-8263-43a7-8788-d567208bbfd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzNiqQH9PT6Md3povwT9xu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 43827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 39 · 2026-05-22T20:43:05.926Z_

<details><summary>↩ Tool result · `toolu_013guP1Tm2r6CLrqmiJ9ciap`</summary>

```text
[rebuttal-b1-b7 34070d0] [paper] B3: Reduce excessive enlargethispage values
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "46424e0a-6bbc-4531-aba7-6a119e145fa5",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 34070d0] [paper] B3: Reduce excessive enlargethispage values\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 1 insertion(+), 1 deletion(-)",
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

_source line 40_

**B4**: Add half-year C% explanation. No existing half-year content, so adding to appendix uncertainty section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "8b339951-6226-4a22-834e-f221cb98471a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015p41pjKSjN16XwmA1EBzsa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 44085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01HL2midWNA3U9maaB4WfajK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "old_string": "The cluster bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples",
  "new_string": "\\paragraph{Half-year granularity.} Splitting at the 6-month boundary yields C\\% $= 34.4\\%$, slightly above the annual 31.3\\%. The higher rate likely reflects more polarized cohort composition: fewer models span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates.\n\nThe cluster bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "5baf7985-d636-4305-9440-b3d1678b09b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015p41pjKSjN16XwmA1EBzsa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 44085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

### Tool result

_source line 42 · 2026-05-22T20:43:14.149Z_

<details><summary>↩ Tool result · reported error · `toolu_01HL2midWNA3U9maaB4WfajK`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: The cluster bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "56ae653b-42b8-4a15-b9ea-c1a63c19fbba",
  "tool_use_result": "Error: String to replace not found in file.\nString: The cluster bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples"
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01WZVR5fFcse8eMPeEi1rvTS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "offset": 163,
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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "7bb7e0df-ad61-40c5-a14a-05a9f59ce2d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7vYXqDeEEB39bPXgXDqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 44364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 44 · 2026-05-22T20:43:17.430Z_

<details><summary>↩ Tool result · `toolu_01WZVR5fFcse8eMPeEi1rvTS`</summary>

```text
163	\label{tab:uncertainty}
164	\end{table}
165	
166	The cluster bootstrap upper bound (53.2\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\%) and simple-mean DEFF adjustment (29.2\%)---converge on $\sim$27--29\%, establishing a robust corrected estimate that remains $>$150$\times$ the random-split baseline (0.18\%). Graduated de-duplication at $K{=}20$ yields C\% $= 19.7\% \pm 0.9\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \approx 450$ vs.\ 1,887), but within-$K$ variance ${<}1.5$\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\%) represents a conservative extreme; even this lower bound exceeds the baseline by 75$\times$.
167	
168	\section{Cross-Benchmark Comparison}
169	\label{app:gsm8k_details}
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "4570ced9-188d-4ebb-b89d-96b146667f32",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
      "content": "\\label{tab:uncertainty}\n\\end{table}\n\nThe cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\\%) and simple-mean DEFF adjustment (29.2\\%)---converge on $\\sim$27--29\\%, establishing a robust corrected estimate that remains $>$150$\\times$ the random-split baseline (0.18\\%). Graduated de-duplication at $K{=}20$ yields C\\% $= 19.7\\% \\pm 0.9\\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \\approx 450$ vs.\\ 1,887), but within-$K$ variance ${<}1.5$\\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\\%) represents a conservative extreme; even this lower bound exceeds the baseline by 75$\\times$.\n\n\\section{Cross-Benchmark Comparison}\n\\label{app:gsm8k_details}\n",
      "numLines": 8,
      "startLine": 163,
      "totalLines": 243
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01QR4LxmAunh8WJRugMLvvff`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "old_string": "The cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples",
  "new_string": "\\paragraph{Half-year granularity.} Splitting at the 6-month boundary yields C\\% $= 34.4\\%$, slightly above the annual 31.3\\%. The higher rate likely reflects more polarized cohort composition: fewer models span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates.\n\nThe cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "efea8216-6c71-4540-9236-efac197399de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZxkfrXJJSnMyJKrEXbjcp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 44827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 474
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

_source line 46 · 2026-05-22T20:43:22.912Z_

<details><summary>↩ Tool result · `toolu_01QR4LxmAunh8WJRugMLvvff`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "41131af2-0c12-4e55-9a61-cd2f87771b79",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
    "oldString": "The cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples",
    "newString": "\\paragraph{Half-year granularity.} Splitting at the 6-month boundary yields C\\% $= 34.4\\%$, slightly above the annual 31.3\\%. The higher rate likely reflects more polarized cohort composition: fewer models span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates.\n\nThe cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples",
    "originalFile": "\\section{Method Details}\n\\label{app:method_details}\n\n\\subsection{Diagnostics}\n\\label{app:diagnostics}\n\nThree diagnostic procedures complement the primary DIF analysis.\n\n\\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\\theta$ captures, which could inflate within-subject DIF rates.\n\n\\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\\rho$ between subject-level C\\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.\n\n\\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\\% measures the contribution of domain-level improvement to the total instability.\n\n\\subsection{Statistical Considerations}\n\\label{app:statistical}\n\n\\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.\n\n\\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\\Delta_{\\mathrm{MH}}| \\in \\{1.0, 1.5, 2.0, 2.5\\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ corresponds to the ETS~C definition used throughout the paper.\n\n\\paragraph{IRT model fit.} For transparency, we report that the MMLU response matrix shows poor fit to a unidimensional 2PL model (expected for a 57-subject multidimensional benchmark). This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.\n\n\\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.\n\n\\paragraph{Power sensitivity to item discrimination.}\n\\label{app:power_sensitivity}\nThe Monte Carlo power analysis in \\Cref{sec:validation} uses average 2PL parameters ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$). \\Cref{tab:power_sensitivity} reports TPR as a function of discrimination $a$ (other parameters at their means, $N = 80$ per cohort, $|\\Delta_b| = 1.4$, 1,000 replications). TPR increases monotonically from 0.40 ($a = 0.5$) to 0.95 ($a = 2.0$); FPR remains below 0.04 throughout. The MMLU item pool shows substantial heterogeneity: $a$ ranges from 0.006 to 2.657 (SD $= 0.54$, IQR $= [0.75, 1.64]$). The aggregate TPR of 0.68 from Phase~2 reflects this full distribution, while TPR at mean $a \\approx 1.2$ is 0.87---the gap is consistent with Jensen's inequality applied to the concave TPR($a$) function. Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation: parametric estimates (TPR $= 0.68$--$0.80$) are validated by empirical semi-synthetic injection ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{sec:semisynthetic}), confirming adequate detection power regardless of parametric assumptions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Power sensitivity to item discrimination. TPR = true positive rate for ETS~C detection ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) at $N = 80$ per cohort, $|\\Delta_b| = 1.4$, 1,000 replications.}\n\\label{tab:power_sensitivity}\n\\small\n\\begin{tabular}{rccc}\n\\toprule\n$a$ & TPR & 95\\% CI & FPR \\\\\n\\midrule\n0.5 & 0.398 & [0.20, 0.60] & 0.033 \\\\\n0.8 & 0.683 & [0.45, 0.90] & 0.036 \\\\\n1.0 & 0.808 & [0.60, 0.95] & 0.038 \\\\\n1.2 ($\\approx \\bar{a}$) & 0.874 & [0.70, 1.00] & 0.038 \\\\\n1.5 & 0.930 & [0.80, 1.00] & 0.038 \\\\\n2.0 & 0.949 & [0.80, 1.00] & 0.037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Nearest-neighbor matching.} The 1:1 nearest-neighbor matching selects, for each focal-cohort model, the reference-cohort model with the closest total score (caliper of 0.02 on normalized accuracy, approximately 0.14~SD). Balance is verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding.\n\n\\paragraph{Logistic regression specification.} The Simpson's paradox analysis (\\Cref{sec:temporal}) uses binary logistic regression with DIF-C classification as the dependent variable, domain-level accuracy change (2024 minus 2023 mean accuracy) as the primary predictor, and item difficulty (proportion correct) and IRT discrimination (point-biserial correlation) as controls. The interaction between domain accuracy change and item difficulty is included. Non-uniform DIF detection (\\Cref{sec:structural}) uses logistic regression with a group $\\times$ ability interaction term; a significant interaction ($p < 0.05$) indicates non-uniform DIF.\n\n\\section{Structural Analysis Details}\n\\label{app:structural}\n\nTwo structural controls and a sensitivity check fail to reduce the temporal C\\% below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal C\\% unchanged at approximately 0.31. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\\% $= 38.1\\%$, exceeding the 25\\% threshold that would indicate viable bifactor structure. As a sensitivity check, IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and C\\% $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. \\Cref{tab:structural_comparison} summarizes these results.\n\nThe temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\\ 2.2\\% cross-subject; $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\\% persists under external matching (full Q3 distributions available in the supplementary material).\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level Cohen's $d$ between 2023 and 2024 cohorts. The narrow range ($0.12$) indicates nearly uniform improvement across domains, supporting total-score matching adequacy for DIF analysis (\\Cref{sec:method}).}\n\\label{tab:domain_cohens_d}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nDomain & Cohen's $d$ \\\\\n\\midrule\nSTEM & 0.261 \\\\\nHumanities & 0.159 \\\\\nSocial Science & 0.147 \\\\\nOther & 0.146 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-subject injection robustness. $k$ = number of simultaneously contaminated subjects (out of 57); values are mean $\\pm$ SD across 5 random subject draws at exploitation rate $p = 0.5$.}\n\\label{tab:multi_subject_injection}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\n$k$ & $\\Delta\\mathrm{FPR}$ & $\\Delta\\mathrm{TPR}$ \\\\\n\\midrule\n1 & $0.000_{\\pm.000}$ & $0.371_{\\pm.048}$ \\\\\n3 & $0.003_{\\pm.002}$ & $0.385_{\\pm.031}$ \\\\\n5 & $0.007_{\\pm.003}$ & $0.392_{\\pm.027}$ \\\\\n10 & $0.047_{\\pm.022}$ & $0.401_{\\pm.024}$ \\\\\n20 & $0.069_{\\pm.018}$ & $0.410_{\\pm.020}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-family-out (LOFO) robustness on MMLU. Removing non-dominant families ($\\leq$15\\% of their cohort) changes C\\% by at most 2.93\\,pp. Larger shifts from removing Mistral or Llama-3 are driven almost entirely by family composition, not statistical power loss: Monte Carlo random-subsample calibration (200 replicates per scenario, matching the reduced sample size) shows the power effect is $\\leq$1\\,pp, while the composition effect accounts for 95--113\\% of the observed C\\% drop (Mistral: $-8.44$\\,pp composition vs.\\ $-0.41$\\,pp power; Llama-3: $-8.17$\\,pp vs.\\ ${+}0.91$\\,pp; observed C\\% falls below the 95\\% random-subsample range in both cases). Stratification uses total test score for computational efficiency; cross-subject matching yields identical baseline C\\%.}\n\\label{tab:lofo}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\nFamily & $N$ removed & Cohort share & C\\% (LOFO) \\\\\n\\midrule\n\\emph{Full sample} & --- & --- & 31.32 \\\\\nMistral & 547 & 51\\% ref & 22.47 \\\\\nLlama-3 & 315 & 39\\% foc & 24.06 \\\\\nMixtral & 120 & 15\\% foc & 34.26 \\\\\nLlama-2 & 161 & 15\\% ref & 31.48 \\\\\nSolar & 91 & 11\\% foc & 31.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Design Effect Estimation}\n\\label{app:deff}\n\nModel families (e.g., Mistral, Llama-3) induce intra-class correlation (ICC) that inflates Mantel-Haenszel $\\chi^2$ statistics beyond the nominal $\\chi^2_1$ reference distribution. We estimate the design effect (DEFF) per item following \\citet{rao1992variance}: $\\mathrm{DEFF}_i = 1 + (\\bar{m} - 1) \\cdot \\mathrm{ICC}_i$, where $\\bar{m}$ is the mean family size and $\\mathrm{ICC}_i$ is the one-way random-effects ICC for item $i$ across 30 families (restricted to ref+foc cohort; 1,884 models with family$\\geq$2).\n\nTwo estimates of $\\bar{m}$ bracket the adjustment: (1)~\\emph{Simple mean} ($\\bar{m} = 62.8$), treating all families equally, yields $\\mathrm{DEFF} = 3.87$ and adjusted C\\% $= 29.2\\%$; (2)~\\emph{Weighted mean} ($\\bar{m} = \\sum n_f^2 / \\sum n_f = 254.5$; \\citealp{kish1965survey}), reflecting the effective cluster size experienced by a randomly sampled model, yields $\\mathrm{DEFF} = 12.79$ and adjusted C\\% $= 13.5\\%$.\n\n\\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\\% of items exceed $0.10$). After dividing each item's $\\chi^2_{\\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\\% of items retain Category~C classification depending on the $\\bar{m}$ variant---both far exceeding the 0.18\\% random-split baseline (75--162$\\times$).\n\n\\paragraph{Size-stratified DEFF.} The aggregate ICC masks a size--ICC inverse relationship: smaller families exhibit higher within-family similarity (\\Cref{tab:deff_stratified}). Tier-level ICC ranges from 0.246 (2--10 members) to 0.082 ({>}200 members), reflecting greater heterogeneity in mega-families. At small family sizes, DEFF correction has negligible impact (Adj.\\ C\\% $= 31.3\\%$); the conservative 13.5\\% bound is driven entirely by the two mega-families (Mistral, Llama-3). Family definition sensitivity is minimal: merging sub-generations (e.g., Llama-2 + Llama-3) into coarse families (22 families) changes C\\% by $\\leq$0.3~pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\\ C\\% applies tier-specific DEFF to all items.}\n\\label{tab:deff_stratified}\n\\small\n\\begin{tabular}{lrrrrc}\n\\toprule\nTier & Families & $\\bar{m}$ & ICC & DEFF & Adj.\\ C\\% \\\\\n\\midrule\n2--10 & 9 & 5.3 & 0.246 & 2.07 & 31.3\\% \\\\\n11--50 & 11 & 22.1 & 0.226 & 5.78 & 24.6\\% \\\\\n51--200 & 8 & 91.4 & 0.137 & 13.34 & 13.7\\% \\\\\n${>}200$ & 2 & 431.0 & 0.082 & 36.11 & 9.0\\% \\\\\n\\midrule\nOverall & 30 & 62.8 & 0.047 & 3.87 & 29.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Uncertainty Quantification Comparison}\n\\label{app:uncertainty}\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison of uncertainty quantification methods for the 31.3\\% C\\% estimate on MMLU.}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llr}\n\\toprule\nMethod & Key assumption & Result \\\\\n\\midrule\nModel-level bootstrap & Models independent & 95\\% CI [29.4\\%, 38.1\\%] \\\\\nFamily-level cluster bootstrap & Family is clustering unit & 95\\% CI [26.7\\%, 53.2\\%] \\\\\nDEFF (simple $\\bar{m}$) & Equal-weight families & Adjusted C\\% = 29.2\\% \\\\\nDEFF (weighted $\\bar{m}$) & Size-proportional weighting & Adjusted C\\% = 13.5\\% \\\\\nGraduated de-dup.\\ ($K{=}20$) & Remove within-family duplicates & C\\% = 19.7\\% $\\pm$ 0.9\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\label{tab:uncertainty}\n\\end{table}\n\nThe cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\\%) and simple-mean DEFF adjustment (29.2\\%)---converge on $\\sim$27--29\\%, establishing a robust corrected estimate that remains $>$150$\\times$ the random-split baseline (0.18\\%). Graduated de-duplication at $K{=}20$ yields C\\% $= 19.7\\% \\pm 0.9\\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \\approx 450$ vs.\\ 1,887), but within-$K$ variance ${<}1.5$\\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\\%) represents a conservative extreme; even this lower bound exceeds the baseline by 75$\\times$.\n\n\\section{Cross-Benchmark Comparison}\n\\label{app:gsm8k_details}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal measurement instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\\pm$ values denote standard deviations across 5 random injection seeds.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.18\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\\pm.006}$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\\pm.027}$ & $+0.514_{\\pm.028}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Figures}\n\\label{app:figures}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{app:fig_matching}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}\n\\label{app:fig_downstream}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{Exploratory: GSM1K contamination gap vs.\\ DIF ranking advantage ($N = 33$; small sample, results should be interpreted cautiously). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items. Three of 33 models exceed the Cook's $D$ threshold ($4/N = 0.12$); leave-one-out analysis confirms all individual-removal correlations remain significant ($r \\in [-0.54, -0.37]$, all $p < 0.05$), and removing all three outliers yields $r = -0.38$ ($p = 0.036$, $N = 30$).}\n\\label{app:fig_gsm1k}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_A3_rho_degradation.pdf}\n\\caption{Ranking degradation under DIF-ordered vs.\\ random item removal across six benchmarks. DIF-ordered removal (orange) consistently degrades $\\rho$ faster than random removal (blue band = mean $\\pm$ 1 SD, 20 seeds). Vertical dashed lines mark the Monitor/Flag (15\\%) and Flag/Act (25\\%) thresholds from \\Cref{sec:disc_protocol}.}\n\\label{app:fig_rho_degradation}\n\\end{figure}\n\n\\section{Item-Property Predictive Analysis}\n\\label{app:predictive}\n\nTo test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \\pm 0.020$ (LR) and $0.599 \\pm 0.026$ (LightGBM)---near chance. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \\Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.\n\n\\section{Within-Family Similarity by Family Size}\n\\label{app:icc_family}\n\nWithin-family similarity (mean pairwise Pearson $r$ over 12{,}508-item response vectors) shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; 30 families with $\\geq 2$ members, 1{,}884 models). Large families (Mistral, $m = 547$, $\\bar{r} = 0.47$; Llama-3, $m = 315$, $\\bar{r} = 0.53$) are no more homogeneous than small or mid-sized families. Of the 5{,}227 models, 3{,}343 lack family assignments; these are retained in DIF analysis but excluded from similarity estimation. Within the temporal DIF cohorts ($N_{\\mathrm{ref}} + N_{\\mathrm{foc}} = 1{,}887$), 1{,}884 (99.8\\%) belong to identified families with $\\geq 2$ members, so DEFF estimates are computed over nearly the full cohort. This indicates that the weighted-mean DEFF variant's effective cluster size ($\\bar{m} = 254$) reflects an arithmetic artifact of mega-family dominance rather than genuine within-family homogeneity.\n\n\\section{Graduated De-Duplication Sensitivity}\n\\label{app:dedup_k}\n\nFor each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC\\% increases monotonically from 0.3\\% ($K = 1$) to 31.3\\% ($K = \\text{all}$). At each fixed $K$, variance across random member draws is negligible (SD ${<} 1.5$\\,pp), confirming that the signal scales with statistical power rather than within-family redundancy. At $K{=}20$, C\\% $= 19.7\\% \\pm 0.9\\%$ ($N \\approx 450$); the gap from the full-sample 31.3\\% reflects reduced power, not reduced bias.\n\n\\section{Rank-Reversal by Distance}\n\\label{app:rank_reversal}\n\nPairwise rank reversals between full-item and stable-item rankings concentrate among closely-ranked models. At $\\Delta\\mathrm{rank} < 50$ (mean $\\Delta\\mathrm{acc} = 0.003$, effectively statistical ties), the reversal rate is 35.2\\%. It drops to 15.1\\% for $\\Delta\\mathrm{rank} \\in [50, 200)$, 4.0\\% for $[200, 500)$, 0.6\\% for $[500, 1000)$, and 0.0\\% above 1000. Broad leaderboard structure is fully preserved; instability affects only models within each other's noise margin.\n\n",
    "structuredPatch": [
      {
        "oldStart": 163,
        "oldLines": 6,
        "newStart": 163,
        "newLines": 8,
        "lines": [
          " \\label{tab:uncertainty}",
          " \\end{table}",
          " ",
          "+\\paragraph{Half-year granularity.} Splitting at the 6-month boundary yields C\\% $= 34.4\\%$, slightly above the annual 31.3\\%. The higher rate likely reflects more polarized cohort composition: fewer models span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates.",
          "+",
          " The cluster bootstrap upper bound (53.2\\%) is driven by extreme bootstrap resamples that over-represent Mistral ($n = 547$) or Llama-3 ($n = 315$), producing atypical cohort compositions. Two independent methods---cluster bootstrap lower bound (26.7\\%) and simple-mean DEFF adjustment (29.2\\%)---converge on $\\sim$27--29\\%, establishing a robust corrected estimate that remains $>$150$\\times$ the random-split baseline (0.18\\%). Graduated de-duplication at $K{=}20$ yields C\\% $= 19.7\\% \\pm 0.9\\%$ (random member selection, 5 draws), lower than the corrected estimate due to reduced statistical power ($N \\approx 450$ vs.\\ 1,887), but within-$K$ variance ${<}1.5$\\,pp at all $K$ confirms the signal is power-driven rather than redundancy-inflated (\\Cref{app:dedup_k}). The weighted-mean DEFF (13.5\\%) represents a conservative extreme; even this lower bound exceeds the baseline by 75$\\times$.",
          " ",
          " \\section{Cross-Benchmark Comparison}"
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

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01XEMSvy1sJ7ApGQSNgsm9Qp`</summary>

```json
{
  "command": "git add paper/sections/appendix.tex && git commit -m \"[paper] B4: Explain half-year vs annual C% difference\"",
  "description": "Commit B4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "37013133-d7b2-401c-80d7-547ed6f5a053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fTfmMcwKmn726TN5JXKb2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 45301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 331
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 48 · 2026-05-22T20:43:26.074Z_

<details><summary>↩ Tool result · `toolu_01XEMSvy1sJ7ApGQSNgsm9Qp`</summary>

```text
[rebuttal-b1-b7 55c57c8] [paper] B4: Explain half-year vs annual C% difference
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 2 insertions(+)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "8f2f40b0-62dd-40dc-bae5-a5e5d1adf1ba",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 55c57c8] [paper] B4: Explain half-year vs annual C% difference\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 2 insertions(+)",
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

_source line 49_

**B5**: Soften ≥500 threshold.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "efcceb7a-a76e-4b5c-87ae-16f9c30fd3cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvqvJadVUXn3JP1WnFzBRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 45632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 280
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01RxpGkJ7kKVNTtQeMFxnVeL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "old_string": "We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation})",
  "new_string": "We recommend MH-DIF audits whenever $\\geq$500 models accumulate ($\\geq$80 per stratum for adequate MH power at $K{=}5$; smaller corpora may suffice with $K{=}3$ or $2{\\times}2$ designs; \\Cref{sec:validation})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "5bbe9d47-2214-4404-94eb-8c0ef07b4b52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvqvJadVUXn3JP1WnFzBRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 45632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 280
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

### Tool result

_source line 51 · 2026-05-22T20:43:42.981Z_

<details><summary>↩ Tool result · `toolu_01RxpGkJ7kKVNTtQeMFxnVeL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "1c0c65e6-deac-4f5a-b33c-1c8b8d5aadd0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "oldString": "We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation})",
    "newString": "We recommend MH-DIF audits whenever $\\geq$500 models accumulate ($\\geq$80 per stratum for adequate MH power at $K{=}5$; smaller corpora may suffice with $K{=}3$ or $2{\\times}2$ designs; \\Cref{sec:validation})",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\\enlargethispage*{4\\baselineskip}\n\n\\subsection{What Drives Temporal DIF?}\n\\label{sec:disc_temporal}\n\n\\looseness=-1\nTemporal DIF detects \\emph{that} items function differently across cohorts, not \\emph{why}. Three non-exclusive mechanisms may drive the observed ${\\approx}$27--29\\% rate: (1)~differential contamination; (2)~capability evolution; (3)~training methodology shifts. The ETS baseline of 5--15\\% C\\%~\\citep{clauser1998dif} is for concurrent demographic groups; the comparison to temporal LLM cohorts is illustrative, not normative.\n\n\\looseness=-1\nFour exclusion arguments constrain this ambiguity: ability confounds explain at most 2.4~pp (matched C\\% $= 28.9\\%$; \\Cref{sec:temporal}); domain-level improvement explains ${<}0.1\\%$ of item-level DIF variance ($R^2 = 0.0007$); no enrichment among expert-annotated errors~\\citep{gema2024mmlu} ($= 1.10$, $p = 0.23$); web-overlap labels~\\citep{li2024contamination} are near-independent (Jaccard $= 0.206$; \\Cref{sec:groundtruth}).\n\n\\looseness=-1\nThe aggregate difficulty--direction interaction ($\\rho = -0.597$, robust at $[0.2, 0.8]$: $\\rho = -0.447$, $p < 10^{-100}$; \\Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\\Cref{sec:semisynthetic}) shows uniform injection also produces $\\rho \\approx -0.52$ via ceiling effects, while difficulty-dependent injection yields $\\rho \\approx +0.77$ (zero overlap across seeds); the observed $\\rho$ cannot alone distinguish contamination from capability evolution~\\citep{suk2026rethinking}. The aggregate $\\rho \\approx 0.997$ masks subject-level instability (22/57 below 0.95; five below 0.90), motivating targeted replacement~\\citep{zhao2025mmlucf,habba2026growingpains}.\n\n\\looseness=-1\nStratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\\% reference-favoring with a strong difficulty gradient ($\\rho = -0.570$), consistent with differential memorization decay, while instruct models ($N{=}478$) are 65.6\\% focal-favoring with a near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$), consistent with uniform alignment improvements. The aggregate gradient is driven by base models; the instruct flat gradient is compatible with either capability gains or difficulty-independent memorization. This decomposition provides positive evidence for mechanism separation, complementing the exclusion arguments above. An alternative explanation---that easy items are uniformly contaminated ($\\to$ DIF-A) while hard items are differentially contaminated ($\\to$ DIF-C)---is partially addressed by this base-vs-instruct direction reversal: under a pure difficulty-dependent contamination account, both model types should exhibit the same DIF direction, yet we observe opposite patterns ($\\chi^2 = 562.7$, $p < 10^{-124}$; \\Cref{sec:temporal}).\n\n\\subsection{Recommended DIF Audit Protocol}\n\\label{sec:disc_protocol}\n\n\\looseness=-1\nItem-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \\Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation}), with three action levels (calibrate via $\\rho$-degradation; \\Cref{app:fig_rho_degradation}): \\emph{Monitor} (C\\% $< 15\\%$), \\emph{Flag} ($15$--$25\\%$: dual rankings), \\emph{Act} ($\\geq 25\\%$: stable-item rankings). Difficulty--direction and model-type signals (\\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\\Cref{app:fig_downstream}), motivating equating~\\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\\rho = 0.95$).\n",
    "structuredPatch": [
      {
        "oldStart": 21,
        "oldLines": 4,
        "newStart": 21,
        "newLines": 4,
        "lines": [
          " \\label{sec:disc_protocol}",
          " ",
          " \\looseness=-1",
          "-Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \\Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\\geq$500 models accumulate (ensuring $\\geq$80 per stratum at $K{=}5$; \\Cref{sec:validation}), with three action levels (calibrate via $\\rho$-degradation; \\Cref{app:fig_rho_degradation}): \\emph{Monitor} (C\\% $< 15\\%$), \\emph{Flag} ($15$--$25\\%$: dual rankings), \\emph{Act} ($\\geq 25\\%$: stable-item rankings). Difficulty--direction and model-type signals (\\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\\Cref{app:fig_downstream}), motivating equating~\\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\\rho = 0.95$).",
          "+Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \\Cref{app:predictive}), so monitoring cannot be replaced by pre-screening. We recommend MH-DIF audits whenever $\\geq$500 models accumulate ($\\geq$80 per stratum for adequate MH power at $K{=}5$; smaller corpora may suffice with $K{=}3$ or $2{\\times}2$ designs; \\Cref{sec:validation}), with three action levels (calibrate via $\\rho$-degradation; \\Cref{app:fig_rho_degradation}): \\emph{Monitor} (C\\% $< 15\\%$), \\emph{Flag} ($15$--$25\\%$: dual rankings), \\emph{Act} ($\\geq 25\\%$: stable-item rankings). Difficulty--direction and model-type signals (\\Cref{sec:disc_temporal}) inform triage; DIF removal is the least disruptive strategy (\\Cref{app:fig_downstream}), motivating equating~\\citep{kolen2014equating,habba2026growingpains}. Subject-level monitoring is essential (22/57 below $\\rho = 0.95$)."
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mrvs7g979SHMeNb33EsszU`</summary>

```json
{
  "command": "git add paper/sections/discussion.tex && git commit -m \"[paper] B5: Soften ≥500 threshold with smaller-corpus alternatives\"",
  "description": "Commit B5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "40c0084c-d26d-49eb-bc65-9333ae813ef3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017j1LjcoGQbvrvcfiZeM4SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 45912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 53 · 2026-05-22T20:43:45.384Z_

<details><summary>↩ Tool result · `toolu_01Mrvs7g979SHMeNb33EsszU`</summary>

```text
[rebuttal-b1-b7 53b10c2] [paper] B5: Soften ≥500 threshold with smaller-corpus alternatives
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "9689e25f-e9f8-421f-9a87-c88eaca54ac5",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 53b10c2] [paper] B5: Soften ≥500 threshold with smaller-corpus alternatives\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 1 insertion(+), 1 deletion(-)",
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

_source line 54_

**B6**: Empty commit for reference verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "41543409-6ec0-420b-8691-921ea766e683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnGHXXAAJAgJcNAkZvierw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 46259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
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

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01KxdfuZe66h9iSgCXDWrVZs`</summary>

```json
{
  "command": "git commit --allow-empty -m \"$(cat <<'EOF'\n[paper] B6: Reference verification — all 3 citations verified real\n\nAlzahrani et al. (2024): already in bib as alzahrani2024benchmarks\nMMLU-Pro (Wang et al., 2024): already in bib as wang2024mmlupro\nKamata & Binici (2003): real (IMPS 2003) but unpublished conference\nreport, not cited in text — not added\nEOF\n)\"",
  "description": "Commit B6 (empty, reference verification)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "51409e68-ab67-4acb-9079-afa6a3a1a721",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnGHXXAAJAgJcNAkZvierw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 46259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
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

### Tool result

_source line 56 · 2026-05-22T20:44:02.519Z_

<details><summary>↩ Tool result · `toolu_01KxdfuZe66h9iSgCXDWrVZs`</summary>

```text
[rebuttal-b1-b7 2ac5324] [paper] B6: Reference verification — all 3 citations verified real
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "ad7306f4-27de-480e-9fe1-8815adf0c109",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 2ac5324] [paper] B6: Reference verification — all 3 citations verified real\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author",
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

**B7**: Strengthen NUDIF caveat. Current wording in experiments.tex line 16: "consistent with residual non-uniform DIF that MH does not capture".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "854ac2c7-22a5-449a-bece-c6ee34c2db00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8jxt5i4n7sAqRvWRYHGW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 46551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01XB4TSvqjnPVXFk5Byzt5mA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "old_string": "consistent with residual non-uniform DIF that MH does not capture",
  "new_string": "which may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "8dcf08a3-dcfa-4dcf-b424-404dd9a47158",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8jxt5i4n7sAqRvWRYHGW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 46551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 59 · 2026-05-22T20:44:09.477Z_

<details><summary>↩ Tool result · `toolu_01XB4TSvqjnPVXFk5Byzt5mA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "09df35e3-b9b3-4bcd-b870-260e91e97714",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "oldString": "consistent with residual non-uniform DIF that MH does not capture",
    "newString": "which may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH response matrix~\\citep{kipnis2024metabench} (5,227 models $\\times$ 12,508 MMLU items~\\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\n\\looseness=-1\nAs approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\\citep{zhou2026psnirt} ($\\bar{a} = 1.2$, $\\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \\geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ (details in \\Cref{app:method_details}). Our temporal cohorts ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\\Cref{app:power_sensitivity}).\n\n\\subsection{Temporal Comparability: 31\\% Measurement Instability}\n\\label{sec:temporal}\n\n\\looseness=-1\nWe compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 95\\% bootstrap CI: [29.4\\%, 38.1\\%]; family-level cluster bootstrap CI $[26.7\\%, 53.2\\%]$). Two independent non-independence corrections converge on approximately 27--29\\%: simple-mean DEFF correction (29.2\\%) and family-level cluster bootstrap lower bound (26.7\\%). The weighted-mean DEFF variant yields 13.5\\%, but its effective cluster size ($\\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\\rho_s = -0.009$, $p = 0.96$; \\Cref{app:icc_family}), so the weighted variant over-corrects. The $[13.5\\%, 29.2\\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ unchanged). We adopt ${\\approx}$27--29\\% as our primary estimate, with 13.5\\% as a lower bound under weighted-mean DEFF (\\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp). Graduated de-duplication independently confirms C\\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\\,pp across random draws (\\Cref{app:dedup_k}). C\\% is stable across $K \\geq 5$ (31.3\\%--35.9\\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, consistent with residual non-uniform DIF that MH does not capture, while $K{=}3$ inflates to 39.4\\% from under-stratification.\n\n\\looseness=-1\nThree controls confirm genuine temporal change (\\Cref{tab:temporal_landscape}): random splits yield C\\% of 0.18\\% (2023) and 1.3\\% (2024), both ${\\geq}23\\times$ below temporal C\\%; ability-quintile comparison yields 2.9\\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\\% $= 28.9\\% \\pm 0.1\\%$, confirming at most ${\\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \\Cref{app:method_details}).\n\n\\looseness=-1\nAcross all 57 subjects, C\\% ranges from 20.7\\% to 48.4\\% (mean $\\approx 30\\%$; \\Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \\emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\\%), Humanities favor 2023 (64.4\\%). Domain-level accuracy gains explain ${<}0.1\\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); a Simpson's paradox confirms DIF is associated with item properties rather than aggregate gains (OR reverses from 1.55 to 0.73 after controlling for difficulty; \\Cref{app:structural}). A difficulty--direction interaction emerges ($\\rho = -0.597$): 2024 models gain on hard items while eroding on easy ones. The conclusion is robust across thresholds ($18.3\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 2.0$, $10.2\\%$ at $\\geq 2.5$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. C\\% (web-clean) is the DIF-C flagging rate among items classified as web-clean by \\citet{li2024contamination}. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels. Dashes (--) indicate comparisons where Li et al.\\ labels are not applicable.}\n\\label{tab:temporal_landscape}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & C\\% & C\\% (web-clean) & Enrich. \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split 2023 (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nRandom split 2024 (sanity) & ${\\sim}$400 / ${\\sim}$400 & 1.3 & -- & -- \\\\\nWithin-subject (avg, 5 subj.) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\n\\looseness=-1\nDirect comparison of DIF flags against the web-overlap labels of \\citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (bootstrap 95\\% CI: $[0.94, 1.02]$; \\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\\% among web-contaminated items and 31.8\\% among clean items. Association tests confirm near-independence ($\\phi = 0.012$, OR $= 1.05$ [0.96, 1.15], Jaccard $= 0.206$, within permutation null $[0.203, 0.222]$; $p = 0.88$). This near-independence holds across contamination subtypes. The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \\emph{global exposure} (whether an item exists in training corpora), while DIF measures \\emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The two constructs---global exposure and differential functioning---are empirically orthogonal.\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\n\\looseness=-1\nTwo structural controls and a sensitivity check fail to reduce temporal C\\% below 31\\% (\\Cref{tab:structural_comparison}): matched-ability quintiles, within-subject DIF (C\\% $= 38.1\\%$; cross-subject C\\% is more conservative due to lower local dependence), and IRT $\\theta$-conditioning ($r(\\theta, \\mathrm{total\\ score}) = 0.9986$). Logistic regression on nine subjects (1{,}787 items; 9/57---full-benchmark rates require further analysis) detects an additional 17.7\\% with non-uniform DIF ($|\\beta_{\\mathrm{interaction}}| \\geq 0.5$; effect-size criterion; LR $p$-values not adjusted for clustering); the union reaches 47\\% (Jaccard $= 0.28$): ${\\approx}$27--29\\% uniform (MH) plus 17.7\\% non-uniform (interaction-only), mutually exclusive by construction. Ability-matched analysis yields C\\% $= 28.9\\%$ (temporal) and $28.3\\%$ (Llama-2 vs.\\ 3)---consistent matched values (${\\sim}$28--29\\%) despite vastly different unmatched rates (\\Cref{app:structural}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural controls and sensitivity checks for temporal DIF. None reduces C\\% below 31\\%; $\\theta$-conditioning serves as a sensitivity check confirming total-score adequacy.}\n\\label{tab:structural_comparison}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temp.\\ C\\% & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (ext.) & Cross-bench.\\ total score & $0.314_{\\pm.009}$ & $0.834_{\\pm.027}$ & Reference \\\\\nMatched-ability & Within-quintile temp.\\ DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-cond.\\ (sens.) & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\n\\looseness=-1\nCross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$, upper-bound estimate under uniform binary flipping; \\Cref{sec:injection}), while within-subject matching inflates FPR by ${+}0.186$ on average. The $\\Delta\\mathrm{FPR} = 0$ guarantee holds for single-subject contamination ($k \\leq 5$, $\\Delta\\mathrm{FPR} < 0.007$). Under broader contamination spanning $k = 10$ subjects (18\\% of domains), $\\Delta\\mathrm{FPR}$ rises to $0.047 \\pm 0.022$; at $k = 20$, to $0.069 \\pm 0.018$ (\\Cref{tab:multi_subject_injection,app:fig_matching}). Even worst-case multi-subject inflation ($\\sim$7~pp) cannot account for the observed 31\\% C\\% rate, which exceeds the 0.18\\% random baseline by ${>}170\\times$. Under DEFF adjustment, worst-case $\\Delta\\mathrm{FPR}$ at $k{=}20$ (0.069) represents up to 50\\% of the 13.5\\% lower bound, underscoring $k \\leq 5$ in practice. Difficulty-dependent injection produces distinguishable $\\rho$ signatures (capability-like: $+0.77$ vs.\\ contamination-like: $-0.52$; zero seed overlap), though mapping to real-data mechanisms requires further work.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\n\\looseness=-1\nStable-item ranks are preserved across all six benchmarks ($\\rho = 0.997$, $\\tau = 0.958$; flip rate $\\leq 2.8\\%$; \\Cref{tab:cross_benchmark}). DIF-flagged items concentrate discriminative signal ($z = -8$ to $-49$ vs.\\ random removal; \\Cref{app:fig_downstream}). Among the 200 most displaced models (top 3.8\\%), 33.6\\% of pairwise rankings reverse, concentrating among closely-ranked pairs (35.2\\% at $\\Delta\\mathrm{rank} < 50$ vs.\\ 0.0\\% above 1000; \\Cref{app:rank_reversal}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\\times$ random; $p < 0.001$).\n\n\\subsection{Cross-Benchmark Validation}\n\\label{sec:gsm8k}\n\n\\looseness=-1\nTemporal DIF extends across all six METABENCH benchmarks (\\Cref{tab:cross_benchmark}): C\\% ranges from 17.9\\% (HellaSwag~\\citep{zellers2019hellaswag}) to 31.3\\% (MMLU), with knowledge/reasoning benchmarks consistently higher than procedural ones (C\\% $= 26.9$--$31.3\\%$ vs.\\ $17.9$--$18.9\\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six METABENCH benchmarks. C\\% = ETS~C items ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$) between 2023 and 2024 cohorts; $\\rho$/$\\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\\%/Rand.\\ C\\%, with baseline varying by benchmark. All six show substantial DIF (45--174$\\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\\% than procedural ones.}\n\\label{tab:cross_benchmark}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrl}\n\\toprule\nBenchmark & Items & C\\% & $\\rho$ & $\\tau$ & Flip\\% & Rand.\\ C\\% & Ratio \\\\\n\\midrule\nMMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.18 & 174$\\times$ \\\\\nWinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\\times$ \\\\\nARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSemi-synthetic injection on GSM8K confirms detection power ($\\Delta\\mathrm{TPR} = {+}0.514$; \\Cref{app:gsm8k_details}). As an exploratory cross-benchmark signal, GSM1K contamination gaps correlate with DIF-C item accuracy ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{app:fig_gsm1k}), but the small sample requires replication.\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " \\label{sec:temporal}",
          " ",
          " \\looseness=-1",
          "-We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 95\\% bootstrap CI: [29.4\\%, 38.1\\%]; family-level cluster bootstrap CI $[26.7\\%, 53.2\\%]$). Two independent non-independence corrections converge on approximately 27--29\\%: simple-mean DEFF correction (29.2\\%) and family-level cluster bootstrap lower bound (26.7\\%). The weighted-mean DEFF variant yields 13.5\\%, but its effective cluster size ($\\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\\rho_s = -0.009$, $p = 0.96$; \\Cref{app:icc_family}), so the weighted variant over-corrects. The $[13.5\\%, 29.2\\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ unchanged). We adopt ${\\approx}$27--29\\% as our primary estimate, with 13.5\\% as a lower bound under weighted-mean DEFF (\\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp). Graduated de-duplication independently confirms C\\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\\,pp across random draws (\\Cref{app:dedup_k}). C\\% is stable across $K \\geq 5$ (31.3\\%--35.9\\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, consistent with residual non-uniform DIF that MH does not capture, while $K{=}3$ inflates to 39.4\\% from under-stratification.",
          "+We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$; 95\\% bootstrap CI: [29.4\\%, 38.1\\%]; family-level cluster bootstrap CI $[26.7\\%, 53.2\\%]$). Two independent non-independence corrections converge on approximately 27--29\\%: simple-mean DEFF correction (29.2\\%) and family-level cluster bootstrap lower bound (26.7\\%). The weighted-mean DEFF variant yields 13.5\\%, but its effective cluster size ($\\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family similarity is flat across family sizes ($\\rho_s = -0.009$, $p = 0.96$; \\Cref{app:icc_family}), so the weighted variant over-corrects. The $[13.5\\%, 29.2\\%]$ range reflects power uncertainty, not DIF magnitude disagreement ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$ unchanged). We adopt ${\\approx}$27--29\\% as our primary estimate, with 13.5\\% as a lower bound under weighted-mean DEFF (\\Cref{app:deff,app:uncertainty}); even this bound exceeds the random-split baseline by $75\\times$. Leave-one-family-out analysis confirms no single family drives the signal ($|\\Delta\\mathrm{C\\%}| \\leq 2.93$\\,pp). Graduated de-duplication independently confirms C\\% scales with power, not family redundancy: at each fixed $K$, within-$K$ SD ${<}1.5$\\,pp across random draws (\\Cref{app:dedup_k}). C\\% is stable across $K \\geq 5$ (31.3\\%--35.9\\%; $K{=}5$ most conservative); the non-monotonic $K{=}10$ peak reflects ability--DIF interactions in finer strata, which may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation, while $K{=}3$ inflates to 39.4\\% from under-stratification.",
          " ",
          " \\looseness=-1",
          " Three controls confirm genuine temporal change (\\Cref{tab:temporal_landscape}): random splits yield C\\% of 0.18\\% (2023) and 1.3\\% (2024), both ${\\geq}23\\times$ below temporal C\\%; ability-quintile comparison yields 2.9\\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\\% $= 28.9\\% \\pm 0.1\\%$, confirming at most ${\\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \\Cref{app:method_details})."
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

<details open><summary>🔧 Tool call — Bash · `toolu_018CW1Mpj5DrrmvzP8v6aQdR`</summary>

```json
{
  "command": "git add paper/sections/experiments.tex && git commit -m \"[paper] B7: Strengthen NUDIF caveat in K-sensitivity paragraph\"",
  "description": "Commit B7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "98c9ba18-1171-47fc-b519-5d7f7faa8420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Lu9tfDGXkf5EGXybsRBnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 393,
      "cache_read_input_tokens": 46924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 393
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

_source line 61 · 2026-05-22T20:44:11.988Z_

<details><summary>↩ Tool result · `toolu_018CW1Mpj5DrrmvzP8v6aQdR`</summary>

```text
[rebuttal-b1-b7 4bbbb38] [paper] B7: Strengthen NUDIF caveat in K-sensitivity paragraph
 Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "c5c474a1-8203-4b2b-8849-184667474e09",
  "tool_use_result": {
    "stdout": "[rebuttal-b1-b7 4bbbb38] [paper] B7: Strengthen NUDIF caveat in K-sensitivity paragraph\n Committer: Ubuntu &lt;ubuntu@ip-172-31-8-29.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 1 insertion(+), 1 deletion(-)",
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

_source line 62_

All 7 commits done. Verifying and compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "04e57f5d-3a80-4582-bdd5-a4f68d327338",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RCymUXTUZYVLP9w7xDNb3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 47317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01U8whXWCxFE8DFLvDhZC5oQ`</summary>

```json
{
  "command": "git log --oneline rebuttal-b1-b7 ^master",
  "description": "List new commits on rebuttal-b1-b7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "dd06c8b5-ac3a-4195-8ebf-af58a76959d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RCymUXTUZYVLP9w7xDNb3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 47317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 64 · 2026-05-22T20:44:16.184Z_

<details><summary>↩ Tool result · `toolu_01U8whXWCxFE8DFLvDhZC5oQ`</summary>

```text
4bbbb38 [paper] B7: Strengthen NUDIF caveat in K-sensitivity paragraph
2ac5324 [paper] B6: Reference verification — all 3 citations verified real
53b10c2 [paper] B5: Soften ≥500 threshold with smaller-corpus alternatives
55c57c8 [paper] B4: Explain half-year vs annual C% difference
34070d0 [paper] B3: Reduce excessive enlargethispage values
55e0e23 [paper] B2: Mark GSM1K analysis as exploratory with replication caveat
7403f00 [paper] B1: Add difficulty-dependent contamination alternative explanation to §5.1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "f91fad18-41bb-4cc8-b957-a55b4ebe8fbd",
  "tool_use_result": {
    "stdout": "4bbbb38 [paper] B7: Strengthen NUDIF caveat in K-sensitivity paragraph\n2ac5324 [paper] B6: Reference verification — all 3 citations verified real\n53b10c2 [paper] B5: Soften ≥500 threshold with smaller-corpus alternatives\n55c57c8 [paper] B4: Explain half-year vs annual C% difference\n34070d0 [paper] B3: Reduce excessive enlargethispage values\n55e0e23 [paper] B2: Mark GSM1K analysis as exploratory with replication caveat\n7403f00 [paper] B1: Add difficulty-dependent contamination alternative explanation to §5.1",
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01NppbVW8tXH885qAD76QU1J`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile paper",
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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "0506c861-3c66-4b43-832e-a4e5d4560450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RCymUXTUZYVLP9w7xDNb3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 47317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bfbv3un4e",
  "tool_use_id": "toolu_01NppbVW8tXH885qAD76QU1J",
  "description": "Compile paper",
  "task_type": "local_bash",
  "uuid": "1d040aac-d92e-4ccf-8dd2-4e827a4df85f",
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f"
}
```

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bfbv3un4e",
  "tool_use_id": "toolu_01NppbVW8tXH885qAD76QU1J",
  "status": "completed",
  "output_file": "",
  "summary": "Compile paper",
  "uuid": "cfff738d-b9fc-41c8-9151-75a865bc6902",
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f"
}
```

---

### Tool result

_source line 68 · 2026-05-22T20:44:21.015Z_

<details><summary>↩ Tool result · `toolu_01NppbVW8tXH885qAD76QU1J`</summary>

```text
nts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier
/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (17 pages, 647936 bytes).
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
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "020829fc-8421-4441-9e14-f73e57e4050b",
  "tool_use_result": {
    "stdout": "nts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier\n/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (17 pages, 647936 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 69_

编译成功（17 页，无错误）。7 个 commit 汇总：

| Commit | SHA | 描述 |
|--------|-----|------|
| B1 | `7403f00` | §5.1 加 difficulty-dependent contamination 替代解释 |
| B2 | `55e0e23` | GSM1K 标记为 exploratory + replication caveat |
| B3 | `34070d0` | `\enlargethispage*{20}` → `{4}` |
| B4 | `55c57c8` | Appendix 加 half-year vs annual C% 解释 |
| B5 | `53b10c2` | ≥500 threshold 软化，加 K=3 / 2×2 alternatives |
| B6 | `2ac5324` | 引用验证 (empty commit)，3 篇均真实 |
| B7 | `4bbbb38` | K-sensitivity NUDIF caveat 措辞更明确 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "uuid": "2d86aab0-94d6-4f7c-9930-fe41ca63f2c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pchmytVXTykHc82b3TSCk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 47604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
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

_source line 70_

编译成功（17 页，无错误）。7 个 commit 汇总：

| Commit | SHA | 描述 |
|--------|-----|------|
| B1 | `7403f00` | §5.1 加 difficulty-dependent contamination 替代解释 |
| B2 | `55e0e23` | GSM1K 标记为 exploratory + replication caveat |
| B3 | `34070d0` | `\enlargethispage*{20}` → `{4}` |
| B4 | `55c57c8` | Appendix 加 half-year vs annual C% 解释 |
| B5 | `53b10c2` | ≥500 threshold 软化，加 K=3 / 2×2 alternatives |
| B6 | `2ac5324` | 引用验证 (empty commit)，3 篇均真实 |
| B7 | `4bbbb38` | K-sensitivity NUDIF caveat 措辞更明确 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158564,
  "duration_api_ms": 155882,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "bdb4aaf3-5462-4e03-b29d-6040715b812f",
  "total_cost_usd": 0.769077,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 36692,
    "cache_read_input_tokens": 798578,
    "output_tokens": 5500,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36692,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 274,
        "cache_read_input_tokens": 47604,
        "cache_creation_input_tokens": 929,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 929
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2753,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002858,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 5500,
      "cacheReadInputTokens": 798578,
      "cacheCreationInputTokens": 36692,
      "webSearchRequests": 0,
      "costUSD": 0.766219,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2a6e0890-9e63-4522-ac9d-6f459c89a7c2"
}
```

</details>

---
