# paper model count fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_paper_model_count_fix_20260516T024526.log`
- **Structured JSON:** [`b9077abac9b55fc35dd7.json`](../../sessions/b9/b9077abac9b55fc35dd7.json)

## Before a recorded user message

92 recorded events

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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
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
  "uuid": "92a6e381-266b-4add-b057-c2e6953196d2",
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
    "resetsAt": 1778904600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dac236f8-52c8-48a1-b360-4429b54b349b",
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e"
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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "5e877c0e-b8d5-4586-84c1-2bc8dc8080ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

Let me read the current state of all relevant tex files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "e583bce2-7a95-443d-88c1-b3ab423c0dfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Tknb3D2L6MoKHb3wsXfrxY`</summary>

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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "a7615e3e-7c99-4f3b-85d8-f8ec71883ed0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 7 · 2026-05-16T02:45:38.835Z_

<details><summary>↩ Tool result · `toolu_01Tknb3D2L6MoKHb3wsXfrxY`</summary>

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
11	Table~\ref{tab:heterogeneity} summarizes the results across nine models at $4\times$ compression.
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
23	CodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\%$ of top-5 delta, $11.3\times$ the second-ranked head) confirms that even very high concentration yields no benefit when dominated by a single outlier. %exp_id=codellama_hires_profiling
24	Mistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
25	
26	Pythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).
27	Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
28	
29	Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, predicting neutral MCKP benefit. %exp_id=phi3_medium_hires_profiling_v2
30	
31	\paragraph{Scale-dependent concentration dilution.}
32	Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\times$ more heads into the flat regime.
33	Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
34	Concentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\times$scale combination where non-uniform allocation helps.
35	
36	\begin{table}[t]
37	\centering
38	\small
39	\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}
40	\label{tab:heterogeneity}
41	\begin{tabular}{lcccccc}
42	\toprule
43	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
44	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
45	\midrule
46	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
47	Qwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\
48	Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
49	Llama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
50	Mistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\
51	Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\
52	Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\
53	CodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\
54	Pythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	The per-head heatmap (Figure~\ref{fig:heatmap}, Appendix~\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.
60	
61	\subsection{Empirical Decision Rule}
62	\label{sec:diagnostic}
63	
64	MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
65	This motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.
66	Given the profiling results from \S\ref{sec:profiling}, compute the top-5\% concentration and $t_1/t_5$ ratio, then select:
67	\begin{itemize}[nosep]
68	\item \textbf{Spread} (concentration $\geq 0.50$ \emph{and} $t_1/t_5 \leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
69	\item \textbf{Spike} ($t_1/t_5 > 0.70$ \emph{and} concentration $\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.
70	\item \textbf{Flat} (concentration $< 0.25$, or concentration $\in [0.25, 0.50)$ with $t_1/t_5 \leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.
71	\end{itemize}
72	
73	Both conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \geq 0.70$) correctly override.
74	A concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.
75	The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).
76	Only Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.
77	The rule reuses profiling data already required by the solver and adds no overhead.
78	
79	\paragraph{Why is Qwen-7B the only spread model?}
80	We offer two non-exclusive hypotheses, both requiring further validation.
81	First, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.
82	However, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.
83	Second, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\ 0.57).
84	This suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.
85	
86	Additional analyses---granularity tradeoff (Appendix~\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\ref{sec:granularity}--\ref{sec:kv_separation}.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "85578d80-a3ad-43b5-bb58-241666aa9575",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nCodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\\%$ of top-5 delta, $11.3\\times$ the second-ranked head) confirms that even very high concentration yields no benefit when dominated by a single outlier. %exp_id=codellama_hires_profiling\nMistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\nPhi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, predicting neutral MCKP benefit. %exp_id=phi3_medium_hires_profiling_v2\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPhi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\\\\nCodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\geq 0.50$ \\emph{and} $t_1/t_5 \\leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 > 0.70$ \\emph{and} concentration $\\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.\n\\item \\textbf{Flat} (concentration $< 0.25$, or concentration $\\in [0.25, 0.50)$ with $t_1/t_5 \\leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \\geq 0.70$) correctly override.\nA concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.\nThe rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\n\\paragraph{Why is Qwen-7B the only spread model?}\nWe offer two non-exclusive hypotheses, both requiring further validation.\nFirst, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.\nHowever, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.\nSecond, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\\ 0.57).\nThis suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_011im8HFLousFCTJ1cHqggaN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "0e97c4e3-2e91-4cb9-b096-563a4729c48d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 9 · 2026-05-16T02:45:39.393Z_

<details><summary>↩ Tool result · `toolu_011im8HFLousFCTJ1cHqggaN`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate seven models spanning five architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
14	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
15	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
16	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
17	
18	\paragraph{Evaluation.}
19	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
20	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
21	
22	\paragraph{Profiling.}
23	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
24	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
25	
26	\paragraph{Compression and constraint.}
27	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
28	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).
29	
30	\paragraph{Baselines.}
31	We compare against:
32	(1)~uniform 4-bit quantization;
33	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
34	(3)~unconstrained MCKP allocation;
35	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
36	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
37	
38	\subsection{Main Results}
39	\label{sec:main_results}
40	
41	\begin{table}[t]
42	\centering
43	\small
44	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
45	\label{tab:main_results}
46	\begin{tabular}{lccccc}
47	\toprule
48	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
49	\cmidrule(lr){4-5}
50	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
51	\midrule
52	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{10.91} \\
53	Qwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\
54	Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\
55	Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \textbf{8.45} \\
56	Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\
57	Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\
58	Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\
59	\bottomrule
60	\end{tabular}
61	\end{table}
62	
63	On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
64	Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
65	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
66	
67	On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
68	Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.
69	
70	On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
71	On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.
72	
73	On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17 ($+$0.4\%).
74	Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
75	
76	Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen-7B ($3.3\times$ bf16, 60\% heads at 2-bit), \emph{severe} on Pythia ($1.9\times$), \emph{moderate} on Gemma-2 ($1.47\times$), and \emph{mild} on remaining models (${\sim}1.07$--$1.12\times$) including Qwen-14B ($1.12\times$, 20\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\ flat).
77	See Appendix~\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\ref{sec:budget_sweep} (budget sweep) for additional detail.
78	
79	MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
80	
81	\paragraph{Comparison with KIVI.}
82	KIVI~\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.
83	At 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.
84	Within the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).
85	The two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.
86	However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.
87	Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.
88	
89	\subsection{Cross-Architecture Compounding}
90	\label{sec:compounding_cross}
91	
92	\begin{figure}[t]
93	\centering
94	\includegraphics[width=\columnwidth]{figures/fig_compounding_curves.pdf}
95	\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\times$). All three stay near-baseline for $k{\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\approx}96$ due to its 112 KV heads (maximum ${\sim}96$ eligible for 2-bit assignment).}
96	\label{fig:compounding_cross}
97	\end{figure}
98	
99	Figure~\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.
100	At small $k$ (${\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\leq}2.5\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.
101	
102	Beyond $k{=}8$, divergence is stark.
103	Llama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.
104	Qwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\times$) and $98.75$ at $k{=}256$ ($10.1\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.
105	Mistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.
106	
107	These curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\times$ baseline) is ${\sim}32$ for Qwen, ${\sim}64$ for Llama, and ${\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.
108	
109	\subsection{Downstream Evaluation}
110	\label{sec:downstream}
111	
112	\begin{table}[t]
113	\centering
114	\small
115	\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen values are mean over 3 calibration seeds ($\pm$1$\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}
116	\label{tab:downstream}
117	\begin{tabular}{lccccc}
118	\toprule
119	Model & ARC-C & HS & PIQA & WG & Avg \\
120	\midrule
121	Qwen2.5-7B        & $+$0.0{\scriptsize$\pm$0.4} & $+$4.1{\scriptsize$\pm$0.2} & $+$2.0{\scriptsize$\pm$0.2} & $+$1.6{\scriptsize$\pm$1.2} & $+$1.9 \\
122	Yi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\
123	Llama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\
124	Mistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\
125	Gemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
131	The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
132	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
133	Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "6a9b709d-313c-4d9b-a5fe-5616d9a9a18c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate seven models spanning five architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
      "numLines": 133,
      "startLine": 1,
      "totalLines": 133
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01JFqBmJcDfQEbYzJMvKq8AQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "7df417e4-7351-4035-90db-0115a9abb2c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 11 · 2026-05-16T02:45:40.352Z_

<details><summary>↩ Tool result · `toolu_01JFqBmJcDfQEbYzJMvKq8AQ`</summary>

```text
1	Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\{2,4,8,16\}$ provides negligible improvement over uniform 4-bit for eight of nine models.
2	The sole exception is Qwen2.5-7B, where a cardinality-constrained solver achieves 10.91 perplexity at $4\times$ compression---a 29.4\% reduction over uniform 4-bit (15.45)---while unconstrained solvers degrade catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.
3	The benefit depends not on GQA ratio or model scale, but on whether sensitivity heterogeneity is \emph{spread} across multiple heads with cross-bitwidth gradients---a pattern observed in only one model ($N{=}1$) in our study.
4	On the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.
5	The cardinality constraint prevents catastrophic over-allocation on Qwen-7B and moderate degradation on flat models (Gemma-2: unconstrained $1.47\times$ degradation reduced to within 0.5\% of uniform), while rendering solver choice irrelevant---constrained greedy and MCKP produce identical allocations---enabling a simple $O(H\log H)$ greedy algorithm.
6	We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "10529178-c29c-47a0-86dd-9d0dfaa19093",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
      "content": "Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\\{2,4,8,16\\}$ provides negligible improvement over uniform 4-bit for eight of nine models.\nThe sole exception is Qwen2.5-7B, where a cardinality-constrained solver achieves 10.91 perplexity at $4\\times$ compression---a 29.4\\% reduction over uniform 4-bit (15.45)---while unconstrained solvers degrade catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.\nThe benefit depends not on GQA ratio or model scale, but on whether sensitivity heterogeneity is \\emph{spread} across multiple heads with cross-bitwidth gradients---a pattern observed in only one model ($N{=}1$) in our study.\nOn the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.\nThe cardinality constraint prevents catastrophic over-allocation on Qwen-7B and moderate degradation on flat models (Gemma-2: unconstrained $1.47\\times$ degradation reduced to within 0.5\\% of uniform), while rendering solver choice irrelevant---constrained greedy and MCKP produce identical allocations---enabling a simple $O(H\\log H)$ greedy algorithm.\nWe characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01G1mEnRuHSVrw5urbMYRsBH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "8f38badd-d174-4846-a3b1-52468af4b5a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 13 · 2026-05-16T02:45:40.809Z_

<details><summary>↩ Tool result · `toolu_01G1mEnRuHSVrw5urbMYRsBH`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The issue traces not to solver suboptimality but to a violation of the additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors compound through the residual stream.
17	The additive model predicts $\sim$11 PPL; the actual PPL is $3$--$4\times$ higher, because 2-bit distortions are orders of magnitude larger than 4-bit and compound super-linearly when many heads are quantized simultaneously.
18	
19	This observation points to a minimal intervention: cap the number of 2-bit assignments.
20	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
21	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 10.91 PPL---a 29.4\% reduction over uniform 4-bit.
22	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
23	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
24	The constraint is beneficial even on flat-distribution architectures: on Gemma-2-9B, unconstrained MCKP assigns 31.5\% of heads to 2-bit, producing a moderate $1.47\times$ degradation; the constraint reduces this to within 0.5\% of uniform.
25	
26	A surprising consequence is that the cardinality constraint renders solver choice irrelevant.
27	Constrained greedy and MCKP produce identical allocations across all tested architectures (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm.
28	A per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
29	
30	However, non-uniform allocation does not help universally.
31	On the remaining eight models---including Qwen2.5-14B, where the $3.4\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.
32	The difference traces to the \emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5, CodeLlama, and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Phi-3-medium, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').
33	
34	This motivates a question prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
35	We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.
36	Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.
37	
38	Our contributions are:
39	\begin{enumerate}[nosep]
40	\item We identify 2-bit distortion compounding as a major contributing factor in the degradation observed under unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a single cardinality constraint on 2-bit assignments suffices to prevent it, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
41	
42	\item RateQuant~\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
43	
44	\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "7cc8b5fb-ed85-447d-9e77-203b089e56b3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPer-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.\nRecent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\nRateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).\n\nIn practice, hardware-efficient inference requires bit-widths drawn from $\\{2, 4, 8, 16\\}$---the formats natively supported by modern accelerators.\nOn this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.\nOne might expect that exact MCKP solvers would fill this gap.\nThey do not.\nOn Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\nThe optimization does not merely underperform; it fails catastrophically.\n\nThe issue traces not to solver suboptimality but to a violation of the additive distortion assumption.\nBoth solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors compound through the residual stream.\nThe additive model predicts $\\sim$11 PPL; the actual PPL is $3$--$4\\times$ higher, because 2-bit distortions are orders of magnitude larger than 4-bit and compound super-linearly when many heads are quantized simultaneously.\n\nThis observation points to a minimal intervention: cap the number of 2-bit assignments.\nWe add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\nOn Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 10.91 PPL---a 29.4\\% reduction over uniform 4-bit.\nThe constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.\nThis is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.\nThe constraint is beneficial even on flat-distribution architectures: on Gemma-2-9B, unconstrained MCKP assigns 31.5\\% of heads to 2-bit, producing a moderate $1.47\\times$ degradation; the constraint reduces this to within 0.5\\% of uniform.\n\nA surprising consequence is that the cardinality constraint renders solver choice irrelevant.\nConstrained greedy and MCKP produce identical allocations across all tested architectures (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm.\nA per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n\nHowever, non-uniform allocation does not help universally.\nOn the remaining eight models---including Qwen2.5-14B, where the $3.4\\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.\nThe difference traces to the \\emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5, CodeLlama, and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Phi-3-medium, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').\n\nThis motivates a question prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\nWe propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.\nYi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.\n\nOur contributions are:\n\\begin{enumerate}[nosep]\n\\item We identify 2-bit distortion compounding as a major contributing factor in the degradation observed under unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a single cardinality constraint on 2-bit assignments suffices to prevent it, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n\n\\item RateQuant~\\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\\S\\ref{sec:solver_equiv}).\n\n\\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\\S\\ref{sec:heterogeneity}).\n\\end{enumerate}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01AmFJwBWXPHj2vusFYCeR77`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "ef18d476-c2b8-4d25-b99c-109fe4afea82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6EvJe86gn88u5rK9S5DhK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12860
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 15 · 2026-05-16T02:45:40.965Z_

<details><summary>↩ Tool result · `toolu_01AmFJwBWXPHj2vusFYCeR77`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
4	On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
5	Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.
6	An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
7	Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
8	
9	\section*{Limitations}
10	
11	\paragraph{$N{=}1$ spread.}
12	The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
13	
14	\paragraph{Model scale.}
15	The largest model evaluated is 14B parameters (384 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.
16	
17	\paragraph{Runtime.}
18	All latency measurements use PyTorch-level per-head \texttt{quantize}/\texttt{dequantize} dispatch and do not represent optimized CUDA kernel performance. The overhead reported in Appendix~\ref{sec:runtime} is an upper bound on the mixed-precision penalty; production inference engines with fused attention kernels would likely narrow this gap. No real-kernel latency benchmarks are reported.
19	
20	\paragraph{Downstream scope.}
21	Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). For HellaSwag, we report raw accuracy (\texttt{acc}) rather than length-normalized accuracy (\texttt{acc\_norm}). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.
22	
23	\paragraph{Calibration domain.}
24	Cross-dataset stability is verified only between WikiText-2 and C4 (96--97\% bit-assignment agreement); other domains (code, dialogue, multilingual) are untested.
25	
26	\paragraph{Long-context.}
27	Long-context evaluation extends only to 8K tokens; deployment scenarios at 32K--128K context lengths are not tested.
28	
29	\paragraph{Missing direct competitors.}
30	No existing tool performs per-head mixed-precision KV cache quantization on hardware-aligned bit-widths, precluding direct comparison with an established baseline at the same granularity.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "a5f89148-c13d-4ec4-9aeb-aef9968a82ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nPer-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.\nOn Qwen2.5-7B, limiting 2-bit heads to $k{\\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\\%) at $4\\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.\nWhether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.\nAn empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nExtending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) are natural next steps.\n\n\\section*{Limitations}\n\n\\paragraph{$N{=}1$ spread.}\nThe spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\\geq 0.50$, $t_1/t_5 \\leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.\n\n\\paragraph{Model scale.}\nThe largest model evaluated is 14B parameters (384 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.\n\n\\paragraph{Runtime.}\nAll latency measurements use PyTorch-level per-head \\texttt{quantize}/\\texttt{dequantize} dispatch and do not represent optimized CUDA kernel performance. The overhead reported in Appendix~\\ref{sec:runtime} is an upper bound on the mixed-precision penalty; production inference engines with fused attention kernels would likely narrow this gap. No real-kernel latency benchmarks are reported.\n\n\\paragraph{Downstream scope.}\nDownstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). For HellaSwag, we report raw accuracy (\\texttt{acc}) rather than length-normalized accuracy (\\texttt{acc\\_norm}). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.\n\n\\paragraph{Calibration domain.}\nCross-dataset stability is verified only between WikiText-2 and C4 (96--97\\% bit-assignment agreement); other domains (code, dialogue, multilingual) are untested.\n\n\\paragraph{Long-context.}\nLong-context evaluation extends only to 8K tokens; deployment scenarios at 32K--128K context lengths are not tested.\n\n\\paragraph{Missing direct competitors.}\nNo existing tool performs per-head mixed-precision KV cache quantization on hardware-aligned bit-widths, precluding direct comparison with an established baseline at the same granularity.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me understand the current state:

1. **Abstract**: Says "nine models" and "eight of nine models" — consistent at 9.
2. **Introduction**: Says "nine models", "eight models", "9/9" — consistent at 9.
3. **Conclusion**: Says "nine evaluated models (9/9)" — consistent at 9.

4. **experiments.tex §4.1**: Says "We evaluate **seven** models" — lists only 7 models (Qwen2.5-7B, Qwen2.5-14B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B-v0.3, Gemma-2-9B, Pythia-1.4B). 
   - Missing from Table 1: Phi-3-medium-14B and CodeLlama-7B
   - Table 1 has 7 rows matching these 7 models.

5. **analysis.tex Table 2**: Has 9 rows including Phi-3-medium-14B (with `---` for Δ PPL columns) and CodeLlama-7B (also `---`). This matches the "nine models" count. Phi-3-medium-14B has constrained MCKP data (PPL = 5.815, baseline = 5.636, uniform = 5.799), so it should have actual Δ PPL values rather than `---`.

Looking at Table 2, I need to calculate the delta values: the difference between the uniform PPL and baseline, and between the constrained PPL and baseline. For Phi-3-medium-14B, that means replacing the `---` entries with the computed deltas based on the provided metrics. I'm calculating the perplexity deltas for Phi-3 and realizing the "Δ≈0" notation in Table 2 likely indicates when the difference between uniform and constrained approaches is negligible, suggesting no benefit from the MCKP method. Since Phi-3 now has evaluation data, I should update Table 2 to include these results alongside the existing entries that show `---` for models that only had profiling runs. Let me finish that thought — the MCKP benefit is approximately zero, so I need to pull the actual Δ PPL values for the constrained approach. For Phi-3, that means updating Table 2 with the real numbers instead of dashes, adding Phi-3 to Table 1, and adjusting the model count in section 4.1. CodeLlama will stay as dashes since there's no constrained evaluation for it. Now I'm looking at what Table 1 actually needs — the baseline in bf16, then the 4-bit uniform quantization, followed by the unconstrained greedy and MCKP results, so I need to figure out where Phi-3-medium-14B fits in that structure.

The issue is that I only have three values for Phi-3: baseline at 5.636, uniform 4-bit at 5.799, and constrained MCKP at 5.815, but no unconstrained greedy or MCKP results. Since every other model in Table 1 has all five columns filled, I'll probably need to use dashes for the missing unconstrained values. That means updating the model count from seven to eight models in section 4.1. I need to figure out what values to use for Phi-3 in Table 1—the task only gives me the constrained MCKP value of 5.815, but looking at the existing entries, every model has values across all columns. Let me check if I should fill in the unconstrained columns with dashes or if there's another approach I'm missing.

Since I don't have the unconstrained data for Phi-3, I'll add it with dashes for those columns and update the caption to clarify this. Then I'll update the model count from seven to eight and add Phi-3 to the list in section 4.1. Since Phi-3 doesn't have unconstrained evaluation data, the "5/7" count for models with matching allocations remains accurate—I could clarify this by noting "5/7 models with unconstrained evaluations," but that feels redundant, so I'll just add Phi-3 to the table and note that it lacks unconstrained results.

For the table itself, I'll go with Option A: add Phi-3 with dashes for missing data and update the caption accordingly. Now I need to handle the constraint parameters in §4.1—currently it lists specific k values for each model, so I'll need to add Phi-3's constraint value to that list.

The problem is I don't have explicit information about what k was used for Phi-3. Looking at the analysis, it's described as a flat model with 400 heads and GQA 4:1 compression, which suggests it might follow the same pattern as other flat models like Gemma-2 and Pythia (k=8), but I can't be certain without the actual data. I should probably leave it as unknown rather than guess.

Now I'm calculating the precise Δ values for Phi-3 from the baseline and modified perplexities: uniform gives +0.163 and constrained gives +0.179, which rounds to +0.16 and +0.18 in the table format. But the task description mentions "Δ≈0" which seems inconsistent with these values, so I need to clarify what the table actually expects.

Looking at the analysis.tex file, it describes Phi-3 as having "neutral MCKP benefit" due to its flat attention pattern, which would mean the difference between constrained and uniform improvements is minimal—essentially +0.02 net, which is negligible. So for Table 2, I should represent this as approximately zero difference between the two conditions.

Now I'm mapping out the specific edits needed across both files. In analysis.tex, I need to fill in the Phi-3 row with the actual PPL values of +0.16 for uniform and +0.18 for constrained. Then in experiments.tex, I'll need to update the model count from seven to eight, add Phi-3 to the model list and Table 1, adjust the table caption accordingly, and revise the compression parameter discussion to account for the additional model. I'm deciding whether to add Phi-3 to Table 1 as requested, and if so, how to format it. The row would include the model name and metrics, with `---` for the unconstrained columns since that data isn't available. For the constrained result of 5.815, I need to determine if it should be bolded — since it's slightly worse than the uniform baseline of 5.799, it shouldn't be bolded, unlike other models where constrained outperforms uniform. Looking at the rest of the table, I can see the pattern now — the bold formatting appears only when the constrained approach yields a lower error than the uniform approach. Qwen-7B and Llama-3.1-8B both show this improvement, while the other models either perform worse with constraints or show negligible differences.

For placing Phi-3 in the table, I need to figure out where it fits in the model size ordering alongside the other entries. Generating markdown table... I'm verifying the PPL values and deltas match between the tables—Table 1 shows actual values while Table 2 shows the differences. Now I need to update the model list in section 4.1 to include Phi-3 alongside the other models like Qwen2.5 and Yi-1.5. I need to update the model count to eight families and add Phi-3-medium-14B with its GQA 4:1 configuration and 40 layers × 10 KV heads per layer, which gives 400 total KV heads.

Let me recount the architecture families: Qwen, Yi, Llama, Mistral, Gemma-2, Pythia, and now Phi-3 makes six families total. Now I'm confirming the final count: eight models across six architecture families, with Phi-3-medium-14B fitting between Gemma-2 and Pythia in the table ordering.

For the compression paragraph, I need to determine Phi-3's k value—since it's a flat model with 400 heads like the others, I'll assume k=8 to match that pattern, though I should verify this against the experiment scripts if possible. The "5/7" count still holds since it refers to models with unconstrained data, and Phi-3 simply lacks that evaluation. I need to add a sentence about Phi-3 to the results section—something noting that constrained MCKP performs nearly identically to uniform allocation on this flat GQA model, which aligns with its sensitivity profile. I'm deciding where best to insert this in the discussion.

Looking at the paragraph structure, I can slot it after the Gemma-2 discussion and before the unconstrained failure section. I should also scan through experiments.tex to check if other references need updating—particularly around the model count and attention type descriptions in the abstract and introduction.

Wait, there's a discrepancy I'm catching: the abstract mentions "seven architecture families" but experiments.tex says "five." Let me recount across all nine models including CodeLlama and Phi-3. That gives me Qwen, Yi, Llama (with CodeLlama), Mistral, Gemma-2, Phi-3, and Pythia—which actually does total seven families. So the abstract is correct and experiments.tex needs the update. I need to track down the specific edits required and locate any Phi-3 scripts to find the k parameter value.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "ba003050-3125-4b14-b603-97bcd6f6a607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Th7nSEqNo2c6RfRwRccDfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 24701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11827
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

Let me search for Phi-3 related data and all count references across the tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "9bf97097-6e3d-4067-aea2-2661224b4c02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Th7nSEqNo2c6RfRwRccDfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 24701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11827
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

<details open><summary>🔧 Tool call — Bash · `toolu_01VYVjsZGzPwzbGx84kwU8yF`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper && grep -n \"seven\\|eight\\|nine\\|7/7\\|8/8\\|9/9\\|7 model\\|8 model\\|9 model\\|five architecture\\|six architecture\\|seven architecture\\|eight architecture\" *.tex",
  "description": "Grep all model count references in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "163c28ec-e26b-4cd0-afff-eaccb6b3d3cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Th7nSEqNo2c6RfRwRccDfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 24701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11827
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

_source line 19 · 2026-05-16T02:48:06.293Z_

<details><summary>↩ Tool result · `toolu_01VYVjsZGzPwzbGx84kwU8yF`</summary>

```text
abstract.tex:1:Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\{2,4,8,16\}$ provides negligible improvement over uniform 4-bit for eight of nine models.
abstract.tex:4:On the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.
abstract.tex:6:We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.
analysis.tex:11:Table~\ref{tab:heterogeneity} summarizes the results across nine models at $4\times$ compression.
analysis.tex:75:The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).
appendix.tex:53:\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}
conclusion.tex:6:An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
conclusion.tex:12:The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
experiments.tex:8:We evaluate seven models spanning five architecture families and diverse attention configurations:
experiments.tex:44:\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
introduction.tex:31:On the remaining eight models---including Qwen2.5-14B, where the $3.4\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.
introduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.
introduction.tex:42:\item RateQuant~\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
introduction.tex:44:\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
related_work.tex:14:\paragraph{Mixed-Precision Quantization (Weights).}
related_work.tex:15:Mixed-precision allocation has a long history at the weight level.
related_work.tex:16:HAWQ~\cite{dong2019hawq} and HAWQ-V2~\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.
related_work.tex:17:These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.
related_work.tex:18:KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\S\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.
related_work.tex:26:Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\cite{xia2025kitty}, token-level via a learned on-device controller~\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\cite{lei2026arkv}---at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "5d25bbcd-2e2c-4436-8ec8-fb00c02d47e1",
  "tool_use_result": {
    "stdout": "abstract.tex:1:Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\\{2,4,8,16\\}$ provides negligible improvement over uniform 4-bit for eight of nine models.\nabstract.tex:4:On the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.\nabstract.tex:6:We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.\nanalysis.tex:11:Table~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nanalysis.tex:75:The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).\nappendix.tex:53:\\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}\nconclusion.tex:6:An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nconclusion.tex:12:The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\\geq 0.50$, $t_1/t_5 \\leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.\nexperiments.tex:8:We evaluate seven models spanning five architecture families and diverse attention configurations:\nexperiments.tex:44:\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\nintroduction.tex:31:On the remaining eight models---including Qwen2.5-14B, where the $3.4\\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.\nintroduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.\nintroduction.tex:42:\\item RateQuant~\\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\\S\\ref{sec:solver_equiv}).\nintroduction.tex:44:\\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\\S\\ref{sec:heterogeneity}).\nrelated_work.tex:14:\\paragraph{Mixed-Precision Quantization (Weights).}\nrelated_work.tex:15:Mixed-precision allocation has a long history at the weight level.\nrelated_work.tex:16:HAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nrelated_work.tex:17:These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.\nrelated_work.tex:18:KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nrelated_work.tex:26:Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
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

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01B4q5MWUMKCmoJGmbHgBzFt`</summary>

```json
{
  "pattern": "**/run_phi3*",
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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "42025197-1028-4363-bf51-33cb1b200d74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Th7nSEqNo2c6RfRwRccDfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 24701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11827
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

_source line 21 · 2026-05-16T02:48:06.743Z_

<details><summary>↩ Tool result · `toolu_01B4q5MWUMKCmoJGmbHgBzFt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_hires_profiling.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_compounding_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_compounding_sweep.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "3ed37738-b272-4724-bdc5-4a250f1f4311",
  "tool_use_result": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_hires_profiling.py",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_compounding_sweep.py",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_compounding_sweep.py"
    ],
    "durationMs": 15,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me check the Phi-3 constrained pipeline script to find the k value and exact PPL numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "9b681ab2-1501-4cc8-bbfd-2e81aa0f151a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGKJkZYbBDz6q8Ri3C2vUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10495,
      "cache_read_input_tokens": 36528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10495
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

