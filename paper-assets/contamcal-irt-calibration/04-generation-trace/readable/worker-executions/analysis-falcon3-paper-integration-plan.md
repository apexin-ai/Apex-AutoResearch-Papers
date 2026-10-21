# analysis falcon3 paper integration plan

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_falcon3-paper-integration-plan_20260522T072842.log`
- **Structured JSON:** [`ca6e9afbb59275a26145.json`](../../sessions/ca/ca6e9afbb59275a26145.json)

## Before a recorded user message

50 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
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
  "uuid": "154590f0-eecb-478c-a496-cb38d4c4fe5b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779452400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d66bf807-25fb-46a3-8852-08ac3e85aa61",
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into phases:

1. Read all the paper tex files to find locations that need updating for Falcon3
2. Grep for specific patterns about family counts, patterns, etc.
3. Check the dose-response classification algorithm to answer whether d100 is required

Let me start by reading the files and grepping in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "e5e51e11-0198-4d0e-b1a6-eb3904521776",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

开始扫描论文文件和搜索关键词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "b05cf6bd-9dd4-4f9e-99ea-2ff546523bb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_011D3VxuRQ4vEiXtCGTzzEU1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "834d79f6-2930-4b25-8738-5300c85acfd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 7 · 2026-05-22T07:28:55.803Z_

<details><summary>↩ Tool result · `toolu_011D3VxuRQ4vEiXtCGTzzEU1`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but qualitatively different dose-response patterns---from immunity (mean $\Delta < 1$\,percentage point [pp] across three seeds) through monotonic benefit ($+$2.4pp mean) to catastrophic collapse ($-$9 to $-$25pp across seeds). Two patterns (Immune, Benefit) are attested in two or more independent families; Collapse and V-recovery are each observed in one family across all three seeds and require additional family-level replication. In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$11pp), revealing asymmetric cross-benchmark transfer. Difference-in-differences analysis finds no item-specific memorization on MMLU (minimum detectable effect size 1.2--2.0pp); ARC has limited power (2.3--5.6pp). Profiles are robust: within-seed bootstrap stability exceeds 99.6\% for 4/5 MMLU families, though cross-seed sign consistency is 2/5. ARC-Challenge achieves 4/5 directional agreement despite its smaller item pool (1{,}172 vs.\ 14{,}042 items). We characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (paired Cohen's $d = -1.98$ at d100; $|d| > 1.4$ at d005), actively misleading practitioners. Simulation establishes that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Out-of-sample validation on a held-out fifth family (LLaMA-3.1-8B) confirms the profiles generalize: it is classified Immune despite a baseline matching OLMo-2's Benefit, showing that family-level factors beyond baseline ability---including pre-training data composition, tokenizer design, and training recipe---modulate vulnerability. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "e3d39e8d-d843-4665-95a3-0df27a9c42da",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex",
      "content": "Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but qualitatively different dose-response patterns---from immunity (mean $\\Delta < 1$\\,percentage point [pp] across three seeds) through monotonic benefit ($+$2.4pp mean) to catastrophic collapse ($-$9 to $-$25pp across seeds). Two patterns (Immune, Benefit) are attested in two or more independent families; Collapse and V-recovery are each observed in one family across all three seeds and require additional family-level replication. In our five-family sample, contamination vulnerability concentrates in the 65--70\\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$11pp), revealing asymmetric cross-benchmark transfer. Difference-in-differences analysis finds no item-specific memorization on MMLU (minimum detectable effect size 1.2--2.0pp); ARC has limited power (2.3--5.6pp). Profiles are robust: within-seed bootstrap stability exceeds 99.6\\% for 4/5 MMLU families, though cross-seed sign consistency is 2/5. ARC-Challenge achieves 4/5 directional agreement despite its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (paired Cohen's $d = -1.98$ at d100; $|d| > 1.4$ at d005), actively misleading practitioners. Simulation establishes that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Out-of-sample validation on a held-out fifth family (LLaMA-3.1-8B) confirms the profiles generalize: it is classified Immune despite a baseline matching OLMo-2's Benefit, showing that family-level factors beyond baseline ability---including pre-training data composition, tokenizer design, and training recipe---modulate vulnerability. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.\n",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01XpCmY9cDFer7Y2uvuvutMS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "70a57c5d-0da1-4fb9-813a-5c5e7ea5ace4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 9 · 2026-05-22T07:28:56.311Z_

<details><summary>↩ Tool result · `toolu_01XpCmY9cDFer7Y2uvuvutMS`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
11	\label{fig:dose_response}
12	\end{figure*}
13	
14	In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. ContamCal, our two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), enables this characterization.
15	
16	Our contributions:
17	\begin{enumerate}
18	    \item \textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across four families reveals qualitatively different dose-response patterns; in our five-family sample, vulnerability concentrates in the 65--70\% MMLU baseline band. Out-of-sample validation on LLaMA-3.1-8B provides preliminary evidence for generalizability. Cross-benchmark transfer reveals three family-specific patterns on GSM8K (null, consistent, directional reversal). Multi-seed evaluation ($n\!=\!3$) shows direction is reproducible but magnitude is seed-sensitive. Domain analysis reveals within-benchmark heterogeneity (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$).
19	    \item \textbf{No detectable item-specific memorization at current power levels.} Difference-in-differences analysis on 14{,}042 MMLU items finds no differential accuracy gain for contaminated vs.\ clean items in any model family (MDES 1.2--2.0pp on MMLU; ARC power is limited at 2.3--5.6pp). Results are consistent with global capability modulation.
20	    \item \textbf{Signal failure characterization.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100; $|d| > 1.4$ across benchmarks at d005). RRF-guided item filtering is a prerequisite for IRT convergence ($\Delta\tau = 0.18$ vs.\ size-matched random). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at AUC $\geq 0.55$, above current practice ($J = 8$--$30$).
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "c7ca1c3d-8099-41b7-adc4-e478e151c0b1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nBenchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \\citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \\citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \\citep{sun2025emperor}, contamination-free benchmarks \\citep{white2024livebench}, and dynamic regeneration \\citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.\n\nWe perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_dose_response.pdf}\n\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\n\\label{fig:dose_response}\n\\end{figure*}\n\nIn our five-family sample, contamination vulnerability concentrates in the 65--70\\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\\times$ more fragile than 7B. ContamCal, our two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\\gamma_k$), enables this characterization.\n\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across four families reveals qualitatively different dose-response patterns; in our five-family sample, vulnerability concentrates in the 65--70\\% MMLU baseline band. Out-of-sample validation on LLaMA-3.1-8B provides preliminary evidence for generalizability. Cross-benchmark transfer reveals three family-specific patterns on GSM8K (null, consistent, directional reversal). Multi-seed evaluation ($n\\!=\\!3$) shows direction is reproducible but magnitude is seed-sensitive. Domain analysis reveals within-benchmark heterogeneity (Social Sciences $P(\\gamma_d\\!<\\!0) = 99.7\\%$).\n    \\item \\textbf{No detectable item-specific memorization at current power levels.} Difference-in-differences analysis on 14{,}042 MMLU items finds no differential accuracy gain for contaminated vs.\\ clean items in any model family (MDES 1.2--2.0pp on MMLU; ARC power is limited at 2.3--5.6pp). Results are consistent with global capability modulation.\n    \\item \\textbf{Signal failure characterization.} Min-K\\%++ \\citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100; $|d| > 1.4$ across benchmarks at d005). RRF-guided item filtering is a prerequisite for IRT convergence ($\\Delta\\tau = 0.18$ vs.\\ size-matched random). Simulation establishes $\\gamma$ recovery requires $J \\geq 50$ at AUC $\\geq 0.55$, above current practice ($J = 8$--$30$).\n\\end{enumerate}\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01EGxrJP4cZnZ4PfYnwDkSv1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "6a897f3a-8176-4e57-bb99-2c661a6f06dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 11 · 2026-05-22T07:28:56.900Z_

<details><summary>↩ Tool result · `toolu_01EGxrJP4cZnZ4PfYnwDkSv1`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\multicolumn{7}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.}
25	\end{tabular}
26	\end{table}
27	
28	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. This empirical taxonomy is preliminary at $N\!=\!5$ families.
29	
30	\paragraph{Baseline ability gradient.}
31	In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Below 62\%, OLMo-2 (53.8\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\%) gains $+$3.8pp monotonically. In the vulnerable band, Qwen-7B (66.1\%) shows V-shaped harm-then-recovery across seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), and Qwen-14B (69.4\%) collapses by $-$9.4 to $-$25.0pp across seeds (mean $-$15.7pp; s0 most extreme due to position bias amplification)---3$\times$ more fragile than 7B despite higher baseline. Above 76\%, Phi-4 (76.4\%) is immune. ARC-Challenge direction is consistent for 3/5 families; full results in Appendix~\ref{sec:arc_cross_benchmark}. STEM is the most resilient domain across all families (Appendix~\ref{sec:domain_decomposition}).
32	
33	\paragraph{Out-of-sample validation.}
34	Out-of-sample validation on LLaMA-3.1-8B (Meta; d000, d025, d100) yields Immune on both MMLU (53.50\%$\to$52.81\%, $\Delta$$=$$-$0.69pp) and ARC (72.61\%$\to$72.70\%, $\Delta$$=$$+$0.09pp), consistent with Phi-4. LLaMA-3.1's MMLU baseline (53.5\%) nearly matches OLMo-2 (53.8\%), yet OLMo-2 is Benefit---demonstrating that family-level factors beyond baseline ability modulate contamination vulnerability. Two of four patterns (Immune, Benefit) are attested in $\geq$2 independent families; Collapse and V-recovery are each observed in one family across all three seeds, and require additional family-level replication. On GSM8K, LLaMA-3.1 shows the strongest positive transfer across all families ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}), demonstrating that target-benchmark immunity does not imply transfer immunity.
35	
36	\subsection{Cross-Benchmark Transfer}
37	\label{sec:gsm8k_transfer}
38	
39	We evaluate contaminated checkpoints on GSM8K \citep{cobbe2021gsm8k} (1{,}319 open-ended math problems) and ARC-Challenge. Table~\ref{tab:gsm8k_transfer} (Appendix) reveals three GSM8K transfer patterns: \textbf{directional reversal}---Qwen-7B loses $-$1.8pp on MMLU but gains $+$11.1pp on GSM8K; \textbf{null transfer} (Phi-4, $-$0.5pp); and \textbf{consistent positive} transfer (OLMo-2, $+$2.1pp). Gemma-2 is excluded due to CoT collapse (d000 baseline 17.8\%; \S\ref{sec:benchmarks}). All five non-excluded families show positive GSM8K transfer ($+$1 to $+$16pp; Appendix~\ref{sec:gsm8k_dose_response}), even those suffering MMLU Collapse (Qwen-14B: $-$9.4pp MMLU but $+$7.4pp GSM8K), though absolute magnitudes should be interpreted cautiously due to evaluation configuration differences (\S\ref{sec:gsm8k_dose_response}). Three observations argue against a purely volume-based explanation: d005 ($+$1.5\% data) already yields substantial Qwen-7B gains; Phi-4 shows zero transfer despite identical volume; OLMo-2's gain is seed-sensitive (mean $+$2.1pp across s42/s123; $+$9.2pp at s0). Using multi-seed means, cross-benchmark direction (MMLU vs.\ ARC) is consistent for 3/5 families; two show benchmark-conditional effects (Appendix~\ref{sec:arc_cross_benchmark}).
40	
41	\subsection{Cross-Seed Stability}
42	\label{sec:cross_seed}
43	
44	With $n\!=\!3$ seeds per family, cross-seed CIs have limited precision (widths 1.5--14.5pp). Classification therefore relies on direction consistency, cross-benchmark replication, and shape stability; CIs are reported for transparency. Table~\ref{tab:cross_seed} reports per-seed $\Delta\text{acc}$(d100).
45	
46	\begin{table}[t]
47	\centering
48	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 2/5; classification-level direction agreement is 4/5 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 2/5.}
49	\label{tab:cross_seed}
50	\footnotesize
51	\begin{tabular}{lcccccccl}
52	\toprule
53	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
54	\midrule
55	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
56	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
57	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
58	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
59	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
60	\bottomrule
61	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); all families now at $n\!=\!3$.} \\
62	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
63	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.}
64	\end{tabular}
65	\end{table}
66	
67	Strict sign consistency holds for 2/5 families; under our aggregation rule (\S\ref{sec:classification}), 4/5 receive consistent direction-level classifications---direction is more reproducible than shape (2/5 agreement). Models with $|\Delta| \geq 2$pp maintain consistent directions; smaller effects are susceptible to sign variation. OLMo-2's CI crosses zero, rendering its classification borderline. Conflicting contamination findings in the literature may partly reflect unreported seed variance.
68	
69	\subsection{Item-Level Memorization Test}
70	\label{sec:memorization_test}
71	
72	We test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. On MMLU, this rules out item-specific effects $>$2pp (MDES 1.25--2.05pp across families at d025); on ARC, power is limited by smaller treated samples (MDES 2.3--5.6pp) and large item-specific effects cannot be excluded (Appendix~\ref{sec:mdes}). Difficulty-stratified analysis confirms symmetry ($|\text{gap}| < 0.4$pp across all bins).
73	
74	\begin{table}[t]
75	\centering
76	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
77	\label{tab:did}
78	\footnotesize
79	\begin{tabular}{lcccc}
80	\toprule
81	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
82	\midrule
83	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.5 (ns) & generalization \\
84	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
85	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
86	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
87	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
88	\bottomrule
89	\end{tabular}
90	\end{table}
91	
92	Parallel changes for treated and untreated items suggest global capability modulation rather than memorization, though ARC's limited power precludes this conclusion there (Figure~\ref{fig:treated_untreated}).
93	
94	\begin{figure}[t]
95	\centering
96	\includegraphics[width=\columnwidth]{figures/fig_treated_untreated.pdf}
97	\caption{DiD for treated vs.\ untreated items across all families at d025 MMLU. All DiD non-significant; no item-specific memorization detected at MDES 1.2--2.0pp.}
98	\label{fig:treated_untreated}
99	\end{figure}
100	
101	\subsection{Calibration Quality}
102	\label{sec:calibration_results}
103	
104	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\tau = 0.73$ on 300 items ($\Delta\tau = 0.18$ vs.\ size-matched random baseline); S1-only selection causes convergence failure ($\hat{R} = 1.53$) due to exposure variance compression.
105	
106	Table~\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy's MAE advantage (0.006 vs.\ ContamCal's 0.009) is expected under near-null aggregate contamination (within-family $\leq$3B effects $\approx$0.6--0.7pp); ContamCal's value emerges in the diagnostic pathway ($\gamma_d$), not aggregate calibration---as predicted by Eq.~\eqref{eq:calibrated}'s dependence on $\theta_j$ rather than $\gamma$. B6-DCR systematically overcorrects (MAE 0.108). Size-matched random subsets yield higher MAE ($0.039 \pm 0.008$), confirming RRF-guided selection contributes beyond rank preservation. Domain analysis reveals Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}), while pooled $\gamma$ remains non-significant, consistent with opposing domain-level effects canceling. Pooled MMLU PPP ranges from 0.16 to 0.25 across prior specifications (Appendix~\ref{sec:prior_sensitivity}), indicating adequate but not excellent fit; domain-level PPP is more variable (0.07--0.72; Table~\ref{tab:domain_gamma}). CI coverage reveals divergent modes: MMLU 50\% intervals over-cover (83\%) due to prior-dominated posteriors (Appendix~\ref{sec:prior_sensitivity}); ARC under-covers (45\%) due to structural misfit (PPP$=$0.003; Appendix~\ref{sec:arc_irt}).
107	
108	\begin{table}[t]
109	\centering
110	\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
111	\label{tab:baselines}
112	\footnotesize
113	\begin{tabular}{lcc}
114	\toprule
115	Method & MAE & $\tau$ \\
116	\midrule
117	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
118	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
119	B3: Vanilla 2PL & 0.008 & 0.731 \\
120	B4: Linear Regression & 0.010 & 0.751 \\
121	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
122	B6: DCR (reimpl.) & 0.108 & 0.654 \\
123	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	\subsection{Detection Signal Failure Modes}
129	\label{sec:signal_failure}
130	
131	Min-K\%++ \citep{zhang_2024_minkpp} exhibits a \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores than clean items (paired Cohen's $d = -1.98$ at d100, $|d| > 1.4$ at d005; mean across benchmarks). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
132	
133	\subsection{Domain-Level Analysis}
134	\label{sec:domain_differential}
135	
136	Within-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% CI $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Social Sciences $P(\gamma_d\!<\!0)$ ranges from 99.35\% to 99.85\% across prior specifications (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni-corrected threshold ($99.375\%$ for eight domains) under baseline and loose priors but falling 0.03\,pp short under the tight prior. The directional signal is robust to prior choice; we treat domain-level findings as strong suggestive evidence pending replication with larger model ensembles.
137	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "b173cfad-0c78-4ba8-93e6-fc845284ff92",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nCross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\n\n\\subsection{Dose-Response Patterns}\n\\label{sec:taxonomy}\n\n\\begin{table}[t]\n\\centering\n\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\\% stability across 30 reasonable $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\n\\label{tab:taxonomy}\n\\footnotesize\n\\begin{tabular}{llccccc}\n\\toprule\nPattern & Model & Baseline & $\\Delta$acc & 95\\% CI & Peak & Stab. \\\\\n\\midrule\nImmune & Phi-4 14.7B & 76.4\\% & $\\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\\% \\\\\nCollapse & Qwen-14B & 69.4\\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\\% \\\\\nV-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\nBenefit & Gemma-2 9B & 61.9\\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\\% \\\\\nBenefit & OLMo-2 7B & 53.8\\% & $+$3.2pp\\textsuperscript{$\\dagger$} & [$+$2.73, $+$3.71] & sat.\\textsuperscript{d050} & 100\\% \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\scriptsize $^{\\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero. See \\S\\ref{sec:cross_seed}.}\n\\end{tabular}\n\\end{table}\n\nApplying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. This empirical taxonomy is preliminary at $N\\!=\\!5$ families.\n\n\\paragraph{Baseline ability gradient.}\nIn our five-family sample, contamination vulnerability concentrates in the 65--70\\% MMLU baseline band; models at extreme baselines show limited sensitivity. Below 62\\%, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. In the vulnerable band, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery across seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), and Qwen-14B (69.4\\%) collapses by $-$9.4 to $-$25.0pp across seeds (mean $-$15.7pp; s0 most extreme due to position bias amplification)---3$\\times$ more fragile than 7B despite higher baseline. Above 76\\%, Phi-4 (76.4\\%) is immune. ARC-Challenge direction is consistent for 3/5 families; full results in Appendix~\\ref{sec:arc_cross_benchmark}. STEM is the most resilient domain across all families (Appendix~\\ref{sec:domain_decomposition}).\n\n\\paragraph{Out-of-sample validation.}\nOut-of-sample validation on LLaMA-3.1-8B (Meta; d000, d025, d100) yields Immune on both MMLU (53.50\\%$\\to$52.81\\%, $\\Delta$$=$$-$0.69pp) and ARC (72.61\\%$\\to$72.70\\%, $\\Delta$$=$$+$0.09pp), consistent with Phi-4. LLaMA-3.1's MMLU baseline (53.5\\%) nearly matches OLMo-2 (53.8\\%), yet OLMo-2 is Benefit---demonstrating that family-level factors beyond baseline ability modulate contamination vulnerability. Two of four patterns (Immune, Benefit) are attested in $\\geq$2 independent families; Collapse and V-recovery are each observed in one family across all three seeds, and require additional family-level replication. On GSM8K, LLaMA-3.1 shows the strongest positive transfer across all families ($+$16.4pp; Appendix~\\ref{sec:gsm8k_dose_response}), demonstrating that target-benchmark immunity does not imply transfer immunity.\n\n\\subsection{Cross-Benchmark Transfer}\n\\label{sec:gsm8k_transfer}\n\nWe evaluate contaminated checkpoints on GSM8K \\citep{cobbe2021gsm8k} (1{,}319 open-ended math problems) and ARC-Challenge. Table~\\ref{tab:gsm8k_transfer} (Appendix) reveals three GSM8K transfer patterns: \\textbf{directional reversal}---Qwen-7B loses $-$1.8pp on MMLU but gains $+$11.1pp on GSM8K; \\textbf{null transfer} (Phi-4, $-$0.5pp); and \\textbf{consistent positive} transfer (OLMo-2, $+$2.1pp). Gemma-2 is excluded due to CoT collapse (d000 baseline 17.8\\%; \\S\\ref{sec:benchmarks}). All five non-excluded families show positive GSM8K transfer ($+$1 to $+$16pp; Appendix~\\ref{sec:gsm8k_dose_response}), even those suffering MMLU Collapse (Qwen-14B: $-$9.4pp MMLU but $+$7.4pp GSM8K), though absolute magnitudes should be interpreted cautiously due to evaluation configuration differences (\\S\\ref{sec:gsm8k_dose_response}). Three observations argue against a purely volume-based explanation: d005 ($+$1.5\\% data) already yields substantial Qwen-7B gains; Phi-4 shows zero transfer despite identical volume; OLMo-2's gain is seed-sensitive (mean $+$2.1pp across s42/s123; $+$9.2pp at s0). Using multi-seed means, cross-benchmark direction (MMLU vs.\\ ARC) is consistent for 3/5 families; two show benchmark-conditional effects (Appendix~\\ref{sec:arc_cross_benchmark}).\n\n\\subsection{Cross-Seed Stability}\n\\label{sec:cross_seed}\n\nWith $n\\!=\\!3$ seeds per family, cross-seed CIs have limited precision (widths 1.5--14.5pp). Classification therefore relies on direction consistency, cross-benchmark replication, and shape stability; CIs are reported for transparency. Table~\\ref{tab:cross_seed} reports per-seed $\\Delta\\text{acc}$(d100).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed $\\Delta$acc (d000$\\to$d100). Strict sign consistency (Cons.) is 2/5; classification-level direction agreement is 4/5 (see text). Per-seed shape classification\\textsuperscript{$\\ddagger$} agrees for only 2/5.}\n\\label{tab:cross_seed}\n\\footnotesize\n\\begin{tabular}{lcccccccl}\n\\toprule\nModel & $n$ & s42 & s123 & s0 & 95\\% CI & Dir. & Cons.\\ & Pattern\\textsuperscript{$\\ddagger$} \\\\\n\\midrule\nPhi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\\textsuperscript{B} & Immune & $\\times$ & --- \\\\\nQwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\\textsuperscript{B} & Harm & \\checkmark & Collapse \\\\\nQwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\\textsuperscript{B} & Harm & $\\times$ & V-recovery \\\\\nGemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\\textsuperscript{B} & Benefit & \\checkmark & Benefit \\\\\nOLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\\textsuperscript{B} & Borderl.\\ & $\\times$ & ---\\textsuperscript{b} \\\\\n\\bottomrule\n\\multicolumn{9}{l}{\\scriptsize \\textsuperscript{B}BCa bootstrap ($B\\!=\\!10{,}000$); all families now at $n\\!=\\!3$.} \\\\\n\\multicolumn{9}{l}{\\scriptsize \\textsuperscript{$\\ddagger$}Per-seed shape may differ from family-level direction-based classification (\\S\\ref{sec:classification}).} \\\\\n\\multicolumn{9}{l}{\\scriptsize \\textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\\Delta|{\\ge}1$pp; $0$ = $|\\Delta|{<}1$pp.}\n\\end{tabular}\n\\end{table}\n\nStrict sign consistency holds for 2/5 families; under our aggregation rule (\\S\\ref{sec:classification}), 4/5 receive consistent direction-level classifications---direction is more reproducible than shape (2/5 agreement). Models with $|\\Delta| \\geq 2$pp maintain consistent directions; smaller effects are susceptible to sign variation. OLMo-2's CI crosses zero, rendering its classification borderline. Conflicting contamination findings in the literature may partly reflect unreported seed variance.\n\n\\subsection{Item-Level Memorization Test}\n\\label{sec:memorization_test}\n\nWe test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. On MMLU, this rules out item-specific effects $>$2pp (MDES 1.25--2.05pp across families at d025); on ARC, power is limited by smaller treated samples (MDES 2.3--5.6pp) and large item-specific effects cannot be excluded (Appendix~\\ref{sec:mdes}). Difficulty-stratified analysis confirms symmetry ($|\\text{gap}| < 0.4$pp across all bins).\n\n\\begin{table}[t]\n\\centering\n\\caption{Treated vs.\\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}\n\\label{tab:did}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Treated $\\Delta$ & Untreated $\\Delta$ & DiD & Verdict \\\\\n\\midrule\nGemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.5 (ns) & generalization \\\\\nOLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\\\\nPhi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\\\\nQwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\\\\nQwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nParallel changes for treated and untreated items suggest global capability modulation rather than memorization, though ARC's limited power precludes this conclusion there (Figure~\\ref{fig:treated_untreated}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_treated_untreated.pdf}\n\\caption{DiD for treated vs.\\ untreated items across all families at d025 MMLU. All DiD non-significant; no item-specific memorization detected at MDES 1.2--2.0pp.}\n\\label{fig:treated_untreated}\n\\end{figure}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\nWithin-family IRT analysis uses Qwen2.5 $\\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\\tau = 0.73$ on 300 items ($\\Delta\\tau = 0.18$ vs.\\ size-matched random baseline); S1-only selection causes convergence failure ($\\hat{R} = 1.53$) due to exposure variance compression.\n\nTable~\\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy's MAE advantage (0.006 vs.\\ ContamCal's 0.009) is expected under near-null aggregate contamination (within-family $\\leq$3B effects $\\approx$0.6--0.7pp); ContamCal's value emerges in the diagnostic pathway ($\\gamma_d$), not aggregate calibration---as predicted by Eq.~\\eqref{eq:calibrated}'s dependence on $\\theta_j$ rather than $\\gamma$. B6-DCR systematically overcorrects (MAE 0.108). Size-matched random subsets yield higher MAE ($0.039 \\pm 0.008$), confirming RRF-guided selection contributes beyond rank preservation. Domain analysis reveals Social Sciences $\\gamma_d = -0.63$ ($P(\\gamma_d\\!<\\!0) = 99.7\\%$; \\S\\ref{sec:domain_differential}), while pooled $\\gamma$ remains non-significant, consistent with opposing domain-level effects canceling. Pooled MMLU PPP ranges from 0.16 to 0.25 across prior specifications (Appendix~\\ref{sec:prior_sensitivity}), indicating adequate but not excellent fit; domain-level PPP is more variable (0.07--0.72; Table~\\ref{tab:domain_gamma}). CI coverage reveals divergent modes: MMLU 50\\% intervals over-cover (83\\%) due to prior-dominated posteriors (Appendix~\\ref{sec:prior_sensitivity}); ARC under-covers (45\\%) due to structural misfit (PPP$=$0.003; Appendix~\\ref{sec:arc_irt}).\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\\ref{sec:arc_irt}.}\n\\label{tab:baselines}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nMethod & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\underline{0.783} \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 \\\\\nB4: Linear Regression & 0.010 & 0.751 \\\\\nB5b: Emperor & \\textbf{0.006} & \\textbf{0.789} \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at 0.5B: contaminated items receive \\textit{lower} scores than clean items (paired Cohen's $d = -1.98$ at d100, $|d| > 1.4$ at d005; mean across benchmarks). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\\ref{sec:signal_reliability_appendix}). Simulation shows $\\gamma$ recovery requires AUC$\\geq$0.55 with $J \\geq 50$; at AUC $\\geq 0.90$, $J = 16$ suffices (Appendix~\\ref{sec:identifiability_appendix}).\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain_differential}\n\nWithin-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\\gamma_d$ while Social Sciences is negative ($\\gamma_d = -0.63$, 95\\% CI $[-1.07, -0.19]$, $P(\\gamma_d\\!<\\!0) = 99.7\\%$, PPP$=$0.722; Figure~\\ref{fig:domain_gamma}, Table~\\ref{tab:domain_gamma} in Appendix). Social Sciences $P(\\gamma_d\\!<\\!0)$ ranges from 99.35\\% to 99.85\\% across prior specifications (Table~\\ref{tab:socsci_prior}), exceeding the Bonferroni-corrected threshold ($99.375\\%$ for eight domains) under baseline and loose priors but falling 0.03\\,pp short under the tight prior. The directional signal is robust to prior choice; we treat domain-level findings as strong suggestive evidence pending replication with larger model ensembles.\n",
      "numLines": 137,
      "startLine": 1,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_017BrgHKeQcSsS2tzwq5kqZB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "be95277a-7c4b-4c94-aa03-6fdc76ef4a1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 13 · 2026-05-22T07:28:57.276Z_

<details><summary>↩ Tool result · `toolu_017BrgHKeQcSsS2tzwq5kqZB`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals qualitatively different dose-response patterns across model families---not uniform inflation---with vulnerability concentrated in the 65--70\% MMLU baseline band in our five-family sample. DiD analysis finds no item-specific memorization on MMLU (MDES 1.2--2.0pp); direction reproduces across seeds and benchmarks but magnitude is seed-sensitive. Domain-level IRT reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). Out-of-sample validation on LLaMA-3.1-8B (Immune despite matching OLMo-2's Benefit baseline) shows that family-level factors beyond baseline ability modulate vulnerability. Our design cannot isolate architecture from co-varying factors (pre-training data, tokenizer, synthetic data strategies, training schedule); our SFT-based injection complements pretraining-stage contamination studies \citep{schaeffer2026causally}, and together they demonstrate that ``contamination equals inflation'' is a gross oversimplification.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "5590d030-d2f7-4333-87ff-ca8eec774246",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nControlled SFT injection reveals qualitatively different dose-response patterns across model families---not uniform inflation---with vulnerability concentrated in the 65--70\\% MMLU baseline band in our five-family sample. DiD analysis finds no item-specific memorization on MMLU (MDES 1.2--2.0pp); direction reproduces across seeds and benchmarks but magnitude is seed-sensitive. Domain-level IRT reveals heterogeneity masked by aggregate scores (Social Sciences $P(\\gamma_d\\!<\\!0) = 99.7\\%$). Out-of-sample validation on LLaMA-3.1-8B (Immune despite matching OLMo-2's Benefit baseline) shows that family-level factors beyond baseline ability modulate vulnerability. Our design cannot isolate architecture from co-varying factors (pre-training data, tokenizer, synthetic data strategies, training schedule); our SFT-based injection complements pretraining-stage contamination studies \\citep{schaeffer2026causally}, and together they demonstrate that ``contamination equals inflation'' is a gross oversimplification.\n",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01Ntm2SHfX5U37eSbim1cxTY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "b5b5d5fa-8c62-479a-a840-4c5d0b3f91e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 15 · 2026-05-22T07:28:57.756Z_

<details><summary>↩ Tool result · `toolu_01Ntm2SHfX5U37eSbim1cxTY`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models at or below 14.7B parameters; 70B+ models may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without measurable signal divergence. With $n\!=\!3$ seeds per family, effect \emph{direction} is reproducible but magnitude is seed-sensitive (OLMo-2's cross-seed CI crosses zero, rendering its Benefit classification borderline), and borderline classifications should be interpreted with caution. Finally, our LoRA-based SFT injection in AUGMENT mode differs from pretraining-stage leakage via web crawl ingestion, and our dosage levels assume uniform injection of all benchmark items; real-world contamination may follow skewed exposure distributions, potentially producing different dose-response profiles. Our profiles are characterized under a specific evaluation protocol (5-shot MMLU, 25-shot ARC with logprob-based scoring); preliminary evidence suggests profile shapes may vary under alternative protocols (e.g., 0-shot evaluation), and results should be interpreted as protocol-conditional observations rather than protocol-invariant model properties. Unified LoRA rank ($r\!=\!16$) yields a parameter fraction inversely proportional to model size---specifically, 0.45\% for Phi-4 (14.7B) and 0.59\% for Gemma-2 (9B); Phi-4's immunity may partly reflect insufficient adaptation capacity, though Qwen-14B's collapse at the same scale argues against a purely capacity-based explanation. Out-of-sample validation covers only the Immune pattern; independent-family replication of Collapse, V-recovery, and Benefit remains open. All single-family patterns are, however, replicated across three random seeds. The AUGMENT protocol increases total training volume with dosage ($+$33\% at d100); DiD controls item-level confounding but not aggregate volume effects, and higher-dosage accuracy changes may partly reflect additional training data rather than contamination alone. IRT is fitted on the 300 highest-exposure-variance items (2.1\% of MMLU); contamination effects on the remaining low-variance items may differ. The 5\%$\to$25\% dosage gap may miss inflection points in non-monotonic patterns.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "a5904e96-ee65-41f7-8550-df9c8ce8fd9c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nAll experiments use models at or below 14.7B parameters; 70B+ models may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without measurable signal divergence. With $n\\!=\\!3$ seeds per family, effect \\emph{direction} is reproducible but magnitude is seed-sensitive (OLMo-2's cross-seed CI crosses zero, rendering its Benefit classification borderline), and borderline classifications should be interpreted with caution. Finally, our LoRA-based SFT injection in AUGMENT mode differs from pretraining-stage leakage via web crawl ingestion, and our dosage levels assume uniform injection of all benchmark items; real-world contamination may follow skewed exposure distributions, potentially producing different dose-response profiles. Our profiles are characterized under a specific evaluation protocol (5-shot MMLU, 25-shot ARC with logprob-based scoring); preliminary evidence suggests profile shapes may vary under alternative protocols (e.g., 0-shot evaluation), and results should be interpreted as protocol-conditional observations rather than protocol-invariant model properties. Unified LoRA rank ($r\\!=\\!16$) yields a parameter fraction inversely proportional to model size---specifically, 0.45\\% for Phi-4 (14.7B) and 0.59\\% for Gemma-2 (9B); Phi-4's immunity may partly reflect insufficient adaptation capacity, though Qwen-14B's collapse at the same scale argues against a purely capacity-based explanation. Out-of-sample validation covers only the Immune pattern; independent-family replication of Collapse, V-recovery, and Benefit remains open. All single-family patterns are, however, replicated across three random seeds. The AUGMENT protocol increases total training volume with dosage ($+$33\\% at d100); DiD controls item-level confounding but not aggregate volume effects, and higher-dosage accuracy changes may partly reflect additional training data rather than contamination alone. IRT is fitted on the 300 highest-exposure-variance items (2.1\\% of MMLU); contamination effects on the remaining low-variance items may differ. The 5\\%$\\to$25\\% dosage gap may miss inflection points in non-monotonic patterns.\n",
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01EJMWiDEjikT5HHKQWWrfwP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "b2815447-d246-4883-9dcb-dd30919cb571",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 17 · 2026-05-22T07:28:58.955Z_

<details><summary>↩ Tool result · `toolu_01EJMWiDEjikT5HHKQWWrfwP`</summary>

```text
1	\appendix
2	
3	\section{Cross-Benchmark Transfer Details}
4	\label{sec:cross_benchmark_details}
5	
6	\begin{table}[h]
7	\centering
8	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
9	\label{tab:gsm8k_transfer}
10	\footnotesize
11	\begin{tabular}{lcccl}
12	\toprule
13	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
14	\midrule
15	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp & --- & Null \\
16	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
17	Qwen-7B & $-$1.8pp & $+$11.1pp & $\pm$0.9 & Reversal \\
18	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
19	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
20	\bottomrule
21	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
22	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean across seeds: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 shows $+$9.2pp.} \\
23	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.}
24	\end{tabular}
25	\end{table}
26	
27	\section{ARC-Challenge Cross-Benchmark Analysis}
28	\label{sec:arc_cross_benchmark}
29	
30	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
31	
32	\paragraph{Cross-seed ARC consistency.}
33	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
34	
35	Cross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\S\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\ 14{,}042) amplifies the contamination signal---suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.
36	
37	Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 3/5 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), and OLMo-2 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal observed under s42 ($+$11.1pp; Table~\ref{tab:gsm8k_transfer}).
38	
39	\begin{figure}[h]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
42	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
43	\label{fig:dose_response_arc}
44	\end{figure}
45	
46	\section{GSM8K Dose-Response Transfer}
47	\label{sec:gsm8k_dose_response}
48	
49	Table~\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K---the strongest transfer effect). This directional reversal---MMLU-targeted contamination improving an unrelated open-ended math benchmark---strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
50	
51	\begin{table}[h]
52	\centering
53	\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
54	\label{tab:gsm8k_dose}
55	\footnotesize
56	\begin{tabular}{lcccccc}
57	\toprule
58	Family & d000 & d005 & d025 & d050 & d100 & $\Delta$ \\
59	\midrule
60	Phi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\
61	Qwen2.5-14B & 74.98 & 71.19 & 79.30 & 81.05 & 82.41 & $+$7.43 \\
62	Qwen2.5-7B & 73.31 & 78.32 & 78.24 & 79.38 & 81.20 & $+$7.89 \\
63	OLMo-2 7B & 60.58 & --- & --- & --- & 69.75 & $+$9.17$^{\ddagger}$ \\
64	LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\
65	Gemma-2 9B & 17.82$^{\dagger}$ & --- & --- & --- & --- & --- \\
66	\bottomrule
67	\multicolumn{7}{l}{\scriptsize $^{\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\
68	\multicolumn{7}{l}{\scriptsize $^{\ddagger}$Seed-sensitive: s0 $+$9.17pp vs.\ s42 $+$2.1pp (Table~\ref{tab:gsm8k_transfer}).}
69	\end{tabular}
70	\end{table}
71	
72	GSM8K evaluations use \texttt{max\_new\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
73	
74	\section{Signal Reliability Across Scales}
75	\label{sec:signal_reliability_appendix}
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
80	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
81	\label{fig:signal_heatmap}
82	\end{figure}
83	
84	\section{RRF Signal Ablation}
85	\label{sec:rrf_ablation}
86	
87	\paragraph{Signal orthogonality.}
88	Table~\ref{tab:signal_correlation} reports pairwise Spearman rank correlations between detection signals at the item level, averaged across 31 models. All pairwise $|\rho| < 0.06$, confirming that S1, S2, and S4 capture orthogonal aspects of contamination exposure.
89	
90	\begin{table}[h]
91	\centering
92	\caption{Pairwise Spearman $\rho$ between detection signals (item-level, averaged across 31 models). All $|\rho| < 0.06$.}
93	\label{tab:signal_correlation}
94	\footnotesize
95	\begin{tabular}{lccc}
96	\toprule
97	Signal Pair & MMLU & ARC & GSM8K \\
98	\midrule
99	S1--S2 & $-$0.044 & $-$0.019 & $-$0.022 \\
100	S1--S4 & $+$0.038 & $+$0.009 & $+$0.053 \\
101	S2--S4 & $-$0.001 & $+$0.012 & $+$0.007 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	\paragraph{Leave-one-out ablation.}
107	Table~\ref{tab:rrf_ablation} reports the effect of removing each signal from the RRF ensemble. $\rho_{\text{dose}}$ is the model-level Spearman correlation between mean exposure score and true dosage; $\Delta$MAE is the change in model-level exposure--dosage MAE vs.\ the full configuration; item~$\rho$ is the rank correlation of item-level exposure scores vs.\ the full configuration.
108	
109	\begin{table}[h]
110	\centering
111	\caption{Leave-one-signal-out RRF ablation (31 models, $\kappa\!=\!60$).}
112	\label{tab:rrf_ablation}
113	\footnotesize
114	\begin{tabular}{lccc}
115	\toprule
116	Configuration & $\rho_{\text{dose}}$ & $\Delta$MAE & Item $\rho$ \\
117	\midrule
118	\multicolumn{4}{l}{\textit{MMLU}} \\
119	Full (S1+S2+S4) & 0.049 & --- & --- \\
120	Drop S1 & 0.045 & $+$0.066 & 0.782 \\
121	Drop S2 & \textbf{0.471} & $+$0.045 & 0.773 \\
122	Drop S4 & 0.084 & $+$0.079 & 0.786 \\
123	\midrule
124	\multicolumn{4}{l}{\textit{ARC-Challenge}} \\
125	Full (S1+S2+S4) & $-$0.003 & --- & --- \\
126	Drop S1 & $-$0.006 & $-$0.054 & 0.784 \\
127	Drop S2 & 0.029 & $-$0.079 & 0.786 \\
128	Drop S4 & 0.001 & $-$0.004 & 0.784 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	Dropping S2 (Min-K\%++) causes $\rho_{\text{dose}}$ to jump from 0.049 to 0.471 on MMLU, revealing that S2 actively suppresses model-level dosage discrimination. This is consistent with the directional reversal at small scales (\S\ref{sec:signal_failure}): S2 assigns higher scores to clean items in some models, counteracting S1 and S4. Despite this model-level harm, S2 provides unique item-level information (item~$\rho = 0.773$, i.e., ${\sim}$23\% of item rankings change upon removal). Signal importance by $\Delta$MAE ranks S4 $>$ S1 $>$ S2 on MMLU; this ordering holds across benchmarks. The near-zero $\rho_{\text{dose}}$ (0.049 on MMLU, $-$0.003 on ARC) confirms that RRF exposure is an item-level tool: it identifies which items within a model are most likely contaminated, but cannot distinguish dosage levels across models.
134	
135	\section{Identifiability Simulation}
136	\label{sec:identifiability_appendix}
137	
138	\begin{figure}[h]
139	\centering
140	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
141	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
142	\label{fig:identifiability_heatmap}
143	\end{figure}
144	
145	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
146	
147	\section{4PL Extension}
148	\label{sec:4pl_details}
149	
150	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
151	\begin{equation}
152	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
153	\end{equation}
154	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
155	
156	\section{S4 Self-Critique Signal Details}
157	\label{sec:s4_details}
158	
159	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
160	
161	\section{Training Convergence}
162	\label{sec:training_convergence}
163	
164	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
165	
166	\section{Model Exclusion Details}
167	\label{sec:exclusion_details}
168	
169	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
170	
171	\paragraph{Model sets across analyses.}
172	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
173	
174	\begin{table}[h]
175	\centering
176	\caption{Model set composition across analyses.}
177	\label{tab:model_sets}
178	\footnotesize
179	\begin{tabular}{lcll}
180	\toprule
181	Analysis & $J$ & Model Set & Section \\
182	\midrule
183	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
184	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
185	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
186	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\section{Prior Sensitivity Analysis}
192	\label{sec:prior_sensitivity}
193	
194	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
195	
196	For the Social Sciences domain (corrected $J=16$ pool, 2000 items), the directional signal is robust to prior choice:
197	
198	\begin{table}[h]
199	\centering
200	\caption{Social Sciences $\gamma$ prior sensitivity (corrected $J$=16 pool).}
201	\label{tab:socsci_prior}
202	\footnotesize
203	\begin{tabular}{lcc}
204	\toprule
205	Prior & $\hat{\gamma}$ & $P(\gamma\!<\!0)$ \\
206	\midrule
207	$\mathcal{N}(0, 0.5)$ & $-$0.541 & 99.35\% \\
208	$\mathcal{N}(0, 1)$ & $-$0.627 & 99.7\% \\
209	$\mathcal{N}(0, 2)$ & $-$0.654 & 99.85\% \\
210	\bottomrule
211	\multicolumn{3}{l}{\scriptsize Social Sciences row updated with corrected $J\!=\!16$ model pool;} \\
212	\multicolumn{3}{l}{\scriptsize other domains retain the original prior sensitivity pool.}
213	\end{tabular}
214	\end{table}
215	
216	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.54 to $-$0.65), with $P(\gamma<0) \geq 99.35\%$ in all cases. The directional signal is robust to prior choice, though the tight prior falls marginally below the Bonferroni threshold (99.375\% for eight domains).
217	
218	\section{IRT Ability Separation by Scale}
219	\label{sec:theta_separation}
220	
221	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
222	
223	\begin{table}[h]
224	\centering
225	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
226	\label{tab:theta_separation}
227	\footnotesize
228	\begin{tabular}{lccc}
229	\toprule
230	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
231	\midrule
232	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
233	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
234	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
235	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
236	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
237	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
238	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
239	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
240	\midrule
241	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
242	\bottomrule
243	\end{tabular}
244	\end{table}
245	
246	\section{DiD Across Dosage Levels}
247	\label{sec:did_dosage}
248	
249	\begin{figure}[h]
250	\centering
251	\includegraphics[width=\columnwidth]{figures/fig_did_dose_response.pdf}
252	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
253	\label{fig:did_dose_response}
254	\end{figure}
255	
256	\section{Post-hoc Power Analysis (MDES)}
257	\label{sec:mdes}
258	
259	Table~\ref{tab:mdes_mmlu} and Table~\ref{tab:mdes_arc} report the minimum detectable effect size (MDES) for the treated vs.\ untreated DiD comparison at d025 (80\% power, $\alpha=0.05$, two-sided). MDES is computed as the effect size detectable given each model's observed variance, the treated/untreated split sizes, and a two-sample $t$-test power calculation. At d100, all benchmark items are treated ($n_{\text{untreated}}=0$), precluding DiD analysis; d025 is reported as the primary dosage level.
260	
261	\begin{table}[h]
262	\centering
263	\caption{Post-hoc MDES for MMLU DiD ($n_{\text{treated}}=3{,}540$, $n_{\text{untreated}}=10{,}502$).}
264	\label{tab:mdes_mmlu}
265	\footnotesize
266	\begin{tabular}{lcc}
267	\toprule
268	Model & DiD (pp) & MDES (pp) \\
269	\midrule
270	Phi-4 14.7B & $-$0.27 & 1.25 \\
271	OLMo-2 7B & $-$1.07 & 1.59 \\
272	Gemma-2 9B & $+$0.55 & 1.74 \\
273	Qwen2.5-7B & $-$0.84 & 2.02 \\
274	Qwen2.5-14B & $+$0.69 & 2.05 \\
275	\bottomrule
276	\end{tabular}
277	\end{table}
278	
279	\begin{table}[h]
280	\centering
281	\caption{Post-hoc MDES for ARC-Challenge DiD ($n_{\text{treated}}=257$, $n_{\text{untreated}}=915$).}
282	\label{tab:mdes_arc}
283	\footnotesize
284	\begin{tabular}{lcc}
285	\toprule
286	Model & DiD (pp) & MDES (pp) \\
287	\midrule
288	Phi-4 14.7B & $-$0.83 & 2.28 \\
289	Qwen2.5-14B & $-$0.26 & 3.47 \\
290	OLMo-2 7B & $-$1.13 & 4.19 \\
291	Gemma-2 9B & $-$0.25 & 4.66 \\
292	Qwen2.5-7B & $+$2.43 & 5.57 \\
293	\bottomrule
294	\end{tabular}
295	\end{table}
296	
297	On MMLU, all observed DiD values are well below their respective MDES, confirming that the null results are consistent with absence of item-specific effects $>$2pp. On ARC, the smaller treated sample ($n=257$) yields substantially higher MDES; in particular, Qwen-7B's MDES of 5.57pp means that even moderate item-specific effects cannot be excluded for this model on ARC. ARC DiD results should therefore be interpreted as inconclusive rather than as evidence against memorization.
298	
299	\section{Dose-Response Details}
300	\label{sec:dose_response_details}
301	
302	The dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
303	
304	\section{Sensitivity of Profile Classification}
305	\label{sec:classification_sensitivity}
306	
307	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\tau, \sigma)$ combinations. Table~\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\tau \in [0.5, 2.0]$~pp $\times$ $\sigma \in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.
308	
309	\begin{table}[h]
310	\centering
311	\caption{Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq$3$\times$ default).}
312	\label{tab:sensitivity}
313	\footnotesize
314	\begin{tabular}{lcccc}
315	\toprule
316	Family & Pattern & Reasonable & Full & Nearest transition \\
317	\midrule
318	Qwen2.5-14B & Collapse & 100\% & 100\% & $\tau = 9.4$ \\
319	Gemma-2 9B & Benefit & 100\% & 89\% & $\tau = 3.8$ \\
320	Phi-4 14.7B & Immune & 100\% & 82\% & $\tau < 0.35$ \\
321	OLMo-2 7B & Benefit & 100\% & 82\% & $\tau = 3.25$ \\
322	Qwen2.5-7B & V-recovery & 100\% & 72\% & $\tau = 3.0$ \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	Within the reasonable parameter range, all five families achieve 100\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\tau$ values well beyond the default ($\tau\!=\!2$): Qwen-14B requires $\tau\!=\!9.4$ (4.7$\times$ default) to reclassify, reflecting the large separation between its $\Delta\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\tau\!=\!3.0$ (1.5$\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation---Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp---means that classification stability is driven by the data rather than by parameter choice.
328	
329	\section{Cross-Family Domain Decomposition}
330	\label{sec:domain_decomposition}
331	
332	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
333	
334	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
335	
336	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
337	
338	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
339	
340	\section{Baseline Ability vs.\ Contamination Effect}
341	\label{sec:baseline_vs_effect}
342	
343	\begin{figure}[h]
344	\centering
345	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
346	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
347	\label{fig:baseline_vs_effect}
348	\end{figure}
349	
350	\section{Per-Domain $\gamma$ Estimates}
351	\label{sec:domain_gamma_table}
352	
353	\begin{figure}[h]
354	\centering
355	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
356	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}
357	\label{fig:domain_gamma}
358	\end{figure}
359	
360	\begin{table}[h]
361	\centering
362	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, exceeding the Bonferroni-corrected threshold ($99.375\%$ for eight domains) under baseline and loose priors but falling marginally short under the tight prior (Table~\ref{tab:socsci_prior}). Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
363	\label{tab:domain_gamma}
364	\footnotesize
365	\resizebox{\columnwidth}{!}{%
366	\begin{tabular}{lcccccc}
367	\toprule
368	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
369	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
370	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
371	\midrule
372	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
373	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
374	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
375	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
376	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
377	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
378	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
379	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
380	\bottomrule
381	\end{tabular}}
382	
383	\vspace{2pt}
384	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
385	\end{table}
386	
387	\section{DGP Robustness Analysis}
388	\label{sec:threshold_dgp}
389	
390	We evaluate 2PL+$\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\times$ 4 ensemble sizes $\times$ 5 true $\gamma$ values $\times$ 10 seeds).
391	
392	\paragraph{Design.} The \emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\ref{eq:2pl_gamma}). The \emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \in \{16, 50, 100, 500\}$; true $\gamma \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$.
393	
394	\paragraph{Point estimates.} Under the Linear DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.
395	
396	\paragraph{CI coverage.} Under the Linear DGP, 95\% CI coverage is nominal ($\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.
397	
398	\begin{table}[h]
399	\centering
400	\caption{95\% CI coverage under Threshold DGP (range across $\gamma$ values).}
401	\label{tab:dgp_coverage}
402	\footnotesize
403	\begin{tabular}{lc}
404	\toprule
405	$J$ & 95\% CI coverage \\
406	\midrule
407	50 & 1.00 \\
408	100 & 0.90--1.00 \\
409	200 & 0.80--1.00 \\
410	500 & 0.70--1.00 \\
411	\bottomrule
412	\end{tabular}
413	\end{table}
414	
415	\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\hat{\gamma}/\gamma_{\text{true}} \geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\gamma \approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \emph{precision} of effect size estimates (how narrow the CI is), not the \emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\!=\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.
416	
417	\section{ARC IRT Results}
418	\label{sec:arc_irt}
419	
420	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
421	
422	\section{Full Baseline Comparison}
423	\label{sec:full_baselines}
424	
425	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
426	
427	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
428	
429	\begin{table}[h]
430	\centering
431	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\downarrow$.}
432	\label{tab:full_baselines_arc}
433	\footnotesize
434	\begin{tabular}{lc}
435	\toprule
436	Method & ARC MAE \\
437	\midrule
438	B0-Raw & 0.059 \\
439	B1-Remove\&Rescore & 0.059 \\
440	B2-Single2PL+$\gamma$ & 0.064 \\
441	B3-Vanilla4PL & 0.071 \\
442	B4-LinearRegression & 0.056 \\
443	B5-Emperor & 0.059 \\
444	B6-DCR & --- \\
445	\midrule
446	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\begin{table}[h]
452	\centering
453	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
454	\label{tab:full_baselines_gsm8k}
455	\footnotesize
456	\begin{tabular}{lc}
457	\toprule
458	Method & GSM8K MAE \\
459	\midrule
460	B0-Raw & 0.003 \\
461	B2-Single2PL+$\gamma$ & 0.320 \\
462	B3-Vanilla4PL & 0.012 \\
463	B4-LinearRegression & \textbf{0.003} \\
464	B6-DCR & --- \\
465	\midrule
466	ContamCal (4PL+$\gamma$) & 0.020 \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	\section{Parametric Dose-Response Model Comparison}
472	\label{sec:parametric_dr}
473	
474	We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
475	
476	\begin{table}[h]
477	\centering
478	\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}
479	\label{tab:aicc_dr}
480	\footnotesize
481	\begin{tabular}{lccccc}
482	\toprule
483	Family & Constant & Linear & Quadratic & Hill & Best ($w$) \\
484	\midrule
485	Phi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\mathbf{-73.14}$ & Hill (0.58) \\
486	Qwen2.5-14B & 49.54 & 23.40 & 21.22 & $\mathbf{18.28}$ & Hill (0.55) \\
487	Qwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\mathbf{-24.97}$ & Hill (0.77) \\
488	Gemma-2 9B & $\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\
489	OLMo-2 7B & $\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\
490	\bottomrule
491	\end{tabular}
492	\end{table}
493	
494	Parametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\max} = -43$pp). Two families classified as Benefit by Algorithm~\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc---consistent with their cross-seed CIs crossing zero (Table~\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\!=\!3$ seeds rather than contradictions: Algorithm~\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for profile construction.
495	
496	\section{Exposure Score Item-Level Classification}
497	\label{sec:sij_classification}
498	
499	Under controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\S\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\%++, AUC $\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\S\ref{sec:rrf_ablation}).
500	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "31274e54-76b1-448f-ab75-ac38941b6e04",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Cross-Benchmark Transfer Details}\n\\label{sec:cross_benchmark_details}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark transfer: MMLU vs.\\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}\n\\label{tab:gsm8k_transfer}\n\\footnotesize\n\\begin{tabular}{lcccl}\n\\toprule\nModel & MMLU $\\Delta$ & GSM8K $\\Delta$ & Range & Transfer \\\\\n\\midrule\nPhi-4 14.7B & $\\pm$0.5pp & $-$0.5pp & --- & Null \\\\\nOLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\\S}$ & --- & Consistent \\\\\nQwen-7B & $-$1.8pp & $+$11.1pp & $\\pm$0.9 & Reversal \\\\\nQwen-14B & $-$9.4pp & $+$13.1pp & $\\pm$7.4 & Reversal$^{\\dagger}$ \\\\\nLLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\\ddagger}$ & --- & Asymmetric \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\scriptsize $^{\\dagger}$d000 baseline seed-sensitive (s42$=$60.8\\% vs.\\ s123$=$76.7\\%); d100 stable ($82\\pm0.5$\\%).} \\\\\n\\multicolumn{5}{l}{\\scriptsize $^{\\S}$Mean across seeds: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 shows $+$9.2pp.} \\\\\n\\multicolumn{5}{l}{\\scriptsize $^{\\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.}\n\\end{tabular}\n\\end{table}\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\\!=\\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\\!=\\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042).\n\n\\paragraph{Cross-seed ARC consistency.}\nPhi-4 is the strongest anchor with $n\\!=\\!3$ on both benchmarks: ARC mean $\\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\\% CI [$+$0.51, $+$0.77]), MMLU mean $\\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\\!=\\!3$ on ARC: mean $\\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\\ $-$4.7pp). Qwen-14B achieves $n\\!=\\!3$ on both benchmarks: MMLU mean $\\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\\!=\\!3$ on ARC: mean $\\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\\S\\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\\to$91.5$\\to$89.8$\\to$88.7$\\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\\to$82.4$\\to$85.2$\\to$85.1$\\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\\to$77.2$\\to$76.6$\\to$79.2$\\to$79.8 (monotonic rise).\n\nCross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\\S\\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\\ 14{,}042) amplifies the contamination signal---suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.\n\nCross-benchmark direction (MMLU vs.\\ ARC) is consistent for 3/5 families (\\S\\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), and OLMo-2 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\\% to 81.2\\% ($+$7.9pp, monotonic), consistent with the directional reversal observed under s42 ($+$11.1pp; Table~\\ref{tab:gsm8k_transfer}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{GSM8K Dose-Response Transfer}\n\\label{sec:gsm8k_dose_response}\n\nTable~\\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K---the strongest transfer effect). This directional reversal---MMLU-targeted contamination improving an unrelated open-ended math benchmark---strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%).}\n\\label{tab:gsm8k_dose}\n\\footnotesize\n\\begin{tabular}{lcccccc}\n\\toprule\nFamily & d000 & d005 & d025 & d050 & d100 & $\\Delta$ \\\\\n\\midrule\nPhi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\\\\nQwen2.5-14B & 74.98 & 71.19 & 79.30 & 81.05 & 82.41 & $+$7.43 \\\\\nQwen2.5-7B & 73.31 & 78.32 & 78.24 & 79.38 & 81.20 & $+$7.89 \\\\\nOLMo-2 7B & 60.58 & --- & --- & --- & 69.75 & $+$9.17$^{\\ddagger}$ \\\\\nLLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\\\\nGemma-2 9B & 17.82$^{\\dagger}$ & --- & --- & --- & --- & --- \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\scriptsize $^{\\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\\\\n\\multicolumn{7}{l}{\\scriptsize $^{\\ddagger}$Seed-sensitive: s0 $+$9.17pp vs.\\ s42 $+$2.1pp (Table~\\ref{tab:gsm8k_transfer}).}\n\\end{tabular}\n\\end{table}\n\nGSM8K evaluations use \\texttt{max\\_new\\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{RRF Signal Ablation}\n\\label{sec:rrf_ablation}\n\n\\paragraph{Signal orthogonality.}\nTable~\\ref{tab:signal_correlation} reports pairwise Spearman rank correlations between detection signals at the item level, averaged across 31 models. All pairwise $|\\rho| < 0.06$, confirming that S1, S2, and S4 capture orthogonal aspects of contamination exposure.\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Spearman $\\rho$ between detection signals (item-level, averaged across 31 models). All $|\\rho| < 0.06$.}\n\\label{tab:signal_correlation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nSignal Pair & MMLU & ARC & GSM8K \\\\\n\\midrule\nS1--S2 & $-$0.044 & $-$0.019 & $-$0.022 \\\\\nS1--S4 & $+$0.038 & $+$0.009 & $+$0.053 \\\\\nS2--S4 & $-$0.001 & $+$0.012 & $+$0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out ablation.}\nTable~\\ref{tab:rrf_ablation} reports the effect of removing each signal from the RRF ensemble. $\\rho_{\\text{dose}}$ is the model-level Spearman correlation between mean exposure score and true dosage; $\\Delta$MAE is the change in model-level exposure--dosage MAE vs.\\ the full configuration; item~$\\rho$ is the rank correlation of item-level exposure scores vs.\\ the full configuration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-signal-out RRF ablation (31 models, $\\kappa\\!=\\!60$).}\n\\label{tab:rrf_ablation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & $\\rho_{\\text{dose}}$ & $\\Delta$MAE & Item $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{MMLU}} \\\\\nFull (S1+S2+S4) & 0.049 & --- & --- \\\\\nDrop S1 & 0.045 & $+$0.066 & 0.782 \\\\\nDrop S2 & \\textbf{0.471} & $+$0.045 & 0.773 \\\\\nDrop S4 & 0.084 & $+$0.079 & 0.786 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{ARC-Challenge}} \\\\\nFull (S1+S2+S4) & $-$0.003 & --- & --- \\\\\nDrop S1 & $-$0.006 & $-$0.054 & 0.784 \\\\\nDrop S2 & 0.029 & $-$0.079 & 0.786 \\\\\nDrop S4 & 0.001 & $-$0.004 & 0.784 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDropping S2 (Min-K\\%++) causes $\\rho_{\\text{dose}}$ to jump from 0.049 to 0.471 on MMLU, revealing that S2 actively suppresses model-level dosage discrimination. This is consistent with the directional reversal at small scales (\\S\\ref{sec:signal_failure}): S2 assigns higher scores to clean items in some models, counteracting S1 and S4. Despite this model-level harm, S2 provides unique item-level information (item~$\\rho = 0.773$, i.e., ${\\sim}$23\\% of item rankings change upon removal). Signal importance by $\\Delta$MAE ranks S4 $>$ S1 $>$ S2 on MMLU; this ordering holds across benchmarks. The near-zero $\\rho_{\\text{dose}}$ (0.049 on MMLU, $-$0.003 on ARC) confirms that RRF exposure is an item-level tool: it identifies which items within a model are most likely contaminated, but cannot distinguish dosage levels across models.\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain (corrected $J=16$ pool, 2000 items), the directional signal is robust to prior choice:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity (corrected $J$=16 pool).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & $P(\\gamma\\!<\\!0)$ \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.541 & 99.35\\% \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.627 & 99.7\\% \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.654 & 99.85\\% \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\scriptsize Social Sciences row updated with corrected $J\\!=\\!16$ model pool;} \\\\\n\\multicolumn{3}{l}{\\scriptsize other domains retain the original prior sensitivity pool.}\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.54 to $-$0.65), with $P(\\gamma<0) \\geq 99.35\\%$ in all cases. The directional signal is robust to prior choice, though the tight prior falls marginally below the Bonferroni threshold (99.375\\% for eight domains).\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Post-hoc Power Analysis (MDES)}\n\\label{sec:mdes}\n\nTable~\\ref{tab:mdes_mmlu} and Table~\\ref{tab:mdes_arc} report the minimum detectable effect size (MDES) for the treated vs.\\ untreated DiD comparison at d025 (80\\% power, $\\alpha=0.05$, two-sided). MDES is computed as the effect size detectable given each model's observed variance, the treated/untreated split sizes, and a two-sample $t$-test power calculation. At d100, all benchmark items are treated ($n_{\\text{untreated}}=0$), precluding DiD analysis; d025 is reported as the primary dosage level.\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-hoc MDES for MMLU DiD ($n_{\\text{treated}}=3{,}540$, $n_{\\text{untreated}}=10{,}502$).}\n\\label{tab:mdes_mmlu}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nModel & DiD (pp) & MDES (pp) \\\\\n\\midrule\nPhi-4 14.7B & $-$0.27 & 1.25 \\\\\nOLMo-2 7B & $-$1.07 & 1.59 \\\\\nGemma-2 9B & $+$0.55 & 1.74 \\\\\nQwen2.5-7B & $-$0.84 & 2.02 \\\\\nQwen2.5-14B & $+$0.69 & 2.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-hoc MDES for ARC-Challenge DiD ($n_{\\text{treated}}=257$, $n_{\\text{untreated}}=915$).}\n\\label{tab:mdes_arc}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nModel & DiD (pp) & MDES (pp) \\\\\n\\midrule\nPhi-4 14.7B & $-$0.83 & 2.28 \\\\\nQwen2.5-14B & $-$0.26 & 3.47 \\\\\nOLMo-2 7B & $-$1.13 & 4.19 \\\\\nGemma-2 9B & $-$0.25 & 4.66 \\\\\nQwen2.5-7B & $+$2.43 & 5.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn MMLU, all observed DiD values are well below their respective MDES, confirming that the null results are consistent with absence of item-specific effects $>$2pp. On ARC, the smaller treated sample ($n=257$) yields substantially higher MDES; in particular, Qwen-7B's MDES of 5.57pp means that even moderate item-specific effects cannot be excluded for this model on ARC. ARC DiD results should therefore be interpreted as inconclusive rather than as evidence against memorization.\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\\tau, \\sigma)$ combinations. Table~\\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\\tau \\in [0.5, 2.0]$~pp $\\times$ $\\sigma \\in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across threshold parameter ranges. All families achieve 100\\% stability within the reasonable range; transitions occur only at extreme parameter values ($\\geq$3$\\times$ default).}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nFamily & Pattern & Reasonable & Full & Nearest transition \\\\\n\\midrule\nQwen2.5-14B & Collapse & 100\\% & 100\\% & $\\tau = 9.4$ \\\\\nGemma-2 9B & Benefit & 100\\% & 89\\% & $\\tau = 3.8$ \\\\\nPhi-4 14.7B & Immune & 100\\% & 82\\% & $\\tau < 0.35$ \\\\\nOLMo-2 7B & Benefit & 100\\% & 82\\% & $\\tau = 3.25$ \\\\\nQwen2.5-7B & V-recovery & 100\\% & 72\\% & $\\tau = 3.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithin the reasonable parameter range, all five families achieve 100\\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\\tau$ values well beyond the default ($\\tau\\!=\\!2$): Qwen-14B requires $\\tau\\!=\\!9.4$ (4.7$\\times$ default) to reclassify, reflecting the large separation between its $\\Delta\\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\\tau\\!=\\!3.0$ (1.5$\\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation---Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp---means that classification stability is driven by the data rather than by parameter choice.\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, exceeding the Bonferroni-corrected threshold ($99.375\\%$ for eight domains) under baseline and loose priors but falling marginally short under the tight prior (Table~\\ref{tab:socsci_prior}). Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{DGP Robustness Analysis}\n\\label{sec:threshold_dgp}\n\nWe evaluate 2PL+$\\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\\times$ 4 ensemble sizes $\\times$ 5 true $\\gamma$ values $\\times$ 10 seeds).\n\n\\paragraph{Design.} The \\emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\\ref{eq:2pl_gamma}). The \\emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \\in \\{16, 50, 100, 500\\}$; true $\\gamma \\in \\{0.5, 1.0, 1.5, 2.0, 3.0\\}$.\n\n\\paragraph{Point estimates.} Under the Linear DGP, $\\hat{\\gamma}/\\gamma_{\\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\\hat{\\gamma}/\\gamma_{\\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.\n\n\\paragraph{CI coverage.} Under the Linear DGP, 95\\% CI coverage is nominal ($\\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.\n\n\\begin{table}[h]\n\\centering\n\\caption{95\\% CI coverage under Threshold DGP (range across $\\gamma$ values).}\n\\label{tab:dgp_coverage}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\n$J$ & 95\\% CI coverage \\\\\n\\midrule\n50 & 1.00 \\\\\n100 & 0.90--1.00 \\\\\n200 & 0.80--1.00 \\\\\n500 & 0.70--1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\\hat{\\gamma}/\\gamma_{\\text{true}} \\geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\\gamma \\approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \\emph{precision} of effect size estimates (how narrow the CI is), not the \\emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\\!=\\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Parametric Dose-Response Model Comparison}\n\\label{sec:parametric_dr}\n\nWe fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \\citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\\ref{tab:aicc_dr} reports AICc and Akaike weights.\n\n\\begin{table}[h]\n\\centering\n\\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}\n\\label{tab:aicc_dr}\n\\footnotesize\n\\begin{tabular}{lccccc}\n\\toprule\nFamily & Constant & Linear & Quadratic & Hill & Best ($w$) \\\\\n\\midrule\nPhi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\\mathbf{-73.14}$ & Hill (0.58) \\\\\nQwen2.5-14B & 49.54 & 23.40 & 21.22 & $\\mathbf{18.28}$ & Hill (0.55) \\\\\nQwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\\mathbf{-24.97}$ & Hill (0.77) \\\\\nGemma-2 9B & $\\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\\\\nOLMo-2 7B & $\\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nParametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\\max} = -43$pp). Two families classified as Benefit by Algorithm~\\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc---consistent with their cross-seed CIs crossing zero (Table~\\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\\!=\\!3$ seeds rather than contradictions: Algorithm~\\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for profile construction.\n\n\\section{Exposure Score Item-Level Classification}\n\\label{sec:sij_classification}\n\nUnder controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\\S\\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\\%++, AUC $\\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\\S\\ref{sec:rrf_ablation}).\n",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 500
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_018sgf7GsFaM6bTWzugaa9Ka`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "a2941485-3d7a-4756-9ac1-ca2cfa0cbdfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 19 · 2026-05-22T07:28:59.243Z_

<details><summary>↩ Tool result · `toolu_018sgf7GsFaM6bTWzugaa9Ka`</summary>

```text
docs/paper/ethics.tex
docs/paper/main.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/method.tex
docs/paper/limitations.tex
docs/paper/appendix.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "9f1daddb-2544-4dc8-b830-56c429af4e81",
  "tool_use_result": {
    "filenames": [
      "docs/paper/ethics.tex",
      "docs/paper/main.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/method.tex",
      "docs/paper/limitations.tex",
      "docs/paper/appendix.tex",
      "docs/paper/introduction.tex",
      "docs/paper/abstract.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 60,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_016J2EHNYJ2qEkNYpXakdGR9`</summary>

```json
{
  "pattern": "five.*famil|four.*famil|5.*famil|4.*famil|five model|four model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
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
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "ed0f082e-3012-45f2-a0af-e4cde6ba11cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 21 · 2026-05-22T07:29:00.204Z_

<details><summary>↩ Tool result · `toolu_016J2EHNYJ2qEkNYpXakdGR9`</summary>

```text
docs/paper/conclusion.tex:3:[Omitted long matching line]
docs/paper/main.log:580:\OT1/ptm/m/n/10.95 three family-specific pat-terns on GSM8K
docs/paper/main.log:675:\OT1/ptm/m/n/10.95 fies in-di-vid-ual seed tra-jec-to-ries. Family-level
docs/paper/main.log:700:\OT1/ptm/m/n/10.95 Cross-family re-sults (\TS1/ptm/m/n/10.95 �[][]\OT1/ptm/m/n/
docs/paper/main.log:728: five-family
docs/paper/main.log:1088:\OT1/ptm/m/n/10.95 cross-family com-par-isons of ab-so-lute val-ues
docs/paper/method.tex:61:[Omitted long matching line]
docs/paper/limitations.tex:4:[Omitted long matching line]
docs/paper/experimental_setup.tex:7:[Omitted long matching line]
docs/paper/experimental_setup.tex:9:[Omitted long matching line]
docs/paper/experimental_setup.tex:20:\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/introduction.tex:3:[Omitted long matching line]
docs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
docs/paper/introduction.tex:10:\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
docs/paper/introduction.tex:14:In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. ContamCal, our two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), enables this characterization.
docs/paper/introduction.tex:18:[Omitted long matching line]
docs/paper/introduction.tex:19:    \item \textbf{No detectable item-specific memorization at current power levels.} Difference-in-differences analysis on 14{,}042 MMLU items finds no differential accuracy gain for contaminated vs.\ clean items in any model family (MDES 1.2--2.0pp on MMLU; ARC power is limited at 2.3--5.6pp). Results are consistent with global capability modulation.
docs/paper/appendix.tex:23:\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.}
docs/paper/appendix.tex:30:[Omitted long matching line]
docs/paper/appendix.tex:33:[Omitted long matching line]
docs/paper/appendix.tex:35:[Omitted long matching line]
docs/paper/appendix.tex:37:[Omitted long matching line]
docs/paper/appendix.tex:49:[Omitted long matching line]
docs/paper/appendix.tex:53:\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
docs/paper/appendix.tex:72:GSM8K evaluations use \texttt{max\_new\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
docs/paper/appendix.tex:302:[Omitted long matching line]
docs/paper/appendix.tex:307:We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\tau, \sigma)$ combinations. Table~\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\tau \in [0.5, 2.0]$~pp $\times$ $\sigma \in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.
docs/paper/appendix.tex:327:[Omitted long matching line]
docs/paper/appendix.tex:332:We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
docs/paper/appendix.tex:346:\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
docs/paper/appendix.tex:474:We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
docs/paper/appendix.tex:494:[Omitted long matching line]
docs/paper/results.tex:4:Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
docs/paper/results.tex:11:\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
docs/paper/results.tex:28:Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. This empirical taxonomy is preliminary at $N\!=\!5$ families.
docs/paper/results.tex:31:[Omitted long matching line]
docs/paper/results.tex:34:[Omitted long matching line]
docs/paper/results.tex:39:[Omitted long matching line]
docs/paper/results.tex:67:[Omitted long matching line]
docs/paper/results.tex:72:[Omitted long matching line]
docs/paper/main.aux:117:\@writefile{lof}{\contentsline {figure}{\numberline {1}{\ignorespaces MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\ref {tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times $ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref {sec:arc_cross_benchmark}.}}{2}{figure.caption.1}\protected@file@percent }
docs/paper/main.aux:119:\newlabel{fig:dose_response}{{1}{2}{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\ref {tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times $ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref {sec:arc_cross_benchmark}}{figure.caption.1}{}}
docs/paper/main.aux:554:[Omitted long matching line]
docs/paper/main.aux:555:\newlabel{tab:taxonomy}{{1}{6}{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta $acc: d000$\to $d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau ,\sigma )$ combinations; Appendix~\ref {sec:classification_sensitivity})}{table.caption.9}{}}
docs/paper/main.aux:1334:\@writefile{lot}{\contentsline {table}{\numberline {6}{\ignorespaces GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}}{13}{table.caption.22}\protected@file@percent }
docs/paper/main.aux:1335:\newlabel{tab:gsm8k_dose}{{6}{13}{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%)}{table.caption.22}{}}
docs/paper/main.aux:1565:\@writefile{lot}{\contentsline {table}{\numberline {14}{\ignorespaces Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq $3$\times $ default).}}{16}{table.caption.36}\protected@file@percent }
docs/paper/main.aux:1566:\newlabel{tab:sensitivity}{{14}{16}{Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq $3$\times $ default)}{table.caption.36}{}}
docs/paper/main.aux:1632:\@writefile{lof}{\contentsline {figure}{\numberline {7}{\ignorespaces Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta $acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}}{17}{figure.caption.37}\protected@file@percent }
docs/paper/main.aux:1633:\newlabel{fig:baseline_vs_effect}{{7}{17}{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta $acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families}{figure.caption.37}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "bedb43b0-6060-4a09-9c25-ca8d894a35ea",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/conclusion.tex:3:[Omitted long matching line]\ndocs/paper/main.log:580:\\OT1/ptm/m/n/10.95 three family-specific pat-terns on GSM8K\ndocs/paper/main.log:675:\\OT1/ptm/m/n/10.95 fies in-di-vid-ual seed tra-jec-to-ries. Family-level\ndocs/paper/main.log:700:\\OT1/ptm/m/n/10.95 Cross-family re-sults (\\TS1/ptm/m/n/10.95 �[][]\\OT1/ptm/m/n/\ndocs/paper/main.log:728: five-family\ndocs/paper/main.log:1088:\\OT1/ptm/m/n/10.95 cross-family com-par-isons of ab-so-lute val-ues\ndocs/paper/method.tex:61:[Omitted long matching line]\ndocs/paper/limitations.tex:4:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:7:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:20:\\textbf{GSM8K} \\citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\\% (vs.\\ 73--84\\% for other families), indicating CoT collapse rather than a contamination effect.\ndocs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/introduction.tex:3:[Omitted long matching line]\ndocs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).\ndocs/paper/introduction.tex:10:\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\ndocs/paper/introduction.tex:14:In our five-family sample, contamination vulnerability concentrates in the 65--70\\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\\times$ more fragile than 7B. ContamCal, our two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\\gamma_k$), enables this characterization.\ndocs/paper/introduction.tex:18:[Omitted long matching line]\ndocs/paper/introduction.tex:19:    \\item \\textbf{No detectable item-specific memorization at current power levels.} Difference-in-differences analysis on 14{,}042 MMLU items finds no differential accuracy gain for contaminated vs.\\ clean items in any model family (MDES 1.2--2.0pp on MMLU; ARC power is limited at 2.3--5.6pp). Results are consistent with global capability modulation.\ndocs/paper/appendix.tex:23:\\multicolumn{5}{l}{\\scriptsize $^{\\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.}\ndocs/paper/appendix.tex:30:[Omitted long matching line]\ndocs/paper/appendix.tex:33:[Omitted long matching line]\ndocs/paper/appendix.tex:35:[Omitted long matching line]\ndocs/paper/appendix.tex:37:[Omitted long matching line]\ndocs/paper/appendix.tex:49:[Omitted long matching line]\ndocs/paper/appendix.tex:53:\\caption{GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%).}\ndocs/paper/appendix.tex:72:GSM8K evaluations use \\texttt{max\\_new\\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.\ndocs/paper/appendix.tex:302:[Omitted long matching line]\ndocs/paper/appendix.tex:307:We assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\\tau, \\sigma)$ combinations. Table~\\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\\tau \\in [0.5, 2.0]$~pp $\\times$ $\\sigma \\in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.\ndocs/paper/appendix.tex:327:[Omitted long matching line]\ndocs/paper/appendix.tex:332:We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.\ndocs/paper/appendix.tex:346:\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}\ndocs/paper/appendix.tex:474:We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \\citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\\ref{tab:aicc_dr} reports AICc and Akaike weights.\ndocs/paper/appendix.tex:494:[Omitted long matching line]\ndocs/paper/results.tex:4:Cross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\ndocs/paper/results.tex:11:\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\\% stability across 30 reasonable $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\ndocs/paper/results.tex:28:Applying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. This empirical taxonomy is preliminary at $N\\!=\\!5$ families.\ndocs/paper/results.tex:31:[Omitted long matching line]\ndocs/paper/results.tex:34:[Omitted long matching line]\ndocs/paper/results.tex:39:[Omitted long matching line]\ndocs/paper/results.tex:67:[Omitted long matching line]\ndocs/paper/results.tex:72:[Omitted long matching line]\ndocs/paper/main.aux:117:\\@writefile{lof}{\\contentsline {figure}{\\numberline {1}{\\ignorespaces MMLU accuracy vs.\\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\\ref {tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\\times $ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref {sec:arc_cross_benchmark}.}}{2}{figure.caption.1}\\protected@file@percent }\ndocs/paper/main.aux:119:\\newlabel{fig:dose_response}{{1}{2}{MMLU accuracy vs.\\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\\ref {tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\\times $ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref {sec:arc_cross_benchmark}}{figure.caption.1}{}}\ndocs/paper/main.aux:554:[Omitted long matching line]\ndocs/paper/main.aux:555:\\newlabel{tab:taxonomy}{{1}{6}{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta $acc: d000$\\to $d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\\% stability across 30 reasonable $(\\tau ,\\sigma )$ combinations; Appendix~\\ref {sec:classification_sensitivity})}{table.caption.9}{}}\ndocs/paper/main.aux:1334:\\@writefile{lot}{\\contentsline {table}{\\numberline {6}{\\ignorespaces GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%).}}{13}{table.caption.22}\\protected@file@percent }\ndocs/paper/main.aux:1335:\\newlabel{tab:gsm8k_dose}{{6}{13}{GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%)}{table.caption.22}{}}\ndocs/paper/main.aux:1565:\\@writefile{lot}{\\contentsline {table}{\\numberline {14}{\\ignorespaces Profile classification stability across threshold parameter ranges. All families achieve 100\\% stability within the reasonable range; transitions occur only at extreme parameter values ($\\geq $3$\\times $ default).}}{16}{table.caption.36}\\protected@file@percent }\ndocs/paper/main.aux:1566:\\newlabel{tab:sensitivity}{{14}{16}{Profile classification stability across threshold parameter ranges. All families achieve 100\\% stability within the reasonable range; transitions occur only at extreme parameter values ($\\geq $3$\\times $ default)}{table.caption.36}{}}\ndocs/paper/main.aux:1632:\\@writefile{lof}{\\contentsline {figure}{\\numberline {7}{\\ignorespaces Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta $acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}}{17}{figure.caption.37}\\protected@file@percent }\ndocs/paper/main.aux:1633:\\newlabel{fig:baseline_vs_effect}{{7}{17}{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta $acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families}{figure.caption.37}{}}",
    "numLines": 51
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_01LwS4FdXnQdxzPeYTNhoSSt`</summary>

```json
{
  "pattern": "single.*family|one.*family|each.*observed.*one",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
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
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "dea43f90-7fe0-4b1a-b842-0b6f81023e9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 23 · 2026-05-22T07:29:01.108Z_

<details><summary>↩ Tool result · `toolu_01LwS4FdXnQdxzPeYTNhoSSt`</summary>

```text
docs/paper/limitations.tex:4:[Omitted long matching line]
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/appendix.tex:49:[Omitted long matching line]
docs/paper/experimental_setup.tex:9:[Omitted long matching line]
docs/paper/results.tex:34:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "00a72880-e711-4d4e-be47-89b30a254640",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/limitations.tex:4:[Omitted long matching line]\ndocs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/appendix.tex:49:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/results.tex:34:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01WtVfRX9nBN4PuXeEPvWQ16`</summary>

```json
{
  "pattern": "Collapse|V-recovery|two patterns|three patterns|four patterns",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
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
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "cd4b02c1-5381-409b-93de-609e13923766",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLvdXjyCLjhWacx7mEewYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14123
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 25 · 2026-05-22T07:29:02.328Z_

<details><summary>↩ Tool result · `toolu_01WtVfRX9nBN4PuXeEPvWQ16`</summary>

```text
docs/paper/method.tex:16:[Omitted long matching line]
docs/paper/method.tex:61:[Omitted long matching line]
docs/paper/method.tex:70:\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, \textsc{Benefit}\}$
docs/paper/method.tex:78:        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
docs/paper/method.tex:84:        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
docs/paper/method.tex:86:        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
docs/paper/method.tex:88:        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
docs/paper/limitations.tex:4:[Omitted long matching line]
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/appendix.tex:8:\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
docs/paper/appendix.tex:33:[Omitted long matching line]
docs/paper/appendix.tex:49:[Omitted long matching line]
docs/paper/appendix.tex:53:\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
docs/paper/appendix.tex:67:\multicolumn{7}{l}{\scriptsize $^{\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\
docs/paper/appendix.tex:145:Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
docs/paper/appendix.tex:318:Qwen2.5-14B & Collapse & 100\% & 100\% & $\tau = 9.4$ \\
docs/paper/appendix.tex:322:Qwen2.5-7B & V-recovery & 100\% & 72\% & $\tau = 3.0$ \\
docs/paper/appendix.tex:334:[Omitted long matching line]
docs/paper/appendix.tex:336:Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
docs/paper/appendix.tex:494:[Omitted long matching line]
docs/paper/experimental_setup.tex:20:\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
docs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
docs/paper/results.tex:19:Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
docs/paper/results.tex:20:V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
docs/paper/results.tex:31:[Omitted long matching line]
docs/paper/results.tex:34:[Omitted long matching line]
docs/paper/results.tex:39:[Omitted long matching line]
docs/paper/results.tex:56:Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
docs/paper/results.tex:57:Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
docs/paper/main.aux:1228:\@writefile{lot}{\contentsline {table}{\numberline {5}{\ignorespaces Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}}{12}{table.caption.19}\protected@file@percent }
docs/paper/main.aux:1229:\newlabel{tab:gsm8k_transfer}{{5}{12}{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT}{table.caption.19}{}}
docs/paper/main.aux:1334:\@writefile{lot}{\contentsline {table}{\numberline {6}{\ignorespaces GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}}{13}{table.caption.22}\protected@file@percent }
docs/paper/main.aux:1335:\newlabel{tab:gsm8k_dose}{{6}{13}{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%)}{table.caption.22}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "5592074f-1bd1-4c6d-b252-26e2bcb7a552",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/method.tex:16:[Omitted long matching line]\ndocs/paper/method.tex:61:[Omitted long matching line]\ndocs/paper/method.tex:70:\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{Collapse}, \\textsc{V-recovery}, \\textsc{Benefit}\\}$\ndocs/paper/method.tex:78:        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\ndocs/paper/method.tex:84:        \\State \\Return \\textsc{Collapse} \\Comment{severe monotonic degradation}\ndocs/paper/method.tex:86:        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\ndocs/paper/method.tex:88:        \\State \\Return \\textsc{Collapse} \\Comment{moderate decline, no V-shape}\ndocs/paper/limitations.tex:4:[Omitted long matching line]\ndocs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/appendix.tex:8:\\caption{Cross-benchmark transfer: MMLU vs.\\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}\ndocs/paper/appendix.tex:33:[Omitted long matching line]\ndocs/paper/appendix.tex:49:[Omitted long matching line]\ndocs/paper/appendix.tex:53:\\caption{GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%).}\ndocs/paper/appendix.tex:67:\\multicolumn{7}{l}{\\scriptsize $^{\\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\\\\ndocs/paper/appendix.tex:145:Fisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\ndocs/paper/appendix.tex:318:Qwen2.5-14B & Collapse & 100\\% & 100\\% & $\\tau = 9.4$ \\\\\ndocs/paper/appendix.tex:322:Qwen2.5-7B & V-recovery & 100\\% & 72\\% & $\\tau = 3.0$ \\\\\ndocs/paper/appendix.tex:334:[Omitted long matching line]\ndocs/paper/appendix.tex:336:Second, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\ndocs/paper/appendix.tex:494:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:20:\\textbf{GSM8K} \\citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\\% (vs.\\ 73--84\\% for other families), indicating CoT collapse rather than a contamination effect.\ndocs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).\ndocs/paper/results.tex:19:Collapse & Qwen-14B & 69.4\\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\\% \\\\\ndocs/paper/results.tex:20:V-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\ndocs/paper/results.tex:31:[Omitted long matching line]\ndocs/paper/results.tex:34:[Omitted long matching line]\ndocs/paper/results.tex:39:[Omitted long matching line]\ndocs/paper/results.tex:56:Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\\textsuperscript{B} & Harm & \\checkmark & Collapse \\\\\ndocs/paper/results.tex:57:Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\\textsuperscript{B} & Harm & $\\times$ & V-recovery \\\\\ndocs/paper/main.aux:1228:\\@writefile{lot}{\\contentsline {table}{\\numberline {5}{\\ignorespaces Cross-benchmark transfer: MMLU vs.\\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}}{12}{table.caption.19}\\protected@file@percent }\ndocs/paper/main.aux:1229:\\newlabel{tab:gsm8k_transfer}{{5}{12}{Cross-benchmark transfer: MMLU vs.\\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT}{table.caption.19}{}}\ndocs/paper/main.aux:1334:\\@writefile{lot}{\\contentsline {table}{\\numberline {6}{\\ignorespaces GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%).}}{13}{table.caption.22}\\protected@file@percent }\ndocs/paper/main.aux:1335:\\newlabel{tab:gsm8k_dose}{{6}{13}{GSM8K accuracy (\\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\\%)}{table.caption.22}{}}",
    "numLines": 33
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining files - method.tex and experimental_setup.tex - and also look at the Algorithm 1 classification logic in method.tex to answer the d100 question.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "1aa75e2f-1417-4245-aac6-683020b3fea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzcMi9W5bmrpY742nKejR1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29716,
      "cache_read_input_tokens": 25964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 29716
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

