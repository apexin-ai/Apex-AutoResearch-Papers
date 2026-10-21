# paper r30 p0c confound final

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_r30-p0c-confound-final_20260522T155849.log`
- **Structured JSON:** [`a7ef51c1f11fe31177a5.json`](../../sessions/a7/a7ef51c1f11fe31177a5.json)

## Before a recorded user message

49 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__read_repo_file",
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
  "uuid": "89097707-614e-4077-b875-58c0b7eae7c7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1779469200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1bf35ab7-d0bf-4081-9970-34d94f1ac226",
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down into clear tasks:

1. Update experiments.tex in both directories with the precise confound discussion framing
2. Update appendix.tex in both directories with McNemar results and premise-bin table
3. Compile and verify

Let me start by reading the relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "5639780c-3fa2-44f7-bddd-af5b63d580c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpgoGEbGbXqVcL8FCtfqp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16111,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16111
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

_source line 5_

Reading the relevant sections of experiments.tex and appendix.tex in both directories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "aeb14437-1c6c-429d-acbe-de9f7b7b5cd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpgoGEbGbXqVcL8FCtfqp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16111,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16111
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01UhkkA2RuSWVFErNh1BWfR9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 70,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "fb9dedd4-4ec4-43b0-8f7d-d78ee15121f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpgoGEbGbXqVcL8FCtfqp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16111,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16111
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

_source line 7 · 2026-05-22T15:59:05.297Z_

<details><summary>↩ Tool result · `toolu_01UhkkA2RuSWVFErNh1BWfR9`</summary>

```text
70	\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\times$ is the premise-count-matched value relative to random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\sim}55\%$ non-hacking each; Appendix~\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\S\ref{sec:goodhart}) provides the primary diagnostic.}
71	\label{tab:goodhart-landscape}
72	\end{table*}
73	
74	\textbf{Low-dose ISR ($\beta{=}0.1$).}
75	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random ($\text{OR}_{\text{CMH}}{=}2.46$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
76	TS is the canonical Goodhart move: a single premise identical to the conclusion yields $\text{ISR}\geq 0.5$ by construction, directly satisfying the LOO metric (\S\ref{sec:taxonomy-method}).
77	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
78	
79	\textbf{Premise-count confound.}
80	Raw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.
81	After matching for premise count, the apparent $3.2\times$ advantage shrinks to $1.06\times$ (Appendix~\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test
82	The asymmetry operates at two distinct levels: at the \emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\times \to 1.06\times$ after matching; Appendix~\ref{app:premise-count}); at the \emph{compositional} level, the CE-to-TS mode shift ($\text{OR}_{\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.
83	This compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.
84	
85	\textbf{Higher doses and temporal dynamics.}
86	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps as TS escalates (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
87	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
88	
89	\textbf{Bimodal seed-dependence (5-seed extension).}
90	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking, qualitatively different from the 3-seed average of $6\%$.
91	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
92	Seeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\times}2$ vs $2{\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\ref{app:detailed-results}).
93	
94	\subsection{Cross-Domain and Cross-Dataset Evidence}
95	\label{sec:crossdomain}
96	\label{sec:crosslogic}
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
101	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
102	\label{fig:prolog-comparison}
103	\end{figure}
104	
105	\textbf{Prolog: universal Goodhart.}
106	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.
107	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
108	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
109	
110	\textbf{ProofFOL exec-only: cross-dataset replication.}
111	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
112	The dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
113	
114	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
115	ISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.
116	
117	\textbf{Mechanism.}
118	The asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
119	ISR-as-reward inherits the dataset's hacking topology.
120	
121	\paragraph{Cross-scale validation (Qwen3-8B).}
122	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
123	
124	\subsection{Hacking Taxonomy}
125	\label{sec:taxonomy}
126	
127	\begin{figure}[t]
128	\centering
129	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "78d0ec67-f199-4e90-b416-9f042726243f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}",
      "numLines": 60,
      "startLine": 70,
      "totalLines": 160
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01UwEbigT8RLPEwGyWHNb6zp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "offset": 70,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "260d26af-624b-40b7-9622-bd1f6809cc24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpgoGEbGbXqVcL8FCtfqp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16111,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16111
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

_source line 9 · 2026-05-22T15:59:06.229Z_

<details><summary>↩ Tool result · `toolu_01UwEbigT8RLPEwGyWHNb6zp`</summary>

```text
70	\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\times$ is the premise-count-matched value relative to random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\sim}55\%$ non-hacking each; Appendix~\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\S\ref{sec:goodhart}) provides the primary diagnostic.}
71	\label{tab:goodhart-landscape}
72	\end{table*}
73	
74	\textbf{Low-dose ISR ($\beta{=}0.1$).}
75	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random ($\text{OR}_{\text{CMH}}{=}2.46$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
76	TS is the canonical Goodhart move: a single premise identical to the conclusion yields $\text{ISR}\geq 0.5$ by construction, directly satisfying the LOO metric (\S\ref{sec:taxonomy-method}).
77	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
78	
79	\textbf{Premise-count confound.}
80	Raw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.
81	After matching for premise count, the apparent $3.2\times$ advantage shrinks to $1.06\times$ (Appendix~\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test
82	The asymmetry operates at two distinct levels: at the \emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\times \to 1.06\times$ after matching; Appendix~\ref{app:premise-count}); at the \emph{compositional} level, the CE-to-TS mode shift ($\text{OR}_{\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.
83	This compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.
84	
85	\textbf{Higher doses and temporal dynamics.}
86	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps as TS escalates (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
87	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
88	
89	\textbf{Bimodal seed-dependence (5-seed extension).}
90	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking, qualitatively different from the 3-seed average of $6\%$.
91	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
92	Seeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\times}2$ vs $2{\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\ref{app:detailed-results}).
93	
94	\subsection{Cross-Domain and Cross-Dataset Evidence}
95	\label{sec:crossdomain}
96	\label{sec:crosslogic}
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
101	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
102	\label{fig:prolog-comparison}
103	\end{figure}
104	
105	\textbf{Prolog: universal Goodhart.}
106	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.
107	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
108	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
109	
110	\textbf{ProofFOL exec-only: cross-dataset replication.}
111	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
112	The dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
113	
114	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
115	ISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.
116	
117	\textbf{Mechanism.}
118	The asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
119	ISR-as-reward inherits the dataset's hacking topology.
120	
121	\paragraph{Cross-scale validation (Qwen3-8B).}
122	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
123	
124	\subsection{Hacking Taxonomy}
125	\label{sec:taxonomy}
126	
127	\begin{figure}[t]
128	\centering
129	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "e30fed7b-0f61-4b25-bb2b-c85ec817ca57",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
      "content": "\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}",
      "numLines": 60,
      "startLine": 70,
      "totalLines": 160
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_014am2eARzQpUq4kv3e127ep`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 100,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "27ae6b14-bdf2-4237-80d2-e40bb440ef67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpgoGEbGbXqVcL8FCtfqp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16111,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16111
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

_source line 11 · 2026-05-22T15:59:07.198Z_

<details><summary>↩ Tool result · `toolu_014am2eARzQpUq4kv3e127ep`</summary>

```text
100	
101	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
102	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
103	
104	
105	\section{Extended Discussion}
106	\label{app:extended-discussion}
107	
108	\paragraph{What ISR measures---and what it does not.}
109	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
110	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
111	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
112	ISR and downstream task performance are uncorrelated.
113	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
114	
115	Critically, low ISR carries different semantics depending on the training objective.
116	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
117	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
118	ISR values must always be interpreted relative to the optimization objective that produced them.
119	
120	\paragraph{The premise-count confound.}
121	\label{app:premise-count}
122	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
123	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
124	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
125	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
126	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
127	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
128	The $1.06\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.
129	Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
130	
131	\begin{table*}[ht]
132	\centering
133	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
134	\label{tab:bootstrap-ci}
135	\small
136	\begin{tabular}{@{}lcccc@{}}
137	\toprule
138	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
139	\midrule
140	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
141	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
142	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
143	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
144	\midrule
145	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
146	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
147	\midrule
148	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
149	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
150	\bottomrule
151	\end{tabular}
152	\\[2pt]
153	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
154	\end{table*}
155	
156	\paragraph{TS dose-response gradient.}
157	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
158	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "1f71cf36-76f2-4ff8-bb10-9a9abcf481f0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\n\\label{app:premise-count}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\nThe $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n",
      "numLines": 60,
      "startLine": 100,
      "totalLines": 820
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Qjj6Au4uTdemz9TaRdEjS5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 100,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "4c2daef7-c43b-4877-a098-4917760eca62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpgoGEbGbXqVcL8FCtfqp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16111,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16111
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

_source line 13 · 2026-05-22T15:59:07.786Z_

<details><summary>↩ Tool result · `toolu_01Qjj6Au4uTdemz9TaRdEjS5`</summary>

```text
100	
101	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
102	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
103	
104	
105	\section{Extended Discussion}
106	\label{app:extended-discussion}
107	
108	\paragraph{What ISR measures---and what it does not.}
109	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
110	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
111	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
112	ISR and downstream task performance are uncorrelated.
113	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
114	
115	Critically, low ISR carries different semantics depending on the training objective.
116	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
117	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
118	ISR values must always be interpreted relative to the optimization objective that produced them.
119	
120	\paragraph{The premise-count confound.}
121	\label{app:premise-count}
122	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
123	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
124	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
125	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
126	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
127	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
128	The $1.06\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.
129	Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
130	
131	\begin{table*}[ht]
132	\centering
133	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
134	\label{tab:bootstrap-ci}
135	\small
136	\begin{tabular}{@{}lcccc@{}}
137	\toprule
138	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
139	\midrule
140	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
141	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
142	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
143	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
144	\midrule
145	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
146	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
147	\midrule
148	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
149	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
150	\bottomrule
151	\end{tabular}
152	\\[2pt]
153	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
154	\end{table*}
155	
156	\paragraph{TS dose-response gradient.}
157	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
158	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "97ab26d9-9588-4ce2-8fde-8ddd90768ec1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
      "content": "\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\n\\label{app:premise-count}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\nThe $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n",
      "numLines": 60,
      "startLine": 100,
      "totalLines": 820
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the current state of both files. Let me analyze what needs to change:

**experiments.tex (lines 79-83)**: The current "Premise-count confound" paragraph needs updating. Key issues:
1. Line 80-81: Says "$3.2\times$ advantage shrinks to $1.06\times$" - need to change the "214×" mentioned in the task... wait, the task says "$214\times$ raw ISR collapse" but the current text says "$3.2\times$". Let me re-read the task. 

The task specifies "$214\times$ raw ISR collapse is largely explained by premise-count reduction" as the Director's confirmed wording, but the current text uses $3.2\times$ instead. I need to verify which numbers should actually appear here and whether there's a mismatch between what the task is asking for and what's currently in the file. I need to carefully parse what the task is actually asking for. The Director confirmed specific wording with exact numbers: $214\times$ for the raw ISR collapse and $1.06\times$ after premise-count matching, along with the McNemar test statistics. The task seems to want me to revise the existing text in experiments.tex with these precise values and additional details like the modal range robustness claim and the specific premise-bin percentages (19.7% vs 0%).

Let me identify the exact edits needed: replace the scalar Goodhart section with the new framing that emphasizes premise-count reduction as the explanation, update the compositional section to highlight robustness in the 4-6 premise range with those specific percentages, and strengthen the conclusion to make clear that the compositional shift is the primary evidence, not the scalar difference. The compositional shift from CE to TS mode—with an odds ratio of 2.46—persists independently of premise count, since tautological proof structure drives TS classification rather than formalization length. This compositional effect, not the scalar ISR difference, is the real evidence for the Goodhart effect. I need to clarify the distinction between the raw ISR collapse and the matched comparison—the Director specified 214× as the correct raw value, while the 1.06× represents the premise-count-matched comparison that controls for the confound. Now I'm revising the appendix section on the premise-count confound to properly explain this mathematical bias in leave-one-out metrics. The near-unity ratio confirms that ISR's advantage disappears once I account for premise count, and the McNemar test on 100 problem-level matched pairs supports this ($\chi^2=1.0$, $p=0.317$). Mode composition analysis remains unaffected by this confound since tautological proof structure drives the TS classification independent of premise count.

Now I'm constructing the full edits for the experiments section, starting with replacing the premise-count confound paragraph and then inserting the premise-bin breakdown table. The TS mode shift persists across the modal premise-count range where most proofs occur, showing that TS hacking is mechanistically constrained by formalization complexity—models can't ignore premises when problems become harder. This complexity-dependent behavior is a genuine mechanistic finding, not a statistical artifact, and it's the compositional mode shift itself, not the raw ISR scalar difference, that provides the real evidence for the Goodhart effect.

For the appendix edits, I need to replace the n=16 line with the Director's confirmed numbers using McNemar's test statistics, then insert the premise-bin table right after the mode composition analysis paragraph. Let me verify the table reference will work once it's added to the appendix.

Now I'm ready to execute all four edits across both files. I should be careful with the experiments.tex replacement string to ensure it's unique—the paragraph spanning lines 79-83 should work well. The new version is shifting focus from non-hacking rates to the scalar versus compositional comparison, so that detail about p=0.182 is being replaced rather than preserved. I need to replace the confound paragraph with the Director's framing across four files. The key content includes the Scalar Goodhart result, the Compositional Goodhart finding, and the conclusion. The non-hacking rate information will stay in the appendix since the Director's approved wording doesn't include it. Let me update all four files now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "c9158327-9ff1-4410-a88c-27bd7aed987e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8x5dsLqUwCVJvupQDvjpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8980,
      "cache_read_input_tokens": 27952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8980
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

_source line 15_

I have the current state of both files in both directories. The files are identical across the two directories. Now I'll apply all edits in parallel.

**experiments.tex**: Replace lines 79-83 (the "Premise-count confound" paragraph) with the Director-confirmed framing.
**appendix.tex**: Update McNemar line (128) and add premise-bin table after line 129.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "73e9930e-45bc-4035-bab2-a714e51bec71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8x5dsLqUwCVJvupQDvjpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8980,
      "cache_read_input_tokens": 27952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8980
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01A7MiEMp36gkSo1RoaSQzSk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
  "new_string": "\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\nThe TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "3dd87695-7f0c-48f3-a9ab-1b4a24da91b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8x5dsLqUwCVJvupQDvjpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8980,
      "cache_read_input_tokens": 27952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8980
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

_source line 17 · 2026-05-22T16:00:39.252Z_

<details><summary>↩ Tool result · `toolu_01A7MiEMp36gkSo1RoaSQzSk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "38059c86-d8d2-46f4-85a3-fec0d7cc4af6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
    "newString": "\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\nThe TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 77,
        "oldLines": 10,
        "newStart": 77,
        "newLines": 12,
        "lines": [
          " Total conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).",
          " ",
          " \\textbf{Premise-count confound.}",
          "-Raw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.",
          "-After matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test",
          "-The asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.",
          "-This compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
          "+The $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.",
          "+The premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.",
          "+The TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).",
          "+TS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.",
          "+This complexity dependence is a mechanistic insight, not a confound.",
          "+The compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
          " ",
          " \\textbf{Higher doses and temporal dynamics.}",
          " Any genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42"
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01GL5dfXNezVduqNDRBEnKfH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
  "new_string": "\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\nThe TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "30da5bea-886d-44ab-81ef-7920c2f41e6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8x5dsLqUwCVJvupQDvjpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8980,
      "cache_read_input_tokens": 27952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8980
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

_source line 19 · 2026-05-22T16:00:43.952Z_

<details><summary>↩ Tool result · `toolu_01GL5dfXNezVduqNDRBEnKfH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "5750ce5d-a951-4228-8cc3-5091321f47de",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
    "newString": "\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\nThe TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.\nThis compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 77,
        "oldLines": 10,
        "newStart": 77,
        "newLines": 12,
        "lines": [
          " Total conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).",
          " ",
          " \\textbf{Premise-count confound.}",
          "-Raw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.",
          "-After matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test",
          "-The asymmetry operates at two distinct levels: at the \\emph{scalar} level, the apparent ISR advantage is a premise-count artifact ($3.2\\times \\to 1.06\\times$ after matching; Appendix~\\ref{app:premise-count}); at the \\emph{compositional} level, the CE-to-TS mode shift ($\\text{OR}_{\\text{CMH}}{=}2.46$) is independent of premise count, since TS classification depends on tautological proof structure, not formalization length.",
          "-This compositional shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
          "+The $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.",
          "+The premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.",
          "+The TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).",
          "+TS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.",
          "+This complexity dependence is a mechanistic insight, not a confound.",
          "+The compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.",
          " ",
          " \\textbf{Higher doses and temporal dynamics.}",
          " Any genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42"
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01BP3W3LnUYHWbvzHUDgnvyf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "old_string": "The $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.",
  "new_string": "The matched comparison yields $1.06\\times$ (McNemar's test: $\\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs), confirming that the scalar ISR advantage is not statistically significant.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\n$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\\n         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\\n\\midrule\n4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\\n         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\\n\\midrule\n$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\\n         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}\n\\label{tab:premise-bin-modes}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "bf54c7fa-173b-4cbc-8536-80f950ad40a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8x5dsLqUwCVJvupQDvjpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8980,
      "cache_read_input_tokens": 27952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8980
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

_source line 21 · 2026-05-22T16:00:53.433Z_

<details><summary>↩ Tool result · `toolu_01BP3W3LnUYHWbvzHUDgnvyf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "1763819d-99f5-48ca-9ca9-bb89c0fc3360",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "oldString": "The $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.",
    "newString": "The matched comparison yields $1.06\\times$ (McNemar's test: $\\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs), confirming that the scalar ISR advantage is not statistically significant.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\n$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\\n         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\\n\\midrule\n4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\\n         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\\n\\midrule\n$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\\n         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}\n\\label{tab:premise-bin-modes}\n\\end{table}",
    "originalFile": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{SFT convergence.}\nSFT training converged across all three seeds: final-step loss ${\\leq}0.04$ and token accuracy ${>}99\\%$ after ${\\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\n\\label{app:premise-count}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\nThe $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcr}\n\\toprule\n\\textbf{Mode} & \\textbf{Validated $N$} & \\textbf{Precision} \\\\\n\\midrule\nCE (Concl.\\ Embedding) & 80$^\\dagger$ & 1.00 \\\\\nTS (Tautological) & 7 & 1.00 \\\\\nPG (Premise-Subset) & 20 & 1.00 \\\\\nContradiction & 20 & 1.00 \\\\\nGenuine & 25 & 1.00 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{152} & \\textbf{1.00} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\\dagger$Includes 50 randomly sampled CE$\\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}\n\\label{tab:classifier-precision}\n\\end{table}\n\nThe TS\\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\\geq}91\\%$ ($149/163$) under ISR $\\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.\n\n\\subsection{PG --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (71--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\nThe premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\FloatBarrier\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) achieves $\\text{PR}{=}16\\%$ ($n{=}100$) after correcting the generation-termination issue.\nHowever, the model produces Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.\nSubsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\\text{PR}{=}15.0{\\pm}1.0\\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\\pm}0.9\\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\\sigma_{\\text{PR}}{=}1$\\,pp).\nThis contrasts sharply with Qwen3-4B, where GRPO reaches $93\\%$ PR but collapses to $8\\%$ genuine with high cross-seed variance.\nThe result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \\emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.\n\n\\subsection{Seed-Dependent Convergence in Exec-Only GRPO}\n\\label{app:seed-convergence}\n\nNot all exec-only seeds converge.\nOf 6 seeds tested (s42--s46, s52), we observe three regimes: \\emph{converging with degeneration} (s42: $\\text{PR}{=}93\\%$, genuine${=}7.5\\%$; s44: $\\text{PR}{=}96\\%$, genuine${=}0\\%$; s46: $\\text{PR}{=}93\\%$ at 500 steps), \\emph{slow convergence with degeneration} (s43: $\\text{PR}{=}14\\%$ but $100\\%$ hacking at 500 steps), and \\emph{non-converging} (s45: $\\text{PR}{=}15\\%$, genuine${=}86.7\\%$; s52: $\\text{PR}{=}14\\%$, genuine${=}85.7\\%$).\nNon-converging seeds retain high genuine rates (85--87\\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.\nExtended training to 1000 steps for s45 confirms persistent non-convergence ($\\text{PR}{=}15\\%$, $\\text{ISR}^*{=}0.592$, genuine${=}86.7\\%$, $n{=}15$ proved); the model neither improves nor degenerates.\n\nThis parallels the LLaMA-3.2-3B finding (Appendix~\\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.\nBoth cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.\n\n\\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}\n\\label{app:n2-sensitivity}\n\nSeed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\\S\\ref{app:setup}).\nTo assess whether this non-standard protocol affects qualitative conclusions, Table~\\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{PR (\\%)} & \\textbf{ISR$^*$} & \\textbf{N-H (\\%)} \\\\\n\\midrule\nExec-only 500-step & $95.5 \\pm 3.5$ & $0.357 \\pm 0.318$ & $3.8 \\pm 5.3$ \\\\\nExec-only 1000-step & $98.0 \\pm 2.8$ & $0.003 \\pm 0.001$ & $0.0 \\pm 0.0$ \\\\\nISR $\\beta{=}0.1$ 500-step & $85.0 \\pm 5.7$ & $0.659 \\pm 0.344$ & $8.7 \\pm 12.2$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\\leq}7.5\\%$ non-hacking; ISR $\\beta{=}0.1$ shifts composition toward TS.}\n\\label{tab:n2-sensitivity}\n\\end{table}\n\nExcluding seed~43, exec-only converges to ${\\leq}7.5\\%$ non-hacking at 500 steps and $0\\%$ at 1000 steps.\nUnder ISR $\\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\\%$, s44: $100\\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.\nThe large per-seed ISR$^*$ variance ($0.357 \\pm 0.318$) reflects different degeneration modes (CE in s42 vs.\\ TS in s44), not data quality issues.\n\n\\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}\n\\label{app:8b-results}\n\nTo test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).\nTable~\\ref{tab:8b-combined} summarizes configuration differences and results.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} \\\\\n\\midrule\nRollouts ($K$) & 4 & 8 \\\\\nBatch size & 4 & 1 \\\\\nGradient accum. & 2 & 16 \\\\\nEffective batch & 8 & 16 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{PR\\%} & \\textbf{Genuine\\%} & \\textbf{Converged?} & \\textbf{Gradient} \\\\\n\\midrule\n4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\\\\n8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\\\\n8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-scale: Qwen3-4B vs.\\ Qwen3-8B. \\textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \\textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}\n\\label{tab:8b-combined}\n\\end{table}\n\nWe first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\\text{PR}{=}15.5\\%$, cold-start stagnation).\nIncreasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\\text{PR}{=}14\\%$ ($n{=}14$ proved), $\\text{ISR}^*{=}0.573$, genuine${=}92.9\\%$ (13/14), with a single CE sample.\nCosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.\n\nThis result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.\nTogether, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \\S\\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.\n",
    "structuredPatch": [
      {
        "oldStart": 125,
        "oldLines": 9,
        "newStart": 125,
        "newLines": 30,
        "lines": [
          " Premise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).",
          " This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.",
          " We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.",
          "-The $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.",
          "+The matched comparison yields $1.06\\times$ (McNemar's test: $\\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs), confirming that the scalar ISR advantage is not statistically significant.",
          " Mode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.",
          " ",
          "+\\begin{table}[h]",
          "+\\centering",
          "+\\small",
          "+\\begin{tabular}{@{}llrrrr@{}}",
          "+\\toprule",
          "+\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\",
          "+\\midrule",
          "+$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\",
          "+         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\",
          "+\\midrule",
          "+4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\",
          "+         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\",
          "+\\midrule",
          "+$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\",
          "+         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}",
          "+\\label{tab:premise-bin-modes}",
          "+\\end{table}",
          "+",
          " \\begin{table*}[ht]",
          " \\centering",
          " \\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}"
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01KFv9EPNMFcHBXMj4Hi5FL3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "old_string": "The $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.",
  "new_string": "The matched comparison yields $1.06\\times$ (McNemar's test: $\\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs), confirming that the scalar ISR advantage is not statistically significant.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\n$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\\n         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\\n\\midrule\n4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\\n         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\\n\\midrule\n$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\\n         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}\n\\label{tab:premise-bin-modes}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "cf6e6a6c-7f93-4d14-8b9f-343fa27109ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8x5dsLqUwCVJvupQDvjpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8980,
      "cache_read_input_tokens": 27952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8980
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

_source line 23 · 2026-05-22T16:00:59.012Z_

<details><summary>↩ Tool result · `toolu_01KFv9EPNMFcHBXMj4Hi5FL3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "85e4e56d-ccf5-46f5-b0b4-92b534012de2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
    "oldString": "The $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.",
    "newString": "The matched comparison yields $1.06\\times$ (McNemar's test: $\\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs), confirming that the scalar ISR advantage is not statistically significant.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\n$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\\n         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\\n\\midrule\n4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\\n         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\\n\\midrule\n$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\\n         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}\n\\label{tab:premise-bin-modes}\n\\end{table}",
    "originalFile": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{SFT convergence.}\nSFT training converged across all three seeds: final-step loss ${\\leq}0.04$ and token accuracy ${>}99\\%$ after ${\\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\n\\label{app:premise-count}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\nThe $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcr}\n\\toprule\n\\textbf{Mode} & \\textbf{Validated $N$} & \\textbf{Precision} \\\\\n\\midrule\nCE (Concl.\\ Embedding) & 80$^\\dagger$ & 1.00 \\\\\nTS (Tautological) & 7 & 1.00 \\\\\nPG (Premise-Subset) & 20 & 1.00 \\\\\nContradiction & 20 & 1.00 \\\\\nGenuine & 25 & 1.00 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{152} & \\textbf{1.00} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\\dagger$Includes 50 randomly sampled CE$\\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}\n\\label{tab:classifier-precision}\n\\end{table}\n\nThe TS\\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\\geq}91\\%$ ($149/163$) under ISR $\\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.\n\n\\subsection{PG --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (71--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\nThe premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\FloatBarrier\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) achieves $\\text{PR}{=}16\\%$ ($n{=}100$) after correcting the generation-termination issue.\nHowever, the model produces Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.\nSubsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\\text{PR}{=}15.0{\\pm}1.0\\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\\pm}0.9\\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\\sigma_{\\text{PR}}{=}1$\\,pp).\nThis contrasts sharply with Qwen3-4B, where GRPO reaches $93\\%$ PR but collapses to $8\\%$ genuine with high cross-seed variance.\nThe result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \\emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.\n\n\\subsection{Seed-Dependent Convergence in Exec-Only GRPO}\n\\label{app:seed-convergence}\n\nNot all exec-only seeds converge.\nOf 6 seeds tested (s42--s46, s52), we observe three regimes: \\emph{converging with degeneration} (s42: $\\text{PR}{=}93\\%$, genuine${=}7.5\\%$; s44: $\\text{PR}{=}96\\%$, genuine${=}0\\%$; s46: $\\text{PR}{=}93\\%$ at 500 steps), \\emph{slow convergence with degeneration} (s43: $\\text{PR}{=}14\\%$ but $100\\%$ hacking at 500 steps), and \\emph{non-converging} (s45: $\\text{PR}{=}15\\%$, genuine${=}86.7\\%$; s52: $\\text{PR}{=}14\\%$, genuine${=}85.7\\%$).\nNon-converging seeds retain high genuine rates (85--87\\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.\nExtended training to 1000 steps for s45 confirms persistent non-convergence ($\\text{PR}{=}15\\%$, $\\text{ISR}^*{=}0.592$, genuine${=}86.7\\%$, $n{=}15$ proved); the model neither improves nor degenerates.\n\nThis parallels the LLaMA-3.2-3B finding (Appendix~\\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.\nBoth cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.\n\n\\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}\n\\label{app:n2-sensitivity}\n\nSeed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\\S\\ref{app:setup}).\nTo assess whether this non-standard protocol affects qualitative conclusions, Table~\\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{PR (\\%)} & \\textbf{ISR$^*$} & \\textbf{N-H (\\%)} \\\\\n\\midrule\nExec-only 500-step & $95.5 \\pm 3.5$ & $0.357 \\pm 0.318$ & $3.8 \\pm 5.3$ \\\\\nExec-only 1000-step & $98.0 \\pm 2.8$ & $0.003 \\pm 0.001$ & $0.0 \\pm 0.0$ \\\\\nISR $\\beta{=}0.1$ 500-step & $85.0 \\pm 5.7$ & $0.659 \\pm 0.344$ & $8.7 \\pm 12.2$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\\leq}7.5\\%$ non-hacking; ISR $\\beta{=}0.1$ shifts composition toward TS.}\n\\label{tab:n2-sensitivity}\n\\end{table}\n\nExcluding seed~43, exec-only converges to ${\\leq}7.5\\%$ non-hacking at 500 steps and $0\\%$ at 1000 steps.\nUnder ISR $\\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\\%$, s44: $100\\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.\nThe large per-seed ISR$^*$ variance ($0.357 \\pm 0.318$) reflects different degeneration modes (CE in s42 vs.\\ TS in s44), not data quality issues.\n\n\\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}\n\\label{app:8b-results}\n\nTo test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).\nTable~\\ref{tab:8b-combined} summarizes configuration differences and results.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} \\\\\n\\midrule\nRollouts ($K$) & 4 & 8 \\\\\nBatch size & 4 & 1 \\\\\nGradient accum. & 2 & 16 \\\\\nEffective batch & 8 & 16 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{PR\\%} & \\textbf{Genuine\\%} & \\textbf{Converged?} & \\textbf{Gradient} \\\\\n\\midrule\n4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\\\\n8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\\\\n8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-scale: Qwen3-4B vs.\\ Qwen3-8B. \\textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \\textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}\n\\label{tab:8b-combined}\n\\end{table}\n\nWe first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\\text{PR}{=}15.5\\%$, cold-start stagnation).\nIncreasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\\text{PR}{=}14\\%$ ($n{=}14$ proved), $\\text{ISR}^*{=}0.573$, genuine${=}92.9\\%$ (13/14), with a single CE sample.\nCosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.\n\nThis result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.\nTogether, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \\S\\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.\n",
    "structuredPatch": [
      {
        "oldStart": 125,
        "oldLines": 9,
        "newStart": 125,
        "newLines": 30,
        "lines": [
          " Premise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).",
          " This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.",
          " We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.",
          "-The $1.06\\times$ matched comparison is based on $n{=}16$ paired samples; the near-unity ratio indicates that the scalar ISR advantage is negligible after controlling for premise count.",
          "+The matched comparison yields $1.06\\times$ (McNemar's test: $\\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs), confirming that the scalar ISR advantage is not statistically significant.",
          " Mode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.",
          " ",
          "+\\begin{table}[h]",
          "+\\centering",
          "+\\small",
          "+\\begin{tabular}{@{}llrrrr@{}}",
          "+\\toprule",
          "+\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\",
          "+\\midrule",
          "+$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\",
          "+         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\",
          "+\\midrule",
          "+4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\",
          "+         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\",
          "+\\midrule",
          "+$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\",
          "+         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}",
          "+\\label{tab:premise-bin-modes}",
          "+\\end{table}",
          "+",
          " \\begin{table*}[ht]",
          " \\centering",
          " \\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}"
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
All 4 edits succeeded. Now let me also check if the table caption in experiments.tex (around line 70) references "$3.2\times$" that should be updated to "$214\times$". Let me re-read line 70.

Looking at line 70 again: "ISR$^*$ raw mean inflated by TS gaming; $1.06\times$ is the premise-count-matched value relative to random"

It doesn't mention $3.2\times$ or $214\times$ in the caption. Good.


Now I should search through the rest of the paper to see if there are any other instances of "$3.2\times$" that need to be changed to "$214\times$".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "0ac386b1-d2e7-4b31-a5d0-b9d88b8cf979",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqoCHJXV145s1D85mzXVHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7141,
      "cache_read_input_tokens": 36932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7141
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

All 4 edits applied. Let me check for any remaining references to the old `$3.2\times$` that should be updated to `$214\times$`, and then compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "8c14f8b1-7659-4a24-b313-a2dac7a44a2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqoCHJXV145s1D85mzXVHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7141,
      "cache_read_input_tokens": 36932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7141
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

<details open><summary>🔧 Tool call — Grep · `toolu_01WnjvHQ4R84avTYbes1rKwM`</summary>

```json
{
  "pattern": "3\\.2\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
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
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "751beb5e-6514-4e64-9abb-99adf2db3822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqoCHJXV145s1D85mzXVHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7141,
      "cache_read_input_tokens": 36932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7141
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

_source line 27 · 2026-05-22T16:01:07.887Z_

<details><summary>↩ Tool result · `toolu_01WnjvHQ4R84avTYbes1rKwM`</summary>

```text
artifacts/submission/experiments.tex:77:The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
artifacts/submission/experiments.tex:82:The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
artifacts/submission_package/experiments.tex:77:The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
artifacts/submission_package/experiments.tex:82:The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
artifacts/dream_reports/dream_20260514T092544/median/paper.tex:255:At $\beta{=}0.1$, ISR reward achieves ISR$=$0.337 vs.\ random control ISR$=$0.104---a $3.2\times$ improvement with comparable prove rate (0.81 vs.\ 0.79).
paper/experiments.tex:44:ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$ after controlling for premise count.
docs/paper/experiments.tex:44:ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$ after controlling for premise count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "f48d1dc5-1415-409b-bc14-83b5243efb77",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/submission/experiments.tex:77:The one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nartifacts/submission/experiments.tex:82:The raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\nartifacts/submission_package/experiments.tex:77:The one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nartifacts/submission_package/experiments.tex:82:The raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\nartifacts/dream_reports/dream_20260514T092544/median/paper.tex:255:At $\\beta{=}0.1$, ISR reward achieves ISR$=$0.337 vs.\\ random control ISR$=$0.104---a $3.2\\times$ improvement with comparable prove rate (0.81 vs.\\ 0.79).\npaper/experiments.tex:44:ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\ndocs/paper/experiments.tex:44:ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
    "numLines": 7
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01LuZVY3LngBv2qQkewKyYA8`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "5e543a5c-cd51-48bf-a1bb-6d8db4151429",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqoCHJXV145s1D85mzXVHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7141,
      "cache_read_input_tokens": 36932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7141
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

_source line 29 · 2026-05-22T16:01:10.303Z_

<details><summary>↩ Tool result · `toolu_01LuZVY3LngBv2qQkewKyYA8`</summary>

```text
mti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (24 pages, 601473 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "24bf12ed-f637-4f2b-baea-baf3ff275eb2",
  "tool_use_result": {
    "stdout": "mti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (24 pages, 601473 bytes).\nTranscript written on main.log.",
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

<details><summary>Logged reasoning block</summary>

```text
There are remaining references to `$3.2\times$` in the main paper files at:
- `paper/experiments.tex:44` — "the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$ after controlling for premise count"
- `docs/paper/experiments.tex:44` — same

These should be updated to match the new $214\times$ number. Let me read those lines to get the exact context.

The artifacts/ and dream_reports/ files are old versions and shouldn't be touched.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "a53f6fd6-1a28-49e1-a5b7-8ad3bbf71134",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6vMz8ncTbhiziDW5up2Df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 44073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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

_source line 31_

Found remaining `$3.2\times$` references in experiments.tex line 44. Need to update those too.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "69fdf0ee-afbf-4f13-8619-8f4e18c88439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6vMz8ncTbhiziDW5up2Df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 44073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01HiNeD4EA7jCgpgmAoFgG88`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 42,
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
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "4b090f71-d40c-4e24-a3d3-85b43d20e542",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6vMz8ncTbhiziDW5up2Df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 44073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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

_source line 33 · 2026-05-22T16:01:16.328Z_

<details><summary>↩ Tool result · `toolu_01HiNeD4EA7jCgpgmAoFgG88`</summary>

```text
42	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
43	The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
44	ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$ after controlling for premise count.
45	
46	\paragraph{Multiplicative coupling.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "76d1862e-0c26-45a5-8f9e-735cafd096e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "We reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}",
      "numLines": 5,
      "startLine": 42,
      "totalLines": 162
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01Me1BpD82trxYQVgDaUM53s`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
  "new_string": "the apparent $214\\times$ raw ISR advantage collapses to $1.06\\times$ after controlling for premise count."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "eb3306ea-03be-42c9-95db-96b9e5994ef6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUZ7TGbpgRna6vgn7jwBoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 45277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 35 · 2026-05-22T16:01:19.884Z_

<details><summary>↩ Tool result · `toolu_01Me1BpD82trxYQVgDaUM53s`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "d939f366-1133-4793-b3b4-52335ad74d30",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
    "newString": "the apparent $214\\times$ raw ISR advantage collapses to $1.06\\times$ after controlling for premise count.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\nThe TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " We reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).",
          " The result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.",
          "-ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
          "+ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent $214\\times$ raw ISR advantage collapses to $1.06\\times$ after controlling for premise count.",
          " ",
          " \\paragraph{Multiplicative coupling.}",
          " The multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics."
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01Te31fW78pzNbETJ74Jyamy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
  "new_string": "the apparent $214\\times$ raw ISR advantage collapses to $1.06\\times$ after controlling for premise count."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "5a72ebb9-48f1-4fd3-8e80-a344c83423a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUZ7TGbpgRna6vgn7jwBoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 45277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 37 · 2026-05-22T16:01:20.938Z_

<details><summary>↩ Tool result · `toolu_01Te31fW78pzNbETJ74Jyamy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "ac608b64-50df-43b0-b728-d69747308374",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
    "newString": "the apparent $214\\times$ raw ISR advantage collapses to $1.06\\times$ after controlling for premise count.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\nThe TS mode shift, however, is robust in the modal premise-count range (4--6 premises, where most proved samples fall): $19.7\\%$ TS under ISR versus $0\\%$ under random reward (Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " We reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).",
          " The result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.",
          "-ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.",
          "+ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent $214\\times$ raw ISR advantage collapses to $1.06\\times$ after controlling for premise count.",
          " ",
          " \\paragraph{Multiplicative coupling.}",
          " The multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics."
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

_source line 38_

Now compiling with full bibtex cycle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "0a943199-ea1b-4360-b16b-2263e93eb759",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XUNYmo1rp6B957jWaitn9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 45773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01HCiw7h8wrAcUcQrqLyQfqC`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "description": "Full pdflatex+bibtex compile cycle",
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
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "bcefeaf2-e432-4821-b7d2-b064ca67fa7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XUNYmo1rp6B957jWaitn9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 45773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b724amq67",
  "tool_use_id": "toolu_01HCiw7h8wrAcUcQrqLyQfqC",
  "description": "Full pdflatex+bibtex compile cycle",
  "task_type": "local_bash",
  "uuid": "cf121f18-ff09-4514-b95f-b72e67e5aaaf",
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4"
}
```

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b724amq67",
  "tool_use_id": "toolu_01HCiw7h8wrAcUcQrqLyQfqC",
  "status": "completed",
  "output_file": "",
  "summary": "Full pdflatex+bibtex compile cycle",
  "uuid": "4db3a7e4-ce6e-4231-abca-3ca05dc6f425",
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4"
}
```

---

### Tool result

_source line 42 · 2026-05-22T16:01:34.482Z_

<details><summary>↩ Tool result · `toolu_01HCiw7h8wrAcUcQrqLyQfqC`</summary>

```text
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (24 pages, 601051 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "e840e0de-f9cd-47ba-b6a7-bd7f83a82d79",
  "tool_use_result": {
    "stdout": "fonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (24 pages, 601051 bytes).\nTranscript written on main.log.",
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_018SMJkuPG6Y67g5yxYAzmfF`</summary>

```json
{
  "command": "grep -ci \"undefined\" main.log && grep \"Warning.*Citation\" main.log | head -10 && grep -ci \"multiply\" main.log && pdfinfo main.pdf | grep Pages",
  "description": "Check compile warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "021e92c0-12ec-41ea-b500-3ee8e0af0e6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XZy5FEJsLBfHi16JvKAhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 46293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 253
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

_source line 44 · 2026-05-22T16:01:41.770Z_

<details><summary>↩ Tool result · `toolu_018SMJkuPG6Y67g5yxYAzmfF`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "85a56047-cb05-4352-8789-0c587abbf7c6",
  "tool_use_result": {
    "stdout": "0",
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

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
The grep output shows:
- 0 undefined references
- No citation warnings (empty output)
- 0 multiply-defined labels (wait, it seems the output was 0 but there was nothing after the first grep. Let me re-check.)

Actually, looking at the output: "0\n\n" suggests:
- `grep -ci "undefined" main.log` → 0 (no undefined references)
- `grep "Warning.*Citation" main.log | head -10` → empty (no citation warnings)
- `grep -ci "multiply" main.log` → not shown (maybe 0 too or a different issue)


- `pdfinfo main.pdf | grep Pages` → also not shown

I should run these checks individually to get clearer results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "a8c69070-96c5-488a-84fc-09934f25c40e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWRukFsfsaNeQtnayG9Hnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 46546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

<details open><summary>🔧 Tool call — Bash · `toolu_01FE53QdzL2hWFhdq7ik5Kot`</summary>

```json
{
  "command": "echo \"=== Undefined ===\" && grep -ci \"undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.log ; echo \"=== Multiply ===\" && grep -ci \"multiply\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.log ; echo \"=== Pages ===\" && pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf | grep Pages",
  "description": "Check compile results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "dd2bcfe9-d314-4ddf-80b7-d9c9f5a3abd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWRukFsfsaNeQtnayG9Hnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 46546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 47 · 2026-05-22T16:01:49.953Z_

<details><summary>↩ Tool result · `toolu_01FE53QdzL2hWFhdq7ik5Kot`</summary>

```text
=== Undefined ===
0
=== Multiply ===
0
=== Pages ===
Pages:           24
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "761491ec-dde5-429a-b698-d76e1f78075c",
  "tool_use_result": {
    "stdout": "=== Undefined ===\n0\n=== Multiply ===\n0\n=== Pages ===\nPages:           24",
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

_source line 48_

Compile clean: 0 undefined refs, 0 multiply-defined labels, 24 pages.

---

**修改汇总**:

### 任务 1: experiments.tex (paper/ + docs/paper/)

**L44** — `$3.2\times$ → $214\times$ raw`:
- Before: `the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$`
- After: `the apparent $214\times$ raw ISR advantage collapses to $1.06\times$`

**L79-85** — Premise-count confound paragraph 全量替换:
- Before: 用 `$3.2\times$` 和 "independent of premise count" 的两层框架（5行）
- After: Director 确认的精确措辞——Scalar Goodhart（`$214\times$ → $1.06\times$`, McNemar `p=0.317`, `n=100`）+ Compositional Goodhart（"robust in modal premise-count range 4–6", `19.7%` vs `0%` TS, complexity dependence is mechanistic）（7行）

### 任务 2: appendix.tex (paper/ + docs/paper/)

**L128** — McNemar 详情更新:
- Before: `$n{=}16$ paired samples; the near-unity ratio indicates...negligible`
- After: `McNemar's test: $\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs...not statistically significant`

**L130+** — 新增 `tab:premise-bin-modes` 表格（6行数据，3 premise bins × 2 conditions）

### 编译
0 undefined, 0 multiply, 24 pages, 无 citation warnings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "uuid": "a7daa030-d4df-435c-9d07-41c6139586f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011T9RMuR2iuYHMP3a4Sy4tH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 46776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
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

### Task result

_source line 49_

Compile clean: 0 undefined refs, 0 multiply-defined labels, 24 pages.

---

**修改汇总**:

### 任务 1: experiments.tex (paper/ + docs/paper/)

**L44** — `$3.2\times$ → $214\times$ raw`:
- Before: `the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$`
- After: `the apparent $214\times$ raw ISR advantage collapses to $1.06\times$`

**L79-85** — Premise-count confound paragraph 全量替换:
- Before: 用 `$3.2\times$` 和 "independent of premise count" 的两层框架（5行）
- After: Director 确认的精确措辞——Scalar Goodhart（`$214\times$ → $1.06\times$`, McNemar `p=0.317`, `n=100`）+ Compositional Goodhart（"robust in modal premise-count range 4–6", `19.7%` vs `0%` TS, complexity dependence is mechanistic）（7行）

### 任务 2: appendix.tex (paper/ + docs/paper/)

**L128** — McNemar 详情更新:
- Before: `$n{=}16$ paired samples; the near-unity ratio indicates...negligible`
- After: `McNemar's test: $\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs...not statistically significant`

**L130+** — 新增 `tab:premise-bin-modes` 表格（6行数据，3 premise bins × 2 conditions）

### 编译
0 undefined, 0 multiply, 24 pages, 无 citation warnings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 185025,
  "duration_api_ms": 181720,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "7546f32c-2de6-478c-99a6-1b48b690e1c4",
  "total_cost_usd": 0.6409050000000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 35382,
    "cache_read_input_tokens": 351463,
    "output_tokens": 9592,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35382,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 467,
        "cache_read_input_tokens": 46776,
        "cache_creation_input_tokens": 447,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 447
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4091,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.004181,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 9592,
      "cacheReadInputTokens": 351463,
      "cacheCreationInputTokens": 35382,
      "webSearchRequests": 0,
      "costUSD": 0.6367240000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ccaec155-dbcf-44cc-8077-7a30bfd6d6fe"
}
```

</details>

---