<details open><summary>🔧 Tool call — Read · `toolu_01RDm1aVnkhpxVqy7raE4pQu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "4215af31-348a-4913-87ef-c41e02b39c22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGKJkZYbBDz6q8Ri3C2vUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10495,
      "cache_read_input_tokens": 36528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10495
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

_source line 24 · 2026-05-16T02:48:10.264Z_

<details><summary>↩ Tool result · `toolu_01RDm1aVnkhpxVqy7raE4pQu`</summary>

```text
1	"""Phi-3-medium-14B constrained MCKP + WikiText-2 eval pipeline.
2	
3	Architecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.
4	Profiling source: artifacts/phi3_medium_profiles_hires.json (2-bit only).
5	4-bit/8-bit deltas synthesized from 2-bit via fixed ratios.
6	"""
7	import os
8	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
9	os.environ["HF_DATASETS_OFFLINE"] = "1"
10	
11	import argparse
12	import json
13	import time
14	import torch
15	from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
16	from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
17	from solver import (solve_mckp_constrained, solve_mckp,
18	                    solve_greedy_ratequant, uniform_quantization_baseline)
19	
20	MODEL_PATH = "/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct"
21	PROFILE_PATH = "artifacts/phi3_medium_profiles_hires.json"
22	OUTPUT_PATH = "artifacts/phi3_medium_constrained_results.json"
23	BUDGET = 0.25
24	MAX_2BIT = 8
25	RATIO_4BIT = 0.25
26	RATIO_8BIT = 0.05
27	
28	
29	def synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads):
30	    """Synthesize 4-bit and 8-bit deltas from 2-bit-only profiling data."""
31	    profiles = {}
32	    for li in range(num_layers):
33	        l_str = str(li)
34	        layer_data = raw_profiles[l_str]
35	        profiles[l_str] = {}
36	        for hi in range(num_kv_heads):
37	            h_str = str(hi)
38	            d2 = layer_data[h_str]["quantization"]["2"]
39	            profiles[l_str][h_str] = {
40	                "quantization": {
41	                    "2": d2,
42	                    "4": d2 * RATIO_4BIT,
43	                    "8": d2 * RATIO_8BIT,
44	                }
45	            }
46	    return profiles
47	
48	
49	def main():
50	    parser = argparse.ArgumentParser(description="Phi-3-medium-14B constrained MCKP pipeline")
51	    parser.add_argument("--gpu", type=str, default="cuda:1")
52	    args = parser.parse_args()
53	
54	    device = args.gpu
55	    t0 = time.time()
56	
57	    config = AutoConfig.from_pretrained(MODEL_PATH, trust_remote_code=False)
58	    num_layers = config.num_hidden_layers
59	    num_kv_heads = config.num_key_value_heads
60	    num_q_heads = config.num_attention_heads
61	    gqa_ratio = num_q_heads // num_kv_heads
62	    total_kv_heads = num_layers * num_kv_heads
63	    print(f"Phi-3-medium-14B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")
64	
65	    # Load 2-bit-only profiles and synthesize multi-bit
66	    print(f"\nLoading profiles from {PROFILE_PATH}...")
67	    with open(PROFILE_PATH) as f:
68	        raw = json.load(f)
69	    raw_profiles = raw["profiles"] if "profiles" in raw else raw
70	    profiles = synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads)
71	    print(f"Synthesized multi-bit profiles: {num_layers} layers x {num_kv_heads} heads")
72	
73	    # Concentration analysis
74	    all_deltas_2bit = []
75	    for l_str in sorted(profiles.keys(), key=int):
76	        for h_str in sorted(profiles[l_str].keys(), key=int):
77	            d2 = profiles[l_str][h_str]["quantization"]["2"]
78	            all_deltas_2bit.append(d2)
79	    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
80	    n_top5 = max(1, int(len(sorted_d2) * 0.05))
81	    total_sum = sum(all_deltas_2bit)
82	    top5_sum = sum(sorted_d2[:n_top5])
83	    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0
84	    print(f"Top-5% concentration: {top5_concentration:.4f} (Spread pattern)")
85	
86	    # --- Solve allocations ---
87	    print(f"\n--- Solving allocations (budget={BUDGET}, max_2bit={MAX_2BIT}) ---")
88	
89	    constrained = solve_mckp_constrained(
90	        profiles, BUDGET, mode="quant_only",
91	        max_2bit=MAX_2BIT, l0_exclude_2bit=True)
92	
93	    unconstrained = solve_mckp(profiles, BUDGET, mode="quant_only")
94	
95	    greedy = solve_greedy_ratequant(profiles, budget=BUDGET, mode="quant_only")
96	
97	    uniform = uniform_quantization_baseline(profiles, bits=4)
98	
99	    for name, sol in [("Constrained MCKP", constrained),
100	                      ("Unconstrained MCKP", unconstrained),
101	                      ("Greedy", greedy),
102	                      ("Uniform-4bit", uniform)]:
103	        bits_dist = {}
104	        for k, v in sol["allocation"].items():
105	            b = int(v[1])
106	            bits_dist[b] = bits_dist.get(b, 0) + 1
107	        print(f"  {name}: mem={sol['actual_memory_ratio']:.4f}, "
108	              f"dist={sol['total_distortion']:.6f}, bits={bits_dist}")
109	
110	    # --- Load model ---
111	    print(f"\nLoading model in bf16 to {device}...")
112	    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)
113	    model = AutoModelForCausalLM.from_pretrained(
114	        MODEL_PATH, torch_dtype=torch.bfloat16,
115	        attn_implementation="eager", trust_remote_code=False
116	    )
117	    model = model.to(device)
118	    model.eval()
119	    mem_gb = torch.cuda.memory_allocated(device) / 1e9
120	    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")
121	
122	    # --- Eval: BF16 baseline ---
123	    print("\n[1/5] BF16 baseline PPL...")
124	    ppl_bf16 = evaluate_perplexity(model, tokenizer, device)
125	    print(f"  BF16 PPL = {ppl_bf16:.4f}")
126	
127	    # --- Eval: Uniform 4-bit ---
128	    print("\n[2/5] Uniform 4-bit PPL...")
129	    orig_fwds = patch_attention(model, uniform["allocation"])
130	    ppl_uniform = evaluate_perplexity(model, tokenizer, device)
131	    restore_attention(model, orig_fwds)
132	    print(f"  Uniform-4bit PPL = {ppl_uniform:.4f}")
133	
134	    # --- Eval: Constrained MCKP ---
135	    print("\n[3/5] Constrained MCKP PPL...")
136	    orig_fwds = patch_attention(model, constrained["allocation"])
137	    ppl_constrained = evaluate_perplexity(model, tokenizer, device)
138	    restore_attention(model, orig_fwds)
139	    print(f"  Constrained PPL = {ppl_constrained:.4f}")
140	
141	    # --- Eval: Unconstrained MCKP ---
142	    print("\n[4/5] Unconstrained MCKP PPL...")
143	    orig_fwds = patch_attention(model, unconstrained["allocation"])
144	    ppl_unconstrained = evaluate_perplexity(model, tokenizer, device)
145	    restore_attention(model, orig_fwds)
146	    print(f"  Unconstrained PPL = {ppl_unconstrained:.4f}")
147	
148	    # --- Eval: Greedy ---
149	    print("\n[5/5] Greedy PPL...")
150	    orig_fwds = patch_attention(model, greedy["allocation"])
151	    ppl_greedy = evaluate_perplexity(model, tokenizer, device)
152	    restore_attention(model, orig_fwds)
153	    print(f"  Greedy PPL = {ppl_greedy:.4f}")
154	
155	    # --- Save results ---
156	    elapsed = time.time() - t0
157	
158	    results = {
159	        "model": MODEL_PATH,
160	        "model_name": "Phi-3-medium-14B",
161	        "precision": "bfloat16",
162	        "architecture": {
163	            "num_layers": num_layers,
164	            "num_kv_heads": num_kv_heads,
165	            "num_attention_heads": num_q_heads,
166	            "head_dim": config.hidden_size // num_q_heads,
167	            "hidden_size": config.hidden_size,
168	            "gqa_ratio": gqa_ratio,
169	            "total_kv_heads": total_kv_heads,
170	        },
171	        "profiling_source": PROFILE_PATH,
172	        "synthesis": {"ratio_4bit": RATIO_4BIT, "ratio_8bit": RATIO_8BIT},
173	        "constraint": {"budget": BUDGET, "max_2bit": MAX_2BIT, "l0_exclude_2bit": True},
174	        "analysis": {"top5_concentration": round(top5_concentration, 4)},
175	        "ppl_bf16": round(ppl_bf16, 4),
176	        "ppl_uniform_4bit": round(ppl_uniform, 4),
177	        "ppl_constrained_mckp": round(ppl_constrained, 4),
178	        "ppl_unconstrained_mckp": round(ppl_unconstrained, 4),
179	        "ppl_greedy": round(ppl_greedy, 4),
180	        "delta_uniform": round(ppl_uniform - ppl_bf16, 4),
181	        "delta_constrained": round(ppl_constrained - ppl_bf16, 4),
182	        "delta_unconstrained": round(ppl_unconstrained - ppl_bf16, 4),
183	        "delta_greedy": round(ppl_greedy - ppl_bf16, 4),
184	        "constrained_vs_uniform": round(ppl_uniform - ppl_constrained, 4),
185	        "constrained_bit_distribution": constrained.get("bit_distribution", {}),
186	        "unconstrained_bit_distribution": unconstrained.get("bit_distribution", {}),
187	        "greedy_bit_distribution": greedy.get("bit_distribution", {}),
188	        "constrained_allocation": {k: list(v) for k, v in constrained["allocation"].items()},
189	        "elapsed_seconds": round(elapsed, 1),
190	    }
191	
192	    os.makedirs("artifacts", exist_ok=True)
193	    with open(OUTPUT_PATH, "w") as f:
194	        json.dump(results, f, indent=2)
195	    print(f"\nResults saved to {OUTPUT_PATH}")
196	
197	    # --- Summary ---
198	    print(f"\n{'='*65}")
199	    print("RESULTS — Phi-3-medium-14B Constrained MCKP Pipeline")
200	    print(f"{'='*65}")
201	    print(f"{'Method':<28} {'PPL':>10} {'Delta':>10} {'vs Uniform':>12}")
202	    print("-" * 65)
203	    print(f"{'Baseline (bf16)':<28} {ppl_bf16:>10.4f} {'---':>10} {'---':>12}")
204	    print(f"{'Constrained MCKP (k=8)':<28} {ppl_constrained:>10.4f} {ppl_constrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_constrained:>+12.4f}")
205	    print(f"{'Unconstrained MCKP':<28} {ppl_unconstrained:>10.4f} {ppl_unconstrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_unconstrained:>+12.4f}")
206	    print(f"{'Greedy':<28} {ppl_greedy:>10.4f} {ppl_greedy-ppl_bf16:>+10.4f} {ppl_uniform-ppl_greedy:>+12.4f}")
207	    print(f"{'Uniform 4-bit':<28} {ppl_uniform:>10.4f} {ppl_uniform-ppl_bf16:>+10.4f} {'---':>12}")
208	    print(f"\nTop-5% concentration: {top5_concentration:.4f}")
209	    print(f"Total time: {elapsed/60:.1f}min")
210	
211	
212	if __name__ == "__main__":
213	    main()
214	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "f0e1b3e3-8879-4b05-b2ad-6fef85e6b335",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py",
      "content": "\"\"\"Phi-3-medium-14B constrained MCKP + WikiText-2 eval pipeline.\n\nArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\nProfiling source: artifacts/phi3_medium_profiles_hires.json (2-bit only).\n4-bit/8-bit deltas synthesized from 2-bit via fixed ratios.\n\"\"\"\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\nos.environ[\"HF_DATASETS_OFFLINE\"] = \"1\"\n\nimport argparse\nimport json\nimport time\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\nfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\nfrom solver import (solve_mckp_constrained, solve_mckp,\n                    solve_greedy_ratequant, uniform_quantization_baseline)\n\nMODEL_PATH = \"/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\"\nPROFILE_PATH = \"artifacts/phi3_medium_profiles_hires.json\"\nOUTPUT_PATH = \"artifacts/phi3_medium_constrained_results.json\"\nBUDGET = 0.25\nMAX_2BIT = 8\nRATIO_4BIT = 0.25\nRATIO_8BIT = 0.05\n\n\ndef synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads):\n    \"\"\"Synthesize 4-bit and 8-bit deltas from 2-bit-only profiling data.\"\"\"\n    profiles = {}\n    for li in range(num_layers):\n        l_str = str(li)\n        layer_data = raw_profiles[l_str]\n        profiles[l_str] = {}\n        for hi in range(num_kv_heads):\n            h_str = str(hi)\n            d2 = layer_data[h_str][\"quantization\"][\"2\"]\n            profiles[l_str][h_str] = {\n                \"quantization\": {\n                    \"2\": d2,\n                    \"4\": d2 * RATIO_4BIT,\n                    \"8\": d2 * RATIO_8BIT,\n                }\n            }\n    return profiles\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Phi-3-medium-14B constrained MCKP pipeline\")\n    parser.add_argument(\"--gpu\", type=str, default=\"cuda:1\")\n    args = parser.parse_args()\n\n    device = args.gpu\n    t0 = time.time()\n\n    config = AutoConfig.from_pretrained(MODEL_PATH, trust_remote_code=False)\n    num_layers = config.num_hidden_layers\n    num_kv_heads = config.num_key_value_heads\n    num_q_heads = config.num_attention_heads\n    gqa_ratio = num_q_heads // num_kv_heads\n    total_kv_heads = num_layers * num_kv_heads\n    print(f\"Phi-3-medium-14B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\")\n\n    # Load 2-bit-only profiles and synthesize multi-bit\n    print(f\"\\nLoading profiles from {PROFILE_PATH}...\")\n    with open(PROFILE_PATH) as f:\n        raw = json.load(f)\n    raw_profiles = raw[\"profiles\"] if \"profiles\" in raw else raw\n    profiles = synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads)\n    print(f\"Synthesized multi-bit profiles: {num_layers} layers x {num_kv_heads} heads\")\n\n    # Concentration analysis\n    all_deltas_2bit = []\n    for l_str in sorted(profiles.keys(), key=int):\n        for h_str in sorted(profiles[l_str].keys(), key=int):\n            d2 = profiles[l_str][h_str][\"quantization\"][\"2\"]\n            all_deltas_2bit.append(d2)\n    sorted_d2 = sorted(all_deltas_2bit, reverse=True)\n    n_top5 = max(1, int(len(sorted_d2) * 0.05))\n    total_sum = sum(all_deltas_2bit)\n    top5_sum = sum(sorted_d2[:n_top5])\n    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\n    print(f\"Top-5% concentration: {top5_concentration:.4f} (Spread pattern)\")\n\n    # --- Solve allocations ---\n    print(f\"\\n--- Solving allocations (budget={BUDGET}, max_2bit={MAX_2BIT}) ---\")\n\n    constrained = solve_mckp_constrained(\n        profiles, BUDGET, mode=\"quant_only\",\n        max_2bit=MAX_2BIT, l0_exclude_2bit=True)\n\n    unconstrained = solve_mckp(profiles, BUDGET, mode=\"quant_only\")\n\n    greedy = solve_greedy_ratequant(profiles, budget=BUDGET, mode=\"quant_only\")\n\n    uniform = uniform_quantization_baseline(profiles, bits=4)\n\n    for name, sol in [(\"Constrained MCKP\", constrained),\n                      (\"Unconstrained MCKP\", unconstrained),\n                      (\"Greedy\", greedy),\n                      (\"Uniform-4bit\", uniform)]:\n        bits_dist = {}\n        for k, v in sol[\"allocation\"].items():\n            b = int(v[1])\n            bits_dist[b] = bits_dist.get(b, 0) + 1\n        print(f\"  {name}: mem={sol['actual_memory_ratio']:.4f}, \"\n              f\"dist={sol['total_distortion']:.6f}, bits={bits_dist}\")\n\n    # --- Load model ---\n    print(f\"\\nLoading model in bf16 to {device}...\")\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)\n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_PATH, torch_dtype=torch.bfloat16,\n        attn_implementation=\"eager\", trust_remote_code=False\n    )\n    model = model.to(device)\n    model.eval()\n    mem_gb = torch.cuda.memory_allocated(device) / 1e9\n    print(f\"Model loaded. GPU mem: {mem_gb:.1f}GB\")\n\n    # --- Eval: BF16 baseline ---\n    print(\"\\n[1/5] BF16 baseline PPL...\")\n    ppl_bf16 = evaluate_perplexity(model, tokenizer, device)\n    print(f\"  BF16 PPL = {ppl_bf16:.4f}\")\n\n    # --- Eval: Uniform 4-bit ---\n    print(\"\\n[2/5] Uniform 4-bit PPL...\")\n    orig_fwds = patch_attention(model, uniform[\"allocation\"])\n    ppl_uniform = evaluate_perplexity(model, tokenizer, device)\n    restore_attention(model, orig_fwds)\n    print(f\"  Uniform-4bit PPL = {ppl_uniform:.4f}\")\n\n    # --- Eval: Constrained MCKP ---\n    print(\"\\n[3/5] Constrained MCKP PPL...\")\n    orig_fwds = patch_attention(model, constrained[\"allocation\"])\n    ppl_constrained = evaluate_perplexity(model, tokenizer, device)\n    restore_attention(model, orig_fwds)\n    print(f\"  Constrained PPL = {ppl_constrained:.4f}\")\n\n    # --- Eval: Unconstrained MCKP ---\n    print(\"\\n[4/5] Unconstrained MCKP PPL...\")\n    orig_fwds = patch_attention(model, unconstrained[\"allocation\"])\n    ppl_unconstrained = evaluate_perplexity(model, tokenizer, device)\n    restore_attention(model, orig_fwds)\n    print(f\"  Unconstrained PPL = {ppl_unconstrained:.4f}\")\n\n    # --- Eval: Greedy ---\n    print(\"\\n[5/5] Greedy PPL...\")\n    orig_fwds = patch_attention(model, greedy[\"allocation\"])\n    ppl_greedy = evaluate_perplexity(model, tokenizer, device)\n    restore_attention(model, orig_fwds)\n    print(f\"  Greedy PPL = {ppl_greedy:.4f}\")\n\n    # --- Save results ---\n    elapsed = time.time() - t0\n\n    results = {\n        \"model\": MODEL_PATH,\n        \"model_name\": \"Phi-3-medium-14B\",\n        \"precision\": \"bfloat16\",\n        \"architecture\": {\n            \"num_layers\": num_layers,\n            \"num_kv_heads\": num_kv_heads,\n            \"num_attention_heads\": num_q_heads,\n            \"head_dim\": config.hidden_size // num_q_heads,\n            \"hidden_size\": config.hidden_size,\n            \"gqa_ratio\": gqa_ratio,\n            \"total_kv_heads\": total_kv_heads,\n        },\n        \"profiling_source\": PROFILE_PATH,\n        \"synthesis\": {\"ratio_4bit\": RATIO_4BIT, \"ratio_8bit\": RATIO_8BIT},\n        \"constraint\": {\"budget\": BUDGET, \"max_2bit\": MAX_2BIT, \"l0_exclude_2bit\": True},\n        \"analysis\": {\"top5_concentration\": round(top5_concentration, 4)},\n        \"ppl_bf16\": round(ppl_bf16, 4),\n        \"ppl_uniform_4bit\": round(ppl_uniform, 4),\n        \"ppl_constrained_mckp\": round(ppl_constrained, 4),\n        \"ppl_unconstrained_mckp\": round(ppl_unconstrained, 4),\n        \"ppl_greedy\": round(ppl_greedy, 4),\n        \"delta_uniform\": round(ppl_uniform - ppl_bf16, 4),\n        \"delta_constrained\": round(ppl_constrained - ppl_bf16, 4),\n        \"delta_unconstrained\": round(ppl_unconstrained - ppl_bf16, 4),\n        \"delta_greedy\": round(ppl_greedy - ppl_bf16, 4),\n        \"constrained_vs_uniform\": round(ppl_uniform - ppl_constrained, 4),\n        \"constrained_bit_distribution\": constrained.get(\"bit_distribution\", {}),\n        \"unconstrained_bit_distribution\": unconstrained.get(\"bit_distribution\", {}),\n        \"greedy_bit_distribution\": greedy.get(\"bit_distribution\", {}),\n        \"constrained_allocation\": {k: list(v) for k, v in constrained[\"allocation\"].items()},\n        \"elapsed_seconds\": round(elapsed, 1),\n    }\n\n    os.makedirs(\"artifacts\", exist_ok=True)\n    with open(OUTPUT_PATH, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nResults saved to {OUTPUT_PATH}\")\n\n    # --- Summary ---\n    print(f\"\\n{'='*65}\")\n    print(\"RESULTS — Phi-3-medium-14B Constrained MCKP Pipeline\")\n    print(f\"{'='*65}\")\n    print(f\"{'Method':<28} {'PPL':>10} {'Delta':>10} {'vs Uniform':>12}\")\n    print(\"-\" * 65)\n    print(f\"{'Baseline (bf16)':<28} {ppl_bf16:>10.4f} {'---':>10} {'---':>12}\")\n    print(f\"{'Constrained MCKP (k=8)':<28} {ppl_constrained:>10.4f} {ppl_constrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_constrained:>+12.4f}\")\n    print(f\"{'Unconstrained MCKP':<28} {ppl_unconstrained:>10.4f} {ppl_unconstrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_unconstrained:>+12.4f}\")\n    print(f\"{'Greedy':<28} {ppl_greedy:>10.4f} {ppl_greedy-ppl_bf16:>+10.4f} {ppl_uniform-ppl_greedy:>+12.4f}\")\n    print(f\"{'Uniform 4-bit':<28} {ppl_uniform:>10.4f} {ppl_uniform-ppl_bf16:>+10.4f} {'---':>12}\")\n    print(f\"\\nTop-5% concentration: {top5_concentration:.4f}\")\n    print(f\"Total time: {elapsed/60:.1f}min\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 214,
      "startLine": 1,
      "totalLines": 214
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01EW5NZw8YfXzLZRVUFkXNvj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "1cc4754b-7782-4339-85c5-cfeb78c139a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGKJkZYbBDz6q8Ri3C2vUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10495,
      "cache_read_input_tokens": 36528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10495
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

_source line 26 · 2026-05-16T02:48:10.515Z_

<details><summary>↩ Tool result · `toolu_01EW5NZw8YfXzLZRVUFkXNvj`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We use symmetric per-channel quantization with per-head granularity: each KV head is independently quantized to one of the candidate bit-widths $\mathcal{B} = \{2, 4, 8, 16\}$, without per-token scaling.
25	We profile each head by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
26	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
27	
28	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
29	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
30	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
31	
32	\subsection{Compounding Effect}
33	\label{sec:compounding}
34	
35	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively: truncation errors from multiple 2-bit heads accumulate through the residual stream, and once their count exceeds the network's capacity to compensate, PPL degrades super-linearly.
36	
37	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
38	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
39	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
40	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
41	
42	This compounding is specific to 2-bit quantization and is \emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\times$ at $k{=}64$.
43	A random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.
44	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
45	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
46	
47	The relationship between $k$ and PPL is U-shaped (Figure~\ref{fig:compounding}, Appendix~\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 10.89 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.
48	
49	\subsection{Cardinality Constraint}
50	\label{sec:cardinality}
51	
52	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
53	\begin{equation}
54	\label{eq:constraint}
55	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
56	\end{equation}
57	
58	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
59	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
60	
61	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
62	
63	One might expect Layer-0 heads to require explicit protection.
64	On Qwen2.5-7B, however, the profiler assigns very high 2-bit distortion to Layer-0 heads (L0H0: $+$31.9\%, L0H2: $+$23.2\%, L0H3: $+$11.7\% relative to bf16), so no solver would assign them 2-bit under any reasonable budget.
65	Running the solver with and without manual Layer-0 exclusion produces identical allocations; no manual rule is needed.
66	
67	\paragraph{Restoring additivity.}
68	The additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.
69	Restricting 2-bit heads to $k \ll H$ pushes the allocation back into a near-additive regime where the profiler's prediction agrees with measured PPL.
70	For Qwen2.5-7B, $k{=}8$ ($\sim$7\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\ref{fig:compounding}).
71	This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (10.91 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
72	
73	\subsection{Solver Equivalence}
74	\label{sec:solver_equiv}
75	
76	\begin{table}[t]
77	\centering
78	\small
79	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
80	\label{tab:solver_equiv}
81	\begin{tabular}{llcccc}
82	\toprule
83	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
84	 & & & 2-bit & 4-bit & 8/16-bit \\
85	\midrule
86	Greedy & None & 32.45 & 68 & 30 & 14 \\
87	MCKP & None & 36.92 & 75 & 33 & 4 \\
88	Greedy & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
89	MCKP & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
90	Uniform & --- & 15.45 & 0 & 112 & 0 \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	\footnotetext{Constrained results use high-resolution profiling; unconstrained rows use standard-resolution profiling to illustrate the failure mode (the exact PPL is irrelevant---any unconstrained allocation fails catastrophically).}
95	
96	With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (10.91), same bit distribution on Qwen2.5-7B.
97	
98	\paragraph{Empirical observation.}
99	When $k \ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.
100	The constraint restricts the feasible set so that the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this uniquely, so greedy's local choice coincides with the global optimum.
101	We verify this across three architectures: Qwen2.5-7B (112/112 heads identical), Llama-3.1-8B (256/256), Mistral-7B-v0.3 (255/256; the single difference is a zero-distortion tie with no PPL impact).
102	Without the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.
103	Practitioners can therefore use the simpler $O(H \log H)$ greedy algorithm without sacrificing optimality.
104	
105	A per-layer brute-force oracle on Qwen2.5-7B confirms near-optimality: of 8 layers with non-trivial allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL (0.4\% of the total improvement), closing the optimality chain from greedy through MCKP to brute-force.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "c9b568f1-efe8-4380-ae12-0d60fc942d4e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nWe formulate per-head KV cache quantization as a constrained optimization problem.\nLet $h \\in \\{1,\\ldots,H\\}$ index the KV heads across all layers, $b_h \\in \\mathcal{B}$ the bit-width assigned to head $h$, and $\\mathcal{B} = \\{2, 4, 8, 16\\}$ the set of hardware-aligned bit-widths.\nEach head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.\nGiven a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\\times$ compression), we seek the allocation that minimizes total distortion:\n\\begin{equation}\n\\label{eq:objective}\n\\min_{\\{b_h\\}} \\sum_{h=1}^{H} d_h(b_h) \\quad \\text{s.t.} \\quad \\frac{1}{H \\cdot 16}\\sum_{h=1}^{H} b_h \\leq R.\n\\end{equation}\n\nThis is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\\mathcal{B}$ to minimize total distortion under a budget.\nRateQuant~\\cite{zuo2026ratequant} solves this for consecutive bit-widths $\\{2,3,4,5,6\\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).\nHardware-aligned bit-widths $\\{2,4,8,16\\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.\nMoreover, as we show in \\S\\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.\n\n\\subsection{PPL-based Per-Head Profiling}\n\\label{sec:profiling}\n\nWe use symmetric per-channel quantization with per-head granularity: each KV head is independently quantized to one of the candidate bit-widths $\\mathcal{B} = \\{2, 4, 8, 16\\}$, without per-token scaling.\nWe profile each head by quantizing it to each $b \\in \\mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\\times$ 2048 tokens from WikiText-2 train.\nThis yields a distortion table of $H \\times |\\mathcal{B}|$ entries that serves as input to the solver.\n\nThe optimization in Eq.~\\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\\sum_h d_h(b_h)$.\nThis holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.\nAt 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.\n\n\\subsection{Compounding Effect}\n\\label{sec:compounding}\n\nWhen many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively: truncation errors from multiple 2-bit heads accumulate through the residual stream, and once their count exceeds the network's capacity to compensate, PPL degrades super-linearly.\n\nUnconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.\nOn Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).\nStandard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \\approx 0$, so most 2-bit assignments appear free to the additive objective.\nThe resulting additive prediction is $\\sum_h d_h(b_h) + \\text{baseline} \\approx 11$ PPL---$3\\text{--}4\\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.\n\nThis compounding is specific to 2-bit quantization and is \\emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\\times$ at $k{=}64$.\nA random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.\nAt 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).\nThe qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.\n\nThe relationship between $k$ and PPL is U-shaped (Figure~\\ref{fig:compounding}, Appendix~\\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 10.89 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.\n\n\\subsection{Cardinality Constraint}\n\\label{sec:cardinality}\n\nThe compounding effect motivates a simple addition to Eq.~\\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.\n\\begin{equation}\n\\label{eq:constraint}\n\\sum_{h=1}^{H} \\mathbb{1}[b_h = 2] \\leq k.\n\\end{equation}\n\nThe constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\\ref{fig:compounding}).\nFor Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\\sim$7\\% of heads).\n\nThe constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.\n\nOne might expect Layer-0 heads to require explicit protection.\nOn Qwen2.5-7B, however, the profiler assigns very high 2-bit distortion to Layer-0 heads (L0H0: $+$31.9\\%, L0H2: $+$23.2\\%, L0H3: $+$11.7\\% relative to bf16), so no solver would assign them 2-bit under any reasonable budget.\nRunning the solver with and without manual Layer-0 exclusion produces identical allocations; no manual rule is needed.\n\n\\paragraph{Restoring additivity.}\nThe additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.\nRestricting 2-bit heads to $k \\ll H$ pushes the allocation back into a near-additive regime where the profiler's prediction agrees with measured PPL.\nFor Qwen2.5-7B, $k{=}8$ ($\\sim$7\\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\\ref{fig:compounding}).\nThis explains the constrained--unconstrained gap in Table~\\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (10.91 PPL, matching the ${\\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\\text{--}4\\times$.\n\n\\subsection{Solver Equivalence}\n\\label{sec:solver_equiv}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Solver comparison on Qwen2.5-7B at $4\\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\\leq}8$) makes greedy and MCKP produce identical allocations.\\protect\\footnotemark}\n\\label{tab:solver_equiv}\n\\begin{tabular}{llcccc}\n\\toprule\nSolver & Constraint & PPL & \\multicolumn{3}{c}{Bit distribution} \\\\\n & & & 2-bit & 4-bit & 8/16-bit \\\\\n\\midrule\nGreedy & None & 32.45 & 68 & 30 & 14 \\\\\nMCKP & None & 36.92 & 75 & 33 & 4 \\\\\nGreedy & $k{\\leq}8$ & 10.91 & 8 & 100 & 4 \\\\\nMCKP & $k{\\leq}8$ & 10.91 & 8 & 100 & 4 \\\\\nUniform & --- & 15.45 & 0 & 112 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{Constrained results use high-resolution profiling; unconstrained rows use standard-resolution profiling to illustrate the failure mode (the exact PPL is irrelevant---any unconstrained allocation fails catastrophically).}\n\nWith the cardinality constraint, greedy and MCKP produce identical results (Table~\\ref{tab:solver_equiv}): same PPL (10.91), same bit distribution on Qwen2.5-7B.\n\n\\paragraph{Empirical observation.}\nWhen $k \\ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.\nThe constraint restricts the feasible set so that the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this uniquely, so greedy's local choice coincides with the global optimum.\nWe verify this across three architectures: Qwen2.5-7B (112/112 heads identical), Llama-3.1-8B (256/256), Mistral-7B-v0.3 (255/256; the single difference is a zero-distortion tie with no PPL impact).\nWithout the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.\nPractitioners can therefore use the simpler $O(H \\log H)$ greedy algorithm without sacrificing optimality.\n\nA per-layer brute-force oracle on Qwen2.5-7B confirms near-optimality: of 8 layers with non-trivial allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL (0.4\\% of the total improvement), closing the optimality chain from greedy through MCKP to brute-force.",
      "numLines": 105,
      "startLine": 1,
      "totalLines": 105
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now let me check for the actual results. The script has `MAX_2BIT = 8` (k=8). It also runs unconstrained MCKP and greedy. Let me check if the results JSON exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "2a89e72c-e4a9-4ef7-b21a-608115390d3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015q9B1YC416BYEyF6MYrGn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7365,
      "cache_read_input_tokens": 47023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7365
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

<details open><summary>🔧 Tool call — Bash · `toolu_012inboajQAA2NjmZdCoNZvW`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/phi3_medium_constrained_results.json 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in ['ppl_bf16','ppl_uniform_4bit','ppl_constrained_mckp','ppl_unconstrained_mckp','ppl_greedy','delta_uniform','delta_constrained','delta_unconstrained','delta_greedy','constrained_vs_uniform']}, indent=2))\"",
  "description": "Extract Phi-3 PPL results from artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "b3d55f1e-ea7d-42c7-8547-b1d2bebcb596",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015q9B1YC416BYEyF6MYrGn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7365,
      "cache_read_input_tokens": 47023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7365
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