读取 method.tex 和 experimental_setup.tex 中的关键内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "5c1cd862-5a9c-4f5e-a1f0-703d281a748b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzcMi9W5bmrpY742nKejR1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29716,
      "cache_read_input_tokens": 25964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 29716
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

<details open><summary>🔧 Tool call — Read · `toolu_01KwNzVMgBrNCEB3H8MLL23b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "b56efd66-38ed-4517-97aa-53545857085d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzcMi9W5bmrpY742nKejR1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29716,
      "cache_read_input_tokens": 25964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 29716
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

_source line 29 · 2026-05-22T07:29:08.425Z_

<details><summary>↩ Tool result · `toolu_01KwNzVMgBrNCEB3H8MLL23b`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard smoothing constant, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to $e_{ij} \in [0,1]$; the distribution is highly right-skewed (mean 0.041).
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\paragraph{Primary model: 2PL+$\gamma$.}
29	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
30	\begin{equation}
31	\label{eq:2pl_gamma}
32	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
33	\end{equation}
34	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\gamma_k$ with per-domain effects $\gamma_d$ ($d=1,\ldots,D$), fitting Eq.~\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\S\ref{sec:domain_differential}).
35	
36	We place $\gamma_k$ outside the item discrimination bracket ($\sigma(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij})$) rather than the standard DIF form ($\sigma(a_i(\theta_j - b_i + \gamma \cdot e))$), modeling contamination as a uniform logit shift that does not scale with item discrimination. This corresponds to the uniform DIF specification \citep{de_ayala_2009_irt}; the alternative non-uniform form would assume contamination effects are amplified for high-discrimination items, an assumption we lack evidence to support.
37	
38	The additive structure shifts the effective difficulty of item~$i$ by $\gamma_k \cdot e_{ij} / a_i$ units on the ability scale.
39	
40	For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
41	
42	\paragraph{Inference.}
43	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
44	
45	\paragraph{Calibrated score.}
46	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
47	\begin{equation}
48	\label{eq:calibrated}
49	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
50	\end{equation}
51	with credible intervals from posterior quantiles. In practice, we average $\sigma(a_i(\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.
52	
53	\paragraph{Identifiability.}
54	\label{sec:fisher}
55	\label{sec:value_decomposition}
56	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}). Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
57	
58	\subsection{Dose-Response Profile Classification}
59	\label{sec:classification}
60	
61	Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern, drawing on the dose-response modeling tradition in pharmacology \citep{hill1910aggregation,ritz2015dose}. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by noise threshold $\tau$, severity threshold $\sigma$, saturation ratio $\rho$, and late-gain floor $\lambda$. The top-level split is governed by $\Delta = a_{100} - a_0$ relative to $\tau$; within-branch refinements distinguish Collapse from V-recovery via mid-dosage trough detection. A mid-trajectory volatility check ($v^*$) distinguishes true immunity (Phi-4: $v^* = 0.34$pp) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $v^* = 3.22$pp $> \tau$). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms all families are stable across all $(\tau, \sigma)$ combinations (180/180 model--seed--threshold pairs; Appendix~\ref{sec:classification_sensitivity}).
62	
63	\begin{algorithm}[H]
64	\caption{Dose-Response Profile Classification}
65	\label{alg:profile-classification}
66	\begin{algorithmic}[1]
67	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
68	\Require Noise threshold $\tau = 2$ pp, severity threshold $\sigma = 5$ pp
69	\Require Saturation ratio $\rho = 0.3$, late-gain floor $\lambda = 0.5$ pp
70	\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, \textsc{Benefit}\}$
71	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
72	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
73	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
74	\If{$|\Delta| \le \tau$}
75	    \If{$v^* \le \tau$}
76	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
77	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
78	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
79	    \Else
80	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
81	    \EndIf
82	\ElsIf{$\Delta < -\tau$}
83	    \If{$\Delta \le -\sigma$}
84	        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
85	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
86	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
87	    \Else
88	        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
89	    \EndIf
90	\Else \Comment{$\Delta > \tau$}
91	    \State $g_1 \gets a_{25} - a_{0}$ \Comment{first-half gain}
92	    \State $g_2 \gets a_{100} - a_{25}$ \Comment{second-half gain}
93	    \State $\ell \gets a_{100} - a_{50}$ \Comment{late gain}
94	    \If{$(g_1 > 0$ \textbf{and} $g_2 < \rho \cdot g_1)$ \textbf{or} $\ell < \lambda$}
95	        \State \Return \textsc{Benefit} \Comment{saturating gain}
96	    \Else
97	        \State \Return \textsc{Benefit} \Comment{sustained gain}
98	    \EndIf
99	\EndIf
100	\end{algorithmic}
101	\end{algorithm}
102	
103	\paragraph{Family-level aggregation.}
104	Algorithm~\ref{alg:profile-classification} classifies individual seed trajectories. Family-level classification uses \emph{direction} as the primary criterion (\S\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\Delta$(d100) includes zero and $|\text{mean}~\Delta| < \tau$; Borderline if the CI includes zero but $|\text{mean}~\Delta| \geq \tau$; otherwise Harm/Benefit by sign, with per-seed shape providing supplementary characterization. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms Algorithm~\ref{alg:profile-classification}'s classifications for extreme effects but lacks power to resolve moderate patterns at $n\!=\!3$ seeds, motivating the per-seed rule-based approach. Our methodological contribution lies not in the IRT specification---which follows standard explanatory IRT practice---but in the controlled SFT injection paradigm that enables causal dose-response profiling of contamination effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "d9f5785b-aea9-47fc-b5d2-e26caffb2b45",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \\citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \\citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \\in [0,1]$, fitting per-benchmark models to handle the shared item pool \\citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we consider four candidate detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{zhang_2024_minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \\citep{kadavath2022}; concurrent work by \\citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\\mathcal{S} = \\{\\text{S1, S2, S4}\\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\\ref{sec:sij_classification}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack_2009_rrf}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s \\in \\mathcal{S}} \\frac{1}{\\kappa + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\\kappa=60$ is the standard smoothing constant, and $|\\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to $e_{ij} \\in [0,1]$; the distribution is highly right-skewed (mean 0.041).\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic (2PL) model \\citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\\gamma_k$ with per-domain effects $\\gamma_d$ ($d=1,\\ldots,D$), fitting Eq.~\\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\\S\\ref{sec:domain_differential}).\n\nWe place $\\gamma_k$ outside the item discrimination bracket ($\\sigma(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij})$) rather than the standard DIF form ($\\sigma(a_i(\\theta_j - b_i + \\gamma \\cdot e))$), modeling contamination as a uniform logit shift that does not scale with item discrimination. This corresponds to the uniform DIF specification \\citep{de_ayala_2009_irt}; the alternative non-uniform form would assume contamination effects are amplified for high-discrimination items, an assumption we lack evidence to support.\n\nThe additive structure shifts the effective difficulty of item~$i$ by $\\gamma_k \\cdot e_{ij} / a_i$ units on the ability scale.\n\nFor MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\\ref{sec:4pl_details}); this requires $J \\geq 16$ and is not used in domain-level analyses ($J = 13$).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_k \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. In practice, we average $\\sigma(a_i(\\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.\n\n\\paragraph{Identifiability.}\n\\label{sec:fisher}\n\\label{sec:value_decomposition}\nThe reliability of $\\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\\geq$0.55 with $J \\geq 50$ (Appendix~\\ref{sec:identifiability_appendix}). Eq.~\\eqref{eq:calibrated} depends on $\\theta_j$, not $\\gamma$ directly, predicting that vanilla 2PL ($\\gamma\\!=\\!0$) achieves comparable calibration to 2PL+$\\gamma$, with $\\gamma_k$ serving diagnosis rather than calibration (\\S\\ref{sec:calibration_results}).\n\n\\subsection{Dose-Response Profile Classification}\n\\label{sec:classification}\n\nIndependent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern, drawing on the dose-response modeling tradition in pharmacology \\citep{hill1910aggregation,ritz2015dose}. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The top-level split is governed by $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish Collapse from V-recovery via mid-dosage trough detection. A mid-trajectory volatility check ($v^*$) distinguishes true immunity (Phi-4: $v^* = 0.34$pp) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $v^* = 3.22$pp $> \\tau$). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms all families are stable across all $(\\tau, \\sigma)$ combinations (180/180 model--seed--threshold pairs; Appendix~\\ref{sec:classification_sensitivity}).\n\n\\begin{algorithm}[H]\n\\caption{Dose-Response Profile Classification}\n\\label{alg:profile-classification}\n\\begin{algorithmic}[1]\n\\Require Accuracy vector $\\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \\in \\{0, 5, 25, 50, 100\\}\\%$\n\\Require Noise threshold $\\tau = 2$ pp, severity threshold $\\sigma = 5$ pp\n\\Require Saturation ratio $\\rho = 0.3$, late-gain floor $\\lambda = 0.5$ pp\n\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{Collapse}, \\textsc{V-recovery}, \\textsc{Benefit}\\}$\n\\State $\\Delta \\gets a_{100} - a_{0}$ \\Comment{end-to-end accuracy shift}\n\\State $m^* \\gets \\min(a_{5},\\, a_{25},\\, a_{50})$ \\Comment{mid-dosage minimum}\n\\State $v^* \\gets \\max_{i \\in \\{5,25,50\\}} |a_i - a_0|$ \\Comment{max mid-trajectory deviation}\n\\If{$|\\Delta| \\le \\tau$}\n    \\If{$v^* \\le \\tau$}\n        \\State \\Return \\textsc{Immune} \\Comment{fluctuation within noise band}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\n    \\Else\n        \\State \\Return \\textsc{Immune} \\Comment{non-V volatility, endpoint stable}\n    \\EndIf\n\\ElsIf{$\\Delta < -\\tau$}\n    \\If{$\\Delta \\le -\\sigma$}\n        \\State \\Return \\textsc{Collapse} \\Comment{severe monotonic degradation}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\n    \\Else\n        \\State \\Return \\textsc{Collapse} \\Comment{moderate decline, no V-shape}\n    \\EndIf\n\\Else \\Comment{$\\Delta > \\tau$}\n    \\State $g_1 \\gets a_{25} - a_{0}$ \\Comment{first-half gain}\n    \\State $g_2 \\gets a_{100} - a_{25}$ \\Comment{second-half gain}\n    \\State $\\ell \\gets a_{100} - a_{50}$ \\Comment{late gain}\n    \\If{$(g_1 > 0$ \\textbf{and} $g_2 < \\rho \\cdot g_1)$ \\textbf{or} $\\ell < \\lambda$}\n        \\State \\Return \\textsc{Benefit} \\Comment{saturating gain}\n    \\Else\n        \\State \\Return \\textsc{Benefit} \\Comment{sustained gain}\n    \\EndIf\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Family-level aggregation.}\nAlgorithm~\\ref{alg:profile-classification} classifies individual seed trajectories. Family-level classification uses \\emph{direction} as the primary criterion (\\S\\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\\Delta$(d100) includes zero and $|\\text{mean}~\\Delta| < \\tau$; Borderline if the CI includes zero but $|\\text{mean}~\\Delta| \\geq \\tau$; otherwise Harm/Benefit by sign, with per-seed shape providing supplementary characterization. Parametric model selection (Appendix~\\ref{sec:parametric_dr}) confirms Algorithm~\\ref{alg:profile-classification}'s classifications for extreme effects but lacks power to resolve moderate patterns at $n\\!=\\!3$ seeds, motivating the per-seed rule-based approach. Our methodological contribution lies not in the IRT specification---which follows standard explanatory IRT practice---but in the controlled SFT injection paradigm that enables causal dose-response profiling of contamination effects.",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01TLCREErFgJphjm6JY42vPP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "d7b7d74e-f5da-41d2-8df2-d7764125cdac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzcMi9W5bmrpY742nKejR1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29716,
      "cache_read_input_tokens": 25964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 29716
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

_source line 31 · 2026-05-22T07:29:08.808Z_

<details><summary>↩ Tool result · `toolu_01TLCREErFgJphjm6JY42vPP`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). We additionally validate our dose-response profiles on a held-out fifth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during taxonomy construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via MAE (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines: \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "3280d081-6a75-4d7e-9c5d-be1074c74ea6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\subsection{Controlled SFT Injection}\n\\label{sec:injection}\n\nWe construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \\citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \\citep{abdin2024phi4} (14.7B), OLMo-2 \\citep{olmo2team2025} (7B), and Gemma-2 \\citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \\citep{hu2022lora} ($r=16$, $\\alpha=32$, lr$=5\\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\\%, clean control), d005 (5\\%), d025 (25\\%), d050 (50\\%), and d100 (100\\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples.\n\nQwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\\% at d000 to 98\\% at d100; \\S\\ref{sec:signal_failure}). We additionally validate our dose-response profiles on a held-out fifth family, LLaMA-3.1-8B \\citep{grattafiori2024llama3} (Meta), which was not used during taxonomy construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\\ref{alg:profile-classification} generalizes to unseen model families.\n\n\\subsection{Benchmarks, Domains, and Evaluation}\n\\label{sec:benchmarks}\n\nWe evaluate on three benchmarks spanning distinct cognitive demands and response formats.\n\n\\textbf{MMLU} \\citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \\& Engineering, Medical, Humanities, Social Sciences, Business \\& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\\S\\ref{sec:results}).\n\n\\textbf{ARC-Challenge} \\citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.\n\n\\textbf{GSM8K} \\citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\\% (vs.\\ 73--84\\% for other families), indicating CoT collapse rather than a contamination effect.\n\nAll multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.\n\nWe assess calibration quality via MAE (calibrated vs.\\ ground-truth clean accuracy), Kendall $\\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\\gamma$ direction ($P(\\gamma\\!<\\!0 \\mid \\text{data})$), and split-$\\hat{R}$ convergence.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\nWe compare against seven baselines: \\textbf{B0-Raw} (no adjustment), \\textbf{B1-Remove\\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \\textbf{B2-Single2PL+$\\gamma$} (aggregate $\\gamma$ without domain stratification), \\textbf{B3-Vanilla2PL} ($\\gamma=0$, isolating IRT ability estimation), \\textbf{B4-LinearRegression} (residuals on exposure scores), \\textbf{B5-Emperor} (mitigation strategies from \\citet{sun2025emperor}; B5b uses the best-performing variant), and \\textbf{B6-DCR} (our reimplementation following \\citealp{xu2025dcr}).",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
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
Now I have all the information I need. Let me compile the Falcon3 integration checklist.

Key findings from the scan:

1. **Current state**: The paper describes experiments on:
   - 4 families from 4 labs: Qwen2.5, Phi-4, OLMo-2, Gemma-2
   - Plus LLaMA-3.1-8B as out-of-sample validation (5th family)
   - "five models spanning four independent families"
   - Falcon3-7B-Base would be a 6th model / 5th independent family (TII)
   
2. **Family counts throughout the paper**: The abstract, introduction, results, and conclusion all consistently reference "five models spanning four independent families" and use "five-family sample" language, with specific counts like "2/5" and "4/5" for pattern attestation across families. The limitations section begins discussing out-of-sample validation coverage.

3. **Algorithm 1 requirements**: The profile classification algorithm needs the full accuracy vector at five dosage points (0, 5, 25, 50, 100%), with the 100% dosage being critical for computing the delta between endpoints, which serves as the primary split criterion. The algorithm also uses the minimum accuracy across the intermediate dosages.

4. **Precedent from LLaMA-3.1**: That model was validated with only three dosage levels but still included the 100% dosage point, establishing that this endpoint is consistently necessary.

For Phase 3, I'm considering whether we can evaluate patterns using only d000-d050 without the d100 measurement. Algorithm 1 fundamentally requires d100 to compute the delta that drives the entire classification logic, so we can't fully run it without that endpoint. That said, the intermediate dosages alone could provide an early signal—severe decline at d050 would suggest Collapse is likely, while improvement would point toward Benefit, though we'd lose information about saturation effects. V-recovery detection specifically needs both the mid-range points and the endpoint to work properly. So partial evaluation is possible for preliminary signals, but the complete algorithm can't execute without d100.

Now I'm thinking through what changes with Falcon3—

it would add TII as a fifth lab, bringing the total to six models across five independent families. This means updating all the references throughout the paper: the taxonomy table needs a new row, the cross-seed comparisons need revision, and all the fraction references like "2/5" or "5/5" need recalculating. Looking at the current paper, it mentions "five models spanning four independent families," which are Qwen-7B, Qwen-14B, Phi-4, OLMo-2, and Gemma-2. So with Falcon3 added as a main taxonomy member, I'd have six models spanning five independent families from five labs, with LLaMA-3.1-8B serving as the held-out sixth family for validation—making it a "six-family sample" overall.

Let me lay out the full checklist to keep this organized.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "6e1c09aa-169e-4c2c-b11c-2b180abaacfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtrcXop8XA6qEtiu8T4Gxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 55680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

搜索更多关键词补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "047fac34-4301-4d9b-8aa1-9a37b1d6b9f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtrcXop8XA6qEtiu8T4Gxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 55680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

<details open><summary>🔧 Tool call — Grep · `toolu_01Wk4wgDCfGkZ9y8ygyGA4HE`</summary>

```json
{
  "pattern": "N\\s*[=!]\\s*5|N=5|\\\\$N\\\\$\\s*=\\s*5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "64517a86-f067-48dc-a928-181c551ff9d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtrcXop8XA6qEtiu8T4Gxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 55680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 35 · 2026-05-22T07:29:44.169Z_

<details><summary>↩ Tool result · `toolu_01Wk4wgDCfGkZ9y8ygyGA4HE`</summary>

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
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "bf25cb17-da54-4b86-88ed-acb67fb342d8",
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

<details open><summary>🔧 Tool call — Grep · `toolu_016B5u2JG44iz4X2gYf48SLN`</summary>

```json
{
  "pattern": "[2345]/5|five.family|six.family",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "7d66b6ed-6b2e-4ae3-8758-c8241e20ef04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtrcXop8XA6qEtiu8T4Gxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 55680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 37 · 2026-05-22T07:29:45.464Z_

<details><summary>↩ Tool result · `toolu_016B5u2JG44iz4X2gYf48SLN`</summary>

```text
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/conclusion.tex:3:[Omitted long matching line]
docs/paper/appendix.tex:35:[Omitted long matching line]
docs/paper/appendix.tex:37:[Omitted long matching line]
docs/paper/appendix.tex:42:\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
docs/paper/results.tex:11:\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
docs/paper/results.tex:31:[Omitted long matching line]
docs/paper/results.tex:39:[Omitted long matching line]
docs/paper/results.tex:48:\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 2/5; classification-level direction agreement is 4/5 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 2/5.}
docs/paper/results.tex:67:[Omitted long matching line]
docs/paper/introduction.tex:10:\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
docs/paper/introduction.tex:14:In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. ContamCal, our two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), enables this characterization.
docs/paper/introduction.tex:18:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "f329b5bc-2faa-41d7-b51e-a017fb5af807",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/conclusion.tex:3:[Omitted long matching line]\ndocs/paper/appendix.tex:35:[Omitted long matching line]\ndocs/paper/appendix.tex:37:[Omitted long matching line]\ndocs/paper/appendix.tex:42:\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\ndocs/paper/results.tex:11:\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\\% stability across 30 reasonable $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\ndocs/paper/results.tex:31:[Omitted long matching line]\ndocs/paper/results.tex:39:[Omitted long matching line]\ndocs/paper/results.tex:48:\\caption{Cross-seed $\\Delta$acc (d000$\\to$d100). Strict sign consistency (Cons.) is 2/5; classification-level direction agreement is 4/5 (see text). Per-seed shape classification\\textsuperscript{$\\ddagger$} agrees for only 2/5.}\ndocs/paper/results.tex:67:[Omitted long matching line]\ndocs/paper/introduction.tex:10:\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot, seed$=$42; cross-seed patterns in Table~\\ref{tab:cross_seed}). In our five-family sample, vulnerability concentrates in the 65--70\\% baseline band; models at extreme baselines (low or high) show limited sensitivity. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\ndocs/paper/introduction.tex:14:In our five-family sample, contamination vulnerability concentrates in the 65--70\\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\\times$ more fragile than 7B. ContamCal, our two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\\gamma_k$), enables this characterization.\ndocs/paper/introduction.tex:18:[Omitted long matching line]",
    "numLines": 13
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01S93oh2JzbFQtz6nz5Y2rFy`</summary>

```json
{
  "pattern": "four labs|four independent|five independent|five labs",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "2af17872-520e-4c8a-9bca-b34796bc5e23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtrcXop8XA6qEtiu8T4Gxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 55680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 39 · 2026-05-22T07:29:46.506Z_

<details><summary>↩ Tool result · `toolu_01S93oh2JzbFQtz6nz5Y2rFy`</summary>

```text
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/appendix.tex:346:\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
docs/paper/experimental_setup.tex:7:[Omitted long matching line]
docs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
docs/paper/results.tex:4:Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "bedf018a-0118-4159-97d3-938b56bcb8fb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/appendix.tex:346:\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}\ndocs/paper/experimental_setup.tex:7:[Omitted long matching line]\ndocs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).\ndocs/paper/results.tex:4:Cross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.",
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
Now I have a comprehensive picture. Let me also check for "Alibaba, Microsoft, Allen AI, Google" to find lab listing mentions, and any references to specific model counts in experimental_setup.tex.

Let me also check the fractions more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "a6d1f151-5584-41c9-bf16-3e6e5d01ccc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1GBdyuRyXntR6yr1i3tck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 61227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3106
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

_source line 41_

最后搜索一些关键数字和 pattern 统计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "8bd61f24-3fbe-44ac-a2ff-5fb005f6913a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1GBdyuRyXntR6yr1i3tck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 61227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3106
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

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_015oiGqL1wEVMqPMKAURVP5Q`</summary>

```json
{
  "pattern": "Alibaba.*Microsoft|four labs|five labs",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "b07ed810-1b21-42c2-80b0-11435bfdf170",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1GBdyuRyXntR6yr1i3tck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 61227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3106
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

_source line 43 · 2026-05-22T07:29:51.950Z_

<details><summary>↩ Tool result · `toolu_015oiGqL1wEVMqPMKAURVP5Q`</summary>

```text
docs/paper/experimental_setup.tex:7:[Omitted long matching line]
docs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "66e38820-f8bd-4838-84b5-c0ba72275572",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experimental_setup.tex:7:[Omitted long matching line]\ndocs/paper/introduction.tex:5:We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns (Figure~\\ref{fig:dose_response})---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds).",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Grep · `toolu_01DeAcYwgFEFQAHkofNq5aTR`</summary>

