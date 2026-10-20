# audit appendix discoverability

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_audit_appendix_discoverability_20260524T050201.log`
- **Structured JSON:** [`2e388c641a5969e306f8.json`](../../sessions/2e/2e388c641a5969e306f8.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
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
  "uuid": "c6076a98-aaeb-407b-b2f9-429611be4482",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "resetsAt": 1779608400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "378b18de-dfb1-4796-abc0-01bdc1018f51",
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the appendix file first to extract all sections, tables, and figures with their labels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "683adfdc-6091-40e1-ab52-b06286a5a9d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2PY5damTSjHZBiDMdYSDT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01JEn99QUrJkuXM6Rj16pxjZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "ced5be24-b27a-43bd-babf-9445897df390",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2PY5damTSjHZBiDMdYSDT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
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

_source line 6 · 2026-05-24T05:02:14.745Z_

<details><summary>↩ Tool result · `toolu_01JEn99QUrJkuXM6Rj16pxjZ`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (102\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').
69	
70	Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.
71	
72	The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
73	
74	\begin{table}[h]
75	\centering\small
76	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
77	\label{tab:ir-results}
78	\begin{tabular}{lccc}
79	\toprule
80	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
81	\midrule
82	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
83	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
84	Count      & 100\%  & 100\%  & 0 \\
85	Format     & 100\%  & 100\%  & 0 \\
86	\midrule
87	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
88	\bottomrule
89	\end{tabular}
90	\end{table}
91	
92	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
93	
94	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each. In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. This length dependence is consistent with exposure bias compounding over turns---each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn 10 the accumulated drift overwhelms any gating signal.
95	
96	\begin{table}[h]
97	\centering\small
98	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
99	\label{tab:n5-ar}
100	\begin{tabular}{lcc}
101	\toprule
102	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
103	\midrule
104	Base & 0.012 & $-$0.007 \\
105	\midrule
106	ThreadGate & 0.016 & $-$0.048 \\
107	\;+\,PCGrad & 0.015 & $-$0.015 \\
108	Uniform Gate & 0.015 & $-$0.018 \\
109	LoRA-only & 0.025 & $-$0.012 \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\section{Statistical Test Details}\label{sec:appendix-stats}
115	
116	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
117	
118	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
119	
120	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
121	
122	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
123	
124	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
125	
126	\begin{table}[h]
127	\centering\small
128	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
129	\label{tab:stat-tests}
130	\begin{tabular}{llcc}
131	\toprule
132	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
133	\midrule
134	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
135	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
136	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
137	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
138	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
139	\midrule
140	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
141	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
142	\midrule
143	\multicolumn{4}{l}{\emph{Instruction retention}} \\
144	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
145	GAR--compliance & Pearson & 0.007 & 0.200 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
151	
152	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
153	
154	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
155	
156	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
157	
158	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
159	
160	\begin{table}[h]
161	\centering\small
162	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20, mid-turn). Median is more representative due to heavy-tailed AR distributions.}
163	\label{tab:llama-full}
164	\resizebox{\columnwidth}{!}{%
165	\begin{tabular}{lcccc}
166	\toprule
167	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
170	\midrule
171	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
172	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
173	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
179	
180	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
181	
182	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
183	
184	\section{Additional Visualizations}\label{sec:appendix-viz}
185	
186	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
187	
188	\subsection{Gate Profile Heatmap}
189	
190	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
191	
192	\begin{figure*}[h]
193	\centering
194	\includegraphics[width=0.95\textwidth]{fig_gate_profile_heatmap.pdf}
195	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
196	\label{fig:gate-heatmap}
197	\end{figure*}
198	
199	\subsection{Cross-Model Gate Profile Comparison}
200	
201	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
202	
203	\begin{figure*}[h]
204	\centering
205	\includegraphics[width=0.95\textwidth]{fig_gate_profile_crossmodel.pdf}
206	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
207	\label{fig:gate-crossmodel}
208	\end{figure*}
209	
210	\subsection{Per-Turn AR GAR Decay}
211	
212	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
213	
214	\begin{figure*}[h]
215	\centering
216	\includegraphics[width=0.95\textwidth]{fig_ar_gar_perturn.pdf}
217	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
218	\label{fig:ar-gar-perturn}
219	\end{figure*}
220	
221	\subsection{Gate Value Distributions}
222	
223	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
224	
225	\begin{figure*}[h]
226	\centering
227	\includegraphics[width=0.95\textwidth]{fig_gate_distribution.pdf}
228	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
229	\label{fig:gate-distribution}
230	\end{figure*}
231	
232	\subsection{Training Loss Curves}
233	
234	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
235	
236	\begin{figure*}[h]
237	\centering
238	\includegraphics[width=0.95\textwidth]{fig_training_loss_curves.pdf}
239	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
240	\label{fig:training-loss}
241	\end{figure*}
242	
243	\input{../artifacts/table_steering_full}
244	
245	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
246	
247	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
248	
249	\begin{table}[h]
250	\centering\small
251	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
252	\label{tab:gate-profile}
253	\resizebox{\columnwidth}{!}{%
254	\begin{tabular}{cccccccc}
255	\toprule
256	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
257	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
258	\midrule
259	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
260	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
261	\midrule
262	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
263	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
264	\midrule
265	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
266	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
267	\bottomrule
268	\end{tabular}}
269	\end{table}
270	
271	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
272	
273	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
274	
275	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
276	
277	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
278	
279	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
280	
281	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
282	
283	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
284	
285	\section{Computational Cost Analysis}\label{sec:appendix-cost}
286	
287	\begin{table}[h]
288	\centering\small
289	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\,GB VRAM).}
290	\label{tab:cost}
291	\resizebox{\columnwidth}{!}{%
292	\begin{tabular}{lcccc}
293	\toprule
294	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
295	\midrule
296	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
297	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
298	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
299	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
300	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
301	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
302	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
303	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
304	\midrule
305	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
306	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
307	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
308	\bottomrule
309	\end{tabular}}
310	\end{table}
311	
312	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
313	
314	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
315	
316	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
317	
318	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
319	
320	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
321	
322	\begin{table*}[h]
323	\centering\small
324	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
325	\label{tab:examples}
326	\begin{tabular}{c p{5.5cm} p{5.5cm}}
327	\toprule
328	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
329	\midrule
330	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
331	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
332	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
333	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
334	\bottomrule
335	\end{tabular}
336	\end{table*}
337	
338	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
339	
340	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
341	
342	Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate (v7) and PCGrad (v9) training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---NTP magnitude dominance grows from 7.5$\times$ to 14.7$\times$ across epochs. Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane. The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). Despite this spatial correlation, eliminating directional conflict via PCGrad does not improve AR GAR (\S\ref{subsec:pcgrad}), confirming that the 7.5--14.7$\times$ magnitude dominance---not directional opposition---determines the effective optimization trajectory.
343	
344	\begin{figure*}[h]
345	\centering
346	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
347	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out directional conflict as the cause (\S\ref{subsec:pcgrad}).}
348	\label{fig:gradient-heatmap}
349	\end{figure*}
350	
351	\section{Training Data Characteristics}\label{sec:appendix-data}
352	
353	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
354	
355	\begin{table}[h]
356	\centering\small
357	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
358	\label{tab:data-stats}
359	\begin{tabular}{lcc}
360	\toprule
361	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
362	\midrule
363	Conversations & 8,000 & 50 \\
364	Min user turns & 3 & 3 \\
365	Max sequence length & 2,048 & 2,048 \\
366	Source & UltraChat train & UltraChat train \\
367	Overlap & --- & non-overlapping \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
373	
374	Figure~\ref{fig:eb-scaling} quantifies two dimensions of the exposure bias phenomenon. Panel~(a) compares the TF/AR gap ratio across all training variants and both architectures. On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
375	
376	\begin{figure*}[h]
377	\centering
378	\includegraphics[width=0.95\textwidth]{fig_eb_scaling.pdf}
379	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
380	\label{fig:eb-scaling}
381	\end{figure*}
382	
383	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
384	
385	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
386	
387	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:four-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
388	
389	\begin{figure}[t]
390	\centering
391	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
392	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
393	\label{fig:kl_ar_gar_curves}
394	\end{figure}
395	
396	\begin{figure}[t]
397	\centering
398	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
399	\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
400	\label{fig:kl_ar_gar_bar}
401	\end{figure}
402	
403	This pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \S\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.
404	
405	%% TODO: per-head KL analysis results
406	%% When per-head GPU analysis completes, add:
407	%% - per-head KL divergence between TF and AR attention distributions
408	%% - identification of which heads are most affected by exposure bias
409	%% - layer-level breakdown of attention shift patterns
410	
411	\section{Use of AI Assistants}\label{sec:appendix-ai}
412	
413	We used Claude (Anthropic) as an AI coding and writing assistant
414	throughout this work. Specifically:
415	\begin{itemize}
416	    \item \textbf{Code:} drafting experiment scripts, data-processing
417	    pipelines, and analysis utilities; debugging and refactoring.
418	    \item \textbf{Writing:} drafting and revising paper sections,
419	    polishing prose, and reformatting LaTeX.
420	    \item \textbf{Literature:} summarizing related papers to inform
421	    related-work section.
422	\end{itemize}
423	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "6422ff9f-e3f3-404e-a2ec-b032aea4a530",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (102\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').\n\nTable~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.\n\nThe GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:four-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each. In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. This length dependence is consistent with exposure bias compounding over turns---each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn 10 the accumulated drift overwhelms any gating signal.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:four-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:four-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20, mid-turn). Median is more representative due to heavy-tailed AR distributions.}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure*}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure*}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure*}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure*}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure*}\n\n\\input{../artifacts/table_steering_full}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\\,GB VRAM).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 6.0 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[h]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\nFigure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate (v7) and PCGrad (v9) training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---NTP magnitude dominance grows from 7.5$\\times$ to 14.7$\\times$ across epochs. Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane. The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). Despite this spatial correlation, eliminating directional conflict via PCGrad does not improve AR GAR (\\S\\ref{subsec:pcgrad}), confirming that the 7.5--14.7$\\times$ magnitude dominance---not directional opposition---determines the effective optimization trajectory.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out directional conflict as the cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two dimensions of the exposure bias phenomenon. Panel~(a) compares the TF/AR gap ratio across all training variants and both architectures. On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$, the only variant approaching parity. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure*}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:four-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_bar.pdf}\n\\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}\n\\label{fig:kl_ar_gar_bar}\n\\end{figure}\n\nThis pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \\S\\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.\n\n%% TODO: per-head KL analysis results\n%% When per-head GPU analysis completes, add:\n%% - per-head KL divergence between TF and AR attention distributions\n%% - identification of which heads are most affected by exposure bias\n%% - layer-level breakdown of attention shift patterns\n\n\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
      "numLines": 423,
      "startLine": 1,
      "totalLines": 423
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now let me also check the steering table that's included via `\input`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "111cd666-aac9-4e36-93b9-ec5cb5ebacfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnc5ZN2XDUGfjt9n9MDKiu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12435,
      "cache_read_input_tokens": 25332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12435
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

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01QfbB9oyGVAbzrJV8c6Wamx`</summary>

