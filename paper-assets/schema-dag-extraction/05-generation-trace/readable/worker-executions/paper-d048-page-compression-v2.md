# paper d048 page compression v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_paper_d048_page_compression_v2_20260516T151046.log`
- **Structured JSON:** [`299da42f86202270a04e.json`](../../sessions/29/299da42f86202270a04e.json)

## Before a recorded user message

78 recorded events

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "bb7b6f89-980d-495e-9c7e-7c20cb218d74",
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
  "uuid": "8c242b3b-bc49-4904-8e46-1e0d17cb2dda",
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant tex files to understand the current state of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "2b634fbc-ca1b-439b-80f9-874863963d9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELXNrX2xYRyG41BP5c9RRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11736
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

_source line 5_

Let me read the relevant files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "b038619c-96b7-4f7a-a120-70e647008c38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELXNrX2xYRyG41BP5c9RRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11736
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01FfJLEjCuNYz2GfWoUhPJyY`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "c4072b34-1cce-423f-b1c0-77c08d5ca744",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELXNrX2xYRyG41BP5c9RRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11736
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

_source line 7 · 2026-05-16T15:10:59.811Z_

<details><summary>↩ Tool result · `toolu_01FfJLEjCuNYz2GfWoUhPJyY`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1 extreme-batch gap; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \approx 7\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\sim}3\times$ amplification confirmed by Monte Carlo simulation (Appendix~\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\% of accuracy variance, sufficient for pre-hoc schema screening.
9	
10	\paragraph{Schema design implications.}
11	Since typical random batches differ by only ${\approx}\,2.2$\,pp (\S\ref{sec:practical_magnitude}), the practical impact depends on schema composition.
12	Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:
13	(i)~\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;
14	(ii)~\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;
15	(iii)~\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\S\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.
16	We deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.
17	
18	\paragraph{Cross-domain connections.}
19	Schema complexity effects may parallel findings in schema-guided dialogue systems (\S2; see Appendix~\ref{app:cross-domain} for discussion).
20	
21	\paragraph{Model scale and confusability sensitivity.}
22	Preliminary evidence from two model sizes (32B vs.\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.
23	
24	\paragraph{Future directions.}
25	Three directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\S\ref{sec:sdgd}).
26	
27	\section{Conclusion}
28	\label{sec:conclusion}
29	
30	We presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "c0cd543b-a370-40f7-afda-e9fd3a587a3e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01U6cCFM19B7G59J4nvCzLpN`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "0764a242-60da-4310-8d33-b5c1c9ce91cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELXNrX2xYRyG41BP5c9RRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11736,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11736
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

_source line 9 · 2026-05-16T15:11:00.190Z_

<details><summary>↩ Tool result · `toolu_01U6cCFM19B7G59J4nvCzLpN`</summary>

```text
docs/paper/conclusion.tex
docs/paper/prompt_appendix.tex
docs/paper/related_work.tex
docs/paper/sdgd_negative.tex
docs/paper/results.tex
docs/paper/experimental_setup.tex
docs/paper/checklist.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/main.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "d8b65a95-812e-49ba-a2e3-bf21bfc0c239",
  "tool_use_result": {
    "filenames": [
      "docs/paper/conclusion.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/related_work.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/results.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/checklist.tex",
      "docs/paper/introduction.tex",
      "docs/paper/abstract.tex",
      "docs/paper/main.tex",
      "docs/paper/discussion.tex"
    ],
    "durationMs": 7,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_012evR7QpsXtrWJqW8NTcaAq`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "0d4de2c6-4a89-4deb-ac3f-f643e0776630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KcAjos4X74A3135RBQct3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 23577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1555
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

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_016bYiSYnry3HvfvhKHbabQc`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "d4167742-f836-407b-bc70-534ccfe7f57c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KcAjos4X74A3135RBQct3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 23577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1555
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

_source line 12 · 2026-05-16T15:11:03.906Z_

<details><summary>↩ Tool result · `toolu_016bYiSYnry3HvfvhKHbabQc`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "47d702f0-7c33-4c7b-acc2-f8515d2b8a39",
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

### Tool result

_source line 13 · 2026-05-16T15:11:04.262Z_

<details><summary>↩ Tool result · `toolu_012evR7QpsXtrWJqW8NTcaAq`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "8c2eb8e0-e9b6-4e7b-846b-3663440f858e",
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

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the sdgd_negative.tex file (which seems to be the §5 applications file) and the conclusion.tex file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "afec11e4-780a-4597-a660-9e79cd87a10e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSubqeLFrbvrXBZbwoSR2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3777,
      "cache_creation_input_tokens": 9868,
      "cache_read_input_tokens": 25132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9868
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

Now let me check the sdgd_negative.tex file (§5) and compile to see the current page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "5152cd74-a000-4f6f-8381-c6956eb9639d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSubqeLFrbvrXBZbwoSR2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3777,
      "cache_creation_input_tokens": 9868,
      "cache_read_input_tokens": 25132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9868
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

<details open><summary>🔧 Tool call — Read · `toolu_01MpQi9FAKuaYbKYtxYdjgwR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "f511f74d-eb82-4a53-be3b-2251fa88307f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSubqeLFrbvrXBZbwoSR2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3777,
      "cache_creation_input_tokens": 9868,
      "cache_read_input_tokens": 25132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9868
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

<details open><summary>🔧 Tool call — Bash · `toolu_01LzALJo59XYBXPq7BXF6HX8`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper to check current page count",
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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "b74f70d3-d623-4d2f-b027-df6288731ce9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSubqeLFrbvrXBZbwoSR2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3777,
      "cache_creation_input_tokens": 9868,
      "cache_read_input_tokens": 25132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9868
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

_source line 18 · 2026-05-16T15:11:12.815Z_

<details><summary>↩ Tool result · `toolu_01MpQi9FAKuaYbKYtxYdjgwR`</summary>