```json
{
  "pattern": "two or more independent|one family|each observed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "ccc6c58e-2ba9-452f-af1f-4dc45065c760",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1GBdyuRyXntR6yr1i3tck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 61227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3106
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

_source line 45 · 2026-05-22T07:29:53.348Z_

<details><summary>↩ Tool result · `toolu_01DeAcYwgFEFQAHkofNq5aTR`</summary>

```text
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/results.tex:34:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "67b20699-3c97-4fc6-a9a1-89eb4ddd6a59",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/results.tex:34:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Grep · `toolu_01KoBDLJD4RDnypdN876oK9u`</summary>

```json
{
  "pattern": "held-out|out-of-sample|LLaMA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "a26319a6-7503-404c-b2aa-ae6050dce3b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1GBdyuRyXntR6yr1i3tck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 61227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3106
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

_source line 47 · 2026-05-22T07:29:54.122Z_

<details><summary>↩ Tool result · `toolu_01KoBDLJD4RDnypdN876oK9u`</summary>

```text
docs/paper/conclusion.tex:3:[Omitted long matching line]
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/appendix.tex:8:\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
docs/paper/appendix.tex:19:LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
docs/paper/appendix.tex:49:[Omitted long matching line]
docs/paper/appendix.tex:64:LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\
docs/paper/experimental_setup.tex:9:[Omitted long matching line]
docs/paper/introduction.tex:18:[Omitted long matching line]
docs/paper/results.tex:34:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "a8ec7791-51b9-4a09-b7e8-9ea52a06df62",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/conclusion.tex:3:[Omitted long matching line]\ndocs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/appendix.tex:8:\\caption{Cross-benchmark transfer: MMLU vs.\\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}\ndocs/paper/appendix.tex:19:LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\\ddagger}$ & --- & Asymmetric \\\\\ndocs/paper/appendix.tex:49:[Omitted long matching line]\ndocs/paper/appendix.tex:64:LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\\\\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/introduction.tex:18:[Omitted long matching line]\ndocs/paper/results.tex:34:[Omitted long matching line]",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me compile the full checklist.

