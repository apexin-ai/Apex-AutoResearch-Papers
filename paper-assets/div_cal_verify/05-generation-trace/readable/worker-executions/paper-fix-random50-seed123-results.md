# paper fix random50 seed123 results

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_paper_fix_random50_seed123_results_20260514T083701.log`
- **Structured JSON:** [`3f3a38c890d6904bb617.json`](../../sessions/3f/3f3a38c890d6904bb617.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
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
  "uuid": "a0913b39-5898-48b2-9c65-9bd502787617",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-div-cal-verify/memory/"
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
    "resetsAt": 1778764200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "97119498-29c5-4430-9096-ceed5ec7cd47",
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get the RGDS seed=123 data, and also read the results.tex file to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "458d9358-a8e5-41fc-8e73-0476e24a3156",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APW5ZUVUWWfrJzVEgQ1jbU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11538,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11538
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

Let me first read the registry and the results.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "0fb94fbd-42a9-49ff-b938-a53083e20414",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APW5ZUVUWWfrJzVEgQ1jbU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11538,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11538
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011Tdpz3MQrbKq5gntLeQb3U`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "7fc85cd6-64f5-4e46-8c48-e1c9e17bd364",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APW5ZUVUWWfrJzVEgQ1jbU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11538,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11538
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

_source line 7 · 2026-05-14T08:37:15.902Z_

<details><summary>↩ Tool result · `toolu_011Tdpz3MQrbKq5gntLeQb3U`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "d2300cf4-1c5f-49e0-91e5-f0bbd567c2a7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_017jAkSabvQm4tmhskhrvzpY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "24682bad-66c1-43ed-94dd-71b389b7c6ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APW5ZUVUWWfrJzVEgQ1jbU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11538,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11538
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

_source line 9 · 2026-05-14T08:37:16.074Z_

<details><summary>↩ Tool result · reported error · `toolu_017jAkSabvQm4tmhskhrvzpY`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "41c3ea02-0968-4d0b-9825-a34c392fbb31",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify."
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The file doesn't exist at that path. Let me find the actual location of results.tex and also query the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "a03e317c-be3c-4c82-b86a-78ff5166def4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrLBti5DFBig8WmVMKKNG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 23379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
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

<details open><summary>🔧 Tool call — Glob · `toolu_01V7v1GaYNdWX3M3beaGVsB2`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "26db93d7-45c9-4cb7-9eea-8dfe34457f72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrLBti5DFBig8WmVMKKNG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 23379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
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

_source line 12 · 2026-05-14T08:37:20.754Z_

<details><summary>↩ Tool result · `toolu_01V7v1GaYNdWX3M3beaGVsB2`</summary>

```text
artifacts/dream_reports/dream_20260513T081019/best/paper.tex
artifacts/dream_reports/dream_20260513T081019/median/paper.tex
artifacts/dream_reports/dream_20260513T081019/worst/paper.tex
artifacts/_project/paper/methodology.tex
artifacts/tables/table1_gen7_summary_latex.tex
artifacts/_project/paper/experiments_112f46.tex
artifacts/_project/paper/experiments.tex
docs/paper/methodology.tex
docs/paper/main.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "56ec69d5-57e5-4bfa-a631-7fe505c62bf0",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T081019/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T081019/worst/paper.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/tables/table1_gen7_summary_latex.tex",
      "artifacts/_project/paper/experiments_112f46.tex",
      "artifacts/_project/paper/experiments.tex",
      "docs/paper/methodology.tex",
      "docs/paper/main.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/experiments.tex",
      "docs/paper/discussion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 21,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Aobgqb9EX49jmR7mpzSi5m`</summary>

```json
{
  "project": "div_cal_verify",
  "filters": {
    "exp_id_prefix": "medium_rgds"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "63244d5a-f715-4e23-801b-048328150b8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrLBti5DFBig8WmVMKKNG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 23379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
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

_source line 14 · 2026-05-14T08:37:21.271Z_

<details><summary>↩ Tool result · `toolu_01Aobgqb9EX49jmR7mpzSi5m`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.189}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "e21902e6-5784-410c-b010-25a1c2699021",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.189}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.189}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01DZC1pURzUY1rZmxHDrMhNB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "a54436ac-ebf1-4b56-b9d3-2e6655b759b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu8Z5kQMY99GG46hAwztze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 24037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 530
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

_source line 16 · 2026-05-14T08:37:23.676Z_

<details><summary>↩ Tool result · `toolu_01DZC1pURzUY1rZmxHDrMhNB`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Table~\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.
5	
6	\begin{table*}[t]
7	\centering
8	\small
9	\begin{tabular}{lcccccccc}
10	\toprule
11	Method & Budget & Gen\,0 PPL & Gen\,7 PPL & $\Delta$\% & Sel.\ Ratio & Rare n-gram & RankMe & $n$ \\
12	\midrule
13	Random 50\% & 50\% & 36.87 & 43.18$\pm$1.43 & +17 & $\approx$1.00 & .0098$\pm$.0003 & 290.98$\pm$0.98 & 3 \\
14	External-only & 50\% & 36.74 & 46.36$\pm$2.97 & +26 & 1.16$\pm$0.08 & .0103$\pm$.0004 & 291.45$\pm$1.08 & 3 \\
15	Uncurated & 100\% & 36.81 & 47.04$\pm$2.90 & +28 & --- & .0090$\pm$.0004 & 289.83$\pm$1.77 & 3 \\
16	RGDS & 50\% & 36.83 & 74.29$\pm$7.71 & +102 & 0.64$\pm$0.20 & .0061$\pm$.0009 & 292.54$\pm$5.91 & 3 \\
17	\bottomrule
18	\end{tabular}
19	\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\Delta$\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}
20	\label{tab:gen7_summary}
21	\end{table*}
22	
23	\begin{figure}[t]
24	\centering
25	\includegraphics[width=\columnwidth]{figures/fig_ppl_trends.pdf}
26	\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \pm 7.71$), while the other three methods converge to a narrow band (43--47).}
27	\label{fig:ppl_trends}
28	\end{figure}
29	
30	\begin{figure}[t]
31	\centering
32	\includegraphics[width=\columnwidth]{figures/fig_ratio_trajectory.pdf}
33	\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\sim}1.0$ to $0.64 \pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\to$0.87) without perplexity recovery.}
34	\label{fig:ratio_trajectory}
35	\end{figure}
36	
37	\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}
38	\label{sec:result_c1}
39	
40	RGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \pm 7.71$ ($n{=}3$), compared to $47.04 \pm 2.90$ for Uncurated ($n{=}3$; +58\%) and $43.18 \pm 1.43$ for Random~50\% ($n{=}3$; +72\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\sigma = 7.71$) substantially exceeds that of any other method ($\sigma \leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.
41	
42	The selection ratio traces the mechanism behind this degradation (Figure~\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\sim}1.0$ at Generation~0 to $0.64 \pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.
43	
44	\subsection{External Embeddings Avoid the Alignment Gap}
45	\label{sec:result_c2}
46	
47	External-only selection applies the identical selection algorithm and 50\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \pm 2.90$) and Random~50\% ($43.18 \pm 1.43$).
48	
49	External-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.
50	
51	Since RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.
52	
53	Notably, External-only does not significantly outperform Random~50\% in perplexity ($46.36 \pm 2.97$ vs.\ $43.18 \pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \S\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.
54	
55	\subsection{Internal Selection Underperforms Random Baseline}
56	\label{sec:result_c3}
57	
58	The comparison between RGDS and Random~50\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\% vs.\ 100\%).
59	
60	Under this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \pm 7.71$, $n{=}3$) exceeds Random~50\% ($43.18 \pm 1.43$, $n{=}3$) by $+$72\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.
61	
62	Rare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \pm 0.0009$ at Generation~7, compared to $0.0098 \pm 0.0003$ for Random~50\%---a 38\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \emph{less} diverse than those from uninformed subsampling.
63	
64	This within-budget contrast should be distinguished from the RGDS vs.\ Uncurated comparison ($+$58\%), which conflates any selection effect with a data quantity difference (50\% vs.\ 100\%). The Random~50\% vs.\ Uncurated comparison (\S\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.
65	
66	\subsection{Random Pruning: A Directional Observation}
67	\label{sec:result_s3}
68	
69	Random~50\% ($43.18 \pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \pm 2.90$, $n{=}3$), a reduction of 8.2\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\% vs.\ 100\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.
70	
71	If confirmed with additional statistical power, this result would suggest that training on a random 50\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \citep{sorscher2022beyond}.
72	
73	While the perplexity difference remains directional, Random~50\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \pm 0.0003$) exceeds Uncurated ($0.0090 \pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.
74	
75	\subsection{Lexical Diversity Collapse Across Methods}
76	\label{sec:result_diversity}
77	
78	RGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \pm 0.0009$ at Generation~7 (Table~\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\% ($0.0098 \pm 0.0003$), Uncurated ($0.0090 \pm 0.0004$), and External-only ($0.0102 \pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\%.
79	
80	Unlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \S\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.
81	
82	\begin{table*}[t]
83	\centering
84	\small
85	\begin{tabular}{llrrrrl}
86	\toprule
87	Comparison & Metric & $\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\
88	\midrule
89	\multicolumn{7}{l}{\textit{RGDS vs.\ non-RGDS methods}} \\
90	RGDS vs.\ Random 50\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\
91	RGDS vs.\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\
92	RGDS vs.\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\
93	RGDS vs.\ Random 50\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\
94	RGDS vs.\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\
95	RGDS vs.\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\
96	\midrule
97	\multicolumn{7}{l}{\textit{Within-cluster comparisons}} \\
98	External vs.\ Random 50\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\
99	Random 50\% vs.\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\
100	Random 50\% vs.\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\
101	\midrule
102	\multicolumn{7}{l}{\textit{ANOVA (one-way)}} \\
103	Non-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\,6 & .219 & --- \\
104	Non-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\,6 & .007 & --- \\
105	\midrule
106	\multicolumn{7}{l}{\textit{GPT2-Medium (355M)---statistical tests pending $\geq$3 seeds}} \\
107	RGDS vs.\ Random 50\% & PPL & $+$12.59$^\dagger$ & \multicolumn{3}{c}{---} & --- \\
108	Random 50\% vs.\ Uncurated & PPL & $-$21.41$^\dagger$ & \multicolumn{3}{c}{---} & --- \\
109	RGDS vs.\ Uncurated & PPL & $-$8.82 / $+$3.20$^\ddagger$ & \multicolumn{3}{c}{---} & --- \\
110	\bottomrule
111	\end{tabular}
112	\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\dagger$seed=42 only (Random~50\% seed=123 pending). $^\ddagger$RGDS vs.\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}
113	\label{tab:stat_tests}
114	\end{table*}
115	
116	\subsection{Representation Metrics Do Not Track Content Collapse}
117	\label{sec:result_rankme}
118	
119	RankMe values at Generation~7 are comparable across all methods (289--293; Table~\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \pm 5.91$ for RGDS vs.\ ${\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.
120	
121	\subsection{Scaling to GPT2-Medium (355M)}
122	\label{sec:result_scaling}
123	
124	Results from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\% seed=123 pending).%
125	%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete
126	
127	\begin{table}[t]
128	\centering
129	\small
130	\begin{tabular}{lcccc}
131	\toprule
132	Method & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\
133	\midrule
134	Random 50\% & 50\% & 70.25 & --- & 1 \\
135	External-only & 50\% & 77.74 & 79.56 & 2 \\
136	RGDS & 50\% & 82.84 & 90.25 & 2 \\
137	Uncurated & 100\% & 91.66 & 87.05 & 2 \\
138	\bottomrule
139	\end{tabular}
140	\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\ 91.66 at seed=42; 90.25 vs.\ 87.05 at seed=123). Random~50\% seed=123 and all seed=456 experiments are pending.}
141	\label{tab:medium_comparison}
142	\end{table}
143	
144	\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\% (70.25) by +18\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%
145	%TODO(355M-seeds): confirm with seed=123 and report significance
146	
147	\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\ 91.66) but underperforms at seed=123 (90.25 vs.\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\% ($74.29$ vs.\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \S\ref{sec:discuss_scaling}. The cross-budget comparison (50\% vs.\ 100\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\ Random~50\%, both at 50\%) isolates the effect of the selection mechanism.%
148	%TODO(355M-seeds): update with seed=456 data
149	
150	\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\% perplexity penalty relative to Random (vs.\ +72\% at 125M) is consistent with this narrower gap.%
151	%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "f7f8e120-9a18-457b-9159-d8c52c2900df",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & --- & 1 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). Random~50\\% seed=123 and all seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): confirm with seed=123 and report significance\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
      "numLines": 152,
      "startLine": 1,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BMWjs61ooAiqc98WAhKgQL`</summary>