_source line 29 · 2026-05-16T02:48:18.302Z_

<details><summary>↩ Tool result · reported error · `toolu_012inboajQAA2NjmZdCoNZvW`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import sys,json; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in ['ppl_bf16','ppl_uniform_4bit','ppl_constrained_mckp','ppl_unconstrained_mckp','ppl_greedy','delta_uniform','delta_constrained','delta_unconstrained','delta_greedy','constrained_vs_uniform']}, indent=2))
                       ~~~~~~~~~^^^^^^^^^^^
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "5dfeb287-d715-4118-bacd-5b3cab013499",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 1, in &lt;module>\n    import sys,json; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in ['ppl_bf16','ppl_uniform_4bit','ppl_constrained_mckp','ppl_unconstrained_mckp','ppl_greedy','delta_uniform','delta_constrained','delta_unconstrained','delta_greedy','constrained_vs_uniform']}, indent=2))\n                       ~~~~~~~~~^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/__init__.py\", line 298, in load\n    return loads(fp.read(),\n        cls=cls, object_hook=object_hook,\n        parse_float=parse_float, parse_int=parse_int,\n        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Glob · `toolu_01N7m3rRAv76wtt5fQ9GC9Nn`</summary>

```json
{
  "pattern": "artifacts/phi3*",
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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "71be09ea-73e4-4170-b074-3cec843c9fe7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsWR551MEyY4fRWzWgUQzo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 54388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 731
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

_source line 31 · 2026-05-16T02:48:21.347Z_

<details><summary>↩ Tool result · `toolu_01N7m3rRAv76wtt5fQ9GC9Nn`</summary>

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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "3d2396fe-bf55-4cad-9557-3feb8ab78bf4",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 23,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
The artifacts file doesn't exist locally. The experiment was run on the remote server. But the task gives us the data:
- baseline PPL = 5.636
- uniform 4-bit PPL = 5.799
- constrained MCKP PPL = 5.815

And from the script: MAX_2BIT = 8 (k=8).

The script also runs unconstrained MCKP and greedy, so in theory those results exist on the server. But the task only gives us 3 values. Since the task says to add these values, I'll use what's given. 

I don't have the unconstrained MCKP or greedy results locally, so I'll check if there's a log file or other output that might contain the full results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "82979f6f-fe49-4533-88e2-21fcab3dfa5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5ru17m1vEVNH8WWAguMHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 112,
      "cache_read_input_tokens": 55119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 112
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01L2o5fBDfNK4i17pg7nU89n`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs -name \"*phi3*\" 2>/dev/null | head -5",
  "description": "Find Phi-3 log files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "5410e455-dec0-4f94-91d3-365d16d6cfdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5ru17m1vEVNH8WWAguMHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 112,
      "cache_read_input_tokens": 55119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 112
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 34 · 2026-05-16T02:48:29.565Z_

<details><summary>↩ Tool result · `toolu_01L2o5fBDfNK4i17pg7nU89n`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_exp_phi3_medium_hires_profiling_20260515T154952.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_check_phi3_profiling_result_20260516T014722_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_exp_phi3_medium_hires_profiling_check_20260515T161633_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ops_check_phi3_and_codellama_status_20260515T183752_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_status_check_20260515T194308.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "e816da60-0680-43a1-ac53-850a7ad8d668",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_exp_phi3_medium_hires_profiling_20260515T154952.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_check_phi3_profiling_result_20260516T014722_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_exp_phi3_medium_hires_profiling_check_20260515T161633_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ops_check_phi3_and_codellama_status_20260515T183752_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_status_check_20260515T194308.log",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01UyYLJNgS6UhgEHsQYRHcnq`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs -name \"*phi3*constrained*\" 2>/dev/null | head -10",
  "description": "Find Phi-3 constrained pipeline logs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "c9025c06-11a0-4bc9-863f-e1f177fba774",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWaUEeFaymtzUye4iB3S4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 55231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 610
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

_source line 36 · 2026-05-16T02:48:32.426Z_

<details><summary>↩ Tool result · `toolu_01UyYLJNgS6UhgEHsQYRHcnq`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/chats/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/chats/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.lock
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "6f917fdb-d02a-46e8-9c89-68438a427c50",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/chats/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/chats/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.lock",
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01A5hbQsbZV5euiu2BbbufJ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "b8b531a4-8924-41c4-a522-17d31aca3900",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTertASzcftSH5s6WBo6En",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 55841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 372
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

_source line 38 · 2026-05-16T02:48:35.135Z_

<details><summary>↩ Tool result · `toolu_01A5hbQsbZV5euiu2BbbufJ6`</summary>

```text
1	{
2	  "raw": "实验正在运行。模型已加载，solver 分配完成，正在评估 WikiText-2 PPL。\n\n关键中间结果：\n- **Constrained MCKP**: 388×4bit + 8×2bit + 4×8bit (mem=0.25)\n- **Unconstrained MCKP**: 301×4bit + 66×2bit + 33×8bit (mem=0.25)\n- **Greedy**: 与 Unconstrained 完全一致\n- **Uniform-4bit**: 400×4bit (mem=0.25)\n- Constrained 总 distortion (2.47) 比 Uniform (2.61) 低 5.2%，说明非均匀分配在 Spread 模式下仍有收益\n\ntoken 长度警告是 Phi-3 的 131072 context window 限制，WikiText-2 eval 不受影响（每段 2048 tokens）。\n\n实验预计运行 ~30-40 分钟（14B 模型 5 次 PPL eval）。constrained MCKP 完成后再提交 compounding sweep（共享 cuda:1）。\n\n需要我等进程完成后自动提交 compounding sweep 吗？"
3	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "0c08ef8d-fd26-460b-9603-bde89f4f41af",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003_result.json",
      "content": "{\n  \"raw\": \"实验正在运行。模型已加载，solver 分配完成，正在评估 WikiText-2 PPL。\\n\\n关键中间结果：\\n- **Constrained MCKP**: 388×4bit + 8×2bit + 4×8bit (mem=0.25)\\n- **Unconstrained MCKP**: 301×4bit + 66×2bit + 33×8bit (mem=0.25)\\n- **Greedy**: 与 Unconstrained 完全一致\\n- **Uniform-4bit**: 400×4bit (mem=0.25)\\n- Constrained 总 distortion (2.47) 比 Uniform (2.61) 低 5.2%，说明非均匀分配在 Spread 模式下仍有收益\\n\\ntoken 长度警告是 Phi-3 的 131072 context window 限制，WikiText-2 eval 不受影响（每段 2048 tokens）。\\n\\n实验预计运行 ~30-40 分钟（14B 模型 5 次 PPL eval）。constrained MCKP 完成后再提交 compounding sweep（共享 cuda:1）。\\n\\n需要我等进程完成后自动提交 compounding sweep 吗？\"\n}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
This is a mid-run status update. Let me look for the final results. Let me check the log file itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "5532fc40-722d-4175-8ac1-2d9d93d61d13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BgZ2etCFSBt7RYqArZQ8N5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 56213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 484
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01LFi6a6Fv5owYbQtooHTCVm`</summary>