Current paper structure:
- **Main taxonomy**: 5 models (Qwen-7B, Qwen-14B, Phi-4, OLMo-2, Gemma-2) from 4 families (Qwen, Phi, OLMo, Gemma) from 4 labs (Alibaba, Microsoft, Allen AI, Google)
- **Out-of-sample validation**: LLaMA-3.1-8B (Meta) = 5th family


- **Five-family sample**: includes all 5 families with LLaMA counted

Adding Falcon3-7B-Base (TII, 67.4% MMLU baseline) would expand the taxonomy to 6 models from 5 families across 5 labs, with LLaMA bringing it to a 6-family sample total. Falcon3's baseline performance sits squarely in the vulnerable band (65-70%), making it a strong candidate for the full 5-dosage training protocol.

Falcon3 at 67.4% falls right alongside Qwen-7B (66.1%) and Qwen-14B (69.4%) in that critical range—any of the four patterns could emerge from this group.

Now examining Algorithm 1's requirements: it mandates all five dosage points (d0, d5, d25, d50, d100), with the primary split criterion depending on d100 specifically. The algorithm uses d100 minus d0 as the key differentiator, while the intermediate points inform the minimum midpoint value and maximum deviation calculations.

Throughout the algorithm, d100 appears repeatedly—it's essential for the top-level split decision, for determining benefit subtypes through saturation versus sustained response comparisons, and for detecting V-recovery patterns. Without d100, Algorithm 1 simply cannot execute. That said, the algorithm could potentially function with just d0 through d50 if necessary, though with significant limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "08b27e43-94d6-4913-bf73-b9f03b739537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qi2q1sNfXPq4qWfTXwqj4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 64333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
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