```text
1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.
10	
11	Quantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\to$ 0.314 for sdgd\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\to$ 0.251 (sdgd\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\,=\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.
12	
13	\paragraph{Confidence gating does not resolve merge amplification.}
14	Confidence-based gating (retaining only predictions above threshold) trades recall for precision but does not recover net F1 (0.251$\to$0.241), confirming that merge artifacts are systemic rather than confined to low-confidence predictions (Appendix~\ref{sec:appendix_sdgd}).
15	
16	\paragraph{Why NER fails but RE does not.}
17	Merge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.
18	
19	\paragraph{Oracle routing as performance ceiling.}
20	Oracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\,pp (Table~\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.
21	
22	However, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\,pp for random batching, +29.8\,pp for graph coloring), the \emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\,pp, $p \approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\resizebox{\columnwidth}{!}{%
28	\begin{tabular}{@{}lcc@{}}
29	\toprule
30	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
31	\midrule
32	Single-pass (80 types) & 0.504 & 0.557 \\
33	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
34	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds. Graph coloring yields +1.4\,pp over random batching ($p \approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}
38	\label{tab:batch_composition}
39	\end{table}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "fd8abfe2-f954-4997-b75f-e168c2017063",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Merge amplification in NER.}\nThe core failure mechanism is \\emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \\cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.\n\nQuantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\\to$ 0.314 for sdgd\\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\\to$ 0.251 (sdgd\\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\\,=\\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.\n\n\\paragraph{Confidence gating does not resolve merge amplification.}\nConfidence-based gating (retaining only predictions above threshold) trades recall for precision but does not recover net F1 (0.251$\\to$0.241), confirming that merge artifacts are systemic rather than confined to low-confidence predictions (Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.\n\n\\paragraph{Oracle routing as performance ceiling.}\nOracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.\n\nHowever, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds. Graph coloring yields +1.4\\,pp over random batching ($p \\approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}\n\\label{tab:batch_composition}\n\\end{table}\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T15:11:14.697Z_

<details><summary>↩ Tool result · `toolu_01LzALJo59XYBXPq7BXF6HX8`</summary>

```text
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (18 pages, 417280 bytes).
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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "15db00fa-1f21-4090-8a94-de43b915dc0f",
  "tool_use_result": {
    "stdout": "/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (18 pages, 417280 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
The paper compiles to 18 pages. Now I need to check where the conclusion ends. Let me check the PDF or look for a way to determine where the conclusion falls. Let me check the log for page breaks or use a different method to find where the conclusion ends.

Actually, I should look at where things are page-wise. Let me use `pdftotext` or a similar tool to check which pages have what content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "bb31f2a4-19cb-44d3-add7-6ec7a4098087",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2n2Bux9bD36Ut98f6gd2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6425,
      "cache_read_input_tokens": 35000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6425
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

Let me check where the Conclusion ends in the compiled PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "4ddf0fcd-e659-4cef-9091-197933a5a86d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2n2Bux9bD36Ut98f6gd2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6425,
      "cache_read_input_tokens": 35000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6425
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

<details open><summary>🔧 Tool call — Bash · `toolu_01PxP3wmH1hLgw6j9HXhB4Yh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdftotext main.pdf - 2>/dev/null | grep -n \"Conclusion\\|Limitations\\|References\" | head -10",
  "description": "Find Conclusion and Limitations positions in PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "6ace0f23-2fbf-4ece-ae1a-11dc67fcd566",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2n2Bux9bD36Ut98f6gd2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6425,
      "cache_read_input_tokens": 35000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6425
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

_source line 23 · 2026-05-16T15:11:21.550Z_

<details><summary>↩ Tool result · `toolu_01PxP3wmH1hLgw6j9HXhB4Yh`</summary>

```text
1238:on 8B NER (Limitations, item 1).
1716:Conclusion
1735:Limitations
1864:Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise
2211:References
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "05d30280-3b8f-42bf-a3fa-d3b4727901aa",
  "tool_use_result": {
    "stdout": "1238:on 8B NER (Limitations, item 1).\n1716:Conclusion\n1735:Limitations\n1864:Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise\n2211:References",
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01HY4yFEBX1bevuyi3Vn9Vn1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdftotext -layout main.pdf - 2>/dev/null | grep -n \"^$\" | head -5; echo \"---\"; pdftotext main.pdf /tmp/paper_text.txt 2>/dev/null && grep -n \"Conclusion\\|Limitations\" /tmp/paper_text.txt",
  "description": "Extract text and find section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "2b5b9fbb-125d-4bf7-8d13-18e541a28960",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2n2Bux9bD36Ut98f6gd2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6425,
      "cache_read_input_tokens": 35000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6425
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

_source line 25 · 2026-05-16T15:11:23.500Z_

<details><summary>↩ Tool result · `toolu_01HY4yFEBX1bevuyi3Vn9Vn1`</summary>

```text
3:
4:
6:
7:
8:
---
1238:on 8B NER (Limitations, item 1).
1716:Conclusion
1735:Limitations
1864:Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "58035299-91c7-4cba-89e6-80148c71b3c1",
  "tool_use_result": {
    "stdout": "3:\n4:\n6:\n7:\n8:\n---\n1238:on 8B NER (Limitations, item 1).\n1716:Conclusion\n1735:Limitations\n1864:Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise",
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01H9YBTE9Cpo7Uzp8ZSeZkBQ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\n')\n# Find page breaks (form feeds)\npage = 1\nfor i, line in enumerate(lines):\n    if '\\f' in line:\n        page += 1\n    if 'Conclusion' in line and page <= 10:\n        print(f'Page {page}, line {i}: {line.strip()}')\n    if 'Limitations' in line and page <= 10:\n        print(f'Page {page}, line {i}: {line.strip()}')\nprint(f'Total pages in text: {page}')\n\"",
  "description": "Find which page Conclusion and Limitations fall on"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "e343773a-27f7-4151-9a09-e2bde2fccfcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx97fhibCYXwcdp2RgRe2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 41425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 27 · 2026-05-16T15:11:29.179Z_

<details><summary>↩ Tool result · `toolu_01H9YBTE9Cpo7Uzp8ZSeZkBQ`</summary>

```text
Page 6, line 485: 447      on 8B NER (Limitations, item 1).
Page 8, line 632: 630   amplification confirmed by Monte Carlo simulation            7   Conclusion                                          679
Page 8, line 647: 643   mitigation strategies follow from the two-channel            Limitations                                             691
Page 9, line 676: 706      not reach significance (p = 0.50; Appendix C).                 Yes. The Limitations section (after §7) dis-       753
Total pages in text: 19
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "690ec99d-8cb3-41de-8421-0798b65f1600",
  "tool_use_result": {
    "stdout": "Page 6, line 485: 447      on 8B NER (Limitations, item 1).\nPage 8, line 632: 630   amplification confirmed by Monte Carlo simulation            7   Conclusion                                          679\nPage 8, line 647: 643   mitigation strategies follow from the two-channel            Limitations                                             691\nPage 9, line 676: 706      not reach significance (p = 0.50; Appendix C).                 Yes. The Limitations section (after §7) dis-       753\nTotal pages in text: 19",
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

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
The output seems to indicate that the Conclusion is on page 8, line 632 and Limitations is on page 8, line 647. But also there's something on page 9 about limitations. Let me look more carefully. It seems like it might be a two-column layout.

Wait, looking at the content more carefully:
- Page 8, line 632: "amplification confirmed by Monte Carlo simulation" + "7 Conclusion 679"
- Page 8, line 647: "mitigation strategies follow from the two-channel" + "Limitations 691"

So it seems like the layout extracts two columns side by side. 

Now I'm checking the actual source file to see what's really there. The Conclusion section is quite brief—just a few lines—and it wraps up the main finding about schema-induced degradation operating through two separable channels with replication across model families.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "188ef257-6e3f-4327-a517-5dbbca9c3b52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWzsiSWGzE9u2Yza3YK3oa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 42150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 29_

Let me get a clearer picture of what's on each page boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "11e76f16-bfef-42fd-b1a8-c1f4781e3429",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWzsiSWGzE9u2Yza3YK3oa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 42150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01GD2rNdUDMGTCmMPcTvhfxw`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages[:10], 1):\n    lines = [l for l in page.strip().split('\\n') if l.strip()]\n    if lines:\n        print(f'=== Page {i} (last 5 lines) ===')\n        for l in lines[-5:]:\n            print(f'  {l.strip()[:80]}')\n        print()\n\"",
  "description": "Show last 5 lines of each page to find Conclusion location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "12a22642-8c5a-4ffa-afb3-bf4a9b1dca91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWzsiSWGzE9u2Yza3YK3oa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 42150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 31 · 2026-05-16T15:11:47.412Z_

<details><summary>↩ Tool result · `toolu_01GD2rNdUDMGTCmMPcTvhfxw`</summary>

```text
=== Page 1 (last 5 lines) ===
  078
  079
  080
  081
  082

=== Page 2 (last 5 lines) ===
  177
  178
  179
  180
  181

=== Page 3 (last 5 lines) ===
  262
  263
  264
  265
  266

=== Page 4 (last 5 lines) ===
  359
  360
  361
  362
  363

=== Page 5 (last 5 lines) ===
  425
  426
  427
  428
  429

=== Page 6 (last 5 lines) ===
  510
  511
  512
  513
  514

=== Page 7 (last 5 lines) ===
  599
  600
  601
  602
  603

=== Page 8 (last 5 lines) ===
  696
  697
  698
  699
  700

=== Page 9 (last 5 lines) ===
  790
  789
  791
  792
  793

=== Page 10 (last 5 lines) ===
  875
  876
  877
  878
  879
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "2e5f289f-f7ff-419c-9002-764055e5757d",
  "tool_use_result": {
    "stdout": "=== Page 1 (last 5 lines) ===\n  078\n  079\n  080\n  081\n  082\n\n=== Page 2 (last 5 lines) ===\n  177\n  178\n  179\n  180\n  181\n\n=== Page 3 (last 5 lines) ===\n  262\n  263\n  264\n  265\n  266\n\n=== Page 4 (last 5 lines) ===\n  359\n  360\n  361\n  362\n  363\n\n=== Page 5 (last 5 lines) ===\n  425\n  426\n  427\n  428\n  429\n\n=== Page 6 (last 5 lines) ===\n  510\n  511\n  512\n  513\n  514\n\n=== Page 7 (last 5 lines) ===\n  599\n  600\n  601\n  602\n  603\n\n=== Page 8 (last 5 lines) ===\n  696\n  697\n  698\n  699\n  700\n\n=== Page 9 (last 5 lines) ===\n  790\n  789\n  791\n  792\n  793\n\n=== Page 10 (last 5 lines) ===\n  875\n  876\n  877\n  878\n  879",
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

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
These are line numbers from the PDF text (it's in review mode with line numbers). Let me look at it differently - I need to see the actual content near the page breaks, particularly around page 8-9.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "66702122-ad9e-4d34-8528-7045dcd533df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBjSj7V5duidhenLkFHijq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 42587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1031
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SLwL32LzWhKcDFGVXMsUYF`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\n# Show page 8 and 9 content\nfor i in [7, 8]:  # 0-indexed\n    page = pages[i]\n    lines = page.strip().split('\\n')\n    print(f'=== Page {i+1} ===')\n    # Show first 15 and last 15 lines\n    print('--- First 15 lines ---')\n    for l in lines[:15]:\n        print(f'  {l[:100]}')\n    print('--- Last 15 lines ---')\n    for l in lines[-15:]:\n        print(f'  {l[:100]}')\n    print()\n\"",
  "description": "Show content of pages 8-9 to find Conclusion boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "a579b12e-a42a-4530-b963-b8e06dac1dc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBjSj7V5duidhenLkFHijq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 42587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1031
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

_source line 34 · 2026-05-16T15:11:54.299Z_

<details><summary>↩ Tool result · `toolu_01SLwL32LzWhKcDFGVXMsUYF`</summary>

```text
=== Page 8 ===
--- First 15 lines ---
  604
  
  6
  
  605
  
  Boundary conditions. The two-channel decomposition applies to cross-domain schemas; samedomain schem
  that obscures per-type aggregated signals, requiring
  pairwise SCS or centrality adjustment (§4.5). HighBCS accuracy converges to ≈51% across tested
  models, suggesting a task-inherent difficulty ceiling. RE’s clean channel separation may partly
  reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope −0.71).
  Prompt design modulates but does not eliminate
  the effect (v2 gap: −25.5 pp vs. v1 extreme-batch
  gap; Appendix H).
  
--- Last 15 lines ---
  684
  685
  686
  687
  688
  689
  
  693
  694
  695
  696
  697
  698
  699
  700

=== Page 9 ===
--- First 15 lines ---
  701
  702
  703
  704
  705
  706
  707
  708
  709
  710
  711
  712
  713
  714
  715
--- Last 15 lines ---
  
  788
  
  Yes. All four datasets are publicly available
  research benchmarks. Few-NERD is released
  under CC-BY-SA 4.0; FewRel, DocRED, and
  MAVEN are publicly released for research use.
  
  790
  
  789
  
  791
  792
  793
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "61b0bc33-e5e4-43f3-b96a-42c55176e2f8",
  "tool_use_result": {
    "stdout": "=== Page 8 ===\n--- First 15 lines ---\n  604\n  \n  6\n  \n  605\n  \n  Boundary conditions. The two-channel decomposition applies to cross-domain schemas; samedomain schem\n  that obscures per-type aggregated signals, requiring\n  pairwise SCS or centrality adjustment (§4.5). HighBCS accuracy converges to ≈51% across tested\n  models, suggesting a task-inherent difficulty ceiling. RE’s clean channel separation may partly\n  reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope −0.71).\n  Prompt design modulates but does not eliminate\n  the effect (v2 gap: −25.5 pp vs. v1 extreme-batch\n  gap; Appendix H).\n  \n--- Last 15 lines ---\n  684\n  685\n  686\n  687\n  688\n  689\n  \n  693\n  694\n  695\n  696\n  697\n  698\n  699\n  700\n\n=== Page 9 ===\n--- First 15 lines ---\n  701\n  702\n  703\n  704\n  705\n  706\n  707\n  708\n  709\n  710\n  711\n  712\n  713\n  714\n  715\n--- Last 15 lines ---\n  \n  788\n  \n  Yes. All four datasets are publicly available\n  research benchmarks. Few-NERD is released\n  under CC-BY-SA 4.0; FewRel, DocRED, and\n  MAVEN are publicly released for research use.\n  \n  790\n  \n  789\n  \n  791\n  792\n  793",
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01RdQ9HwW1RS2m7SgPxJBYjk`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\n# Show full page 8\npage = pages[7]\nlines = page.strip().split('\\n')\nprint(f'=== Page 8 ({len(lines)} lines) ===')\nfor l in lines:\n    stripped = l.strip()\n    if stripped and not stripped.isdigit() and len(stripped) > 3:\n        print(f'  {stripped[:120]}')\n\" 2>&1 | tail -60",
  "description": "Show all content lines on page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "697aafb8-6b30-4d32-8f9d-cba376b053c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNFwh11irVKXL9CLCd7kJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 43618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 795
      },
      "output_tokens": 69,
      "service_tier": "standard",
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

_source line 36 · 2026-05-16T15:11:59.084Z_

<details><summary>↩ Tool result · `toolu_01RdQ9HwW1RS2m7SgPxJBYjk`</summary>

```text
  reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope −0.71).
  Prompt design modulates but does not eliminate
  the effect (v2 gap: −25.5 pp vs. v1 extreme-batch
  gap; Appendix H).
  Discussion
  ity graph (§5), accepting the precision–recall tradeoff that merge introduces. We deliberately avoid
  recommending a fixed SCS threshold, as optimal
  granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema
  size, and available compute budget for multi-pass
  extraction.
  Why does embedding similarity predict LLM
  confusion? Type name embeddings capture semantic proximity in the same representational
  space LLMs use for in-context type resolution;
  high SCS indexes the degree of representational
  overlap that causes substitution errors during decoding. The pair-level effect is modest (R2 ≈ 7%)
  because individual substitutions are stochastic, but
  pairs sharing a common type exhibit correlated
  SCS values (ρ = 0.35), so co-occurring high-SCS
  pairs aggregate constructively—an effective ∼3×
  amplification confirmed by Monte Carlo simulation
  (Appendix M). Batch-level BCS therefore explains
  22–53% of accuracy variance, sufficient for prehoc schema screening.
  Schema design implications. Since typical random batches differ by only ≈ 2.2 pp (§4.3), the
  practical impact depends on schema composition.
  Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compu
  the type inventory and flag pairs exceeding a high
  percentile (e.g., 75th) of the corpus’s SCS distribution as high-risk for mutual confusion. Three
  mitigation strategies follow from the two-channel
  decomposition: (i) Expand definitions—for highSCS pairs, include contrastive definitions or disambiguating examples in t
  representational separation; (ii) Rename types—
  replace semantically proximate labels with more
  descriptive alternatives (e.g., “person-artist” → “visual artist (painter/sculptor)”) to reduce embedding overlap; (iii)
  high-SCS pairs to different extraction passes using
  graph coloring on the SCS-thresholded confusabil-
  Cross-domain connections. Schema complexity
  effects may parallel findings in schema-guided dialogue systems (§2; see Appendix N for discussion).
  Model scale and confusability sensitivity. Preliminary evidence from two model sizes (32B vs.
  8B) suggests that Channel 2 (confusability) effects
  attenuate on smaller models due to floor effects,
  while Channel 1 (count) replicates fully (Tables 4–
  5). Systematic scaling studies remain future work.
  Future directions. Three directions merit investigation: (i) non-oracle routing strategies that make
  decomposition deployable without gold labels;
  (ii) broader model coverage, particularly proprietary APIs; and (iii) definition-inclusive SCS (current name+definition 
  improvement; Appendix L). For NER, calibrationaware merge or joint decoding may address merge
  amplification (§5).
  Conclusion
  We presented controlled evidence that schemainduced degradation operates through two additively separable channels—count
  replicating across model families and extraction
  granularities (R2 up to 0.53). The practical contribution is a lightweight pre-hoc screening tool:
  batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle
  routing for decomposition and broader model coverage including proprietary APIs.
  Limitations
  1. Model coverage. Primary experiments use
  Qwen3-32B with cross-model validation on
  Llama-3.1-8B-Instruct. Whether patterns hold
  for proprietary models (GPT-4, Gemini) remains unverified. Channel 2 was not robustly
  detectable on NER at 8B scale, likely due to
  floor effects.
  2. Modest pairwise effect size. Pairwise SCS explains 1.3–1.7% of type confusion variance; en8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "6b207b88-39c5-4fb9-aec5-2cfee1576bd8",
  "tool_use_result": {
    "stdout": "  reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope −0.71).\n  Prompt design modulates but does not eliminate\n  the effect (v2 gap: −25.5 pp vs. v1 extreme-batch\n  gap; Appendix H).\n  Discussion\n  ity graph (§5), accepting the precision–recall tradeoff that merge introduces. We deliberately avoid\n  recommending a fixed SCS threshold, as optimal\n  granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema\n  size, and available compute budget for multi-pass\n  extraction.\n  Why does embedding similarity predict LLM\n  confusion? Type name embeddings capture semantic proximity in the same representational\n  space LLMs use for in-context type resolution;\n  high SCS indexes the degree of representational\n  overlap that causes substitution errors during decoding. The pair-level effect is modest (R2 ≈ 7%)\n  because individual substitutions are stochastic, but\n  pairs sharing a common type exhibit correlated\n  SCS values (ρ = 0.35), so co-occurring high-SCS\n  pairs aggregate constructively—an effective ∼3×\n  amplification confirmed by Monte Carlo simulation\n  (Appendix M). Batch-level BCS therefore explains\n  22–53% of accuracy variance, sufficient for prehoc schema screening.\n  Schema design implications. Since typical random batches differ by only ≈ 2.2 pp (§4.3), the\n  practical impact depends on schema composition.\n  Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compu\n  the type inventory and flag pairs exceeding a high\n  percentile (e.g., 75th) of the corpus’s SCS distribution as high-risk for mutual confusion. Three\n  mitigation strategies follow from the two-channel\n  decomposition: (i) Expand definitions—for highSCS pairs, include contrastive definitions or disambiguating examples in t\n  representational separation; (ii) Rename types—\n  replace semantically proximate labels with more\n  descriptive alternatives (e.g., “person-artist” → “visual artist (painter/sculptor)”) to reduce embedding overlap; (iii)\n  high-SCS pairs to different extraction passes using\n  graph coloring on the SCS-thresholded confusabil-\n  Cross-domain connections. Schema complexity\n  effects may parallel findings in schema-guided dialogue systems (§2; see Appendix N for discussion).\n  Model scale and confusability sensitivity. Preliminary evidence from two model sizes (32B vs.\n  8B) suggests that Channel 2 (confusability) effects\n  attenuate on smaller models due to floor effects,\n  while Channel 1 (count) replicates fully (Tables 4–\n  5). Systematic scaling studies remain future work.\n  Future directions. Three directions merit investigation: (i) non-oracle routing strategies that make\n  decomposition deployable without gold labels;\n  (ii) broader model coverage, particularly proprietary APIs; and (iii) definition-inclusive SCS (current name+definition \n  improvement; Appendix L). For NER, calibrationaware merge or joint decoding may address merge\n  amplification (§5).\n  Conclusion\n  We presented controlled evidence that schemainduced degradation operates through two additively separable channels—count\n  replicating across model families and extraction\n  granularities (R2 up to 0.53). The practical contribution is a lightweight pre-hoc screening tool:\n  batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle\n  routing for decomposition and broader model coverage including proprietary APIs.\n  Limitations\n  1. Model coverage. Primary experiments use\n  Qwen3-32B with cross-model validation on\n  Llama-3.1-8B-Instruct. Whether patterns hold\n  for proprietary models (GPT-4, Gemini) remains unverified. Channel 2 was not robustly\n  detectable on NER at 8B scale, likely due to\n  floor effects.\n  2. Modest pairwise effect size. Pairwise SCS explains 1.3–1.7% of type confusion variance; en8",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Looking at this, it seems like the Conclusion actually ends on page 8 already. The "8" at the very end is the page number. The Limitations section also starts on page 8. Let me check what's on page 9.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "97677980-504f-4bef-856a-f2eeed147c03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EW9mhTZQbb4WYhQBUUisR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 44413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1288
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SekwjjYPjJQM55qpfFyVkR`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\n# Show full page 9\npage = pages[8]\nlines = page.strip().split('\\n')\nprint(f'=== Page 9 ({len(lines)} lines) ===')\nfor l in lines:\n    stripped = l.strip()\n    if stripped and not stripped.isdigit() and len(stripped) > 3:\n        print(f'  {stripped[:120]}')\n\" 2>&1 | head -60",
  "description": "Show page 9 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "16059c84-03a8-4561-843b-4923dbe3b8bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EW9mhTZQbb4WYhQBUUisR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 44413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1288
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

_source line 39 · 2026-05-16T15:12:04.420Z_

<details><summary>↩ Tool result · `toolu_01SekwjjYPjJQM55qpfFyVkR`</summary>

```text
=== Page 9 (219 lines) ===
  tity frequency, prompt position, mention ambiguity, and type definition quality likely account
  for the remainder.
  3. Factorial interaction tests. Within-dataset
  count × BCS interaction on Few-NERD did
  not reach significance (p = 0.50; Appendix C).
  However, a FewRel factorial with TOST equivalence testing confirms additive separability
  (pTOST = .003, interaction = 0.47 pp; Appendix C), and cross-pool slope consistency
  (p = 0.60) corroborates stable rather than amplifying sensitivity.
  5. RE format specificity. RE’s clean channel separation may reflect its closed-set classification
  format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather tha
  6. Causal mechanism. The study establishes correlational evidence with controlled stratification;
  mechanistic analysis at the attention or logit
  level is needed to confirm the causal pathway.
  The controlled stratification provides evidence
  consistent with a directional relationship but
  does not establish interventional causality.
  7. Data contamination. FewRel (2018) may appear in pretraining corpora. However, trainorigin relations show numerically 
  opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7%→50.4%) cannot
  by uniform contamination, which would elevate
  all conditions equally.
  Responsible NLP Research Checklist
  For each question, the answer is Yes, No, or N/A.
  If Yes, the relevant section is indicated. If No, a
  For Every Submission
  A1. Did you describe the limitations of your
  work?
  Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise
  effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence,
  decomposition scope, and metric scope.
  A2. Did you discuss any potential risks of your
  work?
  N/A. This is a purely analytical study of
  schema-induced degradation in existing LLM
  IE systems. It does not introduce new models,
  datasets, or deployment-facing artifacts. The
  findings characterize failure modes and are
  intended to inform safer schema design.
  A3. Do the abstract and introduction summarize the paper’s main claims?
  Yes. The abstract and §1 state the two-channel
  degradation pattern (count and confusability),
  the cross-model consistency check, and the
  negative SDGD result.
  A4. Did you use AI assistants (e.g., ChatGPT,
  Copilot) when working on this paper?
  Yes. An AI coding assistant was used for
  experiment scripting and LaTeX formatting.
  All scientific claims, experimental design, and
  analysis were conducted by the authors.
  Scientific Artifacts
  4. Decomposition and metric scope. RE batch
  composition is tested on FewRel only; NER
  merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may 
  Multiple comparisons. We do not apply familywise correction across datasets, treating each as an
  independent replication. Within-dataset secondary
  analyses are reported with individual p-values; core
  claims rest on effects reaching p < 0.001.
  justification is provided.
  B1. Did you cite the creators of artifacts you
  used?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "6c588cd7-af16-42a9-a48e-d70b3ba79d14",
  "tool_use_result": {
    "stdout": "=== Page 9 (219 lines) ===\n  tity frequency, prompt position, mention ambiguity, and type definition quality likely account\n  for the remainder.\n  3. Factorial interaction tests. Within-dataset\n  count × BCS interaction on Few-NERD did\n  not reach significance (p = 0.50; Appendix C).\n  However, a FewRel factorial with TOST equivalence testing confirms additive separability\n  (pTOST = .003, interaction = 0.47 pp; Appendix C), and cross-pool slope consistency\n  (p = 0.60) corroborates stable rather than amplifying sensitivity.\n  5. RE format specificity. RE’s clean channel separation may reflect its closed-set classification\n  format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather tha\n  6. Causal mechanism. The study establishes correlational evidence with controlled stratification;\n  mechanistic analysis at the attention or logit\n  level is needed to confirm the causal pathway.\n  The controlled stratification provides evidence\n  consistent with a directional relationship but\n  does not establish interventional causality.\n  7. Data contamination. FewRel (2018) may appear in pretraining corpora. However, trainorigin relations show numerically \n  opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7%→50.4%) cannot\n  by uniform contamination, which would elevate\n  all conditions equally.\n  Responsible NLP Research Checklist\n  For each question, the answer is Yes, No, or N/A.\n  If Yes, the relevant section is indicated. If No, a\n  For Every Submission\n  A1. Did you describe the limitations of your\n  work?\n  Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise\n  effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence,\n  decomposition scope, and metric scope.\n  A2. Did you discuss any potential risks of your\n  work?\n  N/A. This is a purely analytical study of\n  schema-induced degradation in existing LLM\n  IE systems. It does not introduce new models,\n  datasets, or deployment-facing artifacts. The\n  findings characterize failure modes and are\n  intended to inform safer schema design.\n  A3. Do the abstract and introduction summarize the paper’s main claims?\n  Yes. The abstract and §1 state the two-channel\n  degradation pattern (count and confusability),\n  the cross-model consistency check, and the\n  negative SDGD result.\n  A4. Did you use AI assistants (e.g., ChatGPT,\n  Copilot) when working on this paper?\n  Yes. An AI coding assistant was used for\n  experiment scripting and LaTeX formatting.\n  All scientific claims, experimental design, and\n  analysis were conducted by the authors.\n  Scientific Artifacts\n  4. Decomposition and metric scope. RE batch\n  composition is tested on FewRel only; NER\n  merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may \n  Multiple comparisons. We do not apply familywise correction across datasets, treating each as an\n  independent replication. Within-dataset secondary\n  analyses are reported with individual p-values; core\n  claims rest on effects reaching p < 0.001.\n  justification is provided.\n  B1. Did you cite the creators of artifacts you\n  used?",
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

<details><summary>Logged reasoning block</summary>

```text
Now I can see the picture more clearly. Looking at page 8's content:
- Discussion section starts on page 8 (section 6)
- Conclusion starts and ends on page 8
- Limitations starts on page 8

And page 9 continues with:
- Rest of Limitations
- Responsible NLP Research Checklist

So the Conclusion actually already fits on page 8! But wait, let me re-read the user's problem statement. They said "当前 Conclusion 延伸到 p9 上半部分，超约 0.5 页". Let me look more carefully...


Actually, I need to check the ACL format rules more carefully. The body text from Introduction through Conclusion has a hard limit of 8 pages, and looking at the line distribution across pages, the Conclusion does technically fit on page 8, but the real issue is that Limitations is spilling over into page 9.

Let me reconsider the structure: in standard ACL format, the abstract appears on page 1 along with the start of the Introduction, and then the main content (Introduction through Conclusion) must stay within those 8 pages total. Anything after Conclusion—like Limitations, Ethics statements, and References—can extend beyond that limit.

Looking at the actual page numbers in the PDF, the Conclusion wraps up on page 8, and the Limitations section begins right after it on the same page. This suggests the body content is actually within the 8-page constraint, even though it might feel tight. The confusion might be coming from how the two-column layout affects the text extraction, making it harder to see where exactly the page breaks fall. Looking at the two-column layout of page 8, I can see the Discussion section flows into the Conclusion, and then the Limitations section begins—all on the same page. The real question is whether the Conclusion actually wraps up before the Limitations starts, or if there's overlap that's causing the formatting issue. Given how much content is packed into page 8 across both columns, it seems like everything is compressed right at the boundary, which might be why the layout feels tight.

Let me check the LaTeX log file for any overfull box warnings or page overflow messages that would tell me exactly where the content is breaking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "e7fd0725-2376-4c19-be47-23c412401683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrxViAAMx55cVynKbAo8So",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 45701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1184
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

<details open><summary>🔧 Tool call — Bash · `toolu_01KTVsPvpnDGzwFXxjnfHDpB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -i \"overfull\\|underfull\\|page\" main.log | grep -i \"page\" | tail -20",
  "description": "Check log for page overflow warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "2f0016b3-f78c-4052-9670-c0f49c6fb3d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrxViAAMx55cVynKbAo8So",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 45701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1184
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

_source line 42 · 2026-05-16T15:12:37.993Z_

<details><summary>↩ Tool result · `toolu_01KTVsPvpnDGzwFXxjnfHDpB`</summary>

```text
\c@pagewiselinenumber=\count287
\c@LN@truepage=\count288
Package: geometry 2020/01/02 v5.9 Page Geometry
\Hy@pagecounter=\count301
Package hyperref Info: Plain pages OFF on input line 4210.
\Hy@abspage=\count305
Output written on main.pdf (18 pages, 417280 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "1ae8a849-9481-4992-827b-94f680a0db00",
  "tool_use_result": {
    "stdout": "\\c@pagewiselinenumber=\\count287\n\\c@LN@truepage=\\count288\nPackage: geometry 2020/01/02 v5.9 Page Geometry\n\\Hy@pagecounter=\\count301\nPackage hyperref Info: Plain pages OFF on input line 4210.\n\\Hy@abspage=\\count305\nOutput written on main.pdf (18 pages, 417280 bytes).",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01GQ5iYf868Z79ZdQHoScwMb`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\n# Use pdfinfo to check page count and pdftotext to find where Conclusion ends\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\n\n# Find which page contains 'Limitations' section header (the section AFTER conclusion)\nfor i, page in enumerate(pages, 1):\n    if 'Limitations' in page and i <= 10:\n        # Check if Conclusion is on this page too\n        has_conclusion = 'Conclusion' in page\n        # Find the position of Limitations relative to page\n        lines = page.split('\\n')\n        for j, line in enumerate(lines):\n            if 'Limitations' in line and 'section' not in line.lower() and j < 20:\n                print(f'Page {i}: Limitations found at relative line {j}/{len(lines)}')\n                break\n        if has_conclusion:\n            for j, line in enumerate(lines):\n                if 'Conclusion' in line and 'section' not in line.lower():\n                    print(f'Page {i}: Conclusion found at relative line {j}/{len(lines)}')\n                    break\n\"",
  "description": "Find Conclusion and Limitations page positions precisely"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "6ca87496-20b2-4e19-b972-4b0a1bd1cfad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrxViAAMx55cVynKbAo8So",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 45701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1184
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

_source line 44 · 2026-05-16T15:12:43.684Z_

<details><summary>↩ Tool result · `toolu_01GQ5iYf868Z79ZdQHoScwMb`</summary>

```text
Page 8: Conclusion found at relative line 138/195
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "e2f0908e-f93d-4f00-ba8a-0dcd40a375cc",
  "tool_use_result": {
    "stdout": "Page 8: Conclusion found at relative line 138/195",
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

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
So the Conclusion is at line 138 out of 195 lines on page 8. And Limitations is not found on page 8 in the first 20 lines. Let me check where Limitations starts.

Wait, actually let me re-run - I had a condition `j < 20` for Limitations. Let me remove that constraint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "72276b1d-9d50-4311-be61-d27e5743866d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP1wTQgPWqUFYYcijgoee9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1996,
      "cache_read_input_tokens": 46885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1996
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

<details open><summary>🔧 Tool call — Bash · `toolu_01TuSyKeZY2zXA94YZh1ZFPF`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\n\n# Page 8 (0-indexed: 7)\npage8 = pages[7]\nlines8 = page8.split('\\n')\nprint(f'Page 8 total lines: {len(lines8)}')\n# Find Conclusion and Limitations positions\nfor j, line in enumerate(lines8):\n    if 'Conclusion' in line:\n        print(f'  Conclusion at line {j}: {line.strip()[:80]}')\n    if 'Limitations' in line:\n        print(f'  Limitations at line {j}: {line.strip()[:80]}')\n\n# Page 9 (0-indexed: 8)  \npage9 = pages[8]\nlines9 = page9.split('\\n')\nprint(f'\\\\nPage 9 total lines: {len(lines9)}')\nfor j, line in enumerate(lines9[:30]):\n    if line.strip() and not line.strip().isdigit() and len(line.strip()) > 3:\n        print(f'  line {j}: {line.strip()[:100]}')\n\"",
  "description": "Precisely locate Conclusion and Limitations across pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "0c858c0d-eae3-4c59-819a-dc3862dac0ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP1wTQgPWqUFYYcijgoee9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1996,
      "cache_read_input_tokens": 46885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1996
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

_source line 47 · 2026-05-16T15:12:52.658Z_

<details><summary>↩ Tool result · `toolu_01TuSyKeZY2zXA94YZh1ZFPF`</summary>

```text
Page 8 total lines: 195
  Conclusion at line 138: Conclusion
  Limitations at line 157: Limitations

Page 9 total lines: 221
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "b485d57a-3664-46e0-a599-20e587716be3",
  "tool_use_result": {
    "stdout": "Page 8 total lines: 195\n  Conclusion at line 138: Conclusion\n  Limitations at line 157: Limitations\n\nPage 9 total lines: 221",
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

<details><summary>Logged reasoning block</summary>

```text
So on page 8:
- Conclusion starts at line 138/195
- Limitations starts at line 157/195

Both Conclusion and Limitations start on page 8. The Limitations section then continues onto page 9. 

So actually, the Conclusion is already within page 8! The body (Intro through Conclusion) fits in 8 pages.

But wait - maybe the user has additional content that I'm not seeing, or they compiled with different settings. Let me check if the Limitations section is supposed to come after page 8 (unlimited pages). 

Looking at the ACL rules more carefully: the main content from intro through conclusion should be ≤ 8 pages, while Limitations, Ethics statements, References, and Appendix are all unlimited and don't count toward the page limit. So if the Conclusion ends on page 8 and Limitations starts on page 8, that's actually fine — the Conclusion is within the 8-page constraint. But the user mentioned that the Conclusion currently extends into the top half of page 9, which would mean it's exceeding the limit.

Let me reconsider what's happening here. The user might be working with a slightly different version of the document, or perhaps the Discussion section is so lengthy that it's pushing the Conclusion to the very end of page 8, creating a tight situation if any edits are needed. I should verify the actual page structure by checking the page footer numbers in the extracted content — if the last line shows "8" as the page number, then that's definitely page 8 in the document.

Looking at the line distribution, the Conclusion heading appears around line 138 out of 195 total lines, with Limitations starting at line 157, which suggests the Conclusion occupies roughly 19 lines of extracted text. In a two-column format, that's probably 10-15 lines per column, so it might actually fit on page 8. But the user's assessment could be more accurate than my pdftotext analysis, especially given the two-column layout complexities. Either way, compressing the Conclusion is worthwhile since it creates more breathing room and prevents overflow issues. I'm checking the line counts more carefully—with the two-column layout, page 8's 195 lines makes sense when both columns are extracted together. The Conclusion sits around 71% through the page and Limitations around 80%, which aligns with them being in the right column's lower section. The paper seems to be right at the boundary, so I'll proceed with compressing the Conclusion first to ensure it stays within page 8, then tackle the Discussion section.

Looking at the Conclusion itself, it's already quite compact at just 5 lines in the source—probably 8-9 lines in the compiled PDF, which is already hitting the target of 8-10 lines. So that's actually in good shape.

Now I need to focus on compressing the Discussion. The first priority is that paragraph about why embedding similarity predicts LLM confusion—it's currently too verbose with repeated derivations that should be moved to the appendix, leaving only the key takeaway in the main text.

The core insight is that type name embeddings capture the semantic proximity that LLMs use for in-context resolution, and high SCS values indicate representational overlap causing substitution errors. The pair-level effect is modest individually, but when high-SCS pairs co-occur, their effects aggregate constructively to produce a substantial batch-level signal—this is what makes BCS effective for pre-hoc screening. I can trim the Monte Carlo simulation details since those belong in the appendix, and just state the conclusion that batch-level BCS explains 22–53% of accuracy variance.

For the cross-domain connections paragraph, I'm removing it entirely since it only cites the appendix and doesn't add substantive content to the main narrative.

For the model scale section, I need to merge the key finding about confusability effects attenuating on smaller models into the boundary conditions discussion, then delete the standalone section. The core point is that channel 1 (count) effects hold across model sizes while channel 2 (confusability) shows floor effects on smaller models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "cce64177-3cd7-4987-a22c-7e6db82c312b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfyxTnH2HgkZANR6HqUGKh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 48881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 573
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

The Conclusion is on page 8 at ~71% of the page. It's on the boundary. Let me proceed with the compression.

**Priority 1**: The Conclusion is already 4 lines in source / ~8 rendered lines — it's at the target. No change needed.

**Priority 2**: Compressing Discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "d0644c90-7762-4888-bd0b-ef771d91c51e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfyxTnH2HgkZANR6HqUGKh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 48881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 573
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01V9tYyym2WQTc9hX4gDk7od`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
  "new_string": "\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "2bd4a480-c532-4cf0-8807-ed155b7dc11c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfyxTnH2HgkZANR6HqUGKh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 48881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 573
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

_source line 51 · 2026-05-16T15:13:48.478Z_

<details><summary>↩ Tool result · `toolu_01V9tYyym2WQTc9hX4gDk7od`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "0cbd84bd-58d3-4261-9bfb-431968a3acfb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
    "newString": "\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Boundary conditions.}",
          "-The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          "+The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).",
          " ",
          " \\paragraph{Why does embedding similarity predict LLM confusion?}",
          " Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening."
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

Now compress the "Why does embedding similarity..." paragraph and remove "Cross-domain connections" and "Model scale" paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "fda9ba9f-3060-43f7-8ce0-4e4bea6a3183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcUAf3F4nYftGDx9UMR6X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2675,
      "cache_read_input_tokens": 49454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2675
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

<details open><summary>🔧 Tool call — Edit · `toolu_016ZzW1zWYBv1YWLYqTkYRW1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening.",
  "new_string": "\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "8cbeef07-75fb-4ce2-b364-c58d1b4f62d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcUAf3F4nYftGDx9UMR6X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2675,
      "cache_read_input_tokens": 49454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2675
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

_source line 54 · 2026-05-16T15:13:55.754Z_

<details><summary>↩ Tool result · `toolu_016ZzW1zWYBv1YWLYqTkYRW1`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "09912e7e-bf4c-42ab-9a66-9f788dfe6b40",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening.",
    "newString": "\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
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
          "-Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes the degree of representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) because individual substitutions are stochastic, but pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so co-occurring high-SCS pairs aggregate constructively---an effective ${\\sim}3\\times$ amplification confirmed by Monte Carlo simulation (Appendix~\\ref{app:aggregation-sim}). Batch-level BCS therefore explains 22--53\\% of accuracy variance, sufficient for pre-hoc schema screening.",
          "+Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.",
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

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_012oEfSJS33z58pZcE5aGsq4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (§2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "1858adb0-bc17-4463-82e3-df2f3235cb82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KidKAGQHAcz3Hbt288EQXC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 52129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
      },
      "output_tokens": 72,
      "service_tier": "standard",
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

_source line 56 · 2026-05-16T15:14:01.482Z_

<details><summary>↩ Tool result · reported error · `toolu_012oEfSJS33z58pZcE5aGsq4`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: \paragraph{Cross-domain connections.}
Schema complexity effects may parallel findings in schema-guided dialogue systems (§2; see Appendix~\ref{app:cross-domain} for discussion).

\paragraph{Model scale and confusability sensitivity.}
Preliminary evidence from two model sizes (32B vs.\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.


(note: Edit also tried swapping \uXXXX escapes and their characters; neither form matched, so the mismatch is likely elsewhere in old_string. Re-read the file and copy the exact surrounding text.)&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "76aaa077-7375-427a-96bd-046bce3ad95f",
  "tool_use_result": "Error: String to replace not found in file.\nString: \\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (§2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\n(note: Edit also tried swapping \\uXXXX escapes and their characters; neither form matched, so the mismatch is likely elsewhere in old_string. Re-read the file and copy the exact surrounding text.)"
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_011bKymmk3KQUQK2zsWhaZoj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "offset": 15,
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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "17d401a3-b5d6-4eac-9c07-c87081c6cfae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGJBsejpSDPhP1zWKkvZjk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 52673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 58 · 2026-05-16T15:14:04.470Z_

<details><summary>↩ Tool result · `toolu_011bKymmk3KQUQK2zsWhaZoj`</summary>

```text
15	(iii)~\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\S\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.
16	We deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.
17	
18	\paragraph{Cross-domain connections.}
19	Schema complexity effects may parallel findings in schema-guided dialogue systems (\S2; see Appendix~\ref{app:cross-domain} for discussion).
20	
21	\paragraph{Model scale and confusability sensitivity.}
22	Preliminary evidence from two model sizes (32B vs.\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.
23	
24	\paragraph{Future directions.}
25	Three directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\S\ref{sec:sdgd}).
26	
27	\section{Conclusion}
28	\label{sec:conclusion}
29	
30	We presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "3101b057-63ef-463c-a20a-5d3209bd5f49",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
      "numLines": 17,
      "startLine": 15,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
I see - the cross-domain connections paragraph uses `\S2` (with `\S`) instead of `§2`. Let me use the exact text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "25cde555-e939-4151-8dc9-cf4f535fbb80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qmpaGGyZB4sM3jgTmmeiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 53196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01FGsQdR2z4K5hTLxAk2bGdt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}",
  "new_string": "\\paragraph{Future directions.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "df1a1021-58c4-4ca3-95db-cb054554d80d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qmpaGGyZB4sM3jgTmmeiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 53196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

_source line 61 · 2026-05-16T15:14:12.616Z_

<details><summary>↩ Tool result · `toolu_01FGsQdR2z4K5hTLxAk2bGdt`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "20cb8d7e-41c6-4898-b119-bf96ca12a93a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}",
    "newString": "\\paragraph{Future directions.}",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest ($R^2 \\approx 7\\%$) but amplifies ${\\sim}3\\times$ at the batch level through inter-pair correlation (Appendix~\\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\\%---sufficient for pre-hoc schema screening.\n\n\\paragraph{Schema design implications.}\nSince typical random batches differ by only ${\\approx}\\,2.2$\\,pp (\\S\\ref{sec:practical_magnitude}), the practical impact depends on schema composition.\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented controlled evidence that schema-induced degradation operates through two additively separable channels---count-driven recall decline and confusability-driven type confusion---replicating across model families and extraction granularities ($R^2$ up to 0.53). The practical contribution is a lightweight pre-hoc screening tool: batch-level BCS flags high-risk schemas before deployment. Future work should address non-oracle routing for decomposition and broader model coverage including proprietary APIs.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 12,
        "newStart": 15,
        "newLines": 6,
        "lines": [
          " (iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.",
          " We deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.",
          " ",
          "-\\paragraph{Cross-domain connections.}",
          "-Schema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).",
          "-",
          "-\\paragraph{Model scale and confusability sensitivity.}",
          "-Preliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.",
          "-",
          " \\paragraph{Future directions.}",
          " Three directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).",
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

_source line 62_

Now compile to check the result.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "3c3dc678-b6e2-490a-8f5a-c35fdacc2725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVm2ec1AAGP88bKtNNX2Kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 53859,
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01EUFJqRpcud6z995xkABBYN`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"Error|error|Output written\"",
  "description": "Compile paper after Priority 2 edits",
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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "80fe15fa-137e-4025-887d-9a18e08ddf09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVm2ec1AAGP88bKtNNX2Kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 53859,
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

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b8qf0ocgb",
  "tool_use_id": "toolu_01EUFJqRpcud6z995xkABBYN",
  "description": "Compile paper after Priority 2 edits",
  "task_type": "local_bash",
  "uuid": "897ecc9d-ae41-4f50-88a3-4fd981de27db",
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d"
}
```

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b8qf0ocgb",
  "tool_use_id": "toolu_01EUFJqRpcud6z995xkABBYN",
  "status": "completed",
  "output_file": "",
  "summary": "Compile paper after Priority 2 edits",
  "uuid": "f0e5242e-9c24-4c56-be17-e9374430c81f",
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d"
}
```

---

### Tool result

_source line 66 · 2026-05-16T15:14:20.491Z_

<details><summary>↩ Tool result · `toolu_01EUFJqRpcud6z995xkABBYN`</summary>

```text
 [6 <../../figures/paper/fig_error_taxonomy.pdf>]) (./discussion.tex [7]
Output written on main.pdf (18 pages, 416546 bytes).
 [6 <../../figures/paper/fig_error_taxonomy.pdf>]) (./discussion.tex [7]
Output written on main.pdf (18 pages, 416365 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "e0567baa-ddca-4327-98c5-2a93e16c681e",
  "tool_use_result": {
    "stdout": " [6 <../../figures/paper/fig_error_taxonomy.pdf>]) (./discussion.tex [7]\nOutput written on main.pdf (18 pages, 416546 bytes).\n [6 <../../figures/paper/fig_error_taxonomy.pdf>]) (./discussion.tex [7]\nOutput written on main.pdf (18 pages, 416365 bytes).",
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

_source line 67_

Compiles fine. Let me verify where Conclusion ends now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "db4cd46a-69d7-4038-8181-12e7f53ed85f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxMKg9DDmjCUpBq9a48TPk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 54260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_011rzggD8GtVNGpM5deUmJmP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\n\n# Check pages 7 and 8 (0-indexed)\nfor idx in [6, 7, 8]:\n    page = pages[idx]\n    lines = page.split('\\n')\n    has_conclusion = any('Conclusion' in l for l in lines)\n    has_limitations = any('Limitations' in l for l in lines)\n    has_discussion = any('Discussion' in l for l in lines)\n    print(f'Page {idx+1}: Discussion={has_discussion}, Conclusion={has_conclusion}, Limitations={has_limitations}')\n    if has_conclusion:\n        for j, line in enumerate(lines):\n            if 'Conclusion' in line:\n                print(f'  Conclusion at line {j}/{len(lines)}')\n    if has_limitations:\n        for j, line in enumerate(lines):\n            if 'Limitations' in line:\n                print(f'  Limitations at line {j}/{len(lines)}')\n                break\n\"",
  "description": "Check Conclusion page position after compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "cdc0f647-ff71-430e-a19a-237fe9e3ed9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxMKg9DDmjCUpBq9a48TPk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 54260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 69 · 2026-05-16T15:14:33.140Z_

<details><summary>↩ Tool result · `toolu_011rzggD8GtVNGpM5deUmJmP`</summary>

```text
Page 7: Discussion=False, Conclusion=False, Limitations=False
Page 8: Discussion=True, Conclusion=True, Limitations=True
  Conclusion at line 112/191
  Limitations at line 131/191
Page 9: Discussion=False, Conclusion=False, Limitations=True
  Limitations at line 184/224
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "823e7bf2-f92f-49da-b14f-f12a1f1510f3",
  "tool_use_result": {
    "stdout": "Page 7: Discussion=False, Conclusion=False, Limitations=False\nPage 8: Discussion=True, Conclusion=True, Limitations=True\n  Conclusion at line 112/191\n  Limitations at line 131/191\nPage 9: Discussion=False, Conclusion=False, Limitations=True\n  Limitations at line 184/224",
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

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
After the compression:
- Conclusion is now at line 112/191 on page 8 (was 138/195)
- Limitations starts at line 131/191 on page 8 (was 157/195)

The Conclusion has moved from 71% of the way through the page to 59%, gaining significant breathing room. Limitations starts at 69% (was 80%). The Conclusion is well within page 8.

Let me verify the final state of the file and check for any compilation warnings, then report the results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "ac4ad5fc-0a76-4bab-a33e-5acf0b875c2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCMqEXEEFoYRG9veAfNo5Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 54532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 71_

Let me verify the final state of discussion.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "e9cba48c-cce4-46da-b65c-9e4979edf0e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCMqEXEEFoYRG9veAfNo5Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 54532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

<details open><summary>🔧 Tool call — Read · `toolu_01M9fjcef3gd3PSH46jyZ9qg`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "a747379f-6bd4-4e5a-b79a-76e1dac4b681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCMqEXEEFoYRG9veAfNo5Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 54532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 73 · 2026-05-16T15:14:38.683Z_

<details><summary>↩ Tool result · `toolu_01M9fjcef3gd3PSH46jyZ9qg`</summary>

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
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "a61c968a-d3d9-4c1d-953b-670a0f5df4e8",
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

### Assistant

_source line 74_

Compression complete. Let me verify no LaTeX errors and confirm the final position.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "c098cc64-9aed-4766-9e8c-ff4d8c0d4468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016J4KfFZztahskJoxEG2VaS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 55038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1396
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

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01LAozWUF8UTmhb3hHTdqxWj`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -c \"^!\" main.log; echo \"---\"; grep \"Undefined control sequence\\|Missing\" main.log | head -5",
  "description": "Check for LaTeX errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "82199b84-be8c-4233-b908-109c6b456189",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016J4KfFZztahskJoxEG2VaS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 55038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1396
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

_source line 76 · 2026-05-16T15:14:43.547Z_

<details><summary>↩ Tool result · `toolu_01LAozWUF8UTmhb3hHTdqxWj`</summary>

```text
0
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "a6961794-98c5-41fc-b519-f1ddd0819a88",
  "tool_use_result": {
    "stdout": "0\n---",
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

_source line 77_

No errors. Final result:

**Priority 1 (Conclusion)**: Already at target (~4 source lines / ~8 rendered lines). No change needed.

**Priority 2 (Discussion)**: Compressed ~12 source lines:
- "Why does embedding similarity..." paragraph: cut from 5 lines to 3 (removed Monte Carlo mechanism details, kept conclusion)
- "Cross-domain connections" paragraph: deleted entirely (2 lines)
- "Model scale" paragraph: deleted (3 lines); merged as 1 sentence into "Boundary conditions"

**Conclusion position**: moved from line 138/195 (71%) to line 112/191 (59%) on page 8. Limitations starts at line 131/191. Well within the 8-page limit — no need for Priority 3.

**Compilation**: 0 errors, 18 pages total (unchanged — savings absorbed into more breathing room on page 8).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "uuid": "a3493ac5-9150-4047-a6c9-740c9ad46515",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mmH6rJeKzTycRum279XP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 172,
      "cache_read_input_tokens": 56434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 172
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

_source line 78_

No errors. Final result:

**Priority 1 (Conclusion)**: Already at target (~4 source lines / ~8 rendered lines). No change needed.

**Priority 2 (Discussion)**: Compressed ~12 source lines:
- "Why does embedding similarity..." paragraph: cut from 5 lines to 3 (removed Monte Carlo mechanism details, kept conclusion)
- "Cross-domain connections" paragraph: deleted entirely (2 lines)
- "Model scale" paragraph: deleted (3 lines); merged as 1 sentence into "Boundary conditions"

**Conclusion position**: moved from line 138/195 (71%) to line 112/191 (59%) on page 8. Limitations starts at line 131/191. Well within the 8-page limit — no need for Priority 3.

**Compilation**: 0 errors, 18 pages total (unchanged — savings absorbed into more breathing room on page 8).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 236041,
  "duration_api_ms": 229311,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "20983ad2-972e-45f0-aba9-63d3da72ab4d",
  "total_cost_usd": 1.02555575,
  "usage": {
    "input_tokens": 3798,
    "cache_creation_input_tokens": 44765,
    "cache_read_input_tokens": 932785,
    "output_tokens": 10349,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44765,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 217,
        "cache_read_input_tokens": 56434,
        "cache_creation_input_tokens": 172,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 172
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1582,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001667,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3798,
      "outputTokens": 10349,
      "cacheReadInputTokens": 932785,
      "cacheCreationInputTokens": 44765,
      "webSearchRequests": 0,
      "costUSD": 1.02388875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3099d08f-4bcf-4e87-9dc7-d0f050b90762"
}
```

</details>

---
