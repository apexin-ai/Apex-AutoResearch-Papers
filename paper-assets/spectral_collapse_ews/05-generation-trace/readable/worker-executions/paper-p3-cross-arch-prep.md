# paper p3 cross arch prep

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_p3-cross-arch-prep_20260523T101106.log`
- **Structured JSON:** [`dd0efe14390c2623d7fd.json`](../../sessions/dd/dd0efe14390c2623d7fd.json)

## Before a recorded user message

19 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
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
  "uuid": "c0df2c95-2f04-404e-8282-a273ae574f8d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-5-projects-spectral-collapse-ews/memory/"
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
    "resetsAt": 1779546000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1f270c24-3435-46ac-88ee-2c781dd10901",
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1"
}
```

---

### Assistant

_source line 4_

I'll read both files first, then make the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "a8945a49-0313-4589-b6b1-17fafe485c6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mjpv5EX9q3XnvHG2SBDbs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13060,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13060
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_011XepyvSZwbu19GhapfE2VJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "09b41ed8-a826-410e-87fc-93b06ff60c08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mjpv5EX9q3XnvHG2SBDbs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13060,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13060
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 6 · 2026-05-23T10:11:17.950Z_

<details><summary>↩ Tool result · `toolu_011XepyvSZwbu19GhapfE2VJ`</summary>