_source line 49_

## Falcon3 论文整合清单

### 当前论文架构

- **Main taxonomy**: 5 models (Qwen-7B, Qwen-14B, Phi-4, OLMo-2, Gemma-2) / 4 families / 4 labs
- **Out-of-sample validation**: LLaMA-3.1-8B (Meta) = 第 5 family
- Falcon3-7B-Base (TII, 67.4% MMLU) 加入后 → **6 models / 5 families / 5 labs** + LLaMA validation = 6-family sample

Falcon3 的 67.4% baseline 落在 **vulnerable band (65–70%)** 内，与 Qwen-7B (66.1%) 和 Qwen-14B (69.4%) 同区间，四种 pattern 均有可能。

---

### 必须更新（结果出来后）

| # | 文件:行号 | 当前文本 | 更新内容 |
|---|----------|---------|---------|
| 1 | `abstract.tex:1` | "five models spanning four independent families" | → "six models spanning five independent families" |
| 2 | `abstract.tex:1` | "five-family sample" (×3处) | → "six-family sample" |
| 3 | `abstract.tex:1` | "Out-of-sample validation on a held-out fifth family" | → "held-out sixth family" |
| 4 | `abstract.tex:1` | "Two patterns (Immune, Benefit) are attested in two or more independent families; Collapse and V-recovery are each observed in one family" | → 按 Falcon3 pattern 更新计数 |
| 5 | `introduction.tex:5` | "five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google)" | → "six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII)" |
| 6 | `introduction.tex:10` | "In our five-family sample" (Figure 1 caption) | → "six-family sample" |
| 7 | `introduction.tex:14` | "In our five-family sample, contamination vulnerability..." | → "six-family sample" |
| 8 | `introduction.tex:18` | "four families reveals qualitatively different..." | → "five families" |
| 9 | `results.tex:4` | "five models from four independent families" | → "six models from five independent families" |
| 10 | `results.tex:11` | Table 1 caption: "5/5 families" | → "6/6 families" (如果 Falcon3 也 stable) |
| 11 | `results.tex:16–23` | Table 1 (tab:taxonomy) 数据行 | 新增 Falcon3 行 |
| 12 | `results.tex:28` | "$N\!=\!5$ families" | → "$N\!=\!6$" |
| 13 | `results.tex:31` | "In our five-family sample..." 整段 baseline gradient | 加入 Falcon3 数据点，更新 vulnerable band 描述 |
| 14 | `results.tex:34` | "Two of four patterns...are attested in ≥2 independent families" | → 按实际更新 |
| 15 | `results.tex:48` | Table 2 caption: "2/5...4/5...2/5" | → x/6 |
| 16 | `results.tex:51–64` | Table 2 (tab:cross_seed) 数据行 | 新增 Falcon3 行 |
| 17 | `results.tex:67` | "Strict sign consistency holds for 2/5...4/5" | → x/6 |
| 18 | `conclusion.tex:3` | "five-family sample" | → "six-family sample" |
| 19 | `experimental_setup.tex:7` | "four independent model families from four labs" + 模型列表 | 加入 "Falcon3 \citep{...} (7B)" + TII |
| 20 | `experimental_setup.tex:9` | "yields over 50 checkpoints" | 更新 checkpoint 总数 |
| 21 | `appendix.tex:42` | Fig caption "4/5 models" | → "x/6 models" (按 ARC 一致性) |
| 22 | `appendix.tex:346` | Fig 7 caption "four independent families" | → "five independent families" |
| 23 | `appendix.tex:307–327` | Table 14 (classification sensitivity) | 新增 Falcon3 行 |