```json
{
  "project": "div_cal_verify",
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
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "61fc742a-942c-43e9-9cf0-4de887c7f49e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu8Z5kQMY99GG46hAwztze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 24037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 530
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

_source line 18 · 2026-05-14T08:37:24.243Z_

<details><summary>↩ Tool result · `toolu_01BMWjs61ooAiqc98WAhKgQL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"medium_uncurated_seed456\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T03:21:27.986Z\", \"updated_at\": \"2026-05-14T08:35:39.375Z\", \"hypothesis\": \"GPT2-medium (355M) Uncurated seed=456: 3-seed 统计检验，验证 355M collapse 跨 seed 一致性\", \"parent\": \"medium_uncurated_seed42\"}, \"medium_random50_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:56:03.403Z\", \"updated_at\": \"2026-05-14T08:34:19.307Z\", \"hypothesis\": \"GPT2-medium (355M) Random 50% seed=123: 2-seed 统计检验依赖，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致\", \"parent\": \"medium_random50_seed42\", \"metrics\": {\"gen0\": {\"ppl\": 26.31, \"rankme\": 363.28, \"knn\": 0.988, \"rare_ngram\": 0.0343, \"rank_corr\": 0.019}, \"gen1\": {\"ppl\": 33.54, \"rankme\": 399.19, \"knn\": 0.988, \"rare_ngram\": 0.0298, \"rank_corr\": 0.013}, \"gen2\": {\"ppl\": 43.31, \"rankme\": 417.48, \"knn\": 0.988, \"rare_ngram\": 0.0224, \"rank_corr\": 0.008}, \"gen3\": {\"ppl\": 50.01, \"rankme\": 423.83, \"knn\": 0.988, \"rare_ngram\": 0.0187, \"rank_corr\": -0.013}, \"gen4\": {\"ppl\": 56.82, \"rankme\": 425.56, \"knn\": 0.988, \"rare_ngram\": 0.016, \"rank_corr\": -0.034}, \"gen5\": {\"ppl\": 65.35, \"rankme\": 426.7, \"knn\": 0.988, \"rare_ngram\": 0.0154, \"rank_corr\": -0.053}, \"gen6\": {\"ppl\": 70.43, \"rankme\": 421.46, \"knn\": 0.988, \"rare_ngram\": 0.014, \"rank_corr\": -0.047}, \"gen7\": {\"ppl\": 72.55, \"rankme\": 421.96, \"knn\": 0.988, \"rare_ngram\": 0.0131, \"rank_corr\": -0.049}}, \"conclusion\": \"success\"}, \"medium_rgds_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:56:02.314Z\", \"updated_at\": \"2026-05-14T07:29:35.117Z\", \"hypothesis\": \"GPT2-medium (355M) RGDS seed=123: 2-seed 统计检验依赖，验证 alignment gap 加速崩塌在 355M 跨 seed 一致\", \"parent\": \"medium_rgds_seed42\", \"conclusion\": \"success\", \"metrics\": {\"gen0\": {\"ppl\": 26.32, \"rankme\": 365.65, \"knn\": 0.988, \"rare\": 0.0343, \"corr\": 0.0301, \"ratio\": 0.9623}, \"gen1\": {\"ppl\": 33.72, \"rankme\": 396.58, \"knn\": 0.988, \"rare\": 0.0285, \"corr\": 0.0135, \"ratio\": 0.8893}, \"gen2\": {\"ppl\": 43.58, \"rankme\": 416.12, \"knn\": 0.988, \"rare\": 0.0224, \"corr\": 0.0148, \"ratio\": 0.9445}, \"gen3\": {\"ppl\": 51.8, \"rankme\": 422.63, \"knn\": 0.988, \"rare\": 0.0194, \"corr\": -0.0004, \"ratio\": 0.8469}, \"gen4\": {\"ppl\": 57.08, \"rankme\": 422.85, \"knn\": 0.988, \"rare\": 0.0183, \"corr\": -0.0109, \"ratio\": 0.9441}, \"gen5\": {\"ppl\": 69.28, \"rankme\": 426.34, \"knn\": 0.988, \"rare\": 0.0171, \"corr\": -0.0089, \"ratio\": 0.8997}, \"gen6\": {\"ppl\": 77.57, \"rankme\": 428.93, \"knn\": 0.988, \"rare\": 0.0162, \"corr\": -0.0274, \"ratio\": 0.9364}, \"gen7\": {\"ppl\": 90.25, \"rankme\": 431.19, \"knn\": 0.988, \"rare\": 0.0149, \"corr\": -0.017, \"ratio\": 0.8728}}}, \"medium_uncurated_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:55:48.455Z\", \"updated_at\": \"2026-05-14T07:29:31.269Z\", \"hypothesis\": \"GPT2-medium (355M) Uncurated baseline seed=123: 2-seed 统计检验依赖，验证 355M collapse 严重度跨 seed 一致\", \"parent\": \"medium_uncurated_seed42\", \"conclusion\": \"success\", \"metrics\": {\"gen0\": {\"ppl\": 26.48, \"rankme\": 368.37, \"knn\": 0.988, \"rare\": 0.0343, \"corr\": 0.0407}, \"gen1\": {\"ppl\": 35.54, \"rankme\": 402.99, \"knn\": 0.988, \"rare\": 0.0286, \"corr\": 0.0311}, \"gen2\": {\"ppl\": 48.53, \"rankme\": 421.72, \"knn\": 0.988, \"rare\": 0.0218, \"corr\": 0.0264}, \"gen3\": {\"ppl\": 61.54, \"rankme\": 434.05, \"knn\": 0.988, \"rare\": 0.0185, \"corr\": 0.0021}, \"gen4\": {\"ppl\": 69.38, \"rankme\": 438.69, \"knn\": 0.988, \"rare\": 0.0169, \"corr\": -0.0367}, \"gen5\": {\"ppl\": 76.22, \"rankme\": 438.77, \"knn\": 0.988, \"rare\": 0.0154, \"corr\": -0.0375}, \"gen6\": {\"ppl\": 83.35, \"rankme\": 437.49, \"knn\": 0.988, \"rare\": 0.0145, \"corr\": -0.0391}, \"gen7\": {\"ppl\": 87.05, \"rankme\": 436.04, \"knn\": 0.988, \"rare\": 0.0136, \"corr\": -0.0375}}}, \"medium_external_seed456\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T03:21:29.786Z\", \"updated_at\": \"2026-05-14T07:13:53.442Z\", \"hypothesis\": \"GPT2-medium (355M) External-only seed=456: 3-seed 统计检验，验证 frozen embeddings 在 355M 跨 seed 避免 alignment gap\", \"parent\": \"medium_external_seed42\"}, \"medium_external_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:56:03.780Z\", \"updated_at\": \"2026-05-14T06:49:14.249Z\", \"hypothesis\": \"GPT2-medium (355M) External-only seed=123: 2-seed 统计检验依赖，验证 frozen Contriever embeddings 在 355M 跨 seed 仍避免 alignment gap\", \"parent\": \"medium_external_seed42\", \"conclusion\": \"success\", \"metrics\": {\"gen0\": {\"ppl\": 26.3, \"rankme\": 366.16, \"knn\": 0.988, \"rare\": 0.0343, \"corr\": 0.0119}, \"gen1\": {\"ppl\": 33.62, \"rankme\": 400.2, \"knn\": 0.988, \"rare\": 0.0303, \"corr\": 0.0077}, \"gen2\": {\"ppl\": 44.51, \"rankme\": 417.58, \"knn\": 0.988, \"rare\": 0.0246, \"corr\": -0.0114}, \"gen3\": {\"ppl\": 51.18, \"rankme\": 421.73, \"knn\": 0.988, \"rare\": 0.0206, \"corr\": -0.014}, \"gen4\": {\"ppl\": 61.11, \"rankme\": 427.42, \"knn\": 0.988, \"rare\": 0.0184, \"corr\": -0.0282}, \"gen5\": {\"ppl\": 69.58, \"rankme\": 429.36, \"knn\": 0.988, \"rare\": 0.0172, \"corr\": -0.0232}, \"gen6\": {\"ppl\": 74.33, \"rankme\": 428.14, \"knn\": 0.988, \"rare\": 0.0168, \"corr\": -0.0458}, \"gen7\": {\"ppl\": 79.56, \"rankme\": 429.83, \"knn\": 0.988, \"rare\": 0.0161, \"corr\": -0.0533, \"ratio\": 1.222}}}, \"medium_random50_seed456\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T03:21:29.247Z\", \"updated_at\": \"2026-05-14T03:22:00.608Z\", \"hypothesis\": \"GPT2-medium (355M) Random 50% seed=456: 3-seed 统计检验，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致\", \"parent\": \"medium_random50_seed42\"}, \"medium_rgds_seed456\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T03:21:28.342Z\", \"updated_at\": \"2026-05-14T03:21:59.635Z\", \"hypothesis\": \"GPT2-medium (355M) RGDS seed=456: 3-seed 统计检验，验证 alignment gap 在 355M 跨 seed 一致\", \"parent\": \"medium_rgds_seed42\"}, \"medium_external_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:32:08.840Z\", \"updated_at\": \"2026-05-14T03:11:09.334Z\", \"hypothesis\": \"GPT2-medium (355M) External-only diversity selection: 验证 frozen Contriever embeddings 在更大模型上是否仍能避免 alignment gap（model scaling + external embedding interaction）\", \"conclusion\": \"success\", \"metrics\": {\"gen7_ppl\": 77.74, \"gen7_rankme\": 421.5, \"gen7_knn\": 0.988, \"gen7_rare_ngram\": 0.0165, \"gen7_rank_corr\": -0.0072, \"gen0_ppl\": 26.33, \"gen0_rankme\": 363.43, \"ppl_increase_ratio\": 2.95, \"rankme_increase\": 58.07}}, \"medium_random50_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:01:02.034Z\", \"updated_at\": \"2026-05-14T01:53:02.738Z\", \"hypothesis\": \"GPT2-medium (355M) Random 50% baseline: 验证同 budget 随机选择在更大模型上的表现，作为 RGDS alignment gap 在 355M scale 的关键对照组\", \"parent\": \"medium_rgds_seed42\", \"metrics\": {\"gen0\": {\"ppl\": 26.12, \"rankme\": 361.63, \"knn\": 0.988, \"rare\": 0.0346, \"corr\": 0.0101}, \"gen1\": {\"ppl\": 32.57, \"rankme\": 387.8, \"knn\": 0.988, \"rare\": 0.0277, \"corr\": 0.0331}, \"gen2\": {\"ppl\": 41.58, \"rankme\": 410.08, \"knn\": 0.988, \"rare\": 0.0214, \"corr\": 0.0088}, \"gen3\": {\"ppl\": 49.87, \"rankme\": 421.67, \"knn\": 0.988, \"rare\": 0.0182, \"corr\": -0.0018}, \"gen4\": {\"ppl\": 59.83, \"rankme\": 427.23, \"knn\": 0.988, \"rare\": 0.0161, \"corr\": -0.0014}, \"gen5\": {\"ppl\": 60.62, \"rankme\": 426.16, \"knn\": 0.988, \"rare\": 0.0144, \"corr\": -0.0004}, \"gen6\": {\"ppl\": 68.34, \"rankme\": 427.19, \"knn\": 0.988, \"rare\": 0.0134, \"corr\": -0.0071}, \"gen7\": {\"ppl\": 70.25, \"rankme\": 426.5, \"knn\": 0.988, \"rare\": 0.0128, \"corr\": -0.0034}}, \"conclusion\": \"success\"}, \"medium_rgds_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T21:37:18.001Z\", \"updated_at\": \"2026-05-14T00:53:34.267Z\", \"hypothesis\": \"GPT2-medium (355M) RGDS diversity selection: 验证 alignment gap 加速崩塌在更大模型上是否复现（model scaling + method interaction）\", \"parent\": \"medium_uncurated_seed42\", \"metrics\": {\"gen0\": {\"ppl\": 26.04, \"rankme\": 365.07, \"knn\": 0.988, \"rare\": 0.0346, \"corr\": 0.0196, \"ratio\": 0.9759}, \"gen1\": {\"ppl\": 32.99, \"rankme\": 398.29, \"knn\": 0.988, \"rare\": 0.0286, \"corr\": 0.0402, \"ratio\": 0.9991}, \"gen2\": {\"ppl\": 41.99, \"rankme\": 418.21, \"knn\": 0.988, \"rare\": 0.0232, \"corr\": 0.0014, \"ratio\": 0.9225}, \"gen3\": {\"ppl\": 50.8, \"rankme\": 421.44, \"knn\": 0.988, \"rare\": 0.0198, \"corr\": 0.0058, \"ratio\": 0.9127}, \"gen4\": {\"ppl\": 60.71, \"rankme\": 425.62, \"knn\": 0.988, \"rare\": 0.0187, \"corr\": -0.0068, \"ratio\": 0.7989}, \"gen5\": {\"ppl\": 66.29, \"rankme\": 424.71, \"knn\": 0.988, \"rare\": 0.018, \"corr\": -0.0235, \"ratio\": 0.9002}, \"gen6\": {\"ppl\": 72, \"rankme\": 423.93, \"knn\": 0.988, \"rare\": 0.0168, \"corr\": -0.0197, \"ratio\": 0.7622}, \"gen7\": {\"ppl\": 82.84, \"rankme\": 424.72, \"knn\": 0.988, \"rare\": 0.0166, \"corr\": -0.0286, \"ratio\": 0.8313}}, \"conclusion\": \"success\"}, \"rgds_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:44:56.404Z\", \"updated_at\": \"2026-05-13T23:32:22.643Z\", \"hypothesis\": \"RGDS (50% internal embedding selection) seed=456 复现：3-seed 统计检验依赖，验证 RGDS alignment gap 加速崩塌跨 seed 一致\", \"parent\": \"phase2_3method_selfit\", \"metrics\": {\"gen0_ppl\": 36.7, \"gen0_rankme\": 274.06, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0284, \"gen0_corr\": -0.0138, \"gen0_ratio\": 0.9114, \"gen1_ppl\": 44.59, \"gen1_rankme\": 291.76, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0189, \"gen1_corr\": -0.0418, \"gen1_ratio\": 0.8895, \"gen2_ppl\": 45.3, \"gen2_rankme\": 290.79, \"gen2_knn\": 0.988, \"gen2_rare\": 0.0139, \"gen2_corr\": -0.0356, \"gen2_ratio\": 0.9071, \"gen3_ppl\": 49.13, \"gen3_rankme\": 289.92, \"gen3_knn\": 0.988, \"gen3_rare\": 0.0111, \"gen3_corr\": -0.0403, \"gen3_ratio\": 0.8774, \"gen4_ppl\": 47.4, \"gen4_rankme\": 287.04, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0098, \"gen4_corr\": -0.0342, \"gen4_ratio\": 0.8292, \"gen5_ppl\": 55.99, \"gen5_rankme\": 290.71, \"gen5_knn\": 0.988, \"gen5_rare\": 0.0078, \"gen5_corr\": -0.0269, \"gen5_ratio\": 0.7065, \"gen6_ppl\": 55.99, \"gen6_rankme\": 287.52, \"gen6_knn\": 0.988, \"gen6_rare\": 0.0065, \"gen6_corr\": -0.0247, \"gen6_ratio\": 0.6447, \"gen7_ppl\": 66.22, \"gen7_rankme\": 286.54, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0069, \"gen7_corr\": -0.0228, \"gen7_ratio\": 0.8682}, \"conclusion\": \"success\"}, \"ext_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:44:57.069Z\", \"updated_at\": \"2026-05-13T21:47:35.556Z\", \"hypothesis\": \"External_only (50% Contriever frozen embedding) seed=456 复现：3-seed 统计检验依赖，验证 external_only 免疫 alignment gap 跨 seed 一致\", \"parent\": \"phase2_ext_seed123\", \"conclusion\": \"success\", \"metrics\": {\"gen0_ppl\": 36.51, \"gen0_rankme\": 273.85, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0284, \"gen0_corr\": -0.0103, \"gen0_ratio\": 1.1621, \"gen1_ppl\": 44.77, \"gen1_rankme\": 291.93, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0203, \"gen1_corr\": -0.0404, \"gen1_ratio\": 1.0686, \"gen2_ppl\": 50.84, \"gen2_rankme\": 298.52, \"gen2_knn\": 0.987, \"gen2_rare\": 0.0152, \"gen2_corr\": -0.0292, \"gen2_ratio\": 1.1119, \"gen3_ppl\": 54.43, \"gen3_rankme\": 298.35, \"gen3_knn\": 0.987, \"gen3_rare\": 0.013, \"gen3_corr\": -0.0223, \"gen3_ratio\": 1.1551, \"gen4_ppl\": 49.91, \"gen4_rankme\": 295.86, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0118, \"gen4_corr\": -0.0321, \"gen4_ratio\": 1.1841, \"gen5_ppl\": 50.45, \"gen5_rankme\": 297.37, \"gen5_knn\": 0.988, \"gen5_rare\": 0.0111, \"gen5_corr\": -0.03, \"gen5_ratio\": 1.2186, \"gen6_ppl\": 47.09, \"gen6_rankme\": 294.35, \"gen6_knn\": 0.988, \"gen6_rare\": 0.01, \"gen6_corr\": -0.0207, \"gen6_ratio\": 1.0818, \"gen7_ppl\": 43.9, \"gen7_rankme\": 292.69, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0106, \"gen7_corr\": -0.0227, \"gen7_ratio\": 1.243}}, \"medium_uncurated_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:20:55.822Z\", \"updated_at\": \"2026-05-13T21:42:26.811Z\", \"hypothesis\": \"GPT2-medium (355M) uncurated baseline: 验证 alignment gap 现象在更大模型上是否复现（model scaling 维度）\", \"parent\": \"phase2_3method_selfit\", \"metrics\": {\"gen0_ppl\": 26.55, \"gen0_rankme\": 371.57, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0346, \"gen0_corr\": 0.0219, \"gen1_ppl\": 35.12, \"gen1_rankme\": 403.8, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0281, \"gen1_corr\": 0.0228, \"gen2_ppl\": 46.9, \"gen2_rankme\": 420.83, \"gen2_knn\": 0.988, \"gen2_rare\": 0.0216, \"gen2_corr\": 0.0181, \"gen3_ppl\": 57.4, \"gen3_rankme\": 425.35, \"gen3_knn\": 0.988, \"gen3_rare\": 0.0185, \"gen3_corr\": 0.0011, \"gen4_ppl\": 67.45, \"gen4_rankme\": 430.68, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0172, \"gen4_corr\": -0.0046, \"gen5_ppl\": 78.55, \"gen5_rankme\": 438.62, \"gen5_knn\": 0.987, \"gen5_rare\": 0.0159, \"gen5_corr\": -0.0175, \"gen6_ppl\": 84.59, \"gen6_rankme\": 442.85, \"gen6_knn\": 0.987, \"gen6_rare\": 0.0144, \"gen6_corr\": -0.0462, \"gen7_ppl\": 91.66, \"gen7_rankme\": 443.98, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0139, \"gen7_corr\": -0.0379}, \"conclusion\": \"success\"}, \"uncurated_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:44:55.468Z\", \"updated_at\": \"2026-05-13T19:28:12.126Z\", \"hypothesis\": \"Uncurated (100% data) seed=456 复现：3-seed 统计检验依赖，验证 uncurated 的 PPL/rare 轨迹跨 seed 一致性\", \"parent\": \"phase2_3method_selfit\", \"conclusion\": \"success\", \"metrics\": {\"gen0_ppl\": 36.64, \"gen0_rankme\": 279.17, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0284, \"gen0_corr\": -0.0205, \"gen7_ppl\": 44.69, \"gen7_rankme\": 287.93, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0086, \"gen7_corr\": -0.0696}}, \"random_50_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:01:32.779Z\", \"updated_at\": \"2026-05-13T19:01:00.100Z\", \"hypothesis\": \"Random 50% seed=456 复现：与 phase2_random50_v2 (seed=42) 完全一致的超参数，验证 random≈external 是否跨 seed 成立（C2-revised + C3 验证，3-seed t 检验依赖）\", \"parent\": \"phase2_random50_v2\", \"conclusion\": \"success\", \"metrics\": {\"gen7_ppl\": 44.6, \"gen7_rare\": 0.0101, \"gen7_rankme\": 289.87}}, \"random_50_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:01:31.859Z\", \"updated_at\": \"2026-05-13T19:00:59.367Z\", \"hypothesis\": \"Random 50% seed=123 复现：与 phase2_random50_v2 (seed=42) 完全一致的超参数，验证 random≈external 是否跨 seed 成立（C2-revised + C3 验证，3-seed t 检验依赖）\", \"parent\": \"phase2_random50_v2\", \"conclusion\": \"success\", \"metrics\": {\"gen7_ppl\": 41.75, \"gen7_rare\": 0.0098, \"gen7_rankme\": 291.7}}, \"phase2_random50_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:46:06.927Z\", \"updated_at\": \"2026-05-13T16:01:33.541Z\", \"hypothesis\": \"Random 50% baseline v2: 与 Phase 2 对照组完全一致的超参数(lr=5e-5, epochs=3, 500K tokens/gen)，随机选择 50% 数据，验证 diversity-aware selection 相比随机选择的增益\", \"parent\": \"phase2_3method_selfit\", \"conclusion\": \"success\", \"metrics\": {\"gen0_ppl\": 36.87, \"gen0_rankme\": 275.24, \"gen0_knn\": 0.988, \"gen0_rare\": 0.029, \"gen0_corr\": -0.0081, \"gen1_ppl\": 44.34, \"gen1_rankme\": 292.46, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0193, \"gen1_corr\": -0.036, \"gen2_ppl\": 49.75, \"gen2_rankme\": 295.61, \"gen2_knn\": 0.988, \"gen2_rare\": 0.0143, \"gen2_corr\": -0.0315, \"gen3_ppl\": 49, \"gen3_rankme\": 295.28, \"gen3_knn\": 0.988, \"gen3_rare\": 0.0125, \"gen3_corr\": -0.0238, \"gen4_ppl\": 50.85, \"gen4_rankme\": 297.01, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0113, \"gen4_corr\": -0.0209, \"gen5_ppl\": 47.31, \"gen5_rankme\": 292.81, \"gen5_knn\": 0.988, \"gen5_rare\": 0.0104, \"gen5_corr\": -0.0207, \"gen6_ppl\": 44.78, \"gen6_rankme\": 293.42, \"gen6_knn\": 0.988, \"gen6_rare\": 0.0099, \"gen6_corr\": -0.029, \"gen7_ppl\": 43.2, \"gen7_rankme\": 291.38, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0096, \"gen7_corr\": -0.0391}}, \"phase2_seed123_remaining\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T10:05:23.998Z\", \"updated_at\": \"2026-05-13T15:41:50.802Z\", \"conclusion\": \"success\", \"metrics\": {\"uncurated\": {\"gen0\": {\"ppl\": 36.69, \"rankme\": 277.86, \"knn\": 0.988, \"rare\": 0.0293, \"corr\": -0.0222}, \"gen1\": {\"ppl\": 45.29, \"rankme\": 297.08, \"knn\": 0.988, \"rare\": 0.0192, \"corr\": -0.0554}, \"gen2\": {\"ppl\": 53.76, \"rankme\": 301.88, \"knn\": 0.988, \"rare\": 0.0137, \"corr\": -0.0448}, \"gen3\": {\"ppl\": 53.76, \"rankme\": 300.7, \"knn\": 0.988, \"rare\": 0.0116, \"corr\": -0.0365}, \"gen4\": {\"ppl\": 54.33, \"rankme\": 298.78, \"knn\": 0.988, \"rare\": 0.0107, \"corr\": -0.0471}, \"gen5\": {\"ppl\": 53, \"rankme\": 293.21, \"knn\": 0.988, \"rare\": 0.01, \"corr\": -0.037}, \"gen6\": {\"ppl\": 49.87, \"rankme\": 295.35, \"knn\": 0.988, \"rare\": 0.0101, \"corr\": -0.0477}, \"gen7\": {\"ppl\": 46.15, \"rankme\": 290.13, \"knn\": 0.988, \"rare\": 0.0093, \"corr\": -0.0755}}, \"rgds\": {\"gen0\": {\"ppl\": 36.71, \"rankme\": 272.68, \"knn\": 0.988, \"rare\": 0.0293, \"corr\": -0.0116, \"ratio\": 0.9997}, \"gen1\": {\"ppl\": 42.81, \"rankme\": 286.96, \"knn\": 0.988, \"rare\": 0.0186, \"corr\": -0.0544, \"ratio\": 0.9066}, \"gen2\": {\"ppl\": 47.35, \"rankme\": 291.31, \"knn\": 0.988, \"rare\": 0.0142, \"corr\": -0.0569, \"ratio\": 0.8604}, \"gen3\": {\"ppl\": 52.64, \"rankme\": 295.72, \"knn\": 0.988, \"rare\": 0.0119, \"corr\": -0.0185, \"ratio\": 0.8689}, \"gen4\": {\"ppl\": 52.74, \"rankme\": 294.9, \"knn\": 0.988, \"rare\": 0.0101, \"corr\": -0.0042, \"ratio\": 0.8863}, \"gen5\": {\"ppl\": 60.62, \"rankme\": 294.93, \"knn\": 0.988, \"rare\": 0.0087, \"corr\": -0.0036, \"ratio\": 0.7809}, \"gen6\": {\"ppl\": 75.03, \"rankme\": 299.36, \"knn\": 0.988, \"rare\": 0.007, \"corr\": -0.0119, \"ratio\": 0.6789}, \"gen7\": {\"ppl\": 81.57, \"rankme\": 298.35, \"knn\": 0.988, \"rare\": 0.0062, \"corr\": -0.0312, \"ratio\": 0.5236}}}}, \"phase2_random50_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:29:42.169Z\", \"updated_at\": \"2026-05-13T15:19:47.746Z\", \"hypothesis\": \"Random 50% baseline: 与 RGDS/external_only 相同的 50% 数据预算但随机选择，验证 diversity-aware selection 相比随机选择的增益\", \"parent\": \"phase2_3method_selfit\", \"conclusion\": \"failed\"}}, \"count\": 20, \"total\": 31, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2369}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "c82a1d12-e6e8-4ef2-9a65-a1d2380c8a1e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"medium_uncurated_seed456\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-14T03:21:27.986Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:35:39.375Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) Uncurated seed=456: 3-seed 统计检验，验证 355M collapse 跨 seed 一致性\\\", \\\"parent\\\": \\\"medium_uncurated_seed42\\\"}, \\\"medium_random50_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:56:03.403Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:34:19.307Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) Random 50% seed=123: 2-seed 统计检验依赖，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致\\\", \\\"parent\\\": \\\"medium_random50_seed42\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.31, \\\"rankme\\\": 363.28, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.0343, \\\"rank_corr\\\": 0.019}, \\\"gen1\\\": {\\\"ppl\\\": 33.54, \\\"rankme\\\": 399.19, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.0298, \\\"rank_corr\\\": 0.013}, \\\"gen2\\\": {\\\"ppl\\\": 43.31, \\\"rankme\\\": 417.48, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.0224, \\\"rank_corr\\\": 0.008}, \\\"gen3\\\": {\\\"ppl\\\": 50.01, \\\"rankme\\\": 423.83, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.0187, \\\"rank_corr\\\": -0.013}, \\\"gen4\\\": {\\\"ppl\\\": 56.82, \\\"rankme\\\": 425.56, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.016, \\\"rank_corr\\\": -0.034}, \\\"gen5\\\": {\\\"ppl\\\": 65.35, \\\"rankme\\\": 426.7, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.0154, \\\"rank_corr\\\": -0.053}, \\\"gen6\\\": {\\\"ppl\\\": 70.43, \\\"rankme\\\": 421.46, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.014, \\\"rank_corr\\\": -0.047}, \\\"gen7\\\": {\\\"ppl\\\": 72.55, \\\"rankme\\\": 421.96, \\\"knn\\\": 0.988, \\\"rare_ngram\\\": 0.0131, \\\"rank_corr\\\": -0.049}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"medium_rgds_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:56:02.314Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:29:35.117Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) RGDS seed=123: 2-seed 统计检验依赖，验证 alignment gap 加速崩塌在 355M 跨 seed 一致\\\", \\\"parent\\\": \\\"medium_rgds_seed42\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.32, \\\"rankme\\\": 365.65, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0343, \\\"corr\\\": 0.0301, \\\"ratio\\\": 0.9623}, \\\"gen1\\\": {\\\"ppl\\\": 33.72, \\\"rankme\\\": 396.58, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0285, \\\"corr\\\": 0.0135, \\\"ratio\\\": 0.8893}, \\\"gen2\\\": {\\\"ppl\\\": 43.58, \\\"rankme\\\": 416.12, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0224, \\\"corr\\\": 0.0148, \\\"ratio\\\": 0.9445}, \\\"gen3\\\": {\\\"ppl\\\": 51.8, \\\"rankme\\\": 422.63, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0194, \\\"corr\\\": -0.0004, \\\"ratio\\\": 0.8469}, \\\"gen4\\\": {\\\"ppl\\\": 57.08, \\\"rankme\\\": 422.85, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0183, \\\"corr\\\": -0.0109, \\\"ratio\\\": 0.9441}, \\\"gen5\\\": {\\\"ppl\\\": 69.28, \\\"rankme\\\": 426.34, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0171, \\\"corr\\\": -0.0089, \\\"ratio\\\": 0.8997}, \\\"gen6\\\": {\\\"ppl\\\": 77.57, \\\"rankme\\\": 428.93, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0162, \\\"corr\\\": -0.0274, \\\"ratio\\\": 0.9364}, \\\"gen7\\\": {\\\"ppl\\\": 90.25, \\\"rankme\\\": 431.19, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0149, \\\"corr\\\": -0.017, \\\"ratio\\\": 0.8728}}}, \\\"medium_uncurated_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:55:48.455Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:29:31.269Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) Uncurated baseline seed=123: 2-seed 统计检验依赖，验证 355M collapse 严重度跨 seed 一致\\\", \\\"parent\\\": \\\"medium_uncurated_seed42\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.48, \\\"rankme\\\": 368.37, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0343, \\\"corr\\\": 0.0407}, \\\"gen1\\\": {\\\"ppl\\\": 35.54, \\\"rankme\\\": 402.99, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0286, \\\"corr\\\": 0.0311}, \\\"gen2\\\": {\\\"ppl\\\": 48.53, \\\"rankme\\\": 421.72, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0218, \\\"corr\\\": 0.0264}, \\\"gen3\\\": {\\\"ppl\\\": 61.54, \\\"rankme\\\": 434.05, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0185, \\\"corr\\\": 0.0021}, \\\"gen4\\\": {\\\"ppl\\\": 69.38, \\\"rankme\\\": 438.69, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0169, \\\"corr\\\": -0.0367}, \\\"gen5\\\": {\\\"ppl\\\": 76.22, \\\"rankme\\\": 438.77, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0154, \\\"corr\\\": -0.0375}, \\\"gen6\\\": {\\\"ppl\\\": 83.35, \\\"rankme\\\": 437.49, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0145, \\\"corr\\\": -0.0391}, \\\"gen7\\\": {\\\"ppl\\\": 87.05, \\\"rankme\\\": 436.04, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0136, \\\"corr\\\": -0.0375}}}, \\\"medium_external_seed456\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-14T03:21:29.786Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:13:53.442Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) External-only seed=456: 3-seed 统计检验，验证 frozen embeddings 在 355M 跨 seed 避免 alignment gap\\\", \\\"parent\\\": \\\"medium_external_seed42\\\"}, \\\"medium_external_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:56:03.780Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:49:14.249Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) External-only seed=123: 2-seed 统计检验依赖，验证 frozen Contriever embeddings 在 355M 跨 seed 仍避免 alignment gap\\\", \\\"parent\\\": \\\"medium_external_seed42\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.3, \\\"rankme\\\": 366.16, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0343, \\\"corr\\\": 0.0119}, \\\"gen1\\\": {\\\"ppl\\\": 33.62, \\\"rankme\\\": 400.2, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0303, \\\"corr\\\": 0.0077}, \\\"gen2\\\": {\\\"ppl\\\": 44.51, \\\"rankme\\\": 417.58, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0246, \\\"corr\\\": -0.0114}, \\\"gen3\\\": {\\\"ppl\\\": 51.18, \\\"rankme\\\": 421.73, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0206, \\\"corr\\\": -0.014}, \\\"gen4\\\": {\\\"ppl\\\": 61.11, \\\"rankme\\\": 427.42, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0184, \\\"corr\\\": -0.0282}, \\\"gen5\\\": {\\\"ppl\\\": 69.58, \\\"rankme\\\": 429.36, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0172, \\\"corr\\\": -0.0232}, \\\"gen6\\\": {\\\"ppl\\\": 74.33, \\\"rankme\\\": 428.14, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0168, \\\"corr\\\": -0.0458}, \\\"gen7\\\": {\\\"ppl\\\": 79.56, \\\"rankme\\\": 429.83, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0161, \\\"corr\\\": -0.0533, \\\"ratio\\\": 1.222}}}, \\\"medium_random50_seed456\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T03:21:29.247Z\\\", \\\"updated_at\\\": \\\"2026-05-14T03:22:00.608Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) Random 50% seed=456: 3-seed 统计检验，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致\\\", \\\"parent\\\": \\\"medium_random50_seed42\\\"}, \\\"medium_rgds_seed456\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T03:21:28.342Z\\\", \\\"updated_at\\\": \\\"2026-05-14T03:21:59.635Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) RGDS seed=456: 3-seed 统计检验，验证 alignment gap 在 355M 跨 seed 一致\\\", \\\"parent\\\": \\\"medium_rgds_seed42\\\"}, \\\"medium_external_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T23:32:08.840Z\\\", \\\"updated_at\\\": \\\"2026-05-14T03:11:09.334Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) External-only diversity selection: 验证 frozen Contriever embeddings 在更大模型上是否仍能避免 alignment gap（model scaling + external embedding interaction）\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen7_ppl\\\": 77.74, \\\"gen7_rankme\\\": 421.5, \\\"gen7_knn\\\": 0.988, \\\"gen7_rare_ngram\\\": 0.0165, \\\"gen7_rank_corr\\\": -0.0072, \\\"gen0_ppl\\\": 26.33, \\\"gen0_rankme\\\": 363.43, \\\"ppl_increase_ratio\\\": 2.95, \\\"rankme_increase\\\": 58.07}}, \\\"medium_random50_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:01:02.034Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:53:02.738Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) Random 50% baseline: 验证同 budget 随机选择在更大模型上的表现，作为 RGDS alignment gap 在 355M scale 的关键对照组\\\", \\\"parent\\\": \\\"medium_rgds_seed42\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.12, \\\"rankme\\\": 361.63, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0346, \\\"corr\\\": 0.0101}, \\\"gen1\\\": {\\\"ppl\\\": 32.57, \\\"rankme\\\": 387.8, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0277, \\\"corr\\\": 0.0331}, \\\"gen2\\\": {\\\"ppl\\\": 41.58, \\\"rankme\\\": 410.08, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0214, \\\"corr\\\": 0.0088}, \\\"gen3\\\": {\\\"ppl\\\": 49.87, \\\"rankme\\\": 421.67, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0182, \\\"corr\\\": -0.0018}, \\\"gen4\\\": {\\\"ppl\\\": 59.83, \\\"rankme\\\": 427.23, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0161, \\\"corr\\\": -0.0014}, \\\"gen5\\\": {\\\"ppl\\\": 60.62, \\\"rankme\\\": 426.16, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0144, \\\"corr\\\": -0.0004}, \\\"gen6\\\": {\\\"ppl\\\": 68.34, \\\"rankme\\\": 427.19, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0134, \\\"corr\\\": -0.0071}, \\\"gen7\\\": {\\\"ppl\\\": 70.25, \\\"rankme\\\": 426.5, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0128, \\\"corr\\\": -0.0034}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"medium_rgds_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T21:37:18.001Z\\\", \\\"updated_at\\\": \\\"2026-05-14T00:53:34.267Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) RGDS diversity selection: 验证 alignment gap 加速崩塌在更大模型上是否复现（model scaling + method interaction）\\\", \\\"parent\\\": \\\"medium_uncurated_seed42\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.04, \\\"rankme\\\": 365.07, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0346, \\\"corr\\\": 0.0196, \\\"ratio\\\": 0.9759}, \\\"gen1\\\": {\\\"ppl\\\": 32.99, \\\"rankme\\\": 398.29, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0286, \\\"corr\\\": 0.0402, \\\"ratio\\\": 0.9991}, \\\"gen2\\\": {\\\"ppl\\\": 41.99, \\\"rankme\\\": 418.21, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0232, \\\"corr\\\": 0.0014, \\\"ratio\\\": 0.9225}, \\\"gen3\\\": {\\\"ppl\\\": 50.8, \\\"rankme\\\": 421.44, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0198, \\\"corr\\\": 0.0058, \\\"ratio\\\": 0.9127}, \\\"gen4\\\": {\\\"ppl\\\": 60.71, \\\"rankme\\\": 425.62, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0187, \\\"corr\\\": -0.0068, \\\"ratio\\\": 0.7989}, \\\"gen5\\\": {\\\"ppl\\\": 66.29, \\\"rankme\\\": 424.71, \\\"knn\\\": 0.988, \\\"rare\\\": 0.018, \\\"corr\\\": -0.0235, \\\"ratio\\\": 0.9002}, \\\"gen6\\\": {\\\"ppl\\\": 72, \\\"rankme\\\": 423.93, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0168, \\\"corr\\\": -0.0197, \\\"ratio\\\": 0.7622}, \\\"gen7\\\": {\\\"ppl\\\": 82.84, \\\"rankme\\\": 424.72, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0166, \\\"corr\\\": -0.0286, \\\"ratio\\\": 0.8313}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"rgds_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:44:56.404Z\\\", \\\"updated_at\\\": \\\"2026-05-13T23:32:22.643Z\\\", \\\"hypothesis\\\": \\\"RGDS (50% internal embedding selection) seed=456 复现：3-seed 统计检验依赖，验证 RGDS alignment gap 加速崩塌跨 seed 一致\\\", \\\"parent\\\": \\\"phase2_3method_selfit\\\", \\\"metrics\\\": {\\\"gen0_ppl\\\": 36.7, \\\"gen0_rankme\\\": 274.06, \\\"gen0_knn\\\": 0.988, \\\"gen0_rare\\\": 0.0284, \\\"gen0_corr\\\": -0.0138, \\\"gen0_ratio\\\": 0.9114, \\\"gen1_ppl\\\": 44.59, \\\"gen1_rankme\\\": 291.76, \\\"gen1_knn\\\": 0.988, \\\"gen1_rare\\\": 0.0189, \\\"gen1_corr\\\": -0.0418, \\\"gen1_ratio\\\": 0.8895, \\\"gen2_ppl\\\": 45.3, \\\"gen2_rankme\\\": 290.79, \\\"gen2_knn\\\": 0.988, \\\"gen2_rare\\\": 0.0139, \\\"gen2_corr\\\": -0.0356, \\\"gen2_ratio\\\": 0.9071, \\\"gen3_ppl\\\": 49.13, \\\"gen3_rankme\\\": 289.92, \\\"gen3_knn\\\": 0.988, \\\"gen3_rare\\\": 0.0111, \\\"gen3_corr\\\": -0.0403, \\\"gen3_ratio\\\": 0.8774, \\\"gen4_ppl\\\": 47.4, \\\"gen4_rankme\\\": 287.04, \\\"gen4_knn\\\": 0.988, \\\"gen4_rare\\\": 0.0098, \\\"gen4_corr\\\": -0.0342, \\\"gen4_ratio\\\": 0.8292, \\\"gen5_ppl\\\": 55.99, \\\"gen5_rankme\\\": 290.71, \\\"gen5_knn\\\": 0.988, \\\"gen5_rare\\\": 0.0078, \\\"gen5_corr\\\": -0.0269, \\\"gen5_ratio\\\": 0.7065, \\\"gen6_ppl\\\": 55.99, \\\"gen6_rankme\\\": 287.52, \\\"gen6_knn\\\": 0.988, \\\"gen6_rare\\\": 0.0065, \\\"gen6_corr\\\": -0.0247, \\\"gen6_ratio\\\": 0.6447, \\\"gen7_ppl\\\": 66.22, \\\"gen7_rankme\\\": 286.54, \\\"gen7_knn\\\": 0.988, \\\"gen7_rare\\\": 0.0069, \\\"gen7_corr\\\": -0.0228, \\\"gen7_ratio\\\": 0.8682}, \\\"conclusion\\\": \\\"success\\\"}, \\\"ext_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:44:57.069Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:47:35.556Z\\\", \\\"hypothesis\\\": \\\"External_only (50% Contriever frozen embedding) seed=456 复现：3-seed 统计检验依赖，验证 external_only 免疫 alignment gap 跨 seed 一致\\\", \\\"parent\\\": \\\"phase2_ext_seed123\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_ppl\\\": 36.51, \\\"gen0_rankme\\\": 273.85, \\\"gen0_knn\\\": 0.988, \\\"gen0_rare\\\": 0.0284, \\\"gen0_corr\\\": -0.0103, \\\"gen0_ratio\\\": 1.1621, \\\"gen1_ppl\\\": 44.77, \\\"gen1_rankme\\\": 291.93, \\\"gen1_knn\\\": 0.988, \\\"gen1_rare\\\": 0.0203, \\\"gen1_corr\\\": -0.0404, \\\"gen1_ratio\\\": 1.0686, \\\"gen2_ppl\\\": 50.84, \\\"gen2_rankme\\\": 298.52, \\\"gen2_knn\\\": 0.987, \\\"gen2_rare\\\": 0.0152, \\\"gen2_corr\\\": -0.0292, \\\"gen2_ratio\\\": 1.1119, \\\"gen3_ppl\\\": 54.43, \\\"gen3_rankme\\\": 298.35, \\\"gen3_knn\\\": 0.987, \\\"gen3_rare\\\": 0.013, \\\"gen3_corr\\\": -0.0223, \\\"gen3_ratio\\\": 1.1551, \\\"gen4_ppl\\\": 49.91, \\\"gen4_rankme\\\": 295.86, \\\"gen4_knn\\\": 0.988, \\\"gen4_rare\\\": 0.0118, \\\"gen4_corr\\\": -0.0321, \\\"gen4_ratio\\\": 1.1841, \\\"gen5_ppl\\\": 50.45, \\\"gen5_rankme\\\": 297.37, \\\"gen5_knn\\\": 0.988, \\\"gen5_rare\\\": 0.0111, \\\"gen5_corr\\\": -0.03, \\\"gen5_ratio\\\": 1.2186, \\\"gen6_ppl\\\": 47.09, \\\"gen6_rankme\\\": 294.35, \\\"gen6_knn\\\": 0.988, \\\"gen6_rare\\\": 0.01, \\\"gen6_corr\\\": -0.0207, \\\"gen6_ratio\\\": 1.0818, \\\"gen7_ppl\\\": 43.9, \\\"gen7_rankme\\\": 292.69, \\\"gen7_knn\\\": 0.988, \\\"gen7_rare\\\": 0.0106, \\\"gen7_corr\\\": -0.0227, \\\"gen7_ratio\\\": 1.243}}, \\\"medium_uncurated_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T19:20:55.822Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:42:26.811Z\\\", \\\"hypothesis\\\": \\\"GPT2-medium (355M) uncurated baseline: 验证 alignment gap 现象在更大模型上是否复现（model scaling 维度）\\\", \\\"parent\\\": \\\"phase2_3method_selfit\\\", \\\"metrics\\\": {\\\"gen0_ppl\\\": 26.55, \\\"gen0_rankme\\\": 371.57, \\\"gen0_knn\\\": 0.988, \\\"gen0_rare\\\": 0.0346, \\\"gen0_corr\\\": 0.0219, \\\"gen1_ppl\\\": 35.12, \\\"gen1_rankme\\\": 403.8, \\\"gen1_knn\\\": 0.988, \\\"gen1_rare\\\": 0.0281, \\\"gen1_corr\\\": 0.0228, \\\"gen2_ppl\\\": 46.9, \\\"gen2_rankme\\\": 420.83, \\\"gen2_knn\\\": 0.988, \\\"gen2_rare\\\": 0.0216, \\\"gen2_corr\\\": 0.0181, \\\"gen3_ppl\\\": 57.4, \\\"gen3_rankme\\\": 425.35, \\\"gen3_knn\\\": 0.988, \\\"gen3_rare\\\": 0.0185, \\\"gen3_corr\\\": 0.0011, \\\"gen4_ppl\\\": 67.45, \\\"gen4_rankme\\\": 430.68, \\\"gen4_knn\\\": 0.988, \\\"gen4_rare\\\": 0.0172, \\\"gen4_corr\\\": -0.0046, \\\"gen5_ppl\\\": 78.55, \\\"gen5_rankme\\\": 438.62, \\\"gen5_knn\\\": 0.987, \\\"gen5_rare\\\": 0.0159, \\\"gen5_corr\\\": -0.0175, \\\"gen6_ppl\\\": 84.59, \\\"gen6_rankme\\\": 442.85, \\\"gen6_knn\\\": 0.987, \\\"gen6_rare\\\": 0.0144, \\\"gen6_corr\\\": -0.0462, \\\"gen7_ppl\\\": 91.66, \\\"gen7_rankme\\\": 443.98, \\\"gen7_knn\\\": 0.988, \\\"gen7_rare\\\": 0.0139, \\\"gen7_corr\\\": -0.0379}, \\\"conclusion\\\": \\\"success\\\"}, \\\"uncurated_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:44:55.468Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:28:12.126Z\\\", \\\"hypothesis\\\": \\\"Uncurated (100% data) seed=456 复现：3-seed 统计检验依赖，验证 uncurated 的 PPL/rare 轨迹跨 seed 一致性\\\", \\\"parent\\\": \\\"phase2_3method_selfit\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_ppl\\\": 36.64, \\\"gen0_rankme\\\": 279.17, \\\"gen0_knn\\\": 0.988, \\\"gen0_rare\\\": 0.0284, \\\"gen0_corr\\\": -0.0205, \\\"gen7_ppl\\\": 44.69, \\\"gen7_rankme\\\": 287.93, \\\"gen7_knn\\\": 0.988, \\\"gen7_rare\\\": 0.0086, \\\"gen7_corr\\\": -0.0696}}, \\\"random_50_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:01:32.779Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:01:00.100Z\\\", \\\"hypothesis\\\": \\\"Random 50% seed=456 复现：与 phase2_random50_v2 (seed=42) 完全一致的超参数，验证 random≈external 是否跨 seed 成立（C2-revised + C3 验证，3-seed t 检验依赖）\\\", \\\"parent\\\": \\\"phase2_random50_v2\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen7_ppl\\\": 44.6, \\\"gen7_rare\\\": 0.0101, \\\"gen7_rankme\\\": 289.87}}, \\\"random_50_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:01:31.859Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:00:59.367Z\\\", \\\"hypothesis\\\": \\\"Random 50% seed=123 复现：与 phase2_random50_v2 (seed=42) 完全一致的超参数，验证 random≈external 是否跨 seed 成立（C2-revised + C3 验证，3-seed t 检验依赖）\\\", \\\"parent\\\": \\\"phase2_random50_v2\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen7_ppl\\\": 41.75, \\\"gen7_rare\\\": 0.0098, \\\"gen7_rankme\\\": 291.7}}, \\\"phase2_random50_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T11:46:06.927Z\\\", \\\"updated_at\\\": \\\"2026-05-13T16:01:33.541Z\\\", \\\"hypothesis\\\": \\\"Random 50% baseline v2: 与 Phase 2 对照组完全一致的超参数(lr=5e-5, epochs=3, 500K tokens/gen)，随机选择 50% 数据，验证 diversity-aware selection 相比随机选择的增益\\\", \\\"parent\\\": \\\"phase2_3method_selfit\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_ppl\\\": 36.87, \\\"gen0_rankme\\\": 275.24, \\\"gen0_knn\\\": 0.988, \\\"gen0_rare\\\": 0.029, \\\"gen0_corr\\\": -0.0081, \\\"gen1_ppl\\\": 44.34, \\\"gen1_rankme\\\": 292.46, \\\"gen1_knn\\\": 0.988, \\\"gen1_rare\\\": 0.0193, \\\"gen1_corr\\\": -0.036, \\\"gen2_ppl\\\": 49.75, \\\"gen2_rankme\\\": 295.61, \\\"gen2_knn\\\": 0.988, \\\"gen2_rare\\\": 0.0143, \\\"gen2_corr\\\": -0.0315, \\\"gen3_ppl\\\": 49, \\\"gen3_rankme\\\": 295.28, \\\"gen3_knn\\\": 0.988, \\\"gen3_rare\\\": 0.0125, \\\"gen3_corr\\\": -0.0238, \\\"gen4_ppl\\\": 50.85, \\\"gen4_rankme\\\": 297.01, \\\"gen4_knn\\\": 0.988, \\\"gen4_rare\\\": 0.0113, \\\"gen4_corr\\\": -0.0209, \\\"gen5_ppl\\\": 47.31, \\\"gen5_rankme\\\": 292.81, \\\"gen5_knn\\\": 0.988, \\\"gen5_rare\\\": 0.0104, \\\"gen5_corr\\\": -0.0207, \\\"gen6_ppl\\\": 44.78, \\\"gen6_rankme\\\": 293.42, \\\"gen6_knn\\\": 0.988, \\\"gen6_rare\\\": 0.0099, \\\"gen6_corr\\\": -0.029, \\\"gen7_ppl\\\": 43.2, \\\"gen7_rankme\\\": 291.38, \\\"gen7_knn\\\": 0.988, \\\"gen7_rare\\\": 0.0096, \\\"gen7_corr\\\": -0.0391}}, \\\"phase2_seed123_remaining\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T10:05:23.998Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:41:50.802Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"uncurated\\\": {\\\"gen0\\\": {\\\"ppl\\\": 36.69, \\\"rankme\\\": 277.86, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0293, \\\"corr\\\": -0.0222}, \\\"gen1\\\": {\\\"ppl\\\": 45.29, \\\"rankme\\\": 297.08, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0192, \\\"corr\\\": -0.0554}, \\\"gen2\\\": {\\\"ppl\\\": 53.76, \\\"rankme\\\": 301.88, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0137, \\\"corr\\\": -0.0448}, \\\"gen3\\\": {\\\"ppl\\\": 53.76, \\\"rankme\\\": 300.7, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0116, \\\"corr\\\": -0.0365}, \\\"gen4\\\": {\\\"ppl\\\": 54.33, \\\"rankme\\\": 298.78, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0107, \\\"corr\\\": -0.0471}, \\\"gen5\\\": {\\\"ppl\\\": 53, \\\"rankme\\\": 293.21, \\\"knn\\\": 0.988, \\\"rare\\\": 0.01, \\\"corr\\\": -0.037}, \\\"gen6\\\": {\\\"ppl\\\": 49.87, \\\"rankme\\\": 295.35, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0101, \\\"corr\\\": -0.0477}, \\\"gen7\\\": {\\\"ppl\\\": 46.15, \\\"rankme\\\": 290.13, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0093, \\\"corr\\\": -0.0755}}, \\\"rgds\\\": {\\\"gen0\\\": {\\\"ppl\\\": 36.71, \\\"rankme\\\": 272.68, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0293, \\\"corr\\\": -0.0116, \\\"ratio\\\": 0.9997}, \\\"gen1\\\": {\\\"ppl\\\": 42.81, \\\"rankme\\\": 286.96, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0186, \\\"corr\\\": -0.0544, \\\"ratio\\\": 0.9066}, \\\"gen2\\\": {\\\"ppl\\\": 47.35, \\\"rankme\\\": 291.31, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0142, \\\"corr\\\": -0.0569, \\\"ratio\\\": 0.8604}, \\\"gen3\\\": {\\\"ppl\\\": 52.64, \\\"rankme\\\": 295.72, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0119, \\\"corr\\\": -0.0185, \\\"ratio\\\": 0.8689}, \\\"gen4\\\": {\\\"ppl\\\": 52.74, \\\"rankme\\\": 294.9, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0101, \\\"corr\\\": -0.0042, \\\"ratio\\\": 0.8863}, \\\"gen5\\\": {\\\"ppl\\\": 60.62, \\\"rankme\\\": 294.93, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0087, \\\"corr\\\": -0.0036, \\\"ratio\\\": 0.7809}, \\\"gen6\\\": {\\\"ppl\\\": 75.03, \\\"rankme\\\": 299.36, \\\"knn\\\": 0.988, \\\"rare\\\": 0.007, \\\"corr\\\": -0.0119, \\\"ratio\\\": 0.6789}, \\\"gen7\\\": {\\\"ppl\\\": 81.57, \\\"rankme\\\": 298.35, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0062, \\\"corr\\\": -0.0312, \\\"ratio\\\": 0.5236}}}}, \\\"phase2_random50_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T11:29:42.169Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:19:47.746Z\\\", \\\"hypothesis\\\": \\\"Random 50% baseline: 与 RGDS/external_only 相同的 50% 数据预算但随机选择，验证 diversity-aware selection 相比随机选择的增益\\\", \\\"parent\\\": \\\"phase2_3method_selfit\\\", \\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 20, \\\"total\\\": 31, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2369}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"medium_uncurated_seed456\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T03:21:27.986Z\", \"updated_at\": \"2026-05-14T08:35:39.375Z\", \"hypothesis\": \"GPT2-medium (355M) Uncurated seed=456: 3-seed 统计检验，验证 355M collapse 跨 seed 一致性\", \"parent\": \"medium_uncurated_seed42\"}, \"medium_random50_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:56:03.403Z\", \"updated_at\": \"2026-05-14T08:34:19.307Z\", \"hypothesis\": \"GPT2-medium (355M) Random 50% seed=123: 2-seed 统计检验依赖，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致\", \"parent\": \"medium_random50_seed42\", \"metrics\": {\"gen0\": {\"ppl\": 26.31, \"rankme\": 363.28, \"knn\": 0.988, \"rare_ngram\": 0.0343, \"rank_corr\": 0.019}, \"gen1\": {\"ppl\": 33.54, \"rankme\": 399.19, \"knn\": 0.988, \"rare_ngram\": 0.0298, \"rank_corr\": 0.013}, \"gen2\": {\"ppl\": 43.31, \"rankme\": 417.48, \"knn\": 0.988, \"rare_ngram\": 0.0224, \"rank_corr\": 0.008}, \"gen3\": {\"ppl\": 50.01, \"rankme\": 423.83, \"knn\": 0.988, \"rare_ngram\": 0.0187, \"rank_corr\": -0.013}, \"gen4\": {\"ppl\": 56.82, \"rankme\": 425.56, \"knn\": 0.988, \"rare_ngram\": 0.016, \"rank_corr\": -0.034}, \"gen5\": {\"ppl\": 65.35, \"rankme\": 426.7, \"knn\": 0.988, \"rare_ngram\": 0.0154, \"rank_corr\": -0.053}, \"gen6\": {\"ppl\": 70.43, \"rankme\": 421.46, \"knn\": 0.988, \"rare_ngram\": 0.014, \"rank_corr\": -0.047}, \"gen7\": {\"ppl\": 72.55, \"rankme\": 421.96, \"knn\": 0.988, \"rare_ngram\": 0.0131, \"rank_corr\": -0.049}}, \"conclusion\": \"success\"}, \"medium_rgds_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:56:02.314Z\", \"updated_at\": \"2026-05-14T07:29:35.117Z\", \"hypothesis\": \"GPT2-medium (355M) RGDS seed=123: 2-seed 统计检验依赖，验证 alignment gap 加速崩塌在 355M 跨 seed 一致\", \"parent\": \"medium_rgds_seed42\", \"conclusion\": \"success\", \"metrics\": {\"gen0\": {\"ppl\": 26.32, \"rankme\": 365.65, \"knn\": 0.988, \"rare\": 0.0343, \"corr\": 0.0301, \"ratio\": 0.9623}, \"gen1\": {\"ppl\": 33.72, \"rankme\": 396.58, \"knn\": 0.988, \"rare\": 0.0285, \"corr\": 0.0135, \"ratio\": 0.8893}, \"gen2\": {\"ppl\": 43.58, \"rankme\": 416.12, \"knn\": 0.988, \"rare\": 0.0224, \"corr\": 0.0148, \"ratio\": 0.9445}, \"gen3\": {\"ppl\": 51.8, \"rankme\": 422.63, \"knn\": 0.988, \"rare\": 0.0194, \"corr\": -0.0004, \"ratio\": 0.8469}, \"gen4\": {\"ppl\": 57.08, \"rankme\": 422.85, \"knn\": 0.988, \"rare\": 0.0183, \"corr\": -0.0109, \"ratio\": 0.9441}, \"gen5\": {\"ppl\": 69.28, \"rankme\": 426.34, \"knn\": 0.988, \"rare\": 0.0171, \"corr\": -0.0089, \"ratio\": 0.8997}, \"gen6\": {\"ppl\": 77.57, \"rankme\": 428.93, \"knn\": 0.988, \"rare\": 0.0162, \"corr\": -0.0274, \"ratio\": 0.9364}, \"gen7\": {\"ppl\": 90.25, \"rankme\": 431.19, \"knn\": 0.988, \"rare\": 0.0149, \"corr\": -0.017, \"ratio\": 0.8728}}}, \"medium_uncurated_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:55:48.455Z\", \"updated_at\": \"2026-05-14T07:29:31.269Z\", \"hypothesis\": \"GPT2-medium (355M) Uncurated baseline seed=123: 2-seed 统计检验依赖，验证 355M collapse 严重度跨 seed 一致\", \"parent\": \"medium_uncurated_seed42\", \"conclusion\": \"success\", \"metrics\": {\"gen0\": {\"ppl\": 26.48, \"rankme\": 368.37, \"knn\": 0.988, \"rare\": 0.0343, \"corr\": 0.0407}, \"gen1\": {\"ppl\": 35.54, \"rankme\": 402.99, \"knn\": 0.988, \"rare\": 0.0286, \"corr\": 0.0311}, \"gen2\": {\"ppl\": 48.53, \"rankme\": 421.72, \"knn\": 0.988, \"rare\": 0.0218, \"corr\": 0.0264}, \"gen3\": {\"ppl\": 61.54, \"rankme\": 434.05, \"knn\": 0.988, \"rare\": 0.0185, \"corr\": 0.0021}, \"gen4\": {\"ppl\": 69.38, \"rankme\": 438.69, \"knn\": 0.988, \"rare\": 0.0169, \"corr\": -0.0367}, \"gen5\": {\"ppl\": 76.22, \"rankme\": 438.77, \"knn\": 0.988, \"rare\": 0.0154, \"corr\": -0.0375}, \"gen6\": {\"ppl\": 83.35, \"rankme\": 437.49, \"knn\": 0.988, \"rare\": 0.0145, \"corr\": -0.0391}, \"gen7\": {\"ppl\": 87.05, \"rankme\": 436.04, \"knn\": 0.988, \"rare\": 0.0136, \"corr\": -0.0375}}}, \"medium_external_seed456\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T03:21:29.786Z\", \"updated_at\": \"2026-05-14T07:13:53.442Z\", \"hypothesis\": \"GPT2-medium (355M) External-only seed=456: 3-seed 统计检验，验证 frozen embeddings 在 355M 跨 seed 避免 alignment gap\", \"parent\": \"medium_external_seed42\"}, \"medium_external_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:56:03.780Z\", \"updated_at\": \"2026-05-14T06:49:14.249Z\", \"hypothesis\": \"GPT2-medium (355M) External-only seed=123: 2-seed 统计检验依赖，验证 frozen Contriever embeddings 在 355M 跨 seed 仍避免 alignment gap\", \"parent\": \"medium_external_seed42\", \"conclusion\": \"success\", \"metrics\": {\"gen0\": {\"ppl\": 26.3, \"rankme\": 366.16, \"knn\": 0.988, \"rare\": 0.0343, \"corr\": 0.0119}, \"gen1\": {\"ppl\": 33.62, \"rankme\": 400.2, \"knn\": 0.988, \"rare\": 0.0303, \"corr\": 0.0077}, \"gen2\": {\"ppl\": 44.51, \"rankme\": 417.58, \"knn\": 0.988, \"rare\": 0.0246, \"corr\": -0.0114}, \"gen3\": {\"ppl\": 51.18, \"rankme\": 421.73, \"knn\": 0.988, \"rare\": 0.0206, \"corr\": -0.014}, \"gen4\": {\"ppl\": 61.11, \"rankme\": 427.42, \"knn\": 0.988, \"rare\": 0.0184, \"corr\": -0.0282}, \"gen5\": {\"ppl\": 69.58, \"rankme\": 429.36, \"knn\": 0.988, \"rare\": 0.0172, \"corr\": -0.0232}, \"gen6\": {\"ppl\": 74.33, \"rankme\": 428.14, \"knn\": 0.988, \"rare\": 0.0168, \"corr\": -0.0458}, \"gen7\": {\"ppl\": 79.56, \"rankme\": 429.83, \"knn\": 0.988, \"rare\": 0.0161, \"corr\": -0.0533, \"ratio\": 1.222}}}, \"medium_random50_seed456\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T03:21:29.247Z\", \"updated_at\": \"2026-05-14T03:22:00.608Z\", \"hypothesis\": \"GPT2-medium (355M) Random 50% seed=456: 3-seed 统计检验，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致\", \"parent\": \"medium_random50_seed42\"}, \"medium_rgds_seed456\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T03:21:28.342Z\", \"updated_at\": \"2026-05-14T03:21:59.635Z\", \"hypothesis\": \"GPT2-medium (355M) RGDS seed=456: 3-seed 统计检验，验证 alignment gap 在 355M 跨 seed 一致\", \"parent\": \"medium_rgds_seed42\"}, \"medium_external_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:32:08.840Z\", \"updated_at\": \"2026-05-14T03:11:09.334Z\", \"hypothesis\": \"GPT2-medium (355M) External-only diversity selection: 验证 frozen Contriever embeddings 在更大模型上是否仍能避免 alignment gap（model scaling + external embedding interaction）\", \"conclusion\": \"success\", \"metrics\": {\"gen7_ppl\": 77.74, \"gen7_rankme\": 421.5, \"gen7_knn\": 0.988, \"gen7_rare_ngram\": 0.0165, \"gen7_rank_corr\": -0.0072, \"gen0_ppl\": 26.33, \"gen0_rankme\": 363.43, \"ppl_increase_ratio\": 2.95, \"rankme_increase\": 58.07}}, \"medium_random50_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:01:02.034Z\", \"updated_at\": \"2026-05-14T01:53:02.738Z\", \"hypothesis\": \"GPT2-medium (355M) Random 50% baseline: 验证同 budget 随机选择在更大模型上的表现，作为 RGDS alignment gap 在 355M scale 的关键对照组\", \"parent\": \"medium_rgds_seed42\", \"metrics\": {\"gen0\": {\"ppl\": 26.12, \"rankme\": 361.63, \"knn\": 0.988, \"rare\": 0.0346, \"corr\": 0.0101}, \"gen1\": {\"ppl\": 32.57, \"rankme\": 387.8, \"knn\": 0.988, \"rare\": 0.0277, \"corr\": 0.0331}, \"gen2\": {\"ppl\": 41.58, \"rankme\": 410.08, \"knn\": 0.988, \"rare\": 0.0214, \"corr\": 0.0088}, \"gen3\": {\"ppl\": 49.87, \"rankme\": 421.67, \"knn\": 0.988, \"rare\": 0.0182, \"corr\": -0.0018}, \"gen4\": {\"ppl\": 59.83, \"rankme\": 427.23, \"knn\": 0.988, \"rare\": 0.0161, \"corr\": -0.0014}, \"gen5\": {\"ppl\": 60.62, \"rankme\": 426.16, \"knn\": 0.988, \"rare\": 0.0144, \"corr\": -0.0004}, \"gen6\": {\"ppl\": 68.34, \"rankme\": 427.19, \"knn\": 0.988, \"rare\": 0.0134, \"corr\": -0.0071}, \"gen7\": {\"ppl\": 70.25, \"rankme\": 426.5, \"knn\": 0.988, \"rare\": 0.0128, \"corr\": -0.0034}}, \"conclusion\": \"success\"}, \"medium_rgds_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T21:37:18.001Z\", \"updated_at\": \"2026-05-14T00:53:34.267Z\", \"hypothesis\": \"GPT2-medium (355M) RGDS diversity selection: 验证 alignment gap 加速崩塌在更大模型上是否复现（model scaling + method interaction）\", \"parent\": \"medium_uncurated_seed42\", \"metrics\": {\"gen0\": {\"ppl\": 26.04, \"rankme\": 365.07, \"knn\": 0.988, \"rare\": 0.0346, \"corr\": 0.0196, \"ratio\": 0.9759}, \"gen1\": {\"ppl\": 32.99, \"rankme\": 398.29, \"knn\": 0.988, \"rare\": 0.0286, \"corr\": 0.0402, \"ratio\": 0.9991}, \"gen2\": {\"ppl\": 41.99, \"rankme\": 418.21, \"knn\": 0.988, \"rare\": 0.0232, \"corr\": 0.0014, \"ratio\": 0.9225}, \"gen3\": {\"ppl\": 50.8, \"rankme\": 421.44, \"knn\": 0.988, \"rare\": 0.0198, \"corr\": 0.0058, \"ratio\": 0.9127}, \"gen4\": {\"ppl\": 60.71, \"rankme\": 425.62, \"knn\": 0.988, \"rare\": 0.0187, \"corr\": -0.0068, \"ratio\": 0.7989}, \"gen5\": {\"ppl\": 66.29, \"rankme\": 424.71, \"knn\": 0.988, \"rare\": 0.018, \"corr\": -0.0235, \"ratio\": 0.9002}, \"gen6\": {\"ppl\": 72, \"rankme\": 423.93, \"knn\": 0.988, \"rare\": 0.0168, \"corr\": -0.0197, \"ratio\": 0.7622}, \"gen7\": {\"ppl\": 82.84, \"rankme\": 424.72, \"knn\": 0.988, \"rare\": 0.0166, \"corr\": -0.0286, \"ratio\": 0.8313}}, \"conclusion\": \"success\"}, \"rgds_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:44:56.404Z\", \"updated_at\": \"2026-05-13T23:32:22.643Z\", \"hypothesis\": \"RGDS (50% internal embedding selection) seed=456 复现：3-seed 统计检验依赖，验证 RGDS alignment gap 加速崩塌跨 seed 一致\", \"parent\": \"phase2_3method_selfit\", \"metrics\": {\"gen0_ppl\": 36.7, \"gen0_rankme\": 274.06, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0284, \"gen0_corr\": -0.0138, \"gen0_ratio\": 0.9114, \"gen1_ppl\": 44.59, \"gen1_rankme\": 291.76, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0189, \"gen1_corr\": -0.0418, \"gen1_ratio\": 0.8895, \"gen2_ppl\": 45.3, \"gen2_rankme\": 290.79, \"gen2_knn\": 0.988, \"gen2_rare\": 0.0139, \"gen2_corr\": -0.0356, \"gen2_ratio\": 0.9071, \"gen3_ppl\": 49.13, \"gen3_rankme\": 289.92, \"gen3_knn\": 0.988, \"gen3_rare\": 0.0111, \"gen3_corr\": -0.0403, \"gen3_ratio\": 0.8774, \"gen4_ppl\": 47.4, \"gen4_rankme\": 287.04, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0098, \"gen4_corr\": -0.0342, \"gen4_ratio\": 0.8292, \"gen5_ppl\": 55.99, \"gen5_rankme\": 290.71, \"gen5_knn\": 0.988, \"gen5_rare\": 0.0078, \"gen5_corr\": -0.0269, \"gen5_ratio\": 0.7065, \"gen6_ppl\": 55.99, \"gen6_rankme\": 287.52, \"gen6_knn\": 0.988, \"gen6_rare\": 0.0065, \"gen6_corr\": -0.0247, \"gen6_ratio\": 0.6447, \"gen7_ppl\": 66.22, \"gen7_rankme\": 286.54, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0069, \"gen7_corr\": -0.0228, \"gen7_ratio\": 0.8682}, \"conclusion\": \"success\"}, \"ext_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:44:57.069Z\", \"updated_at\": \"2026-05-13T21:47:35.556Z\", \"hypothesis\": \"External_only (50% Contriever frozen embedding) seed=456 复现：3-seed 统计检验依赖，验证 external_only 免疫 alignment gap 跨 seed 一致\", \"parent\": \"phase2_ext_seed123\", \"conclusion\": \"success\", \"metrics\": {\"gen0_ppl\": 36.51, \"gen0_rankme\": 273.85, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0284, \"gen0_corr\": -0.0103, \"gen0_ratio\": 1.1621, \"gen1_ppl\": 44.77, \"gen1_rankme\": 291.93, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0203, \"gen1_corr\": -0.0404, \"gen1_ratio\": 1.0686, \"gen2_ppl\": 50.84, \"gen2_rankme\": 298.52, \"gen2_knn\": 0.987, \"gen2_rare\": 0.0152, \"gen2_corr\": -0.0292, \"gen2_ratio\": 1.1119, \"gen3_ppl\": 54.43, \"gen3_rankme\": 298.35, \"gen3_knn\": 0.987, \"gen3_rare\": 0.013, \"gen3_corr\": -0.0223, \"gen3_ratio\": 1.1551, \"gen4_ppl\": 49.91, \"gen4_rankme\": 295.86, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0118, \"gen4_corr\": -0.0321, \"gen4_ratio\": 1.1841, \"gen5_ppl\": 50.45, \"gen5_rankme\": 297.37, \"gen5_knn\": 0.988, \"gen5_rare\": 0.0111, \"gen5_corr\": -0.03, \"gen5_ratio\": 1.2186, \"gen6_ppl\": 47.09, \"gen6_rankme\": 294.35, \"gen6_knn\": 0.988, \"gen6_rare\": 0.01, \"gen6_corr\": -0.0207, \"gen6_ratio\": 1.0818, \"gen7_ppl\": 43.9, \"gen7_rankme\": 292.69, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0106, \"gen7_corr\": -0.0227, \"gen7_ratio\": 1.243}}, \"medium_uncurated_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:20:55.822Z\", \"updated_at\": \"2026-05-13T21:42:26.811Z\", \"hypothesis\": \"GPT2-medium (355M) uncurated baseline: 验证 alignment gap 现象在更大模型上是否复现（model scaling 维度）\", \"parent\": \"phase2_3method_selfit\", \"metrics\": {\"gen0_ppl\": 26.55, \"gen0_rankme\": 371.57, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0346, \"gen0_corr\": 0.0219, \"gen1_ppl\": 35.12, \"gen1_rankme\": 403.8, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0281, \"gen1_corr\": 0.0228, \"gen2_ppl\": 46.9, \"gen2_rankme\": 420.83, \"gen2_knn\": 0.988, \"gen2_rare\": 0.0216, \"gen2_corr\": 0.0181, \"gen3_ppl\": 57.4, \"gen3_rankme\": 425.35, \"gen3_knn\": 0.988, \"gen3_rare\": 0.0185, \"gen3_corr\": 0.0011, \"gen4_ppl\": 67.45, \"gen4_rankme\": 430.68, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0172, \"gen4_corr\": -0.0046, \"gen5_ppl\": 78.55, \"gen5_rankme\": 438.62, \"gen5_knn\": 0.987, \"gen5_rare\": 0.0159, \"gen5_corr\": -0.0175, \"gen6_ppl\": 84.59, \"gen6_rankme\": 442.85, \"gen6_knn\": 0.987, \"gen6_rare\": 0.0144, \"gen6_corr\": -0.0462, \"gen7_ppl\": 91.66, \"gen7_rankme\": 443.98, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0139, \"gen7_corr\": -0.0379}, \"conclusion\": \"success\"}, \"uncurated_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:44:55.468Z\", \"updated_at\": \"2026-05-13T19:28:12.126Z\", \"hypothesis\": \"Uncurated (100% data) seed=456 复现：3-seed 统计检验依赖，验证 uncurated 的 PPL/rare 轨迹跨 seed 一致性\", \"parent\": \"phase2_3method_selfit\", \"conclusion\": \"success\", \"metrics\": {\"gen0_ppl\": 36.64, \"gen0_rankme\": 279.17, \"gen0_knn\": 0.988, \"gen0_rare\": 0.0284, \"gen0_corr\": -0.0205, \"gen7_ppl\": 44.69, \"gen7_rankme\": 287.93, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0086, \"gen7_corr\": -0.0696}}, \"random_50_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:01:32.779Z\", \"updated_at\": \"2026-05-13T19:01:00.100Z\", \"hypothesis\": \"Random 50% seed=456 复现：与 phase2_random50_v2 (seed=42) 完全一致的超参数，验证 random≈external 是否跨 seed 成立（C2-revised + C3 验证，3-seed t 检验依赖）\", \"parent\": \"phase2_random50_v2\", \"conclusion\": \"success\", \"metrics\": {\"gen7_ppl\": 44.6, \"gen7_rare\": 0.0101, \"gen7_rankme\": 289.87}}, \"random_50_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:01:31.859Z\", \"updated_at\": \"2026-05-13T19:00:59.367Z\", \"hypothesis\": \"Random 50% seed=123 复现：与 phase2_random50_v2 (seed=42) 完全一致的超参数，验证 random≈external 是否跨 seed 成立（C2-revised + C3 验证，3-seed t 检验依赖）\", \"parent\": \"phase2_random50_v2\", \"conclusion\": \"success\", \"metrics\": {\"gen7_ppl\": 41.75, \"gen7_rare\": 0.0098, \"gen7_rankme\": 291.7}}, \"phase2_random50_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:46:06.927Z\", \"updated_at\": \"2026-05-13T16:01:33.541Z\", \"hypothesis\": \"Random 50% baseline v2: 与 Phase 2 对照组完全一致的超参数(lr=5e-5, epochs=3, 500K tokens/gen)，随机选择 50% 数据，验证 diversity-aware selection 相比随机选择的增益\", \"parent\": \"phase2_3method_selfit\", \"conclusion\": \"success\", \"metrics\": {\"gen0_ppl\": 36.87, \"gen0_rankme\": 275.24, \"gen0_knn\": 0.988, \"gen0_rare\": 0.029, \"gen0_corr\": -0.0081, \"gen1_ppl\": 44.34, \"gen1_rankme\": 292.46, \"gen1_knn\": 0.988, \"gen1_rare\": 0.0193, \"gen1_corr\": -0.036, \"gen2_ppl\": 49.75, \"gen2_rankme\": 295.61, \"gen2_knn\": 0.988, \"gen2_rare\": 0.0143, \"gen2_corr\": -0.0315, \"gen3_ppl\": 49, \"gen3_rankme\": 295.28, \"gen3_knn\": 0.988, \"gen3_rare\": 0.0125, \"gen3_corr\": -0.0238, \"gen4_ppl\": 50.85, \"gen4_rankme\": 297.01, \"gen4_knn\": 0.988, \"gen4_rare\": 0.0113, \"gen4_corr\": -0.0209, \"gen5_ppl\": 47.31, \"gen5_rankme\": 292.81, \"gen5_knn\": 0.988, \"gen5_rare\": 0.0104, \"gen5_corr\": -0.0207, \"gen6_ppl\": 44.78, \"gen6_rankme\": 293.42, \"gen6_knn\": 0.988, \"gen6_rare\": 0.0099, \"gen6_corr\": -0.029, \"gen7_ppl\": 43.2, \"gen7_rankme\": 291.38, \"gen7_knn\": 0.988, \"gen7_rare\": 0.0096, \"gen7_corr\": -0.0391}}, \"phase2_seed123_remaining\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T10:05:23.998Z\", \"updated_at\": \"2026-05-13T15:41:50.802Z\", \"conclusion\": \"success\", \"metrics\": {\"uncurated\": {\"gen0\": {\"ppl\": 36.69, \"rankme\": 277.86, \"knn\": 0.988, \"rare\": 0.0293, \"corr\": -0.0222}, \"gen1\": {\"ppl\": 45.29, \"rankme\": 297.08, \"knn\": 0.988, \"rare\": 0.0192, \"corr\": -0.0554}, \"gen2\": {\"ppl\": 53.76, \"rankme\": 301.88, \"knn\": 0.988, \"rare\": 0.0137, \"corr\": -0.0448}, \"gen3\": {\"ppl\": 53.76, \"rankme\": 300.7, \"knn\": 0.988, \"rare\": 0.0116, \"corr\": -0.0365}, \"gen4\": {\"ppl\": 54.33, \"rankme\": 298.78, \"knn\": 0.988, \"rare\": 0.0107, \"corr\": -0.0471}, \"gen5\": {\"ppl\": 53, \"rankme\": 293.21, \"knn\": 0.988, \"rare\": 0.01, \"corr\": -0.037}, \"gen6\": {\"ppl\": 49.87, \"rankme\": 295.35, \"knn\": 0.988, \"rare\": 0.0101, \"corr\": -0.0477}, \"gen7\": {\"ppl\": 46.15, \"rankme\": 290.13, \"knn\": 0.988, \"rare\": 0.0093, \"corr\": -0.0755}}, \"rgds\": {\"gen0\": {\"ppl\": 36.71, \"rankme\": 272.68, \"knn\": 0.988, \"rare\": 0.0293, \"corr\": -0.0116, \"ratio\": 0.9997}, \"gen1\": {\"ppl\": 42.81, \"rankme\": 286.96, \"knn\": 0.988, \"rare\": 0.0186, \"corr\": -0.0544, \"ratio\": 0.9066}, \"gen2\": {\"ppl\": 47.35, \"rankme\": 291.31, \"knn\": 0.988, \"rare\": 0.0142, \"corr\": -0.0569, \"ratio\": 0.8604}, \"gen3\": {\"ppl\": 52.64, \"rankme\": 295.72, \"knn\": 0.988, \"rare\": 0.0119, \"corr\": -0.0185, \"ratio\": 0.8689}, \"gen4\": {\"ppl\": 52.74, \"rankme\": 294.9, \"knn\": 0.988, \"rare\": 0.0101, \"corr\": -0.0042, \"ratio\": 0.8863}, \"gen5\": {\"ppl\": 60.62, \"rankme\": 294.93, \"knn\": 0.988, \"rare\": 0.0087, \"corr\": -0.0036, \"ratio\": 0.7809}, \"gen6\": {\"ppl\": 75.03, \"rankme\": 299.36, \"knn\": 0.988, \"rare\": 0.007, \"corr\": -0.0119, \"ratio\": 0.6789}, \"gen7\": {\"ppl\": 81.57, \"rankme\": 298.35, \"knn\": 0.988, \"rare\": 0.0062, \"corr\": -0.0312, \"ratio\": 0.5236}}}}, \"phase2_random50_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:29:42.169Z\", \"updated_at\": \"2026-05-13T15:19:47.746Z\", \"hypothesis\": \"Random 50% baseline: 与 RGDS/external_only 相同的 50% 数据预算但随机选择，验证 diversity-aware selection 相比随机选择的增益\", \"parent\": \"phase2_3method_selfit\", \"conclusion\": \"failed\"}}, \"count\": 20, \"total\": 31, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2369}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compute the values:

