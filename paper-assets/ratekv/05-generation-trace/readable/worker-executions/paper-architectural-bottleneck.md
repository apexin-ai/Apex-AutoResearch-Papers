# paper architectural bottleneck

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_architectural_bottleneck_20260516T102156.log`
- **Structured JSON:** [`f9a6d1a4db93ff39c088.json`](../../sessions/f9/f9a6d1a4db93ff39c088.json)

## Before a recorded user message

21 recorded events

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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
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
  "uuid": "883ea83e-90eb-4e39-a643-105eb08b38a8",
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
    "resetsAt": 1778944800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "42ed4e42-fcdb-43a1-aa47-0bbc66bab9d8",
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d"
}
```

---

### Assistant

_source line 4_

Let me read both files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "fd6170e1-e60b-49f1-8f69-35ce6e22631b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nLVgdZJMQsn6pXajFXxpC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13133
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

<details open><summary>🔧 Tool call — Read · `toolu_01XNNrx76T8vVa2tVdxbpfib`</summary>

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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "eb15684e-73d4-4138-9e3d-58d4becb1f53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nLVgdZJMQsn6pXajFXxpC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13133
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

_source line 6 · 2026-05-16T10:22:07.704Z_

<details><summary>↩ Tool result · `toolu_01XNNrx76T8vVa2tVdxbpfib`</summary>

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
17	Yi-1.5-9B is a critical counterexample: despite high concentration ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's 4-bit and 8-bit deltas are ${\approx}\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.
20	In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling
21	
22	Llama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
23	CodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\%$ of top-5 delta, $11.3\times$ the second-ranked head) yields no benefit when dominated by a single outlier; constrained MCKP ($k{=}2$) confirms: $+$0.17 vs.\ uniform $+$0.19, consistent with a near-uniform allocation (1021/1024 heads at 4-bit). %exp_id=codellama_constrained_mckp
24	Mistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
25	
26	Pythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).
27	Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
28	
29	Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\ uniform $+$0.16 PPL).
30	Although $t_1/t_5$ is low (indicating no dominant outlier), the concentration of 0.17 places the cumulative top-5\% delta below the level required for meaningful reallocation---spread structure without sufficient absolute magnitude does not create optimization opportunities. %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp
31	
32	\paragraph{Scale-dependent concentration dilution.}
33	Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\times$ more heads into the flat regime.
34	Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
35	Concentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\times$scale combination where non-uniform allocation helps.
36	
37	\begin{table}[t]
38	\centering
39	\small
40	\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}
41	\label{tab:heterogeneity}
42	\begin{tabular}{lcccccc}
43	\toprule
44	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
45	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
46	\midrule
47	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
48	Qwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\
49	Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
50	Llama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
51	Mistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\
52	Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\
53	Phi-3-medium-14B & 4:1 & 0.17 & 0.23 & $+$0.16 & $+$0.18 & Flat \\
54	CodeLlama-7B & 1:1 & 0.80 & 0.81 & $+$0.19 & $+$0.17 & Spike \\
55	Pythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	The per-head heatmap (Figure~\ref{fig:heatmap}, Appendix~\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.
61	
62	\subsection{Empirical Decision Rule}
63	\label{sec:diagnostic}
64	
65	MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
66	This motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.
67	Given the profiling results from \S\ref{sec:profiling}, compute the top-5\% concentration and $t_1/t_5$ ratio, then select:
68	\begin{itemize}[nosep]
69	\item \textbf{Spread} (concentration $\geq 0.50$ \emph{and} $t_1/t_5 \leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
70	\item \textbf{Spike} ($t_1/t_5 > 0.70$ \emph{and} concentration $\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.
71	\item \textbf{Flat} (concentration $< 0.25$, or concentration $\in [0.25, 0.50)$ with $t_1/t_5 \leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.
72	\end{itemize}
73	
74	Both conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \geq 0.70$) correctly override.
75	A concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.
76	The rule is experimentally confirmed on all nine models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat), Pythia-1.4B (MHA, flat), and CodeLlama-7B (MHA, spike).
77	Only Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.
78	The rule reuses profiling data already required by the solver and adds no overhead.
79	
80	\paragraph{Why is Qwen-7B the only spread model?}
81	We offer two non-exclusive hypotheses, both requiring further validation.
82	First, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.
83	However, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.
84	Second, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\ 0.57).
85	This suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.
86	
87	On Qwen-7B, a simple L0-protection heuristic with random downgrade captures 93\% of the MCKP benefit under standard-resolution profiling (median PPL 11.52 vs MCKP 11.23), suggesting that identifying which heads to \emph{protect} matters more than the optimization algorithm---consistent with our solver-equivalence finding.
88	
89	Additional analyses---granularity tradeoff (Appendix~\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\ref{sec:granularity}--\ref{sec:kv_separation}.
90	
91	% TODO(kivi-compounding): If KIVI compounding persists, add discussion of
92	% quantization-scheme independence here. If disappears, add scoping discussion.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "3b3ecabe-ddbc-4953-9771-4be7c4ba0cb0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite high concentration ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nCodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\\%$ of top-5 delta, $11.3\\times$ the second-ranked head) yields no benefit when dominated by a single outlier; constrained MCKP ($k{=}2$) confirms: $+$0.17 vs.\\ uniform $+$0.19, consistent with a near-uniform allocation (1021/1024 heads at 4-bit). %exp_id=codellama_constrained_mckp\nMistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\nPhi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL).\nAlthough $t_1/t_5$ is low (indicating no dominant outlier), the concentration of 0.17 places the cumulative top-5\\% delta below the level required for meaningful reallocation---spread structure without sufficient absolute magnitude does not create optimization opportunities. %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPhi-3-medium-14B & 4:1 & 0.17 & 0.23 & $+$0.16 & $+$0.18 & Flat \\\\\nCodeLlama-7B & 1:1 & 0.80 & 0.81 & $+$0.19 & $+$0.17 & Spike \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\geq 0.50$ \\emph{and} $t_1/t_5 \\leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 > 0.70$ \\emph{and} concentration $\\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.\n\\item \\textbf{Flat} (concentration $< 0.25$, or concentration $\\in [0.25, 0.50)$ with $t_1/t_5 \\leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \\geq 0.70$) correctly override.\nA concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.\nThe rule is experimentally confirmed on all nine models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat), Pythia-1.4B (MHA, flat), and CodeLlama-7B (MHA, spike).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\n\\paragraph{Why is Qwen-7B the only spread model?}\nWe offer two non-exclusive hypotheses, both requiring further validation.\nFirst, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.\nHowever, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.\nSecond, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\\ 0.57).\nThis suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.\n\nOn Qwen-7B, a simple L0-protection heuristic with random downgrade captures 93\\% of the MCKP benefit under standard-resolution profiling (median PPL 11.52 vs MCKP 11.23), suggesting that identifying which heads to \\emph{protect} matters more than the optimization algorithm---consistent with our solver-equivalence finding.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n\n% TODO(kivi-compounding): If KIVI compounding persists, add discussion of\n% quantization-scheme independence here. If disappears, add scoping discussion.\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01V4AoeoiF4NZJFQuR1LMMi9`</summary>

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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "d78c1452-413f-4d94-8b4d-34d14acefbbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nLVgdZJMQsn6pXajFXxpC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13133
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

_source line 8 · 2026-05-16T10:22:08.058Z_

<details><summary>↩ Tool result · `toolu_01V4AoeoiF4NZJFQuR1LMMi9`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate nine models spanning seven architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{CodeLlama-7B}\footnote{CodeLlama multi-bit profiles synthesized from 2-bit-only profiling; classification robust as constrained allocation is dominated by 4-bit heads.} (MHA 1:1, 32 $\times$ 32 = 1024),
14	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
15	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
16	\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\times$ 10 = 400),
17	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
18	All nine models undergo full constrained evaluation.
19	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
20	
21	\paragraph{Evaluation.}
22	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
23	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
24	
25	\paragraph{Profiling.}
26	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
27	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
28	
29	\paragraph{Compression and constraint.}
30	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
31	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5, Llama, CodeLlama, and Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).
32	
33	\paragraph{Baselines.}
34	We compare against:
35	(1)~uniform 4-bit quantization;
36	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
37	(3)~unconstrained MCKP allocation;
38	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
39	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
40	
41	\subsection{Main Results}
42	\label{sec:main_results}
43	
44	\begin{table}[t]
45	\centering
46	\small
47	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
48	\label{tab:main_results}
49	\begin{tabular}{lccccc}
50	\toprule
51	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
52	\cmidrule(lr){4-5}
53	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
54	\midrule
55	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{10.91} \\
56	Qwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\
57	Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\
58	Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \textbf{8.45} \\
59	Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\
60	Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\
61	Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\
62	Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
68	Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
69	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
70	
71	On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
72	Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.
73	
74	On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite high concentration (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
75	On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.
76	
77	On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17 ($+$0.4\%).
78	Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
79	
80	On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\times$ bf16). %exp_id=phi3_medium_constrained_mckp
81	
82	Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen-7B ($3.3\times$ bf16, 60\% heads at 2-bit), \emph{severe} on Pythia ($1.9\times$), \emph{moderate} on Gemma-2 ($1.47\times$), and \emph{mild} on remaining models (${\sim}1.07$--$1.12\times$) including Qwen-14B ($1.12\times$, 20\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\ flat).
83	The additive distortion assumption underlying standard MCKP formulations systematically fails at these bit-width gaps.
84	
85	\paragraph{Aggressive compression.}
86	At higher compression (5.3$\times$), the cardinality constraint becomes valuable even for non-spread models: on Llama, constrained MCKP reduces PPL from 2643.8 (uniform 2-bit) to 57.6 (45$\times$ improvement); on Mistral, from 519.1 to 11.9 (44$\times$ improvement). The constraint's universal value emerges at aggressive compression ratios where uniform low-bit becomes insufficient (Appendix~\ref{sec:budget_sweep}).
87	
88	See Appendix~\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\ref{sec:budget_sweep} (budget sweep) for additional detail.
89	
90	MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
91	
92	\paragraph{Comparison with KIVI.}
93	KIVI~\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.
94	At 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.
95	Within the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).
96	The two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.
97	However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.91), as the per-channel method subsumes the head-level reallocation signal.
98	Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.
99	
100	% TODO(kivi-compounding): KIVI asymmetric compounding result goes here.
101	% If compounding persists: "The compounding effect persists under KIVI-style
102	% per-channel asymmetric quantization (unconstrained PPL X.XX vs constrained Y.YY),
103	% confirming that the failure mode is driven by bit-width gaps rather than the
104	% quantization scheme. The cardinality constraint remains necessary even with
105	% more sophisticated per-channel methods."
106	% If compounding disappears: "Under KIVI-style per-channel asymmetric quantization,
107	% unconstrained allocation no longer exhibits compounding (PPL X.XX), suggesting
108	% that the failure mode is specific to symmetric quantization where per-channel
109	% compensation is unavailable. This scopes our cardinality constraint contribution
110	% to symmetric quantization environments."
111	
112	\subsection{Cross-Architecture Compounding}
113	\label{sec:compounding_cross}
114	
115	\begin{figure}[t]
116	\centering
117	\includegraphics[width=\columnwidth]{figures/fig_compounding_curves.pdf}
118	\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $188\times$ baseline (PPL 1519) at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\times$). All three stay near-baseline for $k{\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\approx}96$ due to its 112 KV heads (maximum ${\sim}96$ eligible for 2-bit assignment).}
119	\label{fig:compounding_cross}
120	\end{figure}
121	
122	Figure~\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.
123	At small $k$ (${\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\leq}2.5\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.
124	
125	Beyond $k{=}8$, divergence is stark.
126	Llama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.
127	This binary failure mode---stable until the critical head is corrupted, then catastrophic---is analogous to critical-node failure in sparse networks.
128	Qwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\times$) and $98.75$ at $k{=}256$ ($10.1\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.
129	At $k{=}64$, the observed PPL exceeds the additive prediction by $4.89\times$, confirming severe super-additivity.
130	Mistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.
131	
132	These curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\times$ baseline) is ${\sim}32$ for Qwen, ${\sim}64$ for Llama, and ${\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.
133	
134	\subsection{Downstream Evaluation}
135	\label{sec:downstream}
136	
137	\begin{table}[t]
138	\centering
139	\small
140	\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen values are mean over 3 calibration seeds ($\pm$1$\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}
141	\label{tab:downstream}
142	\begin{tabular}{lccccc}
143	\toprule
144	Model & ARC-C & HS & PIQA & WG & Avg \\
145	\midrule
146	Qwen2.5-7B        & $+$0.0{\scriptsize$\pm$0.4} & $+$4.1{\scriptsize$\pm$0.2} & $+$2.0{\scriptsize$\pm$0.2} & $+$1.6{\scriptsize$\pm$1.2} & $+$1.9 \\
147	Yi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\
148	Llama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\
149	Mistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\
150	Gemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
156	The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
157	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
158	Cross-dataset evaluation (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.
159	Long-context evaluation (Appendix~\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K, while constrained MCKP remains stable ($1.11\times$ to $1.23\times$).
160	In contrast, all three non-spread models show no benefit or slight degradation at 8K.
161	Llama-3.1-8B (spike, $t_1/t_5{=}0.85$): uniform $1.08\times$ bf16, MCKP $1.08\times$---identical.
162	Mistral-7B (flat, $c{=}0.24$): uniform $1.02\times$ bf16, MCKP $1.02\times$---identical.
163	Yi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\times$ bf16, MCKP $1.06\times$---no benefit or slight degradation ($+$0.06~PPL), consistent with spike classification.
164	The uniform-to-constrained PPL ratio on Qwen widens from $1.4\times$ at 2K to $9.1\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.
165	We note that Qwen-7B also has the fewest KV heads (112) in our test set; whether the long-context amplification is driven by the spread pattern, the low head count, or their interaction remains an open question requiring evaluation on additional spread-pattern models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "edfa3d77-0b4b-4f41-aa6b-edd27b9ef171",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate nine models spanning seven architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{CodeLlama-7B}\\footnote{CodeLlama multi-bit profiles synthesized from 2-bit-only profiling; classification robust as constrained allocation is dominated by 4-bit heads.} (MHA 1:1, 32 $\\times$ 32 = 1024),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nAll nine models undergo full constrained evaluation.\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5, Llama, CodeLlama, and Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite high concentration (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nThe additive distortion assumption underlying standard MCKP formulations systematically fails at these bit-width gaps.\n\n\\paragraph{Aggressive compression.}\nAt higher compression (5.3$\\times$), the cardinality constraint becomes valuable even for non-spread models: on Llama, constrained MCKP reduces PPL from 2643.8 (uniform 2-bit) to 57.6 (45$\\times$ improvement); on Mistral, from 519.1 to 11.9 (44$\\times$ improvement). The constraint's universal value emerges at aggressive compression ratios where uniform low-bit becomes insufficient (Appendix~\\ref{sec:budget_sweep}).\n\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.91), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n% TODO(kivi-compounding): KIVI asymmetric compounding result goes here.\n% If compounding persists: \"The compounding effect persists under KIVI-style\n% per-channel asymmetric quantization (unconstrained PPL X.XX vs constrained Y.YY),\n% confirming that the failure mode is driven by bit-width gaps rather than the\n% quantization scheme. The cardinality constraint remains necessary even with\n% more sophisticated per-channel methods.\"\n% If compounding disappears: \"Under KIVI-style per-channel asymmetric quantization,\n% unconstrained allocation no longer exhibits compounding (PPL X.XX), suggesting\n% that the failure mode is specific to symmetric quantization where per-channel\n% compensation is unavailable. This scopes our cardinality constraint contribution\n% to symmetric quantization environments.\"\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $188\\times$ baseline (PPL 1519) at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nThis binary failure mode---stable until the critical head is corrupted, then catastrophic---is analogous to critical-node failure in sparse networks.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nAt $k{=}64$, the observed PPL exceeds the additive prediction by $4.89\\times$, confirming severe super-additivity.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\nLong-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\nIn contrast, all three non-spread models show no benefit or slight degradation at 8K.\nLlama-3.1-8B (spike, $t_1/t_5{=}0.85$): uniform $1.08\\times$ bf16, MCKP $1.08\\times$---identical.\nMistral-7B (flat, $c{=}0.24$): uniform $1.02\\times$ bf16, MCKP $1.02\\times$---identical.\nYi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\\times$ bf16, MCKP $1.06\\times$---no benefit or slight degradation ($+$0.06~PPL), consistent with spike classification.\nThe uniform-to-constrained PPL ratio on Qwen widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.\nWe note that Qwen-7B also has the fewest KV heads (112) in our test set; whether the long-context amplification is driven by the spread pattern, the low head count, or their interaction remains an open question requiring evaluation on additional spread-pattern models.",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me plan:

1. **Task 1**: Add "Architectural bottleneck" paragraph to analysis.tex. The best place is after the TODO comment at line 91-92, or near the end of the analysis section. Looking at the structure, the TODO at line 91-92 says `% TODO(kivi-compounding): If KIVI compounding persists, add discussion of quantization-scheme independence here. If disappears, add scoping discussion.` — this is in analysis.tex at the very end. The "Architectural bottleneck" paragraph should go before this TODO or replace it. 

I'll place the new paragraph after line 89 (the appendix references line) and before the TODO comment, since it's a separate discussion point from the KIVI-specific compounding results.

2. **Task 2**: In experiments.tex, find the KIVI placeholder at lines 100-110 and write the two branch texts there, incorporating the KIVI data points like the uniform 4-bit result of 9.91.

Let me make both edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "ee317b8b-7b2b-4de5-81b9-2377deabd024",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178qeqHpf7VhyiXJRDox4LK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9763,
      "cache_read_input_tokens": 24974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9763
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

_source line 10_

Now I'll make both edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "062b3e27-cc48-4549-a452-13892c96ff5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178qeqHpf7VhyiXJRDox4LK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9763,
      "cache_read_input_tokens": 24974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9763
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

<details open><summary>🔧 Tool call — Edit · `toolu_01DtfJk2pxL3L1yGsE6pJQoY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "Additional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n\n% TODO(kivi-compounding): If KIVI compounding persists, add discussion of\n% quantization-scheme independence here. If disappears, add scoping discussion.",
  "new_string": "Additional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n\n\\paragraph{Architectural bottleneck.}\nThe method's ceiling is architectural, not algorithmic.\nKIVI-style per-channel asymmetric quantization~\\cite{liu2024kivi} achieves 9.91 PPL on Qwen (vs.\\ 9.81 bf16) with uniform 4-bit allocation alone---completely subsuming the head-level reallocation signal that our symmetric constrained MCKP exploits (10.91).\nThe 100\\% gap between KIVI~9.91 and symmetric uniform~15.45 originates in the quantization scheme, not the allocation strategy; composing KIVI with MCKP yields 9.90, identical to KIVI alone, confirming that per-channel information renders head-level optimization redundant.\nThe practical implication is clear: when hardware supports per-channel asymmetric quantization, practitioners should use it directly; our cardinality-constrained allocation provides independent value only in symmetric-only deployment environments---common in hardware accelerators that lack per-channel support---where it is the sole mechanism for exploiting sensitivity heterogeneity.\nIn those symmetric environments, the constraint's value is not PPL optimization per se but catastrophic-failure prevention: on Qwen, unconstrained symmetric allocation degrades to 32.45 PPL ($3.3\\times$ bf16), while the cardinality constraint reduces this to 10.91, a safeguard that no allocation strategy can replicate under per-channel schemes because the failure mode itself disappears."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "79f505d3-6240-4661-9690-bda6d1c5048e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178qeqHpf7VhyiXJRDox4LK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9763,
      "cache_read_input_tokens": 24974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9763
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

_source line 12 · 2026-05-16T10:22:31.364Z_

<details><summary>↩ Tool result · `toolu_01DtfJk2pxL3L1yGsE6pJQoY`</summary>

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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "a39c76ab-366d-45e6-9846-232e406102c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "oldString": "Additional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n\n% TODO(kivi-compounding): If KIVI compounding persists, add discussion of\n% quantization-scheme independence here. If disappears, add scoping discussion.",
    "newString": "Additional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n\n\\paragraph{Architectural bottleneck.}\nThe method's ceiling is architectural, not algorithmic.\nKIVI-style per-channel asymmetric quantization~\\cite{liu2024kivi} achieves 9.91 PPL on Qwen (vs.\\ 9.81 bf16) with uniform 4-bit allocation alone---completely subsuming the head-level reallocation signal that our symmetric constrained MCKP exploits (10.91).\nThe 100\\% gap between KIVI~9.91 and symmetric uniform~15.45 originates in the quantization scheme, not the allocation strategy; composing KIVI with MCKP yields 9.90, identical to KIVI alone, confirming that per-channel information renders head-level optimization redundant.\nThe practical implication is clear: when hardware supports per-channel asymmetric quantization, practitioners should use it directly; our cardinality-constrained allocation provides independent value only in symmetric-only deployment environments---common in hardware accelerators that lack per-channel support---where it is the sole mechanism for exploiting sensitivity heterogeneity.\nIn those symmetric environments, the constraint's value is not PPL optimization per se but catastrophic-failure prevention: on Qwen, unconstrained symmetric allocation degrades to 32.45 PPL ($3.3\\times$ bf16), while the cardinality constraint reduces this to 10.91, a safeguard that no allocation strategy can replicate under per-channel schemes because the failure mode itself disappears.",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across nine models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite high concentration ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nCodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\\%$ of top-5 delta, $11.3\\times$ the second-ranked head) yields no benefit when dominated by a single outlier; constrained MCKP ($k{=}2$) confirms: $+$0.17 vs.\\ uniform $+$0.19, consistent with a near-uniform allocation (1021/1024 heads at 4-bit). %exp_id=codellama_constrained_mckp\nMistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\nPhi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL).\nAlthough $t_1/t_5$ is low (indicating no dominant outlier), the concentration of 0.17 places the cumulative top-5\\% delta below the level required for meaningful reallocation---spread structure without sufficient absolute magnitude does not create optimization opportunities. %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\\\\nPhi-3-medium-14B & 4:1 & 0.17 & 0.23 & $+$0.16 & $+$0.18 & Flat \\\\\nCodeLlama-7B & 1:1 & 0.80 & 0.81 & $+$0.19 & $+$0.17 & Spike \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\geq 0.50$ \\emph{and} $t_1/t_5 \\leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 > 0.70$ \\emph{and} concentration $\\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.\n\\item \\textbf{Flat} (concentration $< 0.25$, or concentration $\\in [0.25, 0.50)$ with $t_1/t_5 \\leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \\geq 0.70$) correctly override.\nA concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.\nThe rule is experimentally confirmed on all nine models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat), Pythia-1.4B (MHA, flat), and CodeLlama-7B (MHA, spike).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\n\\paragraph{Why is Qwen-7B the only spread model?}\nWe offer two non-exclusive hypotheses, both requiring further validation.\nFirst, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.\nHowever, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.\nSecond, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\\ 0.57).\nThis suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.\n\nOn Qwen-7B, a simple L0-protection heuristic with random downgrade captures 93\\% of the MCKP benefit under standard-resolution profiling (median PPL 11.52 vs MCKP 11.23), suggesting that identifying which heads to \\emph{protect} matters more than the optimization algorithm---consistent with our solver-equivalence finding.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n\n% TODO(kivi-compounding): If KIVI compounding persists, add discussion of\n% quantization-scheme independence here. If disappears, add scoping discussion.\n",
    "structuredPatch": [
      {
        "oldStart": 88,
        "oldLines": 5,
        "newStart": 88,
        "newLines": 9,
        "lines": [
          " ",
          " Additional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.",
          " ",
          "-% TODO(kivi-compounding): If KIVI compounding persists, add discussion of",
          "-% quantization-scheme independence here. If disappears, add scoping discussion.",
          "+\\paragraph{Architectural bottleneck.}",
          "+The method's ceiling is architectural, not algorithmic.",
          "+KIVI-style per-channel asymmetric quantization~\\cite{liu2024kivi} achieves 9.91 PPL on Qwen (vs.\\ 9.81 bf16) with uniform 4-bit allocation alone---completely subsuming the head-level reallocation signal that our symmetric constrained MCKP exploits (10.91).",
          "+The 100\\% gap between KIVI~9.91 and symmetric uniform~15.45 originates in the quantization scheme, not the allocation strategy; composing KIVI with MCKP yields 9.90, identical to KIVI alone, confirming that per-channel information renders head-level optimization redundant.",
          "+The practical implication is clear: when hardware supports per-channel asymmetric quantization, practitioners should use it directly; our cardinality-constrained allocation provides independent value only in symmetric-only deployment environments---common in hardware accelerators that lack per-channel support---where it is the sole mechanism for exploiting sensitivity heterogeneity.",
          "+In those symmetric environments, the constraint's value is not PPL optimization per se but catastrophic-failure prevention: on Qwen, unconstrained symmetric allocation degrades to 32.45 PPL ($3.3\\times$ bf16), while the cardinality constraint reduces this to 10.91, a safeguard that no allocation strategy can replicate under per-channel schemes because the failure mode itself disappears."
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01KZRy2aLp6MRC1amSeH9AzY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "% TODO(kivi-compounding): KIVI asymmetric compounding result goes here.\n% If compounding persists: \"The compounding effect persists under KIVI-style\n% per-channel asymmetric quantization (unconstrained PPL X.XX vs constrained Y.YY),\n% confirming that the failure mode is driven by bit-width gaps rather than the\n% quantization scheme. The cardinality constraint remains necessary even with\n% more sophisticated per-channel methods.\"\n% If compounding disappears: \"Under KIVI-style per-channel asymmetric quantization,\n% unconstrained allocation no longer exhibits compounding (PPL X.XX), suggesting\n% that the failure mode is specific to symmetric quantization where per-channel\n% compensation is unavailable. This scopes our cardinality constraint contribution\n% to symmetric quantization environments.\"",
  "new_string": "% BEGIN BRANCH-A (kivi-compounding-persists)\n% Under KIVI-style per-channel asymmetric quantization, unconstrained head-level\n% allocation still exhibits compounding: PPL rises from $\\mathrm{X}$ at $k{=}2$\n% to $\\mathrm{Y}$ at $k{=}64$, a $\\mathrm{Z}{\\times}$ super-linear degradation.\n% The cardinality constraint reduces this to $\\mathrm{W}$, confirming that\n% compounding is driven by bit-width gaps rather than quantization\n% scheme---the constraint provides independent value even when per-channel\n% information is available.\n% END BRANCH-A\n\n% BEGIN BRANCH-B (kivi-compounding-disappears)\n% Under KIVI-style per-channel asymmetric quantization, unconstrained allocation\n% no longer exhibits catastrophic compounding (PPL $\\mathrm{X}$ at $k{=}64$ vs\n% $\\mathrm{Y}$ at $k{=}2$, only $\\mathrm{Z}{\\times}$ increase). Per-channel\n% scaling effectively absorbs the inter-head distortion that causes symmetric\n% compounding. This confirms that the cardinality constraint's primary value lies\n% in symmetric-only deployment environments where per-channel scaling is\n% unavailable.\n% END BRANCH-B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "5d90dc05-ab0a-491e-bb09-3800b0a22ca5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178qeqHpf7VhyiXJRDox4LK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9763,
      "cache_read_input_tokens": 24974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9763
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

_source line 14 · 2026-05-16T10:22:39.387Z_

<details><summary>↩ Tool result · `toolu_01KZRy2aLp6MRC1amSeH9AzY`</summary>

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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "01337ac6-cb97-44fa-b360-4705997c51c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "% TODO(kivi-compounding): KIVI asymmetric compounding result goes here.\n% If compounding persists: \"The compounding effect persists under KIVI-style\n% per-channel asymmetric quantization (unconstrained PPL X.XX vs constrained Y.YY),\n% confirming that the failure mode is driven by bit-width gaps rather than the\n% quantization scheme. The cardinality constraint remains necessary even with\n% more sophisticated per-channel methods.\"\n% If compounding disappears: \"Under KIVI-style per-channel asymmetric quantization,\n% unconstrained allocation no longer exhibits compounding (PPL X.XX), suggesting\n% that the failure mode is specific to symmetric quantization where per-channel\n% compensation is unavailable. This scopes our cardinality constraint contribution\n% to symmetric quantization environments.\"",
    "newString": "% BEGIN BRANCH-A (kivi-compounding-persists)\n% Under KIVI-style per-channel asymmetric quantization, unconstrained head-level\n% allocation still exhibits compounding: PPL rises from $\\mathrm{X}$ at $k{=}2$\n% to $\\mathrm{Y}$ at $k{=}64$, a $\\mathrm{Z}{\\times}$ super-linear degradation.\n% The cardinality constraint reduces this to $\\mathrm{W}$, confirming that\n% compounding is driven by bit-width gaps rather than quantization\n% scheme---the constraint provides independent value even when per-channel\n% information is available.\n% END BRANCH-A\n\n% BEGIN BRANCH-B (kivi-compounding-disappears)\n% Under KIVI-style per-channel asymmetric quantization, unconstrained allocation\n% no longer exhibits catastrophic compounding (PPL $\\mathrm{X}$ at $k{=}64$ vs\n% $\\mathrm{Y}$ at $k{=}2$, only $\\mathrm{Z}{\\times}$ increase). Per-channel\n% scaling effectively absorbs the inter-head distortion that causes symmetric\n% compounding. This confirms that the cardinality constraint's primary value lies\n% in symmetric-only deployment environments where per-channel scaling is\n% unavailable.\n% END BRANCH-B",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate nine models spanning seven architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{CodeLlama-7B}\\footnote{CodeLlama multi-bit profiles synthesized from 2-bit-only profiling; classification robust as constrained allocation is dominated by 4-bit heads.} (MHA 1:1, 32 $\\times$ 32 = 1024),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nAll nine models undergo full constrained evaluation.\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5, Llama, CodeLlama, and Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite high concentration (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nThe additive distortion assumption underlying standard MCKP formulations systematically fails at these bit-width gaps.\n\n\\paragraph{Aggressive compression.}\nAt higher compression (5.3$\\times$), the cardinality constraint becomes valuable even for non-spread models: on Llama, constrained MCKP reduces PPL from 2643.8 (uniform 2-bit) to 57.6 (45$\\times$ improvement); on Mistral, from 519.1 to 11.9 (44$\\times$ improvement). The constraint's universal value emerges at aggressive compression ratios where uniform low-bit becomes insufficient (Appendix~\\ref{sec:budget_sweep}).\n\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.91), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n% TODO(kivi-compounding): KIVI asymmetric compounding result goes here.\n% If compounding persists: \"The compounding effect persists under KIVI-style\n% per-channel asymmetric quantization (unconstrained PPL X.XX vs constrained Y.YY),\n% confirming that the failure mode is driven by bit-width gaps rather than the\n% quantization scheme. The cardinality constraint remains necessary even with\n% more sophisticated per-channel methods.\"\n% If compounding disappears: \"Under KIVI-style per-channel asymmetric quantization,\n% unconstrained allocation no longer exhibits compounding (PPL X.XX), suggesting\n% that the failure mode is specific to symmetric quantization where per-channel\n% compensation is unavailable. This scopes our cardinality constraint contribution\n% to symmetric quantization environments.\"\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $188\\times$ baseline (PPL 1519) at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nThis binary failure mode---stable until the critical head is corrupted, then catastrophic---is analogous to critical-node failure in sparse networks.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nAt $k{=}64$, the observed PPL exceeds the additive prediction by $4.89\\times$, confirming severe super-additivity.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\nLong-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\nIn contrast, all three non-spread models show no benefit or slight degradation at 8K.\nLlama-3.1-8B (spike, $t_1/t_5{=}0.85$): uniform $1.08\\times$ bf16, MCKP $1.08\\times$---identical.\nMistral-7B (flat, $c{=}0.24$): uniform $1.02\\times$ bf16, MCKP $1.02\\times$---identical.\nYi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\\times$ bf16, MCKP $1.06\\times$---no benefit or slight degradation ($+$0.06~PPL), consistent with spike classification.\nThe uniform-to-constrained PPL ratio on Qwen widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.\nWe note that Qwen-7B also has the fewest KV heads (112) in our test set; whether the long-context amplification is driven by the spread pattern, the low head count, or their interaction remains an open question requiring evaluation on additional spread-pattern models.",
    "structuredPatch": [
      {
        "oldStart": 97,
        "oldLines": 18,
        "newStart": 97,
        "newLines": 26,
        "lines": [
          " However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.91), as the per-channel method subsumes the head-level reallocation signal.",
          " Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.",
          " ",
          "-% TODO(kivi-compounding): KIVI asymmetric compounding result goes here.",
          "-% If compounding persists: \"The compounding effect persists under KIVI-style",
          "-% per-channel asymmetric quantization (unconstrained PPL X.XX vs constrained Y.YY),",
          "-% confirming that the failure mode is driven by bit-width gaps rather than the",
          "-% quantization scheme. The cardinality constraint remains necessary even with",
          "-% more sophisticated per-channel methods.\"",
          "-% If compounding disappears: \"Under KIVI-style per-channel asymmetric quantization,",
          "-% unconstrained allocation no longer exhibits compounding (PPL X.XX), suggesting",
          "-% that the failure mode is specific to symmetric quantization where per-channel",
          "-% compensation is unavailable. This scopes our cardinality constraint contribution",
          "-% to symmetric quantization environments.\"",
          "+% BEGIN BRANCH-A (kivi-compounding-persists)",
          "+% Under KIVI-style per-channel asymmetric quantization, unconstrained head-level",
          "+% allocation still exhibits compounding: PPL rises from $\\mathrm{X}$ at $k{=}2$",
          "+% to $\\mathrm{Y}$ at $k{=}64$, a $\\mathrm{Z}{\\times}$ super-linear degradation.",
          "+% The cardinality constraint reduces this to $\\mathrm{W}$, confirming that",
          "+% compounding is driven by bit-width gaps rather than quantization",
          "+% scheme---the constraint provides independent value even when per-channel",
          "+% information is available.",
          "+% END BRANCH-A",
          " ",
          "+% BEGIN BRANCH-B (kivi-compounding-disappears)",
          "+% Under KIVI-style per-channel asymmetric quantization, unconstrained allocation",
          "+% no longer exhibits catastrophic compounding (PPL $\\mathrm{X}$ at $k{=}64$ vs",
          "+% $\\mathrm{Y}$ at $k{=}2$, only $\\mathrm{Z}{\\times}$ increase). Per-channel",
          "+% scaling effectively absorbs the inter-head distortion that causes symmetric",
          "+% compounding. This confirms that the cardinality constraint's primary value lies",
          "+% in symmetric-only deployment environments where per-channel scaling is",
          "+% unavailable.",
          "+% END BRANCH-B",
          "+",
          " \\subsection{Cross-Architecture Compounding}",
          " \\label{sec:compounding_cross}",
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

_source line 15_

验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "1efd4773-fca9-4dde-8115-344f0a216524",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDEjPG9fMjU3Q77hvkmsiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1841,
      "cache_read_input_tokens": 34737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1841
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

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_01S2tEGyhjkeACBNNQviwgLx`</summary>

```json
{
  "pattern": "Architectural bottleneck",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "438e63b9-9f20-446a-a398-7854d96cb2a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDEjPG9fMjU3Q77hvkmsiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1841,
      "cache_read_input_tokens": 34737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1841
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

_source line 17 · 2026-05-16T10:22:42.828Z_

<details><summary>↩ Tool result · `toolu_01S2tEGyhjkeACBNNQviwgLx`</summary>

```text
docs/paper/analysis.tex:91:\paragraph{Architectural bottleneck.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "f1ecf414-9e6a-44ce-b8b6-6f30581ab929",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:91:\\paragraph{Architectural bottleneck.}",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01WbmqxYNL5TBym7EYgE8mG2`</summary>

```json
{
  "pattern": "BRANCH-A|BRANCH-B",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
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
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "e22e38fa-0972-44a4-9dce-cd50f1a6e371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDEjPG9fMjU3Q77hvkmsiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1841,
      "cache_read_input_tokens": 34737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1841
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

_source line 19 · 2026-05-16T10:22:43.370Z_

<details><summary>↩ Tool result · `toolu_01WbmqxYNL5TBym7EYgE8mG2`</summary>

```text
docs/paper/experiments.tex:100:% BEGIN BRANCH-A (kivi-compounding-persists)
docs/paper/experiments.tex:108:% END BRANCH-A
docs/paper/experiments.tex:110:% BEGIN BRANCH-B (kivi-compounding-disappears)
docs/paper/experiments.tex:118:% END BRANCH-B
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "8ecb9f7b-5a83-4dc9-b158-378658514285",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:100:% BEGIN BRANCH-A (kivi-compounding-persists)\ndocs/paper/experiments.tex:108:% END BRANCH-A\ndocs/paper/experiments.tex:110:% BEGIN BRANCH-B (kivi-compounding-disappears)\ndocs/paper/experiments.tex:118:% END BRANCH-B",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 20_

三项验证全部通过：

1. `\paragraph{Architectural bottleneck.}` — analysis.tex L91，在 appendix 引用之后
2. `BRANCH-A` (kivi-compounding-persists) — experiments.tex L100-108
3. `BRANCH-B` (kivi-compounding-disappears) — experiments.tex L110-118

两版预写文本均为纯注释状态，占位符 `$\mathrm{X}$` / `$\mathrm{Y}$` / `$\mathrm{Z}$` / `$\mathrm{W}$` 就位，结果出来后取消注释并填数字即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "uuid": "c9ab5446-68b6-465e-9311-1e794c357d1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Af4dsuoi3qwLDAiaWmY7bb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 36578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 397
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

_source line 21_

三项验证全部通过：

1. `\paragraph{Architectural bottleneck.}` — analysis.tex L91，在 appendix 引用之后
2. `BRANCH-A` (kivi-compounding-persists) — experiments.tex L100-108
3. `BRANCH-B` (kivi-compounding-disappears) — experiments.tex L110-118

两版预写文本均为纯注释状态，占位符 `$\mathrm{X}$` / `$\mathrm{Y}$` / `$\mathrm{Z}$` / `$\mathrm{W}$` 就位，结果出来后取消注释并填数字即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 44392,
  "duration_api_ms": 45483,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "31570cf7-e9fd-45d8-b627-5a46a7b14e2d",
  "total_cost_usd": 0.2690575,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 25134,
    "cache_read_input_tokens": 108130,
    "output_tokens": 2243,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25134,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 184,
        "cache_read_input_tokens": 36578,
        "cache_creation_input_tokens": 397,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 397
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1705,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 2243,
      "cacheReadInputTokens": 108130,
      "cacheCreationInputTokens": 25134,
      "webSearchRequests": 0,
      "costUSD": 0.26725750000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b52a9d85-b9cc-4c07-b6ce-93ea4dad0a17"
}
```

</details>

---