```json
{
  "command": "grep -i \"ppl\\|RESULTS\\|BF16\\|Uniform\\|Constrained\\|Unconstrained\\|Greedy\\|5\\.636\\|5\\.799\\|5\\.815\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.log 2>/dev/null | tail -30",
  "description": "Search Phi-3 log for PPL results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "f150329a-7a17-445d-9b66-6e631bd453a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BgZ2etCFSBt7RYqArZQ8N5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 56213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 484
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

_source line 41 · 2026-05-16T02:48:40.129Z_

<details><summary>↩ Tool result · `toolu_01LFi6a6Fv5owYbQtooHTCVm`</summary>

```text
&lt;persisted-output>
Output too large (83.4KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/b117a00fo.txt

Preview (first 2KB):
{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01Szo5S3HUHJfxL2hzDRsT2M","type":"tool_result","content":"File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py"}]},"parent_tool_use_id":null,"session_id":"9777ac37-86f8-49d9-81d6-d825292be565","uuid":"64142fc9-9231-4ae7-97e9-8ab9a66f16b9","timestamp":"2026-05-16T02:12:26.772Z","tool_use_result":{"type":"create","filePath":"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py","content":"\"\"\"Phi-3-medium-14B constrained MCKP + WikiText-2 eval pipeline.\n\nArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\nProfiling source: artifacts/phi3_medium_profiles_hires.json (2-bit only).\n4-bit/8-bit deltas synthesized from 2-bit via fixed ratios.\n\"\"\"\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\nos.environ[\"HF_DATASETS_OFFLINE\"] = \"1\"\n\nimport argparse\nimport json\nimport time\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\nfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\nfrom solver import (solve_mckp_constrained, solve_mckp,\n                    solve_greedy_ratequant, uniform_quantization_baseline)\n\nMODEL_PATH = \"/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\"\nPROFILE_PATH = \"artifacts/phi3_medium_profiles_hires.json\"\nOUTPUT_PATH = \"artifacts/phi3_medium_constrained_results.json\"\nBUDGET = 0.25\nMAX_2BIT = 8\nRATIO_4BIT = 0.25\nRATIO_8BIT = 0.05\n\n\ndef synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads):\n    \"\"\"Synthesize 4-bit and 8-bit deltas from 2-bit-only profiling data.\"\"\"\n    profiles = {}\n    for li in range(num_layers):\n        l_str = str(li)\n        layer_data = raw_profiles[l_str]\n        profiles[l_str] = {}\n        for hi in range(num_kv_heads):\n            h_str = str(hi)\
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "1591ba05-99ce-4c57-81d1-74c9ae337644",
  "tool_use_result": {
    "stdout": "{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01Szo5S3HUHJfxL2hzDRsT2M\",\"type\":\"tool_result\",\"content\":\"File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py\"}]},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"64142fc9-9231-4ae7-97e9-8ab9a66f16b9\",\"timestamp\":\"2026-05-16T02:12:26.772Z\",\"tool_use_result\":{\"type\":\"create\",\"filePath\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_constrained_pipeline.py\",\"content\":\"\\\"\\\"\\\"Phi-3-medium-14B constrained MCKP + WikiText-2 eval pipeline.\\n\\nArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\\nProfiling source: artifacts/phi3_medium_profiles_hires.json (2-bit only).\\n4-bit/8-bit deltas synthesized from 2-bit via fixed ratios.\\n\\\"\\\"\\\"\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n\\nimport argparse\\nimport json\\nimport time\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\nfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\\nfrom solver import (solve_mckp_constrained, solve_mckp,\\n                    solve_greedy_ratequant, uniform_quantization_baseline)\\n\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\\\"\\nPROFILE_PATH = \\\"artifacts/phi3_medium_profiles_hires.json\\\"\\nOUTPUT_PATH = \\\"artifacts/phi3_medium_constrained_results.json\\\"\\nBUDGET = 0.25\\nMAX_2BIT = 8\\nRATIO_4BIT = 0.25\\nRATIO_8BIT = 0.05\\n\\n\\ndef synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads):\\n    \\\"\\\"\\\"Synthesize 4-bit and 8-bit deltas from 2-bit-only profiling data.\\\"\\\"\\\"\\n    profiles = {}\\n    for li in range(num_layers):\\n        l_str = str(li)\\n        layer_data = raw_profiles[l_str]\\n        profiles[l_str] = {}\\n        for hi in range(num_kv_heads):\\n            h_str = str(hi)\\n            d2 = layer_data[h_str][\\\"quantization\\\"][\\\"2\\\"]\\n            profiles[l_str][h_str] = {\\n                \\\"quantization\\\": {\\n                    \\\"2\\\": d2,\\n                    \\\"4\\\": d2 * RATIO_4BIT,\\n                    \\\"8\\\": d2 * RATIO_8BIT,\\n                }\\n            }\\n    return profiles\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Phi-3-medium-14B constrained MCKP pipeline\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=str, default=\\\"cuda:1\\\")\\n    args = parser.parse_args()\\n\\n    device = args.gpu\\n    t0 = time.time()\\n\\n    config = AutoConfig.from_pretrained(MODEL_PATH, trust_remote_code=False)\\n    num_layers = config.num_hidden_layers\\n    num_kv_heads = config.num_key_value_heads\\n    num_q_heads = config.num_attention_heads\\n    gqa_ratio = num_q_heads // num_kv_heads\\n    total_kv_heads = num_layers * num_kv_heads\\n    print(f\\\"Phi-3-medium-14B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\\\")\\n\\n    # Load 2-bit-only profiles and synthesize multi-bit\\n    print(f\\\"\\\\nLoading profiles from {PROFILE_PATH}...\\\")\\n    with open(PROFILE_PATH) as f:\\n        raw = json.load(f)\\n    raw_profiles = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n    profiles = synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads)\\n    print(f\\\"Synthesized multi-bit profiles: {num_layers} layers x {num_kv_heads} heads\\\")\\n\\n    # Concentration analysis\\n    all_deltas_2bit = []\\n    for l_str in sorted(profiles.keys(), key=int):\\n        for h_str in sorted(profiles[l_str].keys(), key=int):\\n            d2 = profiles[l_str][h_str][\\\"quantization\\\"][\\\"2\\\"]\\n            all_deltas_2bit.append(d2)\\n    sorted_d2 = sorted(all_deltas_2bit, reverse=True)\\n    n_top5 = max(1, int(len(sorted_d2) * 0.05))\\n    total_sum = sum(all_deltas_2bit)\\n    top5_sum = sum(sorted_d2[:n_top5])\\n    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\\n    print(f\\\"Top-5% concentration: {top5_concentration:.4f} (Spread pattern)\\\")\\n\\n    # --- Solve allocations ---\\n    print(f\\\"\\\\n--- Solving allocations (budget={BUDGET}, max_2bit={MAX_2BIT}) ---\\\")\\n\\n    constrained = solve_mckp_constrained(\\n        profiles, BUDGET, mode=\\\"quant_only\\\",\\n        max_2bit=MAX_2BIT, l0_exclude_2bit=True)\\n\\n    unconstrained = solve_mckp(profiles, BUDGET, mode=\\\"quant_only\\\")\\n\\n    greedy = solve_greedy_ratequant(profiles, budget=BUDGET, mode=\\\"quant_only\\\")\\n\\n    uniform = uniform_quantization_baseline(profiles, bits=4)\\n\\n    for name, sol in [(\\\"Constrained MCKP\\\", constrained),\\n                      (\\\"Unconstrained MCKP\\\", unconstrained),\\n                      (\\\"Greedy\\\", greedy),\\n                      (\\\"Uniform-4bit\\\", uniform)]:\\n        bits_dist = {}\\n        for k, v in sol[\\\"allocation\\\"].items():\\n            b = int(v[1])\\n            bits_dist[b] = bits_dist.get(b, 0) + 1\\n        print(f\\\"  {name}: mem={sol['actual_memory_ratio']:.4f}, \\\"\\n              f\\\"dist={sol['total_distortion']:.6f}, bits={bits_dist}\\\")\\n\\n    # --- Load model ---\\n    print(f\\\"\\\\nLoading model in bf16 to {device}...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        MODEL_PATH, torch_dtype=torch.bfloat16,\\n        attn_implementation=\\\"eager\\\", trust_remote_code=False\\n    )\\n    model = model.to(device)\\n    model.eval()\\n    mem_gb = torch.cuda.memory_allocated(device) / 1e9\\n    print(f\\\"Model loaded. GPU mem: {mem_gb:.1f}GB\\\")\\n\\n    # --- Eval: BF16 baseline ---\\n    print(\\\"\\\\n[1/5] BF16 baseline PPL...\\\")\\n    ppl_bf16 = evaluate_perplexity(model, tokenizer, device)\\n    print(f\\\"  BF16 PPL = {ppl_bf16:.4f}\\\")\\n\\n    # --- Eval: Uniform 4-bit ---\\n    print(\\\"\\\\n[2/5] Uniform 4-bit PPL...\\\")\\n    orig_fwds = patch_attention(model, uniform[\\\"allocation\\\"])\\n    ppl_uniform = evaluate_perplexity(model, tokenizer, device)\\n    restore_attention(model, orig_fwds)\\n    print(f\\\"  Uniform-4bit PPL = {ppl_uniform:.4f}\\\")\\n\\n    # --- Eval: Constrained MCKP ---\\n    print(\\\"\\\\n[3/5] Constrained MCKP PPL...\\\")\\n    orig_fwds = patch_attention(model, constrained[\\\"allocation\\\"])\\n    ppl_constrained = evaluate_perplexity(model, tokenizer, device)\\n    restore_attention(model, orig_fwds)\\n    print(f\\\"  Constrained PPL = {ppl_constrained:.4f}\\\")\\n\\n    # --- Eval: Unconstrained MCKP ---\\n    print(\\\"\\\\n[4/5] Unconstrained MCKP PPL...\\\")\\n    orig_fwds = patch_attention(model, unconstrained[\\\"allocation\\\"])\\n    ppl_unconstrained = evaluate_perplexity(model, tokenizer, device)\\n    restore_attention(model, orig_fwds)\\n    print(f\\\"  Unconstrained PPL = {ppl_unconstrained:.4f}\\\")\\n\\n    # --- Eval: Greedy ---\\n    print(\\\"\\\\n[5/5] Greedy PPL...\\\")\\n    orig_fwds = patch_attention(model, greedy[\\\"allocation\\\"])\\n    ppl_greedy = evaluate_perplexity(model, tokenizer, device)\\n    restore_attention(model, orig_fwds)\\n    print(f\\\"  Greedy PPL = {ppl_greedy:.4f}\\\")\\n\\n    # --- Save results ---\\n    elapsed = time.time() - t0\\n\\n    results = {\\n        \\\"model\\\": MODEL_PATH,\\n        \\\"model_name\\\": \\\"Phi-3-medium-14B\\\",\\n        \\\"precision\\\": \\\"bfloat16\\\",\\n        \\\"architecture\\\": {\\n            \\\"num_layers\\\": num_layers,\\n            \\\"num_kv_heads\\\": num_kv_heads,\\n            \\\"num_attention_heads\\\": num_q_heads,\\n            \\\"head_dim\\\": config.hidden_size // num_q_heads,\\n            \\\"hidden_size\\\": config.hidden_size,\\n            \\\"gqa_ratio\\\": gqa_ratio,\\n            \\\"total_kv_heads\\\": total_kv_heads,\\n        },\\n        \\\"profiling_source\\\": PROFILE_PATH,\\n        \\\"synthesis\\\": {\\\"ratio_4bit\\\": RATIO_4BIT, \\\"ratio_8bit\\\": RATIO_8BIT},\\n        \\\"constraint\\\": {\\\"budget\\\": BUDGET, \\\"max_2bit\\\": MAX_2BIT, \\\"l0_exclude_2bit\\\": True},\\n        \\\"analysis\\\": {\\\"top5_concentration\\\": round(top5_concentration, 4)},\\n        \\\"ppl_bf16\\\": round(ppl_bf16, 4),\\n        \\\"ppl_uniform_4bit\\\": round(ppl_uniform, 4),\\n        \\\"ppl_constrained_mckp\\\": round(ppl_constrained, 4),\\n        \\\"ppl_unconstrained_mckp\\\": round(ppl_unconstrained, 4),\\n        \\\"ppl_greedy\\\": round(ppl_greedy, 4),\\n        \\\"delta_uniform\\\": round(ppl_uniform - ppl_bf16, 4),\\n        \\\"delta_constrained\\\": round(ppl_constrained - ppl_bf16, 4),\\n        \\\"delta_unconstrained\\\": round(ppl_unconstrained - ppl_bf16, 4),\\n        \\\"delta_greedy\\\": round(ppl_greedy - ppl_bf16, 4),\\n        \\\"constrained_vs_uniform\\\": round(ppl_uniform - ppl_constrained, 4),\\n        \\\"constrained_bit_distribution\\\": constrained.get(\\\"bit_distribution\\\", {}),\\n        \\\"unconstrained_bit_distribution\\\": unconstrained.get(\\\"bit_distribution\\\", {}),\\n        \\\"greedy_bit_distribution\\\": greedy.get(\\\"bit_distribution\\\", {}),\\n        \\\"constrained_allocation\\\": {k: list(v) for k, v in constrained[\\\"allocation\\\"].items()},\\n        \\\"elapsed_seconds\\\": round(elapsed, 1),\\n    }\\n\\n    os.makedirs(\\\"artifacts\\\", exist_ok=True)\\n    with open(OUTPUT_PATH, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n    print(f\\\"\\\\nResults saved to {OUTPUT_PATH}\\\")\\n\\n    # --- Summary ---\\n    print(f\\\"\\\\n{'='*65}\\\")\\n    print(\\\"RESULTS — Phi-3-medium-14B Constrained MCKP Pipeline\\\")\\n    print(f\\\"{'='*65}\\\")\\n    print(f\\\"{'Method':<28} {'PPL':>10} {'Delta':>10} {'vs Uniform':>12}\\\")\\n    print(\\\"-\\\" * 65)\\n    print(f\\\"{'Baseline (bf16)':<28} {ppl_bf16:>10.4f} {'---':>10} {'---':>12}\\\")\\n    print(f\\\"{'Constrained MCKP (k=8)':<28} {ppl_constrained:>10.4f} {ppl_constrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_constrained:>+12.4f}\\\")\\n    print(f\\\"{'Unconstrained MCKP':<28} {ppl_unconstrained:>10.4f} {ppl_unconstrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_unconstrained:>+12.4f}\\\")\\n    print(f\\\"{'Greedy':<28} {ppl_greedy:>10.4f} {ppl_greedy-ppl_bf16:>+10.4f} {ppl_uniform-ppl_greedy:>+12.4f}\\\")\\n    print(f\\\"{'Uniform 4-bit':<28} {ppl_uniform:>10.4f} {ppl_uniform-ppl_bf16:>+10.4f} {'---':>12}\\\")\\n    print(f\\\"\\\\nTop-5% concentration: {top5_concentration:.4f}\\\")\\n    print(f\\\"Total time: {elapsed/60:.1f}min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"structuredPatch\":[],\"originalFile\":null,\"userModified\":false}}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-6\",\"id\":\"msg_01AKPqVwT6b4iEAUK3qfsCJU\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_015J6oZy1XUych5AycUDMQYw\",\"name\":\"Write\",\"input\":{\"file_path\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_compounding_sweep.py\",\"content\":\"\\\"\\\"\\\"Phi-3-medium-14B compounding sweep — measure super-additivity of 2-bit deltas.\\n\\nArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\\nProgressively apply 2-bit quantization to increasing numbers of heads\\n(sorted by individual delta, most sensitive first) and measure joint PPL.\\n\\\"\\\"\\\"\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n\\nimport argparse\\nimport json\\nimport math\\nimport time\\nimport torch\\nimport torch.nn.functional as F\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\nfrom eval_ppl import patch_attention, restore_attention\\n\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\\\"\\nPROFILE_PATH = \\\"artifacts/phi3_medium_profiles_hires.json\\\"\\nOUTPUT_PATH = \\\"artifacts/phi3_medium_compounding_sweep.json\\\"\\n\\n\\ndef load_calibration_data(tokenizer, path, num_samples, seq_len, device):\\n    with open(path) as f:\\n        samples = json.load(f)\\n    all_ids = []\\n    for s in samples:\\n        tokens = tokenizer.encode(s[\\\"text\\\"], add_special_tokens=False)\\n        if len(tokens) >= seq_len:\\n            all_ids.append(tokens[:seq_len])\\n        if len(all_ids) >= num_samples:\\n            break\\n    if not all_ids:\\n        raise RuntimeError(f\\\"No calibration seqs with >= {seq_len} tokens\\\")\\n    return torch.tensor(all_ids, dtype=torch.long, device=device)\\n\\n\\ndef compute_ppl_batched(model, input_ids, seq_len, batch_size, device):\\n    total_loss = 0.0\\n    total_tokens = 0\\n    n = input_ids.shape[0]\\n    with torch.no_grad():\\n        for start in range(0, n, batch_size):\\n            end = min(start + batch_size, n)\\n            batch = input_ids[start:end]\\n            outputs = model(\\n                batch, use_cache=False,\\n                cache_position=torch.arange(seq_len, device=device)\\n            )\\n            shift_logits = outputs.logits[:, :-1].contiguous()\\n            shift_labels = batch[:, 1:].contiguous()\\n            loss = F.cross_entropy(\\n                shift_logits.float().view(-1, shift_logits.shape[-1]),\\n                shift_labels.view(-1),\\n                reduction=\\\"sum\\\"\\n            )\\n            total_loss += loss.item()\\n            total_tokens += shift_labels.numel()\\n            del outputs, shift_logits, loss\\n            torch.cuda.empty_cache()\\n    return math.exp(total_loss / total_tokens)\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Phi-3-medium-14B compounding sweep\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=str, default=\\\"cuda:1\\\")\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=64)\\n    parser.add_argument(\\\"--seq_len\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=1)\\n    parser.add_argument(\\\"--calibration_data\\\", type=str, default=\\\"calibration_hires.json\\\")\\n    args = parser.parse_args()\\n\\n    device = args.gpu\\n    n_values = [1, 2, 4, 8, 16, 32, 64, 128, 200, 400]\\n    t0 = time.time()\\n\\n    # Load profiles\\n    print(\\\"Loading profiles...\\\")\\n    with open(PROFILE_PATH) as f:\\n        raw = json.load(f)\\n    profiles = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n\\n    head_deltas = []\\n    for l_str in sorted(profiles.keys(), key=int):\\n        for h_str in sorted(profiles[l_str].keys(), key=int):\\n            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n            head_deltas.append({\\n                \\\"layer\\\": int(l_str),\\n                \\\"head\\\": int(h_str),\\n                \\\"key\\\": f\\\"{l_str},{h_str}\\\",\\n                \\\"delta_2bit\\\": d2,\\n            })\\n    head_deltas.sort(key=lambda x: x[\\\"delta_2bit\\\"], reverse=True)\\n\\n    total_kv_heads = len(head_deltas)\\n    n_values = [n for n in n_values if n <= total_kv_heads]\\n    print(f\\\"Total KV heads: {total_kv_heads}\\\")\\n    print(f\\\"Sweep n values: {n_values}\\\")\\n    print(f\\\"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}\\\")\\n\\n    # Load model\\n    print(f\\\"\\\\nLoading {MODEL_PATH} in bf16 to {device}...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        MODEL_PATH, torch_dtype=torch.bfloat16,\\n        attn_implementation=\\\"eager\\\", trust_remote_code=False\\n    )\\n    model = model.to(device)\\n    model.eval()\\n    print(f\\\"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB\\\")\\n\\n    # Load calibration data\\n    print(f\\\"Loading calibration data ({args.num_samples} x {args.seq_len})...\\\")\\n    input_ids = load_calibration_data(\\n        tokenizer, args.calibration_data,\\n        args.num_samples, args.seq_len, device)\\n    print(f\\\"Loaded {input_ids.shape[0]} sequences\\\")\\n\\n    # Baseline\\n    print(\\\"\\\\nMeasuring baseline PPL...\\\")\\n    baseline_ppl = compute_ppl_batched(\\n        model, input_ids, args.seq_len, args.batch_size, device)\\n    print(f\\\"Baseline PPL: {baseline_ppl:.4f}\\\")\\n\\n    # Sweep\\n    results = []\\n    for n in n_values:\\n        print(f\\\"\\\\n--- n={n} ---\\\")\\n        top_n = head_deltas[:n]\\n        allocation = {h[\\\"key\\\"]: [\\\"quant\\\", 2] for h in top_n}\\n        sum_individual = sum(h[\\\"delta_2bit\\\"] for h in top_n)\\n\\n        orig_fwds = patch_attention(model, allocation)\\n        joint_ppl = compute_ppl_batched(\\n            model, input_ids, args.seq_len, args.batch_size, device)\\n        restore_attention(model, orig_fwds)\\n\\n        joint_delta = joint_ppl - baseline_ppl\\n        predicted_ppl = baseline_ppl + sum_individual\\n        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')\\n\\n        print(f\\\"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  \\\"\\n              f\\\"pred={predicted_ppl:.4f}  ratio={ratio:.4f}\\\")\\n\\n        results.append({\\n            \\\"n\\\": n,\\n            \\\"heads\\\": [h[\\\"key\\\"] for h in top_n],\\n            \\\"sum_individual_delta\\\": round(sum_individual, 6),\\n            \\\"joint_ppl\\\": round(joint_ppl, 4),\\n            \\\"joint_delta\\\": round(joint_delta, 6),\\n            \\\"predicted_ppl\\\": round(predicted_ppl, 4),\\n            \\\"super_additive_ratio\\\": round(ratio, 4),\\n        })\\n\\n    elapsed = time.time() - t0\\n\\n    output = {\\n        \\\"experiment\\\": \\\"phi3_medium_compounding_sweep\\\",\\n        \\\"model\\\": MODEL_PATH,\\n        \\\"model_name\\\": \\\"Phi-3-medium-14B\\\",\\n        \\\"pattern\\\": \\\"Spread\\\",\\n        \\\"baseline_ppl_measured\\\": round(baseline_ppl, 4),\\n        \\\"calibration\\\": {\\n            \\\"path\\\": args.calibration_data,\\n            \\\"num_samples\\\": args.num_samples,\\n            \\\"seq_len\\\": args.seq_len,\\n        },\\n        \\\"total_kv_heads\\\": total_kv_heads,\\n        \\\"results\\\": results,\\n        \\\"top_heads\\\": [\\n            {\\\"key\\\": h[\\\"key\\\"], \\\"delta_2bit\\\": round(h[\\\"delta_2bit\\\"], 6)}\\n            for h in head_deltas[:10]\\n        ],\\n        \\\"timing_seconds\\\": round(elapsed, 1),\\n    }\\n\\n    os.makedirs(\\\"artifacts\\\", exist_ok=True)\\n    with open(OUTPUT_PATH, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    print(f\\\"\\\\nJSON saved to {OUTPUT_PATH}\\\")\\n\\n    # Summary\\n    print(f\\\"\\\\n{'='*70}\\\")\\n    print(\\\"COMPOUNDING SWEEP — Phi-3-medium-14B (Spread, c=0.17)\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'n':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}\\\")\\n    print(\\\"-\\\" * 70)\\n    for r in results:\\n        print(f\\\"{r['n']:>5}  {r['sum_individual_delta']:>10.4f}  \\\"\\n              f\\\"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  \\\"\\n              f\\\"{r['super_additive_ratio']:>8.4f}\\\")\\n    print(f\\\"\\\\nTotal time: {elapsed/60:.1f}min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\"},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":1,\"cache_creation_input_tokens\":5514,\"cache_read_input_tokens\":51301,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":5514},\"output_tokens\":69,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"1df0a9a2-2c28-433a-a98e-6775d15d763e\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_015J6oZy1XUych5AycUDMQYw\",\"type\":\"tool_result\",\"content\":\"File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_compounding_sweep.py\"}]},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"b67e2f65-fe54-4030-b2c9-ef9e20837d5b\",\"timestamp\":\"2026-05-16T02:12:58.242Z\",\"tool_use_result\":{\"type\":\"create\",\"filePath\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_compounding_sweep.py\",\"content\":\"\\\"\\\"\\\"Phi-3-medium-14B compounding sweep — measure super-additivity of 2-bit deltas.\\n\\nArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\\nProgressively apply 2-bit quantization to increasing numbers of heads\\n(sorted by individual delta, most sensitive first) and measure joint PPL.\\n\\\"\\\"\\\"\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n\\nimport argparse\\nimport json\\nimport math\\nimport time\\nimport torch\\nimport torch.nn.functional as F\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\nfrom eval_ppl import patch_attention, restore_attention\\n\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\\\"\\nPROFILE_PATH = \\\"artifacts/phi3_medium_profiles_hires.json\\\"\\nOUTPUT_PATH = \\\"artifacts/phi3_medium_compounding_sweep.json\\\"\\n\\n\\ndef load_calibration_data(tokenizer, path, num_samples, seq_len, device):\\n    with open(path) as f:\\n        samples = json.load(f)\\n    all_ids = []\\n    for s in samples:\\n        tokens = tokenizer.encode(s[\\\"text\\\"], add_special_tokens=False)\\n        if len(tokens) >= seq_len:\\n            all_ids.append(tokens[:seq_len])\\n        if len(all_ids) >= num_samples:\\n            break\\n    if not all_ids:\\n        raise RuntimeError(f\\\"No calibration seqs with >= {seq_len} tokens\\\")\\n    return torch.tensor(all_ids, dtype=torch.long, device=device)\\n\\n\\ndef compute_ppl_batched(model, input_ids, seq_len, batch_size, device):\\n    total_loss = 0.0\\n    total_tokens = 0\\n    n = input_ids.shape[0]\\n    with torch.no_grad():\\n        for start in range(0, n, batch_size):\\n            end = min(start + batch_size, n)\\n            batch = input_ids[start:end]\\n            outputs = model(\\n                batch, use_cache=False,\\n                cache_position=torch.arange(seq_len, device=device)\\n            )\\n            shift_logits = outputs.logits[:, :-1].contiguous()\\n            shift_labels = batch[:, 1:].contiguous()\\n            loss = F.cross_entropy(\\n                shift_logits.float().view(-1, shift_logits.shape[-1]),\\n                shift_labels.view(-1),\\n                reduction=\\\"sum\\\"\\n            )\\n            total_loss += loss.item()\\n            total_tokens += shift_labels.numel()\\n            del outputs, shift_logits, loss\\n            torch.cuda.empty_cache()\\n    return math.exp(total_loss / total_tokens)\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Phi-3-medium-14B compounding sweep\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=str, default=\\\"cuda:1\\\")\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=64)\\n    parser.add_argument(\\\"--seq_len\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=1)\\n    parser.add_argument(\\\"--calibration_data\\\", type=str, default=\\\"calibration_hires.json\\\")\\n    args = parser.parse_args()\\n\\n    device = args.gpu\\n    n_values = [1, 2, 4, 8, 16, 32, 64, 128, 200, 400]\\n    t0 = time.time()\\n\\n    # Load profiles\\n    print(\\\"Loading profiles...\\\")\\n    with open(PROFILE_PATH) as f:\\n        raw = json.load(f)\\n    profiles = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n\\n    head_deltas = []\\n    for l_str in sorted(profiles.keys(), key=int):\\n        for h_str in sorted(profiles[l_str].keys(), key=int):\\n            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n            head_deltas.append({\\n                \\\"layer\\\": int(l_str),\\n                \\\"head\\\": int(h_str),\\n                \\\"key\\\": f\\\"{l_str},{h_str}\\\",\\n                \\\"delta_2bit\\\": d2,\\n            })\\n    head_deltas.sort(key=lambda x: x[\\\"delta_2bit\\\"], reverse=True)\\n\\n    total_kv_heads = len(head_deltas)\\n    n_values = [n for n in n_values if n <= total_kv_heads]\\n    print(f\\\"Total KV heads: {total_kv_heads}\\\")\\n    print(f\\\"Sweep n values: {n_values}\\\")\\n    print(f\\\"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}\\\")\\n\\n    # Load model\\n    print(f\\\"\\\\nLoading {MODEL_PATH} in bf16 to {device}...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        MODEL_PATH, torch_dtype=torch.bfloat16,\\n        attn_implementation=\\\"eager\\\", trust_remote_code=False\\n    )\\n    model = model.to(device)\\n    model.eval()\\n    print(f\\\"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB\\\")\\n\\n    # Load calibration data\\n    print(f\\\"Loading calibration data ({args.num_samples} x {args.seq_len})...\\\")\\n    input_ids = load_calibration_data(\\n        tokenizer, args.calibration_data,\\n        args.num_samples, args.seq_len, device)\\n    print(f\\\"Loaded {input_ids.shape[0]} sequences\\\")\\n\\n    # Baseline\\n    print(\\\"\\\\nMeasuring baseline PPL...\\\")\\n    baseline_ppl = compute_ppl_batched(\\n        model, input_ids, args.seq_len, args.batch_size, device)\\n    print(f\\\"Baseline PPL: {baseline_ppl:.4f}\\\")\\n\\n    # Sweep\\n    results = []\\n    for n in n_values:\\n        print(f\\\"\\\\n--- n={n} ---\\\")\\n        top_n = head_deltas[:n]\\n        allocation = {h[\\\"key\\\"]: [\\\"quant\\\", 2] for h in top_n}\\n        sum_individual = sum(h[\\\"delta_2bit\\\"] for h in top_n)\\n\\n        orig_fwds = patch_attention(model, allocation)\\n        joint_ppl = compute_ppl_batched(\\n            model, input_ids, args.seq_len, args.batch_size, device)\\n        restore_attention(model, orig_fwds)\\n\\n        joint_delta = joint_ppl - baseline_ppl\\n        predicted_ppl = baseline_ppl + sum_individual\\n        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')\\n\\n        print(f\\\"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  \\\"\\n              f\\\"pred={predicted_ppl:.4f}  ratio={ratio:.4f}\\\")\\n\\n        results.append({\\n            \\\"n\\\": n,\\n            \\\"heads\\\": [h[\\\"key\\\"] for h in top_n],\\n            \\\"sum_individual_delta\\\": round(sum_individual, 6),\\n            \\\"joint_ppl\\\": round(joint_ppl, 4),\\n            \\\"joint_delta\\\": round(joint_delta, 6),\\n            \\\"predicted_ppl\\\": round(predicted_ppl, 4),\\n            \\\"super_additive_ratio\\\": round(ratio, 4),\\n        })\\n\\n    elapsed = time.time() - t0\\n\\n    output = {\\n        \\\"experiment\\\": \\\"phi3_medium_compounding_sweep\\\",\\n        \\\"model\\\": MODEL_PATH,\\n        \\\"model_name\\\": \\\"Phi-3-medium-14B\\\",\\n        \\\"pattern\\\": \\\"Spread\\\",\\n        \\\"baseline_ppl_measured\\\": round(baseline_ppl, 4),\\n        \\\"calibration\\\": {\\n            \\\"path\\\": args.calibration_data,\\n            \\\"num_samples\\\": args.num_samples,\\n            \\\"seq_len\\\": args.seq_len,\\n        },\\n        \\\"total_kv_heads\\\": total_kv_heads,\\n        \\\"results\\\": results,\\n        \\\"top_heads\\\": [\\n            {\\\"key\\\": h[\\\"key\\\"], \\\"delta_2bit\\\": round(h[\\\"delta_2bit\\\"], 6)}\\n            for h in head_deltas[:10]\\n        ],\\n        \\\"timing_seconds\\\": round(elapsed, 1),\\n    }\\n\\n    os.makedirs(\\\"artifacts\\\", exist_ok=True)\\n    with open(OUTPUT_PATH, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    print(f\\\"\\\\nJSON saved to {OUTPUT_PATH}\\\")\\n\\n    # Summary\\n    print(f\\\"\\\\n{'='*70}\\\")\\n    print(\\\"COMPOUNDING SWEEP — Phi-3-medium-14B (Spread, c=0.17)\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'n':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}\\\")\\n    print(\\\"-\\\" * 70)\\n    for r in results:\\n        print(f\\\"{r['n']:>5}  {r['sum_individual_delta']:>10.4f}  \\\"\\n              f\\\"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  \\\"\\n              f\\\"{r['super_additive_ratio']:>8.4f}\\\")\\n    print(f\\\"\\\\nTotal time: {elapsed/60:.1f}min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"structuredPatch\":[],\"originalFile\":null,\"userModified\":false}}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-6\",\"id\":\"msg_01XysaSfxQQa1EBXmm5A6uUp\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_01X5dAb4Z7tbwGcgmQtQCTiB\",\"name\":\"Bash\",\"input\":{\"command\":\"git add run_phi3_medium_constrained_pipeline.py run_phi3_medium_compounding_sweep.py && git stash\",\"description\":\"Stage and stash new scripts for sync\"},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":1,\"cache_creation_input_tokens\":2667,\"cache_read_input_tokens\":56815,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":2667},\"output_tokens\":5,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"254b8050-28c0-4eb9-a16c-0bbcf24c8840\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01AEkWGeUAMRnPcGCwRbEPxB\",\"type\":\"tool_result\",\"content\":\"On branch master\\nChanges to be committed:\\n  (use \\\"git restore --staged &lt;file>...\\\" to unstage)\\n\\tnew file:   run_phi3_medium_compounding_sweep.py\\n\\tnew file:   run_phi3_medium_constrained_pipeline.py\\n\\nChanges not staged for commit:\\n  (use \\\"git add &lt;file>...\\\" to update what will be committed)\\n  (use \\\"git restore &lt;file>...\\\" to discard changes in working directory)\\n\\tmodified:   docs/paper/abstract.tex\\n\\tmodified:   docs/paper/analysis.tex\\n\\tmodified:   docs/paper/conclusion.tex\\n\\tmodified:   docs/paper/experiments.tex\\n\\tmodified:   docs/paper/figures/fig1_head_delta_heatmap.pdf\\n\\tmodified:   docs/paper/introduction.tex\\n\\tmodified:   docs/paper/main.aux\\n\\tmodified:   docs/paper/main.bbl\\n\\tmodified:   docs/paper/main.blg\\n\\tmodified:   docs/paper/main.fdb_latexmk\\n\\tmodified:   docs/paper/main.fls\\n\\tmodified:   docs/paper/main.log\\n\\tmodified:   docs/paper/main.out\\n\\tmodified:   docs/paper/main.pdf\\n\\tmodified:   docs/paper/method.tex\\n\\tmodified:   paper_provenance.yaml\\n\\tmodified:   run_kivi_baseline.py\\n\\tmodified:   run_pythia14b_constrained_pipeline.py\\n\\tmodified:   run_qwen7b_8k_spotcheck.py\\n\\tmodified:   run_qwen_hires_constrained.py\\n\\tmodified:   run_yi15_full_pipeline.py\\n\\nUntracked files:\\n  (use \\\"git add &lt;file>...\\\" to include in what will be committed)\\n\\t.claude/\\n\\tAGENTS.md\\n\\tROADMAP.lock\\n\\tROADMAP.md\\n\\t__pycache__/\\n\\tanalyze_codellama_profiling.py\\n\\tartifacts/\\n\\tcheckpoints/\\n\\tdecisions.lock\\n\\tdecisions.yaml\\n\\tdocs/IDEA_BRIEF.md\\n\\tdocs/paper/_pdf_images/\\n\\tdocs/paper/figures/fig_compounding_curves.pdf\\n\\tdocs/paper/figures/fig_compounding_curves.png\\n\\tdream_registry.lock\\n\\tdream_registry.yaml\\n\\tdream_registry.yaml.bak\\n\\texperiment_plan.lock\\n\\texperiment_plan.yaml\\n\\tfigures/\\n\\tgenerate_compounding_curves.py\\n\\tgenerate_hires_heatmap.py\\n\\tliterature_map.lock\\n\\tliterature_map.yaml\\",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/b117a00fo.txt",
    "persistedOutputSize": 85397
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01QxRRe9SRGhffKJWnwcHepv`</summary>

```json
{
  "command": "grep -o \"5\\.[0-9]\\{3,4\\}\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.log 2>/dev/null | sort -u | head -20",
  "description": "Extract PPL-like numbers from Phi-3 log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "a8de0330-0d88-4281-b99a-b5c75956dd79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXiNeoZ7P3DCcTMQGLmLuq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1156,
      "cache_read_input_tokens": 56697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1156
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 43 · 2026-05-16T02:48:43.999Z_

<details><summary>↩ Tool result · `toolu_01QxRRe9SRGhffKJWnwcHepv`</summary>

```text
5.344
5.710
5.755
5.758
5.808
5.966
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "22529285-16d5-4a51-84fe-9e1f6cc99568",
  "tool_use_result": {
    "stdout": "5.344\n5.710\n5.755\n5.758\n5.808\n5.966",
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

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Hmm, these numbers don't match 5.636, 5.799, 5.815. Let me search more broadly in the logs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "41231685-1d35-45c2-9ec9-c015a8aeb7b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqfC2Ka1Yt6Mz736jRD1ty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 57853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01HC738TX4VTbehrYQxJnnJ8`</summary>

```json
{
  "command": "grep -oP \"(BF16|bf16|Baseline|Uniform|Constrained|Unconstrained|Greedy).*?(\\d+\\.\\d{3,4})\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.log 2>/dev/null | tail -30",
  "description": "Extract labeled PPL values from Phi-3 log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "2ce54bc9-7e08-4076-bb84-e620b74f68b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqfC2Ka1Yt6Mz736jRD1ty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 57853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 46 · 2026-05-16T02:48:48.771Z_

<details><summary>↩ Tool result · `toolu_01HC738TX4VTbehrYQxJnnJ8`</summary>

```text
&lt;persisted-output>
Output too large (63KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/bxh9e659u.txt

Preview (first 2KB):
Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data.\"\"\"\n2\timport os\n3\tos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n4\tos.environ[\"HF_DATASETS_OFFLINE\"] = \"1\"\n5\t\n6\timport json\n7\timport time\n8\timport torch\n9\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\n10\tfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\n11\tfrom solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity\n12\t\n13\t\n14\tdef main():\n15\t    device = \"cuda:0\"\n16\t    model_name = \"Qwen/Qwen2.5-7B\"\n17\t    profiles_path = \"hires_profiles.json\"\n18\t    output_path = \"qwen_hires_constrained_results.json\"\n19\t    budget = 0.25\n20\t    max_2bit = 8\n21\t    t0 = time.time()\n22\t\n23\t    config = AutoConfig.from_pretrained(model_name)\n24\t    num_layers = config.num_hidden_layers\n25\t    num_kv_heads = config.num_key_value_heads\n26\t    num_q_heads = config.num_attention_heads\n27\t    gqa_ratio = num_q_heads // num_kv_heads\n28\t    total_kv_heads = num_layers * num_kv_heads\n29\t    print(f\"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\")\n30\t\n31\t    # Load D048 float32 hires profiling data\n32\t    print(f\"\\nLoading profiles from {profiles_path}...\")\n33\t    with open(profiles_path) as f:\n34\t        raw = json.load(f)\n35\t    profiles_raw = raw[\"profiles\"] if \"profiles\" in raw else raw\n36\t    print(f\"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer\")\n37\t\n38\t    profiles = enforce_monotonicity(profiles_raw)\n39\t\n40\t    # Constrained MCKP\n41\t    print(f\"\\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...\")\n42\t    mckp_result = solve_mckp_constrained(\n43\t        profiles, budget, mode=\"quant_only\",\n44\t        max_2bit=max_2bit, l0_exclude_2bit=True)\n45\t\n46\t    bit_counts = {}\n47\t    for key, (atype, param) in mckp_
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "43a333c3-fbfd-451e-bb05-737ed7977ef1",
  "tool_use_result": {
    "stdout": "Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data.\\\"\\\"\\\"\\n2\\timport os\\n3\\tos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n4\\tos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n5\\t\\n6\\timport json\\n7\\timport time\\n8\\timport torch\\n9\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\n10\\tfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\\n11\\tfrom solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity\\n12\\t\\n13\\t\\n14\\tdef main():\\n15\\t    device = \\\"cuda:0\\\"\\n16\\t    model_name = \\\"Qwen/Qwen2.5-7B\\\"\\n17\\t    profiles_path = \\\"hires_profiles.json\\\"\\n18\\t    output_path = \\\"qwen_hires_constrained_results.json\\\"\\n19\\t    budget = 0.25\\n20\\t    max_2bit = 8\\n21\\t    t0 = time.time()\\n22\\t\\n23\\t    config = AutoConfig.from_pretrained(model_name)\\n24\\t    num_layers = config.num_hidden_layers\\n25\\t    num_kv_heads = config.num_key_value_heads\\n26\\t    num_q_heads = config.num_attention_heads\\n27\\t    gqa_ratio = num_q_heads // num_kv_heads\\n28\\t    total_kv_heads = num_layers * num_kv_heads\\n29\\t    print(f\\\"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\\\")\\n30\\t\\n31\\t    # Load D048 float32 hires profiling data\\n32\\t    print(f\\\"\\\\nLoading profiles from {profiles_path}...\\\")\\n33\\t    with open(profiles_path) as f:\\n34\\t        raw = json.load(f)\\n35\\t    profiles_raw = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n36\\t    print(f\\\"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer\\\")\\n37\\t\\n38\\t    profiles = enforce_monotonicity(profiles_raw)\\n39\\t\\n40\\t    # Constrained MCKP\\n41\\t    print(f\\\"\\\\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...\\\")\\n42\\t    mckp_result = solve_mckp_constrained(\\n43\\t        profiles, budget, mode=\\\"quant_only\\\",\\n44\\t        max_2bit=max_2bit, l0_exclude_2bit=True)\\n45\\t\\n46\\t    bit_counts = {}\\n47\\t    for key, (atype, param) in mckp_result[\\\"allocation\\\"].items():\\n48\\t        b = int(param) if atype == \\\"quant\\\" else 16\\n49\\t        bit_counts[b] = bit_counts.get(b, 0) + 1\\n50\\t    print(f\\\"Bit distribution: {bit_counts}\\\")\\n51\\t    print(f\\\"Total distortion: {mckp_result['total_distortion']:.6f}\\\")\\n52\\t    print(f\\\"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}\\\")\\n53\\t\\n54\\t    # Load model for eval\\n55\\t    print(f\\\"\\\\nLoading model in bf16 to {device}...\\\")\\n56\\t    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n57\\t    model = AutoModelForCausalLM.from_pretrained(\\n58\\t        model_name, torch_dtype=torch.bfloat16, attn_implementation=\\\"eager\\\"\\n59\\t    )\\n60\\t    model = model.to(device)\\n61\\t    model.eval()\\n62\\t    mem_gb = torch.cuda.memory_allocated(device) / 1e9\\n63\\t    print(f\\\"Model loaded. GPU mem: {mem_gb:.1f}GB\\\")\\n64\\t\\n65\\t    # BF16 baseline WikiText-2\\n66\\t    print(\\\"\\\\nEvaluating bf16 baseline on WikiText-2...\\\")\\n67\\t    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)\\n68\\t    print(f\\\"BF16 WikiText-2 PPL: {baseline_wt2:.4f}\\\")\\n69\\t\\n70\\t    # MCKP eval\\n71\\t    print(\\\"\\\\nEvaluating constrained MCKP allocation on WikiText-2...\\\")\\n72\\t    orig_fwds = patch_attention(model, mckp_result[\\\"allocation\\\"])\\n73\\t    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)\\n74\\t    restore_attention(model, orig_fwds)\\n75\\t    print(f\\\"MCKP PPL: {mckp_wt2:.4f}\\\")\\n76\\t\\n77\\t    # Uniform 4-bit eval\\n78\\t    print(\\\"\\\\nEvaluating uniform 4-bit on WikiText-2...\\\")\\n79\\t    uniform_result = uniform_quantization_baseline(profiles, bits=4)\\n80\\t    orig_fwds = patch_attention(model, uniform_result[\\\"allocation\\\"])\\n81\\t    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)\\n82\\t    restore_attention(model, orig_fwds)\\n83\\t    print(f\\\"Uniform 4-bit PPL: {uniform_wt2:.4f}\\\")\\n84\\t\\n85\\t    delta = uniform_wt2 - mckp_wt2\\n86\\t    pct_improvement = delta / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0\\n87\\t    print(f\\\"\\\\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)\\\")\\n88\\t\\n89\\t    # Concentration analysis\\n90\\t    all_deltas_2bit = []\\n91\\t    for l_str in sorted(profiles.keys(), key=int):\\n92\\t        for h_str in sorted(profiles[l_str].keys(), key=int):\\n93\\t            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n94\\t            all_deltas_2bit.append(d2)\\n95\\t\\n96\\t    sorted_d2 = sorted(all_deltas_2bit, reverse=True)\\n97\\t    n_top5 = max(1, int(len(sorted_d2) * 0.05))\\n98\\t    total_sum = sum(all_deltas_2bit)\\n99\\t    top5_sum = sum(sorted_d2[:n_top5])\\n100\\t    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\\n101\\t\\n102\\t    total_time = time.time() - t0\\n103\\t\\n104\\t    results = {\\n105\\t        \\\"model\\\": model_name,\\n106\\t        \\\"model_name\\\": \\\"Qwen2.5-7B\\\",\\n107\\t        \\\"precision\\\": \\\"float32_hires_profiling\\\",\\n108\\t        \\\"architecture\\\": {\\n109\\t            \\\"num_layers\\\": num_layers,\\n110\\t            \\\"num_kv_heads\\\": num_kv_heads,\\n111\\t            \\\"num_attention_heads\\\": num_q_heads,\\n112\\t            \\\"head_dim\\\": config.hidden_size // num_q_heads,\\n113\\t            \\\"hidden_size\\\": config.hidden_size,\\n114\\t            \\\"gqa_ratio\\\": gqa_ratio,\\n115\\t            \\\"total_kv_heads\\\": total_kv_heads,\\n116\\t        },\\n117\\t        \\\"profiling_source\\\": \\\"qwen_float32_profiles.json (D048 float32 hires)\\\",\\n118\\t        \\\"constraint\\\": {\\\"max_2bit\\\": max_2bit, \\\"budget\\\": budget, \\\"l0_exclude_2bit\\\": True},\\n119\\t        \\\"baseline_wikitext2_ppl\\\": round(baseline_wt2, 4),\\n120\\t        \\\"mckp_wikitext2_ppl\\\": round(mckp_wt2, 4),\\n121\\t        \\\"uniform4bit_wikitext2_ppl\\\": round(uniform_wt2, 4),\\n122\\t        \\\"mckp_improvement_over_uniform\\\": round(delta, 4),\\n123\\t        \\\"mckp_improvement_pct\\\": round(pct_improvement, 2),\\n124\\t        \\\"bit_distribution\\\": bit_counts,\\n125\\t        \\\"mckp_total_distortion\\\": mckp_result[\\\"total_distortion\\\"],\\n126\\t        \\\"mckp_actual_memory_ratio\\\": mckp_result[\\\"actual_memory_ratio\\\"],\\n127\\t        \\\"allocation\\\": {k: list(v) for k, v in mckp_result[\\\"allocation\\\"].items()},\\n128\\t        \\\"analysis\\\": {\\n129\\t            \\\"top5_concentration\\\": round(top5_concentration, 4),\\n130\\t        },\\n131\\t        \\\"timing\\\": {\\\"total_seconds\\\": round(total_time, 1)},\\n132\\t    }\\n133\\t\\n134\\t    with open(output_path, \\\"w\\\") as f:\\n135\\t        json.dump(results, f, indent=2)\\n136\\t\\n137\\t    print(f\\\"\\\\n{'=' * 60}\\\")\\n138\\t    print(\\\"RESULTS — Qwen2.5-7B (float32 hires constrained MCKP)\\\")\\n139\\t    print(f\\\"{'=' * 60}\\\")\\n140\\t    print(f\\\"{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}\\\")\\n141\\t    print(\\\"-\\\" * 60)\\n142\\t    print(f\\\"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}\\\")\\n143\\t    print(f\\\"{'Constrained MCKP (k=8)':<30} {mckp_wt2:>10.4f} {delta:>+18.4f}\\\")\\n144\\t    print(f\\\"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}\\\")\\n145\\t    print(f\\\"\\\\nTop-5% concentration: {top5_concentration:.4f}\\\")\\n146\\t    print(f\\\"Bit distribution: {bit_counts}\\\")\\n147\\t    print(f\\\"Total time: {total_time / 60:.1f}min\\\")\\n148\\t    print(f\\\"Saved to {output_path}\\\")\\n149\\t\\n150\\t\\n151\\tif __name__ == \\\"__main__\\\":\\n152\\t    main()\\n153\\t\"}]},\"parent_tool_use_id\":\"toolu_01XJGBh9tLC6xXf7BqzDb53r\",\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"b5556c7c-8412-4936-a499-8192023d0ea8\",\"timestamp\":\"2026-05-16T02:10:22.258\nbf16 profiling — 2-bit only concentration measurement.\\n2\\tArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\\n3\\tOutput: artifacts/phi3_medium_profiles_hires.json, artifacts/phi3_medium_hires_bf16_2bitonly_results.json\\n4\\t\\\"\\\"\\\"\\n5\\timport os\\n6\\tos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n7\\tos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n8\\t\\n9\\timport argparse\\n10\\timport json\\n11\\timport math\\n12\\timport time\\n13\\timport torch\\n14\\timport torch.nn.functional as F\\n15\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\n16\\tfrom eval_ppl import patch_attention, restore_attention\\n17\\t\\n18\\t\\n19\\tdef load_calibration_data(tokenizer, path, num_samples, seq_len, device):\\n20\\t    with open(path) as f:\\n21\\t        samples = json.load(f)\\n22\\t    all_ids = []\\n23\\t    for s in samples:\\n24\\t        tokens = tokenizer.encode(s[\\\"text\\\"], add_special_tokens=False)\\n25\\t        if len(tokens) >= seq_len:\\n26\\t            all_ids.append(tokens[:seq_len])\\n27\\t        if len(all_ids) >= num_samples:\\n28\\t            break\\n29\\t    if not all_ids:\\n30\\t        raise RuntimeError(f\\\"No calibration seqs with >= {seq_len} tokens\\\")\\n31\\t    return torch.tensor(all_ids, dtype=torch.long, device=device)\\n32\\t\\n33\\t\\n34\\tdef compute_ppl_batched(model, input_ids, seq_len, batch_size, device):\\n35\\t    total_loss = 0.0\\n36\\t    total_tokens = 0\\n37\\t    n = input_ids.shape[0]\\n38\\t    with torch.no_grad():\\n39\\t        for start in range(0, n, batch_size):\\n40\\t            end = min(start + batch_size, n)\\n41\\t            batch = input_ids[start:end]\\n42\\t            outputs = model(\\n43\\t                batch, use_cache=False,\\n44\\t                cache_position=torch.arange(seq_len, device=device)\\n45\\t            )\\n46\\t            shift_logits = outputs.logits[:, :-1].contiguous()\\n47\\t            shift_labels = batch[:, 1:].contiguous()\\n48\\t            loss = F.cross_entropy(\\n49\\t                shift_logits.float().view(-1, shift_logits.shape[-1]),\\n50\\t                shift_labels.view(-1),\\n51\\t                reduction=\\\"sum\\\"\\n52\\t            )\\n53\\t            total_loss += loss.item()\\n54\\t            total_tokens += shift_labels.numel()\\n55\\t            del outputs, shift_logits, loss\\n56\\t            torch.cuda.empty_cache()\\n57\\t    return math.exp(total_loss / total_tokens)\\n58\\t\\n59\\t\\n60\\tdef profile_single_head(model, input_ids, seq_len, batch_size, device, baseline_ppl, layer, head, bits):\\n61\\t    if bits >= 16:\\n62\\t        return 0.0\\n63\\t    allocations = {f\\\"{layer},{head}\\\": [\\\"quant\\\", bits]}\\n64\\t    orig_fwds = patch_attention(model, allocations)\\n65\\t    ppl = compute_ppl_batched(model, input_ids, seq_len, batch_size, device)\\n66\\t    restore_attention(model, orig_fwds)\\n67\\t    return ppl - baseline_ppl\\n68\\t\\n69\\t\\n70\\tdef main():\\n71\\t    parser = argparse.ArgumentParser(description=\\\"Phi-3-medium-14B hires bf16 2-bit-only profiling\\\")\\n72\\t    parser.add_argument(\\\"--model\\\", type=str, default=\\\"/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\\\")\\n73\\t    parser.add_argument(\\\"--calibration_data\\\", type=str, default=\\\"calibration_hires.json\\\")\\n74\\t    parser.add_argument(\\\"--gpu\\\", type=str, default=\\\"cuda:1\\\")\\n75\\t    parser.add_argument(\\\"--batch_size\\\", type=int, default=1)\\n76\\t    parser.add_argument(\\\"--num_samples\\\", type=int, default=64)\\n77\\t    parser.add_argument(\\\"--seq_len\\\", type=int, default=2048)\\n78\\t    args = parser.parse_args()\\n79\\t\\n80\\t    device = args.gpu\\n81\\t    t0 = time.time()\\n82\\t\\n83\\t    config = AutoConfig.from_pretrained(args.model)\\n84\\t    num_layers = config.num_hidden_layers\\n85\\t    num_kv_heads = config.num_key_value_heads\\n86\\t    num_q_heads = config.num_attention_heads\\n87\\t    gqa_ratio = num_q_heads // num_kv_heads\\n88\\t    total_kv_heads = num_layers * num_kv_heads\\n89\\t\\n90\\t    print(f\\\"Phi-3-medium-14B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\\\")\\n91\\t\\n92\\t    print(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n93\\t    print(f\\\"BF16 2-bit-only Profiling ({args.num_samples}seq x {args.seq_len}tok)\\\")\\n94\\t    print(\\\"=\\\" * 60)\\n95\\t\\n96\\t    profile_start = time.time()\\n97\\t\\n98\\t    print(f\\\"Loading model in bf16 to {device}...\\\")\\n99\\t    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\\n100\\t    model = AutoModelForCausalLM.from_pretrained(\\n101\\t        args.model, torch_dtype=torch.bfloat16, attn_implementation=\\\"eager\\\",\\n102\\t        trust_remote_code=True\\n103\\t    )\\n104\\t    model = model.to(device)\\n105\\t    model.eval()\\n106\\t    mem_gb = torch.cuda.memory_allocated(device) / 1e9\\n107\\t    print(f\\\"BF16 model loaded. GPU mem: {mem_gb:.1f}GB\\\")\\n108\\t\\n109\\t    input_ids = load_calibration_data(tokenizer, args.calibration_data,\\n110\\t                                       args.num_samples, args.seq_len, device)\\n111\\t    print(f\\\"Calibration: {input_ids.shape[0]} seqs x {input_ids.shape[1]} tokens\\\")\\n112\\t\\n113\\t    print(\\\"Computing baseline PPL...\\\")\\n114\\t    baseline_ppl = compute_ppl_batched(model, input_ids, args.seq_len, args.batch_size, device)\\n115\\t    print(f\\\"Baseline PPL: {baseline_ppl:.4f}\\\")\\n116\\t\\n117\\t    total_evals = total_kv_heads\\n118\\t    done = 0\\n119\\t    profiles = {}\\n120\\t\\n121\\t    for l in range(num_layers):\\n122\\t        profiles[str(l)] = {}\\n123\\t        for h in range(num_kv_heads):\\n124\\t            delta = profile_single_head(\\n125\\t                model, input_ids, args.seq_len, args.batch_size,\\n126\\t                device, baseline_ppl, l, h, 2\\n127\\t            )\\n128\\t            profiles[str(l)][str(h)] = {\\\"quantization\\\": {\\\"2\\\": delta}}\\n129\\t            done += 1\\n130\\t            elapsed = time.time() - profile_start\\n131\\t            eta_min = (elapsed / done) * (total_evals - done) / 60\\n132\\t            print(f\\\"[{done}/{total_evals}] L{l}H{h} @2bit: delta={delta:.6f}  \\\"\\n133\\t                  f\\\"(elapsed {elapsed/60:.1f}min, ETA {eta_min:.0f}min)\\\", flush=True)\\n134\\t\\n135\\t    profile_time = time.time() - profile_start\\n136\\t\\n137\\t    os.makedirs(\\\"artifacts\\\", exist_ok=True)\\n138\\t    with open(\\\"artifacts/phi3_medium_profiles_hires.json\\\", \\\"w\\\") as f:\\n139\\t        json.dump(profiles, f, indent=2)\\n140\\t    print(f\\\"\\\\nProfiling done in {profile_time / 60:.1f}min\\\")\\n141\\t\\n142\\t    # ========== Concentration Analysis ==========\\n143\\t    print(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n144\\t    print(\\\"Concentration Analysis\\\")\\n145\\t    print(\\\"=\\\" * 60)\\n146\\t\\n147\\t    all_deltas_2bit = []\\n148\\t    layer_deltas = {}\\n149\\t    for l_str in sorted(profiles.keys(), key=int):\\n150\\t        l = int(l_str)\\n151\\t        layer_deltas[l] = []\\n152\\t        for h_str in sorted(profiles[l_str].keys(), key=int):\\n153\\t            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n154\\t            all_deltas_2bit.append((l, int(h_str), d2))\\n155\\t            layer_deltas[l].append(d2)\\n156\\t\\n157\\t    sorted_by_d2 = sorted(all_deltas_2bit, key=lambda x: -x[2])\\n158\\t    n_top5 = max(1, int(len(sorted_by_d2) * 0.05))\\n159\\t    total_sum = sum(x[2] for x in all_deltas_2bit)\\n160\\t    top5_sum = sum(x[2] for x in sorted_by_d2[:n_top5])\\n161\\t    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\\n162\\t\\n163\\t    l0_deltas = layer_deltas.get(0, [0])\\n164\\t    l0_mean = sum(l0_deltas) / max(len(l0_deltas), 1)\\n165\\t    other_means = []\\n166\\t    for l in range(1, num_layers):\\n167\\t        if l in layer_deltas and layer_deltas[l]:\\n168\\t            other_means.append(sum(layer_deltas[l]) / len(layer_deltas[l]))\\n169\\t    other_avg = sum(other_means) / len(other_means) if other_means else 0\\n170\\t    l0_ratio = l0_mean / other_avg if other_avg > 0 else float(\\\"inf\\\")\\n171\\t\\n172\\t    d_tensor = torch.tensor([x[2] for x in all_deltas_2bit])\\n173\\t    n_positive = int((d_tensor > 1e-6).sum().item())\\n174\\t    cv = d_tensor.std().item() / d_tensor.mean().item() if d_tensor.mean().item() > 0 else 0\\n175\\t\\n176\\t    print(f\\\"Top-5% concentration: {top5_concentration:.4f} ({n_top5} heads)\\\")\\n177\\t    print(f\\\"Layer 0 mean delta(2bit): {l0_mean:.6f}\\\")\\n178\\t    print(f\\\"Other layers mean delta(2bit): {other_avg:.6f}\\\")\\n179\\t    print(f\\\"L0 dominance ratio: {l0_ratio:.2f}x\\\")\\n180\\t    print(f\\\"Heads with positive delta: {n_positive}/{len(all_deltas_2bit)}\\\")\\n181\\t    print(f\\\"CV of delta(2bit): {cv:.4f}\\\")\\n182\\t\\n183\\t    print(\\\"\\\\nTop-5 most sensitive heads:\\\")\\n184\\t    for name_l, name_h, d2 in sorted_by_d2[:5]:\\n185\\t        print(f\\\"  L{name_l}H{name_h}: 2bit={d2:+.4f}\\\")\\n186\\t\\n187\\t    # ========== Save Results ==========\\n188\\t    total_time = time.time() - t0\\n189\\t\\n190\\t    results = {\\n191\\t        \\\"model\\\": args.model,\\n192\\t        \\\"model_name\\\": \\\"Phi-3-medium-14B\\\",\\n193\\t        \\\"precision\\\": \\\"bfloat16\\\",\\n194\\t        \\\"profiling_config\\\": {\\n195\\t            \\\"num_samples\\\": args.num_samples,\\n196\\t            \\\"seq_len\\\": args.seq_len,\\n197\\t            \\\"batch_size\\\": args.batch_size,\\n198\\t            \\\"bitwidths\\\": [2],\\n199\\t        },\\n200\\t        \\\"architecture\\\": {\\n201\\t            \\\"num_layers\\\": num_layers,\\n202\\t            \\\"num_kv_heads\\\": num_kv_heads,\\n203\\t            \\\"num_attention_heads\\\": num_q_heads,\\n204\\t            \\\"head_dim\\\": config.hidden_size // num_q_heads,\\n205\\t            \\\"hidden_size\\\": config.hidden_size,\\n206\\t            \\\"gqa_ratio\\\": gqa_ratio,\\n207\\t            \\\"total_kv_heads\\\": total_kv_heads,\\n208\\t        },\\n209\\t        \\\"baseline_calibration_ppl\\\": baseline_ppl,\\n210\\t        \\\"analysis\\\": {\\n211\\t            \\\"top5_concentration\\\": round(top5_concentration, 4),\\n212\\t            \\\"top5_n_heads\\\": n_top5,\\n213\\t            \\\"layer0_mean_delta_2bit\\\": round(l0_mean, 6),\\n214\\t            \\\"other_layers_mean_delta_2bit\\\": round(other_avg, 6),\\n215\\t            \\\"layer0_dominance_ratio\\\": round(l0_ratio, 2),\\n216\\t            \\\"delta_2bit_mean\\\": round(d_tensor.mean().item(), 6),\\n217\\t            \\\"delta_2bit_std\\\": round(d_tensor.std().item(), 6),\\n218\\t            \\\"delta_2bit_cv\\\": round(cv, 4),\\n219\\t            \\\"heads_with_positive_delta\\\": n_positive,\\n220\\t            \\\"total_heads\\\": len(all_deltas_2bit),\\n221\\t        },\\n222\\t        \\\"top5_sensitive_heads\\\": [\\n223\\t            {\\\"layer\\\": l, \\\"head\\\": h, \\\"delta_2bit\\\": round(d2, 6)}\\n224\\t            for l, h, d2 in sorted_by_d2[:5]\\n225\\t        ],\\n226\\t        \\\"timing\\\": {\\n227\\t            \\\"profile_seconds\\\": round(profile_time, 1),\\n228\\t            \\\"total_seconds\\\": round(total_time, 1),\\n229\\t        },\\n230\\t    }\\n231\\t\\n232\\t    with open(\\\"artifacts/phi3_medium_hires_bf16_2bitonly_results.json\\\", \\\"w\\\") as f:\\n233\\t        json.dump(results, f, indent=2)\\n234\\t\\n235\\t    print(f\\\"\\\\nTotal time: {total_time / 3600:.2f}h\\\")\\n236\\t    print(f\\\"Saved: artifacts/phi3_medium_profiles_hires.json, artifacts/phi3_medium_hires_bf16_2bitonly_results.json\\\")\\n237\\t\\n238\\t\\n239\\tif __name__ == \\\"__main__\\\":\\n240\\t    main()\\n241\\t\"}]},\"parent_tool_use_id\":\"toolu_01XJGBh9tLC6xXf7BqzDb53r\",\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"7d91e609-e091-474f-b39e-e24ee395cccf\",\"timestamp\":\"2026-05-16T02:10:22.666\nbf16, evaluates three methods (baseline, MCKP, uniform 4-bit) via WikiText-2 perplexity\\n- **Analysis**: Computes top-5% concentration of 2-bit deltas\\n- **Output**: Comprehensive JSON with architecture, results, bit distribution, timing, and allocation details\\n\\n## 2. generate_compounding_curves.py\\n\\nA visualization script that generates a cross-architecture comparison figure:\\n\\n- **Data structure**: Each model has name, pattern type, k values (number of 2-bit heads), PPL curves, color, marker, concentration\\n- **Models**: Qwen2.5-7B (Spread), Llama-3.1-8B (Spike), Mistral-7B-v0.3 (Flat)\\n- **Plot configuration**: Symlog x-scale, log y-scale, custom ticks, catastrophic threshold line at PPL=100\\n- **Output**: Saves PDF and PNG to docs/paper/figures directory\\n\\n## 3. run_phi3_medium_hires_profiling.py\\n\\nA profiling script for Phi-3-medium-14B focusing on 2-bit-only deltas:\\n\\n- **Architecture**: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads\\n- **Calibration data**: Loads from JSON with configurable seq_len (default 2048)\\n- **Profiling approach**: Per-head evaluation of 2-bit quantization impact on PPL\\n- **Batched evaluation**: Computes perplexity in batches to manage memory\\n- **Concentration analysis**: Top-5% concentration, layer-0 dominance ratio, CV calculation\\n- **Results structure**: Model info, architecture, baseline PPL, analysis metrics, timing\\n- **Output**: Two JSON files (profiles and results) in artifacts directory\\n\\n**Key patterns for creating Phi-3-medium constrained MCKP and compounding sweep scripts:**\\n\\n1. **Constrained MCKP script** should follow run_qwen_hires_constrained.py but:\\n   - Use Phi-3-medium architecture params (40L, 10KV heads)\\n   - Reference phi3_medium_profiles_hires.json as input\\n   - Keep the same constraint framework (max_2bit, budget)\\n   - Output to phi3_medium_hires_constrained_results.json\\n\\n2. **Compounding sweep script** should follow generate_compounding_curves.py but:\\n   - Add Phi-3-medium-14B data point with appropriate k values and PPL curve\\n   - Match the visualization style (marker, color, pattern)\\n   - Extract concentration value from profiling results\\n   - Include in cross-architecture comparison figure\"}]}]},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"c679003b-20a6-4537-b932-528696856d8a\",\"timestamp\":\"2026-05-16T02:10:32.902\nConstrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data.\\\"\\\"\\\"\\n2\\timport os\\n3\\tos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n4\\tos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n5\\t\\n6\\timport json\\n7\\timport time\\n8\\timport torch\\n9\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\n10\\tfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\\n11\\tfrom solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity\\n12\\t\\n13\\t\\n14\\tdef main():\\n15\\t    device = \\\"cuda:0\\\"\\n16\\t    model_name = \\\"Qwen/Qwen2.5-7B\\\"\\n17\\t    profiles_path = \\\"hires_profiles.json\\\"\\n18\\t    output_path = \\\"qwen_hires_constrained_results.json\\\"\\n19\\t    budget = 0.25\\n20\\t    max_2bit = 8\\n21\\t    t0 = time.time()\\n22\\t\\n23\\t    config = AutoConfig.from_pretrained(model_name)\\n24\\t    num_layers = config.num_hidden_layers\\n25\\t    num_kv_heads = config.num_key_value_heads\\n26\\t    num_q_heads = config.num_attention_heads\\n27\\t    gqa_ratio = num_q_heads // num_kv_heads\\n28\\t    total_kv_heads = num_layers * num_kv_heads\\n29\\t    print(f\\\"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\\\")\\n30\\t\\n31\\t    # Load D048 float32 hires profiling data\\n32\\t    print(f\\\"\\\\nLoading profiles from {profiles_path}...\\\")\\n33\\t    with open(profiles_path) as f:\\n34\\t        raw = json.load(f)\\n35\\t    profiles_raw = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n36\\t    print(f\\\"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer\\\")\\n37\\t\\n38\\t    profiles = enforce_monotonicity(profiles_raw)\\n39\\t\\n40\\t    # Constrained MCKP\\n41\\t    print(f\\\"\\\\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...\\\")\\n42\\t    mckp_result = solve_mckp_constrained(\\n43\\t        profiles, budget, mode=\\\"quant_only\\\",\\n44\\t        max_2bit=max_2bit, l0_exclude_2bit=True)\\n45\\t\\n46\\t    bit_counts = {}\\n47\\t    for key, (atype, param) in mckp_result[\\\"allocation\\\"].items():\\n48\\t        b = int(param) if atype == \\\"quant\\\" else 16\\n49\\t        bit_counts[b] = bit_counts.get(b, 0) + 1\\n50\\t    print(f\\\"Bit distribution: {bit_counts}\\\")\\n51\\t    print(f\\\"Total distortion: {mckp_result['total_distortion']:.6f}\\\")\\n52\\t    print(f\\\"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}\\\")\\n53\\t\\n54\\t    # Load model for eval\\n55\\t    print(f\\\"\\\\nLoading model in bf16 to {device}...\\\")\\n56\\t    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n57\\t    model = AutoModelForCausalLM.from_pretrained(\\n58\\t        model_name, torch_dtype=torch.bfloat16, attn_implementation=\\\"eager\\\"\\n59\\t    )\\n60\\t    model = model.to(device)\\n61\\t    model.eval()\\n62\\t    mem_gb = torch.cuda.memory_allocated(device) / 1e9\\n63\\t    print(f\\\"Model loaded. GPU mem: {mem_gb:.1f}GB\\\")\\n64\\t\\n65\\t    # BF16 baseline WikiText-2\\n66\\t    print(\\\"\\\\nEvaluating bf16 baseline on WikiText-2...\\\")\\n67\\t    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)\\n68\\t    print(f\\\"BF16 WikiText-2 PPL: {baseline_wt2:.4f}\\\")\\n69\\t\\n70\\t    # MCKP eval\\n71\\t    print(\\\"\\\\nEvaluating constrained MCKP allocation on WikiText-2...\\\")\\n72\\t    orig_fwds = patch_attention(model, mckp_result[\\\"allocation\\\"])\\n73\\t    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)\\n74\\t    restore_attention(model, orig_fwds)\\n75\\t    print(f\\\"MCKP PPL: {mckp_wt2:.4f}\\\")\\n76\\t\\n77\\t    # Uniform 4-bit eval\\n78\\t    print(\\\"\\\\nEvaluating uniform 4-bit on WikiText-2...\\\")\\n79\\t    uniform_result = uniform_quantization_baseline(profiles, bits=4)\\n80\\t    orig_fwds = patch_attention(model, uniform_result[\\\"allocation\\\"])\\n81\\t    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)\\n82\\t    restore_attention(model, orig_fwds)\\n83\\t    print(f\\\"Uniform 4-bit PPL: {uniform_wt2:.4f}\\\")\\n84\\t\\n85\\t    delta = uniform_wt2 - mckp_wt2\\n86\\t    pct_improvement = delta / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0\\n87\\t    print(f\\\"\\\\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)\\\")\\n88\\t\\n89\\t    # Concentration analysis\\n90\\t    all_deltas_2bit = []\\n91\\t    for l_str in sorted(profiles.keys(), key=int):\\n92\\t        for h_str in sorted(profiles[l_str].keys(), key=int):\\n93\\t            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n94\\t            all_deltas_2bit.append(d2)\\n95\\t\\n96\\t    sorted_d2 = sorted(all_deltas_2bit, reverse=True)\\n97\\t    n_top5 = max(1, int(len(sorted_d2) * 0.05))\\n98\\t    total_sum = sum(all_deltas_2bit)\\n99\\t    top5_sum = sum(sorted_d2[:n_top5])\\n100\\t    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\\n101\\t\\n102\\t    total_time = time.time() - t0\\n103\\t\\n104\\t    results = {\\n105\\t        \\\"model\\\": model_name,\\n106\\t        \\\"model_name\\\": \\\"Qwen2.5-7B\\\",\\n107\\t        \\\"precision\\\": \\\"float32_hires_profiling\\\",\\n108\\t        \\\"architecture\\\": {\\n109\\t            \\\"num_layers\\\": num_layers,\\n110\\t            \\\"num_kv_heads\\\": num_kv_heads,\\n111\\t            \\\"num_attention_heads\\\": num_q_heads,\\n112\\t            \\\"head_dim\\\": config.hidden_size // num_q_heads,\\n113\\t            \\\"hidden_size\\\": config.hidden_size,\\n114\\t            \\\"gqa_ratio\\\": gqa_ratio,\\n115\\t            \\\"total_kv_heads\\\": total_kv_heads,\\n116\\t        },\\n117\\t        \\\"profiling_source\\\": \\\"qwen_float32_profiles.json (D048 float32 hires)\\\",\\n118\\t        \\\"constraint\\\": {\\\"max_2bit\\\": max_2bit, \\\"budget\\\": budget, \\\"l0_exclude_2bit\\\": True},\\n119\\t        \\\"baseline_wikitext2_ppl\\\": round(baseline_wt2, 4),\\n120\\t        \\\"mckp_wikitext2_ppl\\\": round(mckp_wt2, 4),\\n121\\t        \\\"uniform4bit_wikitext2_ppl\\\": round(uniform_wt2, 4),\\n122\\t        \\\"mckp_improvement_over_uniform\\\": round(delta, 4),\\n123\\t        \\\"mckp_improvement_pct\\\": round(pct_improvement, 2),\\n124\\t        \\\"bit_distribution\\\": bit_counts,\\n125\\t        \\\"mckp_total_distortion\\\": mckp_result[\\\"total_distortion\\\"],\\n126\\t        \\\"mckp_actual_memory_ratio\\\": mckp_result[\\\"actual_memory_ratio\\\"],\\n127\\t        \\\"allocation\\\": {k: list(v) for k, v in mckp_result[\\\"allocation\\\"].items()},\\n128\\t        \\\"analysis\\\": {\\n129\\t            \\\"top5_concentration\\\": round(top5_concentration, 4),\\n130\\t        },\\n131\\t        \\\"timing\\\": {\\\"total_seconds\\\": round(total_time, 1)},\\n132\\t    }\\n133\\t\\n134\\t    with open(output_path, \\\"w\\\") as f:\\n135\\t        json.dump(results, f, indent=2)\\n136\\t\\n137\\t    print(f\\\"\\\\n{'=' * 60}\\\")\\n138\\t    print(\\\"RESULTS — Qwen2.5-7B (float32 hires constrained MCKP)\\\")\\n139\\t    print(f\\\"{'=' * 60}\\\")\\n140\\t    print(f\\\"{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}\\\")\\n141\\t    print(\\\"-\\\" * 60)\\n142\\t    print(f\\\"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}\\\")\\n143\\t    print(f\\\"{'Constrained MCKP (k=8)':<30} {mckp_wt2:>10.4f} {delta:>+18.4f}\\\")\\n144\\t    print(f\\\"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}\\\")\\n145\\t    print(f\\\"\\\\nTop-5% concentration: {top5_concentration:.4f}\\\")\\n146\\t    print(f\\\"Bit distribution: {bit_counts}\\\")\\n147\\t    print(f\\\"Total time: {total_time / 60:.1f}min\\\")\\n148\\t    print(f\\\"Saved to {output_path}\\\")\\n149\\t\\n150\\t\\n151\\tif __name__ == \\\"__main__\\\":\\n152\\t    main()\\n153\\t\"}]},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"71b3efd1-9066-4485-b5ef-5d5521765f82\",\"timestamp\":\"2026-05-16T02:10:35.344\nbf16 profiling — 2-bit only concentration measurement.\\n2\\tArchitecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.\\n3\\tOutput: artifacts/phi3_medium_profiles_hires.json, artifacts/phi3_medium_hires_bf16_2bitonly_results.json\\n4\\t\\\"\\\"\\\"\\n5\\timport os\\n6\\tos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n7\\tos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n8\\t\\n9\\timport argparse\\n10\\timport json\\n11\\timport math\\n12\\timport time\\n13\\timport torch\\n14\\timport torch.nn.functional as F\\n15\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\n16\\tfrom eval_ppl import patch_attention, restore_attention\\n17\\t\\n18\\t\\n19\\tdef load_calibration_data(tokenizer, path, num_samples, seq_len, device):\\n20\\t    with open(path) as f:\\n21\\t        samples = json.load(f)\\n22\\t    all_ids = []\\n23\\t    for s in samples:\\n24\\t        tokens = tokenizer.encode(s[\\\"text\\\"], add_special_tokens=False)\\n25\\t        if len(tokens) >= seq_len:\\n26\\t            all_ids.append(tokens[:seq_len])\\n27\\t        if len(all_ids) >= num_samples:\\n28\\t            break\\n29\\t    if not all_ids:\\n30\\t        raise RuntimeError(f\\\"No calibration seqs with >= {seq_len} tokens\\\")\\n31\\t    return torch.tensor(all_ids, dtype=torch.long, device=device)\\n32\\t\\n33\\t\\n34\\tdef compute_ppl_batched(model, input_ids, seq_len, batch_size, device):\\n35\\t    total_loss = 0.0\\n36\\t    total_tokens = 0\\n37\\t    n = input_ids.shape[0]\\n38\\t    with torch.no_grad():\\n39\\t        for start in range(0, n, batch_size):\\n40\\t            end = min(start + batch_size, n)\\n",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/bxh9e659u.txt",
    "persistedOutputSize": 64501
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01PxeXj5bwj7PHY2JrKsTAGp`</summary>

```json
{
  "command": "grep -oP \"PPL[^0-9]*(\\d+\\.\\d{3,4})\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/bxh9e659u.txt 2>/dev/null | tail -20",
  "description": "Extract PPL values from persisted output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "7cbf0d5c-eb9e-46ab-826b-4b0884a4bb13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ws4ZGQa7Ad6NwBhC5ZdPNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 58056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1193
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T02:48:55.378Z_

<details><summary>↩ Tool result · `toolu_01PxeXj5bwj7PHY2JrKsTAGp`</summary>

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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "809d7d4e-06c5-4b69-a0ac-4be30ef51ef4",
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01UjmrdoERxYrEtCFjyWLBL4`</summary>

```json
{
  "command": "grep \"5\\.636\\|5\\.799\\|5\\.815\\|5\\.808\\|5\\.758\\|5\\.755\\|5\\.710\\|5\\.966\\|5\\.344\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003.log 2>/dev/null | head -10",
  "description": "Find exact PPL values in Phi-3 log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "7a7a1d0c-3b9a-4d9b-b228-8b9a063575f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3aLayqsL6VkMFsGdxq28r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 59249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
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

_source line 50 · 2026-05-16T02:49:02.249Z_

<details><summary>↩ Tool result · `toolu_01UjmrdoERxYrEtCFjyWLBL4`</summary>

```text
&lt;persisted-output>
Output too large (48.2KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/bbg1fne8y.txt

Preview (first 2KB):
{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01Nc1ijwcNocG1nmA1qVwsXa","type":"tool_result","content":"1\t\"\"\"Qwen2.5-7B Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data.\"\"\"\n2\timport os\n3\tos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n4\tos.environ[\"HF_DATASETS_OFFLINE\"] = \"1\"\n5\t\n6\timport json\n7\timport time\n8\timport torch\n9\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\n10\tfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\n11\tfrom solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity\n12\t\n13\t\n14\tdef main():\n15\t    device = \"cuda:0\"\n16\t    model_name = \"Qwen/Qwen2.5-7B\"\n17\t    profiles_path = \"hires_profiles.json\"\n18\t    output_path = \"qwen_hires_constrained_results.json\"\n19\t    budget = 0.25\n20\t    max_2bit = 8\n21\t    t0 = time.time()\n22\t\n23\t    config = AutoConfig.from_pretrained(model_name)\n24\t    num_layers = config.num_hidden_layers\n25\t    num_kv_heads = config.num_key_value_heads\n26\t    num_q_heads = config.num_attention_heads\n27\t    gqa_ratio = num_q_heads // num_kv_heads\n28\t    total_kv_heads = num_layers * num_kv_heads\n29\t    print(f\"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\")\n30\t\n31\t    # Load D048 float32 hires profiling data\n32\t    print(f\"\\nLoading profiles from {profiles_path}...\")\n33\t    with open(profiles_path) as f:\n34\t        raw = json.load(f)\n35\t    profiles_raw = raw[\"profiles\"] if \"profiles\" in raw else raw\n36\t    print(f\"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer\")\n37\t\n38\t    profiles = enforce_monotonicity(profiles_raw)\n39\t\n40\t    # Constrained MCKP\n41\t    print(f\"\\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...\")\n42\t    mckp_result = solve_mckp_constrained(\n43\t        profiles, budg
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "dcbf607d-7dd6-406f-8666-bd98f00f50e4",
  "tool_use_result": {
    "stdout": "{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01Nc1ijwcNocG1nmA1qVwsXa\",\"type\":\"tool_result\",\"content\":\"1\\t\\\"\\\"\\\"Qwen2.5-7B Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data.\\\"\\\"\\\"\\n2\\timport os\\n3\\tos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n4\\tos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n5\\t\\n6\\timport json\\n7\\timport time\\n8\\timport torch\\n9\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\n10\\tfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\\n11\\tfrom solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity\\n12\\t\\n13\\t\\n14\\tdef main():\\n15\\t    device = \\\"cuda:0\\\"\\n16\\t    model_name = \\\"Qwen/Qwen2.5-7B\\\"\\n17\\t    profiles_path = \\\"hires_profiles.json\\\"\\n18\\t    output_path = \\\"qwen_hires_constrained_results.json\\\"\\n19\\t    budget = 0.25\\n20\\t    max_2bit = 8\\n21\\t    t0 = time.time()\\n22\\t\\n23\\t    config = AutoConfig.from_pretrained(model_name)\\n24\\t    num_layers = config.num_hidden_layers\\n25\\t    num_kv_heads = config.num_key_value_heads\\n26\\t    num_q_heads = config.num_attention_heads\\n27\\t    gqa_ratio = num_q_heads // num_kv_heads\\n28\\t    total_kv_heads = num_layers * num_kv_heads\\n29\\t    print(f\\\"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\\\")\\n30\\t\\n31\\t    # Load D048 float32 hires profiling data\\n32\\t    print(f\\\"\\\\nLoading profiles from {profiles_path}...\\\")\\n33\\t    with open(profiles_path) as f:\\n34\\t        raw = json.load(f)\\n35\\t    profiles_raw = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n36\\t    print(f\\\"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer\\\")\\n37\\t\\n38\\t    profiles = enforce_monotonicity(profiles_raw)\\n39\\t\\n40\\t    # Constrained MCKP\\n41\\t    print(f\\\"\\\\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...\\\")\\n42\\t    mckp_result = solve_mckp_constrained(\\n43\\t        profiles, budget, mode=\\\"quant_only\\\",\\n44\\t        max_2bit=max_2bit, l0_exclude_2bit=True)\\n45\\t\\n46\\t    bit_counts = {}\\n47\\t    for key, (atype, param) in mckp_result[\\\"allocation\\\"].items():\\n48\\t        b = int(param) if atype == \\\"quant\\\" else 16\\n49\\t        bit_counts[b] = bit_counts.get(b, 0) + 1\\n50\\t    print(f\\\"Bit distribution: {bit_counts}\\\")\\n51\\t    print(f\\\"Total distortion: {mckp_result['total_distortion']:.6f}\\\")\\n52\\t    print(f\\\"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}\\\")\\n53\\t\\n54\\t    # Load model for eval\\n55\\t    print(f\\\"\\\\nLoading model in bf16 to {device}...\\\")\\n56\\t    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n57\\t    model = AutoModelForCausalLM.from_pretrained(\\n58\\t        model_name, torch_dtype=torch.bfloat16, attn_implementation=\\\"eager\\\"\\n59\\t    )\\n60\\t    model = model.to(device)\\n61\\t    model.eval()\\n62\\t    mem_gb = torch.cuda.memory_allocated(device) / 1e9\\n63\\t    print(f\\\"Model loaded. GPU mem: {mem_gb:.1f}GB\\\")\\n64\\t\\n65\\t    # BF16 baseline WikiText-2\\n66\\t    print(\\\"\\\\nEvaluating bf16 baseline on WikiText-2...\\\")\\n67\\t    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)\\n68\\t    print(f\\\"BF16 WikiText-2 PPL: {baseline_wt2:.4f}\\\")\\n69\\t\\n70\\t    # MCKP eval\\n71\\t    print(\\\"\\\\nEvaluating constrained MCKP allocation on WikiText-2...\\\")\\n72\\t    orig_fwds = patch_attention(model, mckp_result[\\\"allocation\\\"])\\n73\\t    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)\\n74\\t    restore_attention(model, orig_fwds)\\n75\\t    print(f\\\"MCKP PPL: {mckp_wt2:.4f}\\\")\\n76\\t\\n77\\t    # Uniform 4-bit eval\\n78\\t    print(\\\"\\\\nEvaluating uniform 4-bit on WikiText-2...\\\")\\n79\\t    uniform_result = uniform_quantization_baseline(profiles, bits=4)\\n80\\t    orig_fwds = patch_attention(model, uniform_result[\\\"allocation\\\"])\\n81\\t    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)\\n82\\t    restore_attention(model, orig_fwds)\\n83\\t    print(f\\\"Uniform 4-bit PPL: {uniform_wt2:.4f}\\\")\\n84\\t\\n85\\t    delta = uniform_wt2 - mckp_wt2\\n86\\t    pct_improvement = delta / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0\\n87\\t    print(f\\\"\\\\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)\\\")\\n88\\t\\n89\\t    # Concentration analysis\\n90\\t    all_deltas_2bit = []\\n91\\t    for l_str in sorted(profiles.keys(), key=int):\\n92\\t        for h_str in sorted(profiles[l_str].keys(), key=int):\\n93\\t            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n94\\t            all_deltas_2bit.append(d2)\\n95\\t\\n96\\t    sorted_d2 = sorted(all_deltas_2bit, reverse=True)\\n97\\t    n_top5 = max(1, int(len(sorted_d2) * 0.05))\\n98\\t    total_sum = sum(all_deltas_2bit)\\n99\\t    top5_sum = sum(sorted_d2[:n_top5])\\n100\\t    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\\n101\\t\\n102\\t    total_time = time.time() - t0\\n103\\t\\n104\\t    results = {\\n105\\t        \\\"model\\\": model_name,\\n106\\t        \\\"model_name\\\": \\\"Qwen2.5-7B\\\",\\n107\\t        \\\"precision\\\": \\\"float32_hires_profiling\\\",\\n108\\t        \\\"architecture\\\": {\\n109\\t            \\\"num_layers\\\": num_layers,\\n110\\t            \\\"num_kv_heads\\\": num_kv_heads,\\n111\\t            \\\"num_attention_heads\\\": num_q_heads,\\n112\\t            \\\"head_dim\\\": config.hidden_size // num_q_heads,\\n113\\t            \\\"hidden_size\\\": config.hidden_size,\\n114\\t            \\\"gqa_ratio\\\": gqa_ratio,\\n115\\t            \\\"total_kv_heads\\\": total_kv_heads,\\n116\\t        },\\n117\\t        \\\"profiling_source\\\": \\\"qwen_float32_profiles.json (D048 float32 hires)\\\",\\n118\\t        \\\"constraint\\\": {\\\"max_2bit\\\": max_2bit, \\\"budget\\\": budget, \\\"l0_exclude_2bit\\\": True},\\n119\\t        \\\"baseline_wikitext2_ppl\\\": round(baseline_wt2, 4),\\n120\\t        \\\"mckp_wikitext2_ppl\\\": round(mckp_wt2, 4),\\n121\\t        \\\"uniform4bit_wikitext2_ppl\\\": round(uniform_wt2, 4),\\n122\\t        \\\"mckp_improvement_over_uniform\\\": round(delta, 4),\\n123\\t        \\\"mckp_improvement_pct\\\": round(pct_improvement, 2),\\n124\\t        \\\"bit_distribution\\\": bit_counts,\\n125\\t        \\\"mckp_total_distortion\\\": mckp_result[\\\"total_distortion\\\"],\\n126\\t        \\\"mckp_actual_memory_ratio\\\": mckp_result[\\\"actual_memory_ratio\\\"],\\n127\\t        \\\"allocation\\\": {k: list(v) for k, v in mckp_result[\\\"allocation\\\"].items()},\\n128\\t        \\\"analysis\\\": {\\n129\\t            \\\"top5_concentration\\\": round(top5_concentration, 4),\\n130\\t        },\\n131\\t        \\\"timing\\\": {\\\"total_seconds\\\": round(total_time, 1)},\\n132\\t    }\\n133\\t\\n134\\t    with open(output_path, \\\"w\\\") as f:\\n135\\t        json.dump(results, f, indent=2)\\n136\\t\\n137\\t    print(f\\\"\\\\n{'=' * 60}\\\")\\n138\\t    print(\\\"RESULTS — Qwen2.5-7B (float32 hires constrained MCKP)\\\")\\n139\\t    print(f\\\"{'=' * 60}\\\")\\n140\\t    print(f\\\"{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}\\\")\\n141\\t    print(\\\"-\\\" * 60)\\n142\\t    print(f\\\"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}\\\")\\n143\\t    print(f\\\"{'Constrained MCKP (k=8)':<30} {mckp_wt2:>10.4f} {delta:>+18.4f}\\\")\\n144\\t    print(f\\\"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}\\\")\\n145\\t    print(f\\\"\\\\nTop-5% concentration: {top5_concentration:.4f}\\\")\\n146\\t    print(f\\\"Bit distribution: {bit_counts}\\\")\\n147\\t    print(f\\\"Total time: {total_time / 60:.1f}min\\\")\\n148\\t    print(f\\\"Saved to {output_path}\\\")\\n149\\t\\n150\\t\\n151\\tif __name__ == \\\"__main__\\\":\\n152\\t    main()\\n153\\t\"}]},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"71b3efd1-9066-4485-b5ef-5d5521765f82\",\"timestamp\":\"2026-05-16T02:10:35.344Z\",\"tool_use_result\":{\"type\":\"text\",\"file\":{\"filePath\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_qwen_hires_constrained.py\",\"content\":\"\\\"\\\"\\\"Qwen2.5-7B Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data.\\\"\\\"\\\"\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\nos.environ[\\\"HF_DATASETS_OFFLINE\\\"] = \\\"1\\\"\\n\\nimport json\\nimport time\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig\\nfrom eval_ppl import patch_attention, restore_attention, evaluate_perplexity\\nfrom solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity\\n\\n\\ndef main():\\n    device = \\\"cuda:0\\\"\\n    model_name = \\\"Qwen/Qwen2.5-7B\\\"\\n    profiles_path = \\\"hires_profiles.json\\\"\\n    output_path = \\\"qwen_hires_constrained_results.json\\\"\\n    budget = 0.25\\n    max_2bit = 8\\n    t0 = time.time()\\n\\n    config = AutoConfig.from_pretrained(model_name)\\n    num_layers = config.num_hidden_layers\\n    num_kv_heads = config.num_key_value_heads\\n    num_q_heads = config.num_attention_heads\\n    gqa_ratio = num_q_heads // num_kv_heads\\n    total_kv_heads = num_layers * num_kv_heads\\n    print(f\\\"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads\\\")\\n\\n    # Load D048 float32 hires profiling data\\n    print(f\\\"\\\\nLoading profiles from {profiles_path}...\\\")\\n    with open(profiles_path) as f:\\n        raw = json.load(f)\\n    profiles_raw = raw[\\\"profiles\\\"] if \\\"profiles\\\" in raw else raw\\n    print(f\\\"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer\\\")\\n\\n    profiles = enforce_monotonicity(profiles_raw)\\n\\n    # Constrained MCKP\\n    print(f\\\"\\\\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...\\\")\\n    mckp_result = solve_mckp_constrained(\\n        profiles, budget, mode=\\\"quant_only\\\",\\n        max_2bit=max_2bit, l0_exclude_2bit=True)\\n\\n    bit_counts = {}\\n    for key, (atype, param) in mckp_result[\\\"allocation\\\"].items():\\n        b = int(param) if atype == \\\"quant\\\" else 16\\n        bit_counts[b] = bit_counts.get(b, 0) + 1\\n    print(f\\\"Bit distribution: {bit_counts}\\\")\\n    print(f\\\"Total distortion: {mckp_result['total_distortion']:.6f}\\\")\\n    print(f\\\"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}\\\")\\n\\n    # Load model for eval\\n    print(f\\\"\\\\nLoading model in bf16 to {device}...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        model_name, torch_dtype=torch.bfloat16, attn_implementation=\\\"eager\\\"\\n    )\\n    model = model.to(device)\\n    model.eval()\\n    mem_gb = torch.cuda.memory_allocated(device) / 1e9\\n    print(f\\\"Model loaded. GPU mem: {mem_gb:.1f}GB\\\")\\n\\n    # BF16 baseline WikiText-2\\n    print(\\\"\\\\nEvaluating bf16 baseline on WikiText-2...\\\")\\n    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)\\n    print(f\\\"BF16 WikiText-2 PPL: {baseline_wt2:.4f}\\\")\\n\\n    # MCKP eval\\n    print(\\\"\\\\nEvaluating constrained MCKP allocation on WikiText-2...\\\")\\n    orig_fwds = patch_attention(model, mckp_result[\\\"allocation\\\"])\\n    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)\\n    restore_attention(model, orig_fwds)\\n    print(f\\\"MCKP PPL: {mckp_wt2:.4f}\\\")\\n\\n    # Uniform 4-bit eval\\n    print(\\\"\\\\nEvaluating uniform 4-bit on WikiText-2...\\\")\\n    uniform_result = uniform_quantization_baseline(profiles, bits=4)\\n    orig_fwds = patch_attention(model, uniform_result[\\\"allocation\\\"])\\n    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)\\n    restore_attention(model, orig_fwds)\\n    print(f\\\"Uniform 4-bit PPL: {uniform_wt2:.4f}\\\")\\n\\n    delta = uniform_wt2 - mckp_wt2\\n    pct_improvement = delta / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0\\n    print(f\\\"\\\\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)\\\")\\n\\n    # Concentration analysis\\n    all_deltas_2bit = []\\n    for l_str in sorted(profiles.keys(), key=int):\\n        for h_str in sorted(profiles[l_str].keys(), key=int):\\n            d2 = profiles[l_str][h_str][\\\"quantization\\\"].get(\\\"2\\\", 0.0)\\n            all_deltas_2bit.append(d2)\\n\\n    sorted_d2 = sorted(all_deltas_2bit, reverse=True)\\n    n_top5 = max(1, int(len(sorted_d2) * 0.05))\\n    total_sum = sum(all_deltas_2bit)\\n    top5_sum = sum(sorted_d2[:n_top5])\\n    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0\\n\\n    total_time = time.time() - t0\\n\\n    results = {\\n        \\\"model\\\": model_name,\\n        \\\"model_name\\\": \\\"Qwen2.5-7B\\\",\\n        \\\"precision\\\": \\\"float32_hires_profiling\\\",\\n        \\\"architecture\\\": {\\n            \\\"num_layers\\\": num_layers,\\n            \\\"num_kv_heads\\\": num_kv_heads,\\n            \\\"num_attention_heads\\\": num_q_heads,\\n            \\\"head_dim\\\": config.hidden_size // num_q_heads,\\n            \\\"hidden_size\\\": config.hidden_size,\\n            \\\"gqa_ratio\\\": gqa_ratio,\\n            \\\"total_kv_heads\\\": total_kv_heads,\\n        },\\n        \\\"profiling_source\\\": \\\"qwen_float32_profiles.json (D048 float32 hires)\\\",\\n        \\\"constraint\\\": {\\\"max_2bit\\\": max_2bit, \\\"budget\\\": budget, \\\"l0_exclude_2bit\\\": True},\\n        \\\"baseline_wikitext2_ppl\\\": round(baseline_wt2, 4),\\n        \\\"mckp_wikitext2_ppl\\\": round(mckp_wt2, 4),\\n        \\\"uniform4bit_wikitext2_ppl\\\": round(uniform_wt2, 4),\\n        \\\"mckp_improvement_over_uniform\\\": round(delta, 4),\\n        \\\"mckp_improvement_pct\\\": round(pct_improvement, 2),\\n        \\\"bit_distribution\\\": bit_counts,\\n        \\\"mckp_total_distortion\\\": mckp_result[\\\"total_distortion\\\"],\\n        \\\"mckp_actual_memory_ratio\\\": mckp_result[\\\"actual_memory_ratio\\\"],\\n        \\\"allocation\\\": {k: list(v) for k, v in mckp_result[\\\"allocation\\\"].items()},\\n        \\\"analysis\\\": {\\n            \\\"top5_concentration\\\": round(top5_concentration, 4),\\n        },\\n        \\\"timing\\\": {\\\"total_seconds\\\": round(total_time, 1)},\\n    }\\n\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n\\n    print(f\\\"\\\\n{'=' * 60}\\\")\\n    print(\\\"RESULTS — Qwen2.5-7B (float32 hires constrained MCKP)\\\")\\n    print(f\\\"{'=' * 60}\\\")\\n    print(f\\\"{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}\\\")\\n    print(\\\"-\\\" * 60)\\n    print(f\\\"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}\\\")\\n    print(f\\\"{'Constrained MCKP (k=8)':<30} {mckp_wt2:>10.4f} {delta:>+18.4f}\\\")\\n    print(f\\\"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}\\\")\\n    print(f\\\"\\\\nTop-5% concentration: {top5_concentration:.4f}\\\")\\n    print(f\\\"Bit distribution: {bit_counts}\\\")\\n    print(f\\\"Total time: {total_time / 60:.1f}min\\\")\\n    print(f\\\"Saved to {output_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"numLines\":153,\"startLine\":1,\"totalLines\":153}}}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_019W2g7cZJ7dE9aKEbR34dmE\",\"type\":\"tool_result\",\"content\":\"1\\t\\\"\\\"\\\"Generate cross-architecture compounding curves figure for RateKV paper.\\\"\\\"\\\"\\n2\\timport matplotlib\\n3\\tmatplotlib.use('Agg')\\n4\\timport matplotlib.pyplot as plt\\n5\\timport matplotlib.ticker as mticker\\n6\\timport numpy as np\\n7\\t\\n8\\tplt.rcParams.update({\\n9\\t    'font.family': 'DejaVu Sans',\\n10\\t    'font.size': 11,\\n11\\t    'axes.titlesize': 13,\\n12\\t    'axes.labelsize': 12,\\n13\\t    'xtick.labelsize': 10,\\n14\\t    'ytick.labelsize': 10,\\n15\\t    'legend.fontsize': 9.5,\\n16\\t    'figure.dpi': 300,\\n17\\t    'savefig.dpi': 300,\\n18\\t    'savefig.bbox': 'tight',\\n19\\t    'savefig.pad_inches': 0.05,\\n20\\t    'axes.spines.top': False,\\n21\\t    'axes.spines.right': False,\\n22\\t    'lines.linewidth': 1.8,\\n23\\t})\\n24\\t\\n25\\tmodels = [\\n26\\t    {\\n27\\t        'name': 'Qwen2.5-7B',\\n28\\t        'pattern': 'Spread',\\n29\\t        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],\\n30\\t        'ppl': [9.8106, 9.83, 9.85, 10.0474, 10.40, 11.63, 23.2176, 98.75, 98.7523],\\n31\\t        'color': '#D55E00',\\n32\\t        'marker': '^',\\n33\\t        'conc': 0.61,\\n34\\t    },\\n35\\t    {\\n36\\t        'name': 'Llama-3.1-8B',\\n37\\t        'pattern': 'Spike',\\n38\\t        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],\\n39\\t        'ppl': [8.09, 8.12, 8.18, 8.23, 8.44, 9.05, 11.99, 40.21, 1519.19],\\n40\\t        'color': '#0072B2',\\n41\\t        'marker': 'o',\\n42\\t        'conc': 0.57,\\n43\\t    },\\n44\\t    {\\n45\\t        'name': 'Mistral-7B-v0.3',\\n46\\t        'pattern': 'Flat',\\n47\\t        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],\\n48\\t        'ppl': [7.04, 7.04, 7.05, 7.06, 7.11, 7.24, 7.77, 10.47, 45.28],\\n49\\t        'color': '#009E73',\\n50\\t        'marker': 's',\\n51\\t        'conc': 0.24,\\n52\\t    },\\n53\\t]\\n54\\t\\n55\\tfig, ax = plt.subplots(figsize=(7, 4.5))\\n56\\t\\n57\\tfor m in models:\\n58\\t    k_arr = np.array(m['k'])\\n59\\t    ppl_arr = np.array(m['ppl'])\\n60\\t    label = f\\\"{m['name']} ({m['pattern']}, $c$ = {m['conc']:.2f})\\\"\\n61\\t    ms = m.get('markersize', 6)\\n62\\t    ax.plot(k_arr, ppl_arr, marker=m['marker'], color=m['color'],\\n63\\t            markersize=ms, label=label, zorder=3, markeredgewidth=0.5,\\n64\\t            markeredgecolor='white')\\n65\\t\\n66\\tax.set_xscale('symlog', linthresh=1)\\n67\\tax.set_yscale('log')\\n68\\t\\n69\\txticks = [0, 2, 8, 32, 64, 128, 256]\\n70\\tax.set_xticks(xticks)\\n71\\tax.set_xticklabels([str(x) for x in xticks])\\n72\\tax.minorticks_off()\\n73\\t\\n74\\tax.yaxis.set_major_formatter(mticker.ScalarFormatter())\\n75\\tax.yaxis.get_major_formatter().set_scientific(False)\\n76\\tyticks = [7, 10, 20, 50, 100, 200, 500, 1500]\\n77\\tax.set_yticks(yticks)\\n78\\tax.set_yticklabels([str(y) for y in yticks])\\n79\\t\\n80\\tax.axhline(y=100, color='#e31a1c', linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)\\n81\\tax.text(260, 115, 'catastrophic', fontsize=8, color='#e31a1c',\\n82\\t        ha='right', va='bottom', style='italic')\\n83\\t\\n84\\tax.set_xlabel('Number of 2-bit heads ($k$)')\\n85\\tax.set_ylabel('Perplexity')\\n86\\tax.legend(loc='upper left', frameon=True, fancybox=False,\\n87\\t          edgecolor='#cccccc')\\n88\\t\\n89\\tax.set_ylim(5, 2000)\\n90\\t\\n91\\tOUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/figures'\\n92\\tfor fmt in ['pdf', 'png']:\\n93\\t    fig.savefig(f'{OUT}/fig_compounding_curves.{fmt}', bbox_inches='tight', dpi=300)\\n94\\tplt.close(fig)\\n95\\tprint(f'Saved to {OUT}/fig_compounding_curves.pdf')\\n96\\t\"}]},\"parent_tool_use_id\":null,\"session_id\":\"9777ac37-86f8-49d9-81d6-d825292be565\",\"uuid\":\"b6ba7517-94a8-4e01-a19c-a9318a934b46\",\"timestamp\":\"2026-05-16T02:10:35.808Z\",\"tool_use_result\":{\"type\":\"text\",\"file\":{\"filePath\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/generate_compounding_curves.py\",\"content\":\"\\\"\\\"\\\"Generate cross-architecture compounding curves figure for RateKV paper.\\\"\\\"\\\"\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport matplotlib.ticker as mticker\\nimport numpy as np\\n\\nplt.rcParams.update({\\n    'font.family': 'DejaVu Sans',\\n    'font.size': 11,\\n    'axes.titlesize': 13,\\n    'axes.labelsize': 12,\\n    'xtick.labelsize': 10,\\n    'ytick.labelsize': 10,\\n    'legend.fontsize': 9.5,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'axes.spines.top': False,\\n    'axes.spines.right': False,\\n    'lines.linewidth': 1.8,\\n})\\n\\nmodels = [\\n    {\\n        'name': 'Qwen2.5-7B',\\n        'pattern': 'Spread',\\n        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],\\n        'ppl': [9.8106, 9.83, 9.85, 10.0474, 10.40, 11.63, 23.2176, 98.75, 98.7523],\\n        'color': '#D55E00',\\n        'marker': '^',\\n        'conc': 0.61,\\n    },\\n    {\\n        'name': 'Llama-3.1-8B',\\n        'pattern': 'Spike',\\n        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],\\n        'ppl': [8.09, 8.12, 8.18, 8.23, 8.44, 9.05, 11.99, 40.21, 1519.19],\\n        'color': '#0072B2',\\n        'marker': 'o',\\n        'conc': 0.57,\\n    },\\n    {\\n        'name': 'Mistral-7B-v0.3',\\n        'pattern': 'Flat',\\n        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],\\n        'ppl': [7.04, 7.04, 7.05, 7.06, 7.11, 7.24, 7.77, 10.47, 45.28],\\n        'color': '#009E73',\\n        'marker': 's',\\n        'conc': 0.24,\\n    },\\n]\\n\\nfig, ax = plt.subplots(figsize=(7, 4.5))\\n\\nfor m in models:\\n    k_arr = np.array(m['k'])\\n    ppl_arr = np.array(m['ppl'])\\n    label = f\\\"{m['name']} ({m['pattern']}, $c$ = {m['conc']:.2f})\\\"\\n    ms = m.get('markersize', 6)\\n    ax.plot(k_arr, ppl_arr, marker=m['marker'], color=m['color'],\\n            markersize=ms, label=label, zorder=3, markeredgewidth=0.5,\\n            markeredgecolor='white')\\n\\nax.set_xscale('symlog', linthresh=1)\\nax.set_yscale('log')\\n\\nxticks = [0, 2, 8, 32, 64, 128, 256]\\nax.set_xticks(xticks)\\nax.set_xticklabels([str(x) for x in xticks])\\nax.minorticks_off()\\n\\nax.yaxis.set_major_formatter(mticker.ScalarFormatter())\\nax.yaxis.get_major_formatter().set_scientific(False)\\nyticks = [7, 10, 20, 50, 100, 200, 500, 1500]\\nax.set_yticks(yticks)\\nax.set_yticklabels([str(y) for y in yticks])\\n\\nax.axhline(y=100, color='#e31a1c', linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)\\nax.text(260, 115, 'catastrophic', fontsize=8, color='#e31a1c',\\n        ha='right', va='bottom', style='italic')\\n\\nax.set_xlabel('Number of 2-bit heads ($k$)')\\nax.set_ylabel('Perplexity')\\nax.legend(loc='upper left', frameon=True, fancybox=False,\\n          edgecolor='#cccccc')\\n\\nax.set_ylim(5, 2000)\\n\\nOUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/figures'\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUT}/fig_compounding_curves.{fmt}', bbox_inches='tight', dpi=300)\\nplt.close(fig)\\nprint(f'Saved to {OUT}/fig_compounding_curves.pdf')\\n\",\"numLines\":96,\"startLine\":1,\"totalLines\":96}}}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01BqFcHfQTuQCsAQoyCAgGbx\",\"type\":\"tool_result\",\"content\":\"IiIiUGhpLTMtbWVkaXVtLTE0QiBjb25zdHJhaW5lZCBNQ0tQICsgV2lraVRleHQtMiBldmFsIHBpcGVsaW5lLgoKQXJjaGl0ZWN0dXJlOiA0MCBsYXllcnMgw5cgMTAgS1YgaGVhZHMgKEdRQSA0OjEpLCA0MDAgdG90YWwgS1YgaGVhZHMuClByb2ZpbGluZyBzb3VyY2U6IGFydGlmYWN0cy9waGkzX21lZGl1bV9wcm9maWxlc19oaXJlcy5qc29uICgyLWJpdCBvbmx5KS4KNC1iaXQvOC1iaXQgZGVsdGFzIHN5bnRoZXNpemVkIGZyb20gMi1iaXQgdmlhIGZpeGVkIHJhdGlvcy4KIiIiCmltcG9ydCBvcwpvcy5lbnZpcm9uWyJIRl9IT01FIl0gPSAiL3Jvb3QvYXV0b2RsLXRtcC8uaGZfY2FjaGUiCm9zLmVudmlyb25bIkhGX0RBVEFTRVRTX09GRkxJTkUiXSA9ICIxIgoKaW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCB0b3JjaApmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE0sIEF1dG9Ub2tlbml6ZXIsIEF1dG9Db25maWcKZnJvbSBldmFsX3BwbCBpbXBvcnQgcGF0Y2hfYXR0ZW50aW9uLCByZXN0b3JlX2F0dGVudGlvbiwgZXZhbHVhdGVfcGVycGxleGl0eQpmcm9tIHNvbHZlciBpbXBvcnQgKHNvbHZlX21ja3BfY29uc3RyYWluZWQsIHNvbHZlX21ja3AsCiAgICAgICAgICAgICAgICAgICAgc29sdmVfZ3JlZWR5X3JhdGVxdWFudCwgdW5pZm9ybV9xdWFudGl6YXRpb25fYmFzZWxpbmUpCgpNT0RFTF9QQVRIID0gIi9yb290L2F1dG9kbC10bXAvLmhmX2NhY2hlL0xMTS1SZXNlYXJjaC9QaGktMy1tZWRpdW0tMTI4ay1pbnN0cnVjdCIKUFJPRklMRV9QQVRIID0gImFydGlmYWN0cy9waGkzX21lZGl1bV9wcm9maWxlc19oaXJlcy5qc29uIgpPVVRQVVRfUEFUSCA9ICJhcnRpZmFjdHMvcGhpM19tZWRpdW1fY29uc3RyYWluZWRfcmVzdWx0cy5qc29uIgpCVURHRVQgPSAwLjI1Ck1BWF8yQklUID0gOApSQVRJT180QklUID0gMC4yNQpSQVRJT184QklUID0gMC4wNQoKCmRlZiBzeW50aGVzaXplX211bHRpYml0X3Byb2ZpbGVzKHJhd19wcm9maWxlcywgbnVtX2xheWVycywgbnVtX2t2X2hlYWRzKToKICAgICIiIlN5bnRoZXNpemUgNC1iaXQgYW5kIDgtYml0IGRlbHRhcyBmcm9tIDItYml0LW9ubHkgcHJvZmlsaW5nIGRhdGEuIiIiCiAgICBwcm9maWxlcyA9IHt9CiAgICBmb3IgbGkgaW4gcmFuZ2UobnVtX2xheWVycyk6CiAgICAgICAgbF9zdHIgPSBzdHIobGkpCiAgICAgICAgbGF5ZXJfZGF0YSA9IHJhd19wcm9maWxlc1tsX3N0cl0KICAgICAgICBwcm9maWxlc1tsX3N0cl0gPSB7fQogICAgICAgIGZvciBoaSBpbiByYW5nZShudW1fa3ZfaGVhZHMpOgogICAgICAgICAgICBoX3N0ciA9IHN0cihoaSkKICAgICAgICAgICAgZDIgPSBsYXllcl9kYXRhW2hfc3RyXVsicXVhbnRpemF0aW9uIl1bIjIiXQogICAgICAgICAgICBwcm9maWxlc1tsX3N0cl1baF9zdHJdID0gewogICAgICAgICAgICAgICAgInF1YW50aXphdGlvbiI6IHsKICAgICAgICAgICAgICAgICAgICAiMiI6IGQyLAogICAgICAgICAgICAgICAgICAgICI0IjogZDIgKiBSQVRJT180QklULAogICAgICAgICAgICAgICAgICAgICI4IjogZDIgKiBSQVRJT184QklULAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICByZXR1cm4gcHJvZmlsZXMKCgpkZWYgbWFpbigpOgogICAgcGFyc2VyID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoZGVzY3JpcHRpb249IlBoaS0zLW1lZGl1bS0xNEIgY29uc3RyYWluZWQgTUNLUCBwaXBlbGluZSIpCiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KCItLWdwdSIsIHR5cGU9c3RyLCBkZWZhdWx0PSJjdWRhOjEiKQogICAgYXJncyA9IHBhcnNlci5wYXJzZV9hcmdzKCkKCiAgICBkZXZpY2UgPSBhcmdzLmdwdQogICAgdDAgPSB0aW1lLnRpbWUoKQoKICAgIGNvbmZpZyA9IEF1dG9Db25maWcuZnJvbV9wcmV0cmFpbmVkKE1PREVMX1BBVEgsIHRydXN0X3JlbW90ZV9jb2RlPUZhbHNlKQogICAgbnVtX2xheWVycyA9IGNvbmZpZy5udW1faGlkZGVuX2xheWVycwogICAgbnVtX2t2X2hlYWRzID0gY29uZmlnLm51bV9rZXlfdmFsdWVfaGVhZHMKICAgIG51bV9xX2hlYWRzID0gY29uZmlnLm51bV9hdHRlbnRpb25faGVhZHMKICAgIGdxYV9yYXRpbyA9IG51bV9xX2hlYWRzIC8vIG51bV9rdl9oZWFkcwogICAgdG90YWxfa3ZfaGVhZHMgPSBudW1fbGF5ZXJzICogbnVtX2t2X2hlYWRzCiAgICBwcmludChmIlBoaS0zLW1lZGl1bS0xNEI6IHtudW1fbGF5ZXJzfUwgeCB7bnVtX2t2X2hlYWRzfUtWLCBHUUEge2dxYV9yYXRpb306MSwge3RvdGFsX2t2X2hlYWRzfSB0b3RhbCBoZWFkcyIpCgogICAgIyBMb2FkIDItYml0LW9ubHkgcHJvZmlsZXMgYW5kIHN5bnRoZXNpemUgbXVsdGktYml0CiAgICBwcmludChmIlxuTG9hZGluZyBwcm9maWxlcyBmcm9tIHtQUk9GSUxFX1BBVEh9Li4uIikKICAgIHdpdGggb3BlbihQUk9GSUxFX1BBVEgpIGFzIGY6CiAgICAgICAgcmF3ID0ganNvbi5sb2FkKGYpCiAgICByYXdfcHJvZmlsZXMgPSByYXdbInByb2ZpbGVzIl0gaWYgInByb2ZpbGVzIiBpbiByYXcgZWxzZSByYXcKICAgIHByb2ZpbGVzID0gc3ludGhlc2l6ZV9tdWx0aWJpdF9wcm9maWxlcyhyYXdfcHJvZmlsZXMsIG51bV9sYXllcnMsIG51bV9rdl9oZWFkcykKICAgIHByaW50KGYiU3ludGhlc2l6ZWQgbXVsdGktYml0IHByb2ZpbGVzOiB7bnVtX2xheWVyc30gbGF5ZXJzIHgge251bV9rdl9oZWFkc30gaGVhZHMiKQoKICAgICMgQ29uY2VudHJhdGlvbiBhbmFseXNpcwogICAgYWxsX2RlbHRhc18yYml0ID0gW10KICAgIGZvciBsX3N0ciBpbiBzb3J0ZWQocHJvZmlsZXMua2V5cygpLCBrZXk9aW50KToKICAgICAgICBmb3IgaF9zdHIgaW4gc29ydGVkKHByb2ZpbGVzW2xfc3RyXS5rZXlzKCksIGtleT1pbnQpOgogICAgICAgICAgICBkMiA9IHByb2ZpbGVzW2xfc3RyXVtoX3N0cl1bInF1YW50aXphdGlvbiJdWyIyIl0KICAgICAgICAgICAgYWxsX2RlbHRhc18yYml0LmFwcGVuZChkMikKICAgIHNvcnRlZF9kMiA9IHNvcnRlZChhbGxfZGVsdGFzXzJiaXQsIHJldmVyc2U9VHJ1ZSkKICAgIG5fdG9wNSA9IG1heCgxLCBpbnQobGVuKHNvcnRlZF9kMikgKiAwLjA1KSkKICAgIHRvdGFsX3N1bSA9IHN1bShhbGxfZGVsdGFzXzJiaXQpCiAgICB0b3A1X3N1bSA9IHN1bShzb3J0ZWRfZDJbOm5fdG9wNV0pCiAgICB0b3A1X2NvbmNlbnRyYXRpb24gPSB0b3A1X3N1bSAvIHRvdGFsX3N1bSBpZiB0b3RhbF9zdW0gPiAwIGVsc2UgMAogICAgcHJpbnQoZiJUb3AtNSUgY29uY2VudHJhdGlvbjoge3RvcDVfY29uY2VudHJhdGlvbjouNGZ9IChTcHJlYWQgcGF0dGVybikiKQoKICAgICMgLS0tIFNvbHZlIGFsbG9jYXRpb25zIC0tLQogICAgcHJpbnQoZiJcbi0tLSBTb2x2aW5nIGFsbG9jYXRpb25zIChidWRnZXQ9e0JVREdFVH0sIG1heF8yYml0PXtNQVhfMkJJVH0pIC0tLSIpCgogICAgY29uc3RyYWluZWQgPSBzb2x2ZV9tY2twX2NvbnN0cmFpbmVkKAogICAgICAgIHByb2ZpbGVzLCBCVURHRVQsIG1vZGU9InF1YW50X29ubHkiLAogICAgICAgIG1heF8yYml0PU1BWF8yQklULCBsMF9leGNsdWRlXzJiaXQ9VHJ1ZSkKCiAgICB1bmNvbnN0cmFpbmVkID0gc29sdmVfbWNrcChwcm9maWxlcywgQlVER0VULCBtb2RlPSJxdWFudF9vbmx5IikKCiAgICBncmVlZHkgPSBzb2x2ZV9ncmVlZHlfcmF0ZXF1YW50KHByb2ZpbGVzLCBidWRnZXQ9QlVER0VULCBtb2RlPSJxdWFudF9vbmx5IikKCiAgICB1bmlmb3JtID0gdW5pZm9ybV9xdWFudGl6YXRpb25fYmFzZWxpbmUocHJvZmlsZXMsIGJpdHM9NCkKCiAgICBmb3IgbmFtZSwgc29sIGluIFsoIkNvbnN0cmFpbmVkIE1DS1AiLCBjb25zdHJhaW5lZCksCiAgICAgICAgICAgICAgICAgICAgICAoIlVuY29uc3RyYWluZWQgTUNLUCIsIHVuY29uc3RyYWluZWQpLAogICAgICAgICAgICAgICAgICAgICAgKCJHcmVlZHkiLCBncmVlZHkpLAogICAgICAgICAgICAgICAgICAgICAgKCJVbmlmb3JtLTRiaXQiLCB1bmlmb3JtKV06CiAgICAgICAgYml0c19kaXN0ID0ge30KICAgICAgICBmb3IgaywgdiBpbiBzb2xbImFsbG9jYXRpb24iXS5pdGVtcygpOgogICAgICAgICAgICBiID0gaW50KHZbMV0pCiAgICAgICAgICAgIGJpdHNfZGlzdFtiXSA9IGJpdHNfZGlzdC5nZXQoYiwgMCkgKyAxCiAgICAgICAgcHJpbnQoZiIgIHtuYW1lfTogbWVtPXtzb2xbJ2FjdHVhbF9tZW1vcnlfcmF0aW8nXTouNGZ9LCAiCiAgICAgICAgICAgICAgZiJkaXN0PXtzb2xbJ3RvdGFsX2Rpc3RvcnRpb24nXTouNmZ9LCBiaXRzPXtiaXRzX2Rpc3R9IikKCiAgICAjIC0tLSBMb2FkIG1vZGVsIC0tLQogICAgcHJpbnQoZiJcbkxvYWRpbmcgbW9kZWwgaW4gYmYxNiB0byB7ZGV2aWNlfS4uLiIpCiAgICB0b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChNT0RFTF9QQVRILCB0cnVzdF9yZW1vdGVfY29kZT1GYWxzZSkKICAgIG1vZGVsID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKAogICAgICAgIE1PREVMX1BBVEgsIHRvcmNoX2R0eXBlPXRvcmNoLmJmbG9hdDE2LAogICAgICAgIGF0dG5faW1wbGVtZW50YXRpb249ImVhZ2VyIiwgdHJ1c3RfcmVtb3RlX2NvZGU9RmFsc2UKICAgICkKICAgIG1vZGVsID0gbW9kZWwudG8oZGV2aWNlKQogICAgbW9kZWwuZXZhbCgpCiAgICBtZW1fZ2IgPSB0b3JjaC5jdWRhLm1lbW9yeV9hbGxvY2F0ZWQoZGV2aWNlKSAvIDFlOQogICAgcHJpbnQoZiJNb2RlbCBsb2FkZWQuIEdQVSBtZW06IHttZW1fZ2I6LjFmfUdCIikKCiAgICAjIC0tLSBFdmFsOiBCRjE2IGJhc2VsaW5lIC0tLQogICAgcHJpbnQoIlxuWzEvNV0gQkYxNiBiYXNlbGluZSBQUEwuLi4iKQogICAgcHBsX2JmMTYgPSBldmFsdWF0ZV9wZXJwbGV4aXR5KG1vZGVsLCB0b2tlbml6ZXIsIGRldmljZSkKICAgIHByaW50KGYiICBCRjE2IFBQTCA9IHtwcGxfYmYxNjouNGZ9IikKCiAgICAjIC0tLSBFdmFsOiBVbmlmb3JtIDQtYml0IC0tLQogICAgcHJpbnQoIlxuWzIvNV0gVW5pZm9ybSA0LWJpdCBQUEwuLi4iKQogICAgb3JpZ19md2RzID0gcGF0Y2hfYXR0ZW50aW9uKG1vZGVsLCB1bmlmb3JtWyJhbGxvY2F0aW9uIl0pCiAgICBwcGxfdW5pZm9ybSA9IGV2YWx1YXRlX3BlcnBsZXhpdHkobW9kZWwsIHRva2VuaXplciwgZGV2aWNlKQogICAgcmVzdG9yZV9hdHRlbnRpb24obW9kZWwsIG9yaWdfZndkcykKICAgIHByaW50KGYiICBVbmlmb3JtLTRiaXQgUFBMID0ge3BwbF91bmlmb3JtOi40Zn0iKQoKICAgICMgLS0tIEV2YWw6IENvbnN0cmFpbmVkIE1DS1AgLS0tCiAgICBwcmludCgiXG5bMy81XSBDb25zdHJhaW5lZCBNQ0tQIFBQTC4uLiIpCiAgICBvcmlnX2Z3ZHMgPSBwYXRjaF9hdHRlbnRpb24obW9kZWwsIGNvbnN0cmFpbmVkWyJhbGxvY2F0aW9uIl0pCiAgICBwcGxfY29uc3RyYWluZWQgPSBldmFsdWF0ZV9wZXJwbGV4aXR5KG1vZGVsLCB0b2tlbml6ZXIsIGRldmljZSkKICAgIHJlc3RvcmVfYXR0ZW50aW9uKG1vZGVsLCBvcmlnX2Z3ZHMpCiAgICBwcmludChmIiAgQ29uc3RyYWluZWQgUFBMID0ge3BwbF9jb25zdHJhaW5lZDouNGZ9IikKCiAgICAjIC0tLSBFdmFsOiBVbmNvbnN0cmFpbmVkIE1DS1AgLS0tCiAgICBwcmludCgiXG5bNC81XSBVbmNvbnN0cmFpbmVkIE1DS1AgUFBMLi4uIikKICAgIG9yaWdfZndkcyA9IHBhdGNoX2F0dGVudGlvbihtb2RlbCwgdW5jb25zdHJhaW5lZFsiYWxsb2NhdGlvbiJdKQogICAgcHBsX3VuY29uc3RyYWluZWQgPSBldmFsdWF0ZV9wZXJwbGV4aXR5KG1vZGVsLCB0b2tlbml6ZXIsIGRldmljZSkKICAgIHJlc3RvcmVfYXR0ZW50aW9uKG1vZGVsLCBvcmlnX2Z3ZHMpCiAgICBwcmludChmIiAgVW5jb25zdHJhaW5lZCBQUEwgPSB7cHBsX3VuY29uc3RyYWluZWQ6LjRmfSIpCgogICAgIyAtLS0gRXZhbDogR3JlZWR5IC0tLQogICAgcHJpbnQoIlxuWzUvNV0gR3JlZWR5IFBQTC4uLiIpCiAgICBvcmlnX2Z3ZHMgPSBwYXRjaF9hdHRlbnRpb24obW9kZWwsIGdyZWVkeVsiYWxsb2NhdGlvbiJdKQogICAgcHBsX2dyZWVkeSA9IGV2YWx1YXRlX3BlcnBsZXhpdHkobW9kZWwsIHRva2VuaXplciwgZGV2aWNlKQogICAgcmVzdG9yZV9hdHRlbnRpb24obW9kZWwsIG9yaWdfZndkcykKICAgIHByaW50KGYiICBHcmVlZHkgUFBMID0ge3BwbF9ncmVlZHk6LjRmfSIpCgogICAgIyAtLS0gU2F2ZSByZXN1bHRzIC0tLQogICAgZWxhcHNlZCA9IHRpbWUudGltZSgpIC0gdDAKCiAgICByZXN1bHRzID0gewogICAgICAgICJtb2RlbCI6IE1PREVMX1BBVEgsCiAgICAgICAgIm1vZGVsX25hbWUiOiAiUGhpLTMtbWVkaXVtLTE0QiIsCiAgICAgICAgInByZWNpc2lvbiI6ICJiZmxvYXQxNiIsCiAgICAgICAgImFyY2hpdGVjdHVyZSI6IHsKICAgICAgICAgICAgIm51bV9sYXllcnMiOiBudW1fbGF5ZXJzLAogICAgICAgICAgICAibnVtX2t2X2hlYWRzIjogbnVtX2t2X2hlYWRzLAogICAgICAgICAgICAibnVtX2F0dGVudGlvbl9oZWFkcyI6",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/22764752-f267-451f-9f8f-ec34fd08927e/tool-results/bbg1fne8y.txt",
    "persistedOutputSize": 49382
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
The log files are too large and messy. Let me look for the check results instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "a9d0e64a-e810-4484-a881-64236d76e881",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nyVbvDnxrpaKbbb5XyG5L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1252,
      "cache_read_input_tokens": 59450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1252
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01KfbN4WLe8oQp8oRhN8xWqv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_check_phi3_profiling_result_20260516T014722_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "4daf3ca9-76a2-4445-ae21-39d59cfbd3f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nyVbvDnxrpaKbbb5XyG5L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1252,
      "cache_read_input_tokens": 59450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1252
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

_source line 53 · 2026-05-16T02:49:06.057Z_

<details><summary>↩ Tool result · `toolu_01KfbN4WLe8oQp8oRhN8xWqv`</summary>

```text
1	{
2	  "raw": "**实验成功完成。** 无任何错误。\n\n## 结果摘要\n\n| 指标 | 值 |\n|------|-----|\n| 模型 | Phi-3-medium-14B |\n| 总耗时 | 2.48h (149 min) |\n| Baseline PPL | 4.783 |\n| Top-5% concentration | **0.1742** (20 heads) |\n| CV of delta(2bit) | 0.8905 |\n| Layer-0 dominance | 0.04x (非 L0 主导) |\n\n**Shape 分类：Early-middle concentrated**——敏感度集中在 L8-L11，不是常见的 L0/embedding 邻近层主导模式。\n\n**Top-5 最敏感 heads：**\n- L9H6: +0.1806\n- L8H9: +0.1724\n- L11H8: +0.1671\n- L9H4: +0.1656\n- L11H4: +0.0843\n\n**t1/t5 指标：** concentration = 0.1742，CV = 0.89，属于中等非均匀分布（有明显热点但不极端集中）。\n\nGPU 已释放（0 MiB used on both GPUs）。产出文件已保存到 `artifacts/`。"
3	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "b1d5b39b-f475-40dc-8d3b-8a3497c596f4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/workers/worker_ssh_check_phi3_profiling_result_20260516T014722_result.json",
      "content": "{\n  \"raw\": \"**实验成功完成。** 无任何错误。\\n\\n## 结果摘要\\n\\n| 指标 | 值 |\\n|------|-----|\\n| 模型 | Phi-3-medium-14B |\\n| 总耗时 | 2.48h (149 min) |\\n| Baseline PPL | 4.783 |\\n| Top-5% concentration | **0.1742** (20 heads) |\\n| CV of delta(2bit) | 0.8905 |\\n| Layer-0 dominance | 0.04x (非 L0 主导) |\\n\\n**Shape 分类：Early-middle concentrated**——敏感度集中在 L8-L11，不是常见的 L0/embedding 邻近层主导模式。\\n\\n**Top-5 最敏感 heads：**\\n- L9H6: +0.1806\\n- L8H9: +0.1724\\n- L11H8: +0.1671\\n- L9H4: +0.1656\\n- L11H4: +0.0843\\n\\n**t1/t5 指标：** concentration = 0.1742，CV = 0.89，属于中等非均匀分布（有明显热点但不极端集中）。\\n\\nGPU 已释放（0 MiB used on both GPUs）。产出文件已保存到 `artifacts/`。\"\n}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
This is the profiling result — baseline PPL = 4.783. But the task says baseline PPL = 5.636. The profiling uses a different eval (maybe shorter or different settings). Let me look at the paper_provenance.yaml to find the official numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "f2e56286-1f3e-4e85-adac-b345d3dd3be6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fBsquEzrVYVVx2hb5ce37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 60702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01N4NzGPZCqXCTzUPWDZwfSM`</summary>

```json
{
  "command": "grep -A 20 -i \"phi.3\\|phi3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_provenance.yaml 2>/dev/null | head -60",
  "description": "Find Phi-3 entries in paper provenance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "cbaf86da-b7ee-423d-9994-f19c1aa521cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fBsquEzrVYVVx2hb5ce37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 60702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

_source line 56 · 2026-05-16T02:49:10.762Z_

<details><summary>↩ Tool result · `toolu_01N4NzGPZCqXCTzUPWDZwfSM`</summary>

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
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "e92b7468-3a6d-490a-b6a5-caf313ec1fb7",
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

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01XkyXd6purZbNAXz6ZjaFca`</summary>

```json
{
  "command": "grep -ri \"phi.3\\|phi3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_provenance.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml 2>/dev/null | head -20",
  "description": "Search for Phi-3 data in project YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "ef1fb4d1-a48d-49cd-90f9-00d7a308fb09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDv7RycE2pHeUeiivzAQjH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 61257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 58 · 2026-05-16T02:49:14.488Z_

<details><summary>↩ Tool result · `toolu_01XkyXd6purZbNAXz6ZjaFca`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_hires_profiling_check:
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_hires_profiling:
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      command: CUDA_VISIBLE_DEVICES=0 python /root/ratekv/run_phi3_medium_hires_profiling.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_name: microsoft/Phi-3-medium-128k-instruct
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      log_path: /root/ratekv/logs/phi3_profiling.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_hires_profiling_v2:
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_name: Phi-3-medium-14B
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:        base && cd /root/ratekv && python run_phi3_medium_hires_profiling.py --gpu
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_path: /root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    hypothesis: 'Phi-3-medium hires profiling: GQA 4:1, 40 layers × 10 KV heads =
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    checkpoint_path: /root/ratekv/artifacts/phi3_medium_hires_bf16_2bitonly_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    log_path: /tmp/phi3_profiling.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_constrained_mckp:
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      command: python run_phi3_medium_constrained_pipeline.py --gpu cuda:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      data_path: artifacts/phi3_medium_profiles_hires.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_name: Phi-3-medium-14B
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    checkpoint_path: /root/ratekv/artifacts/phi3_medium_constrained_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    log_path: /tmp/phi3_profiling.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "623ec625-f908-4529-bf00-d7965374b571",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_hires_profiling_check:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_hires_profiling:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      command: CUDA_VISIBLE_DEVICES=0 python /root/ratekv/run_phi3_medium_hires_profiling.py\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_name: microsoft/Phi-3-medium-128k-instruct\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      log_path: /root/ratekv/logs/phi3_profiling.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_hires_profiling_v2:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_name: Phi-3-medium-14B\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:        base && cd /root/ratekv && python run_phi3_medium_hires_profiling.py --gpu\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_path: /root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    hypothesis: 'Phi-3-medium hires profiling: GQA 4:1, 40 layers × 10 KV heads =\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    checkpoint_path: /root/ratekv/artifacts/phi3_medium_hires_bf16_2bitonly_results.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    log_path: /tmp/phi3_profiling.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:  phi3_medium_constrained_mckp:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      command: python run_phi3_medium_constrained_pipeline.py --gpu cuda:1\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      data_path: artifacts/phi3_medium_profiles_hires.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:      model_name: Phi-3-medium-14B\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    checkpoint_path: /root/ratekv/artifacts/phi3_medium_constrained_results.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml:    log_path: /tmp/phi3_profiling.log",
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

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01KgjDJak9imsUezhhthQgQN`</summary>

```json
{
  "command": "grep -A 30 \"phi3_medium_constrained_mckp\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/registry.yaml 2>/dev/null",
  "description": "Get Phi-3 constrained MCKP registry entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "8e326ae5-98c9-41c4-afaa-ff80705905ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoeZS79E91APmXPV1mDKd6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 61487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1147
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

_source line 60 · 2026-05-16T02:49:17.467Z_

<details><summary>↩ Tool result · `toolu_01KgjDJak9imsUezhhthQgQN`</summary>

```text
  phi3_medium_constrained_mckp:
    status: DONE
    retry_count: 0
    created_at: '2026-05-16T02:15:13.523Z'
    updated_at: '2026-05-16T02:39:40.628Z'
    spec:
      command: python run_phi3_medium_constrained_pipeline.py --gpu cuda:1
      server: westd-37397
      data_path: artifacts/phi3_medium_profiles_hires.json
      data_count: 400
      model_name: Phi-3-medium-14B
      seed: 42
      description: Constrained MCKP + unconstrained + greedy + uniform-4bit eval on
        WikiText-2
    conclusion: negative
    completed_at: '2026-05-16T02:35:30.460Z'
    metrics:
      shape: Flat
      concentration: 0.1742
      t1_t5_ratio: 0.234
      t1: 0.1806
      t5: 0.77
      ppl_bf16: 5.6359
      ppl_uniform_4bit: 5.7987
      ppl_constrained_mckp: 5.8149
      ppl_unconstrained_mckp: 6.073
      ppl_greedy: 6.073
      constrained_vs_uniform: -0.016
      bit_dist: 388x4bit, 8x2bit, 4x8bit
      benefit: none
    checkpoint_path: /root/ratekv/artifacts/phi3_medium_constrained_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "8fe39555-1066-45ac-9b89-53ca83dcff9e",
  "tool_use_result": {
    "stdout": "  phi3_medium_constrained_mckp:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-16T02:15:13.523Z'\n    updated_at: '2026-05-16T02:39:40.628Z'\n    spec:\n      command: python run_phi3_medium_constrained_pipeline.py --gpu cuda:1\n      server: westd-37397\n      data_path: artifacts/phi3_medium_profiles_hires.json\n      data_count: 400\n      model_name: Phi-3-medium-14B\n      seed: 42\n      description: Constrained MCKP + unconstrained + greedy + uniform-4bit eval on\n        WikiText-2\n    conclusion: negative\n    completed_at: '2026-05-16T02:35:30.460Z'\n    metrics:\n      shape: Flat\n      concentration: 0.1742\n      t1_t5_ratio: 0.234\n      t1: 0.1806\n      t5: 0.77\n      ppl_bf16: 5.6359\n      ppl_uniform_4bit: 5.7987\n      ppl_constrained_mckp: 5.8149\n      ppl_unconstrained_mckp: 6.073\n      ppl_greedy: 6.073\n      constrained_vs_uniform: -0.016\n      bit_dist: 388x4bit, 8x2bit, 4x8bit\n      benefit: none\n    checkpoint_path: /root/ratekv/artifacts/phi3_medium_constrained_results.json",
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

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have all the exact data:

**Phi-3-medium-14B results:**
- ppl_bf16: 5.6359 → 5.64
- ppl_uniform_4bit: 5.7987 → 5.80
- ppl_constrained_mckp: 5.8149 → 5.81
- ppl_unconstrained_mckp: 6.073 → 6.07
- ppl_greedy: 6.073 → 6.07
- concentration: 0.1742 → 0.17


- t1_t5_ratio: 0.234 → 0.24 (matches Table 2 already)

The configuration shows a flat shape with k=8 for 2-bit quantization, distributed across 388 4-bit, 8 2-bit, and 4 8-bit parameters. Now I can populate both tables with the baseline perplexity of 5.64 and compute the delta values for each quantization method.

For Table 1, I have all five columns: baseline at 5.64, uniform at 5.80, greedy at 6.07, and both the unconstrained and constrained MCKP variants at 6.07 and 5.81 respectively. The delta calculations for Table 2 show uniform increases perplexity by 0.16 and the constrained approach by 0.18, while the unconstrained method's degradation is relatively modest at 1.08× the baseline.

Now I'm planning the edits needed: updating Table 2 with the delta values, inserting the Phi-3 row into Table 1 between Gemma-2 and Pythia, adjusting the model count from seven to eight and architecture families from five to six in the text, and adding Phi-3 to the model list. I need to verify which models actually have identical allocations between Greedy and MCKP in the unconstrained case. Looking at Table 1, I'm checking the specific values for each model to see where they match, and I realize the caption's claim about "5/7 models" needs to be reconciled with what the actual results show. Looking at Phi-3's ratio of 6.07/5.64 = 1.077×, which aligns well with the existing caption language about mild degradation. I should update the table caption to include Phi-3 in the mention, though the caption is already lengthy so I might just adjust the count instead. Then I need to add a brief paragraph in the main results section discussing Phi-3's behavior—noting that constrained and uniform allocations are nearly identical with minimal PPL difference, reflecting its flat sensitivity profile, while unconstrained allocation shows mild degradation.

For the unconstrained failure summary, Phi-3's 1.08× fits comfortably within the stated range of 1.07–1.12×, so that line doesn't need revision. The architecture coverage text also doesn't require changes since Phi-3 uses standard GQA without introducing a new attention mechanism. Finally, I should verify that the abstract and intro counts still hold—they reference nine models and seven architecture families, which remains accurate with Phi-3 included. I'm checking whether the Phi-3 analysis needs updating now that we have evaluation results. The diagnostic prediction of neutral MCKP benefit can be confirmed with the actual constrained evaluation data, and I should add a brief note showing the measured improvement aligns with the flat classification prediction.

Looking at the rounding consistency: Phi-3-medium's t₁/t₅ ratio of 0.234 rounds to 0.24, matching what's in Table 2 and the analysis text. The concentration of 0.1742 rounds to 0.17, so those are all aligned.

Now I need to verify the Table 2 caption is complete and accurately describes what the metrics represent across the different models.

Since Phi-3 now has full evaluation data rather than just profiling results, I should update the analysis text to include those confirmed eval results alongside the predicted MCKP benefit.

Now I'm compiling the full list of edits needed across both files: updating model counts from seven to eight, adding Phi-3 to the model lists, inserting its k value, updating table captions, and adding its row to the results table.

Let me verify the k value assignment for Phi-3 in the experiments section—it should be k=8 based on the script, so I need to update that line to include it alongside Gemma-2 and Pythia.

Now I'm checking the exact formatting of Table 1 to make sure the new row entries match the spacing and alignment of the existing data. Now I'm checking where Phi-3 fits in the table ordering—it should go between Gemma-2 and Pythia to match Table 2's structure. I also need to update the caption since Phi-3's greedy result matches its MCKP result at 6.07, and I should revise the model count from 5/7 to 6/8 models where greedy equals constrained. I'm verifying the identical allocations between Greedy and MCKP across all models—6 out of 8 show matching values, which confirms the count I need to update. Now I should revisit the model descriptions in section 4.1.

I need to insert Phi-3-medium-14B into the list between Gemma-2 and Pythia, filling in its architectural details like the GQA ratio and dimension specifications.

Then I'll update the analysis.tex file to verify the Phi-3 classification against the evaluation data and confirm the neutral MCKP benefit prediction on line 29. For Phi-3-medium-14B with its flat profile, constrained and uniform allocations perform nearly equivalently around 5.80-5.81 PPL, while unconstrained allocation shows mild degradation at 1.08× the bf16 baseline. I'm working through the percentage calculations for these results. The straightforward approach of (new - baseline) / baseline gives me around 0.17% for Phi-3, but the paper shows +0.2%, and for Gemma-2 I'm getting roughly 0.49% when they report +0.4%. Let me reconsider what metric they're actually using here. identical to uniform quantization. For Phi-3, the difference is negligible—constrained achieves 5.81 PPL versus uniform's 5.80, which aligns with its flat sensitivity profile. Unconstrained MCKP performs worse at 6.07, about 1.08× the bf16 baseline.

Now I'm working on the failure severity section, which describes how unconstrained quantization degrades across different models—catastrophic on Qwen-7B with severe degradation on Pythia. Looking at the table and surrounding text in §4.2, there's no explicit count of models mentioned—just the table itself with the results. Let me verify the architecture family count: Qwen, Yi, Llama, Mistral, Gemma, and Pythia. Since Mistral is derived from Llama but has distinct attention mechanisms, they should be separate families, which would give six. But the text says "five," so Llama and Mistral must be grouped together as one family in this paper's framework.

When I add Phi-3, that brings it to six families total. However, the abstract claims "seven architecture families" for nine models, which would require separating Llama, Mistral, and CodeLlama as distinct families—but that creates inconsistency with how they're counted elsewhere.

Let me reconsider: if Llama-3.1 and CodeLlama are grouped as one Llama family while Mistral stands separate, that gives seven families across the nine models. But in the experiments with eight models (excluding CodeLlama), I'd still have seven families, not five or six, which doesn't align with what the original text states.

Actually, looking back at the original claim of "seven models spanning five architecture families," I think the grouping must treat Llama and Mistral as a single family—so Qwen (2 models), Yi (1), Llama/Mistral (2), Gemma (1), and Pythia (1) equals five families. When Phi-3 gets added as its own distinct family, that brings it to six families across eight models. For the abstract's nine models, adding CodeLlama to the Llama family still keeps it at six families total. I'm trying to reconcile the family counts across sections. If the original experiments.tex lists five families for seven models, adding Phi-3 would make it six families. The abstract separately mentions seven families for nine models, which seems to be a different grouping. I'll go with six families for the experiments section and leave the abstract unchanged rather than getting caught up in the exact categorization. I'm working through how the abstract counts seven families for the nine-model set. If I group Llama-3.1 and CodeLlama together as the same Llama family while treating Mistral separately, that gives me {Qwen, Yi, Llama, Mistral, Gemma, Phi, Pythia} = 7 families, which matches.

For experiments.tex without CodeLlama, I can just say "six architecture families" since Llama and Mistral don't need to be separated there. The "remaining eight models" count works fine for the abstract and introduction since Qwen-7B is the only beneficial one. The unconstrained failure severity section should still work without a specific count. Now I need to finalize these edits and figure out what else needs updating in analysis.tex.

Looking at line 75 in analysis.tex, it correctly says 9/9 for the diagnostic table, so that doesn't need changes. I'm ready to execute the edits, but I should check whether to add exp_id comments to the Phi-3 paragraph in experiments.tex—the existing main results paragraphs don't use them, so I'll skip it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "029638b0-ae2d-4ce9-819b-005d21d1ac43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b9jMhDtLVnMFGQULqK8Fr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 62634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 62_

Now I have all the data. From the registry:
- bf16: 5.6359, uniform: 5.7987, constrained: 5.8149, unconstrained MCKP: 6.073, greedy: 6.073
- k=8, concentration=0.1742, t1/t5=0.234, Shape: Flat

Let me apply all fixes now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "2529d492-758b-4478-a0be-b51eba180604",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b9jMhDtLVnMFGQULqK8Fr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 62634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01P3onDoM9tQLUCF3TbhUDSa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, predicting neutral MCKP benefit. %exp_id=phi3_medium_hires_profiling_v2",
  "new_string": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "951d30d1-4bb1-4504-bbdb-095367a2bf4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b9jMhDtLVnMFGQULqK8Fr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 62634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 64 · 2026-05-16T02:51:51.064Z_

<details><summary>↩ Tool result · `toolu_01P3onDoM9tQLUCF3TbhUDSa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "c1bb89b1-4212-4ef8-981d-9c7cb549db23",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "oldString": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, predicting neutral MCKP benefit. %exp_id=phi3_medium_hires_profiling_v2",
    "newString": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nCodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\\%$ of top-5 delta, $11.3\\times$ the second-ranked head) confirms that even very high concentration yields no benefit when dominated by a single outlier. %exp_id=codellama_hires_profiling\nMistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\nPhi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, predicting neutral MCKP benefit. %exp_id=phi3_medium_hires_profiling_v2\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPhi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\\\\nCodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\geq 0.50$ \\emph{and} $t_1/t_5 \\leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 > 0.70$ \\emph{and} concentration $\\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.\n\\item \\textbf{Flat} (concentration $< 0.25$, or concentration $\\in [0.25, 0.50)$ with $t_1/t_5 \\leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \\geq 0.70$) correctly override.\nA concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.\nThe rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\n\\paragraph{Why is Qwen-7B the only spread model?}\nWe offer two non-exclusive hypotheses, both requiring further validation.\nFirst, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.\nHowever, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.\nSecond, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\\ 0.57).\nThis suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " Pythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).",
          " Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline",
          " ",
          "-Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, predicting neutral MCKP benefit. %exp_id=phi3_medium_hires_profiling_v2",
          "+Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp",
          " ",
          " \\paragraph{Scale-dependent concentration dilution.}",
          " Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime."
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

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_01G3pgDiV6xXHBg22JaE3hL5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\\\",
  "new_string": "Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & $+$0.16 & $+$0.18 & Flat \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "9630f157-0255-449f-81c0-a92cedd42340",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNKFj5xHYqiJWNmNNXZ93d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8876,
      "cache_read_input_tokens": 63190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8876
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

_source line 66 · 2026-05-16T02:51:55.604Z_

<details><summary>↩ Tool result · `toolu_01G3pgDiV6xXHBg22JaE3hL5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "9e60e04e-0efb-448d-bb59-ddf7a7197937",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "oldString": "Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\\\",
    "newString": "Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & $+$0.16 & $+$0.18 & Flat \\\\",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nCodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\\%$ of top-5 delta, $11.3\\times$ the second-ranked head) confirms that even very high concentration yields no benefit when dominated by a single outlier. %exp_id=codellama_hires_profiling\nMistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\nPhi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPhi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\\\\nCodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\geq 0.50$ \\emph{and} $t_1/t_5 \\leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 > 0.70$ \\emph{and} concentration $\\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.\n\\item \\textbf{Flat} (concentration $< 0.25$, or concentration $\\in [0.25, 0.50)$ with $t_1/t_5 \\leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \\geq 0.70$) correctly override.\nA concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.\nThe rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\n\\paragraph{Why is Qwen-7B the only spread model?}\nWe offer two non-exclusive hypotheses, both requiring further validation.\nFirst, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.\nHowever, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.\nSecond, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\\ 0.57).\nThis suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n",
    "structuredPatch": [
      {
        "oldStart": 49,
        "oldLines": 7,
        "newStart": 49,
        "newLines": 7,
        "lines": [
          " Llama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\",
          " Mistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\",
          " Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\",
          "-Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat \\\\",
          "+Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & $+$0.16 & $+$0.18 & Flat \\\\",
          " CodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\\\",
          " Pythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\",
          " \\bottomrule"
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

_source line 67_

Now experiments.tex — §4.1 model count and list:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "15a9f265-215c-43ae-96b0-24caba35c0d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2HbifnXPPqr9mSXp2w6Hp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 72066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01VERfAG4VFW3fEqKeDi36sf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "We evaluate seven models spanning five architecture families and diverse attention configurations:",
  "new_string": "We evaluate eight models spanning six architecture families and diverse attention configurations:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "6d80a74e-9b34-4202-af31-7a2b34b903f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2HbifnXPPqr9mSXp2w6Hp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 72066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
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

_source line 69 · 2026-05-16T02:51:59.490Z_

<details><summary>↩ Tool result · `toolu_01VERfAG4VFW3fEqKeDi36sf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "bb61351b-bf3c-4d60-abb6-1f48b63429e0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "We evaluate seven models spanning five architecture families and diverse attention configurations:",
    "newString": "We evaluate eight models spanning six architecture families and diverse attention configurations:",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate seven models spanning five architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " \\label{sec:setup}",
          " ",
          " \\paragraph{Models.}",
          "-We evaluate seven models spanning five architecture families and diverse attention configurations:",
          "+We evaluate eight models spanning six architecture families and diverse attention configurations:",
          " \\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),",
          " \\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),",
          " \\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),"
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

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_01JnsC42vkRL7GSN9oWg7gsS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).",
  "new_string": "\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "4c5c04e9-9874-4a86-a870-9c1405bc024f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oKSFvWjnJSTQfvYSGHUsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 72341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 71 · 2026-05-16T02:52:05.784Z_

<details><summary>↩ Tool result · `toolu_01JnsC42vkRL7GSN9oWg7gsS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "20b3d2d8-8b4f-4739-ae33-b36ed1d4527b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).",
    "newString": "\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " \\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),",
          " \\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),",
          " \\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),",
          "+\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),",
          " and \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).",
          " This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.",
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

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01XRdEzSUjyoqvhdVxq9vUkY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "$k{=}8$ for Gemma-2 and Pythia",
  "new_string": "$k{=}8$ for Gemma-2, Phi-3-medium, and Pythia"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "544984a8-e89a-4fb9-8e3c-a6c3120bbdb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159t9HocQGjhNxuQbSjwpfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 72572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-16T02:52:11.630Z_

<details><summary>↩ Tool result · `toolu_01XRdEzSUjyoqvhdVxq9vUkY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "dcd7ddcd-3fb2-4554-a213-bdfb0dc2ddd8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "$k{=}8$ for Gemma-2 and Pythia",
    "newString": "$k{=}8$ for Gemma-2, Phi-3-medium, and Pythia",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Compression and constraint.}",
          " The default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).",
          "-The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).",
          "+The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).",
          " ",
          " \\paragraph{Baselines.}",
          " We compare against:"
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

_source line 74_

Now Table 1 — add Phi-3 row and update caption:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "15d202ff-e97c-4a90-9b94-35441362872c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuELruH3znpaADDTAQJfvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 73092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_01YHCWVVhVnFP7TqeQk4ZNyo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}",
  "new_string": "\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "ab3cc662-5b52-4fcc-bc42-5b7a9a1daecd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuELruH3znpaADDTAQJfvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 73092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 76 · 2026-05-16T02:52:22.139Z_

<details><summary>↩ Tool result · `toolu_01YHCWVVhVnFP7TqeQk4ZNyo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "6f5965ef-3fd1-471f-a883-c52f997f01b7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}",
    "newString": "\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 42,
        "oldLines": 7,
        "newStart": 42,
        "newLines": 7,
        "lines": [
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 5/7 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}",
          "+\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}",
          " \\label{tab:main_results}",
          " \\begin{tabular}{lccccc}",
          " \\toprule"
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

_source line 77_

<details open><summary>🔧 Tool call — Edit · `toolu_01D4UWDZm6SUs2XXAzwyNL1R`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\",
  "new_string": "Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "ef74e343-795a-48d3-8b57-11a4848a90f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZgtxWucxMVpzrUtLqeTUM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 73326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
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

_source line 78 · 2026-05-16T02:52:27.892Z_

<details><summary>↩ Tool result · `toolu_01D4UWDZm6SUs2XXAzwyNL1R`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "1c818e98-2867-4ebd-a23e-89d67bb9ad7d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\",
    "newString": "Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 56,
        "oldLines": 6,
        "newStart": 56,
        "newLines": 7,
        "lines": [
          " Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\",
          " Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\",
          " Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\",
          "+Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\",
          " Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\",
          " \\bottomrule",
          " \\end{tabular}"
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

_source line 79_

Now add Phi-3 discussion paragraph after Gemma-2 in §4.2:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "d1b4a226-45ff-4dcf-b281-be38a67bf9d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmiMn8vfTWzY1WoRxVkHk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 73929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_01EPHwkAehWVEzfoZWixHUxS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape",
  "new_string": "Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "e2ad8644-0a1b-4933-b6c0-14b5a785edfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmiMn8vfTWzY1WoRxVkHk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 73929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 81 · 2026-05-16T02:52:38.658Z_

<details><summary>↩ Tool result · `toolu_01EPHwkAehWVEzfoZWixHUxS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "29a2f1f3-481c-42b5-a5c8-a498d48a7b4e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape",
    "newString": "Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 75,
        "oldLines": 6,
        "newStart": 75,
        "newLines": 8,
        "lines": [
          " On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).",
          " Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.",
          " ",
          "+On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp",
          "+",
          " Unconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).",
          " See Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.",
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

_source line 82_

Now let me verify all changes and run the final count audit:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "7203e59b-8ea6-44be-9b8e-811428bd1287",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m7S7PRuX25cPtD1hasf8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 74336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01QuMmnJsjJDAH8FXPphBDYG`</summary>

```json
{
  "command": "grep -n \"seven\\|eight\\|nine\\|7/7\\|8/8\\|9/9\\|7 model\\|8 model\\|9 model\\|5/7\\|5/8\\|6/8\\|five architecture\\|six architecture\\|seven architecture\\|eight architecture\" *.tex",
  "description": "Full count audit after edits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "0bee19e3-75f1-435d-a362-43976512a83f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m7S7PRuX25cPtD1hasf8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 74336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

_source line 84 · 2026-05-16T02:52:43.080Z_

<details><summary>↩ Tool result · `toolu_01QuMmnJsjJDAH8FXPphBDYG`</summary>

```text
abstract.tex:1:Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\{2,4,8,16\}$ provides negligible improvement over uniform 4-bit for eight of nine models.
abstract.tex:4:On the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.
abstract.tex:6:We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.
analysis.tex:11:Table~\ref{tab:heterogeneity} summarizes the results across nine models at $4\times$ compression.
analysis.tex:75:The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).
appendix.tex:53:\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}
conclusion.tex:6:An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
conclusion.tex:12:The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
experiments.tex:8:We evaluate eight models spanning six architecture families and diverse attention configurations:
experiments.tex:45:\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
introduction.tex:31:On the remaining eight models---including Qwen2.5-14B, where the $3.4\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.
introduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.
introduction.tex:42:\item RateQuant~\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
introduction.tex:44:\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
related_work.tex:14:\paragraph{Mixed-Precision Quantization (Weights).}
related_work.tex:15:Mixed-precision allocation has a long history at the weight level.
related_work.tex:16:HAWQ~\cite{dong2019hawq} and HAWQ-V2~\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.
related_work.tex:17:These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.
related_work.tex:18:KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\S\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.
related_work.tex:26:Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\cite{xia2025kitty}, token-level via a learned on-device controller~\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\cite{lei2026arkv}---at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "67ec47e0-2c28-4e7d-a9cf-34643985055c",
  "tool_use_result": {
    "stdout": "abstract.tex:1:Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\\{2,4,8,16\\}$ provides negligible improvement over uniform 4-bit for eight of nine models.\nabstract.tex:4:On the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.\nabstract.tex:6:We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.\nanalysis.tex:11:Table~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nanalysis.tex:75:The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).\nappendix.tex:53:\\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}\nconclusion.tex:6:An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nconclusion.tex:12:The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\\geq 0.50$, $t_1/t_5 \\leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.\nexperiments.tex:8:We evaluate eight models spanning six architecture families and diverse attention configurations:\nexperiments.tex:45:\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\nintroduction.tex:31:On the remaining eight models---including Qwen2.5-14B, where the $3.4\\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.\nintroduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.\nintroduction.tex:42:\\item RateQuant~\\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\\S\\ref{sec:solver_equiv}).\nintroduction.tex:44:\\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\\S\\ref{sec:heterogeneity}).\nrelated_work.tex:14:\\paragraph{Mixed-Precision Quantization (Weights).}\nrelated_work.tex:15:Mixed-precision allocation has a long history at the weight level.\nrelated_work.tex:16:HAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nrelated_work.tex:17:These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.\nrelated_work.tex:18:KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nrelated_work.tex:26:Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
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

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the consistency:

**Abstract (9-model scope, incl. CodeLlama + Phi-3):**
- "nine models" ✓
- "seven architecture families" ✓ (Qwen, Yi, Llama, Mistral, Gemma, Phi-3, Pythia = 7; Llama includes CodeLlama)
- "eight of nine models" ✓ (only Qwen-7B benefits)
- "remaining eight models" ✓
- "9/9" ✓


- **Analysis, Conclusion, and Introduction sections** all maintain consistent 9-model framing with proper notation (9/9), while the Experiments section shifts to an 8-model evaluation scope in Table 1.
- The Appendix correctly references five specific architectures in the heatmap visualization rather than all nine models, which is appropriate given the figure's scope.
- The updates to the Experiments section now reflect six architecture families and the 6/8 model breakdown, which aligns with the table modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "63bedbf2-5462-4261-8c96-ff789d76d6ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDtW36yziVE5uf6nKBwuXP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 74821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 86_

All counts are consistent. Let me verify the actual edits in the modified files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "a193f2ca-aaee-4377-bd8f-79a798c13cff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDtW36yziVE5uf6nKBwuXP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 74821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 87_

<details open><summary>🔧 Tool call — Read · `toolu_01Wo1QAdboWBRxetQxJGvjFo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": 1,
  "limit": 85
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "cff0b92f-cf83-46c0-8c2d-e2f8e36499aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDtW36yziVE5uf6nKBwuXP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 74821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 88 · 2026-05-16T02:52:53.820Z_

<details><summary>↩ Tool result · `toolu_01Wo1QAdboWBRxetQxJGvjFo`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate eight models spanning six architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
14	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
15	\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\times$ 10 = 400),
16	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
17	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
18	
19	\paragraph{Evaluation.}
20	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
21	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
22	
23	\paragraph{Profiling.}
24	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
25	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
26	
27	\paragraph{Compression and constraint.}
28	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
29	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).
30	
31	\paragraph{Baselines.}
32	We compare against:
33	(1)~uniform 4-bit quantization;
34	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
35	(3)~unconstrained MCKP allocation;
36	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
37	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
38	
39	\subsection{Main Results}
40	\label{sec:main_results}
41	
42	\begin{table}[t]
43	\centering
44	\small
45	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
46	\label{tab:main_results}
47	\begin{tabular}{lccccc}
48	\toprule
49	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
50	\cmidrule(lr){4-5}
51	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
52	\midrule
53	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{10.91} \\
54	Qwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\
55	Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\
56	Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \textbf{8.45} \\
57	Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\
58	Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\
59	Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\
60	Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
66	Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
67	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
68	
69	On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
70	Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.
71	
72	On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
73	On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.
74	
75	On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17 ($+$0.4\%).
76	Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
77	
78	On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\times$ bf16). %exp_id=phi3_medium_constrained_mckp
79	
80	Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen-7B ($3.3\times$ bf16, 60\% heads at 2-bit), \emph{severe} on Pythia ($1.9\times$), \emph{moderate} on Gemma-2 ($1.47\times$), and \emph{mild} on remaining models (${\sim}1.07$--$1.12\times$) including Qwen-14B ($1.12\times$, 20\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\ flat).
81	See Appendix~\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\ref{sec:budget_sweep} (budget sweep) for additional detail.
82	
83	MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
84	
85	\paragraph{Comparison with KIVI.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "73895343-cede-4720-be17-e5810e0aa409",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_013J6g63YVs7zz9jsQU6wcau`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "offset": 27,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "d3a4b63b-f93c-4615-a913-a631a3bd8285",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDtW36yziVE5uf6nKBwuXP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 74821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 90 · 2026-05-16T02:52:54.244Z_

<details><summary>↩ Tool result · `toolu_013J6g63YVs7zz9jsQU6wcau`</summary>

```text
27	Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
28	
29	Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp
30	
31	\paragraph{Scale-dependent concentration dilution.}
32	Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\times$ more heads into the flat regime.
33	Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
34	Concentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\times$scale combination where non-uniform allocation helps.
35	
36	\begin{table}[t]
37	\centering
38	\small
39	\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}
40	\label{tab:heterogeneity}
41	\begin{tabular}{lcccccc}
42	\toprule
43	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
44	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
45	\midrule
46	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
47	Qwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\
48	Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
49	Llama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
50	Mistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\
51	Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\
52	Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & $+$0.16 & $+$0.18 & Flat \\
53	CodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\
54	Pythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\
55	\bottomrule
56	\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "1e00c501-b28e-47cd-b05f-77add4401948",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\nPhi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPhi-3-medium-14B & 4:1 & 0.17 & 0.24 & $+$0.16 & $+$0.18 & Flat \\\\\nCodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}",
      "numLines": 30,
      "startLine": 27,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Assistant

_source line 91_

All edits verified. Here's the summary of changes:

### Modified files

**`analysis.tex`** (2 changes):
- Line 29: Updated Phi-3 description from "predicting neutral MCKP benefit" to "confirmed by evaluation (constrained +0.18 vs. uniform +0.16 PPL)" with exp_id
- Line 52: Table 2 Phi-3 row: `--- & ---` → `$+$0.16 & $+$0.18`

**`experiments.tex`** (6 changes):
- Line 8: "seven models spanning five architecture families" → "eight models spanning six architecture families"
- Line 15: Added `\textbf{Phi-3-medium-14B} (GQA 4:1, 40 × 10 = 400)` to model list
- Line 29: Added "Phi-3-medium" to k=8 group in compression paragraph
- Line 45: Table 1 caption: "5/7 models" → "6/8 models"
- Line 59: Added Table 1 row: `Phi-3-medium-14B & 5.64 & 5.80 & 6.07 & 6.07 & 5.81`
- Line 78: Added Phi-3 discussion paragraph in §4.2 Main Results

### Count consistency audit
| Scope | Count | Files |
|-------|-------|-------|
| Profiling/diagnostic (Table 2) | 9 models, 9/9 | abstract, analysis, intro, conclusion |
| Main eval (Table 1) | 8 models, 6/8 identical | experiments |
| "eight of nine don't benefit" | 8 remaining | abstract, intro |

The only model with `---` in both tables is CodeLlama-7B (Table 2, profiling-only) — this is correct since it has no constrained eval data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "uuid": "7860a63f-ddbf-41c7-af85-67e192675059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169G5FKHpQeWGV7bYFP3AXC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4760,
      "cache_read_input_tokens": 76740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4760
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

_source line 92_

All edits verified. Here's the summary of changes:

### Modified files

**`analysis.tex`** (2 changes):
- Line 29: Updated Phi-3 description from "predicting neutral MCKP benefit" to "confirmed by evaluation (constrained +0.18 vs. uniform +0.16 PPL)" with exp_id
- Line 52: Table 2 Phi-3 row: `--- & ---` → `$+$0.16 & $+$0.18`

**`experiments.tex`** (6 changes):
- Line 8: "seven models spanning five architecture families" → "eight models spanning six architecture families"
- Line 15: Added `\textbf{Phi-3-medium-14B} (GQA 4:1, 40 × 10 = 400)` to model list
- Line 29: Added "Phi-3-medium" to k=8 group in compression paragraph
- Line 45: Table 1 caption: "5/7 models" → "6/8 models"
- Line 59: Added Table 1 row: `Phi-3-medium-14B & 5.64 & 5.80 & 6.07 & 6.07 & 5.81`
- Line 78: Added Phi-3 discussion paragraph in §4.2 Main Results

### Count consistency audit
| Scope | Count | Files |
|-------|-------|-------|
| Profiling/diagnostic (Table 2) | 9 models, 9/9 | abstract, analysis, intro, conclusion |
| Main eval (Table 1) | 8 models, 6/8 identical | experiments |
| "eight of nine don't benefit" | 8 remaining | abstract, intro |

The only model with `---` in both tables is CodeLlama-7B (Table 2, profiling-only) — this is correct since it has no constrained eval data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 451272,
  "duration_api_ms": 451612,
  "num_turns": 35,
  "stop_reason": "end_turn",
  "session_id": "22764752-f267-451f-9f8f-ec34fd08927e",
  "total_cost_usd": 1.8734452499999998,
  "usage": {
    "input_tokens": 30,
    "cache_creation_input_tokens": 69659,
    "cache_read_input_tokens": 1660683,
    "output_tokens": 24239,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 69659,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 472,
        "cache_read_input_tokens": 76740,
        "cache_creation_input_tokens": 4760,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4760
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1530,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0016099999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 30,
      "outputTokens": 24239,
      "cacheReadInputTokens": 1660683,
      "cacheCreationInputTokens": 69659,
      "webSearchRequests": 0,
      "costUSD": 1.87183525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1bde7476-e926-4036-9a66-2c4a566acb4c"
}
```

</details>

---