**Registry data for 355M:**
- RGDS seed=42: gen7 PPL = 82.84
- RGDS seed=123: gen7 PPL = 90.25
- RGDS 2-seed mean: (82.84 + 90.25) / 2 = 86.545
- Random 50% seed=42: gen7 PPL = 70.25
- Random 50% seed=123: gen7 PPL = 72.55


- Random 2-seed mean: (70.25 + 72.55) / 2 = 71.40

The gap between these approaches is (86.545 - 71.40) / 71.40 * 100 = 21.21%, which aligns with what the task specifies. Now I need to make three edits to the tables, starting with updating the Random 50% entry in Table 3.

For the second change in §5.7, I'm replacing the single-seed comparison with 2-seed means. The RGDS mean of 86.55 versus Random's 71.40 gives us that ~21% gap, which is more accurate than the previous +18% figure.

Looking at the third modification for Table 2's footnote... Now I need to update the actual data values in Table 2 with the seed=123 results. The delta comparisons for RGDS vs Random 50% and Random 50% vs Uncurated were previously calculated from seed=42 only, but now that seed=123 is complete, I should recalculate these with the new data to get more accurate values. I need to carefully update the footnote to reflect that seed=123 is now complete for all methods, while keeping the delta values as they are since they still only show seed=42 data. The caption should note that seed=42 is the only completed seed for the main results, with seed=456 experiments still pending, and I'll remove the mention of Random 50% seed=123 being pending since that's now done. I need to remove the "pending" notation for Random 50% seed=123 since that experiment is now complete, then recalculate the performance gap using the updated 2-seed means. The new gap between RGDS and Random 50% comes out to about 21.2% instead of the current 18%.