```json
{
  "pattern": "**/table_steering_full*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "2312cf7a-bed6-42ec-b0a0-213f188b9567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnc5ZN2XDUGfjt9n9MDKiu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12435,
      "cache_read_input_tokens": 25332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12435
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

_source line 9 · 2026-05-24T05:02:27.006Z_

<details><summary>↩ Tool result · `toolu_01QfbB9oyGVAbzrJV8c6Wamx`</summary>

```text
artifacts/_project/paper/table_steering_full.tex
artifacts/table_steering_full.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "5aec4c35-4199-4f5d-bfa6-ca0761b4fea7",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/table_steering_full.tex",
      "artifacts/table_steering_full.tex"
    ],
    "durationMs": 18,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_018rF8t5K5UNuhxG6G9KbV5X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/table_steering_full.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "24ee185e-f252-4508-86bc-dc5d22ec3b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oExJPEHeUSPEGmzaHGnFa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 37767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 156
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 11 · 2026-05-24T05:02:29.025Z_

<details><summary>↩ Tool result · `toolu_018rF8t5K5UNuhxG6G9KbV5X`</summary>

```text
1	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
2	
3	\begin{table*}[t]
4	\centering\small
5	\caption{Full attention steering results across evaluation settings.
6	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
7	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
8	\label{tab:steering-full}
9	\begin{tabular}{r cc cc cc}
10	\toprule
11	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
12	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
13	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
14	\midrule
15	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
16	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
17	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
18	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
19	\addlinespace[3pt]
20	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
21	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
22	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
23	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
24	\bottomrule
25	\end{tabular}
26	\end{table*}
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "1d40a453-f7e6-4fa0-9a0b-c5322f9ab850",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/table_steering_full.tex",
      "content": "\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the appendix labels. Let me compile the list:

**Sections:**
1. `sec:appendix-hyper` — Training Configuration
2. `sec:appendix-loss` — Loss Formulation Search
3. `sec:appendix-ir` — Instruction Retention Details
4. `sec:appendix-n5` — Long-Conversation AR Evaluation
5. `sec:appendix-stats` — Statistical Test Details
6. `sec:appendix-llama` — Llama-3.1-8B Complete Results
7. `sec:appendix-viz` — Additional Visualizations


8. `sec:appendix-gate-profile` — Per-Layer Gate Profile
9. `sec:appendix-ss` — Scheduled Sampling Implementation
10. `sec:appendix-cost` — Computational Cost Analysis
11. `sec:appendix-examples` — Qualitative Steering Examples
12. `sec:appendix-gradient` — Gradient Conflict Analysis
13. `sec:appendix-data` — Training Data Characteristics
14. `sec:appendix-eb-scaling` — Exposure Bias Scaling
15. `sec:appendix-ar-gar-dynamics` — Per-Turn AR GAR Dynamics
16. `sec:appendix-ai` — Use of AI Assist
17. `sec:appendix-steering` — Full Attention Steering Results

Now I'm compiling the tables that support these sections—hyperparameters, loss iterations, instruction retention results, AR GAR performance metrics, statistical tests, Llama results, per-layer gate values, computational costs, qualitative examples, data characteristics, and the full attention steering results.

I'm also cataloging the figures: heatmaps showing per-layer gate values and gradient conflicts, cross-model gate comparisons, AR GAR decay patterns across conversation turns, gate value distributions, training loss curves, exposure bias scaling, and per-turn AR GAR trajectories. Now I need to locate each of these labels in the main text files to verify they're properly referenced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "1df8264c-6c3c-47e0-adde-d99ff90680a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qZ4jf54fvHxYpgCbb2a8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 37923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 13_

Now let me search for all these labels in the main text files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "ab7dca2e-d2c3-4072-bb31-409e21e434ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qZ4jf54fvHxYpgCbb2a8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 37923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_015QAiysEnmDCHhWEG6fWM3v`</summary>