**图表必须重新生成：**
- `fig_dose_response.pdf` — 加 Falcon3 曲线
- `fig_baseline_vs_effect.pdf` — 加 Falcon3 数据点
- `fig_arc_dose_response.pdf` — 加 Falcon3 曲线（如有 ARC eval）
- Table 1, Table 2, Table 5 (gsm8k_transfer), Table 6 (gsm8k_dose), Table 14 (sensitivity)

---

### 条件更新（取决于 Falcon3 pattern）

**如果 Falcon3 = Benefit:**
- `abstract.tex:1` → "Three patterns (Immune, Benefit, ...) are attested in ≥2 families" — Benefit 从 2 family 变 3 family
- `results.tex:34` → Benefit 的 family-level replication 增强
- `limitations.tex:4` → "Out-of-sample validation covers only the Immune pattern" 仍不变（除非 Benefit 也算 validated）
- Benefit band 扩展到 67.4%，削弱 "vulnerability concentrates in 65–70%" 的说法（因为同区间也出现了 Benefit）

**如果 Falcon3 = Collapse:**
- `abstract.tex:1` → "Collapse...attested in two independent families" — 最大变化，Collapse 不再是 single-family
- `results.tex:34` → 删除 "Collapse...observed in one family...require additional replication"
- `limitations.tex:4` → 可删 "independent-family replication of Collapse...remains open"（Collapse 已 replicated）
- 极大强化论文结论：两个独立 family 在 vulnerable band 都 Collapse