Now I'm updating the related references throughout the document—the TODO comment on line 145 can be removed since seed=123 is done, and the perplexity penalty mentioned on line 150 needs to change from +18% to +21% to stay consistent. I should also update Table 3's caption to reflect that only seed=456 experiments are pending now. I'm working through a series of edits to update the experimental results—changing the Random 50% baseline from 70.25 to 71.40, updating the RGDS underperformance calculation from +18% to +21%, and cleaning up the table captions and footnotes to reflect that only seed=456 experiments are pending. I'm looking at the statistical findings from the caption—RGDS shows significantly different performance from all other methods on both metrics with large effect sizes, while within the non-RGDS group, perplexity differences aren't significant but rare n-gram differences are. There's also a note about how RGDS versus uncurated ordering flips direction depending on the random seed used. I need to update the status line to reflect that both seed=42 and seed=123 are now complete for all four methods, with seed=456 experiments still pending. I should also remove or update the TODO on line 145 since the seed=123 confirmation is done, and clean up the outdated status note on line 124-125 to match the new completion state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "f76e5db5-3a50-4430-8b89-44e7d505589b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPpXZuBiT1MDTMByrYw3Rw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15994,
      "cache_read_input_tokens": 24567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15994
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

_source line 20_

Data confirmed from registry:
- RGDS seed=42: 82.84, seed=123: 90.25 → 2-seed mean: 86.55
- Random 50% seed=42: 70.25, seed=123: 72.55 → 2-seed mean: 71.40
- Gap: (86.55 - 71.40) / 71.40 = 21.2%