```json
{
  "command": "for label in sec:appendix-hyper sec:appendix-loss sec:appendix-ir sec:appendix-n5 sec:appendix-stats sec:appendix-llama sec:appendix-viz sec:appendix-gate-profile sec:appendix-ss sec:appendix-cost sec:appendix-examples sec:appendix-gradient sec:appendix-data sec:appendix-eb-scaling sec:appendix-ar-gar-dynamics sec:appendix-ai sec:appendix-steering tab:hyperparams tab:loss-iterations tab:ir-results tab:n5-ar tab:stat-tests tab:llama-full tab:gate-profile tab:cost tab:examples tab:data-stats tab:steering-full fig:gate-heatmap fig:gate-crossmodel fig:ar-gar-perturn fig:gate-distribution fig:training-loss fig:gradient-heatmap fig:eb-scaling fig:kl_ar_gar_curves fig:kl_ar_gar_bar; do echo \"=== $label ===\"; grep -rn \"$label\" paper/sections/*.tex | grep -v appendix.tex || echo \"NOT_FOUND\"; done",
  "description": "Search all appendix labels in main text sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "5706cc92-f808-4c86-8bcc-26ee51c705af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qZ4jf54fvHxYpgCbb2a8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 37923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 15 · 2026-05-24T05:02:47.627Z_

<details><summary>↩ Tool result · `toolu_015QAiysEnmDCHhWEG6fWM3v`</summary>

```text
=== sec:appendix-hyper ===
paper/sections/experiments.tex:6:We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
paper/sections/method.tex:58:We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate vs.\ Uniform Gate} (turn conditioning), \textbf{ThreadGate vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient direction conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
=== sec:appendix-loss ===
paper/sections/method.tex:44:$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\mathcal{L}_\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \emph{bidirectional} pressure---penalizing both under-attention (GAR\,$<$\,$\tau$) and over-attention (GAR\,$>$\,$\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\ref{sec:appendix-loss}). The GAR loss is:
paper/sections/method.tex:54:\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.
=== sec:appendix-ir ===
paper/sections/discussion.tex:7:\paragraph{Downstream effects.} Instruction retention ($\beta$\,=\,3) shows late-turn compliance rising from 75.9\% to 87.0\% (+11.1\,pp, McNemar $p$\,=\,0.077; GAR correlation $r$\,=\,0.200, $p$\,=\,0.007). Content constraints benefit most (+23.8\,pp), while format constraints show zero change---consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\ref{sec:appendix-ir}).
=== sec:appendix-n5 ===
paper/sections/experiments.tex:58:Scheduled sampling \citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets the training-inference mismatch identified in \S\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\pm0.047$ (seeds: 0.347 / 0.423 / 0.433), compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ with no PPL cost ($1.441\pm0.001$).\footnote{Seed 123 TF GAR unavailable (checkpoint error); per-seed gaps: 1.45$\times$ (s42), 1.15$\times$ (s456).} Steering on SS models is remarkably stable ($\beta$\,=\,5: $0.717\pm0.001$): the training-time seed variance (std\,=\,0.047 at $\beta$\,=\,0) is nearly eliminated, suggesting $\beta$-steering converges to a seed-independent attention equilibrium. GAR-Dongre also rises substantially under SS ($N$\,=\,5 pilot; see Appendix~\ref{sec:appendix-n5})---the only intervention that moves both metrics. The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
=== sec:appendix-stats ===
paper/sections/experiments.tex:12:Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
=== sec:appendix-llama ===
paper/sections/analysis.tex:39:We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20 conversations, 4 turns each). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit, consistent with Qwen. The AR distribution is heavy-tailed (CoV\,$>$\,100\%): ThreadGate shows a 5\% spike ratio (2/40 turns with GAR\,$\geq$\,0.4, std\,=\,0.100) while LoRA-only has 0\% spikes (std\,=\,0.048). We therefore report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a). Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\times$ and 17$\times$---the mean-median divergence confirms that rare high-GAR turns inflate means without reflecting typical model behavior (Appendix~\ref{sec:appendix-llama}).
=== sec:appendix-viz ===
NOT_FOUND
=== sec:appendix-gate-profile ===
NOT_FOUND
=== sec:appendix-ss ===
NOT_FOUND
=== sec:appendix-cost ===
NOT_FOUND
=== sec:appendix-examples ===
NOT_FOUND
=== sec:appendix-gradient ===
NOT_FOUND
=== sec:appendix-data ===
NOT_FOUND
=== sec:appendix-eb-scaling ===
NOT_FOUND
=== sec:appendix-ar-gar-dynamics ===
NOT_FOUND
=== sec:appendix-ai ===
NOT_FOUND
=== sec:appendix-steering ===
paper/sections/experiments.tex:52:where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero (Figure~\ref{fig:headline}b). The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Appendix~\ref{sec:appendix-steering}).
=== tab:hyperparams ===
NOT_FOUND
=== tab:loss-iterations ===
NOT_FOUND
=== tab:ir-results ===
NOT_FOUND
=== tab:n5-ar ===
NOT_FOUND
=== tab:stat-tests ===
NOT_FOUND
=== tab:llama-full ===
NOT_FOUND
=== tab:gate-profile ===
NOT_FOUND
=== tab:cost ===
NOT_FOUND
=== tab:examples ===
NOT_FOUND
=== tab:data-stats ===
NOT_FOUND
=== tab:steering-full ===
NOT_FOUND
=== fig:gate-heatmap ===
NOT_FOUND
=== fig:gate-crossmodel ===
NOT_FOUND
=== fig:ar-gar-perturn ===
NOT_FOUND
=== fig:gate-distribution ===
NOT_FOUND
=== fig:training-loss ===
NOT_FOUND
=== fig:gradient-heatmap ===
NOT_FOUND
=== fig:eb-scaling ===
NOT_FOUND
=== fig:kl_ar_gar_curves ===
NOT_FOUND
=== fig:kl_ar_gar_bar ===
NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "7ea62e9e-0109-4d20-bcaf-624bfaa29efa",
  "tool_use_result": {
    "stdout": "=== sec:appendix-hyper ===\npaper/sections/experiments.tex:6:We fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\\,GB). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and PPL.\npaper/sections/method.tex:58:We design a five-way comparison where each adjacent pair isolates one factor: \\textbf{ThreadGate vs.\\ Uniform Gate} (turn conditioning), \\textbf{ThreadGate vs.\\ LoRA-only} (gating mechanism), \\textbf{ThreadGate vs.\\ +PCGrad} (gradient direction conflict via gradient surgery \\citep{yu2020pcgrad}), and \\textbf{Fine-tuned vs.\\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\\ref{sec:appendix-hyper}).\n=== sec:appendix-loss ===\npaper/sections/method.tex:44:$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\\mathcal{L}_\\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \\emph{bidirectional} pressure---penalizing both under-attention (GAR\\,$<$\\,$\\tau$) and over-attention (GAR\\,$>$\\,$\\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\\ref{sec:appendix-loss}). The GAR loss is:\npaper/sections/method.tex:54:\\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.\n=== sec:appendix-ir ===\npaper/sections/discussion.tex:7:\\paragraph{Downstream effects.} Instruction retention ($\\beta$\\,=\\,3) shows late-turn compliance rising from 75.9\\% to 87.0\\% (+11.1\\,pp, McNemar $p$\\,=\\,0.077; GAR correlation $r$\\,=\\,0.200, $p$\\,=\\,0.007). Content constraints benefit most (+23.8\\,pp), while format constraints show zero change---consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\\ref{sec:appendix-ir}).\n=== sec:appendix-n5 ===\npaper/sections/experiments.tex:58:Scheduled sampling \\citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets the training-inference mismatch identified in \\S\\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\\pm0.047$ (seeds: 0.347 / 0.423 / 0.433), compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ with no PPL cost ($1.441\\pm0.001$).\\footnote{Seed 123 TF GAR unavailable (checkpoint error); per-seed gaps: 1.45$\\times$ (s42), 1.15$\\times$ (s456).} Steering on SS models is remarkably stable ($\\beta$\\,=\\,5: $0.717\\pm0.001$): the training-time seed variance (std\\,=\\,0.047 at $\\beta$\\,=\\,0) is nearly eliminated, suggesting $\\beta$-steering converges to a seed-independent attention equilibrium. GAR-Dongre also rises substantially under SS ($N$\\,=\\,5 pilot; see Appendix~\\ref{sec:appendix-n5})---the only intervention that moves both metrics. The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n=== sec:appendix-stats ===\npaper/sections/experiments.tex:12:Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n=== sec:appendix-llama ===\npaper/sections/analysis.tex:39:We replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20 conversations, 4 turns each). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit, consistent with Qwen. The AR distribution is heavy-tailed (CoV\\,$>$\\,100\\%): ThreadGate shows a 5\\% spike ratio (2/40 turns with GAR\\,$\\geq$\\,0.4, std\\,=\\,0.100) while LoRA-only has 0\\% spikes (std\\,=\\,0.048). We therefore report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a). Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\\times$ and 17$\\times$---the mean-median divergence confirms that rare high-GAR turns inflate means without reflecting typical model behavior (Appendix~\\ref{sec:appendix-llama}).\n=== sec:appendix-viz ===\nNOT_FOUND\n=== sec:appendix-gate-profile ===\nNOT_FOUND\n=== sec:appendix-ss ===\nNOT_FOUND\n=== sec:appendix-cost ===\nNOT_FOUND\n=== sec:appendix-examples ===\nNOT_FOUND\n=== sec:appendix-gradient ===\nNOT_FOUND\n=== sec:appendix-data ===\nNOT_FOUND\n=== sec:appendix-eb-scaling ===\nNOT_FOUND\n=== sec:appendix-ar-gar-dynamics ===\nNOT_FOUND\n=== sec:appendix-ai ===\nNOT_FOUND\n=== sec:appendix-steering ===\npaper/sections/experiments.tex:52:where $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero (Figure~\\ref{fig:headline}b). The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Appendix~\\ref{sec:appendix-steering}).\n=== tab:hyperparams ===\nNOT_FOUND\n=== tab:loss-iterations ===\nNOT_FOUND\n=== tab:ir-results ===\nNOT_FOUND\n=== tab:n5-ar ===\nNOT_FOUND\n=== tab:stat-tests ===\nNOT_FOUND\n=== tab:llama-full ===\nNOT_FOUND\n=== tab:gate-profile ===\nNOT_FOUND\n=== tab:cost ===\nNOT_FOUND\n=== tab:examples ===\nNOT_FOUND\n=== tab:data-stats ===\nNOT_FOUND\n=== tab:steering-full ===\nNOT_FOUND\n=== fig:gate-heatmap ===\nNOT_FOUND\n=== fig:gate-crossmodel ===\nNOT_FOUND\n=== fig:ar-gar-perturn ===\nNOT_FOUND\n=== fig:gate-distribution ===\nNOT_FOUND\n=== fig:training-loss ===\nNOT_FOUND\n=== fig:gradient-heatmap ===\nNOT_FOUND\n=== fig:eb-scaling ===\nNOT_FOUND\n=== fig:kl_ar_gar_curves ===\nNOT_FOUND\n=== fig:kl_ar_gar_bar ===\nNOT_FOUND",
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

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check for any cross-references within the appendix itself (appendix sections referencing each other), which counts as "referenced" but from within appendix, not from main text. Let me also check for textual references like "Appendix" that don't use \ref.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "2c22f6b9-b660-48a0-92db-fa1524cb429c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ha5thWhVBkXPSVqFczbSy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3650,
      "cache_read_input_tokens": 38770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3650
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

_source line 17_

Let me also check for textual "Appendix" references that might point to these sections without using `\ref`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "2d6e4fc4-311f-4d48-ae75-9a798542c13c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ha5thWhVBkXPSVqFczbSy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3650,
      "cache_read_input_tokens": 38770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3650
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_016oHyMuGDrEgjeD6cBxKtkM`</summary>

```json
{
  "command": "grep -rn -i \"appendix\\|App\\.\" paper/sections/*.tex | grep -v appendix.tex | grep -v \"\\.bib\" | grep -v \"^Binary\"",
  "description": "Search for textual Appendix references in main text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "58956db5-7c5c-45d9-afde-18abbc98cc4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ha5thWhVBkXPSVqFczbSy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3650,
      "cache_read_input_tokens": 38770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3650
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

_source line 19 · 2026-05-24T05:02:53.565Z_

<details><summary>↩ Tool result · `toolu_016oHyMuGDrEgjeD6cBxKtkM`</summary>

```text
paper/sections/analysis.tex:39:We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20 conversations, 4 turns each). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit, consistent with Qwen. The AR distribution is heavy-tailed (CoV\,$>$\,100\%): ThreadGate shows a 5\% spike ratio (2/40 turns with GAR\,$\geq$\,0.4, std\,=\,0.100) while LoRA-only has 0\% spikes (std\,=\,0.048). We therefore report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a). Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\times$ and 17$\times$---the mean-median divergence confirms that rare high-GAR turns inflate means without reflecting typical model behavior (Appendix~\ref{sec:appendix-llama}).
paper/sections/discussion.tex:7:\paragraph{Downstream effects.} Instruction retention ($\beta$\,=\,3) shows late-turn compliance rising from 75.9\% to 87.0\% (+11.1\,pp, McNemar $p$\,=\,0.077; GAR correlation $r$\,=\,0.200, $p$\,=\,0.007). Content constraints benefit most (+23.8\,pp), while format constraints show zero change---consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\ref{sec:appendix-ir}).
paper/sections/experiments.tex:6:We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
paper/sections/experiments.tex:12:Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
paper/sections/experiments.tex:52:where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero (Figure~\ref{fig:headline}b). The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Appendix~\ref{sec:appendix-steering}).
paper/sections/experiments.tex:58:Scheduled sampling \citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets the training-inference mismatch identified in \S\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\pm0.047$ (seeds: 0.347 / 0.423 / 0.433), compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ with no PPL cost ($1.441\pm0.001$).\footnote{Seed 123 TF GAR unavailable (checkpoint error); per-seed gaps: 1.45$\times$ (s42), 1.15$\times$ (s456).} Steering on SS models is remarkably stable ($\beta$\,=\,5: $0.717\pm0.001$): the training-time seed variance (std\,=\,0.047 at $\beta$\,=\,0) is nearly eliminated, suggesting $\beta$-steering converges to a seed-independent attention equilibrium. GAR-Dongre also rises substantially under SS ($N$\,=\,5 pilot; see Appendix~\ref{sec:appendix-n5})---the only intervention that moves both metrics. The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
paper/sections/method.tex:44:$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\mathcal{L}_\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \emph{bidirectional} pressure---penalizing both under-attention (GAR\,$<$\,$\tau$) and over-attention (GAR\,$>$\,$\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\ref{sec:appendix-loss}). The GAR loss is:
paper/sections/method.tex:54:\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.
paper/sections/method.tex:58:We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate vs.\ Uniform Gate} (turn conditioning), \textbf{ThreadGate vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient direction conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "372ce36d-3823-4750-893a-509a1a1acc6b",
  "tool_use_result": {
    "stdout": "paper/sections/analysis.tex:39:We replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20 conversations, 4 turns each). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit, consistent with Qwen. The AR distribution is heavy-tailed (CoV\\,$>$\\,100\\%): ThreadGate shows a 5\\% spike ratio (2/40 turns with GAR\\,$\\geq$\\,0.4, std\\,=\\,0.100) while LoRA-only has 0\\% spikes (std\\,=\\,0.048). We therefore report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a). Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\\times$ and 17$\\times$---the mean-median divergence confirms that rare high-GAR turns inflate means without reflecting typical model behavior (Appendix~\\ref{sec:appendix-llama}).\npaper/sections/discussion.tex:7:\\paragraph{Downstream effects.} Instruction retention ($\\beta$\\,=\\,3) shows late-turn compliance rising from 75.9\\% to 87.0\\% (+11.1\\,pp, McNemar $p$\\,=\\,0.077; GAR correlation $r$\\,=\\,0.200, $p$\\,=\\,0.007). Content constraints benefit most (+23.8\\,pp), while format constraints show zero change---consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\\ref{sec:appendix-ir}).\npaper/sections/experiments.tex:6:We fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\\,GB). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and PPL.\npaper/sections/experiments.tex:12:Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). We analyze this distribution shift in \\S\\ref{sec:analysis}.\npaper/sections/experiments.tex:52:where $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero (Figure~\\ref{fig:headline}b). The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Appendix~\\ref{sec:appendix-steering}).\npaper/sections/experiments.tex:58:Scheduled sampling \\citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets the training-inference mismatch identified in \\S\\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\\pm0.047$ (seeds: 0.347 / 0.423 / 0.433), compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ with no PPL cost ($1.441\\pm0.001$).\\footnote{Seed 123 TF GAR unavailable (checkpoint error); per-seed gaps: 1.45$\\times$ (s42), 1.15$\\times$ (s456).} Steering on SS models is remarkably stable ($\\beta$\\,=\\,5: $0.717\\pm0.001$): the training-time seed variance (std\\,=\\,0.047 at $\\beta$\\,=\\,0) is nearly eliminated, suggesting $\\beta$-steering converges to a seed-independent attention equilibrium. GAR-Dongre also rises substantially under SS ($N$\\,=\\,5 pilot; see Appendix~\\ref{sec:appendix-n5})---the only intervention that moves both metrics. The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\npaper/sections/method.tex:44:$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\\mathcal{L}_\\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \\emph{bidirectional} pressure---penalizing both under-attention (GAR\\,$<$\\,$\\tau$) and over-attention (GAR\\,$>$\\,$\\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\\ref{sec:appendix-loss}). The GAR loss is:\npaper/sections/method.tex:54:\\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.\npaper/sections/method.tex:58:We design a five-way comparison where each adjacent pair isolates one factor: \\textbf{ThreadGate vs.\\ Uniform Gate} (turn conditioning), \\textbf{ThreadGate vs.\\ LoRA-only} (gating mechanism), \\textbf{ThreadGate vs.\\ +PCGrad} (gradient direction conflict via gradient surgery \\citep{yu2020pcgrad}), and \\textbf{Fine-tuned vs.\\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\\ref{sec:appendix-hyper}).",
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

Results are clear. Here's the audit:

---

## == Appendix Sections ==

| Status | Section | Label | Referenced from |
|--------|---------|-------|-----------------|
| ✅ | Training Configuration | `sec:appendix-hyper` | experiments.tex, method.tex |
| ✅ | Loss Formulation Search | `sec:appendix-loss` | method.tex (×2) |
| ✅ | Instruction Retention Details | `sec:appendix-ir` | discussion.tex |
| ✅ | Long-Conversation AR Evaluation | `sec:appendix-n5` | experiments.tex (×2) |
| ✅ | Statistical Test Details | `sec:appendix-stats` | experiments.tex |
| ✅ | Llama-3.1-8B Complete Results | `sec:appendix-llama` | analysis.tex |
| ❌ | **Additional Visualizations** | `sec:appendix-viz` | 正文无引用 |
| ❌ | **Per-Layer Gate Profile** | `sec:appendix-gate-profile` | 正文无引用 |
| ❌ | **Scheduled Sampling Implementation** | `sec:appendix-ss` | 正文无引用 |
| ❌ | **Computational Cost Analysis** | `sec:appendix-cost` | 正文无引用 |
| ❌ | **Qualitative Steering Examples** | `sec:appendix-examples` | 正文无引用 |
| ❌ | **Gradient Conflict Analysis** | `sec:appendix-gradient` | 正文无引用 |
| ❌ | **Training Data Characteristics** | `sec:appendix-data` | 正文无引用 |
| ❌ | **Exposure Bias Scaling** | `sec:appendix-eb-scaling` | 正文无引用 |
| ❌ | **Per-Turn AR GAR Dynamics** | `sec:appendix-ar-gar-dynamics` | 正文无引用 |
| ❌ | **Use of AI Assistants** | `sec:appendix-ai` | 正文无引用 |
| ✅ | Full Attention Steering Results | `sec:appendix-steering` | experiments.tex |

## == Appendix Tables ==

| Status | Table | Label | Referenced from |
|--------|-------|-------|-----------------|
| ❌ | **Training hyperparameters** | `tab:hyperparams` | 正文无 `\ref` (仅通过 section 引用间接可达) |
| ❌ | **Loss formulation iterations** | `tab:loss-iterations` | 正文无引用 |
| ❌ | **Instruction retention by category** | `tab:ir-results` | 正文无引用 |
| ❌ | **AR GAR on N=5 ten-turn** | `tab:n5-ar` | 正文无引用 |
| ❌ | **Consolidated statistical tests** | `tab:stat-tests` | 正文无引用 |
| ❌ | **Llama complete results** | `tab:llama-full` | 正文无引用 |
| ❌ | **Per-layer gate values** | `tab:gate-profile` | 正文无引用 |
| ❌ | **Computational cost** | `tab:cost` | 正文无引用 |
| ❌ | **Qualitative steering examples** | `tab:examples` | 正文无引用 |
| ❌ | **Training/eval data stats** | `tab:data-stats` | 正文无引用 |
| ❌ | **Full steering results** | `tab:steering-full` | 正文无引用 |

## == Appendix Figures ==

| Status | Figure | Label | Referenced from |
|--------|--------|-------|-----------------|
| ❌ | **Gate profile heatmap** | `fig:gate-heatmap` | 正文无引用 |
| ❌ | **Cross-model gate comparison** | `fig:gate-crossmodel` | 正文无引用 |
| ❌ | **Per-turn AR GAR decay** | `fig:ar-gar-perturn` | 正文无引用 |
| ❌ | **Gate value distributions** | `fig:gate-distribution` | 正文无引用 |
| ❌ | **Training loss curves** | `fig:training-loss` | 正文无引用 |
| ❌ | **Gradient conflict heatmap** | `fig:gradient-heatmap` | 正文无引用 |
| ❌ | **Exposure bias scaling** | `fig:eb-scaling` | 正文无引用 |
| ❌ | **Per-turn AR GAR curves** | `fig:kl_ar_gar_curves` | 正文无引用 |
| ❌ | **Mid-turn AR GAR bar** | `fig:kl_ar_gar_bar` | 正文无引用 |

---

## 总结

- **Sections**: 7/17 有正文引用，**10 个无引用**
- **Tables**: 0/11 有正文直接 `\ref` 引用（所有 table 都只在 appendix 内部被引用）
- **Figures**: 0/9 有正文引用

注意：appendix 内部的 tables/figures 被它们所属的 appendix section 间接覆盖（如 `tab:hyperparams` 在 `sec:appendix-hyper` 中，而该 section 被正文引用）。但严格来说，reviewer 检查可发现性时，**10 个 section** 完全没有正文 pointer，读者无法从正文知道这些附录内容的存在。特别需要关注的高价值未引用 section：

1. **`sec:appendix-cost`** — 计算成本分析，reviewer 常问
2. **`sec:appendix-gradient`** — 梯度冲突分析，支撑 PCGrad 讨论
3. **`sec:appendix-ss`** — 调度采样实现细节
4. **`sec:appendix-data`** — 数据特征，可复现性相关
5. **`sec:appendix-eb-scaling`** — 曝光偏差缩放分析
6. **`sec:appendix-examples`** — 定性示例
7. **`sec:appendix-ai`** — AI 使用声明（部分会议要求）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "uuid": "11526e2f-ad51-4b6b-91b5-84ec63a8320a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEqttsErKnbBjdiQBaVtUc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 42420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2222
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

Results are clear. Here's the audit:

---

## == Appendix Sections ==

| Status | Section | Label | Referenced from |
|--------|---------|-------|-----------------|
| ✅ | Training Configuration | `sec:appendix-hyper` | experiments.tex, method.tex |
| ✅ | Loss Formulation Search | `sec:appendix-loss` | method.tex (×2) |
| ✅ | Instruction Retention Details | `sec:appendix-ir` | discussion.tex |
| ✅ | Long-Conversation AR Evaluation | `sec:appendix-n5` | experiments.tex (×2) |
| ✅ | Statistical Test Details | `sec:appendix-stats` | experiments.tex |
| ✅ | Llama-3.1-8B Complete Results | `sec:appendix-llama` | analysis.tex |
| ❌ | **Additional Visualizations** | `sec:appendix-viz` | 正文无引用 |
| ❌ | **Per-Layer Gate Profile** | `sec:appendix-gate-profile` | 正文无引用 |
| ❌ | **Scheduled Sampling Implementation** | `sec:appendix-ss` | 正文无引用 |
| ❌ | **Computational Cost Analysis** | `sec:appendix-cost` | 正文无引用 |
| ❌ | **Qualitative Steering Examples** | `sec:appendix-examples` | 正文无引用 |
| ❌ | **Gradient Conflict Analysis** | `sec:appendix-gradient` | 正文无引用 |
| ❌ | **Training Data Characteristics** | `sec:appendix-data` | 正文无引用 |
| ❌ | **Exposure Bias Scaling** | `sec:appendix-eb-scaling` | 正文无引用 |
| ❌ | **Per-Turn AR GAR Dynamics** | `sec:appendix-ar-gar-dynamics` | 正文无引用 |
| ❌ | **Use of AI Assistants** | `sec:appendix-ai` | 正文无引用 |
| ✅ | Full Attention Steering Results | `sec:appendix-steering` | experiments.tex |

## == Appendix Tables ==

| Status | Table | Label | Referenced from |
|--------|-------|-------|-----------------|
| ❌ | **Training hyperparameters** | `tab:hyperparams` | 正文无 `\ref` (仅通过 section 引用间接可达) |
| ❌ | **Loss formulation iterations** | `tab:loss-iterations` | 正文无引用 |
| ❌ | **Instruction retention by category** | `tab:ir-results` | 正文无引用 |
| ❌ | **AR GAR on N=5 ten-turn** | `tab:n5-ar` | 正文无引用 |
| ❌ | **Consolidated statistical tests** | `tab:stat-tests` | 正文无引用 |
| ❌ | **Llama complete results** | `tab:llama-full` | 正文无引用 |
| ❌ | **Per-layer gate values** | `tab:gate-profile` | 正文无引用 |
| ❌ | **Computational cost** | `tab:cost` | 正文无引用 |
| ❌ | **Qualitative steering examples** | `tab:examples` | 正文无引用 |
| ❌ | **Training/eval data stats** | `tab:data-stats` | 正文无引用 |
| ❌ | **Full steering results** | `tab:steering-full` | 正文无引用 |

## == Appendix Figures ==

| Status | Figure | Label | Referenced from |
|--------|--------|-------|-----------------|
| ❌ | **Gate profile heatmap** | `fig:gate-heatmap` | 正文无引用 |
| ❌ | **Cross-model gate comparison** | `fig:gate-crossmodel` | 正文无引用 |
| ❌ | **Per-turn AR GAR decay** | `fig:ar-gar-perturn` | 正文无引用 |
| ❌ | **Gate value distributions** | `fig:gate-distribution` | 正文无引用 |
| ❌ | **Training loss curves** | `fig:training-loss` | 正文无引用 |
| ❌ | **Gradient conflict heatmap** | `fig:gradient-heatmap` | 正文无引用 |
| ❌ | **Exposure bias scaling** | `fig:eb-scaling` | 正文无引用 |
| ❌ | **Per-turn AR GAR curves** | `fig:kl_ar_gar_curves` | 正文无引用 |
| ❌ | **Mid-turn AR GAR bar** | `fig:kl_ar_gar_bar` | 正文无引用 |

---

## 总结

- **Sections**: 7/17 有正文引用，**10 个无引用**
- **Tables**: 0/11 有正文直接 `\ref` 引用（所有 table 都只在 appendix 内部被引用）
- **Figures**: 0/9 有正文引用

注意：appendix 内部的 tables/figures 被它们所属的 appendix section 间接覆盖（如 `tab:hyperparams` 在 `sec:appendix-hyper` 中，而该 section 被正文引用）。但严格来说，reviewer 检查可发现性时，**10 个 section** 完全没有正文 pointer，读者无法从正文知道这些附录内容的存在。特别需要关注的高价值未引用 section：

1. **`sec:appendix-cost`** — 计算成本分析，reviewer 常问
2. **`sec:appendix-gradient`** — 梯度冲突分析，支撑 PCGrad 讨论
3. **`sec:appendix-ss`** — 调度采样实现细节
4. **`sec:appendix-data`** — 数据特征，可复现性相关
5. **`sec:appendix-eb-scaling`** — 曝光偏差缩放分析
6. **`sec:appendix-examples`** — 定性示例
7. **`sec:appendix-ai`** — AI 使用声明（部分会议要求）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 73438,
  "duration_api_ms": 74034,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "e42c867e-e425-47f8-a1ea-57c8cf152dad",
  "total_cost_usd": 0.39044724999999997,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 33195,
    "cache_read_input_tokens": 193659,
    "output_tokens": 3390,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33195,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1707,
        "cache_read_input_tokens": 42420,
        "cache_creation_input_tokens": 2222,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2222
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1264,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001359,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 3390,
      "cacheReadInputTokens": 193659,
      "cacheCreationInputTokens": 33195,
      "webSearchRequests": 0,
      "costUSD": 0.38908824999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b9914038-3ee3-4fda-b4c5-02161681aceb"
}
```

</details>

---