**如果 Falcon3 = Immune:**
- `abstract.tex` → "Immune attested in three families" — 有趣但与 67.4% baseline 矛盾 (vulnerable band 内的 Immune)
- `results.tex:31` → 需修改 "above [76%], immune" 的表述，因为 67.4% 也 Immune
- 削弱 baseline gradient 叙事

**如果 Falcon3 = V-recovery:**
- `abstract.tex:1` → "V-recovery attested in two independent families" — V-recovery 不再是 single-family
- `results.tex:34` → 删除 "V-recovery...observed in one family...require additional replication"
- `limitations.tex:4` → 可删 V-recovery 的 replication caveat
- 在 vulnerable band 内出现第二个 V-recovery，强化 band-specific vulnerability

---

### 不需要更新

- **method.tex** — Algorithm 1 逻辑不变，仅适用范围从 "four families" 隐式扩展
- **IRT calibration 部分** (results.tex §5.5–5.7) — 仍基于 Qwen2.5 within-family，Falcon3 不影响
- **Signal failure 部分** (results.tex §5.6) — Min-K\%++ 分析不涉及 Falcon3（除非另做）
- **DiD memorization test** (results.tex §5.4, Table 3) — 除非对 Falcon3 也做 DiD
- **Domain-level analysis** (results.tex §5.7) — 仍基于 Qwen2.5
- **Prior sensitivity** (appendix) — 仍基于 Qwen2.5