Applying all three modifications now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "75208bed-2162-4c40-8422-789c9918b42e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPpXZuBiT1MDTMByrYw3Rw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15994,
      "cache_read_input_tokens": 24567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15994
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01KiXyihL5ssdD56Wec7UdsC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "\tRandom 50\\% & 50\\% & 70.25 & --- & 1 \\\\",
  "new_string": "\tRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "2814f5d9-5d0c-4cc1-8205-09d20032e5bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPpXZuBiT1MDTMByrYw3Rw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15994,
      "cache_read_input_tokens": 24567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15994
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

_source line 22 · 2026-05-14T08:38:32.357Z_

<details><summary>↩ Tool result · reported error · `toolu_01KiXyihL5ssdD56Wec7UdsC`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: 	Random 50\% & 50\% & 70.25 & --- & 1 \\&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "88be6fd6-48c8-43e2-ba87-118211b7485f",
  "tool_use_result": "Error: String to replace not found in file.\nString: \tRandom 50\\% & 50\\% & 70.25 & --- & 1 \\\\"
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01C4nFSb9g56PjErTuyVxgLb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "offset": 130,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "753c95f7-f81b-44db-9c1e-047dd39bf1fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JSGtYZQcznruwHPveujZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3537,
      "cache_read_input_tokens": 40561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3537
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

