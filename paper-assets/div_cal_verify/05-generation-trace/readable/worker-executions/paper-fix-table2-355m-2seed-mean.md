# paper fix table2 355m 2seed mean

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_fix_table2_355m_2seed_mean_20260514T084140.log`
- **Structured JSON:** [`19005fe9dc6ce3486ff5.json`](../../sessions/19/19005fe9dc6ce3486ff5.json)

## Before a recorded user message

36 recorded events

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
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
  "uuid": "3a8be9a5-cc85-4857-9e50-71a4637066e1",
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
  "uuid": "40fc2661-036a-43c8-a9db-1daf01ccd000",
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11"
}
```

---

### Assistant

_source line 4_

Let me read the current state of the results.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "c911f93a-9466-4726-81b3-48616776f63d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUN9aZS5DTu6v3hVwZwh42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11524,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11524
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

<details open><summary>🔧 Tool call — Read · `toolu_01SmfNXiNGba6nyCjC8WMscJ`</summary>

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "29d76006-878b-4edf-979b-2d5dfb0655b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUN9aZS5DTu6v3hVwZwh42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11524,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11524
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

_source line 6 · 2026-05-14T08:41:52.795Z_

<details><summary>↩ Tool result · reported error · `toolu_01SmfNXiNGba6nyCjC8WMscJ`</summary>

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "5a8c1d0c-3723-44e6-b10f-a970287528c4",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01HQPVgrTqscFq5XaBsQNJeq`</summary>

```json
{
  "pattern": "paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "09307510-5526-4bb4-944c-a297a1093e7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013skaDXcG2qtYqybgFvjnP4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 23365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

_source line 8 · 2026-05-14T08:41:55.419Z_

<details><summary>↩ Tool result · `toolu_01HQPVgrTqscFq5XaBsQNJeq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "49dbff61-a237-4d68-8d22-03370e12fa03",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 8,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01ReuFYAgGcyf5KgPVs7XM68`</summary>

```json
{
  "pattern": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "6e79e59b-10c0-4f46-9767-01fe8832feed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kTk56Cujoqu86PoC7kZTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 70,
      "cache_read_input_tokens": 23525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 70
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 10 · 2026-05-14T08:41:57.714Z_

<details><summary>↩ Tool result · `toolu_01ReuFYAgGcyf5KgPVs7XM68`</summary>

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "fe2d0082-6405-4a61-87f2-9316afc93b8e",
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
    "durationMs": 13,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01XLyzbPRB2iPzVtCeXQ8r87`</summary>

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "27efd4bd-d6a9-4d4a-a1cd-88f69878fc56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JgkduYLaHGUTJZqT75AN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 23595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 12 · 2026-05-14T08:42:00.419Z_

<details><summary>↩ Tool result · `toolu_01XLyzbPRB2iPzVtCeXQ8r87`</summary>

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
112	\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\dagger$seed=42 only (all seed=456 experiments pending). $^\ddagger$RGDS vs.\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}
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
124	Results from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%
125	%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete
126	
127	\begin{table}[t]
128	\centering
129	\small
130	\begin{tabular}{lcccc}
131	\toprule
132	Method & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\
133	\midrule
134	Random 50\% & 50\% & 70.25 & 72.55 & 2 \\
135	External-only & 50\% & 77.74 & 79.56 & 2 \\
136	RGDS & 50\% & 82.84 & 90.25 & 2 \\
137	Uncurated & 100\% & 91.66 & 87.05 & 2 \\
138	\bottomrule
139	\end{tabular}
140	\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\ 91.66 at seed=42; 90.25 vs.\ 87.05 at seed=123). All seed=456 experiments are pending.}
141	\label{tab:medium_comparison}
142	\end{table}
143	
144	\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\% (71.40) by +21\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%
145	%TODO(355M-seeds): report significance with seed=456
146	
147	\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\ 91.66) but underperforms at seed=123 (90.25 vs.\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\% ($74.29$ vs.\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \S\ref{sec:discuss_scaling}. The cross-budget comparison (50\% vs.\ 100\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\ Random~50\%, both at 50\%) isolates the effect of the selection mechanism.%
148	%TODO(355M-seeds): update with seed=456 data
149	
150	\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\% perplexity penalty relative to Random (vs.\ +72\% at 125M) is consistent with this narrower gap.%
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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "f9c0070b-7a23-4cc0-a788-726f22f0a499",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
      "numLines": 152,
      "startLine": 1,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the current state. Let me analyze what needs to be changed:

1. **Table 2 (tab:stat_tests)** - The 355M section (lines 106-110) needs updating:
   - Line 107: RGDS vs Random 50% Δ = +12.59 → +15.15
   - Line 108: Random 50% vs Uncurated Δ = -21.41 → need to recalculate: 71.40 - 89.36 = -17.96
   - Line 109: RGDS vs Uncurated - need to recalculate: 86.55 - 89.36 = -2.81
   - The footnote at line 112 needs updating

I need to verify which table is actually Table 2 by checking the document structure. Looking at the tables, tab:stat_tests appears to be the one I need to modify, so I'll proceed with updating those specific delta values and the corresponding footnote.

Now I'm recalculating the 355M section with the new 2-seed means. The RGDS vs Random 50% comparison should be 15.15 instead of 12.59, and I need to compute the remaining delta values with these updated baseline numbers. I'm finishing the calculation for RGDS vs Uncurated, which comes to -2.81. Now I need to verify all three pairwise comparisons are correct: RGDS vs Random 50% at +15.15, and I should only update the rows that actually exist in the current table rather than adding new comparisons. Now I'm mapping out the specific edits needed for Table 2 and its footnotes—updating the 355M row values to reflect the 2-seed mean calculations, removing the seed-specific markers, and clarifying that results are based on seeds 42 and 123 with seed 456 still pending.

Let me verify the consistency across the document by checking the paragraph claims against the actual numbers—the +21% improvement for RGDS versus Random at 355M checks out mathematically, and the existing text about which seeds are complete already aligns with what needs to be documented. Looking at the table structure more carefully—Table 2 shows delta values rather than raw PPL numbers, while Table 3 contains the individual per-seed PPL measurements. I need to clarify what the task is actually asking me to update: whether it's asking me to convert Table 3's per-seed values to mean values, or if there's a mismatch between what the task calls "Table 2" and the actual LaTeX table numbering. actually, the `\begin{table*}` for tab:gen7_summary is floated and numbered 1. Then tab:stat_tests is also a `table*`, so it's numbered 2. Then tab:medium_comparison is a `table`, numbered 3.

But wait, the user says "Table 2 355M 区域" and mentions updating Gen7 PPL values AND pairwise Δ values. Table 2 (tab:stat_tests) has the Δ values but not Gen7 PPL directly. The 355M PPL values are in Table 3 (tab:medium_comparison).

Looking at the task data, I can see the per-seed values and their 2-seed means for each method. Table 3 already contains these exact values, so the user probably wants me to either add a mean column or restructure it to show means. For Table 2, I need to update the 355M Δ values based on the new mean calculations, and possibly update the footnotes as well. Looking at the actual table structure in tab:stat_tests, I see the 355M section still has the † footnote indicating seed=42 only values, even though tab:medium_comparison appears to already show both seeds. So I need to update those Δ values in the 355M rows to reflect the 2-seed mean instead of just the single seed, and adjust the corresponding footnotes accordingly. Looking at the 355M section, I notice it's much sparser than the 125M section which has comparisons across multiple metrics and dataset pairs. The task mentions RGDS vs External with a +7.90 difference, so I should add that row to match the structure of the 125M results, even though it's not currently there. the task says "如果表中还有其他 pairwise Δ，同样按 2-seed mean 重算", I'll only update existing rows.

But the task explicitly mentions "RGDS vs External Δ = +7.90". Maybe they want me to add this row too? Let me re-read... "更新所有 pairwise Δ 值：RGDS vs Random Δ = +15.15（原来是 +12.59）, RGDS vs External Δ = +7.90, RGDS vs Uncurated Δ = -2.81（RGDS 好于 Uncurated）". This lists 3 Δ values to put in the table, replacing the current 3 rows. So the mapping would be:

Current rows → New rows:
1. RGDS vs Random 50%: +12.59 → +15.15
2. Random 50% vs Uncurated: -21.41 → RGDS vs External +7.90
3. RGDS vs Uncurated: -8.82/+3.20 → -2.81

Looking at the task data more carefully, it gives three Δ values (RGDS-Random, RGDS-External, RGDS-Uncurated) while the current table has RGDS-Random, Random-Uncurated, and RGDS-Uncurated. So I need to update the first row to +15.15, replace the second row with RGDS vs External at +7.90, and update the third row to -2.81. I'm recalculating the pairwise comparisons using the 2-seed means, so I need to update the existing rows and add the RGDS vs External comparison. Let me map out the precise edits for the table: RGDS vs Random 50% becomes +15.15, Random 50% vs Uncurated becomes -17.96, and I'll add the new RGDS vs External row with +7.90. I'm looking at the performance comparisons for GPT2-Medium and need to update the table footnotes to reflect that we're working with 2-seed means while the third seed is still pending, and that statistical tests will wait until we have at least 3 seeds. I should also verify the numbers in section 5.7 where the RGDS mean is being compared against the Random 50% baseline. The section 5.7 text is already consistent with the two-seed mean values and percentage calculations, so I can proceed with making the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "95ecc0d1-791d-4f5a-afd0-ee336976b5e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8bH7fcFzmqzkuSBxTBgJj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6202,
      "cache_read_input_tokens": 23839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6202
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 14_

I see the current state. The 355M section of Table 2 (tab:stat_tests) still has seed=42-only Δ values with † markers. Table 3 (tab:medium_comparison) and the §5.7 prose already show both seeds correctly. I need to update Table 2's 355M rows and footnotes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "66b52c87-e0b1-4d07-8fe9-872a40c2821c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8bH7fcFzmqzkuSBxTBgJj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6202,
      "cache_read_input_tokens": 23839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6202
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_018FzHBk2KPfV9WhbbGtUd6s`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "\t\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\n\tRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\tRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\tRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
  "new_string": "\t\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\\\\n\tRGDS vs.\\ Random 50\\% & PPL & $+$15.15 & \\multicolumn{3}{c}{---} & --- \\\\\n\tRGDS vs.\\ External-only & PPL & $+$7.90 & \\multicolumn{3}{c}{---} & --- \\\\\n\tRGDS vs.\\ Uncurated & PPL & $-$2.81 & \\multicolumn{3}{c}{---} & --- \\\\\n\tRandom 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "b37a2688-fe26-41b4-8e53-67288a583939",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8bH7fcFzmqzkuSBxTBgJj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6202,
      "cache_read_input_tokens": 23839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6202
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 16 · 2026-05-14T08:43:21.555Z_

<details><summary>↩ Tool result · reported error · `toolu_018FzHBk2KPfV9WhbbGtUd6s`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: 	\multicolumn{7}{l}{\textit{GPT2-Medium (355M)---statistical tests pending $\geq$3 seeds}} \\
	RGDS vs.\ Random 50\% & PPL & $+$12.59$^\dagger$ & \multicolumn{3}{c}{---} & --- \\
	Random 50\% vs.\ Uncurated & PPL & $-$21.41$^\dagger$ & \multicolumn{3}{c}{---} & --- \\
	RGDS vs.\ Uncurated & PPL & $-$8.82 / $+$3.20$^\ddagger$ & \multicolumn{3}{c}{---} & --- \\&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "44ce5ea4-8c11-4701-b9af-40fec4f2baf0",
  "tool_use_result": "Error: String to replace not found in file.\nString: \t\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\n\tRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\tRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\tRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\"
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
The tab indentation might be different. Let me re-read the exact lines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "aed74e57-dbc4-4777-adb9-98e0a8bf3c21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4mNhso42JYTBojVeCWuG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5862,
      "cache_read_input_tokens": 30041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5862
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

_source line 18_

Let me re-read the exact lines to get the whitespace right.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "6f16825b-5c16-4521-90fc-8a23d38f3561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4mNhso42JYTBojVeCWuG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5862,
      "cache_read_input_tokens": 30041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5862
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

<details open><summary>🔧 Tool call — Read · `toolu_012jxno4MUp6CghnXnVmckKh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "offset": 105,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "6f8da325-a2e0-4f21-ade0-0c39ea804315",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4mNhso42JYTBojVeCWuG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5862,
      "cache_read_input_tokens": 30041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5862
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

_source line 20 · 2026-05-14T08:43:26.290Z_

<details><summary>↩ Tool result · `toolu_012jxno4MUp6CghnXnVmckKh`</summary>

```text
105	\midrule
106	\multicolumn{7}{l}{\textit{GPT2-Medium (355M)---statistical tests pending $\geq$3 seeds}} \\
107	RGDS vs.\ Random 50\% & PPL & $+$12.59$^\dagger$ & \multicolumn{3}{c}{---} & --- \\
108	Random 50\% vs.\ Uncurated & PPL & $-$21.41$^\dagger$ & \multicolumn{3}{c}{---} & --- \\
109	RGDS vs.\ Uncurated & PPL & $-$8.82 / $+$3.20$^\ddagger$ & \multicolumn{3}{c}{---} & --- \\
110	\bottomrule
111	\end{tabular}
112	\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\dagger$seed=42 only (all seed=456 experiments pending). $^\ddagger$RGDS vs.\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}
113	\label{tab:stat_tests}
114	\end{table*}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "bf8ee00d-6e11-4d7f-8bdb-5c6d96cddfb5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
      "content": "\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}",
      "numLines": 10,
      "startLine": 105,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01QvcoifawnVCadqyQm8R1k5`</summary>

```json
{
  "command": "cat -A /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex | sed -n '106,109p'",
  "description": "Check exact whitespace characters on lines 106-109"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "d4c93cfe-573c-4471-9c79-42b27728dcbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZuXohKX4zjsZekKKViLq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 35903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 698
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 22 · 2026-05-14T08:43:29.588Z_

<details><summary>↩ Tool result · `toolu_01QvcoifawnVCadqyQm8R1k5`</summary>

```text
\multicolumn{7}{l}{\textit{GPT2-Medium (355M)---statistical tests pending $\geq$3 seeds}} \\$
RGDS vs.\ Random 50\% & PPL & $+$12.59$^\dagger$ & \multicolumn{3}{c}{---} & --- \\$
Random 50\% vs.\ Uncurated & PPL & $-$21.41$^\dagger$ & \multicolumn{3}{c}{---} & --- \\$
RGDS vs.\ Uncurated & PPL & $-$8.82 / $+$3.20$^\ddagger$ & \multicolumn{3}{c}{---} & --- \\$
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "15208a46-370d-45e4-a33f-28bc2a195631",
  "tool_use_result": {
    "stdout": "\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\$\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\$\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\$\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\$",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
No tabs, just plain text. Let me try the edit again without leading tabs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "01b703fb-fa7b-4427-8ca4-1eb61fdd23fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vgaYdXn8pYFg5NRSNPVZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 36601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 418
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

_source line 24_

No leading tabs — lines start directly. Let me apply the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "0cc99e82-b606-4402-8136-5fcc55226f4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vgaYdXn8pYFg5NRSNPVZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 36601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 418
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01TFQJy5QourNTvvXZbqpYte`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
  "new_string": "\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$15.15 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ External-only & PPL & $+$7.90 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$2.81 & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "8e969107-0c25-4c8b-ac4b-31dc4ef95a6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vgaYdXn8pYFg5NRSNPVZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 36601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 418
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

_source line 26 · 2026-05-14T08:43:37.141Z_

<details><summary>↩ Tool result · `toolu_01TFQJy5QourNTvvXZbqpYte`</summary>

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "208183b4-e345-4752-8910-148063351e0e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
    "newString": "\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$15.15 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ External-only & PPL & $+$7.90 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$2.81 & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 103,
        "oldLines": 10,
        "newStart": 103,
        "newLines": 11,
        "lines": [
          " Non-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\",
          " Non-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\",
          " \\midrule",
          "-\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---statistical tests pending $\\geq$3 seeds}} \\\\",
          "-RGDS vs.\\ Random 50\\% & PPL & $+$12.59$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
          "-Random 50\\% vs.\\ Uncurated & PPL & $-$21.41$^\\dagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
          "-RGDS vs.\\ Uncurated & PPL & $-$8.82 / $+$3.20$^\\ddagger$ & \\multicolumn{3}{c}{---} & --- \\\\",
          "+\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\\\",
          "+RGDS vs.\\ Random 50\\% & PPL & $+$15.15 & \\multicolumn{3}{c}{---} & --- \\\\",
          "+RGDS vs.\\ External-only & PPL & $+$7.90 & \\multicolumn{3}{c}{---} & --- \\\\",
          "+RGDS vs.\\ Uncurated & PPL & $-$2.81 & \\multicolumn{3}{c}{---} & --- \\\\",
          "+Random 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}"
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

_source line 27_

Now update the caption to remove the old † and ‡ footnotes and update the 355M description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "710fb7ab-b4b6-4f0e-91dd-0bab06edc6e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPrjPTftX345SkHXKEcJA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 37019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
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

<details open><summary>🔧 Tool call — Edit · `toolu_01RUTW7bRrjHHe6cRsfLEyXX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "old_string": "\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
  "new_string": "\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). 355M: $n{=}2$ seeds (42, 123); seed=456 pending; $t$-tests deferred until $n \\geq 3$.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "888770d5-c782-4d21-a08c-5db08bef1f0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPrjPTftX345SkHXKEcJA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 37019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
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

_source line 29 · 2026-05-14T08:43:45.403Z_

<details><summary>↩ Tool result · `toolu_01RUTW7bRrjHHe6cRsfLEyXX`</summary>

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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "2d6f8dcf-465a-43f4-bd1f-dc1323db7e22",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
    "oldString": "\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
    "newString": "\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). 355M: $n{=}2$ seeds (42, 123); seed=456 pending; $t$-tests deferred until $n \\geq 3$.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nTable~\\ref{tab:gen7_summary} summarizes Generation~7 metrics across all methods and seeds; Table~\\ref{tab:stat_tests} reports complete pairwise statistical comparisons. Figure~\\ref{fig:ppl_trends} shows per-generation perplexity trajectories; Figure~\\ref{fig:ratio_trajectory} shows selection ratio trajectories for RGDS and External-only. We organize findings around three primary claims and one directional observation.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & Budget & Gen\\,0 PPL & Gen\\,7 PPL & $\\Delta$\\% & Sel.\\ Ratio & Rare n-gram & RankMe & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 36.87 & 43.18$\\pm$1.43 & +17 & $\\approx$1.00 & .0098$\\pm$.0003 & 290.98$\\pm$0.98 & 3 \\\\\nExternal-only & 50\\% & 36.74 & 46.36$\\pm$2.97 & +26 & 1.16$\\pm$0.08 & .0103$\\pm$.0004 & 291.45$\\pm$1.08 & 3 \\\\\nUncurated & 100\\% & 36.81 & 47.04$\\pm$2.90 & +28 & --- & .0090$\\pm$.0004 & 289.83$\\pm$1.77 & 3 \\\\\nRGDS & 50\\% & 36.83 & 74.29$\\pm$7.71 & +102 & 0.64$\\pm$0.20 & .0061$\\pm$.0009 & 292.54$\\pm$5.91 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Generation~7 summary across methods (GPT2-125M on WikiText-103). PPL: perplexity on WikiText-103 validation set (lower is better). Sel.\\ Ratio: mean rare trigram density of the selected subset divided by the full generated pool ($>$1 = preferential retention of content-diverse samples). Rare n-gram: proportion of generated trigrams at or below the 10th percentile of the WikiText-103 frequency distribution. RankMe: effective embedding rank via singular value entropy. $\\Delta$\\%: relative perplexity increase from Generation~0 to Generation~7. All methods report $n{=}3$ seeds.}\n\\label{tab:gen7_summary}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ppl_trends.pdf}\n\\caption{Per-generation perplexity trajectories across four data selection methods (GPT2-125M on WikiText-103). Lines show means over $n{=}3$ seeds; shaded bands show $\\pm$1 standard deviation. RGDS diverges from the non-RGDS cluster after Generation~4 and reaches catastrophic perplexity by Generation~7 ($74.29 \\pm 7.71$), while the other three methods converge to a narrow band (43--47).}\n\\label{fig:ppl_trends}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ratio_trajectory.pdf}\n\\caption{Selection ratio trajectories for RGDS and External-only across eight generations. The dashed line marks the alignment threshold ($\\text{SR}=1.0$): above it, the method preferentially retains content-diverse samples; below it, content-poor samples are preferentially selected. RGDS's mean ratio declines from ${\\sim}1.0$ to $0.64 \\pm 0.20$, while External-only remains above~1.0 throughout. The large variance at Generation~7 reflects seed=456's late rebound (0.65$\\to$0.87) without perplexity recovery.}\n\\label{fig:ratio_trajectory}\n\\end{figure}\n\n\\subsection{RGDS Accelerates Catastrophic Perplexity Degradation}\n\\label{sec:result_c1}\n\nRGDS is the only method that exhibits catastrophic performance degradation across generations. At Generation~7, RGDS reaches a perplexity of $74.29 \\pm 7.71$ ($n{=}3$), compared to $47.04 \\pm 2.90$ for Uncurated ($n{=}3$; +58\\%) and $43.18 \\pm 1.43$ for Random~50\\% ($n{=}3$; +72\\%). All three seeds show consistent catastrophic degradation---75.07 (seed=42), 81.57 (seed=123), and 66.22 (seed=456)---with all values far exceeding the 43--47 range of the non-RGDS methods. The inter-seed variance of RGDS ($\\sigma = 7.71$) substantially exceeds that of any other method ($\\sigma \\leq 2.97$), reflecting the stochastic dynamics of the co-degradation feedback loop.\n\nThe selection ratio traces the mechanism behind this degradation (Figure~\\ref{fig:ratio_trajectory}). RGDS's mean selection ratio follows an overall declining trend from ${\\sim}1.0$ at Generation~0 to $0.64 \\pm 0.20$ at Generation~7 ($n{=}3$). Seeds 42 and 123 reach deeply inverted ratios (0.52 and 0.52 respectively), while seed=456 exhibits a late-generation rebound from 0.65 at Generation~6 to 0.87 at Generation~7---without any corresponding improvement in perplexity (66.22 vs.\\ 43--47 for non-RGDS methods). This dissociation between ratio recovery and perplexity indicates that once the embedding space has been sufficiently corrupted, even a partial restoration of selection alignment cannot reverse the accumulated damage to model quality. Across all seeds, RGDS preferentially retains vocabulary-poor samples relative to the full generated pool.\n\n\\subsection{External Embeddings Avoid the Alignment Gap}\n\\label{sec:result_c2}\n\nExternal-only selection applies the identical selection algorithm and 50\\% data budget but uses frozen Contriever embeddings. It avoids catastrophic degradation entirely: its Generation~7 perplexity of $46.36 \\pm 2.97$ ($n{=}3$) falls within the range of Uncurated ($47.04 \\pm 2.90$) and Random~50\\% ($43.18 \\pm 1.43$).\n\nExternal-only maintains a selection ratio above~1.0 throughout all generations ($1.16 \\pm 0.08$ at Generation~7), indicating continued preferential retention of content-diverse samples.\n\nSince RGDS and External-only differ in exactly one variable---the embedding source---the 27.9-point perplexity gap at Generation~7 ($74.29$ vs.\\ $46.36$) is directly attributable to the use of co-degrading internal representations. The selection algorithm is not at fault; the failure is specific to coupling data selection to embeddings that co-evolve with the collapsing model.\n\nNotably, External-only does not significantly outperform Random~50\\% in perplexity ($46.36 \\pm 2.97$ vs.\\ $43.18 \\pm 1.43$; $p = 0.198$, Welch's $t$-test, $n{=}3$). Despite maintaining a selection ratio above~1.0, the ``intelligent'' diversity signal from frozen external embeddings provides no measurable advantage over uninformed random subsampling. This null result reinforces the practical implication discussed in \\S\\ref{sec:discussion}: random sampling is a zero-cost alternative that matches the performance of embedding-guided selection when embeddings are stable and avoids the catastrophic failure when they are not.\n\n\\subsection{Internal Selection Underperforms Random Baseline}\n\\label{sec:result_c3}\n\nThe comparison between RGDS and Random~50\\% constitutes the cleanest controlled ablation in our design. Both methods operate under identical conditions---same 50\\% data budget, same training protocol, same seed infrastructure, same Generation~0 checkpoint---differing only in the selection mechanism: diversity-based curation via the model's own embeddings (RGDS) versus uninformed uniform sampling (Random~50\\%). Any performance difference is therefore attributable solely to the selection mechanism, free from the data-volume confound present in comparisons against Uncurated (50\\% vs.\\ 100\\%).\n\nUnder this controlled comparison, RGDS exhibits catastrophically worse performance. Its Generation~7 perplexity ($74.29 \\pm 7.71$, $n{=}3$) exceeds Random~50\\% ($43.18 \\pm 1.43$, $n{=}3$) by $+$72\\% ($p = .017$, Welch's $t$, $d = 5.61$). The effect is consistent across all three seeds, with each RGDS run (75.07, 81.57, 66.22) far exceeding the non-RGDS cluster ceiling of ${\\sim}47$. Internal embedding diversity selection does not merely fail to improve upon random sampling---it actively degrades model quality by a margin that dwarfs all other method differences in this study.\n\nRare n-gram ratio corroborates the perplexity finding: RGDS retains $0.0061 \\pm 0.0009$ at Generation~7, compared to $0.0098 \\pm 0.0003$ for Random~50\\%---a 38\\% reduction in lexical tail content ($p = .014$, $d = -5.66$). The mechanism designed to maximize diversity produces outputs that are measurably \\emph{less} diverse than those from uninformed subsampling.\n\nThis within-budget contrast should be distinguished from the RGDS vs.\\ Uncurated comparison ($+$58\\%), which conflates any selection effect with a data quantity difference (50\\% vs.\\ 100\\%). The Random~50\\% vs.\\ Uncurated comparison (\\S\\ref{sec:result_s3}) similarly involves a budget confound and does not reach significance ($p = .133$), reinforcing that the within-budget RGDS-vs.-Random ablation provides the most interpretable causal evidence for the alignment gap.\n\n\\subsection{Random Pruning: A Directional Observation}\n\\label{sec:result_s3}\n\nRandom~50\\% ($43.18 \\pm 1.43$, $n{=}3$) achieves lower Generation~7 perplexity than Uncurated ($47.04 \\pm 2.90$, $n{=}3$), a reduction of 8.2\\% consistent across all three seeds. However, this cross-budget comparison conflates any selection benefit with a data quantity effect (50\\% vs.\\ 100\\%), and the difference does not reach conventional significance ($p = 0.133$, Welch's $t$-test). We report it as a directional observation rather than a confirmed finding, and draw no causal inference about budget effects from this comparison alone.\n\nIf confirmed with additional statistical power, this result would suggest that training on a random 50\\% subset provides mild regularization compared to using all generated data, consistent with observations that data pruning can improve generalization even without informed selection \\citep{sorscher2022beyond}.\n\nWhile the perplexity difference remains directional, Random~50\\% shows a statistically significant advantage in lexical diversity: its Generation~7 rare n-gram ratio ($0.0098 \\pm 0.0003$) exceeds Uncurated ($0.0090 \\pm 0.0004$) with $p = 0.025$ (two-sided $t$-test, $n{=}3$). Even uninformed subsampling preserves content diversity better than retaining all generated data, suggesting that merely reducing the volume of self-generated training data slows lexical tail erosion.\n\n\\subsection{Lexical Diversity Collapse Across Methods}\n\\label{sec:result_diversity}\n\nRGDS exhibits the sharpest decline in rare token ratio, dropping from approximately 0.010 at Generation~0 to $0.0061 \\pm 0.0009$ at Generation~7 (Table~\\ref{tab:gen7_summary}). The remaining methods converge to a narrower band: Random~50\\% ($0.0098 \\pm 0.0003$), Uncurated ($0.0090 \\pm 0.0004$), and External-only ($0.0102 \\pm 0.0004$). Relative to the WikiText-103 baseline rare token ratio of approximately 0.029, all non-RGDS methods exhibit roughly 65\\% lexical tail erosion by Generation~7; RGDS reaches approximately 80\\%.\n\nUnlike the perplexity-level normal cluster (ANOVA $p = 0.219$; \\S\\ref{sec:result_c1}), the rare n-gram differences among non-RGDS methods are statistically significant (ANOVA $p = 0.007$, $n{=}3$ per method). In particular, Uncurated retains significantly fewer rare n-grams than Random~50\\% ($p = 0.025$, two-sided $t$-test). Lexical diversity collapse is primarily driven by the iterative self-training loop itself \\citep{shumailov2024ai}, but the degree of erosion is modulated by data selection: even uninformed curation (random subsampling) provides measurable protection relative to using all generated data. RGDS is distinctive in accelerating this inherent degradation far beyond all other methods.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrrl}\n\\toprule\nComparison & Metric & $\\Delta$ & Welch $t$ & df & $p$ & Cohen's $d$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{RGDS vs.\\ non-RGDS methods}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$31.10 & 6.88 & 2.1 & .017 & 5.61 \\\\\nRGDS vs.\\ External-only & PPL & $+$27.93 & 5.86 & 2.6 & .015 & 4.78 \\\\\nRGDS vs.\\ Uncurated & PPL & $+$27.25 & 5.73 & 2.6 & .016 & 4.68 \\\\\nRGDS vs.\\ Random 50\\% & Rare & $-$.0038 & $-$6.93 & 2.3 & .014 & $-$5.66 \\\\\nRGDS vs.\\ External-only & Rare & $-$.0042 & $-$7.51 & 2.6 & .008 & $-$6.13 \\\\\nRGDS vs.\\ Uncurated & Rare & $-$.0029 & $-$5.16 & 2.6 & .020 & $-$4.22 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Within-cluster comparisons}} \\\\\nExternal vs.\\ Random 50\\% & PPL & $+$3.17 & 1.67 & 2.9 & .198 & 1.36 \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$3.86 & $-$2.07 & 2.9 & .133 & $-$1.69 \\\\\nRandom 50\\% vs.\\ Uncurated & Rare & $+$.0009 & 3.47 & 3.6 & .030 & 2.84 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{ANOVA (one-way)}} \\\\\nNon-RGDS (3 methods) & PPL & --- & $F{=}1.98$ & 2,\\,6 & .219 & --- \\\\\nNon-RGDS (3 methods) & Rare & --- & $F{=}13.01$ & 2,\\,6 & .007 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$15.15 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ External-only & PPL & $+$7.90 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$2.81 & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n\nRankMe values at Generation~7 are comparable across all methods (289--293; Table~\\ref{tab:gen7_summary}), with no method showing a meaningfully different value ($292.54 \\pm 5.91$ for RGDS vs.\\ ${\\sim}290$ for non-RGDS methods). The metric designed to track effective embedding dimensionality does not distinguish between catastrophically degraded RGDS and the normally performing alternatives, indicating that embedding structural properties can persist even as the space loses content-discriminative fidelity.\n\n\\subsection{Scaling to GPT2-Medium (355M)}\n\\label{sec:result_scaling}\n\nResults from GPT2-Medium (355M) confirm that model collapse generalizes to larger models and is substantially amplified. Table~\\ref{tab:medium_comparison} reports Generation~7 perplexity for all four methods (seed=42 and seed=123 complete for all four methods; all seed=456 experiments pending).%\n%TODO(355M-seeds): update when Random seed=123 and all seed=456 complete\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Budget & PPL$_{42}$ & PPL$_{123}$ & $n$ \\\\\n\\midrule\nRandom 50\\% & 50\\% & 70.25 & 72.55 & 2 \\\\\nExternal-only & 50\\% & 77.74 & 79.56 & 2 \\\\\nRGDS & 50\\% & 82.84 & 90.25 & 2 \\\\\nUncurated & 100\\% & 91.66 & 87.05 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GPT2-Medium (355M) Generation~7 perplexity by seed. PPL$_{42}$ and PPL$_{123}$: WikiText-103 validation perplexity for each seed. RGDS and Uncurated ordering flips across seeds (82.84 vs.\\ 91.66 at seed=42; 90.25 vs.\\ 87.05 at seed=123). All seed=456 experiments are pending.}\n\\label{tab:medium_comparison}\n\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
    "structuredPatch": [
      {
        "oldStart": 110,
        "oldLines": 7,
        "newStart": 110,
        "newLines": 7,
        "lines": [
          " Random 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method; GPT2-Medium rows: seed=42 only ($n{=}1$), all seed=456 experiments pending. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). $^\\dagger$seed=42 only (all seed=456 experiments pending). $^\\ddagger$RGDS vs.\\ Uncurated ordering flips across seeds: $-$8.82 at seed=42, $+$3.20 at seed=123.}",
          "+\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). 355M: $n{=}2$ seeds (42, 123); seed=456 pending; $t$-tests deferred until $n \\geq 3$.}",
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

_source line 30_

Now let me verify the final state and check §5.7 consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "0849b75d-df35-489d-aa54-ce53100a650b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwuEXuBuAEpHHbx5CjqyXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 37635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 744
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_017LXT8wtokQynTMWeRyP99Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "offset": 105,
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
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "c7ba4e41-88e4-42b4-b06f-d13584e98ef2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwuEXuBuAEpHHbx5CjqyXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 37635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 744
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

_source line 32 · 2026-05-14T08:43:49.058Z_

<details><summary>↩ Tool result · `toolu_017LXT8wtokQynTMWeRyP99Z`</summary>

```text
105	\midrule
106	\multicolumn{7}{l}{\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\
107	RGDS vs.\ Random 50\% & PPL & $+$15.15 & \multicolumn{3}{c}{---} & --- \\
108	RGDS vs.\ External-only & PPL & $+$7.90 & \multicolumn{3}{c}{---} & --- \\
109	RGDS vs.\ Uncurated & PPL & $-$2.81 & \multicolumn{3}{c}{---} & --- \\
110	Random 50\% vs.\ Uncurated & PPL & $-$17.96 & \multicolumn{3}{c}{---} & --- \\
111	\bottomrule
112	\end{tabular}
113	\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). 355M: $n{=}2$ seeds (42, 123); seed=456 pending; $t$-tests deferred until $n \geq 3$.}
114	\label{tab:stat_tests}
115	\end{table*}
116	
117	\subsection{Representation Metrics Do Not Track Content Collapse}
118	\label{sec:result_rankme}
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "70fc522d-d60a-4599-9233-14c80c38cb6e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
      "content": "\\midrule\n\\multicolumn{7}{l}{\\textit{GPT2-Medium (355M)---$n{=}2$ seeds (42, 123); seed=456 pending}} \\\\\nRGDS vs.\\ Random 50\\% & PPL & $+$15.15 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ External-only & PPL & $+$7.90 & \\multicolumn{3}{c}{---} & --- \\\\\nRGDS vs.\\ Uncurated & PPL & $-$2.81 & \\multicolumn{3}{c}{---} & --- \\\\\nRandom 50\\% vs.\\ Uncurated & PPL & $-$17.96 & \\multicolumn{3}{c}{---} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise statistical comparisons at Generation~7. GPT2-125M rows: $n{=}3$ seeds per method. All pairwise tests use Welch's $t$-test (two-sided, unequal variance). PPL: perplexity on WikiText-103 validation set. Rare: rare trigram ratio. $\\Delta$: difference (row method $-$ column method for pairwise; not applicable for ANOVA). Cohen's $d$: standardized effect size. RGDS differs significantly from all non-RGDS methods on both metrics ($p < .05$, $|d| > 4$). Within the non-RGDS cluster, PPL differences are not significant (ANOVA $p = .219$), but rare n-gram differences are (ANOVA $p = .007$). 355M: $n{=}2$ seeds (42, 123); seed=456 pending; $t$-tests deferred until $n \\geq 3$.}\n\\label{tab:stat_tests}\n\\end{table*}\n\n\\subsection{Representation Metrics Do Not Track Content Collapse}\n\\label{sec:result_rankme}\n",
      "numLines": 15,
      "startLine": 105,
      "totalLines": 153
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_0127UJyC9LN8jjNbn2sqQBrg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
  "offset": 143,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "ff35e198-cd91-4e78-a9d4-2f315223b8a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeG2Sy5jSVAnYWyNa64x8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 38379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 680
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

_source line 34 · 2026-05-14T08:43:52.197Z_

<details><summary>↩ Tool result · `toolu_0127UJyC9LN8jjNbn2sqQBrg`</summary>

```text
143	\end{table}
144	
145	\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\% (71.40) by +21\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%
146	%TODO(355M-seeds): report significance with seed=456
147	
148	\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\ 91.66) but underperforms at seed=123 (90.25 vs.\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\% ($74.29$ vs.\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \S\ref{sec:discuss_scaling}. The cross-budget comparison (50\% vs.\ 100\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\ Random~50\%, both at 50\%) isolates the effect of the selection mechanism.%
149	%TODO(355M-seeds): update with seed=456 data
150	
151	\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\% perplexity penalty relative to Random (vs.\ +72\% at 125M) is consistent with this narrower gap.%
152	%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "29cfb64f-4100-4563-8a91-12028a92d75f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/results.tex",
      "content": "\\end{table}\n\n\\paragraph{C3 holds across scale.} The RGDS two-seed mean (86.55) underperforms Random~50\\% (71.40) by +21\\% at 355M ($n{=}2$), confirming that internal-embedding diversity selection degrades performance relative to uninformed random sampling regardless of model size. The gap is narrower than at 125M (+72\\%, $n{=}3$), but the direction is consistent: co-degrading embeddings produce systematically worse selection than random chance.%\n%TODO(355M-seeds): report significance with seed=456\n\n\\paragraph{Relative severity shifts at 355M.} At 355M, model collapse is substantially more severe than at 125M across all methods. RGDS and Uncurated converge into a narrow, overlapping band (PPL 83--92) with unstable ordering across seeds: RGDS outperforms Uncurated at seed=42 (82.84 vs.\\ 91.66) but underperforms at seed=123 (90.25 vs.\\ 87.05). This ordering instability contrasts sharply with the 125M setting, where RGDS consistently exceeded Uncurated by 58\\% ($74.29$ vs.\\ $47.04$, $n{=}3$). The compression of method differences at high absolute collapse severity is consistent with both the representational redundancy and floor-compression hypotheses discussed in \\S\\ref{sec:discuss_scaling}. The cross-budget comparison (50\\% vs.\\ 100\\%) remains confounded by data volume differences and should not be interpreted causally. Only the within-budget comparison (RGDS vs.\\ Random~50\\%, both at 50\\%) isolates the effect of the selection mechanism.%\n%TODO(355M-seeds): update with seed=456 data\n\n\\paragraph{Alignment gap narrows but persists.} The RGDS selection ratio at Generation~7 is $0.85 \\pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123), compared to $0.64 \\pm 0.20$ at 125M ($n{=}3$). The ratio remains below~1.0---RGDS still preferentially retains content-poor samples---but the inversion is less severe. The +21\\% perplexity penalty relative to Random (vs.\\ +72\\% at 125M) is consistent with this narrower gap.%\n%TODO(355M-seeds): confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验\n",
      "numLines": 11,
      "startLine": 143,
      "totalLines": 153
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

§5.7 验证通过：

- Line 145: RGDS mean=86.55, Random=71.40, +21% — (86.55−71.40)/71.40×100=21.2% ✓
- Line 151: +21% perplexity penalty ✓
- Table 3 (tab:medium_comparison) 已有两 seed 的 per-seed 数据 ✓

完成的修改：

1. **Table 2 355M Δ 值**：+12.59→+15.15, −21.41→−17.96, −8.82/+3.20→−2.81；新增 RGDS vs External-only +7.90
2. **355M 节标题**：`statistical tests pending ≥3 seeds` → `n=2 seeds (42, 123); seed=456 pending`
3. **脚注**：移除 †/‡ 标注，替换为 `355M: n=2 seeds (42, 123); seed=456 pending; t-tests deferred until n≥3`
4. **§5.7**：已有数字与 Table 2 一致，无需改动

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "uuid": "18267e5a-1bb6-42da-a00b-58b5f8bc6199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194TgHdURMeGnj3UjyK4Tpv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 39059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 36_

§5.7 验证通过：

- Line 145: RGDS mean=86.55, Random=71.40, +21% — (86.55−71.40)/71.40×100=21.2% ✓
- Line 151: +21% perplexity penalty ✓
- Table 3 (tab:medium_comparison) 已有两 seed 的 per-seed 数据 ✓

完成的修改：

1. **Table 2 355M Δ 值**：+12.59→+15.15, −21.41→−17.96, −8.82/+3.20→−2.81；新增 RGDS vs External-only +7.90
2. **355M 节标题**：`statistical tests pending ≥3 seeds` → `n=2 seeds (42, 123); seed=456 pending`
3. **脚注**：移除 †/‡ 标注，替换为 `355M: n=2 seeds (42, 123); seed=456 pending; t-tests deferred until n≥3`
4. **§5.7**：已有数字与 Table 2 一致，无需改动

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 131371,
  "duration_api_ms": 132187,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "203ff529-afe9-4aa9-b4ee-d6516b1fee11",
  "total_cost_usd": 0.55761875,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 28003,
    "cache_read_input_tokens": 360802,
    "output_tokens": 8025,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28003,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 308,
        "cache_read_input_tokens": 39059,
        "cache_creation_input_tokens": 785,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 785
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1394,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0015040000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 8025,
      "cacheReadInputTokens": 360802,
      "cacheCreationInputTokens": 28003,
      "webSearchRequests": 0,
      "costUSD": 0.5561147500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bfad17bf-8e50-4553-ac43-40a0cce985fa"
}
```

</details>

---