```text
1	During the early stages of recursive synthetic training, spectral indicators of the embedding space suggest the model is improving---even as downstream performance is already degrading.
2	We reveal the source of this misleading signal by tracking spectral properties of the embedding matrix across 10 recursive generations of Pythia-410M, with pilot validation on Pythia-1B.
3	The result is a reproducible three-phase pattern, consistent across three random seeds (SLV CV $< 1.3\%$ at all generations): spectral decompression (generations 0--2), where effective rank and SLV increase while HellaSwag accuracy drops 3.3 percentage points (8.0\% relative); collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10).
4	Of eight indicators evaluated, SLV is the most effective collapse indicator: it requires only a single forward pass (${<}\,1$ second on one GPU, compared to ${\sim}70$ minutes for benchmark evaluation), captures volume changes across all spectral directions, and declines monotonically after the decompression peak.
5	By varying the real-data mixing ratio across five levels, we construct a collapse phase diagram that localizes the critical mixing ratio $r_{\text{crit}}$ to the interval $(0.25, 0.3]$ across three random seeds, separating monotonic spectral expansion from a transitional regime with initial contraction followed by recovery.
6	A proportional controller demonstrates an inherent signal attenuation: moderate real-data mixing prevents the spectral contraction that would activate the controller, so reactive spectral feedback becomes ineffective precisely when prevention succeeds.
7	Nevertheless, the empirically calibrated $r_{\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "6e011806-cecd-43fd-9b1b-fcf596b5a81c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex",
      "content": "During the early stages of recursive synthetic training, spectral indicators of the embedding space suggest the model is improving---even as downstream performance is already degrading.\nWe reveal the source of this misleading signal by tracking spectral properties of the embedding matrix across 10 recursive generations of Pythia-410M, with pilot validation on Pythia-1B.\nThe result is a reproducible three-phase pattern, consistent across three random seeds (SLV CV $< 1.3\\%$ at all generations): spectral decompression (generations 0--2), where effective rank and SLV increase while HellaSwag accuracy drops 3.3 percentage points (8.0\\% relative); collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10).\nOf eight indicators evaluated, SLV is the most effective collapse indicator: it requires only a single forward pass (${<}\\,1$ second on one GPU, compared to ${\\sim}70$ minutes for benchmark evaluation), captures volume changes across all spectral directions, and declines monotonically after the decompression peak.\nBy varying the real-data mixing ratio across five levels, we construct a collapse phase diagram that localizes the critical mixing ratio $r_{\\text{crit}}$ to the interval $(0.25, 0.3]$ across three random seeds, separating monotonic spectral expansion from a transitional regime with initial contraction followed by recovery.\nA proportional controller demonstrates an inherent signal attenuation: moderate real-data mixing prevents the spectral contraction that would activate the controller, so reactive spectral feedback becomes ineffective precisely when prevention succeeds.\nNevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01WyPeHKdxxVRcgqE1kzYnB6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "f91bfb4e-c037-4a4f-9e7f-d9f0e400ba3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mjpv5EX9q3XnvHG2SBDbs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13060,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13060
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 8 · 2026-05-23T10:11:18.140Z_

<details><summary>↩ Tool result · `toolu_01WyPeHKdxxVRcgqE1kzYnB6`</summary>

```text
1	
2	\subsection{Experimental Setup}
3	\label{subsec:setup}
4	
5	We use the publicly released final Pythia-410M-deduped checkpoint \citep{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.
6	Starting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.
7	At each generation we compute the spectral indicators from \S\ref{subsec:spectral_metrics} on 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.
8	These three metrics (language modeling capability, natural language understanding, and generation diversity) cover the primary evaluation dimensions accessible to a 410M-parameter model.
9	
10	For the mixing comparison (\S\ref{subsec:phase1}), we evaluate three strategies:
11	(1)~\textbf{pure collapse} ($r_t{=}0$),
12	(2)~\textbf{fixed mix} ($r_t{=}0.50$), and
13	(3)~\textbf{adaptive} ($k{=}10$, Eq.~\ref{eq:controller}).
14	To construct the collapse phase diagram (\S\ref{subsec:phase_diagram_exp}), we additionally evaluate fixed mixing at $r \in \{0.2, 0.25, 0.3\}$.
15	
16	\subsection{Spectral Collapse Characterization}
17	\label{subsec:phase0}
18	
19	Table~\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.
20	
21	\begin{table}[t]
22	\centering
23	\small
24	\setlength{\tabcolsep}{4pt}
25	\begin{tabular}{@{}rrrrrrc@{}}
26	\toprule
27	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
28	\midrule
29	0  & 417.55 & 2366.68 &  9.55 & .413 & .738 & 1942.8 \\
30	2  & \textbf{496.17} & \textbf{2467.98} & 13.56 & .380 & .505 &  718.7 \\
31	5  & 479.77 & 2365.99 & 24.50 & .341 & .412 &  749.2 \\
32	7  & 464.10 & 2293.24 & 37.82 & .319 & .375 &  788.4 \\
33	10 & 438.05 & 2181.35 & 70.99 & .296 & .324 &  874.6 \\
34	\bottomrule
35	\end{tabular}
36	\caption{Spectral and downstream metrics at selected generations (Pythia-410M, mean of three seeds 42, 43, 44; sample s.d.\ at Gen~10: $r_{\text{eff}}$ $\pm$4.8, SLV $\pm$28.3, PPL $\pm$5.6, HeSw $\pm$.006, D-4 $\pm$.15). Bold marks the spectral peak.}
37	\label{tab:phase0}
38	\end{table}
39	
40	\begin{figure}[t]
41	\centering
42	\includegraphics[width=\columnwidth]{figures/spectral_trajectory.pdf}
43	\caption{SLV across 10 recursive generations of Pythia-410M (solid: $r{=}0$, 3-seed mean; dashed: $r{=}0.5$, 2-seed mean) under pure-synthetic training and 50\% real-data mixing. Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2468), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 11\% from peak to 2181). Under 50\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\% above baseline and 104 points above the pure-collapse peak.}
44	\label{fig:spectral_trajectory}
45	\end{figure}
46	
47	\paragraph{Phase I: Spectral Decompression (Gen~0--2).}
48	In the first two generations, $r_{\text{eff}}$ rises from 417.55 to 496.2 (+18.8\%) and SLV increases from 2366.7 to 2468.0 (+4.3\%), while $\sigma_1$ drops sharply from 1942.8 to 718.7 as spectral mass redistributes from the dominant direction to smaller components.
49	The consistency of the peak position (Gen~2 across all three seeds) and its coincidence with the qualitative reversal of $\sigma_1$ dynamics (from declining to rising) suggest that the phase boundary reflects a structural transition rather than a statistical artifact.
50	Crucially, this decompression does not indicate improved model quality: HellaSwag drops from 0.413 to 0.380 ($-$8.0\%) and distinct-4 falls from 0.738 to 0.505 ($-$31.6\%) during the same interval.
51	HellaSwag already declines 5.4\% from Gen~0 to Gen~1, precisely when spectral indicators are still rising; this asymmetry suggests that decompression captures distributional broadening rather than preservation of task-supporting representations.
52	SLV's value lies not in temporal precedence but in computational efficiency ($<$1\,s vs.\ ${\sim}$70\,min for benchmarks) and cross-seed robustness (CV $< 1.3\%$).
53	
54	\paragraph{Phase II: Collapse Onset (Gen~2--4).}
55	Both $r_{\text{eff}}$ and SLV reverse after Gen~2 ($r_{\text{eff}}$: 496.2$\to$493.6, SLV: 2468$\to$2440), and this reversal marks the transition from decompression to collapse while perplexity continues its monotonic rise.
56	
57	\paragraph{Phase III: Accelerating Collapse (Gen~4--10).}
58	Spectral contraction accelerates: the mean per-generation $r_{\text{eff}}$ decline in Phase~III is $1.78 \pm 0.22$\%/gen (mean $\pm$ s.d.\ across three seeds).
59	By Gen~10, $r_{\text{eff}}$ falls to 438.1 ($-$11.7\% from peak), SLV drops to 2181.4 ($-$7.8\% from baseline), perplexity reaches 71.0 ($+$643\%), and $\sigma_1$ reverses its earlier decline, reaching 874.6 at Gen~10, a sign of renewed spectral concentration (Figure~\ref{fig:spectral_trajectory}).
60	
61	\paragraph{Cross-Scale Pilot.}
62	Repeating the protocol on Pythia-1B (Gen~0--3) confirms the same decompression-onset structure ($r_{\text{eff}}$ peak at Gen~2, SLV peak one generation earlier). SLV's low cost and monotonic post-peak decline make it well-suited as an automated collapse indicator.
63	In our setup, SLV computation (1{,}000-sample forward pass plus SVD of the $n {\times} d$ embedding matrix) takes ${<}\,1$~second on a single GPU, whereas HellaSwag 0-shot evaluation requires ${\sim}70$~minutes end-to-end under identical hardware.
64	
65	\subsection{Adaptive Mixing Comparison}
66	\label{subsec:phase1}
67	
68	Under pure synthetic training (\S\ref{subsec:phase0}), SLV peaks at Gen~2 (2468) and declines monotonically; with 50\% mixing, SLV rises to 2572 at Gen~10 (104 points above the pure-collapse peak), with only a negligible Gen~1 dip ($\Delta_1 \approx 0.0003$, well below $\tau$).
69	
70	The adaptive controller ($k{=}10$) remains silent through all ten generations: $\max \Delta_t = 0.0003$ at Gen~1, well below $\tau{=}0.002$, and $\Delta_t \leq 0$ for all $t \geq 2$.
71	Retrospectively computing the controller signal on each fixed-ratio trajectory reveals that even moderate mixing that does not prevent downstream degradation (PPL $+$45\% at $r{=}0.2$) suffices to suppress the rate-based signal.
72	Pure collapse produces SLV decline from Gen~3 while $r{=}0.5$ yields sustained growth, bounding $0.2 < r_{\text{crit}} \leq 0.5$ (\S\ref{subsec:phase_diagram_exp}).
73	
74	Despite sustained spectral expansion, downstream metrics degrade steadily: perplexity increases 58\% ($9.55 \to 15.12$) and distinct-4 falls 79\% ($.738 \to .152$) over ten generations, the lowest D-4 of any condition, below even pure collapse ($r{=}0$: 0.324).
75	This reinforces the asymmetry from \S\ref{subsec:phase0}: spectral health under mixed training does not guarantee model health, and signal attenuation renders per-generation reactive controllers ineffective precisely when collapse prevention succeeds.
76	This attenuation is inherent to any rate-based indicator~\citep{scheffer2009ews}; our contribution is quantifying how it creates a continuous degradation of monitoring capability across the sub-critical regime.
77	
78	\subsection{Alternative EWS Comparison}
79	\label{subsec:alt_ews}
80	
81	We compare SLV against seven alternative collapse indicators from three signal sources: embedding geometry (RankMe, isotropy), attention weights (stable rank, spectral norm), and output distributions (token entropy, raw perplexity, perplexity growth rate).
82	
83	Table~\ref{tab:ews_comparison} summarizes the comparison under pure-synthetic training ($r{=}0$).
84	Two indicators share SLV's decompression-then-collapse trajectory: RankMe~\citep{rankme2023}, the exponential of the normalized singular-value entropy, peaks at Gen~2 and declines monotonically thereafter, though with 2.5$\times$ lower signal-to-noise ratio (4.7\% relative change vs.\ 11.8\% for SLV).
85	Weight-level and output-level indicators (stable rank, spectral norm, token entropy) change monotonically from Gen~0 with no decompression phase; they cannot distinguish collapse onset from the initial fine-tuning transient.
86	Isotropy is the least reliable indicator: random sampling without a fixed seed introduces approximately 5\% variance, and it exhibits six monotonicity violations across ten generations, with direction reversals at Gen~4+ that produce a misleading recovery signal.
87	
88	\begin{table}[t]
89	\centering
90	\small
91	\setlength{\tabcolsep}{4pt}
92	\begin{tabular}{@{}llcrrc@{}}
93	\toprule
94	Indicator & Source & Peak & Mono? & Rel $\Delta$ & Rev.? \\
95	\midrule
96	SLV         & emb-SVD   & Gen 2 & \checkmark & 11.8\% & \checkmark \\
97	RankMe      & emb-SVD   & Gen 2 & \checkmark &  4.7\% & \checkmark \\
98	Token ent.  & logit     & ---   & \checkmark &  9.6\% & \checkmark \\
99	Stable rank & attn wt.  & ---   & \checkmark & 14.0\% & \checkmark \\
100	Spec.\ norm & attn wt.  & ---   & \checkmark &  8.0\% & \checkmark \\
101	Isotropy    & emb       & ---   & $\times$\,(6) & 75\%   & \checkmark \\
102	Raw PPL     & eval      & ---   & \checkmark & 643\%  & $\times$ \\
103	PPL growth  & ppl       & ---   & $\sim$\,(1) &  ---   & \checkmark \\
104	\bottomrule
105	\end{tabular}
106	\caption{Alternative early warning indicators under pure-synthetic training ($r{=}0$, Pythia-410M, 10 gen). \textbf{Peak}: generation at which the indicator reverses (--- = monotonic from Gen~0). \textbf{Mono?}: post-peak monotonicity (\checkmark\ = yes; number = violations). \textbf{Rel $\Delta$}: $|v_{10} - v_0|/|v_0|$, magnitude of total relative change Gen~0--10. \textbf{Rev.?}: direction reversal under $r{=}0.5$ mixing (\checkmark\ = reversed).}
107	\label{tab:ews_comparison}
108	\end{table}
109	
110	The final column of Table~\ref{tab:ews_comparison} reveals that seven of eight indicators reverse direction under 50\% real-data mixing; the exception is raw perplexity, which continues to increase (albeit more slowly), tracking cumulative degradation rather than directional spectral change.
111	This near-universality confirms that signal attenuation (\S\ref{subsec:controller}) is not specific to SLV: any per-generation reactive controller based on spectral or rate-based indicators will fall silent when mixing exceeds $r_{\text{crit}}$.
112	Among embedding-level metrics, SLV offers the highest signal-to-noise ratio (2.5$\times$ that of RankMe) and, together with RankMe, is the only indicator that exhibits a decompression baseline to distinguish collapse onset from training transients.
113	SLV is the only indicator that combines decompression-phase sensitivity, post-peak monotonicity, and sub-second computation cost; it shares a metric foundation with SIGMA's $\log\det G$ ($= 2 \times \text{SLV}$; \S\ref{sec:related}).
114	
115	\subsection{Collapse Phase Diagram}
116	\label{subsec:phase_diagram_exp}
117	
118	We now map SLV trajectories across mixing ratios to construct the collapse phase diagram defined in \S\ref{subsec:phase_diagram}.
119	Figure~\ref{fig:phase_diagram} plots SLV across 10 recursive generations for five mixing ratios; three qualitatively distinct trajectory types emerge:
120	
121	\begin{figure}[t]
122	\centering
123	\includegraphics[width=\columnwidth]{figures/phase_diagram.pdf}
124	\caption{SLV trajectories across mixing ratios (Pythia-410M; $r{=}0$ and $r{=}0.25$: 3-seed mean; $r{=}0.3$: 3-seed mean; $r{=}0.2$: single seed; $r{=}0.5$: 2-seed mean). Type~I ($r{=}0$): decompression then monotonic collapse. Type~II ($r{=}0.2$, $r{=}0.25$): transient dip followed by recovery. Type~III ($r{=}0.3$, $r{=}0.5$): monotonic expansion from Gen~2 onward. The shaded band marks the critical threshold $r_{\text{crit}} \in (0.25, 0.3]$. The dashed horizontal line indicates the Gen~0 baseline.}
125	\label{fig:phase_diagram}
126	\end{figure}
127	
128	\paragraph{Type~I: Pure Collapse ($r{=}0$).}
129	SLV exhibits large decompression ($+$97 points at Gen~1, peaking at Gen~2) followed by accelerating contraction (\S\ref{subsec:phase0}).
130	
131	\paragraph{Type~II: Near-critical Mixing ($r{=}0.2$).}
132	Twenty percent real data suppresses the SLV decompression phase: SLV rises only 0.78 points from Gen~0 to Gen~1 (vs.\ $+$98 under $r{=}0$), dips at Gen~2 ($2367.5 \to 2358.3$, $-9.2$).
133	Recovery begins at Gen~3, with per-generation gains accelerating from $+4.2$ to $+30.9$ (Gen~6) before moderating, reaching 2479.7 at Gen~10 ($+4.8\%$ above baseline).
134	Because $\widetilde{S}_2 = 2362.7 < \widetilde{S}_1 = 2367.1$ (EMA-smoothed SLV; \S\ref{subsec:controller}), the non-decreasing condition is violated and $r{=}0.2$ formally lies below $r_{\text{crit}}$.
135	The trajectory is consistent with the transitional regime (\S\ref{subsec:phase_diagram}): initial contraction followed by sustained recovery over the full 10-generation horizon.
136	The smoothed signal never exceeds the controller threshold ($\max \Delta_t = 0.0019$ at Gen~2, below $\tau = 0.002$), so as little as 20\% real data silences the controller entirely.
137	The effective rank still rises at Gen~2 ($476.7 \to 481.6$) while the EMA-smoothed SLV registers a net decline ($\widetilde{S}_2 < \widetilde{S}_1$), evidence that smoothed SLV detects spectral contraction earlier at this mixing ratio.
138	Effective rank cannot distinguish Type~II from Type~III trajectories---both show monotonic expansion for $r \geq 0.2$---whereas SLV's transient dip at $r{=}0.2$ uniquely identifies the transitional regime, underscoring SLV's finer discriminative power.
139	
140	At $r{=}0.25$, the full 10-generation trajectory follows the same Type~II pattern: SLV dips from Gen~0 to Gen~1 ($2366.7 \to 2362.1$, $-4.6$; seed~42, representative trajectory), reaches a minimum at Gen~2 ($2363.1$), then rises monotonically through Gen~10 (three-seed mean $2488.1$, $+5.1\%$ above baseline).
141	The EMA-smoothed sequence confirms the sub-critical classification: $\widetilde{S}_1 = 2364.4$, $\widetilde{S}_2 = 2363.8$, satisfying $\widetilde{S}_2 < \widetilde{S}_1$ and violating the non-decreasing condition.
142	Controller silence is more pronounced than at $r{=}0.2$: $\max \Delta_t = 0.00028 < \tau = 0.002$, a $6.7\times$ weaker signal than the $r{=}0.2$ maximum ($0.0019$), consistent with further signal attenuation as the real-data fraction increases.
143	The amplitude of the EMA violation at $r{=}0.25$ varies substantially across seeds ($\widetilde{S}_2 - \widetilde{S}_1 = -0.6$, $-1.7$, $-0.9$), consistent with the elevated fluctuations expected near a phase boundary, while trajectories at $r{=}0$ and $r \geq 0.3$ show low cross-seed variance ($< 0.5\%$).
144	
145	\paragraph{Type~III: Super-critical Mixing ($r \geq 0.3$).}
146	SLV rises monotonically from Gen~2 onward, reaching 2572 at Gen~10 ($+$8.7\% above baseline), consistent with $r{=}0.5 \geq r_{\text{crit}}$ (\S\ref{subsec:phase1}).
147	Per-generation gains remain positive through all post-transient generations ($\Delta_t \in [+11, +35]$ for $t \geq 2$; mean $+23.0$), sustaining expansion with no reversal toward the contraction trajectory of Type~I within the observed horizon.
148	
149	These three types partition the mixing-ratio axis into sub-critical ($r < r_{\text{crit}}$), transitional, and stable ($r \geq r_{\text{crit}}$) zones.
150	Type classification is based solely on spectral trajectory shape; downstream metrics such as D-4 may diverge, as demonstrated by the non-monotonic D-4 pattern across mixing ratios (Table~\ref{tab:phase_summary}).
151	At $r{=}0.3$, SLV expands monotonically from Gen~2 to 2508.2 at Gen~10 ($+$6.0\% above baseline), with sustained positive growth across all eight post-transient generations.
152	This confirms $r{=}0.3 \geq r_{\text{crit}}$ over the full 10-generation horizon, tightening the bound to $0.25 < r_{\text{crit}} \leq 0.3$.
153	Across three seeds, one individual EMA-smoothed trajectory shows a transient violation of 0.83~points at Gen~2; the remaining two satisfy non-decreasing from $t \geq 2$. The cross-seed mean trajectory is non-decreasing at all post-transient generations (Gen~10 SLV CV $= 0.12\%$), confirming the Type~III classification.
154	The single-seed transient is consistent with the continuous crossover interpretation: near the phase boundary, individual realizations may briefly exhibit sub-critical behavior even when the mean trajectory is stable.
155	The critical threshold is robust to the smoothing parameter: recomputing the EMA-smoothed SLV for $\alpha \in \{0.3, 0.5, 0.7\}$ yields $r_{\text{crit}} \in (0.25, 0.3]$ in all cases, with the non-decreasing condition violated at Gen~2 for $r \leq 0.25$ and satisfied on the cross-seed mean for $r \geq 0.3$ regardless of $\alpha$.
156	
157	The largest single-generation SLV drop in the first two generations shrinks with $r$: $-9.2$ at $r{=}0.2$ (Gen~1$\to$2), $-4.6$ at $r{=}0.25$ (Gen~0$\to$1; seed~42), and $-0.6$ at $r{=}0.3$ (Gen~0$\to$1), consistent with a continuous crossover rather than a sharp boundary.
158	The Type~II trajectory clarifies what $r_{\text{crit}}$ marks in practice: not a boundary between collapse and stability in final outcome, but a transition in trajectory shape.
159	Below $r_{\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion through Gen~10 once the transient passes.
160	
161	\paragraph{Output Diversity Divergence.}
162	At $r{=}0.2$, D-4 exhibits a V-shaped recovery (0.438 at Gen~5 $\to$ 0.520 at Gen~10), but this pattern does not generalize: at $r{=}0.25$, D-4 declines monotonically to 0.342 despite comparable SLV recovery, indicating that spectral expansion does not guarantee diversity restoration.
163	More broadly, D-4 exhibits a non-monotonic relationship with $r$: it peaks at $r{=}0.2$ (.520), exceeds the pure-collapse baseline (.324) at $r \leq 0.25$ but drops below it at $r \geq 0.3$, reaching .152 at $r{=}0.5$, the lowest across all conditions (Table~\ref{tab:phase_summary}).
164	This pattern is consistent with increasing real-data anchoring: at high $r$, the model converges toward the fixed real-data distribution, producing coherent but stylistically homogeneous text.
165	This divergence between spectral health (monotonically improving with $r$) and n-gram diversity underscores that SLV and D-4 capture orthogonal aspects of model behavior.
166	D-4 exhibits substantially higher cross-seed variance than spectral metrics: at $r{=}0$ (s.d.\ $= 0.15$ vs.\ SLV s.d.\ $= 28$, a ${>}30\times$ lower coefficient of variation for SLV) and $r{=}0.3$ (s.d.\ $= 0.155$ vs.\ SLV s.d.\ $= 2.9$; Table~\ref{tab:phase_summary}), suggesting that n-gram diversity reflects stochastic generation choices rather than the deterministic geometric structure captured by SLV.
167	This pattern generalizes across mixing ratios: at $r{=}0.25$, SLV cross-seed CV is 0.12\% versus 3.9\% for D-4, confirming that spectral geometry captures a deterministic structural property largely independent of stochastic training noise.
168	
169	Table~\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.
170	
171	\begin{table}[t]
172	\centering
173	\small
174	\setlength{\tabcolsep}{4pt}
175	\begin{tabular}{@{}clrrrrrc@{}}
176	\toprule
177	$r$ & Type & SLV & $r_{\text{eff}}$ & PPL & D-4 & $\max\Delta_t$ & Gen. \\
178	\midrule
179	0    & I   & 2181.4 & 438.1 & 71.0\phantom{0} & .324 & ---   & 10 \\
180	0.20 & II  & 2479.7 & 511.3 & 13.83 & .520 & .0019 & 10 \\
181	0.25 & II  & 2488.1 & 513.8 & 13.41 & .342 & .0003 & 10 \\
182	0.30 & III & 2508.2 & 521.1 & 13.35 & .295 & 0     & 10 \\
183	0.50 & III & 2571.7 & 553.5 & 15.12 & .152 & 0     & 10 \\
184	\bottomrule
185	\end{tabular}
186	\caption{Final-generation spectral and downstream metrics across mixing ratios (all runs to Gen~10). $\max\Delta_t$ computed for $t \geq 2$, excluding the initial fine-tuning transient. Type classification follows \S\ref{subsec:phase_diagram}. $r{=}0$ reports the mean of three seeds (42, 43, 44); $r{=}0.3$ the mean of three seeds (42, 43, 44); $r{=}0.2$ reports a single seed; $r{=}0.5$ the mean of two seeds (42, 43); $r{=}0.25$ the mean of three seeds (42, 43, 44). D-4 exhibits high cross-seed variance at $r{=}0$ (s.d.\ $= 0.15$) and $r{=}0.3$ (s.d.\ $= 0.155$).}
187	\label{tab:phase_summary}
188	\end{table}
189	
190	\paragraph{Second-order and alternative triggers.}
191	A second-order acceleration indicator $\Delta^2_t$ (Eq.~\ref{eq:second_order}) does not discriminate between sub- and super-critical regimes: all trajectories exhibit negative $\Delta^2_t$ in late generations regardless of mixing ratio.
192	A level-based trigger keyed to baseline SLV could detect the transient dip in Type~II trajectories, but would not activate under Type~III where SLV exceeds baseline at all generations.
193	Finer resolution between 0.25 and 0.3 would narrow the $r_{\text{crit}}$ bound but would not change the practical recommendation to set $r$ above 0.3.
194	For practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "1b8834ad-9fa9-4c51-83c1-39d8c5046f8e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
      "content": "\n\\subsection{Experimental Setup}\n\\label{subsec:setup}\n\nWe use the publicly released final Pythia-410M-deduped checkpoint \\citep{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.\nStarting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.\nAt each generation we compute the spectral indicators from \\S\\ref{subsec:spectral_metrics} on 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.\nThese three metrics (language modeling capability, natural language understanding, and generation diversity) cover the primary evaluation dimensions accessible to a 410M-parameter model.\n\nFor the mixing comparison (\\S\\ref{subsec:phase1}), we evaluate three strategies:\n(1)~\\textbf{pure collapse} ($r_t{=}0$),\n(2)~\\textbf{fixed mix} ($r_t{=}0.50$), and\n(3)~\\textbf{adaptive} ($k{=}10$, Eq.~\\ref{eq:controller}).\nTo construct the collapse phase diagram (\\S\\ref{subsec:phase_diagram_exp}), we additionally evaluate fixed mixing at $r \\in \\{0.2, 0.25, 0.3\\}$.\n\n\\subsection{Spectral Collapse Characterization}\n\\label{subsec:phase0}\n\nTable~\\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}rrrrrrc@{}}\n\\toprule\nGen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\\n\\midrule\n0  & 417.55 & 2366.68 &  9.55 & .413 & .738 & 1942.8 \\\\\n2  & \\textbf{496.17} & \\textbf{2467.98} & 13.56 & .380 & .505 &  718.7 \\\\\n5  & 479.77 & 2365.99 & 24.50 & .341 & .412 &  749.2 \\\\\n7  & 464.10 & 2293.24 & 37.82 & .319 & .375 &  788.4 \\\\\n10 & 438.05 & 2181.35 & 70.99 & .296 & .324 &  874.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spectral and downstream metrics at selected generations (Pythia-410M, mean of three seeds 42, 43, 44; sample s.d.\\ at Gen~10: $r_{\\text{eff}}$ $\\pm$4.8, SLV $\\pm$28.3, PPL $\\pm$5.6, HeSw $\\pm$.006, D-4 $\\pm$.15). Bold marks the spectral peak.}\n\\label{tab:phase0}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/spectral_trajectory.pdf}\n\\caption{SLV across 10 recursive generations of Pythia-410M (solid: $r{=}0$, 3-seed mean; dashed: $r{=}0.5$, 2-seed mean) under pure-synthetic training and 50\\% real-data mixing. Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2468), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 11\\% from peak to 2181). Under 50\\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\\% above baseline and 104 points above the pure-collapse peak.}\n\\label{fig:spectral_trajectory}\n\\end{figure}\n\n\\paragraph{Phase I: Spectral Decompression (Gen~0--2).}\nIn the first two generations, $r_{\\text{eff}}$ rises from 417.55 to 496.2 (+18.8\\%) and SLV increases from 2366.7 to 2468.0 (+4.3\\%), while $\\sigma_1$ drops sharply from 1942.8 to 718.7 as spectral mass redistributes from the dominant direction to smaller components.\nThe consistency of the peak position (Gen~2 across all three seeds) and its coincidence with the qualitative reversal of $\\sigma_1$ dynamics (from declining to rising) suggest that the phase boundary reflects a structural transition rather than a statistical artifact.\nCrucially, this decompression does not indicate improved model quality: HellaSwag drops from 0.413 to 0.380 ($-$8.0\\%) and distinct-4 falls from 0.738 to 0.505 ($-$31.6\\%) during the same interval.\nHellaSwag already declines 5.4\\% from Gen~0 to Gen~1, precisely when spectral indicators are still rising; this asymmetry suggests that decompression captures distributional broadening rather than preservation of task-supporting representations.\nSLV's value lies not in temporal precedence but in computational efficiency ($<$1\\,s vs.\\ ${\\sim}$70\\,min for benchmarks) and cross-seed robustness (CV $< 1.3\\%$).\n\n\\paragraph{Phase II: Collapse Onset (Gen~2--4).}\nBoth $r_{\\text{eff}}$ and SLV reverse after Gen~2 ($r_{\\text{eff}}$: 496.2$\\to$493.6, SLV: 2468$\\to$2440), and this reversal marks the transition from decompression to collapse while perplexity continues its monotonic rise.\n\n\\paragraph{Phase III: Accelerating Collapse (Gen~4--10).}\nSpectral contraction accelerates: the mean per-generation $r_{\\text{eff}}$ decline in Phase~III is $1.78 \\pm 0.22$\\%/gen (mean $\\pm$ s.d.\\ across three seeds).\nBy Gen~10, $r_{\\text{eff}}$ falls to 438.1 ($-$11.7\\% from peak), SLV drops to 2181.4 ($-$7.8\\% from baseline), perplexity reaches 71.0 ($+$643\\%), and $\\sigma_1$ reverses its earlier decline, reaching 874.6 at Gen~10, a sign of renewed spectral concentration (Figure~\\ref{fig:spectral_trajectory}).\n\n\\paragraph{Cross-Scale Pilot.}\nRepeating the protocol on Pythia-1B (Gen~0--3) confirms the same decompression-onset structure ($r_{\\text{eff}}$ peak at Gen~2, SLV peak one generation earlier). SLV's low cost and monotonic post-peak decline make it well-suited as an automated collapse indicator.\nIn our setup, SLV computation (1{,}000-sample forward pass plus SVD of the $n {\\times} d$ embedding matrix) takes ${<}\\,1$~second on a single GPU, whereas HellaSwag 0-shot evaluation requires ${\\sim}70$~minutes end-to-end under identical hardware.\n\n\\subsection{Adaptive Mixing Comparison}\n\\label{subsec:phase1}\n\nUnder pure synthetic training (\\S\\ref{subsec:phase0}), SLV peaks at Gen~2 (2468) and declines monotonically; with 50\\% mixing, SLV rises to 2572 at Gen~10 (104 points above the pure-collapse peak), with only a negligible Gen~1 dip ($\\Delta_1 \\approx 0.0003$, well below $\\tau$).\n\nThe adaptive controller ($k{=}10$) remains silent through all ten generations: $\\max \\Delta_t = 0.0003$ at Gen~1, well below $\\tau{=}0.002$, and $\\Delta_t \\leq 0$ for all $t \\geq 2$.\nRetrospectively computing the controller signal on each fixed-ratio trajectory reveals that even moderate mixing that does not prevent downstream degradation (PPL $+$45\\% at $r{=}0.2$) suffices to suppress the rate-based signal.\nPure collapse produces SLV decline from Gen~3 while $r{=}0.5$ yields sustained growth, bounding $0.2 < r_{\\text{crit}} \\leq 0.5$ (\\S\\ref{subsec:phase_diagram_exp}).\n\nDespite sustained spectral expansion, downstream metrics degrade steadily: perplexity increases 58\\% ($9.55 \\to 15.12$) and distinct-4 falls 79\\% ($.738 \\to .152$) over ten generations, the lowest D-4 of any condition, below even pure collapse ($r{=}0$: 0.324).\nThis reinforces the asymmetry from \\S\\ref{subsec:phase0}: spectral health under mixed training does not guarantee model health, and signal attenuation renders per-generation reactive controllers ineffective precisely when collapse prevention succeeds.\nThis attenuation is inherent to any rate-based indicator~\\citep{scheffer2009ews}; our contribution is quantifying how it creates a continuous degradation of monitoring capability across the sub-critical regime.\n\n\\subsection{Alternative EWS Comparison}\n\\label{subsec:alt_ews}\n\nWe compare SLV against seven alternative collapse indicators from three signal sources: embedding geometry (RankMe, isotropy), attention weights (stable rank, spectral norm), and output distributions (token entropy, raw perplexity, perplexity growth rate).\n\nTable~\\ref{tab:ews_comparison} summarizes the comparison under pure-synthetic training ($r{=}0$).\nTwo indicators share SLV's decompression-then-collapse trajectory: RankMe~\\citep{rankme2023}, the exponential of the normalized singular-value entropy, peaks at Gen~2 and declines monotonically thereafter, though with 2.5$\\times$ lower signal-to-noise ratio (4.7\\% relative change vs.\\ 11.8\\% for SLV).\nWeight-level and output-level indicators (stable rank, spectral norm, token entropy) change monotonically from Gen~0 with no decompression phase; they cannot distinguish collapse onset from the initial fine-tuning transient.\nIsotropy is the least reliable indicator: random sampling without a fixed seed introduces approximately 5\\% variance, and it exhibits six monotonicity violations across ten generations, with direction reversals at Gen~4+ that produce a misleading recovery signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}llcrrc@{}}\n\\toprule\nIndicator & Source & Peak & Mono? & Rel $\\Delta$ & Rev.? \\\\\n\\midrule\nSLV         & emb-SVD   & Gen 2 & \\checkmark & 11.8\\% & \\checkmark \\\\\nRankMe      & emb-SVD   & Gen 2 & \\checkmark &  4.7\\% & \\checkmark \\\\\nToken ent.  & logit     & ---   & \\checkmark &  9.6\\% & \\checkmark \\\\\nStable rank & attn wt.  & ---   & \\checkmark & 14.0\\% & \\checkmark \\\\\nSpec.\\ norm & attn wt.  & ---   & \\checkmark &  8.0\\% & \\checkmark \\\\\nIsotropy    & emb       & ---   & $\\times$\\,(6) & 75\\%   & \\checkmark \\\\\nRaw PPL     & eval      & ---   & \\checkmark & 643\\%  & $\\times$ \\\\\nPPL growth  & ppl       & ---   & $\\sim$\\,(1) &  ---   & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Alternative early warning indicators under pure-synthetic training ($r{=}0$, Pythia-410M, 10 gen). \\textbf{Peak}: generation at which the indicator reverses (--- = monotonic from Gen~0). \\textbf{Mono?}: post-peak monotonicity (\\checkmark\\ = yes; number = violations). \\textbf{Rel $\\Delta$}: $|v_{10} - v_0|/|v_0|$, magnitude of total relative change Gen~0--10. \\textbf{Rev.?}: direction reversal under $r{=}0.5$ mixing (\\checkmark\\ = reversed).}\n\\label{tab:ews_comparison}\n\\end{table}\n\nThe final column of Table~\\ref{tab:ews_comparison} reveals that seven of eight indicators reverse direction under 50\\% real-data mixing; the exception is raw perplexity, which continues to increase (albeit more slowly), tracking cumulative degradation rather than directional spectral change.\nThis near-universality confirms that signal attenuation (\\S\\ref{subsec:controller}) is not specific to SLV: any per-generation reactive controller based on spectral or rate-based indicators will fall silent when mixing exceeds $r_{\\text{crit}}$.\nAmong embedding-level metrics, SLV offers the highest signal-to-noise ratio (2.5$\\times$ that of RankMe) and, together with RankMe, is the only indicator that exhibits a decompression baseline to distinguish collapse onset from training transients.\nSLV is the only indicator that combines decompression-phase sensitivity, post-peak monotonicity, and sub-second computation cost; it shares a metric foundation with SIGMA's $\\log\\det G$ ($= 2 \\times \\text{SLV}$; \\S\\ref{sec:related}).\n\n\\subsection{Collapse Phase Diagram}\n\\label{subsec:phase_diagram_exp}\n\nWe now map SLV trajectories across mixing ratios to construct the collapse phase diagram defined in \\S\\ref{subsec:phase_diagram}.\nFigure~\\ref{fig:phase_diagram} plots SLV across 10 recursive generations for five mixing ratios; three qualitatively distinct trajectory types emerge:\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/phase_diagram.pdf}\n\\caption{SLV trajectories across mixing ratios (Pythia-410M; $r{=}0$ and $r{=}0.25$: 3-seed mean; $r{=}0.3$: 3-seed mean; $r{=}0.2$: single seed; $r{=}0.5$: 2-seed mean). Type~I ($r{=}0$): decompression then monotonic collapse. Type~II ($r{=}0.2$, $r{=}0.25$): transient dip followed by recovery. Type~III ($r{=}0.3$, $r{=}0.5$): monotonic expansion from Gen~2 onward. The shaded band marks the critical threshold $r_{\\text{crit}} \\in (0.25, 0.3]$. The dashed horizontal line indicates the Gen~0 baseline.}\n\\label{fig:phase_diagram}\n\\end{figure}\n\n\\paragraph{Type~I: Pure Collapse ($r{=}0$).}\nSLV exhibits large decompression ($+$97 points at Gen~1, peaking at Gen~2) followed by accelerating contraction (\\S\\ref{subsec:phase0}).\n\n\\paragraph{Type~II: Near-critical Mixing ($r{=}0.2$).}\nTwenty percent real data suppresses the SLV decompression phase: SLV rises only 0.78 points from Gen~0 to Gen~1 (vs.\\ $+$98 under $r{=}0$), dips at Gen~2 ($2367.5 \\to 2358.3$, $-9.2$).\nRecovery begins at Gen~3, with per-generation gains accelerating from $+4.2$ to $+30.9$ (Gen~6) before moderating, reaching 2479.7 at Gen~10 ($+4.8\\%$ above baseline).\nBecause $\\widetilde{S}_2 = 2362.7 < \\widetilde{S}_1 = 2367.1$ (EMA-smoothed SLV; \\S\\ref{subsec:controller}), the non-decreasing condition is violated and $r{=}0.2$ formally lies below $r_{\\text{crit}}$.\nThe trajectory is consistent with the transitional regime (\\S\\ref{subsec:phase_diagram}): initial contraction followed by sustained recovery over the full 10-generation horizon.\nThe smoothed signal never exceeds the controller threshold ($\\max \\Delta_t = 0.0019$ at Gen~2, below $\\tau = 0.002$), so as little as 20\\% real data silences the controller entirely.\nThe effective rank still rises at Gen~2 ($476.7 \\to 481.6$) while the EMA-smoothed SLV registers a net decline ($\\widetilde{S}_2 < \\widetilde{S}_1$), evidence that smoothed SLV detects spectral contraction earlier at this mixing ratio.\nEffective rank cannot distinguish Type~II from Type~III trajectories---both show monotonic expansion for $r \\geq 0.2$---whereas SLV's transient dip at $r{=}0.2$ uniquely identifies the transitional regime, underscoring SLV's finer discriminative power.\n\nAt $r{=}0.25$, the full 10-generation trajectory follows the same Type~II pattern: SLV dips from Gen~0 to Gen~1 ($2366.7 \\to 2362.1$, $-4.6$; seed~42, representative trajectory), reaches a minimum at Gen~2 ($2363.1$), then rises monotonically through Gen~10 (three-seed mean $2488.1$, $+5.1\\%$ above baseline).\nThe EMA-smoothed sequence confirms the sub-critical classification: $\\widetilde{S}_1 = 2364.4$, $\\widetilde{S}_2 = 2363.8$, satisfying $\\widetilde{S}_2 < \\widetilde{S}_1$ and violating the non-decreasing condition.\nController silence is more pronounced than at $r{=}0.2$: $\\max \\Delta_t = 0.00028 < \\tau = 0.002$, a $6.7\\times$ weaker signal than the $r{=}0.2$ maximum ($0.0019$), consistent with further signal attenuation as the real-data fraction increases.\nThe amplitude of the EMA violation at $r{=}0.25$ varies substantially across seeds ($\\widetilde{S}_2 - \\widetilde{S}_1 = -0.6$, $-1.7$, $-0.9$), consistent with the elevated fluctuations expected near a phase boundary, while trajectories at $r{=}0$ and $r \\geq 0.3$ show low cross-seed variance ($< 0.5\\%$).\n\n\\paragraph{Type~III: Super-critical Mixing ($r \\geq 0.3$).}\nSLV rises monotonically from Gen~2 onward, reaching 2572 at Gen~10 ($+$8.7\\% above baseline), consistent with $r{=}0.5 \\geq r_{\\text{crit}}$ (\\S\\ref{subsec:phase1}).\nPer-generation gains remain positive through all post-transient generations ($\\Delta_t \\in [+11, +35]$ for $t \\geq 2$; mean $+23.0$), sustaining expansion with no reversal toward the contraction trajectory of Type~I within the observed horizon.\n\nThese three types partition the mixing-ratio axis into sub-critical ($r < r_{\\text{crit}}$), transitional, and stable ($r \\geq r_{\\text{crit}}$) zones.\nType classification is based solely on spectral trajectory shape; downstream metrics such as D-4 may diverge, as demonstrated by the non-monotonic D-4 pattern across mixing ratios (Table~\\ref{tab:phase_summary}).\nAt $r{=}0.3$, SLV expands monotonically from Gen~2 to 2508.2 at Gen~10 ($+$6.0\\% above baseline), with sustained positive growth across all eight post-transient generations.\nThis confirms $r{=}0.3 \\geq r_{\\text{crit}}$ over the full 10-generation horizon, tightening the bound to $0.25 < r_{\\text{crit}} \\leq 0.3$.\nAcross three seeds, one individual EMA-smoothed trajectory shows a transient violation of 0.83~points at Gen~2; the remaining two satisfy non-decreasing from $t \\geq 2$. The cross-seed mean trajectory is non-decreasing at all post-transient generations (Gen~10 SLV CV $= 0.12\\%$), confirming the Type~III classification.\nThe single-seed transient is consistent with the continuous crossover interpretation: near the phase boundary, individual realizations may briefly exhibit sub-critical behavior even when the mean trajectory is stable.\nThe critical threshold is robust to the smoothing parameter: recomputing the EMA-smoothed SLV for $\\alpha \\in \\{0.3, 0.5, 0.7\\}$ yields $r_{\\text{crit}} \\in (0.25, 0.3]$ in all cases, with the non-decreasing condition violated at Gen~2 for $r \\leq 0.25$ and satisfied on the cross-seed mean for $r \\geq 0.3$ regardless of $\\alpha$.\n\nThe largest single-generation SLV drop in the first two generations shrinks with $r$: $-9.2$ at $r{=}0.2$ (Gen~1$\\to$2), $-4.6$ at $r{=}0.25$ (Gen~0$\\to$1; seed~42), and $-0.6$ at $r{=}0.3$ (Gen~0$\\to$1), consistent with a continuous crossover rather than a sharp boundary.\nThe Type~II trajectory clarifies what $r_{\\text{crit}}$ marks in practice: not a boundary between collapse and stability in final outcome, but a transition in trajectory shape.\nBelow $r_{\\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion through Gen~10 once the transient passes.\n\n\\paragraph{Output Diversity Divergence.}\nAt $r{=}0.2$, D-4 exhibits a V-shaped recovery (0.438 at Gen~5 $\\to$ 0.520 at Gen~10), but this pattern does not generalize: at $r{=}0.25$, D-4 declines monotonically to 0.342 despite comparable SLV recovery, indicating that spectral expansion does not guarantee diversity restoration.\nMore broadly, D-4 exhibits a non-monotonic relationship with $r$: it peaks at $r{=}0.2$ (.520), exceeds the pure-collapse baseline (.324) at $r \\leq 0.25$ but drops below it at $r \\geq 0.3$, reaching .152 at $r{=}0.5$, the lowest across all conditions (Table~\\ref{tab:phase_summary}).\nThis pattern is consistent with increasing real-data anchoring: at high $r$, the model converges toward the fixed real-data distribution, producing coherent but stylistically homogeneous text.\nThis divergence between spectral health (monotonically improving with $r$) and n-gram diversity underscores that SLV and D-4 capture orthogonal aspects of model behavior.\nD-4 exhibits substantially higher cross-seed variance than spectral metrics: at $r{=}0$ (s.d.\\ $= 0.15$ vs.\\ SLV s.d.\\ $= 28$, a ${>}30\\times$ lower coefficient of variation for SLV) and $r{=}0.3$ (s.d.\\ $= 0.155$ vs.\\ SLV s.d.\\ $= 2.9$; Table~\\ref{tab:phase_summary}), suggesting that n-gram diversity reflects stochastic generation choices rather than the deterministic geometric structure captured by SLV.\nThis pattern generalizes across mixing ratios: at $r{=}0.25$, SLV cross-seed CV is 0.12\\% versus 3.9\\% for D-4, confirming that spectral geometry captures a deterministic structural property largely independent of stochastic training noise.\n\nTable~\\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}clrrrrrc@{}}\n\\toprule\n$r$ & Type & SLV & $r_{\\text{eff}}$ & PPL & D-4 & $\\max\\Delta_t$ & Gen. \\\\\n\\midrule\n0    & I   & 2181.4 & 438.1 & 71.0\\phantom{0} & .324 & ---   & 10 \\\\\n0.20 & II  & 2479.7 & 511.3 & 13.83 & .520 & .0019 & 10 \\\\\n0.25 & II  & 2488.1 & 513.8 & 13.41 & .342 & .0003 & 10 \\\\\n0.30 & III & 2508.2 & 521.1 & 13.35 & .295 & 0     & 10 \\\\\n0.50 & III & 2571.7 & 553.5 & 15.12 & .152 & 0     & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Final-generation spectral and downstream metrics across mixing ratios (all runs to Gen~10). $\\max\\Delta_t$ computed for $t \\geq 2$, excluding the initial fine-tuning transient. Type classification follows \\S\\ref{subsec:phase_diagram}. $r{=}0$ reports the mean of three seeds (42, 43, 44); $r{=}0.3$ the mean of three seeds (42, 43, 44); $r{=}0.2$ reports a single seed; $r{=}0.5$ the mean of two seeds (42, 43); $r{=}0.25$ the mean of three seeds (42, 43, 44). D-4 exhibits high cross-seed variance at $r{=}0$ (s.d.\\ $= 0.15$) and $r{=}0.3$ (s.d.\\ $= 0.155$).}\n\\label{tab:phase_summary}\n\\end{table}\n\n\\paragraph{Second-order and alternative triggers.}\nA second-order acceleration indicator $\\Delta^2_t$ (Eq.~\\ref{eq:second_order}) does not discriminate between sub- and super-critical regimes: all trajectories exhibit negative $\\Delta^2_t$ in late generations regardless of mixing ratio.\nA level-based trigger keyed to baseline SLV could detect the transient dip in Type~II trajectories, but would not activate under Type~III where SLV exceeds baseline at all generations.\nFiner resolution between 0.25 and 0.3 would narrow the $r_{\\text{crit}}$ bound but would not change the practical recommendation to set $r$ above 0.3.\nFor practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
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
Now I'll make both edits.

For the abstract: add a TODO comment after the last sentence (line 7) but before the end of the abstract environment. The abstract ends at line 7 - I need to check if there's a `\end{abstract}` or similar. Let me look at the main.tex to understand the structure, but actually the abstract.tex file just contains the text content (lines 1-7), and it's likely `\input`ed inside an abstract environment in main.tex. So I'll add the comment after line 7.

For experiments.tex: add a commented-out §3.6 after the last line (line 194).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "3de120ee-dcfb-423d-b3a4-c75da2b50b08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uETKC6UnG6u3U6x9CZpFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8114,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8114
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

### Assistant

_source line 10_

Now I'll make both edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "28948ef7-df94-4758-ba31-efec3f93bba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uETKC6UnG6u3U6x9CZpFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8114,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8114
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_017p9xvYFozyGXnKX6xB74n3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex",
  "old_string": "Nevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.",
  "new_string": "Nevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.\n% TODO: Add cross-architecture confirmation sentence once exp_020 completes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "70dac85d-fcf1-45a5-85fc-00130c44143e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uETKC6UnG6u3U6x9CZpFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8114,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8114
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

_source line 12 · 2026-05-23T10:11:29.521Z_

<details><summary>↩ Tool result · `toolu_017p9xvYFozyGXnKX6xB74n3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "d7409df1-474a-49a3-af51-d5a48b614848",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex",
    "oldString": "Nevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.",
    "newString": "Nevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.\n% TODO: Add cross-architecture confirmation sentence once exp_020 completes.",
    "originalFile": "During the early stages of recursive synthetic training, spectral indicators of the embedding space suggest the model is improving---even as downstream performance is already degrading.\nWe reveal the source of this misleading signal by tracking spectral properties of the embedding matrix across 10 recursive generations of Pythia-410M, with pilot validation on Pythia-1B.\nThe result is a reproducible three-phase pattern, consistent across three random seeds (SLV CV $< 1.3\\%$ at all generations): spectral decompression (generations 0--2), where effective rank and SLV increase while HellaSwag accuracy drops 3.3 percentage points (8.0\\% relative); collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10).\nOf eight indicators evaluated, SLV is the most effective collapse indicator: it requires only a single forward pass (${<}\\,1$ second on one GPU, compared to ${\\sim}70$ minutes for benchmark evaluation), captures volume changes across all spectral directions, and declines monotonically after the decompression peak.\nBy varying the real-data mixing ratio across five levels, we construct a collapse phase diagram that localizes the critical mixing ratio $r_{\\text{crit}}$ to the interval $(0.25, 0.3]$ across three random seeds, separating monotonic spectral expansion from a transitional regime with initial contraction followed by recovery.\nA proportional controller demonstrates an inherent signal attenuation: moderate real-data mixing prevents the spectral contraction that would activate the controller, so reactive spectral feedback becomes ineffective precisely when prevention succeeds.\nNevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 3,
        "newStart": 5,
        "newLines": 4,
        "lines": [
          " By varying the real-data mixing ratio across five levels, we construct a collapse phase diagram that localizes the critical mixing ratio $r_{\\text{crit}}$ to the interval $(0.25, 0.3]$ across three random seeds, separating monotonic spectral expansion from a transitional regime with initial contraction followed by recovery.",
          " A proportional controller demonstrates an inherent signal attenuation: moderate real-data mixing prevents the spectral contraction that would activate the controller, so reactive spectral feedback becomes ineffective precisely when prevention succeeds.",
          " Nevertheless, the empirically calibrated $r_{\\text{crit}}$ provides a practical workaround: setting the mixing ratio above this threshold prevents collapse without real-time monitoring, reducing the problem to a one-time offline calibration requiring only forward-pass spectral checks.",
          "+% TODO: Add cross-architecture confirmation sentence once exp_020 completes."
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

<details open><summary>🔧 Tool call — Edit · `toolu_017PySn9C1ysihrxr62dyzCi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "For practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.",
  "new_string": "For practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.\n\n% ==============================================================================\n% §3.6 Cross-Architecture Confirmation [COMMENTED OUT — uncomment after exp_020]\n% ==============================================================================\n%\n% \\subsection{Cross-Architecture Confirmation}\n% \\label{subsec:cross_arch}\n%\n% To provide preliminary cross-architecture evidence, we repeat the pure-synthetic\n% recursive pipeline ($r{=}0$, seed~42) on GPT-2-medium (24 layers, ${\\sim}$355M\n% parameters), a decoder-only transformer with a different pretraining corpus and\n% tokenizer than Pythia-410M.\n%\n% \\paragraph{Hypothesis.}\n% If the three-phase spectral trajectory (decompression, onset, accelerating\n% collapse) reflects a general property of recursive synthetic fine-tuning rather\n% than an architecture-specific artifact of Pythia, GPT-2-medium should exhibit a\n% qualitatively similar SLV trajectory under the same protocol.\n%\n% \\paragraph{Setup.}\n% We fine-tune GPT-2-medium (24 transformer layers, 1024-dimensional embeddings,\n% ${\\sim}$355M parameters) on a 50K-subset of OpenWebText using the same\n% hyperparameters and recursive pipeline as \\S\\ref{subsec:setup}, for\n% \\texttt{TBD} recursive generations under $r{=}0$ with seed~42.\n%\n% \\paragraph{Results.}\n% % TODO: Fill in actual metrics from exp_020\n% Table~\\ref{tab:cross_arch} reports spectral and downstream metrics across\n% generations for GPT-2-medium.\n%\n% % TODO: Uncomment and populate table\n% % \\begin{table}[t]\n% % \\centering\n% % \\small\n% % \\setlength{\\tabcolsep}{4pt}\n% % \\begin{tabular}{@{}rrrrrrc@{}}\n% % \\toprule\n% % Gen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\\n% % \\midrule\n% % 0  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % 2  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % 5  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % 10 & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % \\bottomrule\n% % \\end{tabular}\n% % \\caption{Spectral and downstream metrics for GPT-2-medium ($r{=}0$, seed~42).}\n% % \\label{tab:cross_arch}\n% % \\end{table}\n%\n% % TODO: Describe whether three-phase pattern is reproduced\n% % TODO: Report SLV peak generation and magnitude\n% % TODO: Compare decompression amplitude with Pythia-410M\n%\n% \\paragraph{Discussion.}\n% % TODO: Fill in after exp_020 results\n% These results provide initial confirmation on a second architecture that the\n% three-phase spectral trajectory is not specific to the Pythia model family.\n% The qualitative agreement between Pythia-410M and GPT-2-medium suggests that\n% spectral decompression followed by collapse onset is a recurring pattern in\n% recursive synthetic fine-tuning, though further architectures and scales would\n% be needed to establish broader generality.\n% =============================================================================="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "6d142477-da17-4047-b7fe-baad6fe105ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uETKC6UnG6u3U6x9CZpFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8114,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8114
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

_source line 14 · 2026-05-23T10:11:47.919Z_

<details><summary>↩ Tool result · `toolu_017PySn9C1ysihrxr62dyzCi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "ce1d2c33-de39-4100-a939-5435c99200ae",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "oldString": "For practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.",
    "newString": "For practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.\n\n% ==============================================================================\n% §3.6 Cross-Architecture Confirmation [COMMENTED OUT — uncomment after exp_020]\n% ==============================================================================\n%\n% \\subsection{Cross-Architecture Confirmation}\n% \\label{subsec:cross_arch}\n%\n% To provide preliminary cross-architecture evidence, we repeat the pure-synthetic\n% recursive pipeline ($r{=}0$, seed~42) on GPT-2-medium (24 layers, ${\\sim}$355M\n% parameters), a decoder-only transformer with a different pretraining corpus and\n% tokenizer than Pythia-410M.\n%\n% \\paragraph{Hypothesis.}\n% If the three-phase spectral trajectory (decompression, onset, accelerating\n% collapse) reflects a general property of recursive synthetic fine-tuning rather\n% than an architecture-specific artifact of Pythia, GPT-2-medium should exhibit a\n% qualitatively similar SLV trajectory under the same protocol.\n%\n% \\paragraph{Setup.}\n% We fine-tune GPT-2-medium (24 transformer layers, 1024-dimensional embeddings,\n% ${\\sim}$355M parameters) on a 50K-subset of OpenWebText using the same\n% hyperparameters and recursive pipeline as \\S\\ref{subsec:setup}, for\n% \\texttt{TBD} recursive generations under $r{=}0$ with seed~42.\n%\n% \\paragraph{Results.}\n% % TODO: Fill in actual metrics from exp_020\n% Table~\\ref{tab:cross_arch} reports spectral and downstream metrics across\n% generations for GPT-2-medium.\n%\n% % TODO: Uncomment and populate table\n% % \\begin{table}[t]\n% % \\centering\n% % \\small\n% % \\setlength{\\tabcolsep}{4pt}\n% % \\begin{tabular}{@{}rrrrrrc@{}}\n% % \\toprule\n% % Gen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\\n% % \\midrule\n% % 0  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % 2  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % 5  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % 10 & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\\n% % \\bottomrule\n% % \\end{tabular}\n% % \\caption{Spectral and downstream metrics for GPT-2-medium ($r{=}0$, seed~42).}\n% % \\label{tab:cross_arch}\n% % \\end{table}\n%\n% % TODO: Describe whether three-phase pattern is reproduced\n% % TODO: Report SLV peak generation and magnitude\n% % TODO: Compare decompression amplitude with Pythia-410M\n%\n% \\paragraph{Discussion.}\n% % TODO: Fill in after exp_020 results\n% These results provide initial confirmation on a second architecture that the\n% three-phase spectral trajectory is not specific to the Pythia model family.\n% The qualitative agreement between Pythia-410M and GPT-2-medium suggests that\n% spectral decompression followed by collapse onset is a recurring pattern in\n% recursive synthetic fine-tuning, though further architectures and scales would\n% be needed to establish broader generality.\n% ==============================================================================",
    "originalFile": "\n\\subsection{Experimental Setup}\n\\label{subsec:setup}\n\nWe use the publicly released final Pythia-410M-deduped checkpoint \\citep{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.\nStarting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.\nAt each generation we compute the spectral indicators from \\S\\ref{subsec:spectral_metrics} on 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.\nThese three metrics (language modeling capability, natural language understanding, and generation diversity) cover the primary evaluation dimensions accessible to a 410M-parameter model.\n\nFor the mixing comparison (\\S\\ref{subsec:phase1}), we evaluate three strategies:\n(1)~\\textbf{pure collapse} ($r_t{=}0$),\n(2)~\\textbf{fixed mix} ($r_t{=}0.50$), and\n(3)~\\textbf{adaptive} ($k{=}10$, Eq.~\\ref{eq:controller}).\nTo construct the collapse phase diagram (\\S\\ref{subsec:phase_diagram_exp}), we additionally evaluate fixed mixing at $r \\in \\{0.2, 0.25, 0.3\\}$.\n\n\\subsection{Spectral Collapse Characterization}\n\\label{subsec:phase0}\n\nTable~\\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}rrrrrrc@{}}\n\\toprule\nGen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\\n\\midrule\n0  & 417.55 & 2366.68 &  9.55 & .413 & .738 & 1942.8 \\\\\n2  & \\textbf{496.17} & \\textbf{2467.98} & 13.56 & .380 & .505 &  718.7 \\\\\n5  & 479.77 & 2365.99 & 24.50 & .341 & .412 &  749.2 \\\\\n7  & 464.10 & 2293.24 & 37.82 & .319 & .375 &  788.4 \\\\\n10 & 438.05 & 2181.35 & 70.99 & .296 & .324 &  874.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spectral and downstream metrics at selected generations (Pythia-410M, mean of three seeds 42, 43, 44; sample s.d.\\ at Gen~10: $r_{\\text{eff}}$ $\\pm$4.8, SLV $\\pm$28.3, PPL $\\pm$5.6, HeSw $\\pm$.006, D-4 $\\pm$.15). Bold marks the spectral peak.}\n\\label{tab:phase0}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/spectral_trajectory.pdf}\n\\caption{SLV across 10 recursive generations of Pythia-410M (solid: $r{=}0$, 3-seed mean; dashed: $r{=}0.5$, 2-seed mean) under pure-synthetic training and 50\\% real-data mixing. Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2468), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 11\\% from peak to 2181). Under 50\\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\\% above baseline and 104 points above the pure-collapse peak.}\n\\label{fig:spectral_trajectory}\n\\end{figure}\n\n\\paragraph{Phase I: Spectral Decompression (Gen~0--2).}\nIn the first two generations, $r_{\\text{eff}}$ rises from 417.55 to 496.2 (+18.8\\%) and SLV increases from 2366.7 to 2468.0 (+4.3\\%), while $\\sigma_1$ drops sharply from 1942.8 to 718.7 as spectral mass redistributes from the dominant direction to smaller components.\nThe consistency of the peak position (Gen~2 across all three seeds) and its coincidence with the qualitative reversal of $\\sigma_1$ dynamics (from declining to rising) suggest that the phase boundary reflects a structural transition rather than a statistical artifact.\nCrucially, this decompression does not indicate improved model quality: HellaSwag drops from 0.413 to 0.380 ($-$8.0\\%) and distinct-4 falls from 0.738 to 0.505 ($-$31.6\\%) during the same interval.\nHellaSwag already declines 5.4\\% from Gen~0 to Gen~1, precisely when spectral indicators are still rising; this asymmetry suggests that decompression captures distributional broadening rather than preservation of task-supporting representations.\nSLV's value lies not in temporal precedence but in computational efficiency ($<$1\\,s vs.\\ ${\\sim}$70\\,min for benchmarks) and cross-seed robustness (CV $< 1.3\\%$).\n\n\\paragraph{Phase II: Collapse Onset (Gen~2--4).}\nBoth $r_{\\text{eff}}$ and SLV reverse after Gen~2 ($r_{\\text{eff}}$: 496.2$\\to$493.6, SLV: 2468$\\to$2440), and this reversal marks the transition from decompression to collapse while perplexity continues its monotonic rise.\n\n\\paragraph{Phase III: Accelerating Collapse (Gen~4--10).}\nSpectral contraction accelerates: the mean per-generation $r_{\\text{eff}}$ decline in Phase~III is $1.78 \\pm 0.22$\\%/gen (mean $\\pm$ s.d.\\ across three seeds).\nBy Gen~10, $r_{\\text{eff}}$ falls to 438.1 ($-$11.7\\% from peak), SLV drops to 2181.4 ($-$7.8\\% from baseline), perplexity reaches 71.0 ($+$643\\%), and $\\sigma_1$ reverses its earlier decline, reaching 874.6 at Gen~10, a sign of renewed spectral concentration (Figure~\\ref{fig:spectral_trajectory}).\n\n\\paragraph{Cross-Scale Pilot.}\nRepeating the protocol on Pythia-1B (Gen~0--3) confirms the same decompression-onset structure ($r_{\\text{eff}}$ peak at Gen~2, SLV peak one generation earlier). SLV's low cost and monotonic post-peak decline make it well-suited as an automated collapse indicator.\nIn our setup, SLV computation (1{,}000-sample forward pass plus SVD of the $n {\\times} d$ embedding matrix) takes ${<}\\,1$~second on a single GPU, whereas HellaSwag 0-shot evaluation requires ${\\sim}70$~minutes end-to-end under identical hardware.\n\n\\subsection{Adaptive Mixing Comparison}\n\\label{subsec:phase1}\n\nUnder pure synthetic training (\\S\\ref{subsec:phase0}), SLV peaks at Gen~2 (2468) and declines monotonically; with 50\\% mixing, SLV rises to 2572 at Gen~10 (104 points above the pure-collapse peak), with only a negligible Gen~1 dip ($\\Delta_1 \\approx 0.0003$, well below $\\tau$).\n\nThe adaptive controller ($k{=}10$) remains silent through all ten generations: $\\max \\Delta_t = 0.0003$ at Gen~1, well below $\\tau{=}0.002$, and $\\Delta_t \\leq 0$ for all $t \\geq 2$.\nRetrospectively computing the controller signal on each fixed-ratio trajectory reveals that even moderate mixing that does not prevent downstream degradation (PPL $+$45\\% at $r{=}0.2$) suffices to suppress the rate-based signal.\nPure collapse produces SLV decline from Gen~3 while $r{=}0.5$ yields sustained growth, bounding $0.2 < r_{\\text{crit}} \\leq 0.5$ (\\S\\ref{subsec:phase_diagram_exp}).\n\nDespite sustained spectral expansion, downstream metrics degrade steadily: perplexity increases 58\\% ($9.55 \\to 15.12$) and distinct-4 falls 79\\% ($.738 \\to .152$) over ten generations, the lowest D-4 of any condition, below even pure collapse ($r{=}0$: 0.324).\nThis reinforces the asymmetry from \\S\\ref{subsec:phase0}: spectral health under mixed training does not guarantee model health, and signal attenuation renders per-generation reactive controllers ineffective precisely when collapse prevention succeeds.\nThis attenuation is inherent to any rate-based indicator~\\citep{scheffer2009ews}; our contribution is quantifying how it creates a continuous degradation of monitoring capability across the sub-critical regime.\n\n\\subsection{Alternative EWS Comparison}\n\\label{subsec:alt_ews}\n\nWe compare SLV against seven alternative collapse indicators from three signal sources: embedding geometry (RankMe, isotropy), attention weights (stable rank, spectral norm), and output distributions (token entropy, raw perplexity, perplexity growth rate).\n\nTable~\\ref{tab:ews_comparison} summarizes the comparison under pure-synthetic training ($r{=}0$).\nTwo indicators share SLV's decompression-then-collapse trajectory: RankMe~\\citep{rankme2023}, the exponential of the normalized singular-value entropy, peaks at Gen~2 and declines monotonically thereafter, though with 2.5$\\times$ lower signal-to-noise ratio (4.7\\% relative change vs.\\ 11.8\\% for SLV).\nWeight-level and output-level indicators (stable rank, spectral norm, token entropy) change monotonically from Gen~0 with no decompression phase; they cannot distinguish collapse onset from the initial fine-tuning transient.\nIsotropy is the least reliable indicator: random sampling without a fixed seed introduces approximately 5\\% variance, and it exhibits six monotonicity violations across ten generations, with direction reversals at Gen~4+ that produce a misleading recovery signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}llcrrc@{}}\n\\toprule\nIndicator & Source & Peak & Mono? & Rel $\\Delta$ & Rev.? \\\\\n\\midrule\nSLV         & emb-SVD   & Gen 2 & \\checkmark & 11.8\\% & \\checkmark \\\\\nRankMe      & emb-SVD   & Gen 2 & \\checkmark &  4.7\\% & \\checkmark \\\\\nToken ent.  & logit     & ---   & \\checkmark &  9.6\\% & \\checkmark \\\\\nStable rank & attn wt.  & ---   & \\checkmark & 14.0\\% & \\checkmark \\\\\nSpec.\\ norm & attn wt.  & ---   & \\checkmark &  8.0\\% & \\checkmark \\\\\nIsotropy    & emb       & ---   & $\\times$\\,(6) & 75\\%   & \\checkmark \\\\\nRaw PPL     & eval      & ---   & \\checkmark & 643\\%  & $\\times$ \\\\\nPPL growth  & ppl       & ---   & $\\sim$\\,(1) &  ---   & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Alternative early warning indicators under pure-synthetic training ($r{=}0$, Pythia-410M, 10 gen). \\textbf{Peak}: generation at which the indicator reverses (--- = monotonic from Gen~0). \\textbf{Mono?}: post-peak monotonicity (\\checkmark\\ = yes; number = violations). \\textbf{Rel $\\Delta$}: $|v_{10} - v_0|/|v_0|$, magnitude of total relative change Gen~0--10. \\textbf{Rev.?}: direction reversal under $r{=}0.5$ mixing (\\checkmark\\ = reversed).}\n\\label{tab:ews_comparison}\n\\end{table}\n\nThe final column of Table~\\ref{tab:ews_comparison} reveals that seven of eight indicators reverse direction under 50\\% real-data mixing; the exception is raw perplexity, which continues to increase (albeit more slowly), tracking cumulative degradation rather than directional spectral change.\nThis near-universality confirms that signal attenuation (\\S\\ref{subsec:controller}) is not specific to SLV: any per-generation reactive controller based on spectral or rate-based indicators will fall silent when mixing exceeds $r_{\\text{crit}}$.\nAmong embedding-level metrics, SLV offers the highest signal-to-noise ratio (2.5$\\times$ that of RankMe) and, together with RankMe, is the only indicator that exhibits a decompression baseline to distinguish collapse onset from training transients.\nSLV is the only indicator that combines decompression-phase sensitivity, post-peak monotonicity, and sub-second computation cost; it shares a metric foundation with SIGMA's $\\log\\det G$ ($= 2 \\times \\text{SLV}$; \\S\\ref{sec:related}).\n\n\\subsection{Collapse Phase Diagram}\n\\label{subsec:phase_diagram_exp}\n\nWe now map SLV trajectories across mixing ratios to construct the collapse phase diagram defined in \\S\\ref{subsec:phase_diagram}.\nFigure~\\ref{fig:phase_diagram} plots SLV across 10 recursive generations for five mixing ratios; three qualitatively distinct trajectory types emerge:\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/phase_diagram.pdf}\n\\caption{SLV trajectories across mixing ratios (Pythia-410M; $r{=}0$ and $r{=}0.25$: 3-seed mean; $r{=}0.3$: 3-seed mean; $r{=}0.2$: single seed; $r{=}0.5$: 2-seed mean). Type~I ($r{=}0$): decompression then monotonic collapse. Type~II ($r{=}0.2$, $r{=}0.25$): transient dip followed by recovery. Type~III ($r{=}0.3$, $r{=}0.5$): monotonic expansion from Gen~2 onward. The shaded band marks the critical threshold $r_{\\text{crit}} \\in (0.25, 0.3]$. The dashed horizontal line indicates the Gen~0 baseline.}\n\\label{fig:phase_diagram}\n\\end{figure}\n\n\\paragraph{Type~I: Pure Collapse ($r{=}0$).}\nSLV exhibits large decompression ($+$97 points at Gen~1, peaking at Gen~2) followed by accelerating contraction (\\S\\ref{subsec:phase0}).\n\n\\paragraph{Type~II: Near-critical Mixing ($r{=}0.2$).}\nTwenty percent real data suppresses the SLV decompression phase: SLV rises only 0.78 points from Gen~0 to Gen~1 (vs.\\ $+$98 under $r{=}0$), dips at Gen~2 ($2367.5 \\to 2358.3$, $-9.2$).\nRecovery begins at Gen~3, with per-generation gains accelerating from $+4.2$ to $+30.9$ (Gen~6) before moderating, reaching 2479.7 at Gen~10 ($+4.8\\%$ above baseline).\nBecause $\\widetilde{S}_2 = 2362.7 < \\widetilde{S}_1 = 2367.1$ (EMA-smoothed SLV; \\S\\ref{subsec:controller}), the non-decreasing condition is violated and $r{=}0.2$ formally lies below $r_{\\text{crit}}$.\nThe trajectory is consistent with the transitional regime (\\S\\ref{subsec:phase_diagram}): initial contraction followed by sustained recovery over the full 10-generation horizon.\nThe smoothed signal never exceeds the controller threshold ($\\max \\Delta_t = 0.0019$ at Gen~2, below $\\tau = 0.002$), so as little as 20\\% real data silences the controller entirely.\nThe effective rank still rises at Gen~2 ($476.7 \\to 481.6$) while the EMA-smoothed SLV registers a net decline ($\\widetilde{S}_2 < \\widetilde{S}_1$), evidence that smoothed SLV detects spectral contraction earlier at this mixing ratio.\nEffective rank cannot distinguish Type~II from Type~III trajectories---both show monotonic expansion for $r \\geq 0.2$---whereas SLV's transient dip at $r{=}0.2$ uniquely identifies the transitional regime, underscoring SLV's finer discriminative power.\n\nAt $r{=}0.25$, the full 10-generation trajectory follows the same Type~II pattern: SLV dips from Gen~0 to Gen~1 ($2366.7 \\to 2362.1$, $-4.6$; seed~42, representative trajectory), reaches a minimum at Gen~2 ($2363.1$), then rises monotonically through Gen~10 (three-seed mean $2488.1$, $+5.1\\%$ above baseline).\nThe EMA-smoothed sequence confirms the sub-critical classification: $\\widetilde{S}_1 = 2364.4$, $\\widetilde{S}_2 = 2363.8$, satisfying $\\widetilde{S}_2 < \\widetilde{S}_1$ and violating the non-decreasing condition.\nController silence is more pronounced than at $r{=}0.2$: $\\max \\Delta_t = 0.00028 < \\tau = 0.002$, a $6.7\\times$ weaker signal than the $r{=}0.2$ maximum ($0.0019$), consistent with further signal attenuation as the real-data fraction increases.\nThe amplitude of the EMA violation at $r{=}0.25$ varies substantially across seeds ($\\widetilde{S}_2 - \\widetilde{S}_1 = -0.6$, $-1.7$, $-0.9$), consistent with the elevated fluctuations expected near a phase boundary, while trajectories at $r{=}0$ and $r \\geq 0.3$ show low cross-seed variance ($< 0.5\\%$).\n\n\\paragraph{Type~III: Super-critical Mixing ($r \\geq 0.3$).}\nSLV rises monotonically from Gen~2 onward, reaching 2572 at Gen~10 ($+$8.7\\% above baseline), consistent with $r{=}0.5 \\geq r_{\\text{crit}}$ (\\S\\ref{subsec:phase1}).\nPer-generation gains remain positive through all post-transient generations ($\\Delta_t \\in [+11, +35]$ for $t \\geq 2$; mean $+23.0$), sustaining expansion with no reversal toward the contraction trajectory of Type~I within the observed horizon.\n\nThese three types partition the mixing-ratio axis into sub-critical ($r < r_{\\text{crit}}$), transitional, and stable ($r \\geq r_{\\text{crit}}$) zones.\nType classification is based solely on spectral trajectory shape; downstream metrics such as D-4 may diverge, as demonstrated by the non-monotonic D-4 pattern across mixing ratios (Table~\\ref{tab:phase_summary}).\nAt $r{=}0.3$, SLV expands monotonically from Gen~2 to 2508.2 at Gen~10 ($+$6.0\\% above baseline), with sustained positive growth across all eight post-transient generations.\nThis confirms $r{=}0.3 \\geq r_{\\text{crit}}$ over the full 10-generation horizon, tightening the bound to $0.25 < r_{\\text{crit}} \\leq 0.3$.\nAcross three seeds, one individual EMA-smoothed trajectory shows a transient violation of 0.83~points at Gen~2; the remaining two satisfy non-decreasing from $t \\geq 2$. The cross-seed mean trajectory is non-decreasing at all post-transient generations (Gen~10 SLV CV $= 0.12\\%$), confirming the Type~III classification.\nThe single-seed transient is consistent with the continuous crossover interpretation: near the phase boundary, individual realizations may briefly exhibit sub-critical behavior even when the mean trajectory is stable.\nThe critical threshold is robust to the smoothing parameter: recomputing the EMA-smoothed SLV for $\\alpha \\in \\{0.3, 0.5, 0.7\\}$ yields $r_{\\text{crit}} \\in (0.25, 0.3]$ in all cases, with the non-decreasing condition violated at Gen~2 for $r \\leq 0.25$ and satisfied on the cross-seed mean for $r \\geq 0.3$ regardless of $\\alpha$.\n\nThe largest single-generation SLV drop in the first two generations shrinks with $r$: $-9.2$ at $r{=}0.2$ (Gen~1$\\to$2), $-4.6$ at $r{=}0.25$ (Gen~0$\\to$1; seed~42), and $-0.6$ at $r{=}0.3$ (Gen~0$\\to$1), consistent with a continuous crossover rather than a sharp boundary.\nThe Type~II trajectory clarifies what $r_{\\text{crit}}$ marks in practice: not a boundary between collapse and stability in final outcome, but a transition in trajectory shape.\nBelow $r_{\\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion through Gen~10 once the transient passes.\n\n\\paragraph{Output Diversity Divergence.}\nAt $r{=}0.2$, D-4 exhibits a V-shaped recovery (0.438 at Gen~5 $\\to$ 0.520 at Gen~10), but this pattern does not generalize: at $r{=}0.25$, D-4 declines monotonically to 0.342 despite comparable SLV recovery, indicating that spectral expansion does not guarantee diversity restoration.\nMore broadly, D-4 exhibits a non-monotonic relationship with $r$: it peaks at $r{=}0.2$ (.520), exceeds the pure-collapse baseline (.324) at $r \\leq 0.25$ but drops below it at $r \\geq 0.3$, reaching .152 at $r{=}0.5$, the lowest across all conditions (Table~\\ref{tab:phase_summary}).\nThis pattern is consistent with increasing real-data anchoring: at high $r$, the model converges toward the fixed real-data distribution, producing coherent but stylistically homogeneous text.\nThis divergence between spectral health (monotonically improving with $r$) and n-gram diversity underscores that SLV and D-4 capture orthogonal aspects of model behavior.\nD-4 exhibits substantially higher cross-seed variance than spectral metrics: at $r{=}0$ (s.d.\\ $= 0.15$ vs.\\ SLV s.d.\\ $= 28$, a ${>}30\\times$ lower coefficient of variation for SLV) and $r{=}0.3$ (s.d.\\ $= 0.155$ vs.\\ SLV s.d.\\ $= 2.9$; Table~\\ref{tab:phase_summary}), suggesting that n-gram diversity reflects stochastic generation choices rather than the deterministic geometric structure captured by SLV.\nThis pattern generalizes across mixing ratios: at $r{=}0.25$, SLV cross-seed CV is 0.12\\% versus 3.9\\% for D-4, confirming that spectral geometry captures a deterministic structural property largely independent of stochastic training noise.\n\nTable~\\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}clrrrrrc@{}}\n\\toprule\n$r$ & Type & SLV & $r_{\\text{eff}}$ & PPL & D-4 & $\\max\\Delta_t$ & Gen. \\\\\n\\midrule\n0    & I   & 2181.4 & 438.1 & 71.0\\phantom{0} & .324 & ---   & 10 \\\\\n0.20 & II  & 2479.7 & 511.3 & 13.83 & .520 & .0019 & 10 \\\\\n0.25 & II  & 2488.1 & 513.8 & 13.41 & .342 & .0003 & 10 \\\\\n0.30 & III & 2508.2 & 521.1 & 13.35 & .295 & 0     & 10 \\\\\n0.50 & III & 2571.7 & 553.5 & 15.12 & .152 & 0     & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Final-generation spectral and downstream metrics across mixing ratios (all runs to Gen~10). $\\max\\Delta_t$ computed for $t \\geq 2$, excluding the initial fine-tuning transient. Type classification follows \\S\\ref{subsec:phase_diagram}. $r{=}0$ reports the mean of three seeds (42, 43, 44); $r{=}0.3$ the mean of three seeds (42, 43, 44); $r{=}0.2$ reports a single seed; $r{=}0.5$ the mean of two seeds (42, 43); $r{=}0.25$ the mean of three seeds (42, 43, 44). D-4 exhibits high cross-seed variance at $r{=}0$ (s.d.\\ $= 0.15$) and $r{=}0.3$ (s.d.\\ $= 0.155$).}\n\\label{tab:phase_summary}\n\\end{table}\n\n\\paragraph{Second-order and alternative triggers.}\nA second-order acceleration indicator $\\Delta^2_t$ (Eq.~\\ref{eq:second_order}) does not discriminate between sub- and super-critical regimes: all trajectories exhibit negative $\\Delta^2_t$ in late generations regardless of mixing ratio.\nA level-based trigger keyed to baseline SLV could detect the transient dip in Type~II trajectories, but would not activate under Type~III where SLV exceeds baseline at all generations.\nFiner resolution between 0.25 and 0.3 would narrow the $r_{\\text{crit}}$ bound but would not change the practical recommendation to set $r$ above 0.3.\nFor practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.\n",
    "structuredPatch": [
      {
        "oldStart": 192,
        "oldLines": 3,
        "newStart": 192,
        "newLines": 65,
        "lines": [
          " A level-based trigger keyed to baseline SLV could detect the transient dip in Type~II trajectories, but would not activate under Type~III where SLV exceeds baseline at all generations.",
          " Finer resolution between 0.25 and 0.3 would narrow the $r_{\\text{crit}}$ bound but would not change the practical recommendation to set $r$ above 0.3.",
          " For practitioners, the phase diagram provides a direct prescription: in our setting, setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.",
          "+",
          "+% ==============================================================================",
          "+% §3.6 Cross-Architecture Confirmation [COMMENTED OUT — uncomment after exp_020]",
          "+% ==============================================================================",
          "+%",
          "+% \\subsection{Cross-Architecture Confirmation}",
          "+% \\label{subsec:cross_arch}",
          "+%",
          "+% To provide preliminary cross-architecture evidence, we repeat the pure-synthetic",
          "+% recursive pipeline ($r{=}0$, seed~42) on GPT-2-medium (24 layers, ${\\sim}$355M",
          "+% parameters), a decoder-only transformer with a different pretraining corpus and",
          "+% tokenizer than Pythia-410M.",
          "+%",
          "+% \\paragraph{Hypothesis.}",
          "+% If the three-phase spectral trajectory (decompression, onset, accelerating",
          "+% collapse) reflects a general property of recursive synthetic fine-tuning rather",
          "+% than an architecture-specific artifact of Pythia, GPT-2-medium should exhibit a",
          "+% qualitatively similar SLV trajectory under the same protocol.",
          "+%",
          "+% \\paragraph{Setup.}",
          "+% We fine-tune GPT-2-medium (24 transformer layers, 1024-dimensional embeddings,",
          "+% ${\\sim}$355M parameters) on a 50K-subset of OpenWebText using the same",
          "+% hyperparameters and recursive pipeline as \\S\\ref{subsec:setup}, for",
          "+% \\texttt{TBD} recursive generations under $r{=}0$ with seed~42.",
          "+%",
          "+% \\paragraph{Results.}",
          "+% % TODO: Fill in actual metrics from exp_020",
          "+% Table~\\ref{tab:cross_arch} reports spectral and downstream metrics across",
          "+% generations for GPT-2-medium.",
          "+%",
          "+% % TODO: Uncomment and populate table",
          "+% % \\begin{table}[t]",
          "+% % \\centering",
          "+% % \\small",
          "+% % \\setlength{\\tabcolsep}{4pt}",
          "+% % \\begin{tabular}{@{}rrrrrrc@{}}",
          "+% % \\toprule",
          "+% % Gen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\",
          "+% % \\midrule",
          "+% % 0  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\",
          "+% % 2  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\",
          "+% % 5  & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\",
          "+% % 10 & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} & \\texttt{TBD} \\\\",
          "+% % \\bottomrule",
          "+% % \\end{tabular}",
          "+% % \\caption{Spectral and downstream metrics for GPT-2-medium ($r{=}0$, seed~42).}",
          "+% % \\label{tab:cross_arch}",
          "+% % \\end{table}",
          "+%",
          "+% % TODO: Describe whether three-phase pattern is reproduced",
          "+% % TODO: Report SLV peak generation and magnitude",
          "+% % TODO: Compare decompression amplitude with Pythia-410M",
          "+%",
          "+% \\paragraph{Discussion.}",
          "+% % TODO: Fill in after exp_020 results",
          "+% These results provide initial confirmation on a second architecture that the",
          "+% three-phase spectral trajectory is not specific to the Pythia model family.",
          "+% The qualitative agreement between Pythia-410M and GPT-2-medium suggests that",
          "+% spectral decompression followed by collapse onset is a recurring pattern in",
          "+% recursive synthetic fine-tuning, though further architectures and scales would",
          "+% be needed to establish broader generality.",
          "+% =============================================================================="
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

Both edits done. Compiling to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "7df079c5-8877-4679-ad98-2064a08890cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVjkDTUs3CiTZt7jxXnN8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 33015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1785
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

<details open><summary>🔧 Tool call — Bash · `toolu_01JA5v1WigCQK3D8s8U43C8s`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
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
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "5131f062-bf67-4764-b2b8-0ef91cf6acbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVjkDTUs3CiTZt7jxXnN8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 33015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1785
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

_source line 17 · 2026-05-23T10:11:55.112Z_

<details><summary>↩ Tool result · `toolu_01JA5v1WigCQK3D8s8U43C8s`</summary>

```text
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi
9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/
msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m
sbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (12 pages, 347364 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "ed257829-a783-4187-97dd-733d3c7db25c",
  "tool_use_result": {
    "stdout": "blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi\n9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/\nmsam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m\nsbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (12 pages, 347364 bytes).\nTranscript written on main.log.",
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

_source line 18_

编译成功，12 页，无新 warning。

两处修改完成：
1. **abstract.tex** — 末尾添加了 `% TODO: Add cross-architecture confirmation sentence once exp_020 completes.`
2. **experiments.tex** — §3.5 之后添加了完整的 §3.6 "Cross-Architecture Confirmation" 框架，全部用 `%` 注释掉，包含 hypothesis、setup、results placeholder（`\texttt{TBD}`）、table 模板、discussion，措辞均使用 "preliminary cross-architecture evidence" / "initial confirmation on a second architecture" 等温和表述。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "uuid": "55be11a7-7ec1-4054-b1d8-8e70b064131a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3yMiv2vKRe3VWEVsYF5y6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 34800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 877
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

_source line 19_

编译成功，12 页，无新 warning。

两处修改完成：
1. **abstract.tex** — 末尾添加了 `% TODO: Add cross-architecture confirmation sentence once exp_020 completes.`
2. **experiments.tex** — §3.5 之后添加了完整的 §3.6 "Cross-Architecture Confirmation" 框架，全部用 `%` 注释掉，包含 hypothesis、setup、results placeholder（`\texttt{TBD}`）、table 模板、discussion，措辞均使用 "preliminary cross-architecture evidence" / "initial confirmation on a second architecture" 等温和表述。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 47434,
  "duration_api_ms": 48605,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "7edc433c-2305-4309-9407-3bc6b1808af1",
  "total_cost_usd": 0.2548595,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 23836,
    "cache_read_input_tokens": 104557,
    "output_tokens": 2086,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23836,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 171,
        "cache_read_input_tokens": 34800,
        "cache_creation_input_tokens": 877,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 877
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1351,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001431,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 2086,
      "cacheReadInputTokens": 104557,
      "cacheCreationInputTokens": 23836,
      "webSearchRequests": 0,
      "costUSD": 0.2534285,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a1abde50-5837-4140-b406-d142718477a5"
}
```

</details>

---