_source line 24 · 2026-05-14T08:38:35.079Z_

<details><summary>↩ Tool result · `toolu_01C4nFSb9g56PjErTuyVxgLb`</summary>

```text
130	\begin{tabular}{lcccc}
131	\toprule
132	Method & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\
133	\midrule
134	Random 50\% & 50\% & 70.25 & --- & 1 \\
135	External-only & 50\% & 77.74 & 79.56 & 2 \\
136	RGDS & 50\% & 82.84 & 90.25 & 2 \\
137	Uncurated & 100\% & 91.66 & 87.05 & 2 \\
138	\bottomrule
139	\end{tabular}
140	\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\ 91.66 at seed=42; 90.25 vs.\ 87.05 at seed=123). Random~50\% seed=123 and all seed=456 experiments are pending.}
141	\label{tab:medium_comparison}
142	\end{table}
143	
144	\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\% (70.25) by +18\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "68f6f3fa-283e-4143-a397-f971fc06e782",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
      "content": "\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & --- & 1 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). Random~50\\% seed=123 and all seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%",
      "numLines": 15,
      "startLine": 130,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01JnmRnyTBhfo3U8uGgxaShs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "Random 50\\% & 50\\% & 70.25 & --- & 1 \\\\",
  "new_string": "Random 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "26bb7b30-8e92-4e35-9a2e-d2539826cc56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E64zrSUxBNedEaY2uXBDYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 44098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 680
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 26 · 2026-05-14T08:38:38.971Z_

<details><summary>↩ Tool result · `toolu_01JnmRnyTBhfo3U8uGgxaShs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "dce5456f-c573-4dc6-bcd5-3b1b698aeb8c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "Random 50\\% & 50\\% & 70.25 & --- & 1 \\\\",
    "newString": "Random 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & --- & 1 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). Random~50\\% seed=123 and all seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): confirm with seed=123 and report significance\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 131,
        "oldLines": 7,
        "newStart": 131,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " Method & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\",
          " \\midrule",
          "-Random 50\\% & 50\\% & 70.25 & --- & 1 \\\\",
          "+Random 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\",
          " External-only & 50\\% & 77.74 & 79.56 & 2 \\\\",
          " RGDS & 50\\% & 82.84 & 90.25 & 2 \\\\",
          " Uncurated & 100\\% & 91.66 & 87.05 & 2 \\\\"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01FxxBYEjRoqSbf8GCHsXZeV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "Random~50\\% seed=123 and all seed=456 experiments are pending.}",
  "new_string": "All seed=456 experiments are pending.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "3ff4f8c2-6eb1-4086-b289-c5e20e9c073c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xr6H2tdoostNoM3eptx1FF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 44778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 28 · 2026-05-14T08:38:42.421Z_

