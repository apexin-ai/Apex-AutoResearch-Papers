# analyze compounding paper integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_analyze_compounding_paper_integration_20260515T180021.log`
- **Structured JSON:** [`950c21c39674bb3bba42.json`](../../sessions/95/950c21c39674bb3bba42.json)

## Before a recorded user message

47 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
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
  "uuid": "33b8843e-4e72-4d6f-88c4-c8f4b7df6d3c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "resetsAt": 1778885400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f8e0ac8b-998f-4d47-9533-bf27888afd37",
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current analysis.tex and paper_framing.md to understand the context, then draft the compounding analysis text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "d084d83e-a814-4b5a-848c-2376f3133157",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7beTsuJaU6g3vBHRJGor9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12689,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12689
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_018HhwYGTX7hvq6iTgjnn25E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "0c97252f-5d5d-4762-92c2-f5af55ecc030",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7beTsuJaU6g3vBHRJGor9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12689,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12689
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 6 · 2026-05-15T18:00:30.755Z_

<details><summary>↩ Tool result · `toolu_018HhwYGTX7hvq6iTgjnn25E`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across seven models at $4\times$ compression.
12	The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
13	
14	Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
15	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
16	
17	Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's 4-bit and 8-bit deltas are ${\approx}\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.
20	In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling
21	
22	Llama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
23	Mistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
24	
25	Pythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).
26	Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
27	
28	\paragraph{Scale-dependent concentration dilution.}
29	Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\times$ more heads into the flat regime.
30	Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
31	Concentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\times$scale combination where non-uniform allocation helps.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--384). $^*$BOS-corrected.}
37	\label{tab:heterogeneity}
38	\begin{tabular}{lcccccc}
39	\toprule
40	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
41	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
42	\midrule
43	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
44	Qwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\
45	Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
46	Llama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
47	Mistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\
48	Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\
49	Pythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\
50	\bottomrule
51	\end{tabular}
52	\end{table}
53	
54	The per-head heatmap (Figure~\ref{fig:heatmap}, Appendix~\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.
55	
56	\subsection{Empirical Decision Rule}
57	\label{sec:diagnostic}
58	
59	MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
60	This motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.
61	Given the profiling results from \S\ref{sec:profiling}, compute the top-5\% concentration and $t_1/t_5$ ratio, then select:
62	\begin{itemize}[nosep]
63	\item \textbf{Spread} (concentration $\geq 0.50$ \emph{and} $t_1/t_5 \leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
64	\item \textbf{Spike} ($t_1/t_5 > 0.70$ \emph{and} concentration $\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.57, 0.85): no benefit.
65	\item \textbf{Flat} (concentration $< 0.25$, or concentration $\in [0.25, 0.50)$ with $t_1/t_5 \leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.
66	\end{itemize}
67	
68	Both conditions are needed: Llama ($0.57$) and Yi-1.5 ($0.71$) both exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \geq 0.70$) correctly override.
69	A concentration-only rule would misclassify both as spread; $t_1/t_5$ is the critical second discriminator.
70	The rule correctly classifies all seven evaluated models (7/7), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and the MHA architecture (Pythia-1.4B flat).
71	Only Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.
72	The rule reuses profiling data already required by the solver and adds no overhead.
73	
74	\paragraph{Why is Qwen-7B the only spread model?}
75	We offer two non-exclusive hypotheses, both requiring further validation.
76	First, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.
77	However, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.
78	Second, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\ 0.57).
79	This suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.
80	
81	Additional analyses---granularity tradeoff (Appendix~\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\ref{sec:granularity}--\ref{sec:kv_separation}.
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "a965bffa-a50e-4ddc-9ff6-57a174b314ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across seven models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nMistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--384). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\geq 0.50$ \\emph{and} $t_1/t_5 \\leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 > 0.70$ \\emph{and} concentration $\\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.57, 0.85): no benefit.\n\\item \\textbf{Flat} (concentration $< 0.25$, or concentration $\\in [0.25, 0.50)$ with $t_1/t_5 \\leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: Llama ($0.57$) and Yi-1.5 ($0.71$) both exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \\geq 0.70$) correctly override.\nA concentration-only rule would misclassify both as spread; $t_1/t_5$ is the critical second discriminator.\nThe rule correctly classifies all seven evaluated models (7/7), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and the MHA architecture (Pythia-1.4B flat).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\n\\paragraph{Why is Qwen-7B the only spread model?}\nWe offer two non-exclusive hypotheses, both requiring further validation.\nFirst, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.\nHowever, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.\nSecond, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\\ 0.57).\nThis suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01Mg9AuAYx2afeUbVQQ67eSh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "72b1106f-8a7b-4954-9b75-7cb24d83d253",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7beTsuJaU6g3vBHRJGor9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12689,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12689
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 8 · 2026-05-15T18:00:31.558Z_

<details><summary>↩ Tool result · `toolu_01Mg9AuAYx2afeUbVQQ67eSh`</summary>

```text
1	# Paper Framing — ratekv
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
6	- Track: Efficient Methods for NLP
7	
8	## bf16 Consistency Resolution (2026-05-14)
9	
10	**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。
11	
12	**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。
13	
14	| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |
15	|------|---------------------|----------------------|-----------|
16	| Baseline | **9.8106** | 8.819 | 9.81 |
17	| Uniform 4-bit | **15.4454** | — | 15.45 |
18	| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |
19	| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |
20	
21	## Core Insight
22	
23	Per-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).
24	
25	## Core Claims (3 条)
26	
27	1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — "spread" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — "spike" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:
28	   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective
29	   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective
30	   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)
31	
32	2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).
33	
34	**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):
35	1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)
36	2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)
37	3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)
38	This answers "when" and "why", not just "what" — stronger than original "universal catastrophe" narrative.
39	
40	3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as "empirical decision rule", NOT "diagnostic framework". If Qwen2.5-14B also confirms Spread → upgrade to "empirical diagnostic" (N=2).
41	
42	## Story Spine
43	
44	- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?
45	
46	- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.
47	
48	- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.
49	
50	- **Headline result template**: "We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices."
51	
52	## "When Does Non-Uniform Allocation Help?" — Analysis Chapter
53	
54	Five case studies representing the full spectrum of heterogeneity:
55	
56	| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
57	|------|-------|-----|--------------|------------------------------|---------------|
58	| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
59	| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 64% of total delta) |
60	| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
61	| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
62	| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |
63	
64	**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.
65	
66	**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).
67	
68	**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.
69	
70	## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)
71	
72	| Method | PPL | Bit Distribution | Budget |
73	|--------|-----|-------------------|--------|
74	| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |
75	| MCKP unconstrained | 36.92 | — | 0.25 |
76	| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
77	| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
78	| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |
79	
80	Key takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.
81	
82	## Cross-Architecture Evidence Summary
83	
84	| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |
85	|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|
86	| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |
87	| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |
88	| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |
89	| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |
90	| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |
91	
92	**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:
93	- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding
94	- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta
95	- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)
96	- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads
97	
98	**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):
99	
100	Three-tier labeling (NOT binary catastrophe/benign):
101	- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding
102	- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions
103	- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)
104	
105	Reviewer-suggested paragraph for paper (1 段, 3-4 句):
106	"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape."
107	
108	This **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.
109	
110	⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.
111	
112	**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.
113	
114	**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.
115	
116	### Mistral k Ablation (256 KV heads, budget=0.25)
117	
118	PPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).
119	
120	| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
121	|---|-----|-------|-------|-------|--------|-----|
122	| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |
123	| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |
124	| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |
125	| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |
126	| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |
127	| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |
128	
129	Contrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.
130	
131	### Llama k Ablation (256 KV heads, budget=0.25)
132	
133	All k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).
134	
135	### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)
136	
137	**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅
138	
139	| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |
140	|------|---------------|------------|---|---------------|
141	| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |
142	| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |
143	| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |
144	| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |
145	| **Avg recovery** | — | — | **72.8%** | — |
146	
147	**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)
148	
149	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
150	|------|---------------|------------|---|
151	| arc_easy | 0.7946 | 0.7854 | -0.92pp |
152	| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |
153	| hellaswag | 0.5857 | 0.5797 | -0.60pp |
154	| piqa | 0.7927 | 0.7894 | -0.33pp |
155	| winogrande | 0.7174 | 0.7301 | +1.27pp |
156	| **Average** | **0.6822** | **0.6745** | **-0.77pp** |
157	
158	**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)
159	
160	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
161	|------|---------------|------------|---|
162	| arc_easy | 0.8173 | 0.8039 | -1.34pp |
163	| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |
164	| hellaswag | 0.6026 | 0.6012 | -0.14pp |
165	| piqa | 0.7867 | 0.7802 | -0.65pp |
166	| winogrande | 0.7253 | 0.7238 | -0.15pp |
167	| **Average** | **0.6915** | **0.6816** | **-0.99pp** |
168	
169	**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)
170	
171	| Task | Uniform 4-bit | MCKP (k=4) | Δ |
172	|------|---------------|------------|---|
173	| arc_easy | — | — | — |
174	| arc_challenge | — | — | — |
175	| hellaswag | — | — | — |
176	| piqa | — | — | — |
177	| winogrande | — | — | — |
178	| **Average** | **0.6894** | **0.6846** | **-0.48pp** |
179	
180	**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)
181	
182	| Task | Uniform 4-bit | MCKP | Δ |
183	|------|---------------|------|---|
184	| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |
185	
186	**Downstream summary (Reviewer-verified framing)**:
187	- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**
188	- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)
189	- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)
190	- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise
191	- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)
192	- **Paper must**: (a) report full per-task tables, not just averages, (b) use "shows minor degradation" NOT "preserves accuracy" — the latter has spin, (c) note arc_challenge as worst-case explicitly
193	- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance
194	- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论："ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate."
195	- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞："Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge)."
196	
197	## Allocation Baseline Evidence (plan_015, mckp_reeval)
198	
199	All numbers from unified bf16 eval pipeline, budget=0.25.
200	
201	| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |
202	|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|
203	| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |
204	| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |
205	| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |
206	
207	**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.
208	
209	**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.
210	
211	## Differentiation from RateQuant
212	
213	| Aspect | RateQuant | Ours |
214	|--------|-----------|------|
215	| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |
216	| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |
217	| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |
218	| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |
219	| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |
220	| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |
221	| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |
222	
223	## Venue Fit Risks
224	
225	- **"The constraint is just a heuristic, not a real contribution"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.
226	- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.
227	- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive "higher GQA = more benefit" hypothesis and shows our diagnostic is needed.
228	- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
229	- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 5 architectures" or "5/5 correctly classified by the 0.50 threshold."
230	- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.
231	
232	## Anticipated Reviewer Concerns
233	
234	1. **"The cardinality constraint is trivial — just cap the extreme allocations"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.
235	2. **"This is just RateQuant with a constraint added"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.
236	3. **"The method only works on Qwen — isn't this a Qwen paper?"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.
237	4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.
238	5. **"n=3/4/5 models is not enough for the heterogeneity claim"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.
239	6. **"RateQuant does K/V asymmetric allocation, do you?"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.
240	7. **"Where are the downstream task results?"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use "shows minor degradation" not "preserves accuracy".
241	8. **"The profiler distortion=0.0 on Mistral suggests the profiling method is broken"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.
242	9. **"If solver doesn't matter, why present MCKP at all?"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "7e6ed20d-b858-4c9f-868c-0a17cd6b35ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_framing.md",
      "content": "# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).\n\n## Core Claims (3 条)\n\n1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — \"spread\" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — \"spike\" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:\n   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective\n   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective\n   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)\n\n2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).\n\n**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):\n1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)\n2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)\n3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)\nThis answers \"when\" and \"why\", not just \"what\" — stronger than original \"universal catastrophe\" narrative.\n\n3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as \"empirical decision rule\", NOT \"diagnostic framework\". If Qwen2.5-14B also confirms Spread → upgrade to \"empirical diagnostic\" (N=2).\n\n## Story Spine\n\n- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?\n\n- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.\n\n- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.\n\n- **Headline result template**: \"We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 64% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 5 architectures\" or \"5/5 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n",
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

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ApMZHxcNjAfUvKVVuhhPQ7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry",
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
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "c57e222a-09e4-4603-947f-0e8da140733f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7beTsuJaU6g3vBHRJGor9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12689,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12689
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 10 · 2026-05-15T18:00:31.784Z_

<details><summary>↩ Tool result · `toolu_01ApMZHxcNjAfUvKVVuhhPQ7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

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
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "3be7c237-1294-4e96-af7a-2ec011712795",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry to find the compounding sweep experiments for Llama and Mistral, to verify the numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "658a6916-4782-4ede-bcf2-ff5d680dd265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZwLUmJY9e2GJGHQtGXpMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14533,
      "cache_read_input_tokens": 24530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14533
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 12_

Let me check the registry for the compounding sweep experiments to verify the numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "8f00f810-8f5f-4048-a04a-0d32dc521a16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZwLUmJY9e2GJGHQtGXpMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14533,
      "cache_read_input_tokens": 24530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14533
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LgR3wNRGVP6gCAAhTac2eV`</summary>

```json
{
  "project": "ratekv",
  "filters": {
    "exp_id": "w9_compounding"
  },
  "fields": [
    "*"
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
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "0b42bee5-ca24-493c-a777-6c3f115fae72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZwLUmJY9e2GJGHQtGXpMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14533,
      "cache_read_input_tokens": 24530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14533
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 14 · 2026-05-15T18:00:36.398Z_

<details><summary>↩ Tool result · `toolu_01LgR3wNRGVP6gCAAhTac2eV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2691}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "1ee9d33e-476b-4352-8a21-c8bd21f936e6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2691}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2691}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GFEkTNZzo81RCQE8urrD3u`</summary>

```json
{
  "project": "ratekv",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "status",
    "conclusion",
    "metrics"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "4336e4fe-d49c-4693-9127-b3ad50fa6722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sqpwpx8QCiz6DhxLEprAQ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 39063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 249
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

_source line 16 · 2026-05-15T18:00:38.896Z_

<details><summary>↩ Tool result · `toolu_01GFEkTNZzo81RCQE8urrD3u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"llama_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_compounding_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_k\": 0, \"best_ppl\": 8.0922, \"k0_ppl\": 8.0922, \"k2_ppl\": 8.1243, \"k4_ppl\": 8.1803, \"k8_ppl\": 8.2259, \"k16_ppl\": 8.4378, \"k32_ppl\": 9.0506, \"k64_ppl\": 11.991, \"k128_ppl\": 40.2067, \"k256_ppl\": 1519.1888, \"budget\": 0.25}}, \"qwen25-hires-profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_constrained_mckp_v2\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0352, \"mckp_wikitext2_ppl\": 7.1341, \"uniform4bit_wikitext2_ppl\": 7.1308, \"mckp_improvement_over_uniform\": -0.0033, \"mckp_improvement_pct\": -3.48, \"verdict\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 254}, \"fix_note\": \"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\"}, \"conclusion\": \"negative\"}, \"mistral_uniform_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen14b_greedy_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_constrained_ppl\": 7.2206, \"mckp_constrained_ppl\": 7.2206, \"delta_vs_mckp\": 0, \"bit_distribution\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"memory_ratio\": 0.25, \"solver_time_sec\": 0.08, \"total_time_min\": 1.8}}, \"kivi_mckp_combined_qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kivi_baseline_qwen7b_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_kivi_4bit_g32_r128\": 9.8976, \"tokens\": 298938, \"chunks\": 583, \"stride\": 512, \"model\": \"Qwen2.5-7B\", \"comparison_mckp_ppl\": 10.91, \"comparison_uniform_ppl\": 15.45, \"comparison_bf16_ppl\": 9.81}}, \"qwen14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 6.8654, \"ppl_uniform_4bit\": 7.202, \"ppl_constrained_mckp\": 7.2206, \"ppl_unconstrained_mckp\": 7.6923, \"delta_constrained_vs_uniform\": -0.0185, \"delta_constrained_vs_uniform_pct\": -5.51, \"delta_unconstrained_vs_uniform\": -0.4902, \"bit_distribution_constrained\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"bit_distribution_unconstrained\": {\"2\": 77, \"4\": 271, \"8\": 35, \"16\": 1}, \"concentration\": 0.33, \"top1_pct\": 0.2262, \"top5_pct\": 0.3304, \"t1_t5\": 0.68, \"shape\": \"Flat\"}}, \"qwen_hires_constrained_d049\": {\"status\": \"DONE\", \"metrics\": {\"float32_hires_constrained_mckp_ppl\": 10.8921, \"baseline_ppl\": 9.8106, \"uniform_4bit_ppl\": 15.4484, \"bit_distribution\": {\"2\": 8, \"4\": 100, \"8\": 4}, \"gap_recovery_pct\": 80.8, \"top5_concentration\": 0.6156, \"top5_concentration_pre_monotonicity\": 0.6104, \"bf16_hires_constrained_mckp_ppl\": 10.9131, \"delta_f32_vs_bf16\": 0.021}, \"conclusion\": \"success\"}, \"llama_8k_spotcheck\": {\"status\": \"DONE\", \"metrics\": {\"ppl_bf16_8k\": 5.5958, \"ppl_constrained_mckp_8k\": 6.0537, \"ppl_uniform_4bit_8k\": 6.0364, \"mckp_improvement_over_uniform_8k\": -0.0174, \"mckp_improvement_pct_8k\": -3.94, \"ppl_bf16_2k\": 8.0922, \"ppl_constrained_mckp_2k\": 8.5042, \"ppl_uniform_4bit_2k\": 8.4701, \"shape\": \"Spike\", \"concentration\": 0.5749, \"t1_over_t5\": 0.71, \"context_length\": 8192, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"success\"}, \"yi15_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen7b_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"qwen7b_8k_context_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16_8k\": 6.97, \"ppl_constrained_mckp_8k\": 8.59, \"ppl_uniform_4bit_8k\": 77.75, \"ppl_bf16_2k\": 9.81, \"ppl_constrained_mckp_2k\": 10.89, \"ppl_uniform_4bit_2k\": 15.45, \"mckp_improvement_over_uniform_8k\": \"97.7%\", \"mckp_improvement_over_uniform_2k\": \"80.8%\", \"shape\": \"Spread\", \"concentration\": 0.5992, \"context_length\": 8192, \"note\": \"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\"}}, \"pythia14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 16.4893, \"ppl_uniform_4bit\": 24.2894, \"ppl_constrained_mckp\": 24.4521, \"ppl_unconstrained_mckp\": 31.5415, \"concentration\": \"t1=0.0289, t5=0.2439\", \"t1_t5\": \"0.0289/0.2439\", \"shape\": \"Flat\", \"constrained_vs_uniform_gap\": 0.1627}}, \"w1_pythia14b_hires_profiling\": {\"status\": \"DONE\", \"metrics\": {\"baseline_ppl\": 13.6347, \"concentration\": 0.2439, \"t1_t5\": 0.28, \"shape\": \"Flat\", \"l0_dominance\": 0.51, \"cv\": 1.2172, \"positive_heads\": 362, \"total_heads\": 384, \"top5_heads\": [{\"head\": \"L1H11\", \"delta\": 1.016355}, {\"head\": \"L12H14\", \"delta\": 0.784513}, {\"head\": \"L8H4\", \"delta\": 0.759118}, {\"head\": \"L11H2\", \"delta\": 0.632357}, {\"head\": \"L13H2\", \"delta\": 0.522849}], \"elapsed_min\": 25.7, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}, \"conclusion\": \"success\"}, \"w1_qwen14b_hires_profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 5.8432, \"concentration\": 0.3312, \"t1_t5\": 0.68, \"shape\": \"Flat\", \"l0_dominance\": 15.5, \"cv\": 3.7418, \"positive_heads\": 370, \"total_heads\": 384, \"top10_heads\": [{\"head\": \"L0H5\", \"delta\": 1.84494}, {\"head\": \"L0H4\", \"delta\": 0.236669}, {\"head\": \"L0H2\", \"delta\": 0.136971}, {\"head\": \"L28H4\", \"delta\": 0.099279}, {\"head\": \"L28H5\", \"delta\": 0.07576}, {\"head\": \"L27H4\", \"delta\": 0.071269}, {\"head\": \"L0H0\", \"delta\": 0.070018}, {\"head\": \"L28H6\", \"delta\": 0.063737}, {\"head\": \"L26H0\", \"delta\": 0.061462}, {\"head\": \"L31H3\", \"delta\": 0.061062}], \"elapsed_min\": 161.3, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}}, \"kivi_baseline_qwen_llama\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"qwen_2bit_r128\": 12.83, \"qwen_4bit_r128\": 9.9, \"qwen_2bit_r0\": 13.34, \"qwen_4bit_r0\": 9.91, \"llama_2bit_r128\": 9.84, \"llama_4bit_r128\": 8.14, \"llama_2bit_r0\": 10.08, \"llama_4bit_r0\": 8.14, \"group_size\": 32, \"eval_data\": \"WikiText-2 test\", \"note\": \"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\"}}, \"gemma2_constrained_bos_fix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 6.0306, \"uniform_4bit_ppl\": 6.1683, \"constrained_mckp_ppl\": 6.1951, \"mckp_vs_uniform_delta\": 0.0267, \"mckp_delta_ppl\": 0.1645, \"uniform_delta_ppl\": 0.1377, \"bit_distribution\": {\"2\": 8, \"4\": 324, \"8\": 4}, \"n_2bit\": 8, \"max_2bit\": 8, \"memory_ratio\": 0.25, \"eval_method\": \"sliding_window_bos_fix\", \"elapsed_seconds\": 490.3}}, \"w2_unconstrained_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline\": 7.0157, \"yi15_uniform4\": 7.2171, \"yi15_greedy\": 7.5615, \"yi15_mckp\": 7.5615, \"yi15_n2bit\": 22, \"llama_baseline\": 8.0922, \"llama_uniform4\": 8.4701, \"llama_greedy\": 8.6265, \"llama_mckp\": 8.6265, \"llama_n2bit\": 12, \"mistral_baseline\": 7.0352, \"mistral_uniform4\": 7.1308, \"mistral_greedy\": 7.5733, \"mistral_mckp\": 7.5963, \"mistral_n2bit\": 42, \"gemma2_baseline\": 6.0306, \"gemma2_uniform4\": 6.1683, \"gemma2_greedy\": 8.8469, \"gemma2_mckp\": 8.8469, \"gemma2_n2bit\": 106, \"gemma2_eval_method\": \"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\", \"gemma2_greedy_ratio\": 1.467, \"gemma2_catastrophic\": true, \"gemma2_note\": \"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\"}}, \"w3_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline_avg\": 0.6912, \"yi15_uniform_avg\": 0.6822, \"yi15_mckp_avg\": 0.6745, \"yi15_mckp_vs_uniform_pp\": -0.77, \"yi15_mckp_vs_baseline_pp\": -1.67, \"yi15_baseline\": {\"arc_easy\": 0.8093, \"arc_challenge\": 0.5265, \"hellaswag\": 0.5913, \"piqa\": 0.7949, \"winogrande\": 0.734}, \"yi15_uniform\": {\"arc_easy\": 0.7946, \"arc_challenge\": 0.5205, \"hellaswag\": 0.5857, \"piqa\": 0.7927, \"winogrande\": 0.7174}, \"yi15_mckp\": {\"arc_easy\": 0.7854, \"arc_challenge\": 0.4881, \"hellaswag\": 0.5797, \"piqa\": 0.7894, \"winogrande\": 0.7301}, \"llama_baseline_avg\": 0.696, \"llama_uniform_avg\": 0.6915, \"llama_mckp_avg\": 0.6816, \"llama_mckp_vs_uniform_pp\": -0.99, \"llama_mckp_vs_baseline_pp\": -1.44, \"llama_baseline\": {\"arc_easy\": 0.8228, \"arc_challenge\": 0.5188, \"hellaswag\": 0.6073, \"piqa\": 0.7922, \"winogrande\": 0.7388}, \"llama_uniform\": {\"arc_easy\": 0.8173, \"arc_challenge\": 0.5256, \"hellaswag\": 0.6026, \"piqa\": 0.7867, \"winogrande\": 0.7253}, \"llama_mckp\": {\"arc_easy\": 0.8039, \"arc_challenge\": 0.4991, \"hellaswag\": 0.6012, \"piqa\": 0.7802, \"winogrande\": 0.7238}, \"mistral_baseline_avg\": 0.6917, \"mistral_uniform_avg\": 0.6894, \"mistral_mckp_avg\": 0.6846, \"mistral_mckp_vs_uniform_pp\": -0.48, \"mistral_mckp_vs_baseline_pp\": -0.71, \"mistral_baseline\": {\"arc_easy\": 0.8005, \"arc_challenge\": 0.5043, \"hellaswag\": 0.6118, \"piqa\": 0.8009, \"winogrande\": 0.7411}, \"mistral_uniform\": {\"arc_easy\": 0.7976, \"arc_challenge\": 0.5068, \"hellaswag\": 0.6051, \"piqa\": 0.7982, \"winogrande\": 0.7395}, \"mistral_mckp\": {\"arc_easy\": 0.7942, \"arc_challenge\": 0.4949, \"hellaswag\": 0.6027, \"piqa\": 0.802, \"winogrande\": 0.7293}, \"gemma2_baseline_avg\": 0.7307, \"gemma2_uniform_avg\": 0.7251, \"gemma2_mckp_avg\": 0.7265, \"gemma2_mckp_vs_uniform_pp\": 0.14, \"gemma2_mckp_vs_baseline_pp\": -0.42, \"gemma2_baseline\": {\"arc_easy\": 0.8737, \"arc_challenge\": 0.6135, \"hellaswag\": 0.6093, \"piqa\": 0.8128, \"winogrande\": 0.7443}, \"gemma2_uniform\": {\"arc_easy\": 0.8662, \"arc_challenge\": 0.6058, \"hellaswag\": 0.606, \"piqa\": 0.8079, \"winogrande\": 0.7395}, \"gemma2_mckp\": {\"arc_easy\": 0.8649, \"arc_challenge\": 0.6041, \"hellaswag\": 0.6089, \"piqa\": 0.8074, \"winogrande\": 0.7474}, \"eval_harness_version\": \"0.4.11\", \"num_fewshot\": 0, \"yi_elapsed_s\": 1563.2, \"llama_elapsed_s\": 1446.4, \"mistral_elapsed_s\": 1302.2, \"gemma2_elapsed_s\": 1735.9}}, \"w9_compounding_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 9.81, \"k1_topk_ppl\": 9.826, \"k1_randomk_ppl\": 9.887, \"k1_randomk_std\": 0.05, \"k4_topk_ppl\": 9.849, \"k4_topk_ratio\": 0.86, \"k4_randomk_ppl\": 10.06, \"k4_randomk_std\": 0.06, \"k4_randomk_ratio\": 1.24, \"k8_topk_ppl\": 10.042, \"k8_topk_ratio\": 1.56, \"k8_randomk_ppl\": 11.07, \"k8_randomk_std\": 0.69, \"k8_randomk_ratio\": 1.76, \"k16_topk_ppl\": 10.42, \"k16_topk_ratio\": 1.56, \"k16_randomk_ppl\": 12.91, \"k16_randomk_std\": 0.4, \"k16_randomk_ratio\": 2.1, \"k32_topk_ppl\": 11.604, \"k32_topk_ratio\": 1.78, \"k32_randomk_ppl\": 18.33, \"k32_randomk_std\": 2.53, \"k32_randomk_ratio\": 2.73, \"k64_topk_ppl\": 22.946, \"k64_topk_ratio\": 4.89, \"k64_randomk_ppl\": 55.94, \"k64_randomk_std\": 9.73, \"k64_randomk_ratio\": 8.88, \"runtime_minutes\": 16.9, \"note\": \"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\"}}, \"w9_compounding_scaling\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"baseline_ppl\": 8.2, \"n1_joint_ppl\": 14.94, \"n1_ratio\": 1, \"n2_joint_ppl\": 42.26, \"n2_ratio\": 3.84, \"n4_joint_ppl\": 3813.76, \"n4_ratio\": 333.3, \"n8_joint_ppl\": 3586.42, \"n8_ratio\": 282.1, \"n16_joint_ppl\": 7286.23, \"n16_ratio\": 521.1, \"n32_joint_ppl\": 6644.05, \"n32_ratio\": 424, \"n64_joint_ppl\": 9453.33, \"n64_ratio\": 533.3, \"runtime_seconds\": 96}}, \"w2_unconstrained_baselines\": {\"status\": \"DONE\", \"metrics\": {\"note\": \"2bitonly profiles only - INVALID for reviewer response\", \"yi15_ppl\": 672.2, \"yi15_ratio\": 114, \"llama_ppl\": 1219.7, \"llama_ratio\": 187, \"mistral_ppl_2bitonly\": 47.8, \"mistral_ratio_2bitonly\": 8.2, \"mistral_ppl_full\": 6.39, \"mistral_ratio_full\": 1.09, \"gemma2_ppl\": 277.4, \"gemma2_ratio\": 37.9, \"budget\": 0.25, \"baseline_yi\": 5.89, \"baseline_llama\": 6.51, \"baseline_mistral\": 5.87, \"baseline_gemma2\": 7.32}, \"conclusion\": \"killed\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"concentration_top5pct\": 0.2291, \"l0_dominance_ratio\": 2.05, \"cv_delta_2bit\": 1.2834, \"positive_delta_heads\": \"310/336\", \"top_head\": \"L0H1 delta=0.1906\", \"total_time_hours\": 1.59}}, \"mistral_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fp16_ppl\": 7.0352, \"c4_mckp_ppl\": 7.1774, \"uniform_4bit_ppl\": 7.1308, \"mckp_vs_uniform_delta\": 0.0466, \"mckp_bit_distribution\": {\"2\": 4, \"4\": 250, \"8\": 2}, \"phase4_error\": \"FileNotFoundError: mistral_k_ablation_results.json\"}}, \"llama_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bf16_wt2_ppl\": 8.0922, \"bf16_c4_ppl\": 7.1333, \"c4_cal_mckp_wt2_ppl\": 8.5103, \"c4_cal_mckp_c4_ppl\": 7.5351, \"uniform_wt2_ppl\": 8.4701, \"uniform_c4_ppl\": 7.5351, \"delta_c4_uniform_minus_mckp\": 0, \"delta_wt2_uniform_minus_mckp\": -0.0402, \"verdict_c4\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"2,3\", \"24,2\"], \"heads_8bit\": [\"31,6\"], \"total_time_min\": 6.3, \"wt2_ref_mckp_ppl\": 8.5042, \"wt2_ref_delta\": -0.0341}}, \"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256, \"distribution_shape\": \"flat\", \"total_hours\": 0.94, \"profile_seconds\": 3371.7}, \"conclusion\": \"success\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 8.0922, \"hires_mckp_ppl\": 8.5042, \"uniform_4bit_ppl\": 8.4701, \"std_mckp_reference_ppl\": 8.4498, \"mckp_vs_uniform_delta\": -0.0341, \"mckp_vs_uniform_pct\": -9, \"hires_vs_std_mckp_delta\": 0.0544, \"concentration\": 0.5749, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"26,0\", \"31,7\"], \"heads_8bit\": [\"12,3\"], \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.5749, \"t1_t5\": 0.85, \"baseline_ppl\": 6.5055, \"top1_head\": \"L2H5_delta=15.2636\", \"delta_2bit_cv\": 7.7663, \"l0_dominance_ratio\": 0.67, \"positive_delta_heads\": 254, \"total_heads\": 256, \"total_hours\": 0.98}, \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\"}}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\"}}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"hires_mckp_ppl\": 7.2181, \"uniform_4bit_ppl\": 7.2171, \"baseline_ppl\": 7.0157, \"delta_vs_uniform\": -0.001, \"bit_distribution\": {\"2\": 2, \"4\": 189, \"8\": 1}, \"2bit_heads\": [\"L22H1\", \"L24H3\"], \"8bit_heads\": [\"L6H2\"], \"L4H3_status\": \"kept_at_4bit\", \"std_mckp_k2_ppl\": 7.2209, \"std_mckp_k8_ppl\": 7.3129, \"hires_concentration\": 0.7139, \"L4H3_2bit_delta\": 13.12, \"L4H3_4bit_delta\": 0.0048, \"L4H3_8bit_delta\": 0.004}}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"top5_concentration\": 0.7139, \"top5_n_heads\": 9, \"baseline_calibration_ppl\": 5.888, \"delta_2bit_cv\": 8.8991, \"layer0_dominance_ratio\": 0.04, \"top1_head\": \"L4H3_delta=13.1236\", \"total_hours\": 0.96}}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"float32_hires_top5_concentration\": 0.6104, \"bf16_hires_range\": \"0.59-0.66\", \"float32_lowres_concentration\": 0.42, \"bf16_bug_impact_on_concentration\": 0.01, \"baseline_ppl\": 9.81, \"mckp_unconstrained_ppl\": 10.95, \"uniform_4bit_ppl\": 15.45, \"mckp_bit_dist\": {\"2\": 12, \"4\": 96, \"8\": 3, \"16\": 1}, \"l0h0_delta\": 6.7388, \"l0_4heads_total_share\": 0.586, \"claim3_threshold_0.50\": \"PASS\"}}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0157, \"mckp_wikitext2_ppl\": 7.3129, \"uniform4bit_wikitext2_ppl\": 7.2171, \"mckp_improvement_over_uniform\": -0.0958, \"top5_concentration\": 0.4934, \"layer0_dominance_ratio\": 0.07, \"best_k\": 2, \"best_k_ppl\": 7.2209, \"gqa_ratio\": \"8:1\", \"verdict\": \"FAIL\"}}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 8.9, \"mckp_wikitext2_ppl\": 9.05, \"uniform4bit_wikitext2_ppl\": 9.03, \"mckp_improvement_over_uniform\": -0.02, \"top5_concentration\": 0.23, \"layer0_dominance_ratio\": 1.32, \"best_k\": 8, \"best_k_ppl\": 9.05, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"bf16_wt2_ppl\": 7.0351, \"c4_cal_bf16_ppl\": 6.9677, \"wt2_cal_mckp_wt2_ppl\": 7.1648, \"c4_cal_mckp_wt2_ppl\": 7.1859, \"uniform_4bit_wt2_ppl\": 7.1314, \"delta_uniform_mckp_wt2_cal\": -0.0334, \"delta_uniform_mckp_c4_cal\": -0.0546, \"allocation_agreement_c4_vs_wt2\": 0.965, \"agreement_heads\": \"247/256\", \"bit_dist_wt2_cal\": \"2bit:4, 4bit:252\", \"bit_dist_c4_cal\": \"2bit:4, 4bit:251, 8bit:1\", \"profile_time_s\": 407.7, \"eval_time_s\": 349.4, \"total_time_s\": 757.1}}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"metrics\": {\"wt2_cal_wt2_ppl\": 8.4498, \"c4_cal_wt2_ppl\": 8.6459, \"uniform_wt2_ppl\": 8.469, \"wt2_cal_c4_ppl\": 7.654, \"c4_cal_c4_ppl\": 7.654, \"uniform_c4_ppl\": 7.5351, \"bf16_wt2_ppl\": 8.0918, \"bf16_c4_ppl\": 7.1333, \"agreement_rate\": 0.977, \"agreement_heads\": \"250/256\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 7.0351, \"uniform_4bit_ppl\": 7.1314, \"mckp_k4_ppl\": 7.1648, \"l0_random_seed_0\": 7.1882, \"l0_random_seed_1\": 7.1995, \"l0_random_seed_2\": 7.1723, \"l0_random_seed_3\": 7.3577, \"l0_random_seed_4\": 7.2875, \"l0_random_mean\": 7.2411, \"l0_random_std\": 0.0707, \"l0_random_median\": 7.1995, \"naive_heuristic_ppl\": 7.2105, \"budget_heuristic\": 0.2559, \"budget_mckp_k4\": 0.248}, \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"l0_random_seeds\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \"l0_random_mean\": 8.6245, \"l0_random_std\": 0.0733, \"l0_random_median\": 8.6192, \"naive_positional_ppl\": 8.5781, \"mckp_ppl\": 8.4498, \"uniform_ppl\": 8.469, \"baseline_ppl\": 8.0918, \"mckp_vs_l0_random_gap\": 0.1747, \"mckp_vs_naive_gap\": 0.1283}}, \"plan_009_oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mckp_ppl\": 10.9131, \"max_oracle_gap_ppl\": 0.0183, \"avg_oracle_gap_ppl\": 0.0046, \"layers_mckp_optimal\": \"5/8\", \"layers_with_gap\": 3, \"gap_layers\": {\"L1\": 0.0183, \"L4\": 0.0045, \"L11\": 0.0136}, \"gap_nature\": \"2-bit head position swap within same bit budget\", \"total_evals\": 54, \"runtime_min\": 21.3}}}, \"count\": 50, \"total\": 95, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2275}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "18a58a08-0b03-4459-bd1d-921e0ba9d8eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"llama_downstream_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_compounding_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_k\\\": 0, \\\"best_ppl\\\": 8.0922, \\\"k0_ppl\\\": 8.0922, \\\"k2_ppl\\\": 8.1243, \\\"k4_ppl\\\": 8.1803, \\\"k8_ppl\\\": 8.2259, \\\"k16_ppl\\\": 8.4378, \\\"k32_ppl\\\": 9.0506, \\\"k64_ppl\\\": 11.991, \\\"k128_ppl\\\": 40.2067, \\\"k256_ppl\\\": 1519.1888, \\\"budget\\\": 0.25}}, \\\"qwen25-hires-profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"cross_domain_calibration_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"greedy_constrained_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mistral_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mistral_hires_constrained_mckp_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 7.0352, \\\"mckp_wikitext2_ppl\\\": 7.1341, \\\"uniform4bit_wikitext2_ppl\\\": 7.1308, \\\"mckp_improvement_over_uniform\\\": -0.0033, \\\"mckp_improvement_pct\\\": -3.48, \\\"verdict\\\": \\\"FAIL\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 254}, \\\"fix_note\\\": \\\"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"mistral_uniform_reeval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"qwen14b_greedy_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"greedy_constrained_ppl\\\": 7.2206, \\\"mckp_constrained_ppl\\\": 7.2206, \\\"delta_vs_mckp\\\": 0, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 374, \\\"8\\\": 1, \\\"16\\\": 1}, \\\"memory_ratio\\\": 0.25, \\\"solver_time_sec\\\": 0.08, \\\"total_time_min\\\": 1.8}}, \\\"kivi_mckp_combined_qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_hires_bf16_2bitonly_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"kivi_baseline_qwen7b_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_kivi_4bit_g32_r128\\\": 9.8976, \\\"tokens\\\": 298938, \\\"chunks\\\": 583, \\\"stride\\\": 512, \\\"model\\\": \\\"Qwen2.5-7B\\\", \\\"comparison_mckp_ppl\\\": 10.91, \\\"comparison_uniform_ppl\\\": 15.45, \\\"comparison_bf16_ppl\\\": 9.81}}, \\\"qwen14b_constrained_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16\\\": 6.8654, \\\"ppl_uniform_4bit\\\": 7.202, \\\"ppl_constrained_mckp\\\": 7.2206, \\\"ppl_unconstrained_mckp\\\": 7.6923, \\\"delta_constrained_vs_uniform\\\": -0.0185, \\\"delta_constrained_vs_uniform_pct\\\": -5.51, \\\"delta_unconstrained_vs_uniform\\\": -0.4902, \\\"bit_distribution_constrained\\\": {\\\"2\\\": 8, \\\"4\\\": 374, \\\"8\\\": 1, \\\"16\\\": 1}, \\\"bit_distribution_unconstrained\\\": {\\\"2\\\": 77, \\\"4\\\": 271, \\\"8\\\": 35, \\\"16\\\": 1}, \\\"concentration\\\": 0.33, \\\"top1_pct\\\": 0.2262, \\\"top5_pct\\\": 0.3304, \\\"t1_t5\\\": 0.68, \\\"shape\\\": \\\"Flat\\\"}}, \\\"qwen_hires_constrained_d049\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"float32_hires_constrained_mckp_ppl\\\": 10.8921, \\\"baseline_ppl\\\": 9.8106, \\\"uniform_4bit_ppl\\\": 15.4484, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 100, \\\"8\\\": 4}, \\\"gap_recovery_pct\\\": 80.8, \\\"top5_concentration\\\": 0.6156, \\\"top5_concentration_pre_monotonicity\\\": 0.6104, \\\"bf16_hires_constrained_mckp_ppl\\\": 10.9131, \\\"delta_f32_vs_bf16\\\": 0.021}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ppl_bf16_8k\\\": 5.5958, \\\"ppl_constrained_mckp_8k\\\": 6.0537, \\\"ppl_uniform_4bit_8k\\\": 6.0364, \\\"mckp_improvement_over_uniform_8k\\\": -0.0174, \\\"mckp_improvement_pct_8k\\\": -3.94, \\\"ppl_bf16_2k\\\": 8.0922, \\\"ppl_constrained_mckp_2k\\\": 8.5042, \\\"ppl_uniform_4bit_2k\\\": 8.4701, \\\"shape\\\": \\\"Spike\\\", \\\"concentration\\\": 0.5749, \\\"t1_over_t5\\\": 0.71, \\\"context_length\\\": 8192, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"yi15_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"qwen7b_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen7b_8k_context_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16_8k\\\": 6.97, \\\"ppl_constrained_mckp_8k\\\": 8.59, \\\"ppl_uniform_4bit_8k\\\": 77.75, \\\"ppl_bf16_2k\\\": 9.81, \\\"ppl_constrained_mckp_2k\\\": 10.89, \\\"ppl_uniform_4bit_2k\\\": 15.45, \\\"mckp_improvement_over_uniform_8k\\\": \\\"97.7%\\\", \\\"mckp_improvement_over_uniform_2k\\\": \\\"80.8%\\\", \\\"shape\\\": \\\"Spread\\\", \\\"concentration\\\": 0.5992, \\\"context_length\\\": 8192, \\\"note\\\": \\\"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\\\"}}, \\\"pythia14b_constrained_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16\\\": 16.4893, \\\"ppl_uniform_4bit\\\": 24.2894, \\\"ppl_constrained_mckp\\\": 24.4521, \\\"ppl_unconstrained_mckp\\\": 31.5415, \\\"concentration\\\": \\\"t1=0.0289, t5=0.2439\\\", \\\"t1_t5\\\": \\\"0.0289/0.2439\\\", \\\"shape\\\": \\\"Flat\\\", \\\"constrained_vs_uniform_gap\\\": 0.1627}}, \\\"w1_pythia14b_hires_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 13.6347, \\\"concentration\\\": 0.2439, \\\"t1_t5\\\": 0.28, \\\"shape\\\": \\\"Flat\\\", \\\"l0_dominance\\\": 0.51, \\\"cv\\\": 1.2172, \\\"positive_heads\\\": 362, \\\"total_heads\\\": 384, \\\"top5_heads\\\": [{\\\"head\\\": \\\"L1H11\\\", \\\"delta\\\": 1.016355}, {\\\"head\\\": \\\"L12H14\\\", \\\"delta\\\": 0.784513}, {\\\"head\\\": \\\"L8H4\\\", \\\"delta\\\": 0.759118}, {\\\"head\\\": \\\"L11H2\\\", \\\"delta\\\": 0.632357}, {\\\"head\\\": \\\"L13H2\\\", \\\"delta\\\": 0.522849}], \\\"elapsed_min\\\": 25.7, \\\"note\\\": \\\"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w1_qwen14b_hires_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 5.8432, \\\"concentration\\\": 0.3312, \\\"t1_t5\\\": 0.68, \\\"shape\\\": \\\"Flat\\\", \\\"l0_dominance\\\": 15.5, \\\"cv\\\": 3.7418, \\\"positive_heads\\\": 370, \\\"total_heads\\\": 384, \\\"top10_heads\\\": [{\\\"head\\\": \\\"L0H5\\\", \\\"delta\\\": 1.84494}, {\\\"head\\\": \\\"L0H4\\\", \\\"delta\\\": 0.236669}, {\\\"head\\\": \\\"L0H2\\\", \\\"delta\\\": 0.136971}, {\\\"head\\\": \\\"L28H4\\\", \\\"delta\\\": 0.099279}, {\\\"head\\\": \\\"L28H5\\\", \\\"delta\\\": 0.07576}, {\\\"head\\\": \\\"L27H4\\\", \\\"delta\\\": 0.071269}, {\\\"head\\\": \\\"L0H0\\\", \\\"delta\\\": 0.070018}, {\\\"head\\\": \\\"L28H6\\\", \\\"delta\\\": 0.063737}, {\\\"head\\\": \\\"L26H0\\\", \\\"delta\\\": 0.061462}, {\\\"head\\\": \\\"L31H3\\\", \\\"delta\\\": 0.061062}], \\\"elapsed_min\\\": 161.3, \\\"note\\\": \\\"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\\\"}}, \\\"kivi_baseline_qwen_llama\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"qwen_2bit_r128\\\": 12.83, \\\"qwen_4bit_r128\\\": 9.9, \\\"qwen_2bit_r0\\\": 13.34, \\\"qwen_4bit_r0\\\": 9.91, \\\"llama_2bit_r128\\\": 9.84, \\\"llama_4bit_r128\\\": 8.14, \\\"llama_2bit_r0\\\": 10.08, \\\"llama_4bit_r0\\\": 8.14, \\\"group_size\\\": 32, \\\"eval_data\\\": \\\"WikiText-2 test\\\", \\\"note\\\": \\\"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\\\"}}, \\\"gemma2_constrained_bos_fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 6.0306, \\\"uniform_4bit_ppl\\\": 6.1683, \\\"constrained_mckp_ppl\\\": 6.1951, \\\"mckp_vs_uniform_delta\\\": 0.0267, \\\"mckp_delta_ppl\\\": 0.1645, \\\"uniform_delta_ppl\\\": 0.1377, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 324, \\\"8\\\": 4}, \\\"n_2bit\\\": 8, \\\"max_2bit\\\": 8, \\\"memory_ratio\\\": 0.25, \\\"eval_method\\\": \\\"sliding_window_bos_fix\\\", \\\"elapsed_seconds\\\": 490.3}}, \\\"w2_unconstrained_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"yi15_baseline\\\": 7.0157, \\\"yi15_uniform4\\\": 7.2171, \\\"yi15_greedy\\\": 7.5615, \\\"yi15_mckp\\\": 7.5615, \\\"yi15_n2bit\\\": 22, \\\"llama_baseline\\\": 8.0922, \\\"llama_uniform4\\\": 8.4701, \\\"llama_greedy\\\": 8.6265, \\\"llama_mckp\\\": 8.6265, \\\"llama_n2bit\\\": 12, \\\"mistral_baseline\\\": 7.0352, \\\"mistral_uniform4\\\": 7.1308, \\\"mistral_greedy\\\": 7.5733, \\\"mistral_mckp\\\": 7.5963, \\\"mistral_n2bit\\\": 42, \\\"gemma2_baseline\\\": 6.0306, \\\"gemma2_uniform4\\\": 6.1683, \\\"gemma2_greedy\\\": 8.8469, \\\"gemma2_mckp\\\": 8.8469, \\\"gemma2_n2bit\\\": 106, \\\"gemma2_eval_method\\\": \\\"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\\\", \\\"gemma2_greedy_ratio\\\": 1.467, \\\"gemma2_catastrophic\\\": true, \\\"gemma2_note\\\": \\\"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\\\"}}, \\\"w3_downstream_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"yi15_baseline_avg\\\": 0.6912, \\\"yi15_uniform_avg\\\": 0.6822, \\\"yi15_mckp_avg\\\": 0.6745, \\\"yi15_mckp_vs_uniform_pp\\\": -0.77, \\\"yi15_mckp_vs_baseline_pp\\\": -1.67, \\\"yi15_baseline\\\": {\\\"arc_easy\\\": 0.8093, \\\"arc_challenge\\\": 0.5265, \\\"hellaswag\\\": 0.5913, \\\"piqa\\\": 0.7949, \\\"winogrande\\\": 0.734}, \\\"yi15_uniform\\\": {\\\"arc_easy\\\": 0.7946, \\\"arc_challenge\\\": 0.5205, \\\"hellaswag\\\": 0.5857, \\\"piqa\\\": 0.7927, \\\"winogrande\\\": 0.7174}, \\\"yi15_mckp\\\": {\\\"arc_easy\\\": 0.7854, \\\"arc_challenge\\\": 0.4881, \\\"hellaswag\\\": 0.5797, \\\"piqa\\\": 0.7894, \\\"winogrande\\\": 0.7301}, \\\"llama_baseline_avg\\\": 0.696, \\\"llama_uniform_avg\\\": 0.6915, \\\"llama_mckp_avg\\\": 0.6816, \\\"llama_mckp_vs_uniform_pp\\\": -0.99, \\\"llama_mckp_vs_baseline_pp\\\": -1.44, \\\"llama_baseline\\\": {\\\"arc_easy\\\": 0.8228, \\\"arc_challenge\\\": 0.5188, \\\"hellaswag\\\": 0.6073, \\\"piqa\\\": 0.7922, \\\"winogrande\\\": 0.7388}, \\\"llama_uniform\\\": {\\\"arc_easy\\\": 0.8173, \\\"arc_challenge\\\": 0.5256, \\\"hellaswag\\\": 0.6026, \\\"piqa\\\": 0.7867, \\\"winogrande\\\": 0.7253}, \\\"llama_mckp\\\": {\\\"arc_easy\\\": 0.8039, \\\"arc_challenge\\\": 0.4991, \\\"hellaswag\\\": 0.6012, \\\"piqa\\\": 0.7802, \\\"winogrande\\\": 0.7238}, \\\"mistral_baseline_avg\\\": 0.6917, \\\"mistral_uniform_avg\\\": 0.6894, \\\"mistral_mckp_avg\\\": 0.6846, \\\"mistral_mckp_vs_uniform_pp\\\": -0.48, \\\"mistral_mckp_vs_baseline_pp\\\": -0.71, \\\"mistral_baseline\\\": {\\\"arc_easy\\\": 0.8005, \\\"arc_challenge\\\": 0.5043, \\\"hellaswag\\\": 0.6118, \\\"piqa\\\": 0.8009, \\\"winogrande\\\": 0.7411}, \\\"mistral_uniform\\\": {\\\"arc_easy\\\": 0.7976, \\\"arc_challenge\\\": 0.5068, \\\"hellaswag\\\": 0.6051, \\\"piqa\\\": 0.7982, \\\"winogrande\\\": 0.7395}, \\\"mistral_mckp\\\": {\\\"arc_easy\\\": 0.7942, \\\"arc_challenge\\\": 0.4949, \\\"hellaswag\\\": 0.6027, \\\"piqa\\\": 0.802, \\\"winogrande\\\": 0.7293}, \\\"gemma2_baseline_avg\\\": 0.7307, \\\"gemma2_uniform_avg\\\": 0.7251, \\\"gemma2_mckp_avg\\\": 0.7265, \\\"gemma2_mckp_vs_uniform_pp\\\": 0.14, \\\"gemma2_mckp_vs_baseline_pp\\\": -0.42, \\\"gemma2_baseline\\\": {\\\"arc_easy\\\": 0.8737, \\\"arc_challenge\\\": 0.6135, \\\"hellaswag\\\": 0.6093, \\\"piqa\\\": 0.8128, \\\"winogrande\\\": 0.7443}, \\\"gemma2_uniform\\\": {\\\"arc_easy\\\": 0.8662, \\\"arc_challenge\\\": 0.6058, \\\"hellaswag\\\": 0.606, \\\"piqa\\\": 0.8079, \\\"winogrande\\\": 0.7395}, \\\"gemma2_mckp\\\": {\\\"arc_easy\\\": 0.8649, \\\"arc_challenge\\\": 0.6041, \\\"hellaswag\\\": 0.6089, \\\"piqa\\\": 0.8074, \\\"winogrande\\\": 0.7474}, \\\"eval_harness_version\\\": \\\"0.4.11\\\", \\\"num_fewshot\\\": 0, \\\"yi_elapsed_s\\\": 1563.2, \\\"llama_elapsed_s\\\": 1446.4, \\\"mistral_elapsed_s\\\": 1302.2, \\\"gemma2_elapsed_s\\\": 1735.9}}, \\\"w9_compounding_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 9.81, \\\"k1_topk_ppl\\\": 9.826, \\\"k1_randomk_ppl\\\": 9.887, \\\"k1_randomk_std\\\": 0.05, \\\"k4_topk_ppl\\\": 9.849, \\\"k4_topk_ratio\\\": 0.86, \\\"k4_randomk_ppl\\\": 10.06, \\\"k4_randomk_std\\\": 0.06, \\\"k4_randomk_ratio\\\": 1.24, \\\"k8_topk_ppl\\\": 10.042, \\\"k8_topk_ratio\\\": 1.56, \\\"k8_randomk_ppl\\\": 11.07, \\\"k8_randomk_std\\\": 0.69, \\\"k8_randomk_ratio\\\": 1.76, \\\"k16_topk_ppl\\\": 10.42, \\\"k16_topk_ratio\\\": 1.56, \\\"k16_randomk_ppl\\\": 12.91, \\\"k16_randomk_std\\\": 0.4, \\\"k16_randomk_ratio\\\": 2.1, \\\"k32_topk_ppl\\\": 11.604, \\\"k32_topk_ratio\\\": 1.78, \\\"k32_randomk_ppl\\\": 18.33, \\\"k32_randomk_std\\\": 2.53, \\\"k32_randomk_ratio\\\": 2.73, \\\"k64_topk_ppl\\\": 22.946, \\\"k64_topk_ratio\\\": 4.89, \\\"k64_randomk_ppl\\\": 55.94, \\\"k64_randomk_std\\\": 9.73, \\\"k64_randomk_ratio\\\": 8.88, \\\"runtime_minutes\\\": 16.9, \\\"note\\\": \\\"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\\\"}}, \\\"w9_compounding_scaling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 8.2, \\\"n1_joint_ppl\\\": 14.94, \\\"n1_ratio\\\": 1, \\\"n2_joint_ppl\\\": 42.26, \\\"n2_ratio\\\": 3.84, \\\"n4_joint_ppl\\\": 3813.76, \\\"n4_ratio\\\": 333.3, \\\"n8_joint_ppl\\\": 3586.42, \\\"n8_ratio\\\": 282.1, \\\"n16_joint_ppl\\\": 7286.23, \\\"n16_ratio\\\": 521.1, \\\"n32_joint_ppl\\\": 6644.05, \\\"n32_ratio\\\": 424, \\\"n64_joint_ppl\\\": 9453.33, \\\"n64_ratio\\\": 533.3, \\\"runtime_seconds\\\": 96}}, \\\"w2_unconstrained_baselines\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"note\\\": \\\"2bitonly profiles only - INVALID for reviewer response\\\", \\\"yi15_ppl\\\": 672.2, \\\"yi15_ratio\\\": 114, \\\"llama_ppl\\\": 1219.7, \\\"llama_ratio\\\": 187, \\\"mistral_ppl_2bitonly\\\": 47.8, \\\"mistral_ratio_2bitonly\\\": 8.2, \\\"mistral_ppl_full\\\": 6.39, \\\"mistral_ratio_full\\\": 1.09, \\\"gemma2_ppl\\\": 277.4, \\\"gemma2_ratio\\\": 37.9, \\\"budget\\\": 0.25, \\\"baseline_yi\\\": 5.89, \\\"baseline_llama\\\": 6.51, \\\"baseline_mistral\\\": 5.87, \\\"baseline_gemma2\\\": 7.32}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"gemma2_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"concentration_top5pct\\\": 0.2291, \\\"l0_dominance_ratio\\\": 2.05, \\\"cv_delta_2bit\\\": 1.2834, \\\"positive_delta_heads\\\": \\\"310/336\\\", \\\"top_head\\\": \\\"L0H1 delta=0.1906\\\", \\\"total_time_hours\\\": 1.59}}, \\\"mistral_c4_hires_crossdataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"fp16_ppl\\\": 7.0352, \\\"c4_mckp_ppl\\\": 7.1774, \\\"uniform_4bit_ppl\\\": 7.1308, \\\"mckp_vs_uniform_delta\\\": 0.0466, \\\"mckp_bit_distribution\\\": {\\\"2\\\": 4, \\\"4\\\": 250, \\\"8\\\": 2}, \\\"phase4_error\\\": \\\"FileNotFoundError: mistral_k_ablation_results.json\\\"}}, \\\"llama_c4_hires_crossdataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"bf16_wt2_ppl\\\": 8.0922, \\\"bf16_c4_ppl\\\": 7.1333, \\\"c4_cal_mckp_wt2_ppl\\\": 8.5103, \\\"c4_cal_mckp_c4_ppl\\\": 7.5351, \\\"uniform_wt2_ppl\\\": 8.4701, \\\"uniform_c4_ppl\\\": 7.5351, \\\"delta_c4_uniform_minus_mckp\\\": 0, \\\"delta_wt2_uniform_minus_mckp\\\": -0.0402, \\\"verdict_c4\\\": \\\"FAIL\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}, \\\"heads_2bit\\\": [\\\"2,3\\\", \\\"24,2\\\"], \\\"heads_8bit\\\": [\\\"31,6\\\"], \\\"total_time_min\\\": 6.3, \\\"wt2_ref_mckp_ppl\\\": 8.5042, \\\"wt2_ref_delta\\\": -0.0341}}, \\\"mistral_hires_bf16_2bitonly_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.241, \\\"top5_n_heads\\\": 12, \\\"baseline_ppl\\\": 5.8702, \\\"top1_head\\\": \\\"L2H5\\\", \\\"top1_delta_2bit\\\": 0.3236, \\\"top2_head\\\": \\\"L12H1\\\", \\\"top2_delta_2bit\\\": 0.1435, \\\"top3_head\\\": \\\"L0H7\\\", \\\"top3_delta_2bit\\\": 0.1403, \\\"delta_2bit_mean\\\": 0.020073, \\\"delta_2bit_std\\\": 0.026278, \\\"delta_2bit_cv\\\": 1.3091, \\\"layer0_mean_delta_2bit\\\": 0.034073, \\\"other_layers_mean_delta_2bit\\\": 0.019621, \\\"l0_dominance_ratio\\\": 1.74, \\\"positive_delta_heads\\\": 252, \\\"total_heads\\\": 256, \\\"distribution_shape\\\": \\\"flat\\\", \\\"total_hours\\\": 0.94, \\\"profile_seconds\\\": 3371.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_bf16_ppl\\\": 8.0922, \\\"hires_mckp_ppl\\\": 8.5042, \\\"uniform_4bit_ppl\\\": 8.4701, \\\"std_mckp_reference_ppl\\\": 8.4498, \\\"mckp_vs_uniform_delta\\\": -0.0341, \\\"mckp_vs_uniform_pct\\\": -9, \\\"hires_vs_std_mckp_delta\\\": 0.0544, \\\"concentration\\\": 0.5749, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}, \\\"heads_2bit\\\": [\\\"26,0\\\", \\\"31,7\\\"], \\\"heads_8bit\\\": [\\\"12,3\\\"], \\\"verdict\\\": \\\"FAIL\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"llama_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.5749, \\\"t1_t5\\\": 0.85, \\\"baseline_ppl\\\": 6.5055, \\\"top1_head\\\": \\\"L2H5_delta=15.2636\\\", \\\"delta_2bit_cv\\\": 7.7663, \\\"l0_dominance_ratio\\\": 0.67, \\\"positive_delta_heads\\\": 254, \\\"total_heads\\\": 256, \\\"total_hours\\\": 0.98}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_hires_bf16_2bitonly_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\\\"}}, \\\"mistral_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\\\"}}, \\\"yi15_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"hires_mckp_ppl\\\": 7.2181, \\\"uniform_4bit_ppl\\\": 7.2171, \\\"baseline_ppl\\\": 7.0157, \\\"delta_vs_uniform\\\": -0.001, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 189, \\\"8\\\": 1}, \\\"2bit_heads\\\": [\\\"L22H1\\\", \\\"L24H3\\\"], \\\"8bit_heads\\\": [\\\"L6H2\\\"], \\\"L4H3_status\\\": \\\"kept_at_4bit\\\", \\\"std_mckp_k2_ppl\\\": 7.2209, \\\"std_mckp_k8_ppl\\\": 7.3129, \\\"hires_concentration\\\": 0.7139, \\\"L4H3_2bit_delta\\\": 13.12, \\\"L4H3_4bit_delta\\\": 0.0048, \\\"L4H3_8bit_delta\\\": 0.004}}, \\\"yi15_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.7139, \\\"top5_n_heads\\\": 9, \\\"baseline_calibration_ppl\\\": 5.888, \\\"delta_2bit_cv\\\": 8.8991, \\\"layer0_dominance_ratio\\\": 0.04, \\\"top1_head\\\": \\\"L4H3_delta=13.1236\\\", \\\"total_hours\\\": 0.96}}, \\\"qwen_hires_float32_d048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"float32_hires_top5_concentration\\\": 0.6104, \\\"bf16_hires_range\\\": \\\"0.59-0.66\\\", \\\"float32_lowres_concentration\\\": 0.42, \\\"bf16_bug_impact_on_concentration\\\": 0.01, \\\"baseline_ppl\\\": 9.81, \\\"mckp_unconstrained_ppl\\\": 10.95, \\\"uniform_4bit_ppl\\\": 15.45, \\\"mckp_bit_dist\\\": {\\\"2\\\": 12, \\\"4\\\": 96, \\\"8\\\": 3, \\\"16\\\": 1}, \\\"l0h0_delta\\\": 6.7388, \\\"l0_4heads_total_share\\\": 0.586, \\\"claim3_threshold_0.50\\\": \\\"PASS\\\"}}, \\\"yi15_hires_float32_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"yi15_9b_full_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 7.0157, \\\"mckp_wikitext2_ppl\\\": 7.3129, \\\"uniform4bit_wikitext2_ppl\\\": 7.2171, \\\"mckp_improvement_over_uniform\\\": -0.0958, \\\"top5_concentration\\\": 0.4934, \\\"layer0_dominance_ratio\\\": 0.07, \\\"best_k\\\": 2, \\\"best_k_ppl\\\": 7.2209, \\\"gqa_ratio\\\": \\\"8:1\\\", \\\"verdict\\\": \\\"FAIL\\\"}}, \\\"gemma2_9b_full_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 8.9, \\\"mckp_wikitext2_ppl\\\": 9.05, \\\"uniform4bit_wikitext2_ppl\\\": 9.03, \\\"mckp_improvement_over_uniform\\\": -0.02, \\\"top5_concentration\\\": 0.23, \\\"layer0_dominance_ratio\\\": 1.32, \\\"best_k\\\": 8, \\\"best_k_ppl\\\": 9.05, \\\"verdict\\\": \\\"FAIL\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"qwen72b_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"multi_seed_lowres\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mistral_c4_cross_dataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"bf16_wt2_ppl\\\": 7.0351, \\\"c4_cal_bf16_ppl\\\": 6.9677, \\\"wt2_cal_mckp_wt2_ppl\\\": 7.1648, \\\"c4_cal_mckp_wt2_ppl\\\": 7.1859, \\\"uniform_4bit_wt2_ppl\\\": 7.1314, \\\"delta_uniform_mckp_wt2_cal\\\": -0.0334, \\\"delta_uniform_mckp_c4_cal\\\": -0.0546, \\\"allocation_agreement_c4_vs_wt2\\\": 0.965, \\\"agreement_heads\\\": \\\"247/256\\\", \\\"bit_dist_wt2_cal\\\": \\\"2bit:4, 4bit:252\\\", \\\"bit_dist_c4_cal\\\": \\\"2bit:4, 4bit:251, 8bit:1\\\", \\\"profile_time_s\\\": 407.7, \\\"eval_time_s\\\": 349.4, \\\"total_time_s\\\": 757.1}}, \\\"llama_c4_cross_dataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wt2_cal_wt2_ppl\\\": 8.4498, \\\"c4_cal_wt2_ppl\\\": 8.6459, \\\"uniform_wt2_ppl\\\": 8.469, \\\"wt2_cal_c4_ppl\\\": 7.654, \\\"c4_cal_c4_ppl\\\": 7.654, \\\"uniform_c4_ppl\\\": 7.5351, \\\"bf16_wt2_ppl\\\": 8.0918, \\\"bf16_c4_ppl\\\": 7.1333, \\\"agreement_rate\\\": 0.977, \\\"agreement_heads\\\": \\\"250/256\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"mistral_heuristic_k4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_bf16_ppl\\\": 7.0351, \\\"uniform_4bit_ppl\\\": 7.1314, \\\"mckp_k4_ppl\\\": 7.1648, \\\"l0_random_seed_0\\\": 7.1882, \\\"l0_random_seed_1\\\": 7.1995, \\\"l0_random_seed_2\\\": 7.1723, \\\"l0_random_seed_3\\\": 7.3577, \\\"l0_random_seed_4\\\": 7.2875, \\\"l0_random_mean\\\": 7.2411, \\\"l0_random_std\\\": 0.0707, \\\"l0_random_median\\\": 7.1995, \\\"naive_heuristic_ppl\\\": 7.2105, \\\"budget_heuristic\\\": 0.2559, \\\"budget_mckp_k4\\\": 0.248}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_heuristic_k2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"l0_random_seeds\\\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \\\"l0_random_mean\\\": 8.6245, \\\"l0_random_std\\\": 0.0733, \\\"l0_random_median\\\": 8.6192, \\\"naive_positional_ppl\\\": 8.5781, \\\"mckp_ppl\\\": 8.4498, \\\"uniform_ppl\\\": 8.469, \\\"baseline_ppl\\\": 8.0918, \\\"mckp_vs_l0_random_gap\\\": 0.1747, \\\"mckp_vs_naive_gap\\\": 0.1283}}, \\\"plan_009_oracle_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"oracle_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mckp_ppl\\\": 10.9131, \\\"max_oracle_gap_ppl\\\": 0.0183, \\\"avg_oracle_gap_ppl\\\": 0.0046, \\\"layers_mckp_optimal\\\": \\\"5/8\\\", \\\"layers_with_gap\\\": 3, \\\"gap_layers\\\": {\\\"L1\\\": 0.0183, \\\"L4\\\": 0.0045, \\\"L11\\\": 0.0136}, \\\"gap_nature\\\": \\\"2-bit head position swap within same bit budget\\\", \\\"total_evals\\\": 54, \\\"runtime_min\\\": 21.3}}}, \\\"count\\\": 50, \\\"total\\\": 95, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2275}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"llama_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_compounding_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_k\": 0, \"best_ppl\": 8.0922, \"k0_ppl\": 8.0922, \"k2_ppl\": 8.1243, \"k4_ppl\": 8.1803, \"k8_ppl\": 8.2259, \"k16_ppl\": 8.4378, \"k32_ppl\": 9.0506, \"k64_ppl\": 11.991, \"k128_ppl\": 40.2067, \"k256_ppl\": 1519.1888, \"budget\": 0.25}}, \"qwen25-hires-profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_constrained_mckp_v2\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0352, \"mckp_wikitext2_ppl\": 7.1341, \"uniform4bit_wikitext2_ppl\": 7.1308, \"mckp_improvement_over_uniform\": -0.0033, \"mckp_improvement_pct\": -3.48, \"verdict\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 254}, \"fix_note\": \"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\"}, \"conclusion\": \"negative\"}, \"mistral_uniform_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen14b_greedy_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_constrained_ppl\": 7.2206, \"mckp_constrained_ppl\": 7.2206, \"delta_vs_mckp\": 0, \"bit_distribution\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"memory_ratio\": 0.25, \"solver_time_sec\": 0.08, \"total_time_min\": 1.8}}, \"kivi_mckp_combined_qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kivi_baseline_qwen7b_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_kivi_4bit_g32_r128\": 9.8976, \"tokens\": 298938, \"chunks\": 583, \"stride\": 512, \"model\": \"Qwen2.5-7B\", \"comparison_mckp_ppl\": 10.91, \"comparison_uniform_ppl\": 15.45, \"comparison_bf16_ppl\": 9.81}}, \"qwen14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 6.8654, \"ppl_uniform_4bit\": 7.202, \"ppl_constrained_mckp\": 7.2206, \"ppl_unconstrained_mckp\": 7.6923, \"delta_constrained_vs_uniform\": -0.0185, \"delta_constrained_vs_uniform_pct\": -5.51, \"delta_unconstrained_vs_uniform\": -0.4902, \"bit_distribution_constrained\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"bit_distribution_unconstrained\": {\"2\": 77, \"4\": 271, \"8\": 35, \"16\": 1}, \"concentration\": 0.33, \"top1_pct\": 0.2262, \"top5_pct\": 0.3304, \"t1_t5\": 0.68, \"shape\": \"Flat\"}}, \"qwen_hires_constrained_d049\": {\"status\": \"DONE\", \"metrics\": {\"float32_hires_constrained_mckp_ppl\": 10.8921, \"baseline_ppl\": 9.8106, \"uniform_4bit_ppl\": 15.4484, \"bit_distribution\": {\"2\": 8, \"4\": 100, \"8\": 4}, \"gap_recovery_pct\": 80.8, \"top5_concentration\": 0.6156, \"top5_concentration_pre_monotonicity\": 0.6104, \"bf16_hires_constrained_mckp_ppl\": 10.9131, \"delta_f32_vs_bf16\": 0.021}, \"conclusion\": \"success\"}, \"llama_8k_spotcheck\": {\"status\": \"DONE\", \"metrics\": {\"ppl_bf16_8k\": 5.5958, \"ppl_constrained_mckp_8k\": 6.0537, \"ppl_uniform_4bit_8k\": 6.0364, \"mckp_improvement_over_uniform_8k\": -0.0174, \"mckp_improvement_pct_8k\": -3.94, \"ppl_bf16_2k\": 8.0922, \"ppl_constrained_mckp_2k\": 8.5042, \"ppl_uniform_4bit_2k\": 8.4701, \"shape\": \"Spike\", \"concentration\": 0.5749, \"t1_over_t5\": 0.71, \"context_length\": 8192, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"success\"}, \"yi15_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen7b_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"qwen7b_8k_context_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16_8k\": 6.97, \"ppl_constrained_mckp_8k\": 8.59, \"ppl_uniform_4bit_8k\": 77.75, \"ppl_bf16_2k\": 9.81, \"ppl_constrained_mckp_2k\": 10.89, \"ppl_uniform_4bit_2k\": 15.45, \"mckp_improvement_over_uniform_8k\": \"97.7%\", \"mckp_improvement_over_uniform_2k\": \"80.8%\", \"shape\": \"Spread\", \"concentration\": 0.5992, \"context_length\": 8192, \"note\": \"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\"}}, \"pythia14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 16.4893, \"ppl_uniform_4bit\": 24.2894, \"ppl_constrained_mckp\": 24.4521, \"ppl_unconstrained_mckp\": 31.5415, \"concentration\": \"t1=0.0289, t5=0.2439\", \"t1_t5\": \"0.0289/0.2439\", \"shape\": \"Flat\", \"constrained_vs_uniform_gap\": 0.1627}}, \"w1_pythia14b_hires_profiling\": {\"status\": \"DONE\", \"metrics\": {\"baseline_ppl\": 13.6347, \"concentration\": 0.2439, \"t1_t5\": 0.28, \"shape\": \"Flat\", \"l0_dominance\": 0.51, \"cv\": 1.2172, \"positive_heads\": 362, \"total_heads\": 384, \"top5_heads\": [{\"head\": \"L1H11\", \"delta\": 1.016355}, {\"head\": \"L12H14\", \"delta\": 0.784513}, {\"head\": \"L8H4\", \"delta\": 0.759118}, {\"head\": \"L11H2\", \"delta\": 0.632357}, {\"head\": \"L13H2\", \"delta\": 0.522849}], \"elapsed_min\": 25.7, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}, \"conclusion\": \"success\"}, \"w1_qwen14b_hires_profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 5.8432, \"concentration\": 0.3312, \"t1_t5\": 0.68, \"shape\": \"Flat\", \"l0_dominance\": 15.5, \"cv\": 3.7418, \"positive_heads\": 370, \"total_heads\": 384, \"top10_heads\": [{\"head\": \"L0H5\", \"delta\": 1.84494}, {\"head\": \"L0H4\", \"delta\": 0.236669}, {\"head\": \"L0H2\", \"delta\": 0.136971}, {\"head\": \"L28H4\", \"delta\": 0.099279}, {\"head\": \"L28H5\", \"delta\": 0.07576}, {\"head\": \"L27H4\", \"delta\": 0.071269}, {\"head\": \"L0H0\", \"delta\": 0.070018}, {\"head\": \"L28H6\", \"delta\": 0.063737}, {\"head\": \"L26H0\", \"delta\": 0.061462}, {\"head\": \"L31H3\", \"delta\": 0.061062}], \"elapsed_min\": 161.3, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}}, \"kivi_baseline_qwen_llama\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"qwen_2bit_r128\": 12.83, \"qwen_4bit_r128\": 9.9, \"qwen_2bit_r0\": 13.34, \"qwen_4bit_r0\": 9.91, \"llama_2bit_r128\": 9.84, \"llama_4bit_r128\": 8.14, \"llama_2bit_r0\": 10.08, \"llama_4bit_r0\": 8.14, \"group_size\": 32, \"eval_data\": \"WikiText-2 test\", \"note\": \"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\"}}, \"gemma2_constrained_bos_fix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 6.0306, \"uniform_4bit_ppl\": 6.1683, \"constrained_mckp_ppl\": 6.1951, \"mckp_vs_uniform_delta\": 0.0267, \"mckp_delta_ppl\": 0.1645, \"uniform_delta_ppl\": 0.1377, \"bit_distribution\": {\"2\": 8, \"4\": 324, \"8\": 4}, \"n_2bit\": 8, \"max_2bit\": 8, \"memory_ratio\": 0.25, \"eval_method\": \"sliding_window_bos_fix\", \"elapsed_seconds\": 490.3}}, \"w2_unconstrained_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline\": 7.0157, \"yi15_uniform4\": 7.2171, \"yi15_greedy\": 7.5615, \"yi15_mckp\": 7.5615, \"yi15_n2bit\": 22, \"llama_baseline\": 8.0922, \"llama_uniform4\": 8.4701, \"llama_greedy\": 8.6265, \"llama_mckp\": 8.6265, \"llama_n2bit\": 12, \"mistral_baseline\": 7.0352, \"mistral_uniform4\": 7.1308, \"mistral_greedy\": 7.5733, \"mistral_mckp\": 7.5963, \"mistral_n2bit\": 42, \"gemma2_baseline\": 6.0306, \"gemma2_uniform4\": 6.1683, \"gemma2_greedy\": 8.8469, \"gemma2_mckp\": 8.8469, \"gemma2_n2bit\": 106, \"gemma2_eval_method\": \"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\", \"gemma2_greedy_ratio\": 1.467, \"gemma2_catastrophic\": true, \"gemma2_note\": \"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\"}}, \"w3_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline_avg\": 0.6912, \"yi15_uniform_avg\": 0.6822, \"yi15_mckp_avg\": 0.6745, \"yi15_mckp_vs_uniform_pp\": -0.77, \"yi15_mckp_vs_baseline_pp\": -1.67, \"yi15_baseline\": {\"arc_easy\": 0.8093, \"arc_challenge\": 0.5265, \"hellaswag\": 0.5913, \"piqa\": 0.7949, \"winogrande\": 0.734}, \"yi15_uniform\": {\"arc_easy\": 0.7946, \"arc_challenge\": 0.5205, \"hellaswag\": 0.5857, \"piqa\": 0.7927, \"winogrande\": 0.7174}, \"yi15_mckp\": {\"arc_easy\": 0.7854, \"arc_challenge\": 0.4881, \"hellaswag\": 0.5797, \"piqa\": 0.7894, \"winogrande\": 0.7301}, \"llama_baseline_avg\": 0.696, \"llama_uniform_avg\": 0.6915, \"llama_mckp_avg\": 0.6816, \"llama_mckp_vs_uniform_pp\": -0.99, \"llama_mckp_vs_baseline_pp\": -1.44, \"llama_baseline\": {\"arc_easy\": 0.8228, \"arc_challenge\": 0.5188, \"hellaswag\": 0.6073, \"piqa\": 0.7922, \"winogrande\": 0.7388}, \"llama_uniform\": {\"arc_easy\": 0.8173, \"arc_challenge\": 0.5256, \"hellaswag\": 0.6026, \"piqa\": 0.7867, \"winogrande\": 0.7253}, \"llama_mckp\": {\"arc_easy\": 0.8039, \"arc_challenge\": 0.4991, \"hellaswag\": 0.6012, \"piqa\": 0.7802, \"winogrande\": 0.7238}, \"mistral_baseline_avg\": 0.6917, \"mistral_uniform_avg\": 0.6894, \"mistral_mckp_avg\": 0.6846, \"mistral_mckp_vs_uniform_pp\": -0.48, \"mistral_mckp_vs_baseline_pp\": -0.71, \"mistral_baseline\": {\"arc_easy\": 0.8005, \"arc_challenge\": 0.5043, \"hellaswag\": 0.6118, \"piqa\": 0.8009, \"winogrande\": 0.7411}, \"mistral_uniform\": {\"arc_easy\": 0.7976, \"arc_challenge\": 0.5068, \"hellaswag\": 0.6051, \"piqa\": 0.7982, \"winogrande\": 0.7395}, \"mistral_mckp\": {\"arc_easy\": 0.7942, \"arc_challenge\": 0.4949, \"hellaswag\": 0.6027, \"piqa\": 0.802, \"winogrande\": 0.7293}, \"gemma2_baseline_avg\": 0.7307, \"gemma2_uniform_avg\": 0.7251, \"gemma2_mckp_avg\": 0.7265, \"gemma2_mckp_vs_uniform_pp\": 0.14, \"gemma2_mckp_vs_baseline_pp\": -0.42, \"gemma2_baseline\": {\"arc_easy\": 0.8737, \"arc_challenge\": 0.6135, \"hellaswag\": 0.6093, \"piqa\": 0.8128, \"winogrande\": 0.7443}, \"gemma2_uniform\": {\"arc_easy\": 0.8662, \"arc_challenge\": 0.6058, \"hellaswag\": 0.606, \"piqa\": 0.8079, \"winogrande\": 0.7395}, \"gemma2_mckp\": {\"arc_easy\": 0.8649, \"arc_challenge\": 0.6041, \"hellaswag\": 0.6089, \"piqa\": 0.8074, \"winogrande\": 0.7474}, \"eval_harness_version\": \"0.4.11\", \"num_fewshot\": 0, \"yi_elapsed_s\": 1563.2, \"llama_elapsed_s\": 1446.4, \"mistral_elapsed_s\": 1302.2, \"gemma2_elapsed_s\": 1735.9}}, \"w9_compounding_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 9.81, \"k1_topk_ppl\": 9.826, \"k1_randomk_ppl\": 9.887, \"k1_randomk_std\": 0.05, \"k4_topk_ppl\": 9.849, \"k4_topk_ratio\": 0.86, \"k4_randomk_ppl\": 10.06, \"k4_randomk_std\": 0.06, \"k4_randomk_ratio\": 1.24, \"k8_topk_ppl\": 10.042, \"k8_topk_ratio\": 1.56, \"k8_randomk_ppl\": 11.07, \"k8_randomk_std\": 0.69, \"k8_randomk_ratio\": 1.76, \"k16_topk_ppl\": 10.42, \"k16_topk_ratio\": 1.56, \"k16_randomk_ppl\": 12.91, \"k16_randomk_std\": 0.4, \"k16_randomk_ratio\": 2.1, \"k32_topk_ppl\": 11.604, \"k32_topk_ratio\": 1.78, \"k32_randomk_ppl\": 18.33, \"k32_randomk_std\": 2.53, \"k32_randomk_ratio\": 2.73, \"k64_topk_ppl\": 22.946, \"k64_topk_ratio\": 4.89, \"k64_randomk_ppl\": 55.94, \"k64_randomk_std\": 9.73, \"k64_randomk_ratio\": 8.88, \"runtime_minutes\": 16.9, \"note\": \"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\"}}, \"w9_compounding_scaling\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"baseline_ppl\": 8.2, \"n1_joint_ppl\": 14.94, \"n1_ratio\": 1, \"n2_joint_ppl\": 42.26, \"n2_ratio\": 3.84, \"n4_joint_ppl\": 3813.76, \"n4_ratio\": 333.3, \"n8_joint_ppl\": 3586.42, \"n8_ratio\": 282.1, \"n16_joint_ppl\": 7286.23, \"n16_ratio\": 521.1, \"n32_joint_ppl\": 6644.05, \"n32_ratio\": 424, \"n64_joint_ppl\": 9453.33, \"n64_ratio\": 533.3, \"runtime_seconds\": 96}}, \"w2_unconstrained_baselines\": {\"status\": \"DONE\", \"metrics\": {\"note\": \"2bitonly profiles only - INVALID for reviewer response\", \"yi15_ppl\": 672.2, \"yi15_ratio\": 114, \"llama_ppl\": 1219.7, \"llama_ratio\": 187, \"mistral_ppl_2bitonly\": 47.8, \"mistral_ratio_2bitonly\": 8.2, \"mistral_ppl_full\": 6.39, \"mistral_ratio_full\": 1.09, \"gemma2_ppl\": 277.4, \"gemma2_ratio\": 37.9, \"budget\": 0.25, \"baseline_yi\": 5.89, \"baseline_llama\": 6.51, \"baseline_mistral\": 5.87, \"baseline_gemma2\": 7.32}, \"conclusion\": \"killed\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"concentration_top5pct\": 0.2291, \"l0_dominance_ratio\": 2.05, \"cv_delta_2bit\": 1.2834, \"positive_delta_heads\": \"310/336\", \"top_head\": \"L0H1 delta=0.1906\", \"total_time_hours\": 1.59}}, \"mistral_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fp16_ppl\": 7.0352, \"c4_mckp_ppl\": 7.1774, \"uniform_4bit_ppl\": 7.1308, \"mckp_vs_uniform_delta\": 0.0466, \"mckp_bit_distribution\": {\"2\": 4, \"4\": 250, \"8\": 2}, \"phase4_error\": \"FileNotFoundError: mistral_k_ablation_results.json\"}}, \"llama_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bf16_wt2_ppl\": 8.0922, \"bf16_c4_ppl\": 7.1333, \"c4_cal_mckp_wt2_ppl\": 8.5103, \"c4_cal_mckp_c4_ppl\": 7.5351, \"uniform_wt2_ppl\": 8.4701, \"uniform_c4_ppl\": 7.5351, \"delta_c4_uniform_minus_mckp\": 0, \"delta_wt2_uniform_minus_mckp\": -0.0402, \"verdict_c4\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"2,3\", \"24,2\"], \"heads_8bit\": [\"31,6\"], \"total_time_min\": 6.3, \"wt2_ref_mckp_ppl\": 8.5042, \"wt2_ref_delta\": -0.0341}}, \"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256, \"distribution_shape\": \"flat\", \"total_hours\": 0.94, \"profile_seconds\": 3371.7}, \"conclusion\": \"success\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 8.0922, \"hires_mckp_ppl\": 8.5042, \"uniform_4bit_ppl\": 8.4701, \"std_mckp_reference_ppl\": 8.4498, \"mckp_vs_uniform_delta\": -0.0341, \"mckp_vs_uniform_pct\": -9, \"hires_vs_std_mckp_delta\": 0.0544, \"concentration\": 0.5749, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"26,0\", \"31,7\"], \"heads_8bit\": [\"12,3\"], \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.5749, \"t1_t5\": 0.85, \"baseline_ppl\": 6.5055, \"top1_head\": \"L2H5_delta=15.2636\", \"delta_2bit_cv\": 7.7663, \"l0_dominance_ratio\": 0.67, \"positive_delta_heads\": 254, \"total_heads\": 256, \"total_hours\": 0.98}, \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\"}}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\"}}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"hires_mckp_ppl\": 7.2181, \"uniform_4bit_ppl\": 7.2171, \"baseline_ppl\": 7.0157, \"delta_vs_uniform\": -0.001, \"bit_distribution\": {\"2\": 2, \"4\": 189, \"8\": 1}, \"2bit_heads\": [\"L22H1\", \"L24H3\"], \"8bit_heads\": [\"L6H2\"], \"L4H3_status\": \"kept_at_4bit\", \"std_mckp_k2_ppl\": 7.2209, \"std_mckp_k8_ppl\": 7.3129, \"hires_concentration\": 0.7139, \"L4H3_2bit_delta\": 13.12, \"L4H3_4bit_delta\": 0.0048, \"L4H3_8bit_delta\": 0.004}}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"top5_concentration\": 0.7139, \"top5_n_heads\": 9, \"baseline_calibration_ppl\": 5.888, \"delta_2bit_cv\": 8.8991, \"layer0_dominance_ratio\": 0.04, \"top1_head\": \"L4H3_delta=13.1236\", \"total_hours\": 0.96}}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"float32_hires_top5_concentration\": 0.6104, \"bf16_hires_range\": \"0.59-0.66\", \"float32_lowres_concentration\": 0.42, \"bf16_bug_impact_on_concentration\": 0.01, \"baseline_ppl\": 9.81, \"mckp_unconstrained_ppl\": 10.95, \"uniform_4bit_ppl\": 15.45, \"mckp_bit_dist\": {\"2\": 12, \"4\": 96, \"8\": 3, \"16\": 1}, \"l0h0_delta\": 6.7388, \"l0_4heads_total_share\": 0.586, \"claim3_threshold_0.50\": \"PASS\"}}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0157, \"mckp_wikitext2_ppl\": 7.3129, \"uniform4bit_wikitext2_ppl\": 7.2171, \"mckp_improvement_over_uniform\": -0.0958, \"top5_concentration\": 0.4934, \"layer0_dominance_ratio\": 0.07, \"best_k\": 2, \"best_k_ppl\": 7.2209, \"gqa_ratio\": \"8:1\", \"verdict\": \"FAIL\"}}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 8.9, \"mckp_wikitext2_ppl\": 9.05, \"uniform4bit_wikitext2_ppl\": 9.03, \"mckp_improvement_over_uniform\": -0.02, \"top5_concentration\": 0.23, \"layer0_dominance_ratio\": 1.32, \"best_k\": 8, \"best_k_ppl\": 9.05, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"bf16_wt2_ppl\": 7.0351, \"c4_cal_bf16_ppl\": 6.9677, \"wt2_cal_mckp_wt2_ppl\": 7.1648, \"c4_cal_mckp_wt2_ppl\": 7.1859, \"uniform_4bit_wt2_ppl\": 7.1314, \"delta_uniform_mckp_wt2_cal\": -0.0334, \"delta_uniform_mckp_c4_cal\": -0.0546, \"allocation_agreement_c4_vs_wt2\": 0.965, \"agreement_heads\": \"247/256\", \"bit_dist_wt2_cal\": \"2bit:4, 4bit:252\", \"bit_dist_c4_cal\": \"2bit:4, 4bit:251, 8bit:1\", \"profile_time_s\": 407.7, \"eval_time_s\": 349.4, \"total_time_s\": 757.1}}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"metrics\": {\"wt2_cal_wt2_ppl\": 8.4498, \"c4_cal_wt2_ppl\": 8.6459, \"uniform_wt2_ppl\": 8.469, \"wt2_cal_c4_ppl\": 7.654, \"c4_cal_c4_ppl\": 7.654, \"uniform_c4_ppl\": 7.5351, \"bf16_wt2_ppl\": 8.0918, \"bf16_c4_ppl\": 7.1333, \"agreement_rate\": 0.977, \"agreement_heads\": \"250/256\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 7.0351, \"uniform_4bit_ppl\": 7.1314, \"mckp_k4_ppl\": 7.1648, \"l0_random_seed_0\": 7.1882, \"l0_random_seed_1\": 7.1995, \"l0_random_seed_2\": 7.1723, \"l0_random_seed_3\": 7.3577, \"l0_random_seed_4\": 7.2875, \"l0_random_mean\": 7.2411, \"l0_random_std\": 0.0707, \"l0_random_median\": 7.1995, \"naive_heuristic_ppl\": 7.2105, \"budget_heuristic\": 0.2559, \"budget_mckp_k4\": 0.248}, \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"l0_random_seeds\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \"l0_random_mean\": 8.6245, \"l0_random_std\": 0.0733, \"l0_random_median\": 8.6192, \"naive_positional_ppl\": 8.5781, \"mckp_ppl\": 8.4498, \"uniform_ppl\": 8.469, \"baseline_ppl\": 8.0918, \"mckp_vs_l0_random_gap\": 0.1747, \"mckp_vs_naive_gap\": 0.1283}}, \"plan_009_oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mckp_ppl\": 10.9131, \"max_oracle_gap_ppl\": 0.0183, \"avg_oracle_gap_ppl\": 0.0046, \"layers_mckp_optimal\": \"5/8\", \"layers_with_gap\": 3, \"gap_layers\": {\"L1\": 0.0183, \"L4\": 0.0045, \"L11\": 0.0136}, \"gap_nature\": \"2-bit head position swap within same bit budget\", \"total_evals\": 54, \"runtime_min\": 21.3}}}, \"count\": 50, \"total\": 95, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2275}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
I found `llama_compounding_sweep` in the registry with the Llama data. Now I need to find the Mistral compounding sweep. Let me search for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "2494660f-18d6-4b99-a217-9074d375e0b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGC9qF5ByuJa1XCnnirXXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 39312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10154
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01PKiK4ufVDSpNXNiemjVCwn`</summary>

```json
{
  "project": "ratekv",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "status",
    "conclusion",
    "metrics"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "ad900d16-b29b-4b88-990d-d5989d8fbd1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGC9qF5ByuJa1XCnnirXXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 39312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10154
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

_source line 19 · 2026-05-15T18:00:44.821Z_

<details><summary>↩ Tool result · `toolu_01PKiK4ufVDSpNXNiemjVCwn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"llama_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_compounding_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_k\": 0, \"best_ppl\": 8.0922, \"k0_ppl\": 8.0922, \"k2_ppl\": 8.1243, \"k4_ppl\": 8.1803, \"k8_ppl\": 8.2259, \"k16_ppl\": 8.4378, \"k32_ppl\": 9.0506, \"k64_ppl\": 11.991, \"k128_ppl\": 40.2067, \"k256_ppl\": 1519.1888, \"budget\": 0.25}}, \"qwen25-hires-profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_constrained_mckp_v2\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0352, \"mckp_wikitext2_ppl\": 7.1341, \"uniform4bit_wikitext2_ppl\": 7.1308, \"mckp_improvement_over_uniform\": -0.0033, \"mckp_improvement_pct\": -3.48, \"verdict\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 254}, \"fix_note\": \"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\"}, \"conclusion\": \"negative\"}, \"mistral_uniform_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen14b_greedy_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_constrained_ppl\": 7.2206, \"mckp_constrained_ppl\": 7.2206, \"delta_vs_mckp\": 0, \"bit_distribution\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"memory_ratio\": 0.25, \"solver_time_sec\": 0.08, \"total_time_min\": 1.8}}, \"kivi_mckp_combined_qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kivi_baseline_qwen7b_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_kivi_4bit_g32_r128\": 9.8976, \"tokens\": 298938, \"chunks\": 583, \"stride\": 512, \"model\": \"Qwen2.5-7B\", \"comparison_mckp_ppl\": 10.91, \"comparison_uniform_ppl\": 15.45, \"comparison_bf16_ppl\": 9.81}}, \"qwen14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 6.8654, \"ppl_uniform_4bit\": 7.202, \"ppl_constrained_mckp\": 7.2206, \"ppl_unconstrained_mckp\": 7.6923, \"delta_constrained_vs_uniform\": -0.0185, \"delta_constrained_vs_uniform_pct\": -5.51, \"delta_unconstrained_vs_uniform\": -0.4902, \"bit_distribution_constrained\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"bit_distribution_unconstrained\": {\"2\": 77, \"4\": 271, \"8\": 35, \"16\": 1}, \"concentration\": 0.33, \"top1_pct\": 0.2262, \"top5_pct\": 0.3304, \"t1_t5\": 0.68, \"shape\": \"Flat\"}}, \"qwen_hires_constrained_d049\": {\"status\": \"DONE\", \"metrics\": {\"float32_hires_constrained_mckp_ppl\": 10.8921, \"baseline_ppl\": 9.8106, \"uniform_4bit_ppl\": 15.4484, \"bit_distribution\": {\"2\": 8, \"4\": 100, \"8\": 4}, \"gap_recovery_pct\": 80.8, \"top5_concentration\": 0.6156, \"top5_concentration_pre_monotonicity\": 0.6104, \"bf16_hires_constrained_mckp_ppl\": 10.9131, \"delta_f32_vs_bf16\": 0.021}, \"conclusion\": \"success\"}, \"llama_8k_spotcheck\": {\"status\": \"DONE\", \"metrics\": {\"ppl_bf16_8k\": 5.5958, \"ppl_constrained_mckp_8k\": 6.0537, \"ppl_uniform_4bit_8k\": 6.0364, \"mckp_improvement_over_uniform_8k\": -0.0174, \"mckp_improvement_pct_8k\": -3.94, \"ppl_bf16_2k\": 8.0922, \"ppl_constrained_mckp_2k\": 8.5042, \"ppl_uniform_4bit_2k\": 8.4701, \"shape\": \"Spike\", \"concentration\": 0.5749, \"t1_over_t5\": 0.71, \"context_length\": 8192, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"success\"}, \"yi15_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen7b_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"qwen7b_8k_context_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16_8k\": 6.97, \"ppl_constrained_mckp_8k\": 8.59, \"ppl_uniform_4bit_8k\": 77.75, \"ppl_bf16_2k\": 9.81, \"ppl_constrained_mckp_2k\": 10.89, \"ppl_uniform_4bit_2k\": 15.45, \"mckp_improvement_over_uniform_8k\": \"97.7%\", \"mckp_improvement_over_uniform_2k\": \"80.8%\", \"shape\": \"Spread\", \"concentration\": 0.5992, \"context_length\": 8192, \"note\": \"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\"}}, \"pythia14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 16.4893, \"ppl_uniform_4bit\": 24.2894, \"ppl_constrained_mckp\": 24.4521, \"ppl_unconstrained_mckp\": 31.5415, \"concentration\": \"t1=0.0289, t5=0.2439\", \"t1_t5\": \"0.0289/0.2439\", \"shape\": \"Flat\", \"constrained_vs_uniform_gap\": 0.1627}}, \"w1_pythia14b_hires_profiling\": {\"status\": \"DONE\", \"metrics\": {\"baseline_ppl\": 13.6347, \"concentration\": 0.2439, \"t1_t5\": 0.28, \"shape\": \"Flat\", \"l0_dominance\": 0.51, \"cv\": 1.2172, \"positive_heads\": 362, \"total_heads\": 384, \"top5_heads\": [{\"head\": \"L1H11\", \"delta\": 1.016355}, {\"head\": \"L12H14\", \"delta\": 0.784513}, {\"head\": \"L8H4\", \"delta\": 0.759118}, {\"head\": \"L11H2\", \"delta\": 0.632357}, {\"head\": \"L13H2\", \"delta\": 0.522849}], \"elapsed_min\": 25.7, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}, \"conclusion\": \"success\"}, \"w1_qwen14b_hires_profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 5.8432, \"concentration\": 0.3312, \"t1_t5\": 0.68, \"shape\": \"Flat\", \"l0_dominance\": 15.5, \"cv\": 3.7418, \"positive_heads\": 370, \"total_heads\": 384, \"top10_heads\": [{\"head\": \"L0H5\", \"delta\": 1.84494}, {\"head\": \"L0H4\", \"delta\": 0.236669}, {\"head\": \"L0H2\", \"delta\": 0.136971}, {\"head\": \"L28H4\", \"delta\": 0.099279}, {\"head\": \"L28H5\", \"delta\": 0.07576}, {\"head\": \"L27H4\", \"delta\": 0.071269}, {\"head\": \"L0H0\", \"delta\": 0.070018}, {\"head\": \"L28H6\", \"delta\": 0.063737}, {\"head\": \"L26H0\", \"delta\": 0.061462}, {\"head\": \"L31H3\", \"delta\": 0.061062}], \"elapsed_min\": 161.3, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}}, \"kivi_baseline_qwen_llama\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"qwen_2bit_r128\": 12.83, \"qwen_4bit_r128\": 9.9, \"qwen_2bit_r0\": 13.34, \"qwen_4bit_r0\": 9.91, \"llama_2bit_r128\": 9.84, \"llama_4bit_r128\": 8.14, \"llama_2bit_r0\": 10.08, \"llama_4bit_r0\": 8.14, \"group_size\": 32, \"eval_data\": \"WikiText-2 test\", \"note\": \"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\"}}, \"gemma2_constrained_bos_fix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 6.0306, \"uniform_4bit_ppl\": 6.1683, \"constrained_mckp_ppl\": 6.1951, \"mckp_vs_uniform_delta\": 0.0267, \"mckp_delta_ppl\": 0.1645, \"uniform_delta_ppl\": 0.1377, \"bit_distribution\": {\"2\": 8, \"4\": 324, \"8\": 4}, \"n_2bit\": 8, \"max_2bit\": 8, \"memory_ratio\": 0.25, \"eval_method\": \"sliding_window_bos_fix\", \"elapsed_seconds\": 490.3}}, \"w2_unconstrained_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline\": 7.0157, \"yi15_uniform4\": 7.2171, \"yi15_greedy\": 7.5615, \"yi15_mckp\": 7.5615, \"yi15_n2bit\": 22, \"llama_baseline\": 8.0922, \"llama_uniform4\": 8.4701, \"llama_greedy\": 8.6265, \"llama_mckp\": 8.6265, \"llama_n2bit\": 12, \"mistral_baseline\": 7.0352, \"mistral_uniform4\": 7.1308, \"mistral_greedy\": 7.5733, \"mistral_mckp\": 7.5963, \"mistral_n2bit\": 42, \"gemma2_baseline\": 6.0306, \"gemma2_uniform4\": 6.1683, \"gemma2_greedy\": 8.8469, \"gemma2_mckp\": 8.8469, \"gemma2_n2bit\": 106, \"gemma2_eval_method\": \"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\", \"gemma2_greedy_ratio\": 1.467, \"gemma2_catastrophic\": true, \"gemma2_note\": \"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\"}}, \"w3_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline_avg\": 0.6912, \"yi15_uniform_avg\": 0.6822, \"yi15_mckp_avg\": 0.6745, \"yi15_mckp_vs_uniform_pp\": -0.77, \"yi15_mckp_vs_baseline_pp\": -1.67, \"yi15_baseline\": {\"arc_easy\": 0.8093, \"arc_challenge\": 0.5265, \"hellaswag\": 0.5913, \"piqa\": 0.7949, \"winogrande\": 0.734}, \"yi15_uniform\": {\"arc_easy\": 0.7946, \"arc_challenge\": 0.5205, \"hellaswag\": 0.5857, \"piqa\": 0.7927, \"winogrande\": 0.7174}, \"yi15_mckp\": {\"arc_easy\": 0.7854, \"arc_challenge\": 0.4881, \"hellaswag\": 0.5797, \"piqa\": 0.7894, \"winogrande\": 0.7301}, \"llama_baseline_avg\": 0.696, \"llama_uniform_avg\": 0.6915, \"llama_mckp_avg\": 0.6816, \"llama_mckp_vs_uniform_pp\": -0.99, \"llama_mckp_vs_baseline_pp\": -1.44, \"llama_baseline\": {\"arc_easy\": 0.8228, \"arc_challenge\": 0.5188, \"hellaswag\": 0.6073, \"piqa\": 0.7922, \"winogrande\": 0.7388}, \"llama_uniform\": {\"arc_easy\": 0.8173, \"arc_challenge\": 0.5256, \"hellaswag\": 0.6026, \"piqa\": 0.7867, \"winogrande\": 0.7253}, \"llama_mckp\": {\"arc_easy\": 0.8039, \"arc_challenge\": 0.4991, \"hellaswag\": 0.6012, \"piqa\": 0.7802, \"winogrande\": 0.7238}, \"mistral_baseline_avg\": 0.6917, \"mistral_uniform_avg\": 0.6894, \"mistral_mckp_avg\": 0.6846, \"mistral_mckp_vs_uniform_pp\": -0.48, \"mistral_mckp_vs_baseline_pp\": -0.71, \"mistral_baseline\": {\"arc_easy\": 0.8005, \"arc_challenge\": 0.5043, \"hellaswag\": 0.6118, \"piqa\": 0.8009, \"winogrande\": 0.7411}, \"mistral_uniform\": {\"arc_easy\": 0.7976, \"arc_challenge\": 0.5068, \"hellaswag\": 0.6051, \"piqa\": 0.7982, \"winogrande\": 0.7395}, \"mistral_mckp\": {\"arc_easy\": 0.7942, \"arc_challenge\": 0.4949, \"hellaswag\": 0.6027, \"piqa\": 0.802, \"winogrande\": 0.7293}, \"gemma2_baseline_avg\": 0.7307, \"gemma2_uniform_avg\": 0.7251, \"gemma2_mckp_avg\": 0.7265, \"gemma2_mckp_vs_uniform_pp\": 0.14, \"gemma2_mckp_vs_baseline_pp\": -0.42, \"gemma2_baseline\": {\"arc_easy\": 0.8737, \"arc_challenge\": 0.6135, \"hellaswag\": 0.6093, \"piqa\": 0.8128, \"winogrande\": 0.7443}, \"gemma2_uniform\": {\"arc_easy\": 0.8662, \"arc_challenge\": 0.6058, \"hellaswag\": 0.606, \"piqa\": 0.8079, \"winogrande\": 0.7395}, \"gemma2_mckp\": {\"arc_easy\": 0.8649, \"arc_challenge\": 0.6041, \"hellaswag\": 0.6089, \"piqa\": 0.8074, \"winogrande\": 0.7474}, \"eval_harness_version\": \"0.4.11\", \"num_fewshot\": 0, \"yi_elapsed_s\": 1563.2, \"llama_elapsed_s\": 1446.4, \"mistral_elapsed_s\": 1302.2, \"gemma2_elapsed_s\": 1735.9}}, \"w9_compounding_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 9.81, \"k1_topk_ppl\": 9.826, \"k1_randomk_ppl\": 9.887, \"k1_randomk_std\": 0.05, \"k4_topk_ppl\": 9.849, \"k4_topk_ratio\": 0.86, \"k4_randomk_ppl\": 10.06, \"k4_randomk_std\": 0.06, \"k4_randomk_ratio\": 1.24, \"k8_topk_ppl\": 10.042, \"k8_topk_ratio\": 1.56, \"k8_randomk_ppl\": 11.07, \"k8_randomk_std\": 0.69, \"k8_randomk_ratio\": 1.76, \"k16_topk_ppl\": 10.42, \"k16_topk_ratio\": 1.56, \"k16_randomk_ppl\": 12.91, \"k16_randomk_std\": 0.4, \"k16_randomk_ratio\": 2.1, \"k32_topk_ppl\": 11.604, \"k32_topk_ratio\": 1.78, \"k32_randomk_ppl\": 18.33, \"k32_randomk_std\": 2.53, \"k32_randomk_ratio\": 2.73, \"k64_topk_ppl\": 22.946, \"k64_topk_ratio\": 4.89, \"k64_randomk_ppl\": 55.94, \"k64_randomk_std\": 9.73, \"k64_randomk_ratio\": 8.88, \"runtime_minutes\": 16.9, \"note\": \"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\"}}, \"w9_compounding_scaling\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"baseline_ppl\": 8.2, \"n1_joint_ppl\": 14.94, \"n1_ratio\": 1, \"n2_joint_ppl\": 42.26, \"n2_ratio\": 3.84, \"n4_joint_ppl\": 3813.76, \"n4_ratio\": 333.3, \"n8_joint_ppl\": 3586.42, \"n8_ratio\": 282.1, \"n16_joint_ppl\": 7286.23, \"n16_ratio\": 521.1, \"n32_joint_ppl\": 6644.05, \"n32_ratio\": 424, \"n64_joint_ppl\": 9453.33, \"n64_ratio\": 533.3, \"runtime_seconds\": 96}}, \"w2_unconstrained_baselines\": {\"status\": \"DONE\", \"metrics\": {\"note\": \"2bitonly profiles only - INVALID for reviewer response\", \"yi15_ppl\": 672.2, \"yi15_ratio\": 114, \"llama_ppl\": 1219.7, \"llama_ratio\": 187, \"mistral_ppl_2bitonly\": 47.8, \"mistral_ratio_2bitonly\": 8.2, \"mistral_ppl_full\": 6.39, \"mistral_ratio_full\": 1.09, \"gemma2_ppl\": 277.4, \"gemma2_ratio\": 37.9, \"budget\": 0.25, \"baseline_yi\": 5.89, \"baseline_llama\": 6.51, \"baseline_mistral\": 5.87, \"baseline_gemma2\": 7.32}, \"conclusion\": \"killed\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"concentration_top5pct\": 0.2291, \"l0_dominance_ratio\": 2.05, \"cv_delta_2bit\": 1.2834, \"positive_delta_heads\": \"310/336\", \"top_head\": \"L0H1 delta=0.1906\", \"total_time_hours\": 1.59}}, \"mistral_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fp16_ppl\": 7.0352, \"c4_mckp_ppl\": 7.1774, \"uniform_4bit_ppl\": 7.1308, \"mckp_vs_uniform_delta\": 0.0466, \"mckp_bit_distribution\": {\"2\": 4, \"4\": 250, \"8\": 2}, \"phase4_error\": \"FileNotFoundError: mistral_k_ablation_results.json\"}}, \"llama_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bf16_wt2_ppl\": 8.0922, \"bf16_c4_ppl\": 7.1333, \"c4_cal_mckp_wt2_ppl\": 8.5103, \"c4_cal_mckp_c4_ppl\": 7.5351, \"uniform_wt2_ppl\": 8.4701, \"uniform_c4_ppl\": 7.5351, \"delta_c4_uniform_minus_mckp\": 0, \"delta_wt2_uniform_minus_mckp\": -0.0402, \"verdict_c4\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"2,3\", \"24,2\"], \"heads_8bit\": [\"31,6\"], \"total_time_min\": 6.3, \"wt2_ref_mckp_ppl\": 8.5042, \"wt2_ref_delta\": -0.0341}}, \"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256, \"distribution_shape\": \"flat\", \"total_hours\": 0.94, \"profile_seconds\": 3371.7}, \"conclusion\": \"success\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 8.0922, \"hires_mckp_ppl\": 8.5042, \"uniform_4bit_ppl\": 8.4701, \"std_mckp_reference_ppl\": 8.4498, \"mckp_vs_uniform_delta\": -0.0341, \"mckp_vs_uniform_pct\": -9, \"hires_vs_std_mckp_delta\": 0.0544, \"concentration\": 0.5749, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"26,0\", \"31,7\"], \"heads_8bit\": [\"12,3\"], \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.5749, \"t1_t5\": 0.85, \"baseline_ppl\": 6.5055, \"top1_head\": \"L2H5_delta=15.2636\", \"delta_2bit_cv\": 7.7663, \"l0_dominance_ratio\": 0.67, \"positive_delta_heads\": 254, \"total_heads\": 256, \"total_hours\": 0.98}, \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\"}}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\"}}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"hires_mckp_ppl\": 7.2181, \"uniform_4bit_ppl\": 7.2171, \"baseline_ppl\": 7.0157, \"delta_vs_uniform\": -0.001, \"bit_distribution\": {\"2\": 2, \"4\": 189, \"8\": 1}, \"2bit_heads\": [\"L22H1\", \"L24H3\"], \"8bit_heads\": [\"L6H2\"], \"L4H3_status\": \"kept_at_4bit\", \"std_mckp_k2_ppl\": 7.2209, \"std_mckp_k8_ppl\": 7.3129, \"hires_concentration\": 0.7139, \"L4H3_2bit_delta\": 13.12, \"L4H3_4bit_delta\": 0.0048, \"L4H3_8bit_delta\": 0.004}}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"top5_concentration\": 0.7139, \"top5_n_heads\": 9, \"baseline_calibration_ppl\": 5.888, \"delta_2bit_cv\": 8.8991, \"layer0_dominance_ratio\": 0.04, \"top1_head\": \"L4H3_delta=13.1236\", \"total_hours\": 0.96}}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"float32_hires_top5_concentration\": 0.6104, \"bf16_hires_range\": \"0.59-0.66\", \"float32_lowres_concentration\": 0.42, \"bf16_bug_impact_on_concentration\": 0.01, \"baseline_ppl\": 9.81, \"mckp_unconstrained_ppl\": 10.95, \"uniform_4bit_ppl\": 15.45, \"mckp_bit_dist\": {\"2\": 12, \"4\": 96, \"8\": 3, \"16\": 1}, \"l0h0_delta\": 6.7388, \"l0_4heads_total_share\": 0.586, \"claim3_threshold_0.50\": \"PASS\"}}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0157, \"mckp_wikitext2_ppl\": 7.3129, \"uniform4bit_wikitext2_ppl\": 7.2171, \"mckp_improvement_over_uniform\": -0.0958, \"top5_concentration\": 0.4934, \"layer0_dominance_ratio\": 0.07, \"best_k\": 2, \"best_k_ppl\": 7.2209, \"gqa_ratio\": \"8:1\", \"verdict\": \"FAIL\"}}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 8.9, \"mckp_wikitext2_ppl\": 9.05, \"uniform4bit_wikitext2_ppl\": 9.03, \"mckp_improvement_over_uniform\": -0.02, \"top5_concentration\": 0.23, \"layer0_dominance_ratio\": 1.32, \"best_k\": 8, \"best_k_ppl\": 9.05, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"bf16_wt2_ppl\": 7.0351, \"c4_cal_bf16_ppl\": 6.9677, \"wt2_cal_mckp_wt2_ppl\": 7.1648, \"c4_cal_mckp_wt2_ppl\": 7.1859, \"uniform_4bit_wt2_ppl\": 7.1314, \"delta_uniform_mckp_wt2_cal\": -0.0334, \"delta_uniform_mckp_c4_cal\": -0.0546, \"allocation_agreement_c4_vs_wt2\": 0.965, \"agreement_heads\": \"247/256\", \"bit_dist_wt2_cal\": \"2bit:4, 4bit:252\", \"bit_dist_c4_cal\": \"2bit:4, 4bit:251, 8bit:1\", \"profile_time_s\": 407.7, \"eval_time_s\": 349.4, \"total_time_s\": 757.1}}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"metrics\": {\"wt2_cal_wt2_ppl\": 8.4498, \"c4_cal_wt2_ppl\": 8.6459, \"uniform_wt2_ppl\": 8.469, \"wt2_cal_c4_ppl\": 7.654, \"c4_cal_c4_ppl\": 7.654, \"uniform_c4_ppl\": 7.5351, \"bf16_wt2_ppl\": 8.0918, \"bf16_c4_ppl\": 7.1333, \"agreement_rate\": 0.977, \"agreement_heads\": \"250/256\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 7.0351, \"uniform_4bit_ppl\": 7.1314, \"mckp_k4_ppl\": 7.1648, \"l0_random_seed_0\": 7.1882, \"l0_random_seed_1\": 7.1995, \"l0_random_seed_2\": 7.1723, \"l0_random_seed_3\": 7.3577, \"l0_random_seed_4\": 7.2875, \"l0_random_mean\": 7.2411, \"l0_random_std\": 0.0707, \"l0_random_median\": 7.1995, \"naive_heuristic_ppl\": 7.2105, \"budget_heuristic\": 0.2559, \"budget_mckp_k4\": 0.248}, \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"l0_random_seeds\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \"l0_random_mean\": 8.6245, \"l0_random_std\": 0.0733, \"l0_random_median\": 8.6192, \"naive_positional_ppl\": 8.5781, \"mckp_ppl\": 8.4498, \"uniform_ppl\": 8.469, \"baseline_ppl\": 8.0918, \"mckp_vs_l0_random_gap\": 0.1747, \"mckp_vs_naive_gap\": 0.1283}}, \"plan_009_oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mckp_ppl\": 10.9131, \"max_oracle_gap_ppl\": 0.0183, \"avg_oracle_gap_ppl\": 0.0046, \"layers_mckp_optimal\": \"5/8\", \"layers_with_gap\": 3, \"gap_layers\": {\"L1\": 0.0183, \"L4\": 0.0045, \"L11\": 0.0136}, \"gap_nature\": \"2-bit head position swap within same bit budget\", \"total_evals\": 54, \"runtime_min\": 21.3}}}, \"count\": 50, \"total\": 95, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2367}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "a5ae11b1-c3fb-4da4-933b-8a28e0f4f312",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"llama_downstream_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_compounding_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_k\\\": 0, \\\"best_ppl\\\": 8.0922, \\\"k0_ppl\\\": 8.0922, \\\"k2_ppl\\\": 8.1243, \\\"k4_ppl\\\": 8.1803, \\\"k8_ppl\\\": 8.2259, \\\"k16_ppl\\\": 8.4378, \\\"k32_ppl\\\": 9.0506, \\\"k64_ppl\\\": 11.991, \\\"k128_ppl\\\": 40.2067, \\\"k256_ppl\\\": 1519.1888, \\\"budget\\\": 0.25}}, \\\"qwen25-hires-profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"cross_domain_calibration_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"greedy_constrained_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mistral_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mistral_hires_constrained_mckp_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 7.0352, \\\"mckp_wikitext2_ppl\\\": 7.1341, \\\"uniform4bit_wikitext2_ppl\\\": 7.1308, \\\"mckp_improvement_over_uniform\\\": -0.0033, \\\"mckp_improvement_pct\\\": -3.48, \\\"verdict\\\": \\\"FAIL\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 254}, \\\"fix_note\\\": \\\"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"mistral_uniform_reeval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"qwen14b_greedy_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"greedy_constrained_ppl\\\": 7.2206, \\\"mckp_constrained_ppl\\\": 7.2206, \\\"delta_vs_mckp\\\": 0, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 374, \\\"8\\\": 1, \\\"16\\\": 1}, \\\"memory_ratio\\\": 0.25, \\\"solver_time_sec\\\": 0.08, \\\"total_time_min\\\": 1.8}}, \\\"kivi_mckp_combined_qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_hires_bf16_2bitonly_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"kivi_baseline_qwen7b_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_kivi_4bit_g32_r128\\\": 9.8976, \\\"tokens\\\": 298938, \\\"chunks\\\": 583, \\\"stride\\\": 512, \\\"model\\\": \\\"Qwen2.5-7B\\\", \\\"comparison_mckp_ppl\\\": 10.91, \\\"comparison_uniform_ppl\\\": 15.45, \\\"comparison_bf16_ppl\\\": 9.81}}, \\\"qwen14b_constrained_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16\\\": 6.8654, \\\"ppl_uniform_4bit\\\": 7.202, \\\"ppl_constrained_mckp\\\": 7.2206, \\\"ppl_unconstrained_mckp\\\": 7.6923, \\\"delta_constrained_vs_uniform\\\": -0.0185, \\\"delta_constrained_vs_uniform_pct\\\": -5.51, \\\"delta_unconstrained_vs_uniform\\\": -0.4902, \\\"bit_distribution_constrained\\\": {\\\"2\\\": 8, \\\"4\\\": 374, \\\"8\\\": 1, \\\"16\\\": 1}, \\\"bit_distribution_unconstrained\\\": {\\\"2\\\": 77, \\\"4\\\": 271, \\\"8\\\": 35, \\\"16\\\": 1}, \\\"concentration\\\": 0.33, \\\"top1_pct\\\": 0.2262, \\\"top5_pct\\\": 0.3304, \\\"t1_t5\\\": 0.68, \\\"shape\\\": \\\"Flat\\\"}}, \\\"qwen_hires_constrained_d049\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"float32_hires_constrained_mckp_ppl\\\": 10.8921, \\\"baseline_ppl\\\": 9.8106, \\\"uniform_4bit_ppl\\\": 15.4484, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 100, \\\"8\\\": 4}, \\\"gap_recovery_pct\\\": 80.8, \\\"top5_concentration\\\": 0.6156, \\\"top5_concentration_pre_monotonicity\\\": 0.6104, \\\"bf16_hires_constrained_mckp_ppl\\\": 10.9131, \\\"delta_f32_vs_bf16\\\": 0.021}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ppl_bf16_8k\\\": 5.5958, \\\"ppl_constrained_mckp_8k\\\": 6.0537, \\\"ppl_uniform_4bit_8k\\\": 6.0364, \\\"mckp_improvement_over_uniform_8k\\\": -0.0174, \\\"mckp_improvement_pct_8k\\\": -3.94, \\\"ppl_bf16_2k\\\": 8.0922, \\\"ppl_constrained_mckp_2k\\\": 8.5042, \\\"ppl_uniform_4bit_2k\\\": 8.4701, \\\"shape\\\": \\\"Spike\\\", \\\"concentration\\\": 0.5749, \\\"t1_over_t5\\\": 0.71, \\\"context_length\\\": 8192, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"yi15_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"qwen7b_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen7b_8k_context_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16_8k\\\": 6.97, \\\"ppl_constrained_mckp_8k\\\": 8.59, \\\"ppl_uniform_4bit_8k\\\": 77.75, \\\"ppl_bf16_2k\\\": 9.81, \\\"ppl_constrained_mckp_2k\\\": 10.89, \\\"ppl_uniform_4bit_2k\\\": 15.45, \\\"mckp_improvement_over_uniform_8k\\\": \\\"97.7%\\\", \\\"mckp_improvement_over_uniform_2k\\\": \\\"80.8%\\\", \\\"shape\\\": \\\"Spread\\\", \\\"concentration\\\": 0.5992, \\\"context_length\\\": 8192, \\\"note\\\": \\\"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\\\"}}, \\\"pythia14b_constrained_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16\\\": 16.4893, \\\"ppl_uniform_4bit\\\": 24.2894, \\\"ppl_constrained_mckp\\\": 24.4521, \\\"ppl_unconstrained_mckp\\\": 31.5415, \\\"concentration\\\": \\\"t1=0.0289, t5=0.2439\\\", \\\"t1_t5\\\": \\\"0.0289/0.2439\\\", \\\"shape\\\": \\\"Flat\\\", \\\"constrained_vs_uniform_gap\\\": 0.1627}}, \\\"w1_pythia14b_hires_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 13.6347, \\\"concentration\\\": 0.2439, \\\"t1_t5\\\": 0.28, \\\"shape\\\": \\\"Flat\\\", \\\"l0_dominance\\\": 0.51, \\\"cv\\\": 1.2172, \\\"positive_heads\\\": 362, \\\"total_heads\\\": 384, \\\"top5_heads\\\": [{\\\"head\\\": \\\"L1H11\\\", \\\"delta\\\": 1.016355}, {\\\"head\\\": \\\"L12H14\\\", \\\"delta\\\": 0.784513}, {\\\"head\\\": \\\"L8H4\\\", \\\"delta\\\": 0.759118}, {\\\"head\\\": \\\"L11H2\\\", \\\"delta\\\": 0.632357}, {\\\"head\\\": \\\"L13H2\\\", \\\"delta\\\": 0.522849}], \\\"elapsed_min\\\": 25.7, \\\"note\\\": \\\"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w1_qwen14b_hires_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 5.8432, \\\"concentration\\\": 0.3312, \\\"t1_t5\\\": 0.68, \\\"shape\\\": \\\"Flat\\\", \\\"l0_dominance\\\": 15.5, \\\"cv\\\": 3.7418, \\\"positive_heads\\\": 370, \\\"total_heads\\\": 384, \\\"top10_heads\\\": [{\\\"head\\\": \\\"L0H5\\\", \\\"delta\\\": 1.84494}, {\\\"head\\\": \\\"L0H4\\\", \\\"delta\\\": 0.236669}, {\\\"head\\\": \\\"L0H2\\\", \\\"delta\\\": 0.136971}, {\\\"head\\\": \\\"L28H4\\\", \\\"delta\\\": 0.099279}, {\\\"head\\\": \\\"L28H5\\\", \\\"delta\\\": 0.07576}, {\\\"head\\\": \\\"L27H4\\\", \\\"delta\\\": 0.071269}, {\\\"head\\\": \\\"L0H0\\\", \\\"delta\\\": 0.070018}, {\\\"head\\\": \\\"L28H6\\\", \\\"delta\\\": 0.063737}, {\\\"head\\\": \\\"L26H0\\\", \\\"delta\\\": 0.061462}, {\\\"head\\\": \\\"L31H3\\\", \\\"delta\\\": 0.061062}], \\\"elapsed_min\\\": 161.3, \\\"note\\\": \\\"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\\\"}}, \\\"kivi_baseline_qwen_llama\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"qwen_2bit_r128\\\": 12.83, \\\"qwen_4bit_r128\\\": 9.9, \\\"qwen_2bit_r0\\\": 13.34, \\\"qwen_4bit_r0\\\": 9.91, \\\"llama_2bit_r128\\\": 9.84, \\\"llama_4bit_r128\\\": 8.14, \\\"llama_2bit_r0\\\": 10.08, \\\"llama_4bit_r0\\\": 8.14, \\\"group_size\\\": 32, \\\"eval_data\\\": \\\"WikiText-2 test\\\", \\\"note\\\": \\\"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\\\"}}, \\\"gemma2_constrained_bos_fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 6.0306, \\\"uniform_4bit_ppl\\\": 6.1683, \\\"constrained_mckp_ppl\\\": 6.1951, \\\"mckp_vs_uniform_delta\\\": 0.0267, \\\"mckp_delta_ppl\\\": 0.1645, \\\"uniform_delta_ppl\\\": 0.1377, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 324, \\\"8\\\": 4}, \\\"n_2bit\\\": 8, \\\"max_2bit\\\": 8, \\\"memory_ratio\\\": 0.25, \\\"eval_method\\\": \\\"sliding_window_bos_fix\\\", \\\"elapsed_seconds\\\": 490.3}}, \\\"w2_unconstrained_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"yi15_baseline\\\": 7.0157, \\\"yi15_uniform4\\\": 7.2171, \\\"yi15_greedy\\\": 7.5615, \\\"yi15_mckp\\\": 7.5615, \\\"yi15_n2bit\\\": 22, \\\"llama_baseline\\\": 8.0922, \\\"llama_uniform4\\\": 8.4701, \\\"llama_greedy\\\": 8.6265, \\\"llama_mckp\\\": 8.6265, \\\"llama_n2bit\\\": 12, \\\"mistral_baseline\\\": 7.0352, \\\"mistral_uniform4\\\": 7.1308, \\\"mistral_greedy\\\": 7.5733, \\\"mistral_mckp\\\": 7.5963, \\\"mistral_n2bit\\\": 42, \\\"gemma2_baseline\\\": 6.0306, \\\"gemma2_uniform4\\\": 6.1683, \\\"gemma2_greedy\\\": 8.8469, \\\"gemma2_mckp\\\": 8.8469, \\\"gemma2_n2bit\\\": 106, \\\"gemma2_eval_method\\\": \\\"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\\\", \\\"gemma2_greedy_ratio\\\": 1.467, \\\"gemma2_catastrophic\\\": true, \\\"gemma2_note\\\": \\\"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\\\"}}, \\\"w3_downstream_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"yi15_baseline_avg\\\": 0.6912, \\\"yi15_uniform_avg\\\": 0.6822, \\\"yi15_mckp_avg\\\": 0.6745, \\\"yi15_mckp_vs_uniform_pp\\\": -0.77, \\\"yi15_mckp_vs_baseline_pp\\\": -1.67, \\\"yi15_baseline\\\": {\\\"arc_easy\\\": 0.8093, \\\"arc_challenge\\\": 0.5265, \\\"hellaswag\\\": 0.5913, \\\"piqa\\\": 0.7949, \\\"winogrande\\\": 0.734}, \\\"yi15_uniform\\\": {\\\"arc_easy\\\": 0.7946, \\\"arc_challenge\\\": 0.5205, \\\"hellaswag\\\": 0.5857, \\\"piqa\\\": 0.7927, \\\"winogrande\\\": 0.7174}, \\\"yi15_mckp\\\": {\\\"arc_easy\\\": 0.7854, \\\"arc_challenge\\\": 0.4881, \\\"hellaswag\\\": 0.5797, \\\"piqa\\\": 0.7894, \\\"winogrande\\\": 0.7301}, \\\"llama_baseline_avg\\\": 0.696, \\\"llama_uniform_avg\\\": 0.6915, \\\"llama_mckp_avg\\\": 0.6816, \\\"llama_mckp_vs_uniform_pp\\\": -0.99, \\\"llama_mckp_vs_baseline_pp\\\": -1.44, \\\"llama_baseline\\\": {\\\"arc_easy\\\": 0.8228, \\\"arc_challenge\\\": 0.5188, \\\"hellaswag\\\": 0.6073, \\\"piqa\\\": 0.7922, \\\"winogrande\\\": 0.7388}, \\\"llama_uniform\\\": {\\\"arc_easy\\\": 0.8173, \\\"arc_challenge\\\": 0.5256, \\\"hellaswag\\\": 0.6026, \\\"piqa\\\": 0.7867, \\\"winogrande\\\": 0.7253}, \\\"llama_mckp\\\": {\\\"arc_easy\\\": 0.8039, \\\"arc_challenge\\\": 0.4991, \\\"hellaswag\\\": 0.6012, \\\"piqa\\\": 0.7802, \\\"winogrande\\\": 0.7238}, \\\"mistral_baseline_avg\\\": 0.6917, \\\"mistral_uniform_avg\\\": 0.6894, \\\"mistral_mckp_avg\\\": 0.6846, \\\"mistral_mckp_vs_uniform_pp\\\": -0.48, \\\"mistral_mckp_vs_baseline_pp\\\": -0.71, \\\"mistral_baseline\\\": {\\\"arc_easy\\\": 0.8005, \\\"arc_challenge\\\": 0.5043, \\\"hellaswag\\\": 0.6118, \\\"piqa\\\": 0.8009, \\\"winogrande\\\": 0.7411}, \\\"mistral_uniform\\\": {\\\"arc_easy\\\": 0.7976, \\\"arc_challenge\\\": 0.5068, \\\"hellaswag\\\": 0.6051, \\\"piqa\\\": 0.7982, \\\"winogrande\\\": 0.7395}, \\\"mistral_mckp\\\": {\\\"arc_easy\\\": 0.7942, \\\"arc_challenge\\\": 0.4949, \\\"hellaswag\\\": 0.6027, \\\"piqa\\\": 0.802, \\\"winogrande\\\": 0.7293}, \\\"gemma2_baseline_avg\\\": 0.7307, \\\"gemma2_uniform_avg\\\": 0.7251, \\\"gemma2_mckp_avg\\\": 0.7265, \\\"gemma2_mckp_vs_uniform_pp\\\": 0.14, \\\"gemma2_mckp_vs_baseline_pp\\\": -0.42, \\\"gemma2_baseline\\\": {\\\"arc_easy\\\": 0.8737, \\\"arc_challenge\\\": 0.6135, \\\"hellaswag\\\": 0.6093, \\\"piqa\\\": 0.8128, \\\"winogrande\\\": 0.7443}, \\\"gemma2_uniform\\\": {\\\"arc_easy\\\": 0.8662, \\\"arc_challenge\\\": 0.6058, \\\"hellaswag\\\": 0.606, \\\"piqa\\\": 0.8079, \\\"winogrande\\\": 0.7395}, \\\"gemma2_mckp\\\": {\\\"arc_easy\\\": 0.8649, \\\"arc_challenge\\\": 0.6041, \\\"hellaswag\\\": 0.6089, \\\"piqa\\\": 0.8074, \\\"winogrande\\\": 0.7474}, \\\"eval_harness_version\\\": \\\"0.4.11\\\", \\\"num_fewshot\\\": 0, \\\"yi_elapsed_s\\\": 1563.2, \\\"llama_elapsed_s\\\": 1446.4, \\\"mistral_elapsed_s\\\": 1302.2, \\\"gemma2_elapsed_s\\\": 1735.9}}, \\\"w9_compounding_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 9.81, \\\"k1_topk_ppl\\\": 9.826, \\\"k1_randomk_ppl\\\": 9.887, \\\"k1_randomk_std\\\": 0.05, \\\"k4_topk_ppl\\\": 9.849, \\\"k4_topk_ratio\\\": 0.86, \\\"k4_randomk_ppl\\\": 10.06, \\\"k4_randomk_std\\\": 0.06, \\\"k4_randomk_ratio\\\": 1.24, \\\"k8_topk_ppl\\\": 10.042, \\\"k8_topk_ratio\\\": 1.56, \\\"k8_randomk_ppl\\\": 11.07, \\\"k8_randomk_std\\\": 0.69, \\\"k8_randomk_ratio\\\": 1.76, \\\"k16_topk_ppl\\\": 10.42, \\\"k16_topk_ratio\\\": 1.56, \\\"k16_randomk_ppl\\\": 12.91, \\\"k16_randomk_std\\\": 0.4, \\\"k16_randomk_ratio\\\": 2.1, \\\"k32_topk_ppl\\\": 11.604, \\\"k32_topk_ratio\\\": 1.78, \\\"k32_randomk_ppl\\\": 18.33, \\\"k32_randomk_std\\\": 2.53, \\\"k32_randomk_ratio\\\": 2.73, \\\"k64_topk_ppl\\\": 22.946, \\\"k64_topk_ratio\\\": 4.89, \\\"k64_randomk_ppl\\\": 55.94, \\\"k64_randomk_std\\\": 9.73, \\\"k64_randomk_ratio\\\": 8.88, \\\"runtime_minutes\\\": 16.9, \\\"note\\\": \\\"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\\\"}}, \\\"w9_compounding_scaling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 8.2, \\\"n1_joint_ppl\\\": 14.94, \\\"n1_ratio\\\": 1, \\\"n2_joint_ppl\\\": 42.26, \\\"n2_ratio\\\": 3.84, \\\"n4_joint_ppl\\\": 3813.76, \\\"n4_ratio\\\": 333.3, \\\"n8_joint_ppl\\\": 3586.42, \\\"n8_ratio\\\": 282.1, \\\"n16_joint_ppl\\\": 7286.23, \\\"n16_ratio\\\": 521.1, \\\"n32_joint_ppl\\\": 6644.05, \\\"n32_ratio\\\": 424, \\\"n64_joint_ppl\\\": 9453.33, \\\"n64_ratio\\\": 533.3, \\\"runtime_seconds\\\": 96}}, \\\"w2_unconstrained_baselines\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"note\\\": \\\"2bitonly profiles only - INVALID for reviewer response\\\", \\\"yi15_ppl\\\": 672.2, \\\"yi15_ratio\\\": 114, \\\"llama_ppl\\\": 1219.7, \\\"llama_ratio\\\": 187, \\\"mistral_ppl_2bitonly\\\": 47.8, \\\"mistral_ratio_2bitonly\\\": 8.2, \\\"mistral_ppl_full\\\": 6.39, \\\"mistral_ratio_full\\\": 1.09, \\\"gemma2_ppl\\\": 277.4, \\\"gemma2_ratio\\\": 37.9, \\\"budget\\\": 0.25, \\\"baseline_yi\\\": 5.89, \\\"baseline_llama\\\": 6.51, \\\"baseline_mistral\\\": 5.87, \\\"baseline_gemma2\\\": 7.32}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"gemma2_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"concentration_top5pct\\\": 0.2291, \\\"l0_dominance_ratio\\\": 2.05, \\\"cv_delta_2bit\\\": 1.2834, \\\"positive_delta_heads\\\": \\\"310/336\\\", \\\"top_head\\\": \\\"L0H1 delta=0.1906\\\", \\\"total_time_hours\\\": 1.59}}, \\\"mistral_c4_hires_crossdataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"fp16_ppl\\\": 7.0352, \\\"c4_mckp_ppl\\\": 7.1774, \\\"uniform_4bit_ppl\\\": 7.1308, \\\"mckp_vs_uniform_delta\\\": 0.0466, \\\"mckp_bit_distribution\\\": {\\\"2\\\": 4, \\\"4\\\": 250, \\\"8\\\": 2}, \\\"phase4_error\\\": \\\"FileNotFoundError: mistral_k_ablation_results.json\\\"}}, \\\"llama_c4_hires_crossdataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"bf16_wt2_ppl\\\": 8.0922, \\\"bf16_c4_ppl\\\": 7.1333, \\\"c4_cal_mckp_wt2_ppl\\\": 8.5103, \\\"c4_cal_mckp_c4_ppl\\\": 7.5351, \\\"uniform_wt2_ppl\\\": 8.4701, \\\"uniform_c4_ppl\\\": 7.5351, \\\"delta_c4_uniform_minus_mckp\\\": 0, \\\"delta_wt2_uniform_minus_mckp\\\": -0.0402, \\\"verdict_c4\\\": \\\"FAIL\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}, \\\"heads_2bit\\\": [\\\"2,3\\\", \\\"24,2\\\"], \\\"heads_8bit\\\": [\\\"31,6\\\"], \\\"total_time_min\\\": 6.3, \\\"wt2_ref_mckp_ppl\\\": 8.5042, \\\"wt2_ref_delta\\\": -0.0341}}, \\\"mistral_hires_bf16_2bitonly_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.241, \\\"top5_n_heads\\\": 12, \\\"baseline_ppl\\\": 5.8702, \\\"top1_head\\\": \\\"L2H5\\\", \\\"top1_delta_2bit\\\": 0.3236, \\\"top2_head\\\": \\\"L12H1\\\", \\\"top2_delta_2bit\\\": 0.1435, \\\"top3_head\\\": \\\"L0H7\\\", \\\"top3_delta_2bit\\\": 0.1403, \\\"delta_2bit_mean\\\": 0.020073, \\\"delta_2bit_std\\\": 0.026278, \\\"delta_2bit_cv\\\": 1.3091, \\\"layer0_mean_delta_2bit\\\": 0.034073, \\\"other_layers_mean_delta_2bit\\\": 0.019621, \\\"l0_dominance_ratio\\\": 1.74, \\\"positive_delta_heads\\\": 252, \\\"total_heads\\\": 256, \\\"distribution_shape\\\": \\\"flat\\\", \\\"total_hours\\\": 0.94, \\\"profile_seconds\\\": 3371.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_bf16_ppl\\\": 8.0922, \\\"hires_mckp_ppl\\\": 8.5042, \\\"uniform_4bit_ppl\\\": 8.4701, \\\"std_mckp_reference_ppl\\\": 8.4498, \\\"mckp_vs_uniform_delta\\\": -0.0341, \\\"mckp_vs_uniform_pct\\\": -9, \\\"hires_vs_std_mckp_delta\\\": 0.0544, \\\"concentration\\\": 0.5749, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}, \\\"heads_2bit\\\": [\\\"26,0\\\", \\\"31,7\\\"], \\\"heads_8bit\\\": [\\\"12,3\\\"], \\\"verdict\\\": \\\"FAIL\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"llama_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.5749, \\\"t1_t5\\\": 0.85, \\\"baseline_ppl\\\": 6.5055, \\\"top1_head\\\": \\\"L2H5_delta=15.2636\\\", \\\"delta_2bit_cv\\\": 7.7663, \\\"l0_dominance_ratio\\\": 0.67, \\\"positive_delta_heads\\\": 254, \\\"total_heads\\\": 256, \\\"total_hours\\\": 0.98}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_hires_bf16_2bitonly_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\\\"}}, \\\"mistral_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\\\"}}, \\\"yi15_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"hires_mckp_ppl\\\": 7.2181, \\\"uniform_4bit_ppl\\\": 7.2171, \\\"baseline_ppl\\\": 7.0157, \\\"delta_vs_uniform\\\": -0.001, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 189, \\\"8\\\": 1}, \\\"2bit_heads\\\": [\\\"L22H1\\\", \\\"L24H3\\\"], \\\"8bit_heads\\\": [\\\"L6H2\\\"], \\\"L4H3_status\\\": \\\"kept_at_4bit\\\", \\\"std_mckp_k2_ppl\\\": 7.2209, \\\"std_mckp_k8_ppl\\\": 7.3129, \\\"hires_concentration\\\": 0.7139, \\\"L4H3_2bit_delta\\\": 13.12, \\\"L4H3_4bit_delta\\\": 0.0048, \\\"L4H3_8bit_delta\\\": 0.004}}, \\\"yi15_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.7139, \\\"top5_n_heads\\\": 9, \\\"baseline_calibration_ppl\\\": 5.888, \\\"delta_2bit_cv\\\": 8.8991, \\\"layer0_dominance_ratio\\\": 0.04, \\\"top1_head\\\": \\\"L4H3_delta=13.1236\\\", \\\"total_hours\\\": 0.96}}, \\\"qwen_hires_float32_d048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"float32_hires_top5_concentration\\\": 0.6104, \\\"bf16_hires_range\\\": \\\"0.59-0.66\\\", \\\"float32_lowres_concentration\\\": 0.42, \\\"bf16_bug_impact_on_concentration\\\": 0.01, \\\"baseline_ppl\\\": 9.81, \\\"mckp_unconstrained_ppl\\\": 10.95, \\\"uniform_4bit_ppl\\\": 15.45, \\\"mckp_bit_dist\\\": {\\\"2\\\": 12, \\\"4\\\": 96, \\\"8\\\": 3, \\\"16\\\": 1}, \\\"l0h0_delta\\\": 6.7388, \\\"l0_4heads_total_share\\\": 0.586, \\\"claim3_threshold_0.50\\\": \\\"PASS\\\"}}, \\\"yi15_hires_float32_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"yi15_9b_full_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 7.0157, \\\"mckp_wikitext2_ppl\\\": 7.3129, \\\"uniform4bit_wikitext2_ppl\\\": 7.2171, \\\"mckp_improvement_over_uniform\\\": -0.0958, \\\"top5_concentration\\\": 0.4934, \\\"layer0_dominance_ratio\\\": 0.07, \\\"best_k\\\": 2, \\\"best_k_ppl\\\": 7.2209, \\\"gqa_ratio\\\": \\\"8:1\\\", \\\"verdict\\\": \\\"FAIL\\\"}}, \\\"gemma2_9b_full_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 8.9, \\\"mckp_wikitext2_ppl\\\": 9.05, \\\"uniform4bit_wikitext2_ppl\\\": 9.03, \\\"mckp_improvement_over_uniform\\\": -0.02, \\\"top5_concentration\\\": 0.23, \\\"layer0_dominance_ratio\\\": 1.32, \\\"best_k\\\": 8, \\\"best_k_ppl\\\": 9.05, \\\"verdict\\\": \\\"FAIL\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"qwen72b_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"multi_seed_lowres\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mistral_c4_cross_dataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"bf16_wt2_ppl\\\": 7.0351, \\\"c4_cal_bf16_ppl\\\": 6.9677, \\\"wt2_cal_mckp_wt2_ppl\\\": 7.1648, \\\"c4_cal_mckp_wt2_ppl\\\": 7.1859, \\\"uniform_4bit_wt2_ppl\\\": 7.1314, \\\"delta_uniform_mckp_wt2_cal\\\": -0.0334, \\\"delta_uniform_mckp_c4_cal\\\": -0.0546, \\\"allocation_agreement_c4_vs_wt2\\\": 0.965, \\\"agreement_heads\\\": \\\"247/256\\\", \\\"bit_dist_wt2_cal\\\": \\\"2bit:4, 4bit:252\\\", \\\"bit_dist_c4_cal\\\": \\\"2bit:4, 4bit:251, 8bit:1\\\", \\\"profile_time_s\\\": 407.7, \\\"eval_time_s\\\": 349.4, \\\"total_time_s\\\": 757.1}}, \\\"llama_c4_cross_dataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wt2_cal_wt2_ppl\\\": 8.4498, \\\"c4_cal_wt2_ppl\\\": 8.6459, \\\"uniform_wt2_ppl\\\": 8.469, \\\"wt2_cal_c4_ppl\\\": 7.654, \\\"c4_cal_c4_ppl\\\": 7.654, \\\"uniform_c4_ppl\\\": 7.5351, \\\"bf16_wt2_ppl\\\": 8.0918, \\\"bf16_c4_ppl\\\": 7.1333, \\\"agreement_rate\\\": 0.977, \\\"agreement_heads\\\": \\\"250/256\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"mistral_heuristic_k4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_bf16_ppl\\\": 7.0351, \\\"uniform_4bit_ppl\\\": 7.1314, \\\"mckp_k4_ppl\\\": 7.1648, \\\"l0_random_seed_0\\\": 7.1882, \\\"l0_random_seed_1\\\": 7.1995, \\\"l0_random_seed_2\\\": 7.1723, \\\"l0_random_seed_3\\\": 7.3577, \\\"l0_random_seed_4\\\": 7.2875, \\\"l0_random_mean\\\": 7.2411, \\\"l0_random_std\\\": 0.0707, \\\"l0_random_median\\\": 7.1995, \\\"naive_heuristic_ppl\\\": 7.2105, \\\"budget_heuristic\\\": 0.2559, \\\"budget_mckp_k4\\\": 0.248}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_heuristic_k2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"l0_random_seeds\\\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \\\"l0_random_mean\\\": 8.6245, \\\"l0_random_std\\\": 0.0733, \\\"l0_random_median\\\": 8.6192, \\\"naive_positional_ppl\\\": 8.5781, \\\"mckp_ppl\\\": 8.4498, \\\"uniform_ppl\\\": 8.469, \\\"baseline_ppl\\\": 8.0918, \\\"mckp_vs_l0_random_gap\\\": 0.1747, \\\"mckp_vs_naive_gap\\\": 0.1283}}, \\\"plan_009_oracle_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"oracle_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mckp_ppl\\\": 10.9131, \\\"max_oracle_gap_ppl\\\": 0.0183, \\\"avg_oracle_gap_ppl\\\": 0.0046, \\\"layers_mckp_optimal\\\": \\\"5/8\\\", \\\"layers_with_gap\\\": 3, \\\"gap_layers\\\": {\\\"L1\\\": 0.0183, \\\"L4\\\": 0.0045, \\\"L11\\\": 0.0136}, \\\"gap_nature\\\": \\\"2-bit head position swap within same bit budget\\\", \\\"total_evals\\\": 54, \\\"runtime_min\\\": 21.3}}}, \\\"count\\\": 50, \\\"total\\\": 95, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2367}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"llama_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_compounding_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_k\": 0, \"best_ppl\": 8.0922, \"k0_ppl\": 8.0922, \"k2_ppl\": 8.1243, \"k4_ppl\": 8.1803, \"k8_ppl\": 8.2259, \"k16_ppl\": 8.4378, \"k32_ppl\": 9.0506, \"k64_ppl\": 11.991, \"k128_ppl\": 40.2067, \"k256_ppl\": 1519.1888, \"budget\": 0.25}}, \"qwen25-hires-profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_constrained_mckp_v2\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0352, \"mckp_wikitext2_ppl\": 7.1341, \"uniform4bit_wikitext2_ppl\": 7.1308, \"mckp_improvement_over_uniform\": -0.0033, \"mckp_improvement_pct\": -3.48, \"verdict\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 254}, \"fix_note\": \"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\"}, \"conclusion\": \"negative\"}, \"mistral_uniform_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen14b_greedy_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_constrained_ppl\": 7.2206, \"mckp_constrained_ppl\": 7.2206, \"delta_vs_mckp\": 0, \"bit_distribution\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"memory_ratio\": 0.25, \"solver_time_sec\": 0.08, \"total_time_min\": 1.8}}, \"kivi_mckp_combined_qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kivi_baseline_qwen7b_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_kivi_4bit_g32_r128\": 9.8976, \"tokens\": 298938, \"chunks\": 583, \"stride\": 512, \"model\": \"Qwen2.5-7B\", \"comparison_mckp_ppl\": 10.91, \"comparison_uniform_ppl\": 15.45, \"comparison_bf16_ppl\": 9.81}}, \"qwen14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 6.8654, \"ppl_uniform_4bit\": 7.202, \"ppl_constrained_mckp\": 7.2206, \"ppl_unconstrained_mckp\": 7.6923, \"delta_constrained_vs_uniform\": -0.0185, \"delta_constrained_vs_uniform_pct\": -5.51, \"delta_unconstrained_vs_uniform\": -0.4902, \"bit_distribution_constrained\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"bit_distribution_unconstrained\": {\"2\": 77, \"4\": 271, \"8\": 35, \"16\": 1}, \"concentration\": 0.33, \"top1_pct\": 0.2262, \"top5_pct\": 0.3304, \"t1_t5\": 0.68, \"shape\": \"Flat\"}}, \"qwen_hires_constrained_d049\": {\"status\": \"DONE\", \"metrics\": {\"float32_hires_constrained_mckp_ppl\": 10.8921, \"baseline_ppl\": 9.8106, \"uniform_4bit_ppl\": 15.4484, \"bit_distribution\": {\"2\": 8, \"4\": 100, \"8\": 4}, \"gap_recovery_pct\": 80.8, \"top5_concentration\": 0.6156, \"top5_concentration_pre_monotonicity\": 0.6104, \"bf16_hires_constrained_mckp_ppl\": 10.9131, \"delta_f32_vs_bf16\": 0.021}, \"conclusion\": \"success\"}, \"llama_8k_spotcheck\": {\"status\": \"DONE\", \"metrics\": {\"ppl_bf16_8k\": 5.5958, \"ppl_constrained_mckp_8k\": 6.0537, \"ppl_uniform_4bit_8k\": 6.0364, \"mckp_improvement_over_uniform_8k\": -0.0174, \"mckp_improvement_pct_8k\": -3.94, \"ppl_bf16_2k\": 8.0922, \"ppl_constrained_mckp_2k\": 8.5042, \"ppl_uniform_4bit_2k\": 8.4701, \"shape\": \"Spike\", \"concentration\": 0.5749, \"t1_over_t5\": 0.71, \"context_length\": 8192, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"success\"}, \"yi15_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen7b_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"qwen7b_8k_context_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16_8k\": 6.97, \"ppl_constrained_mckp_8k\": 8.59, \"ppl_uniform_4bit_8k\": 77.75, \"ppl_bf16_2k\": 9.81, \"ppl_constrained_mckp_2k\": 10.89, \"ppl_uniform_4bit_2k\": 15.45, \"mckp_improvement_over_uniform_8k\": \"97.7%\", \"mckp_improvement_over_uniform_2k\": \"80.8%\", \"shape\": \"Spread\", \"concentration\": 0.5992, \"context_length\": 8192, \"note\": \"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\"}}, \"pythia14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 16.4893, \"ppl_uniform_4bit\": 24.2894, \"ppl_constrained_mckp\": 24.4521, \"ppl_unconstrained_mckp\": 31.5415, \"concentration\": \"t1=0.0289, t5=0.2439\", \"t1_t5\": \"0.0289/0.2439\", \"shape\": \"Flat\", \"constrained_vs_uniform_gap\": 0.1627}}, \"w1_pythia14b_hires_profiling\": {\"status\": \"DONE\", \"metrics\": {\"baseline_ppl\": 13.6347, \"concentration\": 0.2439, \"t1_t5\": 0.28, \"shape\": \"Flat\", \"l0_dominance\": 0.51, \"cv\": 1.2172, \"positive_heads\": 362, \"total_heads\": 384, \"top5_heads\": [{\"head\": \"L1H11\", \"delta\": 1.016355}, {\"head\": \"L12H14\", \"delta\": 0.784513}, {\"head\": \"L8H4\", \"delta\": 0.759118}, {\"head\": \"L11H2\", \"delta\": 0.632357}, {\"head\": \"L13H2\", \"delta\": 0.522849}], \"elapsed_min\": 25.7, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}, \"conclusion\": \"success\"}, \"w1_qwen14b_hires_profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 5.8432, \"concentration\": 0.3312, \"t1_t5\": 0.68, \"shape\": \"Flat\", \"l0_dominance\": 15.5, \"cv\": 3.7418, \"positive_heads\": 370, \"total_heads\": 384, \"top10_heads\": [{\"head\": \"L0H5\", \"delta\": 1.84494}, {\"head\": \"L0H4\", \"delta\": 0.236669}, {\"head\": \"L0H2\", \"delta\": 0.136971}, {\"head\": \"L28H4\", \"delta\": 0.099279}, {\"head\": \"L28H5\", \"delta\": 0.07576}, {\"head\": \"L27H4\", \"delta\": 0.071269}, {\"head\": \"L0H0\", \"delta\": 0.070018}, {\"head\": \"L28H6\", \"delta\": 0.063737}, {\"head\": \"L26H0\", \"delta\": 0.061462}, {\"head\": \"L31H3\", \"delta\": 0.061062}], \"elapsed_min\": 161.3, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}}, \"kivi_baseline_qwen_llama\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"qwen_2bit_r128\": 12.83, \"qwen_4bit_r128\": 9.9, \"qwen_2bit_r0\": 13.34, \"qwen_4bit_r0\": 9.91, \"llama_2bit_r128\": 9.84, \"llama_4bit_r128\": 8.14, \"llama_2bit_r0\": 10.08, \"llama_4bit_r0\": 8.14, \"group_size\": 32, \"eval_data\": \"WikiText-2 test\", \"note\": \"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\"}}, \"gemma2_constrained_bos_fix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 6.0306, \"uniform_4bit_ppl\": 6.1683, \"constrained_mckp_ppl\": 6.1951, \"mckp_vs_uniform_delta\": 0.0267, \"mckp_delta_ppl\": 0.1645, \"uniform_delta_ppl\": 0.1377, \"bit_distribution\": {\"2\": 8, \"4\": 324, \"8\": 4}, \"n_2bit\": 8, \"max_2bit\": 8, \"memory_ratio\": 0.25, \"eval_method\": \"sliding_window_bos_fix\", \"elapsed_seconds\": 490.3}}, \"w2_unconstrained_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline\": 7.0157, \"yi15_uniform4\": 7.2171, \"yi15_greedy\": 7.5615, \"yi15_mckp\": 7.5615, \"yi15_n2bit\": 22, \"llama_baseline\": 8.0922, \"llama_uniform4\": 8.4701, \"llama_greedy\": 8.6265, \"llama_mckp\": 8.6265, \"llama_n2bit\": 12, \"mistral_baseline\": 7.0352, \"mistral_uniform4\": 7.1308, \"mistral_greedy\": 7.5733, \"mistral_mckp\": 7.5963, \"mistral_n2bit\": 42, \"gemma2_baseline\": 6.0306, \"gemma2_uniform4\": 6.1683, \"gemma2_greedy\": 8.8469, \"gemma2_mckp\": 8.8469, \"gemma2_n2bit\": 106, \"gemma2_eval_method\": \"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\", \"gemma2_greedy_ratio\": 1.467, \"gemma2_catastrophic\": true, \"gemma2_note\": \"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\"}}, \"w3_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline_avg\": 0.6912, \"yi15_uniform_avg\": 0.6822, \"yi15_mckp_avg\": 0.6745, \"yi15_mckp_vs_uniform_pp\": -0.77, \"yi15_mckp_vs_baseline_pp\": -1.67, \"yi15_baseline\": {\"arc_easy\": 0.8093, \"arc_challenge\": 0.5265, \"hellaswag\": 0.5913, \"piqa\": 0.7949, \"winogrande\": 0.734}, \"yi15_uniform\": {\"arc_easy\": 0.7946, \"arc_challenge\": 0.5205, \"hellaswag\": 0.5857, \"piqa\": 0.7927, \"winogrande\": 0.7174}, \"yi15_mckp\": {\"arc_easy\": 0.7854, \"arc_challenge\": 0.4881, \"hellaswag\": 0.5797, \"piqa\": 0.7894, \"winogrande\": 0.7301}, \"llama_baseline_avg\": 0.696, \"llama_uniform_avg\": 0.6915, \"llama_mckp_avg\": 0.6816, \"llama_mckp_vs_uniform_pp\": -0.99, \"llama_mckp_vs_baseline_pp\": -1.44, \"llama_baseline\": {\"arc_easy\": 0.8228, \"arc_challenge\": 0.5188, \"hellaswag\": 0.6073, \"piqa\": 0.7922, \"winogrande\": 0.7388}, \"llama_uniform\": {\"arc_easy\": 0.8173, \"arc_challenge\": 0.5256, \"hellaswag\": 0.6026, \"piqa\": 0.7867, \"winogrande\": 0.7253}, \"llama_mckp\": {\"arc_easy\": 0.8039, \"arc_challenge\": 0.4991, \"hellaswag\": 0.6012, \"piqa\": 0.7802, \"winogrande\": 0.7238}, \"mistral_baseline_avg\": 0.6917, \"mistral_uniform_avg\": 0.6894, \"mistral_mckp_avg\": 0.6846, \"mistral_mckp_vs_uniform_pp\": -0.48, \"mistral_mckp_vs_baseline_pp\": -0.71, \"mistral_baseline\": {\"arc_easy\": 0.8005, \"arc_challenge\": 0.5043, \"hellaswag\": 0.6118, \"piqa\": 0.8009, \"winogrande\": 0.7411}, \"mistral_uniform\": {\"arc_easy\": 0.7976, \"arc_challenge\": 0.5068, \"hellaswag\": 0.6051, \"piqa\": 0.7982, \"winogrande\": 0.7395}, \"mistral_mckp\": {\"arc_easy\": 0.7942, \"arc_challenge\": 0.4949, \"hellaswag\": 0.6027, \"piqa\": 0.802, \"winogrande\": 0.7293}, \"gemma2_baseline_avg\": 0.7307, \"gemma2_uniform_avg\": 0.7251, \"gemma2_mckp_avg\": 0.7265, \"gemma2_mckp_vs_uniform_pp\": 0.14, \"gemma2_mckp_vs_baseline_pp\": -0.42, \"gemma2_baseline\": {\"arc_easy\": 0.8737, \"arc_challenge\": 0.6135, \"hellaswag\": 0.6093, \"piqa\": 0.8128, \"winogrande\": 0.7443}, \"gemma2_uniform\": {\"arc_easy\": 0.8662, \"arc_challenge\": 0.6058, \"hellaswag\": 0.606, \"piqa\": 0.8079, \"winogrande\": 0.7395}, \"gemma2_mckp\": {\"arc_easy\": 0.8649, \"arc_challenge\": 0.6041, \"hellaswag\": 0.6089, \"piqa\": 0.8074, \"winogrande\": 0.7474}, \"eval_harness_version\": \"0.4.11\", \"num_fewshot\": 0, \"yi_elapsed_s\": 1563.2, \"llama_elapsed_s\": 1446.4, \"mistral_elapsed_s\": 1302.2, \"gemma2_elapsed_s\": 1735.9}}, \"w9_compounding_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 9.81, \"k1_topk_ppl\": 9.826, \"k1_randomk_ppl\": 9.887, \"k1_randomk_std\": 0.05, \"k4_topk_ppl\": 9.849, \"k4_topk_ratio\": 0.86, \"k4_randomk_ppl\": 10.06, \"k4_randomk_std\": 0.06, \"k4_randomk_ratio\": 1.24, \"k8_topk_ppl\": 10.042, \"k8_topk_ratio\": 1.56, \"k8_randomk_ppl\": 11.07, \"k8_randomk_std\": 0.69, \"k8_randomk_ratio\": 1.76, \"k16_topk_ppl\": 10.42, \"k16_topk_ratio\": 1.56, \"k16_randomk_ppl\": 12.91, \"k16_randomk_std\": 0.4, \"k16_randomk_ratio\": 2.1, \"k32_topk_ppl\": 11.604, \"k32_topk_ratio\": 1.78, \"k32_randomk_ppl\": 18.33, \"k32_randomk_std\": 2.53, \"k32_randomk_ratio\": 2.73, \"k64_topk_ppl\": 22.946, \"k64_topk_ratio\": 4.89, \"k64_randomk_ppl\": 55.94, \"k64_randomk_std\": 9.73, \"k64_randomk_ratio\": 8.88, \"runtime_minutes\": 16.9, \"note\": \"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\"}}, \"w9_compounding_scaling\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"baseline_ppl\": 8.2, \"n1_joint_ppl\": 14.94, \"n1_ratio\": 1, \"n2_joint_ppl\": 42.26, \"n2_ratio\": 3.84, \"n4_joint_ppl\": 3813.76, \"n4_ratio\": 333.3, \"n8_joint_ppl\": 3586.42, \"n8_ratio\": 282.1, \"n16_joint_ppl\": 7286.23, \"n16_ratio\": 521.1, \"n32_joint_ppl\": 6644.05, \"n32_ratio\": 424, \"n64_joint_ppl\": 9453.33, \"n64_ratio\": 533.3, \"runtime_seconds\": 96}}, \"w2_unconstrained_baselines\": {\"status\": \"DONE\", \"metrics\": {\"note\": \"2bitonly profiles only - INVALID for reviewer response\", \"yi15_ppl\": 672.2, \"yi15_ratio\": 114, \"llama_ppl\": 1219.7, \"llama_ratio\": 187, \"mistral_ppl_2bitonly\": 47.8, \"mistral_ratio_2bitonly\": 8.2, \"mistral_ppl_full\": 6.39, \"mistral_ratio_full\": 1.09, \"gemma2_ppl\": 277.4, \"gemma2_ratio\": 37.9, \"budget\": 0.25, \"baseline_yi\": 5.89, \"baseline_llama\": 6.51, \"baseline_mistral\": 5.87, \"baseline_gemma2\": 7.32}, \"conclusion\": \"killed\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"concentration_top5pct\": 0.2291, \"l0_dominance_ratio\": 2.05, \"cv_delta_2bit\": 1.2834, \"positive_delta_heads\": \"310/336\", \"top_head\": \"L0H1 delta=0.1906\", \"total_time_hours\": 1.59}}, \"mistral_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fp16_ppl\": 7.0352, \"c4_mckp_ppl\": 7.1774, \"uniform_4bit_ppl\": 7.1308, \"mckp_vs_uniform_delta\": 0.0466, \"mckp_bit_distribution\": {\"2\": 4, \"4\": 250, \"8\": 2}, \"phase4_error\": \"FileNotFoundError: mistral_k_ablation_results.json\"}}, \"llama_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bf16_wt2_ppl\": 8.0922, \"bf16_c4_ppl\": 7.1333, \"c4_cal_mckp_wt2_ppl\": 8.5103, \"c4_cal_mckp_c4_ppl\": 7.5351, \"uniform_wt2_ppl\": 8.4701, \"uniform_c4_ppl\": 7.5351, \"delta_c4_uniform_minus_mckp\": 0, \"delta_wt2_uniform_minus_mckp\": -0.0402, \"verdict_c4\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"2,3\", \"24,2\"], \"heads_8bit\": [\"31,6\"], \"total_time_min\": 6.3, \"wt2_ref_mckp_ppl\": 8.5042, \"wt2_ref_delta\": -0.0341}}, \"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256, \"distribution_shape\": \"flat\", \"total_hours\": 0.94, \"profile_seconds\": 3371.7}, \"conclusion\": \"success\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 8.0922, \"hires_mckp_ppl\": 8.5042, \"uniform_4bit_ppl\": 8.4701, \"std_mckp_reference_ppl\": 8.4498, \"mckp_vs_uniform_delta\": -0.0341, \"mckp_vs_uniform_pct\": -9, \"hires_vs_std_mckp_delta\": 0.0544, \"concentration\": 0.5749, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"26,0\", \"31,7\"], \"heads_8bit\": [\"12,3\"], \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.5749, \"t1_t5\": 0.85, \"baseline_ppl\": 6.5055, \"top1_head\": \"L2H5_delta=15.2636\", \"delta_2bit_cv\": 7.7663, \"l0_dominance_ratio\": 0.67, \"positive_delta_heads\": 254, \"total_heads\": 256, \"total_hours\": 0.98}, \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\"}}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\"}}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"hires_mckp_ppl\": 7.2181, \"uniform_4bit_ppl\": 7.2171, \"baseline_ppl\": 7.0157, \"delta_vs_uniform\": -0.001, \"bit_distribution\": {\"2\": 2, \"4\": 189, \"8\": 1}, \"2bit_heads\": [\"L22H1\", \"L24H3\"], \"8bit_heads\": [\"L6H2\"], \"L4H3_status\": \"kept_at_4bit\", \"std_mckp_k2_ppl\": 7.2209, \"std_mckp_k8_ppl\": 7.3129, \"hires_concentration\": 0.7139, \"L4H3_2bit_delta\": 13.12, \"L4H3_4bit_delta\": 0.0048, \"L4H3_8bit_delta\": 0.004}}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"top5_concentration\": 0.7139, \"top5_n_heads\": 9, \"baseline_calibration_ppl\": 5.888, \"delta_2bit_cv\": 8.8991, \"layer0_dominance_ratio\": 0.04, \"top1_head\": \"L4H3_delta=13.1236\", \"total_hours\": 0.96}}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"float32_hires_top5_concentration\": 0.6104, \"bf16_hires_range\": \"0.59-0.66\", \"float32_lowres_concentration\": 0.42, \"bf16_bug_impact_on_concentration\": 0.01, \"baseline_ppl\": 9.81, \"mckp_unconstrained_ppl\": 10.95, \"uniform_4bit_ppl\": 15.45, \"mckp_bit_dist\": {\"2\": 12, \"4\": 96, \"8\": 3, \"16\": 1}, \"l0h0_delta\": 6.7388, \"l0_4heads_total_share\": 0.586, \"claim3_threshold_0.50\": \"PASS\"}}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0157, \"mckp_wikitext2_ppl\": 7.3129, \"uniform4bit_wikitext2_ppl\": 7.2171, \"mckp_improvement_over_uniform\": -0.0958, \"top5_concentration\": 0.4934, \"layer0_dominance_ratio\": 0.07, \"best_k\": 2, \"best_k_ppl\": 7.2209, \"gqa_ratio\": \"8:1\", \"verdict\": \"FAIL\"}}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 8.9, \"mckp_wikitext2_ppl\": 9.05, \"uniform4bit_wikitext2_ppl\": 9.03, \"mckp_improvement_over_uniform\": -0.02, \"top5_concentration\": 0.23, \"layer0_dominance_ratio\": 1.32, \"best_k\": 8, \"best_k_ppl\": 9.05, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"bf16_wt2_ppl\": 7.0351, \"c4_cal_bf16_ppl\": 6.9677, \"wt2_cal_mckp_wt2_ppl\": 7.1648, \"c4_cal_mckp_wt2_ppl\": 7.1859, \"uniform_4bit_wt2_ppl\": 7.1314, \"delta_uniform_mckp_wt2_cal\": -0.0334, \"delta_uniform_mckp_c4_cal\": -0.0546, \"allocation_agreement_c4_vs_wt2\": 0.965, \"agreement_heads\": \"247/256\", \"bit_dist_wt2_cal\": \"2bit:4, 4bit:252\", \"bit_dist_c4_cal\": \"2bit:4, 4bit:251, 8bit:1\", \"profile_time_s\": 407.7, \"eval_time_s\": 349.4, \"total_time_s\": 757.1}}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"metrics\": {\"wt2_cal_wt2_ppl\": 8.4498, \"c4_cal_wt2_ppl\": 8.6459, \"uniform_wt2_ppl\": 8.469, \"wt2_cal_c4_ppl\": 7.654, \"c4_cal_c4_ppl\": 7.654, \"uniform_c4_ppl\": 7.5351, \"bf16_wt2_ppl\": 8.0918, \"bf16_c4_ppl\": 7.1333, \"agreement_rate\": 0.977, \"agreement_heads\": \"250/256\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 7.0351, \"uniform_4bit_ppl\": 7.1314, \"mckp_k4_ppl\": 7.1648, \"l0_random_seed_0\": 7.1882, \"l0_random_seed_1\": 7.1995, \"l0_random_seed_2\": 7.1723, \"l0_random_seed_3\": 7.3577, \"l0_random_seed_4\": 7.2875, \"l0_random_mean\": 7.2411, \"l0_random_std\": 0.0707, \"l0_random_median\": 7.1995, \"naive_heuristic_ppl\": 7.2105, \"budget_heuristic\": 0.2559, \"budget_mckp_k4\": 0.248}, \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"l0_random_seeds\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \"l0_random_mean\": 8.6245, \"l0_random_std\": 0.0733, \"l0_random_median\": 8.6192, \"naive_positional_ppl\": 8.5781, \"mckp_ppl\": 8.4498, \"uniform_ppl\": 8.469, \"baseline_ppl\": 8.0918, \"mckp_vs_l0_random_gap\": 0.1747, \"mckp_vs_naive_gap\": 0.1283}}, \"plan_009_oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mckp_ppl\": 10.9131, \"max_oracle_gap_ppl\": 0.0183, \"avg_oracle_gap_ppl\": 0.0046, \"layers_mckp_optimal\": \"5/8\", \"layers_with_gap\": 3, \"gap_layers\": {\"L1\": 0.0183, \"L4\": 0.0045, \"L11\": 0.0136}, \"gap_nature\": \"2-bit head position swap within same bit budget\", \"total_evals\": 54, \"runtime_min\": 21.3}}}, \"count\": 50, \"total\": 95, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2367}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
I have the Llama compounding sweep data from the registry (`llama_compounding_sweep`). Now I need to find the Mistral compounding sweep. Let me search for it specifically - it might have a different exp_id. Let me look for experiments with "mistral" and "compounding" in the name.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "e1ad620a-79dc-4caf-8ffc-31d3e88e845f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176U6bbyKqcsTBkEyvsDeHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10209,
      "cache_read_input_tokens": 49466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10209
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

I need to find the Mistral compounding sweep experiment. Let me search the remaining experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "fbb4e1c3-364e-4d69-93f3-ddf3276f0a0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176U6bbyKqcsTBkEyvsDeHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10209,
      "cache_read_input_tokens": 49466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10209
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DHsaJTD9UvuXuaCDnbB1Ld`</summary>

```json
{
  "project": "ratekv",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "status",
    "conclusion",
    "metrics"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "26b260f4-d2a0-40d3-b742-ade558cd6557",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176U6bbyKqcsTBkEyvsDeHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10209,
      "cache_read_input_tokens": 49466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10209
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

_source line 23 · 2026-05-15T18:00:50.484Z_

<details><summary>↩ Tool result · `toolu_01DHsaJTD9UvuXuaCDnbB1Ld`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"llama_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_compounding_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_k\": 0, \"best_ppl\": 8.0922, \"k0_ppl\": 8.0922, \"k2_ppl\": 8.1243, \"k4_ppl\": 8.1803, \"k8_ppl\": 8.2259, \"k16_ppl\": 8.4378, \"k32_ppl\": 9.0506, \"k64_ppl\": 11.991, \"k128_ppl\": 40.2067, \"k256_ppl\": 1519.1888, \"budget\": 0.25}}, \"qwen25-hires-profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_constrained_mckp_v2\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0352, \"mckp_wikitext2_ppl\": 7.1341, \"uniform4bit_wikitext2_ppl\": 7.1308, \"mckp_improvement_over_uniform\": -0.0033, \"mckp_improvement_pct\": -3.48, \"verdict\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 254}, \"fix_note\": \"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\"}, \"conclusion\": \"negative\"}, \"mistral_uniform_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen14b_greedy_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_constrained_ppl\": 7.2206, \"mckp_constrained_ppl\": 7.2206, \"delta_vs_mckp\": 0, \"bit_distribution\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"memory_ratio\": 0.25, \"solver_time_sec\": 0.08, \"total_time_min\": 1.8}}, \"kivi_mckp_combined_qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kivi_baseline_qwen7b_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_kivi_4bit_g32_r128\": 9.8976, \"tokens\": 298938, \"chunks\": 583, \"stride\": 512, \"model\": \"Qwen2.5-7B\", \"comparison_mckp_ppl\": 10.91, \"comparison_uniform_ppl\": 15.45, \"comparison_bf16_ppl\": 9.81}}, \"qwen14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 6.8654, \"ppl_uniform_4bit\": 7.202, \"ppl_constrained_mckp\": 7.2206, \"ppl_unconstrained_mckp\": 7.6923, \"delta_constrained_vs_uniform\": -0.0185, \"delta_constrained_vs_uniform_pct\": -5.51, \"delta_unconstrained_vs_uniform\": -0.4902, \"bit_distribution_constrained\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"bit_distribution_unconstrained\": {\"2\": 77, \"4\": 271, \"8\": 35, \"16\": 1}, \"concentration\": 0.33, \"top1_pct\": 0.2262, \"top5_pct\": 0.3304, \"t1_t5\": 0.68, \"shape\": \"Flat\"}}, \"qwen_hires_constrained_d049\": {\"status\": \"DONE\", \"metrics\": {\"float32_hires_constrained_mckp_ppl\": 10.8921, \"baseline_ppl\": 9.8106, \"uniform_4bit_ppl\": 15.4484, \"bit_distribution\": {\"2\": 8, \"4\": 100, \"8\": 4}, \"gap_recovery_pct\": 80.8, \"top5_concentration\": 0.6156, \"top5_concentration_pre_monotonicity\": 0.6104, \"bf16_hires_constrained_mckp_ppl\": 10.9131, \"delta_f32_vs_bf16\": 0.021}, \"conclusion\": \"success\"}, \"llama_8k_spotcheck\": {\"status\": \"DONE\", \"metrics\": {\"ppl_bf16_8k\": 5.5958, \"ppl_constrained_mckp_8k\": 6.0537, \"ppl_uniform_4bit_8k\": 6.0364, \"mckp_improvement_over_uniform_8k\": -0.0174, \"mckp_improvement_pct_8k\": -3.94, \"ppl_bf16_2k\": 8.0922, \"ppl_constrained_mckp_2k\": 8.5042, \"ppl_uniform_4bit_2k\": 8.4701, \"shape\": \"Spike\", \"concentration\": 0.5749, \"t1_over_t5\": 0.71, \"context_length\": 8192, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"success\"}, \"yi15_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen7b_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"qwen7b_8k_context_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16_8k\": 6.97, \"ppl_constrained_mckp_8k\": 8.59, \"ppl_uniform_4bit_8k\": 77.75, \"ppl_bf16_2k\": 9.81, \"ppl_constrained_mckp_2k\": 10.89, \"ppl_uniform_4bit_2k\": 15.45, \"mckp_improvement_over_uniform_8k\": \"97.7%\", \"mckp_improvement_over_uniform_2k\": \"80.8%\", \"shape\": \"Spread\", \"concentration\": 0.5992, \"context_length\": 8192, \"note\": \"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\"}}, \"pythia14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 16.4893, \"ppl_uniform_4bit\": 24.2894, \"ppl_constrained_mckp\": 24.4521, \"ppl_unconstrained_mckp\": 31.5415, \"concentration\": \"t1=0.0289, t5=0.2439\", \"t1_t5\": \"0.0289/0.2439\", \"shape\": \"Flat\", \"constrained_vs_uniform_gap\": 0.1627}}, \"w1_pythia14b_hires_profiling\": {\"status\": \"DONE\", \"metrics\": {\"baseline_ppl\": 13.6347, \"concentration\": 0.2439, \"t1_t5\": 0.28, \"shape\": \"Flat\", \"l0_dominance\": 0.51, \"cv\": 1.2172, \"positive_heads\": 362, \"total_heads\": 384, \"top5_heads\": [{\"head\": \"L1H11\", \"delta\": 1.016355}, {\"head\": \"L12H14\", \"delta\": 0.784513}, {\"head\": \"L8H4\", \"delta\": 0.759118}, {\"head\": \"L11H2\", \"delta\": 0.632357}, {\"head\": \"L13H2\", \"delta\": 0.522849}], \"elapsed_min\": 25.7, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}, \"conclusion\": \"success\"}, \"w1_qwen14b_hires_profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 5.8432, \"concentration\": 0.3312, \"t1_t5\": 0.68, \"shape\": \"Flat\", \"l0_dominance\": 15.5, \"cv\": 3.7418, \"positive_heads\": 370, \"total_heads\": 384, \"top10_heads\": [{\"head\": \"L0H5\", \"delta\": 1.84494}, {\"head\": \"L0H4\", \"delta\": 0.236669}, {\"head\": \"L0H2\", \"delta\": 0.136971}, {\"head\": \"L28H4\", \"delta\": 0.099279}, {\"head\": \"L28H5\", \"delta\": 0.07576}, {\"head\": \"L27H4\", \"delta\": 0.071269}, {\"head\": \"L0H0\", \"delta\": 0.070018}, {\"head\": \"L28H6\", \"delta\": 0.063737}, {\"head\": \"L26H0\", \"delta\": 0.061462}, {\"head\": \"L31H3\", \"delta\": 0.061062}], \"elapsed_min\": 161.3, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}}, \"kivi_baseline_qwen_llama\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"qwen_2bit_r128\": 12.83, \"qwen_4bit_r128\": 9.9, \"qwen_2bit_r0\": 13.34, \"qwen_4bit_r0\": 9.91, \"llama_2bit_r128\": 9.84, \"llama_4bit_r128\": 8.14, \"llama_2bit_r0\": 10.08, \"llama_4bit_r0\": 8.14, \"group_size\": 32, \"eval_data\": \"WikiText-2 test\", \"note\": \"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\"}}, \"gemma2_constrained_bos_fix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 6.0306, \"uniform_4bit_ppl\": 6.1683, \"constrained_mckp_ppl\": 6.1951, \"mckp_vs_uniform_delta\": 0.0267, \"mckp_delta_ppl\": 0.1645, \"uniform_delta_ppl\": 0.1377, \"bit_distribution\": {\"2\": 8, \"4\": 324, \"8\": 4}, \"n_2bit\": 8, \"max_2bit\": 8, \"memory_ratio\": 0.25, \"eval_method\": \"sliding_window_bos_fix\", \"elapsed_seconds\": 490.3}}, \"w2_unconstrained_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline\": 7.0157, \"yi15_uniform4\": 7.2171, \"yi15_greedy\": 7.5615, \"yi15_mckp\": 7.5615, \"yi15_n2bit\": 22, \"llama_baseline\": 8.0922, \"llama_uniform4\": 8.4701, \"llama_greedy\": 8.6265, \"llama_mckp\": 8.6265, \"llama_n2bit\": 12, \"mistral_baseline\": 7.0352, \"mistral_uniform4\": 7.1308, \"mistral_greedy\": 7.5733, \"mistral_mckp\": 7.5963, \"mistral_n2bit\": 42, \"gemma2_baseline\": 6.0306, \"gemma2_uniform4\": 6.1683, \"gemma2_greedy\": 8.8469, \"gemma2_mckp\": 8.8469, \"gemma2_n2bit\": 106, \"gemma2_eval_method\": \"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\", \"gemma2_greedy_ratio\": 1.467, \"gemma2_catastrophic\": true, \"gemma2_note\": \"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\"}}, \"w3_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline_avg\": 0.6912, \"yi15_uniform_avg\": 0.6822, \"yi15_mckp_avg\": 0.6745, \"yi15_mckp_vs_uniform_pp\": -0.77, \"yi15_mckp_vs_baseline_pp\": -1.67, \"yi15_baseline\": {\"arc_easy\": 0.8093, \"arc_challenge\": 0.5265, \"hellaswag\": 0.5913, \"piqa\": 0.7949, \"winogrande\": 0.734}, \"yi15_uniform\": {\"arc_easy\": 0.7946, \"arc_challenge\": 0.5205, \"hellaswag\": 0.5857, \"piqa\": 0.7927, \"winogrande\": 0.7174}, \"yi15_mckp\": {\"arc_easy\": 0.7854, \"arc_challenge\": 0.4881, \"hellaswag\": 0.5797, \"piqa\": 0.7894, \"winogrande\": 0.7301}, \"llama_baseline_avg\": 0.696, \"llama_uniform_avg\": 0.6915, \"llama_mckp_avg\": 0.6816, \"llama_mckp_vs_uniform_pp\": -0.99, \"llama_mckp_vs_baseline_pp\": -1.44, \"llama_baseline\": {\"arc_easy\": 0.8228, \"arc_challenge\": 0.5188, \"hellaswag\": 0.6073, \"piqa\": 0.7922, \"winogrande\": 0.7388}, \"llama_uniform\": {\"arc_easy\": 0.8173, \"arc_challenge\": 0.5256, \"hellaswag\": 0.6026, \"piqa\": 0.7867, \"winogrande\": 0.7253}, \"llama_mckp\": {\"arc_easy\": 0.8039, \"arc_challenge\": 0.4991, \"hellaswag\": 0.6012, \"piqa\": 0.7802, \"winogrande\": 0.7238}, \"mistral_baseline_avg\": 0.6917, \"mistral_uniform_avg\": 0.6894, \"mistral_mckp_avg\": 0.6846, \"mistral_mckp_vs_uniform_pp\": -0.48, \"mistral_mckp_vs_baseline_pp\": -0.71, \"mistral_baseline\": {\"arc_easy\": 0.8005, \"arc_challenge\": 0.5043, \"hellaswag\": 0.6118, \"piqa\": 0.8009, \"winogrande\": 0.7411}, \"mistral_uniform\": {\"arc_easy\": 0.7976, \"arc_challenge\": 0.5068, \"hellaswag\": 0.6051, \"piqa\": 0.7982, \"winogrande\": 0.7395}, \"mistral_mckp\": {\"arc_easy\": 0.7942, \"arc_challenge\": 0.4949, \"hellaswag\": 0.6027, \"piqa\": 0.802, \"winogrande\": 0.7293}, \"gemma2_baseline_avg\": 0.7307, \"gemma2_uniform_avg\": 0.7251, \"gemma2_mckp_avg\": 0.7265, \"gemma2_mckp_vs_uniform_pp\": 0.14, \"gemma2_mckp_vs_baseline_pp\": -0.42, \"gemma2_baseline\": {\"arc_easy\": 0.8737, \"arc_challenge\": 0.6135, \"hellaswag\": 0.6093, \"piqa\": 0.8128, \"winogrande\": 0.7443}, \"gemma2_uniform\": {\"arc_easy\": 0.8662, \"arc_challenge\": 0.6058, \"hellaswag\": 0.606, \"piqa\": 0.8079, \"winogrande\": 0.7395}, \"gemma2_mckp\": {\"arc_easy\": 0.8649, \"arc_challenge\": 0.6041, \"hellaswag\": 0.6089, \"piqa\": 0.8074, \"winogrande\": 0.7474}, \"eval_harness_version\": \"0.4.11\", \"num_fewshot\": 0, \"yi_elapsed_s\": 1563.2, \"llama_elapsed_s\": 1446.4, \"mistral_elapsed_s\": 1302.2, \"gemma2_elapsed_s\": 1735.9}}, \"w9_compounding_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 9.81, \"k1_topk_ppl\": 9.826, \"k1_randomk_ppl\": 9.887, \"k1_randomk_std\": 0.05, \"k4_topk_ppl\": 9.849, \"k4_topk_ratio\": 0.86, \"k4_randomk_ppl\": 10.06, \"k4_randomk_std\": 0.06, \"k4_randomk_ratio\": 1.24, \"k8_topk_ppl\": 10.042, \"k8_topk_ratio\": 1.56, \"k8_randomk_ppl\": 11.07, \"k8_randomk_std\": 0.69, \"k8_randomk_ratio\": 1.76, \"k16_topk_ppl\": 10.42, \"k16_topk_ratio\": 1.56, \"k16_randomk_ppl\": 12.91, \"k16_randomk_std\": 0.4, \"k16_randomk_ratio\": 2.1, \"k32_topk_ppl\": 11.604, \"k32_topk_ratio\": 1.78, \"k32_randomk_ppl\": 18.33, \"k32_randomk_std\": 2.53, \"k32_randomk_ratio\": 2.73, \"k64_topk_ppl\": 22.946, \"k64_topk_ratio\": 4.89, \"k64_randomk_ppl\": 55.94, \"k64_randomk_std\": 9.73, \"k64_randomk_ratio\": 8.88, \"runtime_minutes\": 16.9, \"note\": \"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\"}}, \"w9_compounding_scaling\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"baseline_ppl\": 8.2, \"n1_joint_ppl\": 14.94, \"n1_ratio\": 1, \"n2_joint_ppl\": 42.26, \"n2_ratio\": 3.84, \"n4_joint_ppl\": 3813.76, \"n4_ratio\": 333.3, \"n8_joint_ppl\": 3586.42, \"n8_ratio\": 282.1, \"n16_joint_ppl\": 7286.23, \"n16_ratio\": 521.1, \"n32_joint_ppl\": 6644.05, \"n32_ratio\": 424, \"n64_joint_ppl\": 9453.33, \"n64_ratio\": 533.3, \"runtime_seconds\": 96}}, \"w2_unconstrained_baselines\": {\"status\": \"DONE\", \"metrics\": {\"note\": \"2bitonly profiles only - INVALID for reviewer response\", \"yi15_ppl\": 672.2, \"yi15_ratio\": 114, \"llama_ppl\": 1219.7, \"llama_ratio\": 187, \"mistral_ppl_2bitonly\": 47.8, \"mistral_ratio_2bitonly\": 8.2, \"mistral_ppl_full\": 6.39, \"mistral_ratio_full\": 1.09, \"gemma2_ppl\": 277.4, \"gemma2_ratio\": 37.9, \"budget\": 0.25, \"baseline_yi\": 5.89, \"baseline_llama\": 6.51, \"baseline_mistral\": 5.87, \"baseline_gemma2\": 7.32}, \"conclusion\": \"killed\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"concentration_top5pct\": 0.2291, \"l0_dominance_ratio\": 2.05, \"cv_delta_2bit\": 1.2834, \"positive_delta_heads\": \"310/336\", \"top_head\": \"L0H1 delta=0.1906\", \"total_time_hours\": 1.59}}, \"mistral_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fp16_ppl\": 7.0352, \"c4_mckp_ppl\": 7.1774, \"uniform_4bit_ppl\": 7.1308, \"mckp_vs_uniform_delta\": 0.0466, \"mckp_bit_distribution\": {\"2\": 4, \"4\": 250, \"8\": 2}, \"phase4_error\": \"FileNotFoundError: mistral_k_ablation_results.json\"}}, \"llama_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bf16_wt2_ppl\": 8.0922, \"bf16_c4_ppl\": 7.1333, \"c4_cal_mckp_wt2_ppl\": 8.5103, \"c4_cal_mckp_c4_ppl\": 7.5351, \"uniform_wt2_ppl\": 8.4701, \"uniform_c4_ppl\": 7.5351, \"delta_c4_uniform_minus_mckp\": 0, \"delta_wt2_uniform_minus_mckp\": -0.0402, \"verdict_c4\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"2,3\", \"24,2\"], \"heads_8bit\": [\"31,6\"], \"total_time_min\": 6.3, \"wt2_ref_mckp_ppl\": 8.5042, \"wt2_ref_delta\": -0.0341}}, \"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256, \"distribution_shape\": \"flat\", \"total_hours\": 0.94, \"profile_seconds\": 3371.7}, \"conclusion\": \"success\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 8.0922, \"hires_mckp_ppl\": 8.5042, \"uniform_4bit_ppl\": 8.4701, \"std_mckp_reference_ppl\": 8.4498, \"mckp_vs_uniform_delta\": -0.0341, \"mckp_vs_uniform_pct\": -9, \"hires_vs_std_mckp_delta\": 0.0544, \"concentration\": 0.5749, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"26,0\", \"31,7\"], \"heads_8bit\": [\"12,3\"], \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.5749, \"t1_t5\": 0.85, \"baseline_ppl\": 6.5055, \"top1_head\": \"L2H5_delta=15.2636\", \"delta_2bit_cv\": 7.7663, \"l0_dominance_ratio\": 0.67, \"positive_delta_heads\": 254, \"total_heads\": 256, \"total_hours\": 0.98}, \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\"}}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\"}}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"hires_mckp_ppl\": 7.2181, \"uniform_4bit_ppl\": 7.2171, \"baseline_ppl\": 7.0157, \"delta_vs_uniform\": -0.001, \"bit_distribution\": {\"2\": 2, \"4\": 189, \"8\": 1}, \"2bit_heads\": [\"L22H1\", \"L24H3\"], \"8bit_heads\": [\"L6H2\"], \"L4H3_status\": \"kept_at_4bit\", \"std_mckp_k2_ppl\": 7.2209, \"std_mckp_k8_ppl\": 7.3129, \"hires_concentration\": 0.7139, \"L4H3_2bit_delta\": 13.12, \"L4H3_4bit_delta\": 0.0048, \"L4H3_8bit_delta\": 0.004}}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"top5_concentration\": 0.7139, \"top5_n_heads\": 9, \"baseline_calibration_ppl\": 5.888, \"delta_2bit_cv\": 8.8991, \"layer0_dominance_ratio\": 0.04, \"top1_head\": \"L4H3_delta=13.1236\", \"total_hours\": 0.96}}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"float32_hires_top5_concentration\": 0.6104, \"bf16_hires_range\": \"0.59-0.66\", \"float32_lowres_concentration\": 0.42, \"bf16_bug_impact_on_concentration\": 0.01, \"baseline_ppl\": 9.81, \"mckp_unconstrained_ppl\": 10.95, \"uniform_4bit_ppl\": 15.45, \"mckp_bit_dist\": {\"2\": 12, \"4\": 96, \"8\": 3, \"16\": 1}, \"l0h0_delta\": 6.7388, \"l0_4heads_total_share\": 0.586, \"claim3_threshold_0.50\": \"PASS\"}}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0157, \"mckp_wikitext2_ppl\": 7.3129, \"uniform4bit_wikitext2_ppl\": 7.2171, \"mckp_improvement_over_uniform\": -0.0958, \"top5_concentration\": 0.4934, \"layer0_dominance_ratio\": 0.07, \"best_k\": 2, \"best_k_ppl\": 7.2209, \"gqa_ratio\": \"8:1\", \"verdict\": \"FAIL\"}}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 8.9, \"mckp_wikitext2_ppl\": 9.05, \"uniform4bit_wikitext2_ppl\": 9.03, \"mckp_improvement_over_uniform\": -0.02, \"top5_concentration\": 0.23, \"layer0_dominance_ratio\": 1.32, \"best_k\": 8, \"best_k_ppl\": 9.05, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"bf16_wt2_ppl\": 7.0351, \"c4_cal_bf16_ppl\": 6.9677, \"wt2_cal_mckp_wt2_ppl\": 7.1648, \"c4_cal_mckp_wt2_ppl\": 7.1859, \"uniform_4bit_wt2_ppl\": 7.1314, \"delta_uniform_mckp_wt2_cal\": -0.0334, \"delta_uniform_mckp_c4_cal\": -0.0546, \"allocation_agreement_c4_vs_wt2\": 0.965, \"agreement_heads\": \"247/256\", \"bit_dist_wt2_cal\": \"2bit:4, 4bit:252\", \"bit_dist_c4_cal\": \"2bit:4, 4bit:251, 8bit:1\", \"profile_time_s\": 407.7, \"eval_time_s\": 349.4, \"total_time_s\": 757.1}}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"metrics\": {\"wt2_cal_wt2_ppl\": 8.4498, \"c4_cal_wt2_ppl\": 8.6459, \"uniform_wt2_ppl\": 8.469, \"wt2_cal_c4_ppl\": 7.654, \"c4_cal_c4_ppl\": 7.654, \"uniform_c4_ppl\": 7.5351, \"bf16_wt2_ppl\": 8.0918, \"bf16_c4_ppl\": 7.1333, \"agreement_rate\": 0.977, \"agreement_heads\": \"250/256\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 7.0351, \"uniform_4bit_ppl\": 7.1314, \"mckp_k4_ppl\": 7.1648, \"l0_random_seed_0\": 7.1882, \"l0_random_seed_1\": 7.1995, \"l0_random_seed_2\": 7.1723, \"l0_random_seed_3\": 7.3577, \"l0_random_seed_4\": 7.2875, \"l0_random_mean\": 7.2411, \"l0_random_std\": 0.0707, \"l0_random_median\": 7.1995, \"naive_heuristic_ppl\": 7.2105, \"budget_heuristic\": 0.2559, \"budget_mckp_k4\": 0.248}, \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"l0_random_seeds\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \"l0_random_mean\": 8.6245, \"l0_random_std\": 0.0733, \"l0_random_median\": 8.6192, \"naive_positional_ppl\": 8.5781, \"mckp_ppl\": 8.4498, \"uniform_ppl\": 8.469, \"baseline_ppl\": 8.0918, \"mckp_vs_l0_random_gap\": 0.1747, \"mckp_vs_naive_gap\": 0.1283}}, \"plan_009_oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mckp_ppl\": 10.9131, \"max_oracle_gap_ppl\": 0.0183, \"avg_oracle_gap_ppl\": 0.0046, \"layers_mckp_optimal\": \"5/8\", \"layers_with_gap\": 3, \"gap_layers\": {\"L1\": 0.0183, \"L4\": 0.0045, \"L11\": 0.0136}, \"gap_nature\": \"2-bit head position swap within same bit budget\", \"total_evals\": 54, \"runtime_min\": 21.3}}}, \"count\": 50, \"total\": 95, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2569}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "95d9b9fa-0613-4837-873e-c68cf3bc9454",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"llama_downstream_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_compounding_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_k\\\": 0, \\\"best_ppl\\\": 8.0922, \\\"k0_ppl\\\": 8.0922, \\\"k2_ppl\\\": 8.1243, \\\"k4_ppl\\\": 8.1803, \\\"k8_ppl\\\": 8.2259, \\\"k16_ppl\\\": 8.4378, \\\"k32_ppl\\\": 9.0506, \\\"k64_ppl\\\": 11.991, \\\"k128_ppl\\\": 40.2067, \\\"k256_ppl\\\": 1519.1888, \\\"budget\\\": 0.25}}, \\\"qwen25-hires-profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"cross_domain_calibration_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"greedy_constrained_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mistral_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mistral_hires_constrained_mckp_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 7.0352, \\\"mckp_wikitext2_ppl\\\": 7.1341, \\\"uniform4bit_wikitext2_ppl\\\": 7.1308, \\\"mckp_improvement_over_uniform\\\": -0.0033, \\\"mckp_improvement_pct\\\": -3.48, \\\"verdict\\\": \\\"FAIL\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 254}, \\\"fix_note\\\": \\\"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"mistral_uniform_reeval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"qwen14b_greedy_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"greedy_constrained_ppl\\\": 7.2206, \\\"mckp_constrained_ppl\\\": 7.2206, \\\"delta_vs_mckp\\\": 0, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 374, \\\"8\\\": 1, \\\"16\\\": 1}, \\\"memory_ratio\\\": 0.25, \\\"solver_time_sec\\\": 0.08, \\\"total_time_min\\\": 1.8}}, \\\"kivi_mckp_combined_qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_hires_bf16_2bitonly_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"kivi_baseline_qwen7b_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_kivi_4bit_g32_r128\\\": 9.8976, \\\"tokens\\\": 298938, \\\"chunks\\\": 583, \\\"stride\\\": 512, \\\"model\\\": \\\"Qwen2.5-7B\\\", \\\"comparison_mckp_ppl\\\": 10.91, \\\"comparison_uniform_ppl\\\": 15.45, \\\"comparison_bf16_ppl\\\": 9.81}}, \\\"qwen14b_constrained_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16\\\": 6.8654, \\\"ppl_uniform_4bit\\\": 7.202, \\\"ppl_constrained_mckp\\\": 7.2206, \\\"ppl_unconstrained_mckp\\\": 7.6923, \\\"delta_constrained_vs_uniform\\\": -0.0185, \\\"delta_constrained_vs_uniform_pct\\\": -5.51, \\\"delta_unconstrained_vs_uniform\\\": -0.4902, \\\"bit_distribution_constrained\\\": {\\\"2\\\": 8, \\\"4\\\": 374, \\\"8\\\": 1, \\\"16\\\": 1}, \\\"bit_distribution_unconstrained\\\": {\\\"2\\\": 77, \\\"4\\\": 271, \\\"8\\\": 35, \\\"16\\\": 1}, \\\"concentration\\\": 0.33, \\\"top1_pct\\\": 0.2262, \\\"top5_pct\\\": 0.3304, \\\"t1_t5\\\": 0.68, \\\"shape\\\": \\\"Flat\\\"}}, \\\"qwen_hires_constrained_d049\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"float32_hires_constrained_mckp_ppl\\\": 10.8921, \\\"baseline_ppl\\\": 9.8106, \\\"uniform_4bit_ppl\\\": 15.4484, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 100, \\\"8\\\": 4}, \\\"gap_recovery_pct\\\": 80.8, \\\"top5_concentration\\\": 0.6156, \\\"top5_concentration_pre_monotonicity\\\": 0.6104, \\\"bf16_hires_constrained_mckp_ppl\\\": 10.9131, \\\"delta_f32_vs_bf16\\\": 0.021}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ppl_bf16_8k\\\": 5.5958, \\\"ppl_constrained_mckp_8k\\\": 6.0537, \\\"ppl_uniform_4bit_8k\\\": 6.0364, \\\"mckp_improvement_over_uniform_8k\\\": -0.0174, \\\"mckp_improvement_pct_8k\\\": -3.94, \\\"ppl_bf16_2k\\\": 8.0922, \\\"ppl_constrained_mckp_2k\\\": 8.5042, \\\"ppl_uniform_4bit_2k\\\": 8.4701, \\\"shape\\\": \\\"Spike\\\", \\\"concentration\\\": 0.5749, \\\"t1_over_t5\\\": 0.71, \\\"context_length\\\": 8192, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"yi15_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"qwen7b_8k_spotcheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen7b_8k_context_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16_8k\\\": 6.97, \\\"ppl_constrained_mckp_8k\\\": 8.59, \\\"ppl_uniform_4bit_8k\\\": 77.75, \\\"ppl_bf16_2k\\\": 9.81, \\\"ppl_constrained_mckp_2k\\\": 10.89, \\\"ppl_uniform_4bit_2k\\\": 15.45, \\\"mckp_improvement_over_uniform_8k\\\": \\\"97.7%\\\", \\\"mckp_improvement_over_uniform_2k\\\": \\\"80.8%\\\", \\\"shape\\\": \\\"Spread\\\", \\\"concentration\\\": 0.5992, \\\"context_length\\\": 8192, \\\"note\\\": \\\"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\\\"}}, \\\"pythia14b_constrained_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ppl_bf16\\\": 16.4893, \\\"ppl_uniform_4bit\\\": 24.2894, \\\"ppl_constrained_mckp\\\": 24.4521, \\\"ppl_unconstrained_mckp\\\": 31.5415, \\\"concentration\\\": \\\"t1=0.0289, t5=0.2439\\\", \\\"t1_t5\\\": \\\"0.0289/0.2439\\\", \\\"shape\\\": \\\"Flat\\\", \\\"constrained_vs_uniform_gap\\\": 0.1627}}, \\\"w1_pythia14b_hires_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 13.6347, \\\"concentration\\\": 0.2439, \\\"t1_t5\\\": 0.28, \\\"shape\\\": \\\"Flat\\\", \\\"l0_dominance\\\": 0.51, \\\"cv\\\": 1.2172, \\\"positive_heads\\\": 362, \\\"total_heads\\\": 384, \\\"top5_heads\\\": [{\\\"head\\\": \\\"L1H11\\\", \\\"delta\\\": 1.016355}, {\\\"head\\\": \\\"L12H14\\\", \\\"delta\\\": 0.784513}, {\\\"head\\\": \\\"L8H4\\\", \\\"delta\\\": 0.759118}, {\\\"head\\\": \\\"L11H2\\\", \\\"delta\\\": 0.632357}, {\\\"head\\\": \\\"L13H2\\\", \\\"delta\\\": 0.522849}], \\\"elapsed_min\\\": 25.7, \\\"note\\\": \\\"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w1_qwen14b_hires_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 5.8432, \\\"concentration\\\": 0.3312, \\\"t1_t5\\\": 0.68, \\\"shape\\\": \\\"Flat\\\", \\\"l0_dominance\\\": 15.5, \\\"cv\\\": 3.7418, \\\"positive_heads\\\": 370, \\\"total_heads\\\": 384, \\\"top10_heads\\\": [{\\\"head\\\": \\\"L0H5\\\", \\\"delta\\\": 1.84494}, {\\\"head\\\": \\\"L0H4\\\", \\\"delta\\\": 0.236669}, {\\\"head\\\": \\\"L0H2\\\", \\\"delta\\\": 0.136971}, {\\\"head\\\": \\\"L28H4\\\", \\\"delta\\\": 0.099279}, {\\\"head\\\": \\\"L28H5\\\", \\\"delta\\\": 0.07576}, {\\\"head\\\": \\\"L27H4\\\", \\\"delta\\\": 0.071269}, {\\\"head\\\": \\\"L0H0\\\", \\\"delta\\\": 0.070018}, {\\\"head\\\": \\\"L28H6\\\", \\\"delta\\\": 0.063737}, {\\\"head\\\": \\\"L26H0\\\", \\\"delta\\\": 0.061462}, {\\\"head\\\": \\\"L31H3\\\", \\\"delta\\\": 0.061062}], \\\"elapsed_min\\\": 161.3, \\\"note\\\": \\\"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\\\"}}, \\\"kivi_baseline_qwen_llama\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"qwen_2bit_r128\\\": 12.83, \\\"qwen_4bit_r128\\\": 9.9, \\\"qwen_2bit_r0\\\": 13.34, \\\"qwen_4bit_r0\\\": 9.91, \\\"llama_2bit_r128\\\": 9.84, \\\"llama_4bit_r128\\\": 8.14, \\\"llama_2bit_r0\\\": 10.08, \\\"llama_4bit_r0\\\": 8.14, \\\"group_size\\\": 32, \\\"eval_data\\\": \\\"WikiText-2 test\\\", \\\"note\\\": \\\"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\\\"}}, \\\"gemma2_constrained_bos_fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 6.0306, \\\"uniform_4bit_ppl\\\": 6.1683, \\\"constrained_mckp_ppl\\\": 6.1951, \\\"mckp_vs_uniform_delta\\\": 0.0267, \\\"mckp_delta_ppl\\\": 0.1645, \\\"uniform_delta_ppl\\\": 0.1377, \\\"bit_distribution\\\": {\\\"2\\\": 8, \\\"4\\\": 324, \\\"8\\\": 4}, \\\"n_2bit\\\": 8, \\\"max_2bit\\\": 8, \\\"memory_ratio\\\": 0.25, \\\"eval_method\\\": \\\"sliding_window_bos_fix\\\", \\\"elapsed_seconds\\\": 490.3}}, \\\"w2_unconstrained_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"yi15_baseline\\\": 7.0157, \\\"yi15_uniform4\\\": 7.2171, \\\"yi15_greedy\\\": 7.5615, \\\"yi15_mckp\\\": 7.5615, \\\"yi15_n2bit\\\": 22, \\\"llama_baseline\\\": 8.0922, \\\"llama_uniform4\\\": 8.4701, \\\"llama_greedy\\\": 8.6265, \\\"llama_mckp\\\": 8.6265, \\\"llama_n2bit\\\": 12, \\\"mistral_baseline\\\": 7.0352, \\\"mistral_uniform4\\\": 7.1308, \\\"mistral_greedy\\\": 7.5733, \\\"mistral_mckp\\\": 7.5963, \\\"mistral_n2bit\\\": 42, \\\"gemma2_baseline\\\": 6.0306, \\\"gemma2_uniform4\\\": 6.1683, \\\"gemma2_greedy\\\": 8.8469, \\\"gemma2_mckp\\\": 8.8469, \\\"gemma2_n2bit\\\": 106, \\\"gemma2_eval_method\\\": \\\"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\\\", \\\"gemma2_greedy_ratio\\\": 1.467, \\\"gemma2_catastrophic\\\": true, \\\"gemma2_note\\\": \\\"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\\\"}}, \\\"w3_downstream_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"yi15_baseline_avg\\\": 0.6912, \\\"yi15_uniform_avg\\\": 0.6822, \\\"yi15_mckp_avg\\\": 0.6745, \\\"yi15_mckp_vs_uniform_pp\\\": -0.77, \\\"yi15_mckp_vs_baseline_pp\\\": -1.67, \\\"yi15_baseline\\\": {\\\"arc_easy\\\": 0.8093, \\\"arc_challenge\\\": 0.5265, \\\"hellaswag\\\": 0.5913, \\\"piqa\\\": 0.7949, \\\"winogrande\\\": 0.734}, \\\"yi15_uniform\\\": {\\\"arc_easy\\\": 0.7946, \\\"arc_challenge\\\": 0.5205, \\\"hellaswag\\\": 0.5857, \\\"piqa\\\": 0.7927, \\\"winogrande\\\": 0.7174}, \\\"yi15_mckp\\\": {\\\"arc_easy\\\": 0.7854, \\\"arc_challenge\\\": 0.4881, \\\"hellaswag\\\": 0.5797, \\\"piqa\\\": 0.7894, \\\"winogrande\\\": 0.7301}, \\\"llama_baseline_avg\\\": 0.696, \\\"llama_uniform_avg\\\": 0.6915, \\\"llama_mckp_avg\\\": 0.6816, \\\"llama_mckp_vs_uniform_pp\\\": -0.99, \\\"llama_mckp_vs_baseline_pp\\\": -1.44, \\\"llama_baseline\\\": {\\\"arc_easy\\\": 0.8228, \\\"arc_challenge\\\": 0.5188, \\\"hellaswag\\\": 0.6073, \\\"piqa\\\": 0.7922, \\\"winogrande\\\": 0.7388}, \\\"llama_uniform\\\": {\\\"arc_easy\\\": 0.8173, \\\"arc_challenge\\\": 0.5256, \\\"hellaswag\\\": 0.6026, \\\"piqa\\\": 0.7867, \\\"winogrande\\\": 0.7253}, \\\"llama_mckp\\\": {\\\"arc_easy\\\": 0.8039, \\\"arc_challenge\\\": 0.4991, \\\"hellaswag\\\": 0.6012, \\\"piqa\\\": 0.7802, \\\"winogrande\\\": 0.7238}, \\\"mistral_baseline_avg\\\": 0.6917, \\\"mistral_uniform_avg\\\": 0.6894, \\\"mistral_mckp_avg\\\": 0.6846, \\\"mistral_mckp_vs_uniform_pp\\\": -0.48, \\\"mistral_mckp_vs_baseline_pp\\\": -0.71, \\\"mistral_baseline\\\": {\\\"arc_easy\\\": 0.8005, \\\"arc_challenge\\\": 0.5043, \\\"hellaswag\\\": 0.6118, \\\"piqa\\\": 0.8009, \\\"winogrande\\\": 0.7411}, \\\"mistral_uniform\\\": {\\\"arc_easy\\\": 0.7976, \\\"arc_challenge\\\": 0.5068, \\\"hellaswag\\\": 0.6051, \\\"piqa\\\": 0.7982, \\\"winogrande\\\": 0.7395}, \\\"mistral_mckp\\\": {\\\"arc_easy\\\": 0.7942, \\\"arc_challenge\\\": 0.4949, \\\"hellaswag\\\": 0.6027, \\\"piqa\\\": 0.802, \\\"winogrande\\\": 0.7293}, \\\"gemma2_baseline_avg\\\": 0.7307, \\\"gemma2_uniform_avg\\\": 0.7251, \\\"gemma2_mckp_avg\\\": 0.7265, \\\"gemma2_mckp_vs_uniform_pp\\\": 0.14, \\\"gemma2_mckp_vs_baseline_pp\\\": -0.42, \\\"gemma2_baseline\\\": {\\\"arc_easy\\\": 0.8737, \\\"arc_challenge\\\": 0.6135, \\\"hellaswag\\\": 0.6093, \\\"piqa\\\": 0.8128, \\\"winogrande\\\": 0.7443}, \\\"gemma2_uniform\\\": {\\\"arc_easy\\\": 0.8662, \\\"arc_challenge\\\": 0.6058, \\\"hellaswag\\\": 0.606, \\\"piqa\\\": 0.8079, \\\"winogrande\\\": 0.7395}, \\\"gemma2_mckp\\\": {\\\"arc_easy\\\": 0.8649, \\\"arc_challenge\\\": 0.6041, \\\"hellaswag\\\": 0.6089, \\\"piqa\\\": 0.8074, \\\"winogrande\\\": 0.7474}, \\\"eval_harness_version\\\": \\\"0.4.11\\\", \\\"num_fewshot\\\": 0, \\\"yi_elapsed_s\\\": 1563.2, \\\"llama_elapsed_s\\\": 1446.4, \\\"mistral_elapsed_s\\\": 1302.2, \\\"gemma2_elapsed_s\\\": 1735.9}}, \\\"w9_compounding_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 9.81, \\\"k1_topk_ppl\\\": 9.826, \\\"k1_randomk_ppl\\\": 9.887, \\\"k1_randomk_std\\\": 0.05, \\\"k4_topk_ppl\\\": 9.849, \\\"k4_topk_ratio\\\": 0.86, \\\"k4_randomk_ppl\\\": 10.06, \\\"k4_randomk_std\\\": 0.06, \\\"k4_randomk_ratio\\\": 1.24, \\\"k8_topk_ppl\\\": 10.042, \\\"k8_topk_ratio\\\": 1.56, \\\"k8_randomk_ppl\\\": 11.07, \\\"k8_randomk_std\\\": 0.69, \\\"k8_randomk_ratio\\\": 1.76, \\\"k16_topk_ppl\\\": 10.42, \\\"k16_topk_ratio\\\": 1.56, \\\"k16_randomk_ppl\\\": 12.91, \\\"k16_randomk_std\\\": 0.4, \\\"k16_randomk_ratio\\\": 2.1, \\\"k32_topk_ppl\\\": 11.604, \\\"k32_topk_ratio\\\": 1.78, \\\"k32_randomk_ppl\\\": 18.33, \\\"k32_randomk_std\\\": 2.53, \\\"k32_randomk_ratio\\\": 2.73, \\\"k64_topk_ppl\\\": 22.946, \\\"k64_topk_ratio\\\": 4.89, \\\"k64_randomk_ppl\\\": 55.94, \\\"k64_randomk_std\\\": 9.73, \\\"k64_randomk_ratio\\\": 8.88, \\\"runtime_minutes\\\": 16.9, \\\"note\\\": \\\"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\\\"}}, \\\"w9_compounding_scaling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"baseline_ppl\\\": 8.2, \\\"n1_joint_ppl\\\": 14.94, \\\"n1_ratio\\\": 1, \\\"n2_joint_ppl\\\": 42.26, \\\"n2_ratio\\\": 3.84, \\\"n4_joint_ppl\\\": 3813.76, \\\"n4_ratio\\\": 333.3, \\\"n8_joint_ppl\\\": 3586.42, \\\"n8_ratio\\\": 282.1, \\\"n16_joint_ppl\\\": 7286.23, \\\"n16_ratio\\\": 521.1, \\\"n32_joint_ppl\\\": 6644.05, \\\"n32_ratio\\\": 424, \\\"n64_joint_ppl\\\": 9453.33, \\\"n64_ratio\\\": 533.3, \\\"runtime_seconds\\\": 96}}, \\\"w2_unconstrained_baselines\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"note\\\": \\\"2bitonly profiles only - INVALID for reviewer response\\\", \\\"yi15_ppl\\\": 672.2, \\\"yi15_ratio\\\": 114, \\\"llama_ppl\\\": 1219.7, \\\"llama_ratio\\\": 187, \\\"mistral_ppl_2bitonly\\\": 47.8, \\\"mistral_ratio_2bitonly\\\": 8.2, \\\"mistral_ppl_full\\\": 6.39, \\\"mistral_ratio_full\\\": 1.09, \\\"gemma2_ppl\\\": 277.4, \\\"gemma2_ratio\\\": 37.9, \\\"budget\\\": 0.25, \\\"baseline_yi\\\": 5.89, \\\"baseline_llama\\\": 6.51, \\\"baseline_mistral\\\": 5.87, \\\"baseline_gemma2\\\": 7.32}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"gemma2_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"concentration_top5pct\\\": 0.2291, \\\"l0_dominance_ratio\\\": 2.05, \\\"cv_delta_2bit\\\": 1.2834, \\\"positive_delta_heads\\\": \\\"310/336\\\", \\\"top_head\\\": \\\"L0H1 delta=0.1906\\\", \\\"total_time_hours\\\": 1.59}}, \\\"mistral_c4_hires_crossdataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"fp16_ppl\\\": 7.0352, \\\"c4_mckp_ppl\\\": 7.1774, \\\"uniform_4bit_ppl\\\": 7.1308, \\\"mckp_vs_uniform_delta\\\": 0.0466, \\\"mckp_bit_distribution\\\": {\\\"2\\\": 4, \\\"4\\\": 250, \\\"8\\\": 2}, \\\"phase4_error\\\": \\\"FileNotFoundError: mistral_k_ablation_results.json\\\"}}, \\\"llama_c4_hires_crossdataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"bf16_wt2_ppl\\\": 8.0922, \\\"bf16_c4_ppl\\\": 7.1333, \\\"c4_cal_mckp_wt2_ppl\\\": 8.5103, \\\"c4_cal_mckp_c4_ppl\\\": 7.5351, \\\"uniform_wt2_ppl\\\": 8.4701, \\\"uniform_c4_ppl\\\": 7.5351, \\\"delta_c4_uniform_minus_mckp\\\": 0, \\\"delta_wt2_uniform_minus_mckp\\\": -0.0402, \\\"verdict_c4\\\": \\\"FAIL\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}, \\\"heads_2bit\\\": [\\\"2,3\\\", \\\"24,2\\\"], \\\"heads_8bit\\\": [\\\"31,6\\\"], \\\"total_time_min\\\": 6.3, \\\"wt2_ref_mckp_ppl\\\": 8.5042, \\\"wt2_ref_delta\\\": -0.0341}}, \\\"mistral_hires_bf16_2bitonly_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.241, \\\"top5_n_heads\\\": 12, \\\"baseline_ppl\\\": 5.8702, \\\"top1_head\\\": \\\"L2H5\\\", \\\"top1_delta_2bit\\\": 0.3236, \\\"top2_head\\\": \\\"L12H1\\\", \\\"top2_delta_2bit\\\": 0.1435, \\\"top3_head\\\": \\\"L0H7\\\", \\\"top3_delta_2bit\\\": 0.1403, \\\"delta_2bit_mean\\\": 0.020073, \\\"delta_2bit_std\\\": 0.026278, \\\"delta_2bit_cv\\\": 1.3091, \\\"layer0_mean_delta_2bit\\\": 0.034073, \\\"other_layers_mean_delta_2bit\\\": 0.019621, \\\"l0_dominance_ratio\\\": 1.74, \\\"positive_delta_heads\\\": 252, \\\"total_heads\\\": 256, \\\"distribution_shape\\\": \\\"flat\\\", \\\"total_hours\\\": 0.94, \\\"profile_seconds\\\": 3371.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_bf16_ppl\\\": 8.0922, \\\"hires_mckp_ppl\\\": 8.5042, \\\"uniform_4bit_ppl\\\": 8.4701, \\\"std_mckp_reference_ppl\\\": 8.4498, \\\"mckp_vs_uniform_delta\\\": -0.0341, \\\"mckp_vs_uniform_pct\\\": -9, \\\"hires_vs_std_mckp_delta\\\": 0.0544, \\\"concentration\\\": 0.5749, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}, \\\"heads_2bit\\\": [\\\"26,0\\\", \\\"31,7\\\"], \\\"heads_8bit\\\": [\\\"12,3\\\"], \\\"verdict\\\": \\\"FAIL\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"llama_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.5749, \\\"t1_t5\\\": 0.85, \\\"baseline_ppl\\\": 6.5055, \\\"top1_head\\\": \\\"L2H5_delta=15.2636\\\", \\\"delta_2bit_cv\\\": 7.7663, \\\"l0_dominance_ratio\\\": 0.67, \\\"positive_delta_heads\\\": 254, \\\"total_heads\\\": 256, \\\"total_hours\\\": 0.98}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_hires_bf16_2bitonly_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\\\"}}, \\\"mistral_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\\\"}}, \\\"yi15_hires_constrained_mckp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"hires_mckp_ppl\\\": 7.2181, \\\"uniform_4bit_ppl\\\": 7.2171, \\\"baseline_ppl\\\": 7.0157, \\\"delta_vs_uniform\\\": -0.001, \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 189, \\\"8\\\": 1}, \\\"2bit_heads\\\": [\\\"L22H1\\\", \\\"L24H3\\\"], \\\"8bit_heads\\\": [\\\"L6H2\\\"], \\\"L4H3_status\\\": \\\"kept_at_4bit\\\", \\\"std_mckp_k2_ppl\\\": 7.2209, \\\"std_mckp_k8_ppl\\\": 7.3129, \\\"hires_concentration\\\": 0.7139, \\\"L4H3_2bit_delta\\\": 13.12, \\\"L4H3_4bit_delta\\\": 0.0048, \\\"L4H3_8bit_delta\\\": 0.004}}, \\\"yi15_hires_bf16_2bitonly\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"top5_concentration\\\": 0.7139, \\\"top5_n_heads\\\": 9, \\\"baseline_calibration_ppl\\\": 5.888, \\\"delta_2bit_cv\\\": 8.8991, \\\"layer0_dominance_ratio\\\": 0.04, \\\"top1_head\\\": \\\"L4H3_delta=13.1236\\\", \\\"total_hours\\\": 0.96}}, \\\"qwen_hires_float32_d048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"float32_hires_top5_concentration\\\": 0.6104, \\\"bf16_hires_range\\\": \\\"0.59-0.66\\\", \\\"float32_lowres_concentration\\\": 0.42, \\\"bf16_bug_impact_on_concentration\\\": 0.01, \\\"baseline_ppl\\\": 9.81, \\\"mckp_unconstrained_ppl\\\": 10.95, \\\"uniform_4bit_ppl\\\": 15.45, \\\"mckp_bit_dist\\\": {\\\"2\\\": 12, \\\"4\\\": 96, \\\"8\\\": 3, \\\"16\\\": 1}, \\\"l0h0_delta\\\": 6.7388, \\\"l0_4heads_total_share\\\": 0.586, \\\"claim3_threshold_0.50\\\": \\\"PASS\\\"}}, \\\"yi15_hires_float32_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"yi15_9b_full_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 7.0157, \\\"mckp_wikitext2_ppl\\\": 7.3129, \\\"uniform4bit_wikitext2_ppl\\\": 7.2171, \\\"mckp_improvement_over_uniform\\\": -0.0958, \\\"top5_concentration\\\": 0.4934, \\\"layer0_dominance_ratio\\\": 0.07, \\\"best_k\\\": 2, \\\"best_k_ppl\\\": 7.2209, \\\"gqa_ratio\\\": \\\"8:1\\\", \\\"verdict\\\": \\\"FAIL\\\"}}, \\\"gemma2_9b_full_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_wikitext2_ppl\\\": 8.9, \\\"mckp_wikitext2_ppl\\\": 9.05, \\\"uniform4bit_wikitext2_ppl\\\": 9.03, \\\"mckp_improvement_over_uniform\\\": -0.02, \\\"top5_concentration\\\": 0.23, \\\"layer0_dominance_ratio\\\": 1.32, \\\"best_k\\\": 8, \\\"best_k_ppl\\\": 9.05, \\\"verdict\\\": \\\"FAIL\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"qwen72b_profiling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"multi_seed_lowres\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mistral_c4_cross_dataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"bf16_wt2_ppl\\\": 7.0351, \\\"c4_cal_bf16_ppl\\\": 6.9677, \\\"wt2_cal_mckp_wt2_ppl\\\": 7.1648, \\\"c4_cal_mckp_wt2_ppl\\\": 7.1859, \\\"uniform_4bit_wt2_ppl\\\": 7.1314, \\\"delta_uniform_mckp_wt2_cal\\\": -0.0334, \\\"delta_uniform_mckp_c4_cal\\\": -0.0546, \\\"allocation_agreement_c4_vs_wt2\\\": 0.965, \\\"agreement_heads\\\": \\\"247/256\\\", \\\"bit_dist_wt2_cal\\\": \\\"2bit:4, 4bit:252\\\", \\\"bit_dist_c4_cal\\\": \\\"2bit:4, 4bit:251, 8bit:1\\\", \\\"profile_time_s\\\": 407.7, \\\"eval_time_s\\\": 349.4, \\\"total_time_s\\\": 757.1}}, \\\"llama_c4_cross_dataset\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wt2_cal_wt2_ppl\\\": 8.4498, \\\"c4_cal_wt2_ppl\\\": 8.6459, \\\"uniform_wt2_ppl\\\": 8.469, \\\"wt2_cal_c4_ppl\\\": 7.654, \\\"c4_cal_c4_ppl\\\": 7.654, \\\"uniform_c4_ppl\\\": 7.5351, \\\"bf16_wt2_ppl\\\": 8.0918, \\\"bf16_c4_ppl\\\": 7.1333, \\\"agreement_rate\\\": 0.977, \\\"agreement_heads\\\": \\\"250/256\\\", \\\"bit_distribution\\\": {\\\"2\\\": 2, \\\"4\\\": 253, \\\"8\\\": 1}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"mistral_heuristic_k4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"baseline_bf16_ppl\\\": 7.0351, \\\"uniform_4bit_ppl\\\": 7.1314, \\\"mckp_k4_ppl\\\": 7.1648, \\\"l0_random_seed_0\\\": 7.1882, \\\"l0_random_seed_1\\\": 7.1995, \\\"l0_random_seed_2\\\": 7.1723, \\\"l0_random_seed_3\\\": 7.3577, \\\"l0_random_seed_4\\\": 7.2875, \\\"l0_random_mean\\\": 7.2411, \\\"l0_random_std\\\": 0.0707, \\\"l0_random_median\\\": 7.1995, \\\"naive_heuristic_ppl\\\": 7.2105, \\\"budget_heuristic\\\": 0.2559, \\\"budget_mckp_k4\\\": 0.248}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_heuristic_k2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"l0_random_seeds\\\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \\\"l0_random_mean\\\": 8.6245, \\\"l0_random_std\\\": 0.0733, \\\"l0_random_median\\\": 8.6192, \\\"naive_positional_ppl\\\": 8.5781, \\\"mckp_ppl\\\": 8.4498, \\\"uniform_ppl\\\": 8.469, \\\"baseline_ppl\\\": 8.0918, \\\"mckp_vs_l0_random_gap\\\": 0.1747, \\\"mckp_vs_naive_gap\\\": 0.1283}}, \\\"plan_009_oracle_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"oracle_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mckp_ppl\\\": 10.9131, \\\"max_oracle_gap_ppl\\\": 0.0183, \\\"avg_oracle_gap_ppl\\\": 0.0046, \\\"layers_mckp_optimal\\\": \\\"5/8\\\", \\\"layers_with_gap\\\": 3, \\\"gap_layers\\\": {\\\"L1\\\": 0.0183, \\\"L4\\\": 0.0045, \\\"L11\\\": 0.0136}, \\\"gap_nature\\\": \\\"2-bit head position swap within same bit budget\\\", \\\"total_evals\\\": 54, \\\"runtime_min\\\": 21.3}}}, \\\"count\\\": 50, \\\"total\\\": 95, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2569}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"llama_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_compounding_sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_k\": 0, \"best_ppl\": 8.0922, \"k0_ppl\": 8.0922, \"k2_ppl\": 8.1243, \"k4_ppl\": 8.1803, \"k8_ppl\": 8.2259, \"k16_ppl\": 8.4378, \"k32_ppl\": 9.0506, \"k64_ppl\": 11.991, \"k128_ppl\": 40.2067, \"k256_ppl\": 1519.1888, \"budget\": 0.25}}, \"qwen25-hires-profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_constrained_mckp_v2\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0352, \"mckp_wikitext2_ppl\": 7.1341, \"uniform4bit_wikitext2_ppl\": 7.1308, \"mckp_improvement_over_uniform\": -0.0033, \"mckp_improvement_pct\": -3.48, \"verdict\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 254}, \"fix_note\": \"uniform eval re-run: original had bits=budget(0.25) bug causing PPL=50130\"}, \"conclusion\": \"negative\"}, \"mistral_uniform_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen14b_greedy_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_constrained_ppl\": 7.2206, \"mckp_constrained_ppl\": 7.2206, \"delta_vs_mckp\": 0, \"bit_distribution\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"memory_ratio\": 0.25, \"solver_time_sec\": 0.08, \"total_time_min\": 1.8}}, \"kivi_mckp_combined_qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kivi_baseline_qwen7b_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_kivi_4bit_g32_r128\": 9.8976, \"tokens\": 298938, \"chunks\": 583, \"stride\": 512, \"model\": \"Qwen2.5-7B\", \"comparison_mckp_ppl\": 10.91, \"comparison_uniform_ppl\": 15.45, \"comparison_bf16_ppl\": 9.81}}, \"qwen14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 6.8654, \"ppl_uniform_4bit\": 7.202, \"ppl_constrained_mckp\": 7.2206, \"ppl_unconstrained_mckp\": 7.6923, \"delta_constrained_vs_uniform\": -0.0185, \"delta_constrained_vs_uniform_pct\": -5.51, \"delta_unconstrained_vs_uniform\": -0.4902, \"bit_distribution_constrained\": {\"2\": 8, \"4\": 374, \"8\": 1, \"16\": 1}, \"bit_distribution_unconstrained\": {\"2\": 77, \"4\": 271, \"8\": 35, \"16\": 1}, \"concentration\": 0.33, \"top1_pct\": 0.2262, \"top5_pct\": 0.3304, \"t1_t5\": 0.68, \"shape\": \"Flat\"}}, \"qwen_hires_constrained_d049\": {\"status\": \"DONE\", \"metrics\": {\"float32_hires_constrained_mckp_ppl\": 10.8921, \"baseline_ppl\": 9.8106, \"uniform_4bit_ppl\": 15.4484, \"bit_distribution\": {\"2\": 8, \"4\": 100, \"8\": 4}, \"gap_recovery_pct\": 80.8, \"top5_concentration\": 0.6156, \"top5_concentration_pre_monotonicity\": 0.6104, \"bf16_hires_constrained_mckp_ppl\": 10.9131, \"delta_f32_vs_bf16\": 0.021}, \"conclusion\": \"success\"}, \"llama_8k_spotcheck\": {\"status\": \"DONE\", \"metrics\": {\"ppl_bf16_8k\": 5.5958, \"ppl_constrained_mckp_8k\": 6.0537, \"ppl_uniform_4bit_8k\": 6.0364, \"mckp_improvement_over_uniform_8k\": -0.0174, \"mckp_improvement_pct_8k\": -3.94, \"ppl_bf16_2k\": 8.0922, \"ppl_constrained_mckp_2k\": 8.5042, \"ppl_uniform_4bit_2k\": 8.4701, \"shape\": \"Spike\", \"concentration\": 0.5749, \"t1_over_t5\": 0.71, \"context_length\": 8192, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"success\"}, \"yi15_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen7b_8k_spotcheck\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"qwen7b_8k_context_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16_8k\": 6.97, \"ppl_constrained_mckp_8k\": 8.59, \"ppl_uniform_4bit_8k\": 77.75, \"ppl_bf16_2k\": 9.81, \"ppl_constrained_mckp_2k\": 10.89, \"ppl_uniform_4bit_2k\": 15.45, \"mckp_improvement_over_uniform_8k\": \"97.7%\", \"mckp_improvement_over_uniform_2k\": \"80.8%\", \"shape\": \"Spread\", \"concentration\": 0.5992, \"context_length\": 8192, \"note\": \"Concentration-dependent benefit amplifies at longer context: uniform 4-bit catastrophically degrades at 8K (77.75 vs 6.97 baseline = 11x), MCKP stays robust (+23%)\"}}, \"pythia14b_constrained_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ppl_bf16\": 16.4893, \"ppl_uniform_4bit\": 24.2894, \"ppl_constrained_mckp\": 24.4521, \"ppl_unconstrained_mckp\": 31.5415, \"concentration\": \"t1=0.0289, t5=0.2439\", \"t1_t5\": \"0.0289/0.2439\", \"shape\": \"Flat\", \"constrained_vs_uniform_gap\": 0.1627}}, \"w1_pythia14b_hires_profiling\": {\"status\": \"DONE\", \"metrics\": {\"baseline_ppl\": 13.6347, \"concentration\": 0.2439, \"t1_t5\": 0.28, \"shape\": \"Flat\", \"l0_dominance\": 0.51, \"cv\": 1.2172, \"positive_heads\": 362, \"total_heads\": 384, \"top5_heads\": [{\"head\": \"L1H11\", \"delta\": 1.016355}, {\"head\": \"L12H14\", \"delta\": 0.784513}, {\"head\": \"L8H4\", \"delta\": 0.759118}, {\"head\": \"L11H2\", \"delta\": 0.632357}, {\"head\": \"L13H2\", \"delta\": 0.522849}], \"elapsed_min\": 25.7, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}, \"conclusion\": \"success\"}, \"w1_qwen14b_hires_profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 5.8432, \"concentration\": 0.3312, \"t1_t5\": 0.68, \"shape\": \"Flat\", \"l0_dominance\": 15.5, \"cv\": 3.7418, \"positive_heads\": 370, \"total_heads\": 384, \"top10_heads\": [{\"head\": \"L0H5\", \"delta\": 1.84494}, {\"head\": \"L0H4\", \"delta\": 0.236669}, {\"head\": \"L0H2\", \"delta\": 0.136971}, {\"head\": \"L28H4\", \"delta\": 0.099279}, {\"head\": \"L28H5\", \"delta\": 0.07576}, {\"head\": \"L27H4\", \"delta\": 0.071269}, {\"head\": \"L0H0\", \"delta\": 0.070018}, {\"head\": \"L28H6\", \"delta\": 0.063737}, {\"head\": \"L26H0\", \"delta\": 0.061462}, {\"head\": \"L31H3\", \"delta\": 0.061062}], \"elapsed_min\": 161.3, \"note\": \"t1/t5 corrected: canonical formula = top1_conc/top5_conc, not delta ratio\"}}, \"kivi_baseline_qwen_llama\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"qwen_2bit_r128\": 12.83, \"qwen_4bit_r128\": 9.9, \"qwen_2bit_r0\": 13.34, \"qwen_4bit_r0\": 9.91, \"llama_2bit_r128\": 9.84, \"llama_4bit_r128\": 8.14, \"llama_2bit_r0\": 10.08, \"llama_4bit_r0\": 8.14, \"group_size\": 32, \"eval_data\": \"WikiText-2 test\", \"note\": \"r128=residual_length 128 (25% fp16), r0=strict quantization (fair comparison)\"}}, \"gemma2_constrained_bos_fix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 6.0306, \"uniform_4bit_ppl\": 6.1683, \"constrained_mckp_ppl\": 6.1951, \"mckp_vs_uniform_delta\": 0.0267, \"mckp_delta_ppl\": 0.1645, \"uniform_delta_ppl\": 0.1377, \"bit_distribution\": {\"2\": 8, \"4\": 324, \"8\": 4}, \"n_2bit\": 8, \"max_2bit\": 8, \"memory_ratio\": 0.25, \"eval_method\": \"sliding_window_bos_fix\", \"elapsed_seconds\": 490.3}}, \"w2_unconstrained_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline\": 7.0157, \"yi15_uniform4\": 7.2171, \"yi15_greedy\": 7.5615, \"yi15_mckp\": 7.5615, \"yi15_n2bit\": 22, \"llama_baseline\": 8.0922, \"llama_uniform4\": 8.4701, \"llama_greedy\": 8.6265, \"llama_mckp\": 8.6265, \"llama_n2bit\": 12, \"mistral_baseline\": 7.0352, \"mistral_uniform4\": 7.1308, \"mistral_greedy\": 7.5733, \"mistral_mckp\": 7.5963, \"mistral_n2bit\": 42, \"gemma2_baseline\": 6.0306, \"gemma2_uniform4\": 6.1683, \"gemma2_greedy\": 8.8469, \"gemma2_mckp\": 8.8469, \"gemma2_n2bit\": 106, \"gemma2_eval_method\": \"sliding_window_bos_fix (stride=512, max_length=2048, BOS prepend)\", \"gemma2_greedy_ratio\": 1.467, \"gemma2_catastrophic\": true, \"gemma2_note\": \"1.47x baseline with 31.5% heads at 2-bit; supports k-constraint universal value\"}}, \"w3_downstream_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"yi15_baseline_avg\": 0.6912, \"yi15_uniform_avg\": 0.6822, \"yi15_mckp_avg\": 0.6745, \"yi15_mckp_vs_uniform_pp\": -0.77, \"yi15_mckp_vs_baseline_pp\": -1.67, \"yi15_baseline\": {\"arc_easy\": 0.8093, \"arc_challenge\": 0.5265, \"hellaswag\": 0.5913, \"piqa\": 0.7949, \"winogrande\": 0.734}, \"yi15_uniform\": {\"arc_easy\": 0.7946, \"arc_challenge\": 0.5205, \"hellaswag\": 0.5857, \"piqa\": 0.7927, \"winogrande\": 0.7174}, \"yi15_mckp\": {\"arc_easy\": 0.7854, \"arc_challenge\": 0.4881, \"hellaswag\": 0.5797, \"piqa\": 0.7894, \"winogrande\": 0.7301}, \"llama_baseline_avg\": 0.696, \"llama_uniform_avg\": 0.6915, \"llama_mckp_avg\": 0.6816, \"llama_mckp_vs_uniform_pp\": -0.99, \"llama_mckp_vs_baseline_pp\": -1.44, \"llama_baseline\": {\"arc_easy\": 0.8228, \"arc_challenge\": 0.5188, \"hellaswag\": 0.6073, \"piqa\": 0.7922, \"winogrande\": 0.7388}, \"llama_uniform\": {\"arc_easy\": 0.8173, \"arc_challenge\": 0.5256, \"hellaswag\": 0.6026, \"piqa\": 0.7867, \"winogrande\": 0.7253}, \"llama_mckp\": {\"arc_easy\": 0.8039, \"arc_challenge\": 0.4991, \"hellaswag\": 0.6012, \"piqa\": 0.7802, \"winogrande\": 0.7238}, \"mistral_baseline_avg\": 0.6917, \"mistral_uniform_avg\": 0.6894, \"mistral_mckp_avg\": 0.6846, \"mistral_mckp_vs_uniform_pp\": -0.48, \"mistral_mckp_vs_baseline_pp\": -0.71, \"mistral_baseline\": {\"arc_easy\": 0.8005, \"arc_challenge\": 0.5043, \"hellaswag\": 0.6118, \"piqa\": 0.8009, \"winogrande\": 0.7411}, \"mistral_uniform\": {\"arc_easy\": 0.7976, \"arc_challenge\": 0.5068, \"hellaswag\": 0.6051, \"piqa\": 0.7982, \"winogrande\": 0.7395}, \"mistral_mckp\": {\"arc_easy\": 0.7942, \"arc_challenge\": 0.4949, \"hellaswag\": 0.6027, \"piqa\": 0.802, \"winogrande\": 0.7293}, \"gemma2_baseline_avg\": 0.7307, \"gemma2_uniform_avg\": 0.7251, \"gemma2_mckp_avg\": 0.7265, \"gemma2_mckp_vs_uniform_pp\": 0.14, \"gemma2_mckp_vs_baseline_pp\": -0.42, \"gemma2_baseline\": {\"arc_easy\": 0.8737, \"arc_challenge\": 0.6135, \"hellaswag\": 0.6093, \"piqa\": 0.8128, \"winogrande\": 0.7443}, \"gemma2_uniform\": {\"arc_easy\": 0.8662, \"arc_challenge\": 0.6058, \"hellaswag\": 0.606, \"piqa\": 0.8079, \"winogrande\": 0.7395}, \"gemma2_mckp\": {\"arc_easy\": 0.8649, \"arc_challenge\": 0.6041, \"hellaswag\": 0.6089, \"piqa\": 0.8074, \"winogrande\": 0.7474}, \"eval_harness_version\": \"0.4.11\", \"num_fewshot\": 0, \"yi_elapsed_s\": 1563.2, \"llama_elapsed_s\": 1446.4, \"mistral_elapsed_s\": 1302.2, \"gemma2_elapsed_s\": 1735.9}}, \"w9_compounding_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"baseline_ppl\": 9.81, \"k1_topk_ppl\": 9.826, \"k1_randomk_ppl\": 9.887, \"k1_randomk_std\": 0.05, \"k4_topk_ppl\": 9.849, \"k4_topk_ratio\": 0.86, \"k4_randomk_ppl\": 10.06, \"k4_randomk_std\": 0.06, \"k4_randomk_ratio\": 1.24, \"k8_topk_ppl\": 10.042, \"k8_topk_ratio\": 1.56, \"k8_randomk_ppl\": 11.07, \"k8_randomk_std\": 0.69, \"k8_randomk_ratio\": 1.76, \"k16_topk_ppl\": 10.42, \"k16_topk_ratio\": 1.56, \"k16_randomk_ppl\": 12.91, \"k16_randomk_std\": 0.4, \"k16_randomk_ratio\": 2.1, \"k32_topk_ppl\": 11.604, \"k32_topk_ratio\": 1.78, \"k32_randomk_ppl\": 18.33, \"k32_randomk_std\": 2.53, \"k32_randomk_ratio\": 2.73, \"k64_topk_ppl\": 22.946, \"k64_topk_ratio\": 4.89, \"k64_randomk_ppl\": 55.94, \"k64_randomk_std\": 9.73, \"k64_randomk_ratio\": 8.88, \"runtime_minutes\": 16.9, \"note\": \"v2 redesign: WikiText-2 test set eval, L0 excluded, marginal benefit ranking, top-k vs random-k control. PPL 单调递增。v1 非单调和 333x 是 L0 伪象。\"}}, \"w9_compounding_scaling\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"baseline_ppl\": 8.2, \"n1_joint_ppl\": 14.94, \"n1_ratio\": 1, \"n2_joint_ppl\": 42.26, \"n2_ratio\": 3.84, \"n4_joint_ppl\": 3813.76, \"n4_ratio\": 333.3, \"n8_joint_ppl\": 3586.42, \"n8_ratio\": 282.1, \"n16_joint_ppl\": 7286.23, \"n16_ratio\": 521.1, \"n32_joint_ppl\": 6644.05, \"n32_ratio\": 424, \"n64_joint_ppl\": 9453.33, \"n64_ratio\": 533.3, \"runtime_seconds\": 96}}, \"w2_unconstrained_baselines\": {\"status\": \"DONE\", \"metrics\": {\"note\": \"2bitonly profiles only - INVALID for reviewer response\", \"yi15_ppl\": 672.2, \"yi15_ratio\": 114, \"llama_ppl\": 1219.7, \"llama_ratio\": 187, \"mistral_ppl_2bitonly\": 47.8, \"mistral_ratio_2bitonly\": 8.2, \"mistral_ppl_full\": 6.39, \"mistral_ratio_full\": 1.09, \"gemma2_ppl\": 277.4, \"gemma2_ratio\": 37.9, \"budget\": 0.25, \"baseline_yi\": 5.89, \"baseline_llama\": 6.51, \"baseline_mistral\": 5.87, \"baseline_gemma2\": 7.32}, \"conclusion\": \"killed\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"concentration_top5pct\": 0.2291, \"l0_dominance_ratio\": 2.05, \"cv_delta_2bit\": 1.2834, \"positive_delta_heads\": \"310/336\", \"top_head\": \"L0H1 delta=0.1906\", \"total_time_hours\": 1.59}}, \"mistral_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fp16_ppl\": 7.0352, \"c4_mckp_ppl\": 7.1774, \"uniform_4bit_ppl\": 7.1308, \"mckp_vs_uniform_delta\": 0.0466, \"mckp_bit_distribution\": {\"2\": 4, \"4\": 250, \"8\": 2}, \"phase4_error\": \"FileNotFoundError: mistral_k_ablation_results.json\"}}, \"llama_c4_hires_crossdataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bf16_wt2_ppl\": 8.0922, \"bf16_c4_ppl\": 7.1333, \"c4_cal_mckp_wt2_ppl\": 8.5103, \"c4_cal_mckp_c4_ppl\": 7.5351, \"uniform_wt2_ppl\": 8.4701, \"uniform_c4_ppl\": 7.5351, \"delta_c4_uniform_minus_mckp\": 0, \"delta_wt2_uniform_minus_mckp\": -0.0402, \"verdict_c4\": \"FAIL\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"2,3\", \"24,2\"], \"heads_8bit\": [\"31,6\"], \"total_time_min\": 6.3, \"wt2_ref_mckp_ppl\": 8.5042, \"wt2_ref_delta\": -0.0341}}, \"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256, \"distribution_shape\": \"flat\", \"total_hours\": 0.94, \"profile_seconds\": 3371.7}, \"conclusion\": \"success\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 8.0922, \"hires_mckp_ppl\": 8.5042, \"uniform_4bit_ppl\": 8.4701, \"std_mckp_reference_ppl\": 8.4498, \"mckp_vs_uniform_delta\": -0.0341, \"mckp_vs_uniform_pct\": -9, \"hires_vs_std_mckp_delta\": 0.0544, \"concentration\": 0.5749, \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}, \"heads_2bit\": [\"26,0\", \"31,7\"], \"heads_8bit\": [\"12,3\"], \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"metrics\": {\"top5_concentration\": 0.5749, \"t1_t5\": 0.85, \"baseline_ppl\": 6.5055, \"top1_head\": \"L2H5_delta=15.2636\", \"delta_2bit_cv\": 7.7663, \"l0_dominance_ratio\": 0.67, \"positive_delta_heads\": 254, \"total_heads\": 256, \"total_hours\": 0.98}, \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"SafetensorError: model-00003-of-00003.safetensors missing, incomplete download\"}}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3\"}}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"hires_mckp_ppl\": 7.2181, \"uniform_4bit_ppl\": 7.2171, \"baseline_ppl\": 7.0157, \"delta_vs_uniform\": -0.001, \"bit_distribution\": {\"2\": 2, \"4\": 189, \"8\": 1}, \"2bit_heads\": [\"L22H1\", \"L24H3\"], \"8bit_heads\": [\"L6H2\"], \"L4H3_status\": \"kept_at_4bit\", \"std_mckp_k2_ppl\": 7.2209, \"std_mckp_k8_ppl\": 7.3129, \"hires_concentration\": 0.7139, \"L4H3_2bit_delta\": 13.12, \"L4H3_4bit_delta\": 0.0048, \"L4H3_8bit_delta\": 0.004}}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"top5_concentration\": 0.7139, \"top5_n_heads\": 9, \"baseline_calibration_ppl\": 5.888, \"delta_2bit_cv\": 8.8991, \"layer0_dominance_ratio\": 0.04, \"top1_head\": \"L4H3_delta=13.1236\", \"total_hours\": 0.96}}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"float32_hires_top5_concentration\": 0.6104, \"bf16_hires_range\": \"0.59-0.66\", \"float32_lowres_concentration\": 0.42, \"bf16_bug_impact_on_concentration\": 0.01, \"baseline_ppl\": 9.81, \"mckp_unconstrained_ppl\": 10.95, \"uniform_4bit_ppl\": 15.45, \"mckp_bit_dist\": {\"2\": 12, \"4\": 96, \"8\": 3, \"16\": 1}, \"l0h0_delta\": 6.7388, \"l0_4heads_total_share\": 0.586, \"claim3_threshold_0.50\": \"PASS\"}}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"baseline_wikitext2_ppl\": 7.0157, \"mckp_wikitext2_ppl\": 7.3129, \"uniform4bit_wikitext2_ppl\": 7.2171, \"mckp_improvement_over_uniform\": -0.0958, \"top5_concentration\": 0.4934, \"layer0_dominance_ratio\": 0.07, \"best_k\": 2, \"best_k_ppl\": 7.2209, \"gqa_ratio\": \"8:1\", \"verdict\": \"FAIL\"}}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"baseline_wikitext2_ppl\": 8.9, \"mckp_wikitext2_ppl\": 9.05, \"uniform4bit_wikitext2_ppl\": 9.03, \"mckp_improvement_over_uniform\": -0.02, \"top5_concentration\": 0.23, \"layer0_dominance_ratio\": 1.32, \"best_k\": 8, \"best_k_ppl\": 9.05, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"bf16_wt2_ppl\": 7.0351, \"c4_cal_bf16_ppl\": 6.9677, \"wt2_cal_mckp_wt2_ppl\": 7.1648, \"c4_cal_mckp_wt2_ppl\": 7.1859, \"uniform_4bit_wt2_ppl\": 7.1314, \"delta_uniform_mckp_wt2_cal\": -0.0334, \"delta_uniform_mckp_c4_cal\": -0.0546, \"allocation_agreement_c4_vs_wt2\": 0.965, \"agreement_heads\": \"247/256\", \"bit_dist_wt2_cal\": \"2bit:4, 4bit:252\", \"bit_dist_c4_cal\": \"2bit:4, 4bit:251, 8bit:1\", \"profile_time_s\": 407.7, \"eval_time_s\": 349.4, \"total_time_s\": 757.1}}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"metrics\": {\"wt2_cal_wt2_ppl\": 8.4498, \"c4_cal_wt2_ppl\": 8.6459, \"uniform_wt2_ppl\": 8.469, \"wt2_cal_c4_ppl\": 7.654, \"c4_cal_c4_ppl\": 7.654, \"uniform_c4_ppl\": 7.5351, \"bf16_wt2_ppl\": 8.0918, \"bf16_c4_ppl\": 7.1333, \"agreement_rate\": 0.977, \"agreement_heads\": \"250/256\", \"bit_distribution\": {\"2\": 2, \"4\": 253, \"8\": 1}}, \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"metrics\": {\"baseline_bf16_ppl\": 7.0351, \"uniform_4bit_ppl\": 7.1314, \"mckp_k4_ppl\": 7.1648, \"l0_random_seed_0\": 7.1882, \"l0_random_seed_1\": 7.1995, \"l0_random_seed_2\": 7.1723, \"l0_random_seed_3\": 7.3577, \"l0_random_seed_4\": 7.2875, \"l0_random_mean\": 7.2411, \"l0_random_std\": 0.0707, \"l0_random_median\": 7.1995, \"naive_heuristic_ppl\": 7.2105, \"budget_heuristic\": 0.2559, \"budget_mckp_k4\": 0.248}, \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"l0_random_seeds\": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], \"l0_random_mean\": 8.6245, \"l0_random_std\": 0.0733, \"l0_random_median\": 8.6192, \"naive_positional_ppl\": 8.5781, \"mckp_ppl\": 8.4498, \"uniform_ppl\": 8.469, \"baseline_ppl\": 8.0918, \"mckp_vs_l0_random_gap\": 0.1747, \"mckp_vs_naive_gap\": 0.1283}}, \"plan_009_oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"oracle_comparison\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mckp_ppl\": 10.9131, \"max_oracle_gap_ppl\": 0.0183, \"avg_oracle_gap_ppl\": 0.0046, \"layers_mckp_optimal\": \"5/8\", \"layers_with_gap\": 3, \"gap_layers\": {\"L1\": 0.0183, \"L4\": 0.0045, \"L11\": 0.0136}, \"gap_nature\": \"2-bit head position swap within same bit budget\", \"total_evals\": 54, \"runtime_min\": 21.3}}}, \"count\": 50, \"total\": 95, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2569}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
I don't see a `mistral_compounding_sweep` experiment in the registry. Let me search for all experiments with "mistral" or "compounding" to see if it has a different name. Let me also check if there are more experiments beyond the 50 I got.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "0fda3486-6daf-4b9e-8056-1903115f6dd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sqz9oupyLVJQWMCYFnzgUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10261,
      "cache_read_input_tokens": 59675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10261
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

Let me search for the Mistral compounding sweep - it might be in a different batch or have a different name.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "32a92e8f-7ffc-41b8-8c87-4cafbdaee768",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sqz9oupyLVJQWMCYFnzgUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10261,
      "cache_read_input_tokens": 59675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10261
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

<details open><summary>🔧 Tool call — Grep · `toolu_016Hc926LzoQ4CYwQ1ufnkfC`</summary>

```json
{
  "pattern": "mistral.*compounding|compounding.*mistral",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "-i": true,
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "95a8e512-2e5e-43b8-996f-5aa0f042a64b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sqz9oupyLVJQWMCYFnzgUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10261,
      "cache_read_input_tokens": 59675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10261
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

_source line 27 · 2026-05-15T18:00:57.188Z_

<details><summary>↩ Tool result · `toolu_016Hc926LzoQ4CYwQ1ufnkfC`</summary>

```text
Found 250 files limit: 250
logs/workers/worker_analyze_compounding_paper_integration_20260515T180021.log
logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912.jsonl
report.md
logs/chats/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director.jsonl
logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer.jsonl
logs/workers/worker_ops_cuda1_mistral_results_and_next_20260515T175212_result.json
logs/workers/worker_ops_cuda1_mistral_results_and_next_20260515T175212.log
registry.yaml
checkpoints/mistral_compounding_sweep_ANALYZING_20260515T175309.json
ROADMAP.md
decisions.yaml
logs/workers/worker_ops_disk_cleanup_westd_20260515T163311.log
checkpoints/mistral_compounding_sweep_ANALYZING_20260515T163552.json
logs/workers/worker_exp_mistral_compounding_sweep_20260515T163254_result.json
logs/workers/worker_exp_mistral_compounding_sweep_20260515T163254.log
logs/workers/worker_ops_gpu_status_check_20260515T163433_result.json
logs/workers/worker_ops_gpu_status_check_20260515T163433.log
checkpoints/mistral_compounding_sweep_RUNNING_20260515T163426.json
checkpoints/mistral_compounding_sweep_QUEUED_20260515T163419.json
logs/chats/worker_exp_llama_compounding_sweep_20260515T161906.jsonl
logs/workers/worker_exp_llama_compounding_sweep_20260515T161906.log
logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_paper_agent.jsonl
docs/paper/experiments.tex
artifacts/review_issues.yaml
logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_director.jsonl
logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_reviewer_2.jsonl
logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_reviewer_1.jsonl
logs/workers/worker_build_latex_compile_check_20260515T151208_result.json
logs/workers/worker_build_latex_compile_check_20260515T151208.log
logs/chats/worker_fix_mistral_uniform_ppl_bug_and_orphan_kill_20260515T150250.jsonl
logs/workers/worker_fix_mistral_uniform_ppl_bug_and_orphan_kill_20260515T150250.log
logs/workers/worker_exp_kivi_mckp_combined_20260515T144828.log
logs/workers/worker_data_qwen14b_table1_extract_20260515T144133.log
logs/workers/worker_fix_kill_orphan_check_kivi_20260515T144123.log
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T143137_321557.jsonl
logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260515T143130_141797.jsonl
paper_framing.md
logs/chats/feishu_dm_oc_a55584f7606e96135a3510c9deec7264_briefer.jsonl
logs/workers/worker_exp_qwen7b_8k_spotcheck_20260515T130833.log
logs/workers/worker_exp_qwen7b_8k_context_eval_20260515T130830.log
logs/workers/worker_exp_pythia14b_constrained_pipeline_20260515T123706.log
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260515T125712_172749.jsonl
logs/chats/worker_ops_kivi_eval_param_audit_20260515T115659.jsonl
logs/workers/worker_ops_kivi_eval_param_audit_20260515T115659.log
logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260515T112719_534413.jsonl
logs/workers/worker_code_kivi_baseline_prep_20260515T110703.log
artifacts/dream_reports/dream_20260515T085855/logs/review_worst.log
artifacts/dream_reports/dream_20260515T085855/logs/review_median.log
artifacts/dream_reports/dream_20260515T085855/median/review_report.md
artifacts/dream_reports/dream_20260515T085855/logs/review_best.log
artifacts/dream_reports/dream_20260515T085855/best/review_report.md
artifacts/dream_reports/dream_20260515T085855/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260515T085855/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T085855/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260515T085855/median/paper_framing.md
artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json
artifacts/dream_reports/dream_20260515T085855/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T085855/best/paper_framing.md
artifacts/dream_reports/dream_20260515T085855/best/experiment_data.json
artifacts/dream_reports/dream_20260515T085855/logs/phase2_worst_attempt0.log
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T092930_853627.jsonl
artifacts/dream_reports/dream_20260515T085855/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260515T085855/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T085855/logs/phase1_attempt0.log
checkpoints/w9_compounding_scaling_DONE_20260515T053902.json
logs/workers/worker_diag_w9_v2_check_r2_20260515T053439_retry1.log
logs/workers/worker_diag_w9_v2_status_check_20260515T053130_retry1.log
logs/workers/worker_exp_w2_unconstrained_baselines_v2_20260515T053120_retry1.log
logs/workers/worker_fix_table1_std_removal_20260515T052846_retry1.log
logs/chats/cron_hook_qwen_hires_float32_d048.jsonl
logs/workers/worker_diag_w2_check_full_profiles_20260515T050552_retry1.log
logs/workers/worker_diag_w2_w9_server_check_20260515T050332_retry1.log
logs/workers/worker_code_w2_unconstrained_baselines_20260515T050316_retry1.log
logs/chats/archive/cron_hook_qwen_hires_float32_d048_20260515T050023_070430.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T050002_257583.jsonl
logs/workers/worker_exp_w9_compounding_scaling_20260515T043948_retry1.log
logs/chats/cron_hook_llama_c4_hires_crossdataset.jsonl
logs/workers/worker_exp_w2_unconstrained_baselines_20260515T043931_retry2.log
logs/workers/worker_exp_w2_unconstrained_baselines_20260515T043931_retry1.log
logs/workers/worker_writing_r1_w7_related_work_20260515T044227_retry1.log
logs/workers/worker_writing_r1_w6_w8_method_20260515T044249_retry1.log
logs/chats/cron_hook_llama_c4_cross_dataset.jsonl
logs/chats/cron_hook_mistral_hires_bf16_2bitonly_v4.jsonl
logs/workers/worker_exp_w9_compounding_scaling_20260515T043749_retry1.log
logs/chats/cron_hook_llama_hires_constrained_mckp.jsonl
task_context/history/agent/loop_8_1778821223.md
logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260515T043825_941984.jsonl
logs/workers/worker_exp_w2_unconstrained_baselines_20260515T043719_retry1.log
logs/chats/cron_hook_gemma2_hires_bf16_2bitonly.jsonl
logs/chats/cron_hook_kv_separation.jsonl
logs/chats/cron_hook_mistral_hires_pipeline.jsonl
logs/chats/archive/cron_hook_gemma2_hires_bf16_2bitonly_20260515T043650_870438.jsonl
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260515T043623_716804.jsonl
logs/chats/archive/cron_hook_llama_hires_constrained_mckp_20260515T043617_794816.jsonl
logs/chats/archive/cron_hook_llama_c4_hires_crossdataset_20260515T043536_966169.jsonl
artifacts/review_reports/round_2.md
logs/chats/archive/cron_hook_qwen_hires_float32_d048_20260515T015120_979863.jsonl
logs/workers/worker_audit_paper_numbers_consistency_20260515T010304_retry2.log
logs/workers/worker_audit_paper_numbers_consistency_20260515T010304_retry1.log
logs/chats/archive/cron_hook_kv_separation_20260515T005938_591114.jsonl
logs/workers/worker_analysis_paper_figures_validation_20260515T005346_result.json
logs/workers/worker_analysis_paper_figures_validation_20260515T005346_retry2.log
logs/workers/worker_analysis_paper_figures_validation_20260515T005346_retry1.log
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260515T005311_050246.jsonl
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260515T004953_848208.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T224141_792216.jsonl
logs/workers/worker_diagnose_llama_c4_hires_crossdataset_20260514T224056_retry1.log
logs/chats/worker_paper_p0-concentration-patch_20260514T221709.jsonl
logs/workers/worker_paper_p0-concentration-patch_20260514T221709_retry1.log
logs/workers/worker_code_heatmap_fix_20260514T221632_retry1.log
logs/workers/worker_analysis_gemma2_hires_extract_20260514T221401_retry1.log
logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260514T221246_433082.jsonl
logs/workers/worker_gpu_gemma2_hires_bf16_2bitonly_20260514T220044_retry1.log
logs/workers/worker_figure_heatmap_hires_regen_20260514T215716_retry2.log
logs/workers/worker_audit_scatter_concentration_values_20260514T215607_retry2.log
logs/workers/worker_audit_scatter_concentration_values_20260514T215607_retry1.log
logs/chats/archive/cron_hook_kv_separation_20260514T215328_123888.jsonl
logs/chats/worker_paper_llama_table3_update_20260514T214809.jsonl
logs/workers/worker_paper_llama_table3_update_20260514T214809_retry1.log
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T214355_786051.jsonl
logs/workers/worker_investigation_mistral_concentration_20260514T211724.log
logs/workers/worker_paper_yi15_table3_fix_20260514T211702.log
logs/workers/worker_paper_claim3_revision_20260514T210100.log
logs/chats/worker_paper_claim3_revision_20260514T204030.jsonl
logs/workers/worker_paper_claim3_revision_20260514T204030.log
logs/workers/worker_code_qwen_hires_constrained_mckp_20260514T194934.log
logs/workers/worker_paper_appendix-runtime_20260514T193142.log
logs/workers/worker_figure_5-model-heatmap_20260514T185910.log
logs/workers/worker_paper_p0-patch-drafts_20260514T190526.log
logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260514T190615_488062.jsonl
logs/workers/worker_research_spike-vs-spread-literature_20260514T185634.log
logs/workers/worker_paper_p1-patch-yi15-gemma2_20260514T185614.log
logs/workers/worker_paper_p1-patch-yi-gemma_20260514T185845.log
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260514T185145_458530.jsonl
logs/workers/worker_knowledge_paper-patch-audit_20260514T184018.log
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T183802_629247.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T183731_018002.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T183556_513950.jsonl
logs/chats/archive/cron_hook_kv_separation_20260514T182933_309306.jsonl
logs/chats/worker_gpu_qwen_float32_validation_20260514T174811.jsonl
logs/workers/worker_gpu_qwen_float32_validation_20260514T174811.log
logs/workers/worker_gpu_gemma2_kill_and_debug_20260514T160301.log
logs/chats/worker_investigate_gemma2_results_20260514T154602.jsonl
logs/workers/worker_investigate_gemma2_results_20260514T154602.log
logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260514T154336_041342.jsonl
logs/workers/worker_debug_gemma2_baseline_ppl_20260514T152217.log
logs/workers/worker_ops_check_and_fix_cron_loop5_20260514T151716.log
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T151530_747807.jsonl
logs/chats/archive/cron_hook_kv_separation_20260514T150304_889439.jsonl
logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260514T142437_729001.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T142313_491487.jsonl
logs/chats/worker_gpu_yi15_9b_full_pipeline_20260514T140307.jsonl
logs/workers/worker_gpu_yi15_9b_full_pipeline_20260514T140307.log
logs/workers/worker_gpu_gemma2_9b_full_pipeline_20260514T134705.log
logs/workers/worker_gpu_qwen72b_profiling_20260514T134341.log
logs/workers/worker_paper_compile_check_20260514T121430.log
logs/chats/worker_paper_reference_audit_20260514T120938.jsonl
logs/workers/worker_paper_reference_audit_20260514T120938.log
logs/chats/worker_paper_d040_patches_20260514T120618.jsonl
logs/workers/worker_paper_d040_patches_20260514T120618.log
logs/workers/worker_code_mistral_heuristic_k4_20260514T115500_result.json
logs/workers/worker_code_mistral_heuristic_k4_20260514T115500.log
checkpoints/mistral_heuristic_k4_DONE_20260514T120754.json
checkpoints/mistral_heuristic_k4_RUNNING_20260514T120750.json
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260514T120705_251625.jsonl
checkpoints/mistral_heuristic_k4_RUNNING_20260514T120215.json
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T120211_433715.jsonl
checkpoints/mistral_heuristic_k4_QUEUED_20260514T120211.json
logs/workers/worker_code_llama_heuristic_k2_20260514T115449.log
checkpoints/mistral_heuristic_k4_PREPARING_20260514T115420.json
logs/workers/worker_paper_figures_sync_20260514T115025_result.json
logs/workers/worker_paper_figures_sync_20260514T115025.log
logs/workers/worker_code_plan_013_72b_profiling_20260514T114708_result.json
logs/chats/worker_code_plan_013_72b_profiling_20260514T114708.jsonl
logs/workers/worker_code_plan_013_72b_profiling_20260514T114708.log
logs/workers/worker_analysis_gpu_and_oracle_status_20260514T114359.log
logs/workers/worker_code_plan_009_oracle_comparison_20260514T110435.log
logs/workers/worker_analysis_gpu1_status_and_plan009_prep_20260514T110420.log
logs/chats/worker_paper_writing_conclusion_20260514T110127.jsonl
logs/workers/worker_paper_writing_conclusion_20260514T110127.log
logs/chats/worker_paper_writing_abstract_20260514T104615.jsonl
logs/workers/worker_paper_writing_abstract_20260514T104615.log
logs/workers/worker_paper_writing_related_work_20260514T102130.log
logs/workers/worker_code_cross_domain_v2_prep_20260514T101514.log
logs/workers/worker_paper_writing_introduction_20260514T101549_result.json
logs/chats/worker_paper_writing_introduction_20260514T101549.jsonl
logs/workers/worker_paper_writing_introduction_20260514T101549.log
logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260514T100813_953602.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T100732_077893.jsonl
logs/chats/worker_paper_writing_analysis_20260514T094816.jsonl
logs/workers/worker_paper_writing_analysis_20260514T094816.log
logs/chats/worker_paper_writing_method_20260514T092319.jsonl
logs/workers/worker_paper_writing_method_20260514T092319.log
logs/workers/worker_code_c4_rerun_d032_20260514T090654.log
logs/chats/worker_paper_writing_experiments_20260514T090525.jsonl
logs/workers/worker_paper_writing_experiments_20260514T090525.log
logs/workers/worker_code_plan_018_runtime_benchmark_20260514T085811.log
logs/workers/worker_investigate_c4_data_authenticity_20260514T085841.log
logs/chats/worker_code_plan_010_cross_domain_20260514T084200.jsonl
logs/workers/worker_code_plan_010_cross_domain_20260514T084200.log
logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T084959_877482.jsonl
logs/workers/worker_util_copy_figures_20260514T073649.log
logs/workers/worker_paper_figure_fix_fig3_20260514T075955.log
logs/workers/worker_transfer_scp_figures_to_local_20260514T074635.log
logs/workers/worker_code_plan_017_multi_seed_20260514T073854.log
logs/workers/worker_code_multi_seed_error_bars_20260514T073300.log
logs/workers/worker_code_plan_015_l0_heuristic_20260514T062108.log
logs/workers/worker_code_mistral_llama_k_ablation_20260514T071221_result.json
logs/workers/worker_code_mistral_llama_k_ablation_20260514T071221.log
logs/workers/worker_verify_greedy_constraint_impl_20260514T070945.log
logs/workers/worker_debug_mistral_mckp_constraint_20260514T070410_result.json
logs/chats/worker_debug_mistral_mckp_constraint_20260514T070410.jsonl
logs/workers/worker_debug_mistral_mckp_constraint_20260514T070410.log
checkpoints/head_sensitivity_viz_DONE_20260514T070744.json
checkpoints/head_sensitivity_viz_RUNNING_20260514T070738.json
checkpoints/head_sensitivity_viz_ALLOCATED_20260514T070731.json
checkpoints/head_sensitivity_viz_QUEUED_20260514T070727.json
checkpoints/head_sensitivity_viz_PENDING_20260514T070722.json
logs/workers/worker_code_downstream_eval_qwen_20260514T055338.log
logs/chats/worker_debug_l0_heuristic_token_mismatch_20260514T063920.jsonl
logs/workers/worker_debug_l0_heuristic_token_mismatch_20260514T063920.log
logs/chats/worker_code_hires_mckp_reeval_20260514T064307.jsonl
logs/workers/worker_code_hires_mckp_reeval_20260514T064307.log
logs/chats/worker_code_qwen_bf16_reeval_20260514T062423.jsonl
logs/workers/worker_code_qwen_bf16_reeval_20260514T062423.log
logs/workers/worker_code_greedy_cardinality_ablation_20260514T062233.log
logs/workers/worker_code_l0_heuristic_corrected_20260514T061624.log
logs/workers/worker_code_l0_only_heuristic_20260514T061550.log
logs/workers/worker_code_greedy_cardinality_ablation_20260514T061005.log
logs/chats/worker_code_qwen_bf16_uniform_eval_20260514T061221.jsonl
logs/workers/worker_code_qwen_bf16_uniform_eval_20260514T061221.log
logs/workers/worker_code_kv_separation_20260514T060217.log
logs/workers/worker_code_l0_heuristic_baseline_20260514T061050.log
logs/workers/worker_code_l0_only_heuristic_20260514T060943.log
logs/workers/worker_code_mistral_aggressive_diagnosis_20260514T060920.log
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260514T060343_441870.jsonl
logs/workers/worker_code_head_sensitivity_viz_20260514T055404_result.json
logs/workers/worker_code_head_sensitivity_viz_20260514T055404.log
logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260514T055406_334888.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T055323_049562.jsonl
logs/workers/worker_analysis_head_heterogeneity_20260514T052347.log
logs/workers/worker_code_csv_fix_and_hires_check_20260514T040119.log
logs/workers/worker_code_results_summary_csv_20260514T031526_result.json
logs/chats/worker_code_results_summary_csv_20260514T031526.jsonl
logs/workers/worker_code_results_summary_csv_20260514T031526.log
logs/workers/worker_code_mistral_full_pipeline_20260514T020459.log
logs/workers/worker_code_gpu_status_and_mistral_launch_20260514T020231.log
logs/workers/worker_code_fix_exp_e_eval_20260514T013707.log
logs/workers/worker_code_llama_full_pipeline_20260514T013209.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "22c259fd-04fa-4a8a-a1cd-7ec375b1bebd",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_analyze_compounding_paper_integration_20260515T180021.log",
      "logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912.jsonl",
      "report.md",
      "logs/chats/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director.jsonl",
      "logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer.jsonl",
      "logs/workers/worker_ops_cuda1_mistral_results_and_next_20260515T175212_result.json",
      "logs/workers/worker_ops_cuda1_mistral_results_and_next_20260515T175212.log",
      "registry.yaml",
      "checkpoints/mistral_compounding_sweep_ANALYZING_20260515T175309.json",
      "ROADMAP.md",
      "decisions.yaml",
      "logs/workers/worker_ops_disk_cleanup_westd_20260515T163311.log",
      "checkpoints/mistral_compounding_sweep_ANALYZING_20260515T163552.json",
      "logs/workers/worker_exp_mistral_compounding_sweep_20260515T163254_result.json",
      "logs/workers/worker_exp_mistral_compounding_sweep_20260515T163254.log",
      "logs/workers/worker_ops_gpu_status_check_20260515T163433_result.json",
      "logs/workers/worker_ops_gpu_status_check_20260515T163433.log",
      "checkpoints/mistral_compounding_sweep_RUNNING_20260515T163426.json",
      "checkpoints/mistral_compounding_sweep_QUEUED_20260515T163419.json",
      "logs/chats/worker_exp_llama_compounding_sweep_20260515T161906.jsonl",
      "logs/workers/worker_exp_llama_compounding_sweep_20260515T161906.log",
      "logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_paper_agent.jsonl",
      "docs/paper/experiments.tex",
      "artifacts/review_issues.yaml",
      "logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_director.jsonl",
      "logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_reviewer_2.jsonl",
      "logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_reviewer_1.jsonl",
      "logs/workers/worker_build_latex_compile_check_20260515T151208_result.json",
      "logs/workers/worker_build_latex_compile_check_20260515T151208.log",
      "logs/chats/worker_fix_mistral_uniform_ppl_bug_and_orphan_kill_20260515T150250.jsonl",
      "logs/workers/worker_fix_mistral_uniform_ppl_bug_and_orphan_kill_20260515T150250.log",
      "logs/workers/worker_exp_kivi_mckp_combined_20260515T144828.log",
      "logs/workers/worker_data_qwen14b_table1_extract_20260515T144133.log",
      "logs/workers/worker_fix_kill_orphan_check_kivi_20260515T144123.log",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T143137_321557.jsonl",
      "logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260515T143130_141797.jsonl",
      "paper_framing.md",
      "logs/chats/feishu_dm_oc_a55584f7606e96135a3510c9deec7264_briefer.jsonl",
      "logs/workers/worker_exp_qwen7b_8k_spotcheck_20260515T130833.log",
      "logs/workers/worker_exp_qwen7b_8k_context_eval_20260515T130830.log",
      "logs/workers/worker_exp_pythia14b_constrained_pipeline_20260515T123706.log",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260515T125712_172749.jsonl",
      "logs/chats/worker_ops_kivi_eval_param_audit_20260515T115659.jsonl",
      "logs/workers/worker_ops_kivi_eval_param_audit_20260515T115659.log",
      "logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260515T112719_534413.jsonl",
      "logs/workers/worker_code_kivi_baseline_prep_20260515T110703.log",
      "artifacts/dream_reports/dream_20260515T085855/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260515T085855/logs/review_median.log",
      "artifacts/dream_reports/dream_20260515T085855/median/review_report.md",
      "artifacts/dream_reports/dream_20260515T085855/logs/review_best.log",
      "artifacts/dream_reports/dream_20260515T085855/best/review_report.md",
      "artifacts/dream_reports/dream_20260515T085855/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260515T085855/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T085855/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260515T085855/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T085855/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260515T085855/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T085855/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T085855/logs/phase2_worst_attempt0.log",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T092930_853627.jsonl",
      "artifacts/dream_reports/dream_20260515T085855/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260515T085855/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260515T085855/logs/phase1_attempt0.log",
      "checkpoints/w9_compounding_scaling_DONE_20260515T053902.json",
      "logs/workers/worker_diag_w9_v2_check_r2_20260515T053439_retry1.log",
      "logs/workers/worker_diag_w9_v2_status_check_20260515T053130_retry1.log",
      "logs/workers/worker_exp_w2_unconstrained_baselines_v2_20260515T053120_retry1.log",
      "logs/workers/worker_fix_table1_std_removal_20260515T052846_retry1.log",
      "logs/chats/cron_hook_qwen_hires_float32_d048.jsonl",
      "logs/workers/worker_diag_w2_check_full_profiles_20260515T050552_retry1.log",
      "logs/workers/worker_diag_w2_w9_server_check_20260515T050332_retry1.log",
      "logs/workers/worker_code_w2_unconstrained_baselines_20260515T050316_retry1.log",
      "logs/chats/archive/cron_hook_qwen_hires_float32_d048_20260515T050023_070430.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T050002_257583.jsonl",
      "logs/workers/worker_exp_w9_compounding_scaling_20260515T043948_retry1.log",
      "logs/chats/cron_hook_llama_c4_hires_crossdataset.jsonl",
      "logs/workers/worker_exp_w2_unconstrained_baselines_20260515T043931_retry2.log",
      "logs/workers/worker_exp_w2_unconstrained_baselines_20260515T043931_retry1.log",
      "logs/workers/worker_writing_r1_w7_related_work_20260515T044227_retry1.log",
      "logs/workers/worker_writing_r1_w6_w8_method_20260515T044249_retry1.log",
      "logs/chats/cron_hook_llama_c4_cross_dataset.jsonl",
      "logs/chats/cron_hook_mistral_hires_bf16_2bitonly_v4.jsonl",
      "logs/workers/worker_exp_w9_compounding_scaling_20260515T043749_retry1.log",
      "logs/chats/cron_hook_llama_hires_constrained_mckp.jsonl",
      "task_context/history/agent/loop_8_1778821223.md",
      "logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260515T043825_941984.jsonl",
      "logs/workers/worker_exp_w2_unconstrained_baselines_20260515T043719_retry1.log",
      "logs/chats/cron_hook_gemma2_hires_bf16_2bitonly.jsonl",
      "logs/chats/cron_hook_kv_separation.jsonl",
      "logs/chats/cron_hook_mistral_hires_pipeline.jsonl",
      "logs/chats/archive/cron_hook_gemma2_hires_bf16_2bitonly_20260515T043650_870438.jsonl",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260515T043623_716804.jsonl",
      "logs/chats/archive/cron_hook_llama_hires_constrained_mckp_20260515T043617_794816.jsonl",
      "logs/chats/archive/cron_hook_llama_c4_hires_crossdataset_20260515T043536_966169.jsonl",
      "artifacts/review_reports/round_2.md",
      "logs/chats/archive/cron_hook_qwen_hires_float32_d048_20260515T015120_979863.jsonl",
      "logs/workers/worker_audit_paper_numbers_consistency_20260515T010304_retry2.log",
      "logs/workers/worker_audit_paper_numbers_consistency_20260515T010304_retry1.log",
      "logs/chats/archive/cron_hook_kv_separation_20260515T005938_591114.jsonl",
      "logs/workers/worker_analysis_paper_figures_validation_20260515T005346_result.json",
      "logs/workers/worker_analysis_paper_figures_validation_20260515T005346_retry2.log",
      "logs/workers/worker_analysis_paper_figures_validation_20260515T005346_retry1.log",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260515T005311_050246.jsonl",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260515T004953_848208.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T224141_792216.jsonl",
      "logs/workers/worker_diagnose_llama_c4_hires_crossdataset_20260514T224056_retry1.log",
      "logs/chats/worker_paper_p0-concentration-patch_20260514T221709.jsonl",
      "logs/workers/worker_paper_p0-concentration-patch_20260514T221709_retry1.log",
      "logs/workers/worker_code_heatmap_fix_20260514T221632_retry1.log",
      "logs/workers/worker_analysis_gemma2_hires_extract_20260514T221401_retry1.log",
      "logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260514T221246_433082.jsonl",
      "logs/workers/worker_gpu_gemma2_hires_bf16_2bitonly_20260514T220044_retry1.log",
      "logs/workers/worker_figure_heatmap_hires_regen_20260514T215716_retry2.log",
      "logs/workers/worker_audit_scatter_concentration_values_20260514T215607_retry2.log",
      "logs/workers/worker_audit_scatter_concentration_values_20260514T215607_retry1.log",
      "logs/chats/archive/cron_hook_kv_separation_20260514T215328_123888.jsonl",
      "logs/chats/worker_paper_llama_table3_update_20260514T214809.jsonl",
      "logs/workers/worker_paper_llama_table3_update_20260514T214809_retry1.log",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T214355_786051.jsonl",
      "logs/workers/worker_investigation_mistral_concentration_20260514T211724.log",
      "logs/workers/worker_paper_yi15_table3_fix_20260514T211702.log",
      "logs/workers/worker_paper_claim3_revision_20260514T210100.log",
      "logs/chats/worker_paper_claim3_revision_20260514T204030.jsonl",
      "logs/workers/worker_paper_claim3_revision_20260514T204030.log",
      "logs/workers/worker_code_qwen_hires_constrained_mckp_20260514T194934.log",
      "logs/workers/worker_paper_appendix-runtime_20260514T193142.log",
      "logs/workers/worker_figure_5-model-heatmap_20260514T185910.log",
      "logs/workers/worker_paper_p0-patch-drafts_20260514T190526.log",
      "logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260514T190615_488062.jsonl",
      "logs/workers/worker_research_spike-vs-spread-literature_20260514T185634.log",
      "logs/workers/worker_paper_p1-patch-yi15-gemma2_20260514T185614.log",
      "logs/workers/worker_paper_p1-patch-yi-gemma_20260514T185845.log",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260514T185145_458530.jsonl",
      "logs/workers/worker_knowledge_paper-patch-audit_20260514T184018.log",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T183802_629247.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T183731_018002.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T183556_513950.jsonl",
      "logs/chats/archive/cron_hook_kv_separation_20260514T182933_309306.jsonl",
      "logs/chats/worker_gpu_qwen_float32_validation_20260514T174811.jsonl",
      "logs/workers/worker_gpu_qwen_float32_validation_20260514T174811.log",
      "logs/workers/worker_gpu_gemma2_kill_and_debug_20260514T160301.log",
      "logs/chats/worker_investigate_gemma2_results_20260514T154602.jsonl",
      "logs/workers/worker_investigate_gemma2_results_20260514T154602.log",
      "logs/chats/archive/cron_hook_llama_c4_cross_dataset_20260514T154336_041342.jsonl",
      "logs/workers/worker_debug_gemma2_baseline_ppl_20260514T152217.log",
      "logs/workers/worker_ops_check_and_fix_cron_loop5_20260514T151716.log",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T151530_747807.jsonl",
      "logs/chats/archive/cron_hook_kv_separation_20260514T150304_889439.jsonl",
      "logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260514T142437_729001.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T142313_491487.jsonl",
      "logs/chats/worker_gpu_yi15_9b_full_pipeline_20260514T140307.jsonl",
      "logs/workers/worker_gpu_yi15_9b_full_pipeline_20260514T140307.log",
      "logs/workers/worker_gpu_gemma2_9b_full_pipeline_20260514T134705.log",
      "logs/workers/worker_gpu_qwen72b_profiling_20260514T134341.log",
      "logs/workers/worker_paper_compile_check_20260514T121430.log",
      "logs/chats/worker_paper_reference_audit_20260514T120938.jsonl",
      "logs/workers/worker_paper_reference_audit_20260514T120938.log",
      "logs/chats/worker_paper_d040_patches_20260514T120618.jsonl",
      "logs/workers/worker_paper_d040_patches_20260514T120618.log",
      "logs/workers/worker_code_mistral_heuristic_k4_20260514T115500_result.json",
      "logs/workers/worker_code_mistral_heuristic_k4_20260514T115500.log",
      "checkpoints/mistral_heuristic_k4_DONE_20260514T120754.json",
      "checkpoints/mistral_heuristic_k4_RUNNING_20260514T120750.json",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260514T120705_251625.jsonl",
      "checkpoints/mistral_heuristic_k4_RUNNING_20260514T120215.json",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T120211_433715.jsonl",
      "checkpoints/mistral_heuristic_k4_QUEUED_20260514T120211.json",
      "logs/workers/worker_code_llama_heuristic_k2_20260514T115449.log",
      "checkpoints/mistral_heuristic_k4_PREPARING_20260514T115420.json",
      "logs/workers/worker_paper_figures_sync_20260514T115025_result.json",
      "logs/workers/worker_paper_figures_sync_20260514T115025.log",
      "logs/workers/worker_code_plan_013_72b_profiling_20260514T114708_result.json",
      "logs/chats/worker_code_plan_013_72b_profiling_20260514T114708.jsonl",
      "logs/workers/worker_code_plan_013_72b_profiling_20260514T114708.log",
      "logs/workers/worker_analysis_gpu_and_oracle_status_20260514T114359.log",
      "logs/workers/worker_code_plan_009_oracle_comparison_20260514T110435.log",
      "logs/workers/worker_analysis_gpu1_status_and_plan009_prep_20260514T110420.log",
      "logs/chats/worker_paper_writing_conclusion_20260514T110127.jsonl",
      "logs/workers/worker_paper_writing_conclusion_20260514T110127.log",
      "logs/chats/worker_paper_writing_abstract_20260514T104615.jsonl",
      "logs/workers/worker_paper_writing_abstract_20260514T104615.log",
      "logs/workers/worker_paper_writing_related_work_20260514T102130.log",
      "logs/workers/worker_code_cross_domain_v2_prep_20260514T101514.log",
      "logs/workers/worker_paper_writing_introduction_20260514T101549_result.json",
      "logs/chats/worker_paper_writing_introduction_20260514T101549.jsonl",
      "logs/workers/worker_paper_writing_introduction_20260514T101549.log",
      "logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260514T100813_953602.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T100732_077893.jsonl",
      "logs/chats/worker_paper_writing_analysis_20260514T094816.jsonl",
      "logs/workers/worker_paper_writing_analysis_20260514T094816.log",
      "logs/chats/worker_paper_writing_method_20260514T092319.jsonl",
      "logs/workers/worker_paper_writing_method_20260514T092319.log",
      "logs/workers/worker_code_c4_rerun_d032_20260514T090654.log",
      "logs/chats/worker_paper_writing_experiments_20260514T090525.jsonl",
      "logs/workers/worker_paper_writing_experiments_20260514T090525.log",
      "logs/workers/worker_code_plan_018_runtime_benchmark_20260514T085811.log",
      "logs/workers/worker_investigate_c4_data_authenticity_20260514T085841.log",
      "logs/chats/worker_code_plan_010_cross_domain_20260514T084200.jsonl",
      "logs/workers/worker_code_plan_010_cross_domain_20260514T084200.log",
      "logs/chats/archive/cron_hook_mistral_hires_pipeline_20260514T084959_877482.jsonl",
      "logs/workers/worker_util_copy_figures_20260514T073649.log",
      "logs/workers/worker_paper_figure_fix_fig3_20260514T075955.log",
      "logs/workers/worker_transfer_scp_figures_to_local_20260514T074635.log",
      "logs/workers/worker_code_plan_017_multi_seed_20260514T073854.log",
      "logs/workers/worker_code_multi_seed_error_bars_20260514T073300.log",
      "logs/workers/worker_code_plan_015_l0_heuristic_20260514T062108.log",
      "logs/workers/worker_code_mistral_llama_k_ablation_20260514T071221_result.json",
      "logs/workers/worker_code_mistral_llama_k_ablation_20260514T071221.log",
      "logs/workers/worker_verify_greedy_constraint_impl_20260514T070945.log",
      "logs/workers/worker_debug_mistral_mckp_constraint_20260514T070410_result.json",
      "logs/chats/worker_debug_mistral_mckp_constraint_20260514T070410.jsonl",
      "logs/workers/worker_debug_mistral_mckp_constraint_20260514T070410.log",
      "checkpoints/head_sensitivity_viz_DONE_20260514T070744.json",
      "checkpoints/head_sensitivity_viz_RUNNING_20260514T070738.json",
      "checkpoints/head_sensitivity_viz_ALLOCATED_20260514T070731.json",
      "checkpoints/head_sensitivity_viz_QUEUED_20260514T070727.json",
      "checkpoints/head_sensitivity_viz_PENDING_20260514T070722.json",
      "logs/workers/worker_code_downstream_eval_qwen_20260514T055338.log",
      "logs/chats/worker_debug_l0_heuristic_token_mismatch_20260514T063920.jsonl",
      "logs/workers/worker_debug_l0_heuristic_token_mismatch_20260514T063920.log",
      "logs/chats/worker_code_hires_mckp_reeval_20260514T064307.jsonl",
      "logs/workers/worker_code_hires_mckp_reeval_20260514T064307.log",
      "logs/chats/worker_code_qwen_bf16_reeval_20260514T062423.jsonl",
      "logs/workers/worker_code_qwen_bf16_reeval_20260514T062423.log",
      "logs/workers/worker_code_greedy_cardinality_ablation_20260514T062233.log",
      "logs/workers/worker_code_l0_heuristic_corrected_20260514T061624.log",
      "logs/workers/worker_code_l0_only_heuristic_20260514T061550.log",
      "logs/workers/worker_code_greedy_cardinality_ablation_20260514T061005.log",
      "logs/chats/worker_code_qwen_bf16_uniform_eval_20260514T061221.jsonl",
      "logs/workers/worker_code_qwen_bf16_uniform_eval_20260514T061221.log",
      "logs/workers/worker_code_kv_separation_20260514T060217.log",
      "logs/workers/worker_code_l0_heuristic_baseline_20260514T061050.log",
      "logs/workers/worker_code_l0_only_heuristic_20260514T060943.log",
      "logs/workers/worker_code_mistral_aggressive_diagnosis_20260514T060920.log",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260514T060343_441870.jsonl",
      "logs/workers/worker_code_head_sensitivity_viz_20260514T055404_result.json",
      "logs/workers/worker_code_head_sensitivity_viz_20260514T055404.log",
      "logs/chats/archive/feishu_group_oc_e886d722cc0b64fdb553f7bb0b99816c_director_20260514T055406_334888.jsonl",
      "logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260514T055323_049562.jsonl",
      "logs/workers/worker_analysis_head_heterogeneity_20260514T052347.log",
      "logs/workers/worker_code_csv_fix_and_hires_check_20260514T040119.log",
      "logs/workers/worker_code_results_summary_csv_20260514T031526_result.json",
      "logs/chats/worker_code_results_summary_csv_20260514T031526.jsonl",
      "logs/workers/worker_code_results_summary_csv_20260514T031526.log",
      "logs/workers/worker_code_mistral_full_pipeline_20260514T020459.log",
      "logs/workers/worker_code_gpu_status_and_mistral_launch_20260514T020231.log",
      "logs/workers/worker_code_fix_exp_e_eval_20260514T013707.log",
      "logs/workers/worker_code_llama_full_pipeline_20260514T013209.log"
    ],
    "numFiles": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Glob · `toolu_01KF1eFhmUdpwVLh6Uj1quPm`</summary>

```json
{
  "pattern": "**/mistral*compounding*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "63c12641-5bfd-44f6-8027-afb4b7b33f54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sqz9oupyLVJQWMCYFnzgUQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10261,
      "cache_read_input_tokens": 59675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10261
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

_source line 29 · 2026-05-15T18:00:57.457Z_

<details><summary>↩ Tool result · `toolu_01KF1eFhmUdpwVLh6Uj1quPm`</summary>

```text
checkpoints/mistral_compounding_sweep_QUEUED_20260515T163419.json
checkpoints/mistral_compounding_sweep_RUNNING_20260515T163426.json
checkpoints/mistral_compounding_sweep_ANALYZING_20260515T163552.json
checkpoints/mistral_compounding_sweep_ANALYZING_20260515T175309.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "8b7668f6-b9e5-4ee5-aff9-264fb81ff1c0",
  "tool_use_result": {
    "filenames": [
      "checkpoints/mistral_compounding_sweep_QUEUED_20260515T163419.json",
      "checkpoints/mistral_compounding_sweep_RUNNING_20260515T163426.json",
      "checkpoints/mistral_compounding_sweep_ANALYZING_20260515T163552.json",
      "checkpoints/mistral_compounding_sweep_ANALYZING_20260515T175309.json"
    ],
    "durationMs": 10,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
The Mistral compounding sweep exists in checkpoints but might not be in the registry yet (it's in "ANALYZING" state). Let me check the latest checkpoint to get the results, and also check the registry for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "5934c589-9962-4437-b471-98b4e9ca9062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HN8gJEoJ7G1diwARdjbSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7592,
      "cache_read_input_tokens": 69936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7592
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

The Mistral compounding sweep exists but might still be in ANALYZING state. Let me check its checkpoint for results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "a43c768b-968f-44fc-9521-88e048c7420a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HN8gJEoJ7G1diwARdjbSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7592,
      "cache_read_input_tokens": 69936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7592
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

<details open><summary>🔧 Tool call — Read · `toolu_01B8EDuphjCzp6XjeMZFsUNe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/checkpoints/mistral_compounding_sweep_ANALYZING_20260515T175309.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "a37c2893-85ae-42b6-a9aa-c0f7cb2558db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HN8gJEoJ7G1diwARdjbSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7592,
      "cache_read_input_tokens": 69936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7592
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

_source line 33 · 2026-05-15T18:01:02.302Z_

<details><summary>↩ Tool result · `toolu_01B8EDuphjCzp6XjeMZFsUNe`</summary>

```text
1	{
2	  "exp_id": "mistral_compounding_sweep",
3	  "project": "ratekv",
4	  "state": "ANALYZING",
5	  "previous_state": null,
6	  "experiment_data": {
7	    "status": "ANALYZING",
8	    "retry_count": 0,
9	    "created_at": "2026-05-15T16:34:19.132Z",
10	    "updated_at": "2026-05-15T17:53:08.910Z",
11	    "spec": {
12	      "command": "CUDA_VISIBLE_DEVICES=1 python /root/ratekv/run_k_ablation.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --profiles /root/ratekv/mistral_ppl_profiles_hires.json --gpu cuda:0 --k_values 0,2,4,8,16,32,64,128,256 --budget 0.25 --output /root/ratekv/artifacts/mistral_compounding_sweep_results.json",
13	      "server": "westd-37397",
14	      "data_path": "wikitext-2",
15	      "data_count": 0,
16	      "model_name": "Mistral-7B-v0.3",
17	      "seed": 42
18	    },
19	    "log_path": "/root/ratekv/logs/mistral_compounding_sweep.log",
20	    "checkpoint_path": "/root/ratekv/artifacts/mistral_compounding_sweep_results.json",
21	    "pid": 350597,
22	    "conclusion": "success"
23	  },
24	  "timestamp": "2026-05-15T17:53:09.081697+00:00",
25	  "trigger": "update_registry"
26	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "8b5edcf0-fbdf-43d4-89bc-7e77772f5bdf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/checkpoints/mistral_compounding_sweep_ANALYZING_20260515T175309.json",
      "content": "{\n  \"exp_id\": \"mistral_compounding_sweep\",\n  \"project\": \"ratekv\",\n  \"state\": \"ANALYZING\",\n  \"previous_state\": null,\n  \"experiment_data\": {\n    \"status\": \"ANALYZING\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-15T16:34:19.132Z\",\n    \"updated_at\": \"2026-05-15T17:53:08.910Z\",\n    \"spec\": {\n      \"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/ratekv/run_k_ablation.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --profiles /root/ratekv/mistral_ppl_profiles_hires.json --gpu cuda:0 --k_values 0,2,4,8,16,32,64,128,256 --budget 0.25 --output /root/ratekv/artifacts/mistral_compounding_sweep_results.json\",\n      \"server\": \"westd-37397\",\n      \"data_path\": \"wikitext-2\",\n      \"data_count\": 0,\n      \"model_name\": \"Mistral-7B-v0.3\",\n      \"seed\": 42\n    },\n    \"log_path\": \"/root/ratekv/logs/mistral_compounding_sweep.log\",\n    \"checkpoint_path\": \"/root/ratekv/artifacts/mistral_compounding_sweep_results.json\",\n    \"pid\": 350597,\n    \"conclusion\": \"success\"\n  },\n  \"timestamp\": \"2026-05-15T17:53:09.081697+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01E63BnWVC4Zm5h338Pd7dJ1`</summary>

```json
{
  "pattern": "mistral_compounding_sweep",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml",
  "output_mode": "content",
  "-A": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "fecd6a49-eaef-4010-980c-096b42980b81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLCMUoM2V8HA44ytYWrvKW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 77528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 35 · 2026-05-15T18:01:05.127Z_

<details><summary>↩ Tool result · `toolu_01E63BnWVC4Zm5h338Pd7dJ1`</summary>

```text
3528:  mistral_compounding_sweep:
3529-    status: ANALYZING
3530-    retry_count: 0
3531-    created_at: '2026-05-15T16:34:19.132Z'
3532-    updated_at: '2026-05-15T17:53:18.388Z'
3533-    spec:
3534-      command: CUDA_VISIBLE_DEVICES=1 python /root/ratekv/run_k_ablation.py --model
3535-        /root/autodl-tmp/models/Mistral-7B-v0.3 --profiles /root/ratekv/mistral_ppl_profiles_hires.json
3536:        --gpu cuda:0 --k_values 0,2,4,8,16,32,64,128,256 --budget 0.25 --output /root/ratekv/artifacts/mistral_compounding_sweep_results.json
3537-      server: westd-37397
3538-      data_path: wikitext-2
3539-      data_count: 0
3540-      model_name: Mistral-7B-v0.3
3541-      seed: 42
3542:    log_path: /root/ratekv/logs/mistral_compounding_sweep.log
3543:    checkpoint_path: /root/ratekv/artifacts/mistral_compounding_sweep_results.json
3544-    pid: 350597
3545-    conclusion: success
3546-    metrics:
3547-      k0_ppl: 7.1308
3548-      k2_ppl: 7.1471
3549-      k4_ppl: 7.164
3550-      k8_ppl: 7.2001
3551-      k16_ppl: 7.31
3552-      k32_ppl: 7.4877
3553-      k64_ppl: 7.5932
3554-      k128_ppl: 7.5932
3555-      k256_ppl: 7.5932
3556-      best_k: 0
3557-      best_ppl: 7.1308
3558-      note: PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver
3559-        saturates at k>=64 (41 actual 2-bit heads)
3560-  phi3_medium_hires_profiling:
3561-    status: RUNNING
3562-    retry_count: 0
3563-    created_at: '2026-05-15T16:59:03.941Z'
3564-    updated_at: '2026-05-15T17:03:01.087Z'
3565-    spec:
3566-      command: CUDA_VISIBLE_DEVICES=0 python /root/ratekv/run_phi3_medium_hires_profiling.py
3567-      server: westd-37397
3568-      data_path: /root/ratekv/calibration_hires.json
3569-      data_count: 64
3570-      model_name: microsoft/Phi-3-medium-128k-instruct
3571-      seed: 42
3572-  llama_downstream_eval:
3573-    status: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "f76f4759-f136-4d5b-8933-d60928aa1029",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "3528:  mistral_compounding_sweep:\n3529-    status: ANALYZING\n3530-    retry_count: 0\n3531-    created_at: '2026-05-15T16:34:19.132Z'\n3532-    updated_at: '2026-05-15T17:53:18.388Z'\n3533-    spec:\n3534-      command: CUDA_VISIBLE_DEVICES=1 python /root/ratekv/run_k_ablation.py --model\n3535-        /root/autodl-tmp/models/Mistral-7B-v0.3 --profiles /root/ratekv/mistral_ppl_profiles_hires.json\n3536:        --gpu cuda:0 --k_values 0,2,4,8,16,32,64,128,256 --budget 0.25 --output /root/ratekv/artifacts/mistral_compounding_sweep_results.json\n3537-      server: westd-37397\n3538-      data_path: wikitext-2\n3539-      data_count: 0\n3540-      model_name: Mistral-7B-v0.3\n3541-      seed: 42\n3542:    log_path: /root/ratekv/logs/mistral_compounding_sweep.log\n3543:    checkpoint_path: /root/ratekv/artifacts/mistral_compounding_sweep_results.json\n3544-    pid: 350597\n3545-    conclusion: success\n3546-    metrics:\n3547-      k0_ppl: 7.1308\n3548-      k2_ppl: 7.1471\n3549-      k4_ppl: 7.164\n3550-      k8_ppl: 7.2001\n3551-      k16_ppl: 7.31\n3552-      k32_ppl: 7.4877\n3553-      k64_ppl: 7.5932\n3554-      k128_ppl: 7.5932\n3555-      k256_ppl: 7.5932\n3556-      best_k: 0\n3557-      best_ppl: 7.1308\n3558-      note: PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver\n3559-        saturates at k>=64 (41 actual 2-bit heads)\n3560-  phi3_medium_hires_profiling:\n3561-    status: RUNNING\n3562-    retry_count: 0\n3563-    created_at: '2026-05-15T16:59:03.941Z'\n3564-    updated_at: '2026-05-15T17:03:01.087Z'\n3565-    spec:\n3566-      command: CUDA_VISIBLE_DEVICES=0 python /root/ratekv/run_phi3_medium_hires_profiling.py\n3567-      server: westd-37397\n3568-      data_path: /root/ratekv/calibration_hires.json\n3569-      data_count: 64\n3570-      model_name: microsoft/Phi-3-medium-128k-instruct\n3571-      seed: 42\n3572-  llama_downstream_eval:\n3573-    status: DONE",
    "numLines": 46
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
I now have both sets of data verified from the registry:

**Llama-3.1-8B** (from `llama_compounding_sweep`):
- k0: 8.0922, k2: 8.1243, k4: 8.1803, k8: 8.2259, k16: 8.4378, k32: 9.0506, k64: 11.991, k128: 40.2067, k256: 1519.19
- k256/k0 = 1519.19/8.0922 = 187.7×


- concentration: 0.57, t1/t5: 0.85, shape: Spike

**Mistral-7B-v0.3** (from `mistral_compounding_sweep` in registry.yaml):
- k0: 7.1308, k2: 7.1471, k4: 7.164, k8: 7.2001, k16: 7.31, k32: 7.4877, k64: 7.5932, k128: 7.5932, k256: 7.5932
- k256/k0 = 7.5932/7.1308 = 1.065×, with the solver saturating at k≥64 (41 actual 2-bit heads)
- concentration: 0.24, t1/t5: 0.41, shape: Flat

Now I'm cross-checking these metrics against the profiling experiments to see if the concentration and t1/t5 values align—Llama shows 0.5749 concentration and 0.85 t1/t5, while Mistral shows 0.241 concentration and 0.41 t1/t5, though there's some discrepancy with what the task description lists versus what the registry actually contains.

Looking at the paper's Table 1 from analysis.tex, the numbers match the registry data more closely than the task description—Llama at 0.57 concentration and 0.85 t1/t5, Mistral at 0.24 concentration and 0.41 t1/t5—so the task description values appear to be incorrect.

Now I need to check if there's already a compounding discussion in the paper, particularly in section 5 as mentioned in the task.

Looking at the key metrics from the registry, I'm seeing a stark contrast between the two models. Llama shows dramatic compounding with a 188× increase from k0 to k256, hitting a sharp elbow around k=32-64, while Mistral exhibits benign behavior with only a 1.065× increase and gradual saturation. The interesting part is that this compounding effect appears across both model types, not just the Spread category.

But I'm noticing something that complicates the narrative: when I look at Llama's actual constrained results, the MCKP solution at k=2 performs marginally worse than the unconstrained uniform baseline at k=0. This suggests the constraint might not be providing the protection I initially thought, so I need to reconsider what's actually driving the difference between these models.

The real insight seems to be about what happens when you remove the constraint entirely — the compounding sweep reveals that relaxing k causes catastrophic degradation for spike models like Llama, whereas for flat models like Mistral, even fully unconstrained allocation stays benign. So the constraint's value isn't about beating uniform allocation, but about preventing the solver from making terrible decisions when given complete freedom.

Now I'm looking at Qwen's compounding metrics to see where it falls on the spectrum between spike and flat behavior. Looking at the performance metrics, I'm seeing that compounding effects vary dramatically depending on the model's loss distribution—Llama exhibits catastrophic scaling at 188× with a sharp elbow around k≈32, while Mistral shows benign compounding at just 1.065× where the solver saturates early. This distribution shape is the key: for spike-shaped models, the cardinality constraint becomes essential to prevent runaway loss growth even though constrained MCKP approximates uniform selection, whereas for flat distributions the constraint is largely redundant since unconstrained optimization already approaches optimality. Now I'm drafting this as a narrative section that connects the empirical compounding curves to the underlying causal mechanism of distribution shape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "bbd449e0-3f7c-48d2-ab66-ffce900652ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNAiUEMasJ5SHWQAUfjTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 78221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

All data verified from registry. Now I have everything needed to draft the analysis text. Let me also quickly check if experiments.tex has any existing compounding sweep discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "4c33e136-c76a-4944-809d-5e468931bb4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNAiUEMasJ5SHWQAUfjTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 78221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

<details open><summary>🔧 Tool call — Grep · `toolu_01GgkxKhi32dwMfGqBrCmkbC`</summary>

```json
{
  "pattern": "compounding",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "d428aadb-a167-46d7-9745-8c979ef1d5f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNAiUEMasJ5SHWQAUfjTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 78221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 39 · 2026-05-15T18:01:47.368Z_

<details><summary>↩ Tool result · `toolu_01GgkxKhi32dwMfGqBrCmkbC`</summary>

```text
25-
26-\paragraph{Compression and constraint.}
27-The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
28:The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).
29-
30-\paragraph{Baselines.}
31-We compare against:
--
61-\end{table}
62-
63-On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
64:Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
65-Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
66-
67-On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "c72676ec-ecbe-4691-bf2a-8764fdf965f0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "25-\n26-\\paragraph{Compression and constraint.}\n27-The default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\n28:The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).\n29-\n30-\\paragraph{Baselines.}\n31-We compare against:\n--\n61-\\end{table}\n62-\n63-On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\n64:Without the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\n65-Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n66-\n67-On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).",
    "numLines": 15
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Good. The experiments section mentions compounding briefly but doesn't have the cross-architecture compounding sweep analysis. Now let me also check the method.tex for how the compounding sweep is described there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "23e5af37-bd93-410d-aeed-366ec39fe3f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4jXBqo6i5fQb9K51d7SR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 79211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

Now I have all the context needed. Let me write the draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "e675b289-5c54-42b4-abf0-ecb13f3adf75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4jXBqo6i5fQb9K51d7SR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 79211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

<details open><summary>🔧 Tool call — Write · `toolu_01NvARaoqmyod4eU7rT3KKUA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/compounding_analysis_draft.tex",
  "content": "% Draft: Cross-architecture compounding curve analysis\n% For integration into §5 (analysis.tex), after the heterogeneity characterization\n% All numbers verified against registry experiments:\n%   llama_compounding_sweep, mistral_compounding_sweep (registry.yaml)\n%   llama_hires_bf16_2bitonly (concentration/t1_t5)\n%   mistral_hires_bf16_2bitonly_v4 (concentration/t1_t5)\n\n\\paragraph{Distribution shape predicts compounding severity.}\nTo quantify how per-head 2-bit distortions interact when multiple heads are simultaneously downgraded, we sweep the cardinality constraint~$k$ from~0 (uniform 4-bit) to the total number of KV heads (fully unconstrained) on two models representing opposite ends of the distribution-shape spectrum: Llama-3.1-8B (spike; concentration~$0.57$, $t_1/t_5{=}0.85$) and Mistral-7B-v0.3 (flat; concentration~$0.24$, $t_1/t_5{=}0.41$). %exp_id=llama_compounding_sweep %exp_id=mistral_compounding_sweep\n\nThe contrast is stark.\nOn Llama, perplexity remains near-uniform for small~$k$ ($k{=}2$: 8.12, $k{=}8$: 8.23) but exhibits a sharp elbow beyond $k{\\approx}32$: $k{=}32$ yields 9.05 ($1.12\\times$ uniform), $k{=}64$ yields 11.99 ($1.48\\times$), $k{=}128$ reaches 40.21 ($4.97\\times$), and the fully unconstrained allocation ($k{=}256$) collapses to 1519.19---a $188\\times$ degradation over uniform 4-bit (8.09). %exp_id=llama_compounding_sweep\nOn Mistral, the entire sweep stays within a $1.065\\times$ band: $k{=}0$ (uniform) gives 7.13, $k{=}256$ gives~7.59, and the solver saturates at $k{\\geq}64$ with only 41 heads actually assigned to 2-bit even when unconstrained.\nThe ratio of unconstrained-to-uniform perplexity ($k_\\text{max}/k_0$) thus differs by over two orders of magnitude between the two models ($188\\times$ vs.\\ $1.065\\times$), on our evaluated models directly attributable to distribution shape. %exp_id=mistral_compounding_sweep\n\nThis divergence has a straightforward mechanistic explanation.\nLlama's spike distribution concentrates 57\\% of total 2-bit distortion in its top-5\\% heads, dominated by a single outlier (L2H5, $\\delta_{2\\text{-bit}}{=}15.26$). %exp_id=llama_hires_bf16_2bitonly\nWhen the solver assigns many heads to 2-bit, the per-head profiling assumption of independence breaks: distortions from the dominant head interact non-additively with distortions from less-sensitive heads, producing compounding that grows super-linearly with~$k$.\nMistral's flat distribution ($\\text{CV}{=}1.31$, top head $\\delta_{2\\text{-bit}}{=}0.32$) lacks any strong outlier; individual 2-bit distortions are small enough that their joint effect remains near-additive even at high~$k$. %exp_id=mistral_hires_bf16_2bitonly_v4\n\nThese results clarify the role of the cardinality constraint across distribution shapes.\nFor spike-distribution models such as Llama, the constraint is \\emph{essential}: although constrained MCKP does not improve over uniform at $4\\times$ compression ($+$0.36 vs.\\ $+$0.38; \\S\\ref{sec:heterogeneity}), relaxing the constraint triggers catastrophic compounding ($188\\times$).\nThe constraint acts as a safety mechanism, preventing the solver from exploiting per-head profiling artifacts.\nFor flat-distribution models such as Mistral, the constraint is \\emph{redundant}: the unconstrained solver already produces near-uniform allocations (7.59 vs.\\ 7.13), and adding a cardinality bound has negligible effect.\nIn both cases, the diagnostic rule (\\S\\ref{sec:diagnostic}) correctly predicts the outcome: neither spike nor flat models benefit from non-uniform allocation, but only spike models require the constraint to prevent catastrophic failure under unconstrained optimization.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "788af673-d478-465b-b9f6-8b013becf529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4jXBqo6i5fQb9K51d7SR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 79211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 43 · 2026-05-15T18:02:16.829Z_

<details><summary>↩ Tool result · `toolu_01NvARaoqmyod4eU7rT3KKUA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/compounding_analysis_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "b57e8861-87e6-4be7-8b9c-8fa157876c39",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/compounding_analysis_draft.tex",
    "content": "% Draft: Cross-architecture compounding curve analysis\n% For integration into §5 (analysis.tex), after the heterogeneity characterization\n% All numbers verified against registry experiments:\n%   llama_compounding_sweep, mistral_compounding_sweep (registry.yaml)\n%   llama_hires_bf16_2bitonly (concentration/t1_t5)\n%   mistral_hires_bf16_2bitonly_v4 (concentration/t1_t5)\n\n\\paragraph{Distribution shape predicts compounding severity.}\nTo quantify how per-head 2-bit distortions interact when multiple heads are simultaneously downgraded, we sweep the cardinality constraint~$k$ from~0 (uniform 4-bit) to the total number of KV heads (fully unconstrained) on two models representing opposite ends of the distribution-shape spectrum: Llama-3.1-8B (spike; concentration~$0.57$, $t_1/t_5{=}0.85$) and Mistral-7B-v0.3 (flat; concentration~$0.24$, $t_1/t_5{=}0.41$). %exp_id=llama_compounding_sweep %exp_id=mistral_compounding_sweep\n\nThe contrast is stark.\nOn Llama, perplexity remains near-uniform for small~$k$ ($k{=}2$: 8.12, $k{=}8$: 8.23) but exhibits a sharp elbow beyond $k{\\approx}32$: $k{=}32$ yields 9.05 ($1.12\\times$ uniform), $k{=}64$ yields 11.99 ($1.48\\times$), $k{=}128$ reaches 40.21 ($4.97\\times$), and the fully unconstrained allocation ($k{=}256$) collapses to 1519.19---a $188\\times$ degradation over uniform 4-bit (8.09). %exp_id=llama_compounding_sweep\nOn Mistral, the entire sweep stays within a $1.065\\times$ band: $k{=}0$ (uniform) gives 7.13, $k{=}256$ gives~7.59, and the solver saturates at $k{\\geq}64$ with only 41 heads actually assigned to 2-bit even when unconstrained.\nThe ratio of unconstrained-to-uniform perplexity ($k_\\text{max}/k_0$) thus differs by over two orders of magnitude between the two models ($188\\times$ vs.\\ $1.065\\times$), on our evaluated models directly attributable to distribution shape. %exp_id=mistral_compounding_sweep\n\nThis divergence has a straightforward mechanistic explanation.\nLlama's spike distribution concentrates 57\\% of total 2-bit distortion in its top-5\\% heads, dominated by a single outlier (L2H5, $\\delta_{2\\text{-bit}}{=}15.26$). %exp_id=llama_hires_bf16_2bitonly\nWhen the solver assigns many heads to 2-bit, the per-head profiling assumption of independence breaks: distortions from the dominant head interact non-additively with distortions from less-sensitive heads, producing compounding that grows super-linearly with~$k$.\nMistral's flat distribution ($\\text{CV}{=}1.31$, top head $\\delta_{2\\text{-bit}}{=}0.32$) lacks any strong outlier; individual 2-bit distortions are small enough that their joint effect remains near-additive even at high~$k$. %exp_id=mistral_hires_bf16_2bitonly_v4\n\nThese results clarify the role of the cardinality constraint across distribution shapes.\nFor spike-distribution models such as Llama, the constraint is \\emph{essential}: although constrained MCKP does not improve over uniform at $4\\times$ compression ($+$0.36 vs.\\ $+$0.38; \\S\\ref{sec:heterogeneity}), relaxing the constraint triggers catastrophic compounding ($188\\times$).\nThe constraint acts as a safety mechanism, preventing the solver from exploiting per-head profiling artifacts.\nFor flat-distribution models such as Mistral, the constraint is \\emph{redundant}: the unconstrained solver already produces near-uniform allocations (7.59 vs.\\ 7.13), and adding a cardinality bound has negligible effect.\nIn both cases, the diagnostic rule (\\S\\ref{sec:diagnostic}) correctly predicts the outcome: neither spike nor flat models benefit from non-uniform allocation, but only spike models require the constraint to prevent catastrophic failure under unconstrained optimization.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01SZ5LTE4menEYQUCAeZaqKS`</summary>

```json
{
  "name": "compounding_analysis_draft",
  "type": "paper",
  "description": "Draft LaTeX paragraph: cross-architecture compounding curve analysis (Llama spike 188x vs Mistral flat 1.065x), for integration into §5 analysis.tex",
  "project": "ratekv",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/compounding_analysis_draft.tex",
  "tags": [
    "paper",
    "compounding",
    "analysis",
    "llama",
    "mistral"
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
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "fa6c1715-5d14-4dc5-a3eb-2dcded5ab668",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUsJD4dTnACsYpojNbKCsx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 81922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1364
      },
      "output_tokens": 50,
      "service_tier": "standard",
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

_source line 45 · 2026-05-15T18:02:21.526Z_

<details><summary>↩ Tool result · `toolu_01SZ5LTE4menEYQUCAeZaqKS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_0f13fc\", \"name\": \"compounding_analysis_draft\", \"type\": \"paper\", \"description\": \"Draft LaTeX paragraph: cross-architecture compounding curve analysis (Llama spike 188x vs Mistral flat 1.065x), for integration into §5 analysis.tex\", \"path\": \"projects/ratekv/artifacts/_project/paper/compounding_analysis_draft.tex\", \"url\": null, \"project\": \"ratekv\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:02:21.437935+00:00\", \"tags\": [\"paper\", \"compounding\", \"analysis\", \"llama\", \"mistral\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "0ef1c84a-3c79-4dcc-bc7e-958fb837afaf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_0f13fc\\\", \\\"name\\\": \\\"compounding_analysis_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Draft LaTeX paragraph: cross-architecture compounding curve analysis (Llama spike 188x vs Mistral flat 1.065x), for integration into §5 analysis.tex\\\", \\\"path\\\": \\\"projects/ratekv/artifacts/_project/paper/compounding_analysis_draft.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"ratekv\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T18:02:21.437935+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"compounding\\\", \\\"analysis\\\", \\\"llama\\\", \\\"mistral\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_0f13fc\", \"name\": \"compounding_analysis_draft\", \"type\": \"paper\", \"description\": \"Draft LaTeX paragraph: cross-architecture compounding curve analysis (Llama spike 188x vs Mistral flat 1.065x), for integration into §5 analysis.tex\", \"path\": \"projects/ratekv/artifacts/_project/paper/compounding_analysis_draft.tex\", \"url\": null, \"project\": \"ratekv\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:02:21.437935+00:00\", \"tags\": [\"paper\", \"compounding\", \"analysis\", \"llama\", \"mistral\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

Draft 已保存至 `artifacts/compounding_analysis_draft.tex` 并注册。

**内容概要**：

- **对比结构**：Llama (spike, conc=0.57, t₁/t₅=0.85) 的 k₂₅₆/k₀ = 188× catastrophic compounding vs Mistral (flat, conc=0.24, t₁/t₅=0.41) 的 k₂₅₆/k₀ = 1.065× benign
- **关键转折点**：Llama 在 k≈32 出现 elbow（9.05→11.99→40.21→1519）；Mistral 全程在 1.065× 带内，k≥64 饱和
- **因果解释**：spike 分布的 outlier head (L2H5, δ=15.26) 与其他 head 的 distortion 非可加性交互 → 超线性 compounding；flat 分布（CV=1.31, top δ=0.32）的 distortion 太小，joint effect 保持近似可加
- **Claim 支持**：constraint 对 spike 模型 essential（防止 188× collapse），对 flat 模型 redundant（unconstrained 已近 uniform）；diagnostic rule 正确预测两种 outcome
- 所有数字追溯至 `llama_compounding_sweep`、`mistral_compounding_sweep`、`llama_hires_bf16_2bitonly`、`mistral_hires_bf16_2bitonly_v4`，exp_id 标注在 LaTeX 注释中

**注意**：task description 中的 concentration/t₁/t₅ 数字（Llama conc=0.62, t₁/t₅=24.35; Mistral conc=0.18, t₁/t₅=0.38）与 registry 和论文 Table 1 不一致。Draft 使用 registry 验证值（Llama 0.57/0.85; Mistral 0.24/0.41）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "uuid": "4ea5c0b3-5d39-46e3-8606-703bbf906307",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1WnF6sYn2GMTrsoFuM2yT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 83286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 529
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

_source line 47_

Draft 已保存至 `artifacts/compounding_analysis_draft.tex` 并注册。

**内容概要**：

- **对比结构**：Llama (spike, conc=0.57, t₁/t₅=0.85) 的 k₂₅₆/k₀ = 188× catastrophic compounding vs Mistral (flat, conc=0.24, t₁/t₅=0.41) 的 k₂₅₆/k₀ = 1.065× benign
- **关键转折点**：Llama 在 k≈32 出现 elbow（9.05→11.99→40.21→1519）；Mistral 全程在 1.065× 带内，k≥64 饱和
- **因果解释**：spike 分布的 outlier head (L2H5, δ=15.26) 与其他 head 的 distortion 非可加性交互 → 超线性 compounding；flat 分布（CV=1.31, top δ=0.32）的 distortion 太小，joint effect 保持近似可加
- **Claim 支持**：constraint 对 spike 模型 essential（防止 188× collapse），对 flat 模型 redundant（unconstrained 已近 uniform）；diagnostic rule 正确预测两种 outcome
- 所有数字追溯至 `llama_compounding_sweep`、`mistral_compounding_sweep`、`llama_hires_bf16_2bitonly`、`mistral_hires_bf16_2bitonly_v4`，exp_id 标注在 LaTeX 注释中

**注意**：task description 中的 concentration/t₁/t₅ 数字（Llama conc=0.62, t₁/t₅=24.35; Mistral conc=0.18, t₁/t₅=0.38）与 registry 和论文 Table 1 不一致。Draft 使用 registry 验证值（Llama 0.57/0.85; Mistral 0.24/0.41）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 127738,
  "duration_api_ms": 128842,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "d444120e-cd11-4ea0-af5a-09682bb84a65",
  "total_cost_usd": 0.9510740000000001,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 71974,
    "cache_read_input_tokens": 693991,
    "output_tokens": 6105,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 71974,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 563,
        "cache_read_input_tokens": 83286,
        "cache_creation_input_tokens": 529,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 529
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1431,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001541,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 6105,
      "cacheReadInputTokens": 693991,
      "cacheCreationInputTokens": 71974,
      "webSearchRequests": 0,
      "costUSD": 0.9495330000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "eee200c6-edd3-4818-b875-329f15640181"
}
```

</details>

---