---

### Phase 3: 先 eval d000–d050 不等 d100 的可行性

**Algorithm 1 明确要求 d100。** 分析 `method.tex:63-101`：

```
Line 67: Require a = (a_0, a_5, a_25, a_50, a_100)  ← 显式要求全 5 个 dosage
Line 71: Δ = a_100 - a_0                              ← 顶层分类判据
Line 77: m* < a_100                                    ← V-recovery 检测
Line 85: m* < a_100                                    ← V-recovery 检测
Line 92: g_2 = a_100 - a_25                            ← Benefit subtype
Line 93: ℓ = a_100 - a_50                              ← Benefit subtype
```

**结论：不能在没有 d100 的情况下运行 Algorithm 1，也不能填入 Table 1。**

但 **d000–d050 可以提供有价值的早期信号**：

| d050 观测 | 初步判断 | 置信度 |
|-----------|---------|--------|
| Δ(d050) < −5pp | 极可能 Collapse | 高 — 因为 d100 只会更差 |
| d005/d025 有 V-dip 但 d050 回升 | 可能 V-recovery | 中 — 需 d100 确认 endpoint |
| 单调上升 >2pp | 可能 Benefit | 中 — 需 d100 确认是否 saturate |
| 全程 ±2pp 内 | 可能 Immune | 中 — d100 可能突变 |

**LLaMA-3.1 先例**：LLaMA 仅训练了 d000/d025/d100 三个点（跳了 d005/d050），但仍有 d100。没有跳 d100 的先例。

**建议**：可以先跑 d000–d050 的 eval 获取方向信号（特别是 Falcon3 baseline 在 vulnerable band 内，early signal 很有价值），但论文正式结果必须等 d100 完成。如果 d050 已经明确 Collapse（>5pp decline），d100 的 eval 优先级可以降低（结果可预测）；其他 pattern 则必须等 d100。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "uuid": "6dd270de-190d-42a1-ab08-ea18fdb62c62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qi2q1sNfXPq4qWfTXwqj4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 64333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
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

_source line 50_

## Falcon3 论文整合清单

### 当前论文架构

- **Main taxonomy**: 5 models (Qwen-7B, Qwen-14B, Phi-4, OLMo-2, Gemma-2) / 4 families / 4 labs
- **Out-of-sample validation**: LLaMA-3.1-8B (Meta) = 第 5 family
- Falcon3-7B-Base (TII, 67.4% MMLU) 加入后 → **6 models / 5 families / 5 labs** + LLaMA validation = 6-family sample

Falcon3 的 67.4% baseline 落在 **vulnerable band (65–70%)** 内，与 Qwen-7B (66.1%) 和 Qwen-14B (69.4%) 同区间，四种 pattern 均有可能。

---

### 必须更新（结果出来后）

| # | 文件:行号 | 当前文本 | 更新内容 |
|---|----------|---------|---------|
| 1 | `abstract.tex:1` | "five models spanning four independent families" | → "six models spanning five independent families" |
| 2 | `abstract.tex:1` | "five-family sample" (×3处) | → "six-family sample" |
| 3 | `abstract.tex:1` | "Out-of-sample validation on a held-out fifth family" | → "held-out sixth family" |
| 4 | `abstract.tex:1` | "Two patterns (Immune, Benefit) are attested in two or more independent families; Collapse and V-recovery are each observed in one family" | → 按 Falcon3 pattern 更新计数 |
| 5 | `introduction.tex:5` | "five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google)" | → "six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII)" |
| 6 | `introduction.tex:10` | "In our five-family sample" (Figure 1 caption) | → "six-family sample" |
| 7 | `introduction.tex:14` | "In our five-family sample, contamination vulnerability..." | → "six-family sample" |
| 8 | `introduction.tex:18` | "four families reveals qualitatively different..." | → "five families" |
| 9 | `results.tex:4` | "five models from four independent families" | → "six models from five independent families" |
| 10 | `results.tex:11` | Table 1 caption: "5/5 families" | → "6/6 families" (如果 Falcon3 也 stable) |
| 11 | `results.tex:16–23` | Table 1 (tab:taxonomy) 数据行 | 新增 Falcon3 行 |
| 12 | `results.tex:28` | "$N\!=\!5$ families" | → "$N\!=\!6$" |
| 13 | `results.tex:31` | "In our five-family sample..." 整段 baseline gradient | 加入 Falcon3 数据点，更新 vulnerable band 描述 |
| 14 | `results.tex:34` | "Two of four patterns...are attested in ≥2 independent families" | → 按实际更新 |
| 15 | `results.tex:48` | Table 2 caption: "2/5...4/5...2/5" | → x/6 |
| 16 | `results.tex:51–64` | Table 2 (tab:cross_seed) 数据行 | 新增 Falcon3 行 |
| 17 | `results.tex:67` | "Strict sign consistency holds for 2/5...4/5" | → x/6 |
| 18 | `conclusion.tex:3` | "five-family sample" | → "six-family sample" |
| 19 | `experimental_setup.tex:7` | "four independent model families from four labs" + 模型列表 | 加入 "Falcon3 \citep{...} (7B)" + TII |
| 20 | `experimental_setup.tex:9` | "yields over 50 checkpoints" | 更新 checkpoint 总数 |
| 21 | `appendix.tex:42` | Fig caption "4/5 models" | → "x/6 models" (按 ARC 一致性) |
| 22 | `appendix.tex:346` | Fig 7 caption "four independent families" | → "five independent families" |
| 23 | `appendix.tex:307–327` | Table 14 (classification sensitivity) | 新增 Falcon3 行 |

**图表必须重新生成：**
- `fig_dose_response.pdf` — 加 Falcon3 曲线
- `fig_baseline_vs_effect.pdf` — 加 Falcon3 数据点
- `fig_arc_dose_response.pdf` — 加 Falcon3 曲线（如有 ARC eval）
- Table 1, Table 2, Table 5 (gsm8k_transfer), Table 6 (gsm8k_dose), Table 14 (sensitivity)

---

### 条件更新（取决于 Falcon3 pattern）

**如果 Falcon3 = Benefit:**
- `abstract.tex:1` → "Three patterns (Immune, Benefit, ...) are attested in ≥2 families" — Benefit 从 2 family 变 3 family
- `results.tex:34` → Benefit 的 family-level replication 增强
- `limitations.tex:4` → "Out-of-sample validation covers only the Immune pattern" 仍不变（除非 Benefit 也算 validated）
- Benefit band 扩展到 67.4%，削弱 "vulnerability concentrates in 65–70%" 的说法（因为同区间也出现了 Benefit）

**如果 Falcon3 = Collapse:**
- `abstract.tex:1` → "Collapse...attested in two independent families" — 最大变化，Collapse 不再是 single-family
- `results.tex:34` → 删除 "Collapse...observed in one family...require additional replication"
- `limitations.tex:4` → 可删 "independent-family replication of Collapse...remains open"（Collapse 已 replicated）
- 极大强化论文结论：两个独立 family 在 vulnerable band 都 Collapse

**如果 Falcon3 = Immune:**
- `abstract.tex` → "Immune attested in three families" — 有趣但与 67.4% baseline 矛盾 (vulnerable band 内的 Immune)
- `results.tex:31` → 需修改 "above [76%], immune" 的表述，因为 67.4% 也 Immune
- 削弱 baseline gradient 叙事

**如果 Falcon3 = V-recovery:**
- `abstract.tex:1` → "V-recovery attested in two independent families" — V-recovery 不再是 single-family
- `results.tex:34` → 删除 "V-recovery...observed in one family...require additional replication"
- `limitations.tex:4` → 可删 V-recovery 的 replication caveat
- 在 vulnerable band 内出现第二个 V-recovery，强化 band-specific vulnerability

---

### 不需要更新

- **method.tex** — Algorithm 1 逻辑不变，仅适用范围从 "four families" 隐式扩展
- **IRT calibration 部分** (results.tex §5.5–5.7) — 仍基于 Qwen2.5 within-family，Falcon3 不影响
- **Signal failure 部分** (results.tex §5.6) — Min-K\%++ 分析不涉及 Falcon3（除非另做）
- **DiD memorization test** (results.tex §5.4, Table 3) — 除非对 Falcon3 也做 DiD
- **Domain-level analysis** (results.tex §5.7) — 仍基于 Qwen2.5
- **Prior sensitivity** (appendix) — 仍基于 Qwen2.5

---

### Phase 3: 先 eval d000–d050 不等 d100 的可行性

**Algorithm 1 明确要求 d100。** 分析 `method.tex:63-101`：

```
Line 67: Require a = (a_0, a_5, a_25, a_50, a_100)  ← 显式要求全 5 个 dosage
Line 71: Δ = a_100 - a_0                              ← 顶层分类判据
Line 77: m* < a_100                                    ← V-recovery 检测
Line 85: m* < a_100                                    ← V-recovery 检测
Line 92: g_2 = a_100 - a_25                            ← Benefit subtype
Line 93: ℓ = a_100 - a_50                              ← Benefit subtype
```

**结论：不能在没有 d100 的情况下运行 Algorithm 1，也不能填入 Table 1。**

但 **d000–d050 可以提供有价值的早期信号**：

| d050 观测 | 初步判断 | 置信度 |
|-----------|---------|--------|
| Δ(d050) < −5pp | 极可能 Collapse | 高 — 因为 d100 只会更差 |
| d005/d025 有 V-dip 但 d050 回升 | 可能 V-recovery | 中 — 需 d100 确认 endpoint |
| 单调上升 >2pp | 可能 Benefit | 中 — 需 d100 确认是否 saturate |
| 全程 ±2pp 内 | 可能 Immune | 中 — d100 可能突变 |

**LLaMA-3.1 先例**：LLaMA 仅训练了 d000/d025/d100 三个点（跳了 d005/d050），但仍有 d100。没有跳 d100 的先例。

**建议**：可以先跑 d000–d050 的 eval 获取方向信号（特别是 Falcon3 baseline 在 vulnerable band 内，early signal 很有价值），但论文正式结果必须等 d100 完成。如果 d050 已经明确 Collapse（>5pp decline），d100 的 eval 优先级可以降低（结果可预测）；其他 pattern 则必须等 d100。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 133291,
  "duration_api_ms": 134225,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "26716284-3da5-4fbb-b21b-7ff57f9f6157",
  "total_cost_usd": 0.63436925,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 53675,
    "cache_read_input_tokens": 219045,
    "output_tokens": 7434,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 53675,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3708,
        "cache_read_input_tokens": 64333,
        "cache_creation_input_tokens": 1183,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1183
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3398,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003498,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 7434,
      "cacheReadInputTokens": 219045,
      "cacheCreationInputTokens": 53675,
      "webSearchRequests": 0,
      "costUSD": 0.63087125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "32d16e27-22bb-4602-bf26-0529ffb0a7df"
}
```

</details>

---