<details><summary>↩ Tool result · `toolu_01FxxBYEjRoqSbf8GCHsXZeV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "dce084d4-411c-4ee2-88e0-bbd20a7f3921",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "Random~50\\% seed=123 and all seed=456 experiments are pending.}",
    "newString": "All seed=456 experiments are pending.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). Random~50\\% seed=123 and all seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): confirm with seed=123 and report significance\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 7,
        "newStart": 137,
        "newLines": 7,
        "lines": [
          " Uncurated & 100\\% & 91.66 & 87.05 & 2 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). Random~50\\% seed=123 and all seed=456 experiments are pending.}",
          "+\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}",
          " \\label{tab:medium_comparison}",
          " \\end{table}",
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_017rpt6V3dDy2u8TdDWupx84`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): confirm with seed=123 and report significance",
  "new_string": "\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "da6a2f89-9e8d-4993-aa31-808dabcf2463",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdapDbfpemYLoPACvmSJva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 45025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 30 · 2026-05-14T08:38:48.715Z_

<details><summary>↩ Tool result · `toolu_017rpt6V3dDy2u8TdDWupx84`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "4f008729-292d-431e-abc7-c23ae69001b0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): confirm with seed=123 and report significance",
    "newString": "\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): confirm with seed=123 and report significance\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 8,
        "newStart": 141,
        "newLines": 8,
        "lines": [
          " \\label{tab:medium_comparison}",
          " \\end{table}",
          " ",
          "-\\paragraph{C3 holds across scale.} RGDS (82.84) underperforms Random~50\\% (70.25) by +18\\% at 355M, confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%",
          "-%TODO(355M-seeds): confirm with seed=123 and report significance",
          "+\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%",
          "+%TODO(355M-seeds): report significance with seed=456",
          " ",
          " \\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%",
          " %TODO(355M-seeds): update with seed=456 data"
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

_source line 31_

Now update the "+18%" reference in the alignment gap paragraph and the §5.7 intro text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "f6fd994d-b449-4e56-b6c3-21ed881a38bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfkCxU3ymu2smiP26VCyhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 456,
      "cache_read_input_tokens": 45248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 456
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

<details open><summary>🔧 Tool call — Edit · `toolu_01EUKprqAqhMHdMnNZkT4Ajm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M)",
  "new_string": "The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "e29fc4df-e020-4230-8e89-b7a7e631f3cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfkCxU3ymu2smiP26VCyhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 456,
      "cache_read_input_tokens": 45248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 456
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

_source line 33 · 2026-05-14T08:38:53.357Z_

<details><summary>↩ Tool result · `toolu_01EUKprqAqhMHdMnNZkT4Ajm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "09281583-b767-4c40-8c92-7d1c5af63bcb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M)",
    "newString": "The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M)",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 147,
        "oldLines": 5,
        "newStart": 147,
        "newLines": 5,
        "lines": [
          " \\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%",
          " %TODO(355M-seeds): update with seed=456 data",
          " ",
          "-\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +18\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%",
          "+\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%",
          " %TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验"
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

_source line 34_

Now update the Table 2 (stat_tests) caption — remove "Random 50% seed=123" from pending.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "c006bc57-fe6d-4ad9-a54c-692aa82b9fa2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qd6fWPmLDHkYTXjCUjg38",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 45704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 268
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01QDFLGkgDga2snokJmaRR3A`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "pending Random~50\\% seed=123 and all seed=456 experiments",
  "new_string": "all seed=456 experiments pending"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "cbfc2f4b-6c4d-430f-9f6f-8d468fa4af58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qd6fWPmLDHkYTXjCUjg38",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 45704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 268
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

_source line 36 · 2026-05-14T08:38:59.767Z_

<details><summary>↩ Tool result · `toolu_01QDFLGkgDga2snokJmaRR3A`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "f52de1e6-aa7e-46ef-9149-9248ebd2d6fd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "pending Random~50\\% seed=123 and all seed=456 experiments",
    "newString": "all seed=456 experiments pending",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 109,
        "oldLines": 7,
        "newStart": 109,
        "newLines": 7,
        "lines": [
          " RGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), pending Random~50\\% seed=123 and all seed=456 experiments. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
          "+\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
          " \\label{tab:stat_tests}",
          " \\end{table*}",
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01QYFZe9ikuWqf62bvYXzdAP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "$^\\dagger$seed=42 only (Random~50\\% seed=123 pending).",
  "new_string": "$^\\dagger$seed=42 only (all seed=456 experiments pending)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "7db3f62f-bb72-436b-9612-c8f6c24cf9b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WtXKWa1EjKttPfhzFTo5B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 45972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 38 · 2026-05-14T08:39:05.107Z_

<details><summary>↩ Tool result · `toolu_01QYFZe9ikuWqf62bvYXzdAP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "4576a633-ea46-4228-89a1-b889869bbfe0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "$^\\dagger$seed=42 only (Random~50\\% seed=123 pending).",
    "newString": "$^\\dagger$seed=42 only (all seed=456 experiments pending).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 109,
        "oldLines": 7,
        "newStart": 109,
        "newLines": 7,
        "lines": [
          " RGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (Random~50\\% seed=123 pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
          "+\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
          " \\label{tab:stat_tests}",
          " \\end{table*}",
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

_source line 39_

Also update the intro paragraph for §5.7 which mentions "Random~50\% seed=123 pending".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "9bf3407e-96f0-4a31-840b-e1f6bf4840f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF4K9GZxiDyQD31RXy8E4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 46219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 236
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01BHDV4voKxJRJLH9LR5BaYH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending",
  "new_string": "seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "86ab56a4-6316-41a3-85ad-fd465fc5a260",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF4K9GZxiDyQD31RXy8E4C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 46219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 236
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

_source line 41 · 2026-05-14T08:39:09.937Z_

<details><summary>↩ Tool result · `toolu_01BHDV4voKxJRJLH9LR5BaYH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "82a5fa38-d98f-4e8d-977e-c07e2a379bdd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending",
    "newString": "seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 121,
        "oldLines": 7,
        "newStart": 121,
        "newLines": 7,
        "lines": [
          " \\subsection{Scaling to GPT2-Medium (355M)}",
          " \\label{sec:result_scaling}",
          " ",
          "-Results from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 complete for all; seed=123 complete for External-only, RGDS, and Uncurated; Random~50\\% seed=123 pending).%",
          "+Results from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%",
          " %TODO(355M-seeds): update when Random seed=123 and all seed=456 complete",
          " ",
          " \\begin{table}[t]"
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

_source line 42_

验证修改结果：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "0962465c-2ea8-4f19-af77-374b38a25604",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoZhiHbiwcXy8qtHNJJiJq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 46455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01Uq2YWWvCare2yNSSbWxtSW`</summary>

```json
{
  "pattern": "72\\.55",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
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
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "1cabe589-33cc-4e67-9f8b-4aeaaa520207",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoZhiHbiwcXy8qtHNJJiJq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 46455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 44 · 2026-05-14T08:39:13.648Z_

<details><summary>↩ Tool result · `toolu_01Uq2YWWvCare2yNSSbWxtSW`</summary>

```text
134:Random 50\% & 50\% & 70.25 & 72.55 & 2 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "8884098e-9d99-4614-9111-2ff4f96e5bed",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "134:Random 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_013apdbHKMSd8SrxJaCmDCZL`</summary>

```json
{
  "pattern": "\\+21",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
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
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "27d5564a-b292-4a49-a80b-0adb3d88d1fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoZhiHbiwcXy8qtHNJJiJq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 46455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 46 · 2026-05-14T08:39:14.589Z_

<details><summary>↩ Tool result · `toolu_013apdbHKMSd8SrxJaCmDCZL`</summary>

```text
144:\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\% (71.40) by +21\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%
150:\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\% perplexity penalty relative to Random (vs.\ +72\% at 125M) is consistent with this narrower gap.%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "845ff8e3-3b3d-49d4-85c8-2026670cb2ad",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "144:\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n150:\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01U58M15mYaviXYp8rbZYMWB`</summary>

```json
{
  "pattern": "seed=456 experiments pending",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
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
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "a40f4a36-08eb-4967-9ce5-1bb7ba3108cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoZhiHbiwcXy8qtHNJJiJq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 46455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 48 · 2026-05-14T08:39:15.217Z_

<details><summary>↩ Tool result · `toolu_01U58M15mYaviXYp8rbZYMWB`</summary>

```text
112:[Omitted long matching line]
124:Results from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "ba969473-728b-4e03-a618-1a81e49dd79d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "112:[Omitted long matching line]\n124:Results from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 49_

三处修改全部完成，验证通过：

1. **Table 3**: Random 50% 行已补充 seed=123 PPL=72.55，n=2
2. **§5.7 C3 段落**: gap 从 +18% 更新为 +21%（两处均已更新：C3 段落和 alignment gap 段落）
3. **Table 2 脚注**: 已移除 "Random~50\% seed=123 pending"，改为 "all seed=456 experiments pending"；§5.7 引言也同步更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "uuid": "bff6173e-f022-433d-bf4a-c3ff373d6a74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kns4kk5L2u5Upsy2souro4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 46840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
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

_source line 50_

三处修改全部完成，验证通过：

1. **Table 3**: Random 50% 行已补充 seed=123 PPL=72.55，n=2
2. **§5.7 C3 段落**: gap 从 +18% 更新为 +21%（两处均已更新：C3 段落和 alignment gap 段落）
3. **Table 2 脚注**: 已移除 "Random~50\% seed=123 pending"，改为 "all seed=456 experiments pending"；§5.7 引言也同步更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 131343,
  "duration_api_ms": 132037,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "02ec03e6-7d07-43a9-84a3-94904043c809",
  "total_cost_usd": 0.6486622500000001,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 35833,
    "cache_read_input_tokens": 534724,
    "output_tokens": 6232,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35833,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 155,
        "cache_read_input_tokens": 46840,
        "cache_creation_input_tokens": 834,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 834
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1369,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001454,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 6232,
      "cacheReadInputTokens": 534724,
      "cacheCreationInputTokens": 35833,
      "webSearchRequests": 0,
      "costUSD": 0.64720825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e5f514c7-c2f3-46af-b8aa-c1bee9de268b"
}
```

</details>

---
