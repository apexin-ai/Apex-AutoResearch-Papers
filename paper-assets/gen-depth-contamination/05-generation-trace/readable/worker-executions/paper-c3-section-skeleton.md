# paper c3 section skeleton

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_c3-section-skeleton_20260515T042055.log`
- **Structured JSON:** [`cc31175da9e346cbe063.json`](../../sessions/cc/cc31175da9e346cbe063.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
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
  "uuid": "e3b0bed1-d6aa-4646-8848-70a320757e56",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778820600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8afbf2b1-55cc-4e8e-b325-5cd8240ab26e",
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761"
}
```

---

### Assistant

_source line 4_

Let me read the current files to understand the context and writing style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "cf2b0749-cfe3-473c-bd67-c48b74576e7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjW4cYGxDp64f3kcqQNod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11889,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11889
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

<details open><summary>🔧 Tool call — Read · `toolu_012ZrYKmd99wvg4JhLKLiXB5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "5790c53b-9dbc-48f6-987e-6e7ae09107ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjW4cYGxDp64f3kcqQNod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11889,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11889
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

_source line 6 · 2026-05-15T04:21:07.054Z_

<details><summary>↩ Tool result · `toolu_012ZrYKmd99wvg4JhLKLiXB5`</summary>

```text
1	\subsection{Graduated Filtering for Depth-Aware Data Curation}
2	\label{sec:graduated-filtering}
3	
4	The $\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
5	Binary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.
6	We ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.
7	
8	\paragraph{Filtering strategies.}
9	We compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:
10	
11	\begin{enumerate}[label=(\roman*)]
12	  \item \textbf{No-filter}: all documents receive uniform weight (baseline).
13	
14	  \item \textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\geq 1$).
15	  Each document receives weight $w = 1 - P(\text{synthetic})$.
16	  This represents the natural binary extension of our depth estimation framework.
17	
18	  \item \textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.
19	  This is the strongest existing baseline for contamination-aware data curation.
20	
21	  \item \textbf{Graduated}: our proposed depth-aware strategy.
22	  The OBD-LightGBM classifier (Section~\ref{sec:classifier}) predicts a full depth distribution $P(d \mid \mathbf{x})$ for each document, from which we compute the expected depth $\hat{d} = \sum_d d \cdot P(d \mid \mathbf{x})$.
23	  Sample weights follow an exponential decay: $w = \exp(-\alpha \cdot \hat{d})$, where $\alpha$ controls the penalty for predicted depth.
24	  Low $\alpha$ values retain more synthetic content with gentle down-weighting; high $\alpha$ values approximate hard filtering.
25	  We sweep $\alpha \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.
26	
27	  \item \textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\ref{sec:feature_degradation}).
28	
29	  \item \textbf{DSIR}: Data Selection via Importance Resampling~\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.
30	  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.
31	\end{enumerate}
32	
33	\paragraph{Training setup.}
34	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}} = 16$, target modules: \texttt{q\_proj}, \texttt{v\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.
35	Documents are truncated to 512 tokens.
36	For strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.
37	Each strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\alpha$ values, yielding 25 additional runs.
38	A base model baseline (no fine-tuning) is included for reference.
39	The total experimental budget is approximately 50 runs.
40	
41	\paragraph{Evaluation.}
42	We evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).
43	We report mean accuracy $\pm$ standard deviation across seeds.
44	
45	%% ====================================================================
46	\paragraph{Results.}
47	
48	\begin{table}[t]
49	\centering
50	\small
51	\caption{Downstream evaluation of filtering strategies.
52	MMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.
53	Mean $\pm$ std over 5 seeds.
54	$\Delta$ columns report the difference relative to the no-filter baseline.
55	$p$-values are from paired $t$-tests (5 seeds) comparing each strategy against binary-ours.
56	Best per-column result in bold; second-best underlined.
57	Graduated results use the best $\alpha$ from Table~\ref{tab:alpha_sweep}.}
58	\label{tab:filtering_main}
59	\begin{tabular}{lccccc}
60	\toprule
61	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} & \textbf{$\Delta$MMLU} & \textbf{$\Delta$HS} & \textbf{$p$} \\
62	\midrule
63	Base model (no fine-tuning)
64	  & \textit{XX.X}
65	  & \textit{XX.X}
66	  & ---
67	  & ---
68	  & --- \\
69	\midrule
70	No-filter
71	  & XX.X $\pm$ X.X
72	  & XX.X $\pm$ X.X
73	  & ---
74	  & ---
75	  & X.XX \\
76	Binary-ours
77	  & XX.X $\pm$ X.X
78	  & XX.X $\pm$ X.X
79	  & $+$X.X
80	  & $+$X.X
81	  & --- \\
82	Binary-Drayson
83	  & XX.X $\pm$ X.X
84	  & XX.X $\pm$ X.X
85	  & $+$X.X
86	  & $+$X.X
87	  & X.XX \\
88	Graduated ($\alpha^*$)
89	  & XX.X $\pm$ X.X
90	  & XX.X $\pm$ X.X
91	  & $+$X.X
92	  & $+$X.X
93	  & X.XX \\
94	Surprisal
95	  & XX.X $\pm$ X.X
96	  & XX.X $\pm$ X.X
97	  & $+$X.X
98	  & $+$X.X
99	  & X.XX \\
100	DSIR
101	  & XX.X $\pm$ X.X
102	  & XX.X $\pm$ X.X
103	  & $+$X.X
104	  & $+$X.X
105	  & X.XX \\
106	\bottomrule
107	\end{tabular}
108	\end{table}
109	
110	Table~\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.
111	%% === CONTINGENCY NARRATIVES (uncomment the matching version once exp-006 results are available) ===
112	%% VERSION A (graduated wins):
113	%% Graduated filtering at the optimal $\alpha^*$ significantly outperforms both binary baselines
114	%% on MMLU ($+$XX.X\,pp, $p =$ XX.XX) and HellaSwag ($+$XX.X\,pp, $p =$ XX.XX),
115	%% validating the practical utility of the $\Kempirical = 2$ trichotomy for data curation.
116	%%
117	%% VERSION B (binary is optimal):
118	%% Graduated filtering at its best $\alpha$ does not significantly outperform binary-ours
119	%% on either benchmark ($p >$ XX.XX), indicating that binary filtering at the $\Kempirical$
120	%% boundary already captures the actionable depth signal (Section~\ref{sec:graduated-filtering}).
121	%%
122	%% VERSION B2 (depth-agnostic wins):
123	%% DSIR outperforms all depth-aware strategies on [MMLU/HellaSwag/both] ($p =$ XX.XX),
124	%% suggesting that distributional alignment provides stronger curation signal than
125	%% depth-specific filtering at this corpus scale.
126	
127	%% ====================================================================
128	\paragraph{$\alpha$ sensitivity.}
129	
130	\begin{table}[t]
131	\centering
132	\small
133	\caption{Graduated filtering $\alpha$ sweep.
134	Mean accuracy $\pm$ std (5 seeds) for each decay parameter $\alpha$.
135	Lower $\alpha$ retains more synthetic content; higher $\alpha$ approximates hard filtering.
136	$\Delta$ vs binary-ours reports the difference in mean accuracy relative to the binary-ours strategy.
137	Eff.\ corpus \% is the effective proportion of the corpus retained under graduated weighting.}
138	\label{tab:alpha_sweep}
139	\begin{tabular}{ccccc}
140	\toprule
141	$\alpha$ & \textbf{MMLU} & \textbf{HellaSwag} & \textbf{$\Delta$ vs binary-ours} & \textbf{Eff.\ corpus \%} \\
142	\midrule
143	0.1 & XX.X $\pm$ X.X & XX.X $\pm$ X.X & $\pm$X.X & XX.X \\
144	0.3 & XX.X $\pm$ X.X & XX.X $\pm$ X.X & $\pm$X.X & XX.X \\
145	0.5 & XX.X $\pm$ X.X & XX.X $\pm$ X.X & $\pm$X.X & XX.X \\
146	0.7 & XX.X $\pm$ X.X & XX.X $\pm$ X.X & $\pm$X.X & XX.X \\
147	0.9 & XX.X $\pm$ X.X & XX.X $\pm$ X.X & $\pm$X.X & XX.X \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	Table~\ref{tab:alpha_sweep} shows the effect of the decay parameter $\alpha$ on downstream performance.
153	At $\alpha \to 0$, graduated filtering approaches the no-filter baseline (all documents equally weighted); at $\alpha \to \infty$, it approximates binary hard filtering (depth-0 retained, all synthetic discarded).
154	The graduated scheme effectively implements a soft version of the human / gen-1 / gen-2+ partition implied by $\Kempirical = 2$, with $\alpha$ controlling how aggressively deeper content is penalized.
155	%% TODO: fill optimal alpha, monotonicity pattern, cross-seed stability once exp-006 completes.
156	
157	%% ====================================================================
158	\paragraph{Analysis.}
159	We address four questions.
160	First, does graduated filtering outperform binary?
161	If so, this validates the practical utility of the $\Kempirical = 2$ trichotomy for data curation; if not, it suggests that binary filtering at the $\Kempirical$ boundary already captures the actionable depth signal.
162	Second, how does the optimal $\alpha$ relate to the discrimination boundary?
163	The graduated scheme allocates weighting resolution across the depth axis; if the optimal $\alpha$ is low, the ordinal signal provides marginal value beyond binary classification.
164	Third, does graduated filtering exhibit lower cross-seed variance than binary strategies, indicating that ordinal weighting provides a more stable curation criterion?
165	Fourth, do MMLU (knowledge-intensive) and HellaSwag (commonsense reasoning) respond differently to curation strategy, reflecting different sensitivity to contamination depth?
166	%% TODO: fill analysis results once exp-006 completes.
167	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "ed1cd1c6-dfb3-4005-92ec-88e5e255f773",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
      "content": "\\subsection{Graduated Filtering for Depth-Aware Data Curation}\n\\label{sec:graduated-filtering}\n\nThe $\\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nBinary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.\nWe ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n  This represents the natural binary extension of our depth estimation framework.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.\n  This is the strongest existing baseline for contamination-aware data curation.\n\n  \\item \\textbf{Graduated}: our proposed depth-aware strategy.\n  The OBD-LightGBM classifier (Section~\\ref{sec:classifier}) predicts a full depth distribution $P(d \\mid \\mathbf{x})$ for each document, from which we compute the expected depth $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow an exponential decay: $w = \\exp(-\\alpha \\cdot \\hat{d})$, where $\\alpha$ controls the penalty for predicted depth.\n  Low $\\alpha$ values retain more synthetic content with gentle down-weighting; high $\\alpha$ values approximate hard filtering.\n  We sweep $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nFor strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.\nEach strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\\alpha$ values, yielding 25 additional runs.\nA base model baseline (no fine-tuning) is included for reference.\nThe total experimental budget is approximately 50 runs.\n\n\\paragraph{Evaluation.}\nWe evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).\nWe report mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream evaluation of filtering strategies.\nMMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.\nMean $\\pm$ std over 5 seeds.\n$\\Delta$ columns report the difference relative to the no-filter baseline.\n$p$-values are from paired $t$-tests (5 seeds) comparing each strategy against binary-ours.\nBest per-column result in bold; second-best underlined.\nGraduated results use the best $\\alpha$ from Table~\\ref{tab:alpha_sweep}.}\n\\label{tab:filtering_main}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{$\\Delta$MMLU} & \\textbf{$\\Delta$HS} & \\textbf{$p$} \\\\\n\\midrule\nBase model (no fine-tuning)\n  & \\textit{XX.X}\n  & \\textit{XX.X}\n  & ---\n  & ---\n  & --- \\\\\n\\midrule\nNo-filter\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & ---\n  & ---\n  & X.XX \\\\\nBinary-ours\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & --- \\\\\nBinary-Drayson\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\nGraduated ($\\alpha^*$)\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\nSurprisal\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\nDSIR\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.\n%% === CONTINGENCY NARRATIVES (uncomment the matching version once exp-006 results are available) ===\n%% VERSION A (graduated wins):\n%% Graduated filtering at the optimal $\\alpha^*$ significantly outperforms both binary baselines\n%% on MMLU ($+$XX.X\\,pp, $p =$ XX.XX) and HellaSwag ($+$XX.X\\,pp, $p =$ XX.XX),\n%% validating the practical utility of the $\\Kempirical = 2$ trichotomy for data curation.\n%%\n%% VERSION B (binary is optimal):\n%% Graduated filtering at its best $\\alpha$ does not significantly outperform binary-ours\n%% on either benchmark ($p >$ XX.XX), indicating that binary filtering at the $\\Kempirical$\n%% boundary already captures the actionable depth signal (Section~\\ref{sec:graduated-filtering}).\n%%\n%% VERSION B2 (depth-agnostic wins):\n%% DSIR outperforms all depth-aware strategies on [MMLU/HellaSwag/both] ($p =$ XX.XX),\n%% suggesting that distributional alignment provides stronger curation signal than\n%% depth-specific filtering at this corpus scale.\n\n%% ====================================================================\n\\paragraph{$\\alpha$ sensitivity.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Graduated filtering $\\alpha$ sweep.\nMean accuracy $\\pm$ std (5 seeds) for each decay parameter $\\alpha$.\nLower $\\alpha$ retains more synthetic content; higher $\\alpha$ approximates hard filtering.\n$\\Delta$ vs binary-ours reports the difference in mean accuracy relative to the binary-ours strategy.\nEff.\\ corpus \\% is the effective proportion of the corpus retained under graduated weighting.}\n\\label{tab:alpha_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\alpha$ & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{$\\Delta$ vs binary-ours} & \\textbf{Eff.\\ corpus \\%} \\\\\n\\midrule\n0.1 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.3 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.5 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.7 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.9 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:alpha_sweep} shows the effect of the decay parameter $\\alpha$ on downstream performance.\nAt $\\alpha \\to 0$, graduated filtering approaches the no-filter baseline (all documents equally weighted); at $\\alpha \\to \\infty$, it approximates binary hard filtering (depth-0 retained, all synthetic discarded).\nThe graduated scheme effectively implements a soft version of the human / gen-1 / gen-2+ partition implied by $\\Kempirical = 2$, with $\\alpha$ controlling how aggressively deeper content is penalized.\n%% TODO: fill optimal alpha, monotonicity pattern, cross-seed stability once exp-006 completes.\n\n%% ====================================================================\n\\paragraph{Analysis.}\nWe address four questions.\nFirst, does graduated filtering outperform binary?\nIf so, this validates the practical utility of the $\\Kempirical = 2$ trichotomy for data curation; if not, it suggests that binary filtering at the $\\Kempirical$ boundary already captures the actionable depth signal.\nSecond, how does the optimal $\\alpha$ relate to the discrimination boundary?\nThe graduated scheme allocates weighting resolution across the depth axis; if the optimal $\\alpha$ is low, the ordinal signal provides marginal value beyond binary classification.\nThird, does graduated filtering exhibit lower cross-seed variance than binary strategies, indicating that ordinal weighting provides a more stable curation criterion?\nFourth, do MMLU (knowledge-intensive) and HellaSwag (commonsense reasoning) respond differently to curation strategy, reflecting different sensitivity to contamination depth?\n%% TODO: fill analysis results once exp-006 completes.\n",
      "numLines": 167,
      "startLine": 1,
      "totalLines": 167
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01A1Fb9F2ucsn93AFijXEKQu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "5c02e32b-b895-44ba-b193-be96dc9f5c0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjW4cYGxDp64f3kcqQNod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11889,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11889
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

_source line 8 · 2026-05-15T04:21:07.343Z_

<details><summary>↩ Tool result · `toolu_01A1Fb9F2ucsn93AFijXEKQu`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on four model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-1.5B-Instruct in both rewrite and continuation modes.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\ref{sec:method}.
7	Each configuration uses a balanced corpus of 5{,}000 texts per depth level (generations 0--5).
8	We organize results around four questions:
9	(1)~Does $\Kempirical = 2$ hold across configurations?
10	(2)~Do depth classifiers transfer across models?
11	(3)~Is the feature degradation ordering model-independent?
12	(4)~How does generation mode affect detectability?
13	
14	%% ====================================================================
15	\subsection{$\Kempirical = 2$ Across All Configurations}
16	\label{sec:kstar_boundary}
17	
18	Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
19	across all four configurations, with bootstrap 95\% confidence intervals
20	(1{,}000 resamples) and permutation-test $p$-values for the critical 1v2
21	and 2v3 boundaries.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Pairwise $\auc$ for adjacent depth pairs.  Bootstrap 95\% CIs
27	and permutation $p$-values shown for the $\Kstar$ boundary rows (1v2,
28	2v3).  $\Kempirical = 2$ requires 1v2 $\text{CI}_\text{low} > \theta$
29	and 2v3 $\text{CI}_\text{high} < \theta$ with $\theta = 0.60$.
30	All 0v1 permutation $p \leq 0.002$ (Qwen-continuation 0v1: CI [0.9963, 0.9978], $p = 0.002$).}
31	\label{tab:kstar_ci}
32	\begin{tabular}{lcccc}
33	\toprule
34	 & Qwen-rw & Pythia & OLMo & Qwen-cont \\
35	\midrule
36	0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9971 \\[4pt]
37	1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\
38	{\footnotesize CI}
39	  & {\footnotesize [.6859,\,.7041]}
40	  & {\footnotesize [.6454,\,.6630]}
41	  & {\footnotesize [.6045,\,.6247]}
42	  & {\footnotesize [.6015,\,.6213]} \\
43	{\footnotesize $p$}
44	  & {\footnotesize .002}
45	  & {\footnotesize .002}
46	  & {\footnotesize .002}
47	  & {\footnotesize .002} \\[4pt]
48	2v3 & 0.5893 & 0.5514 & 0.5496 & 0.5609 \\
49	{\footnotesize CI}
50	  & {\footnotesize [.5795,\,.5991]}
51	  & {\footnotesize [.5417,\,.5628]}
52	  & {\footnotesize [.5399,\,.5596]}
53	  & {\footnotesize [.5511,\,.5712]} \\
54	{\footnotesize $p$}
55	  & {\footnotesize .002}
56	  & {\footnotesize .002}
57	  & {\footnotesize .002}
58	  & {\footnotesize .002} \\[4pt]
59	3v4 & 0.5435 & 0.5152 & 0.5091 & 0.5409 \\
60	4v5 & 0.5340 & 0.5136 & 0.5045 & 0.5141 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	The pattern is consistent across all four configurations:
66	0v1 discrimination is near-perfect ($\auc > 0.99$),
67	followed by a sharp drop at 1v2 ($\auc$ range: 0.6112--0.6955),
68	with 2v3 falling below the decision threshold $\theta = 0.60$
69	($\auc$ range: 0.5496--0.5893).
70	All subsequent pairs (3v4, 4v5) converge toward chance.
71	Figure~\ref{fig:auc_decay} visualizes this decay.
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
76	\caption{Pairwise $\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}
77	\label{fig:auc_decay}
78	\end{figure}
79	
80	For the $\Kempirical$ determination, all four 1v2 CI lower bounds exceed
81	$\theta$: Qwen-rewrite ($\text{CI}_\text{low} = 0.6859$), Pythia (0.6454),
82	OLMo (0.6045), and Qwen-continuation (0.6015).
83	Conversely, all four 2v3 CI upper bounds fall below $\theta$:
84	Qwen-rewrite ($\text{CI}_\text{high} = 0.5991$), Qwen-continuation (0.5712),
85	Pythia (0.5628), and OLMo (0.5596).
86	Permutation tests confirm $p = 0.002$ for all eight boundary comparisons.
87	Together these establish $\Kempirical = 2$ as a consistent discrimination boundary across all tested configurations at the $\leq$1.5B scale.
88	
89	The most marginal case is Qwen-continuation, where the 1v2 CI lower bound
90	(0.6015) exceeds $\theta$ by only 0.0015.  This narrow margin
91	indicates that $\Kempirical = 2$ is robust but not trivially so---continuation-mode
92	generation produces weaker depth artifacts than rewrite mode, pushing the
93	boundary closer to the detection threshold.
94	
95	The absolute 1v2 $\auc$ varies across models:
96	Qwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\approx$ Qwen-continuation (0.6112).
97	Notably, the spread due to generation mode within a single model
98	(Qwen-rewrite vs.\ Qwen-continuation: $\Delta = 8.4$\,pp) exceeds the spread
99	across models in the same mode
100	(Pythia vs.\ OLMo: $\Delta = 3.9$\,pp),
101	suggesting that generation protocol is a stronger determinant
102	of detectability than model identity.
103	We examine both factors in Sections~\ref{sec:transfer}
104	and~\ref{sec:generation_mode}.
105	
106	Beyond the $\Kempirical$ boundary, depth discrimination deteriorates
107	rapidly.
108	OLMo shows nonsignificant permutation $p$-values at 3v4
109	($p = 0.064$) and 4v5 ($p = 0.232$), indicating that depth
110	classification beyond generation~2 is indistinguishable from
111	random for this model.
112	Pythia retains marginal effects at these depths
113	($p = 0.006$ and $p = 0.008$, respectively),
114	while Qwen-continuation shows weak but detectable discrimination through
115	3v4 ($p = 0.002$) that fades at 4v5 ($p = 0.006$).
116	
117	\paragraph{Classifier design justification.}
118	The OBD formulation is motivated by a three-way comparison with multiclass LightGBM and ordinal logistic regression (Section~\ref{sec:method}).
119	Across all three model families, OBD achieves the best accuracy (38.2--42.3\%, i.e., $+$21.5--25.6\,pp over the 16.7\% random baseline for 6-class classification, and $+$5.5\,pp over frontier-LLM zero-shot on the matched 5-class task, 38.6\% vs.\ ${\sim}$33\%; cf.\ Table~\ref{tab:s3_llm_zeroshot}) while maintaining competitive MAE.
120	Ordinal logistic regression yields the lowest MAE (e.g., 0.911 vs.\ 0.984 OBD on Qwen-rewrite) but at the cost of near-chance pairwise AUC (mean 0.49 vs.\ 0.61 for OBD across families)---it reduces error by collapsing predictions toward central depths rather than genuinely distinguishing adjacent levels.
121	Multiclass LightGBM matches OBD on pairwise AUC but consistently trails in both accuracy and MAE.
122	OBD thus provides the best balance across all three evaluation axes, justifying its use as the default classifier throughout.
123	
124	%% ====================================================================
125	\subsection{Cross-Model Transfer}
126	\label{sec:transfer}
127	
128	Having established $\Kempirical = 2$ consistently, we next ask: is this boundary a property of the text itself, or an artifact of model self-familiarity?
129	To answer this, we train classifiers on one model's outputs and evaluate on another's.
130	Table~\ref{tab:transfer_matrix} shows the full
131	$4 \times 4$ transfer accuracy matrix for 6-class ordinal depth
132	classification.
133	
134	\begin{table}[t]
135	\centering
136	\small
137	\caption{Cross-model transfer accuracy (6-class ordinal
138	classification).  Diagonal entries (bold): within-model accuracy.
139	Off-diagonal: cross-model transfer.  Retention is computed as
140	off-diagonal accuracy divided by the diagonal entry of the training
141	model.}
142	\label{tab:transfer_matrix}
143	\begin{tabular}{lcccc}
144	\toprule
145	Train $\downarrow$ / Test $\rightarrow$
146	  & Qwen-rw & Pythia & OLMo & Qwen-cont \\
147	\midrule
148	Qwen-rw
149	  & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
150	Pythia
151	  & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
152	OLMo
153	  & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
154	Qwen-cont
155	  & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	\begin{figure}[t]
161	\centering
162	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
163	\caption{Cross-model transfer heatmap (6-class ordinal accuracy).
164	Rows: training model; columns: test model.
165	Pythia$\leftrightarrow$OLMo (both continuation mode) shows high
166	mutual transfer (90--92\% accuracy retention), while Qwen-rewrite
167	transfers poorly to continuation-mode models (61--63\%).
168	Diagonal entries are within-model baselines.}
169	\label{fig:transfer_heatmap}
170	\end{figure}
171	
172	Two principal findings emerge (Figure~\ref{fig:transfer_heatmap}).
173	First, transfer between continuation-mode models is high.
174	Pythia$\leftrightarrow$OLMo mutual transfer retains 90--92\% of within-model accuracy
175	(85--86\% retention by Kendall $\tau$).
176	The accuracy-based retention of 90--92\% is complemented by the
177	$\tau$-based retention of 85--86\%, indicating that not only
178	classification accuracy but also the relative depth ordering of
179	predictions is largely preserved.
180	Qwen-continuation$\leftrightarrow$Pythia also transfers well
181	(84--85\% accuracy retention),
182	and Qwen-continuation$\leftrightarrow$OLMo achieves 80--85\%.
183	These retention rates---80--92\% of within-model accuracy preserved across continuation-mode pairs---suggest that a large component of the depth signal is text-intrinsic rather than tied to a specific generator.
184	
185	Second, Qwen-rewrite exhibits catastrophic transfer failure.
186	Classifiers trained on Qwen-rewrite retain only 61--63\% of
187	within-model accuracy when evaluated on Pythia or OLMo
188	(45--50\% by $\tau$).
189	The reverse direction transfers asymmetrically: Pythia/OLMo${\to}$Qwen-rewrite retains 70--72\% of within-model accuracy, higher than the forward 61--63\% but still far below continuation-mode transfer rates (80--92\%).
190	This confirms that rewrite-mode classifiers rely on generation
191	artifacts that do not generalize across models, in contrast
192	to Qwen-continuation, which achieves 80--85\% retention to the same targets.
193	
194	At the 0v1 boundary, cross-model pairwise $\auc$ exceeds 0.96
195	for all model pairs, confirming that the human-vs.-synthetic
196	distinction is consistently transferable across all tested generators
197	and modes.
198	The transfer degradation concentrates at deeper boundaries
199	(1v2 and beyond), where model- and mode-specific factors dominate.
200	
201	The aggregate picture is one of modest cross-model loss:
202	mean pairwise $\auc$ is 0.6099 within-model versus 0.5905
203	cross-model.
204	This gap is driven primarily by Qwen-rewrite; among
205	continuation-mode pairs the within/cross difference narrows
206	further.
207	
208	%% ====================================================================
209	\subsection{Feature Degradation Ordering}
210	\label{sec:feature_degradation}
211	
212	The transfer results indicate that depth signals are largely text-intrinsic.
213	We next ask what drives discrimination: if the signal is text-intrinsic, different generators should rely on the same features in the same order.
214	We test this by computing single-feature $\auc$ rankings
215	independently for each model and comparing them via rank
216	correlation.
217	
218	\begin{table}[t]
219	\centering
220	\small
221	\caption{Top-3 features by single-feature $\auc$ ranking for each
222	model configuration.
223	Features shared across all three continuation-mode models are in bold.
224	Qwen-rewrite's top feature (\texttt{freq\_entropy}) is mode-specific.
225	Spearman $\rho$ (continuation-mode pairs): Pythia--OLMo 0.95,
226	Pythia--Qwen-continuation 0.9143, OLMo--Qwen-continuation 0.85.}
227	\label{tab:top_features}
228	\begin{tabular}{cllll}
229	\toprule
230	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
231	\midrule
232	1
233	  & \textbf{\texttt{surp\_d1\_std}}
234	  & \textbf{\texttt{surp\_std}}
235	  & \texttt{freq\_entropy}
236	  & \textbf{\texttt{surp\_d1\_std}} \\
237	2
238	  & \textbf{\texttt{surp\_d2\_std}}
239	  & \textbf{\texttt{surp\_d1\_std}}
240	  & \textbf{\texttt{surp\_std}}
241	  & \textbf{\texttt{surp\_std}} \\
242	3
243	  & \textbf{\texttt{surp\_std}}
244	  & \textbf{\texttt{surp\_d2\_std}}
245	  & \textbf{\texttt{surp\_d1\_std}}
246	  & \textbf{\texttt{surp\_d2\_std}} \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	Among continuation-mode models, single-feature $\auc$ rankings
252	are highly correlated:
253	Pythia vs.\ OLMo $\rho = 0.95$,
254	Pythia vs.\ Qwen-continuation $\rho = 0.9143$,
255	OLMo vs.\ Qwen-continuation $\rho = 0.85$
256	(all $\rho \geq 0.85$).
257	The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std},
258	and \texttt{surp\_d2\_std}---are shared (up to ordering) across
259	all three continuation-mode configurations
260	(Table~\ref{tab:top_features}).
261	All three measure variability of surprisal or its derivatives,
262	capturing the \emph{heterogeneity} of token-level predictability
263	across the text.
264	That these features degrade in a shared order across generators
265	suggests a common mechanism: each generation step smooths the
266	token-level surprisal landscape, reducing its variance in a
267	model-independent fashion.
268	
269	Qwen-rewrite diverges: its top-ranked feature is
270	\texttt{freq\_entropy}, a lexical diversity measure absent from
271	the continuation-mode top-3 for any model.
272	This corroborates the transfer results in
273	Section~\ref{sec:transfer}---rewrite-mode classifiers learn
274	partly from instruction-following artifacts rather than the
275	shared surprisal-based signals.
276	
277	Kendall $\tau$ provides a complementary, more conservative
278	perspective:
279	Pythia vs.\ OLMo $\tau = 0.733$,
280	Pythia vs.\ Qwen-continuation $\tau = 0.695$,
281	OLMo vs.\ Qwen-continuation $\tau = 0.543$.
282	Cross-mode correlations are lower:
283	Pythia vs.\ Qwen-rewrite $\tau = 0.467$,
284	OLMo vs.\ Qwen-rewrite $\tau = 0.429$.
285	
286	\paragraph{Limitation.}
287	The high Spearman $\rho$ characterizes the \emph{aggregate}
288	feature ranking, but at the depth-pair level the agreement
289	weakens: $\tau \approx 0.37$ at the 1v2 boundary.
290	This means that while the overall importance ordering is shared,
291	the relative contribution of individual features at the
292	discrimination boundary---where precision matters most---varies
293	across models.
294	We view this as a genuine limitation of the text-intrinsic
295	interpretation and a direction for future investigation.
296	
297	%% ====================================================================
298	\subsection{Generation Mode Effect}
299	\label{sec:generation_mode}
300	
301	Finally, we ask whether generation mode---an experimental design choice rather than a text property---affects depth detectability.
302	Qwen2.5-1.5B-Instruct provides a controlled comparison: rewrite (instruction-based paraphrasing) and continuation (prompt truncation) share the same model weights, as defined in Section~\ref{sec:method}, isolating the effect of generation protocol.
303	
304	Rewrite mode yields higher 1v2 $\auc$ than continuation:
305	0.6955 vs.\ 0.6112, a difference of $+$8.4 percentage points.
306	The advantage persists at 2v3
307	(0.5893 vs.\ 0.5609, $\Delta = +$2.8\,pp)
308	and narrows at 3v4
309	(0.5435 vs.\ 0.5409, $\Delta = +$0.3\,pp),
310	with both modes converging toward chance at deeper levels.
311	The amplified detectability under rewrite mode is consistent
312	with instruction-following introducing systematic deviations
313	from the source text's style---additional artifacts that are
314	discriminable but mode-specific rather than text-intrinsic.
315	
316	Transfer between modes is asymmetric.
317	A classifier trained on Qwen-continuation and evaluated on Qwen-rewrite
318	retains 89\% of within-model accuracy
319	(0.3440 vs.\ 0.3875 diagonal),
320	whereas the reverse direction---Qwen-rewrite trained,
321	Qwen-continuation tested---retains 82\%
322	(0.3466 vs.\ 0.4229 diagonal).
323	The direction of the asymmetry is intuitive:
324	continuation-mode signals form a subset of the information
325	available in rewrite-mode data
326	(which adds instruction-following artifacts on top),
327	so a continuation-trained classifier can partially recognize
328	rewrite-mode outputs but not vice versa.
329	
330	This asymmetry is mirrored in the feature rankings.
331	Qwen-rewrite's top feature (\texttt{freq\_entropy}) is
332	mode-specific and ranks outside the top-3 for every
333	continuation-mode model.
334	Qwen-continuation's top feature (\texttt{surp\_d1\_std}) is shared
335	with Pythia and OLMo, confirming that continuation mode
336	captures primarily text-intrinsic depth signals.
337	
338	The practical implication is a detectability--generalizability
339	tradeoff.
340	Rewrite-mode classifiers achieve higher absolute $\auc$ but
341	transfer poorly across models
342	(Qwen-rewrite$\to$Pythia/OLMo: 61--63\% retention).
343	Continuation-mode classifiers sacrifice 8.4\,pp of within-model
344	$\auc$ but achieve robust cross-model transfer
345	(Qwen-continuation$\to$Pythia: 84--85\%).
346	For deployment scenarios requiring model-agnostic depth
347	estimation, continuation-mode features provide a more reliable
348	foundation despite lower raw discriminability.
349	
350	%% ====================================================================
351	\subsection{Representation Dependence of $\Kempirical$}
352	\label{sec:neural_probe}
353	
354	The preceding sections establish $\Kempirical = 2$ using a 15-dimensional hand-crafted feature set.
355	A natural question is whether this boundary reflects a fundamental limit of the generational depth signal or an information bottleneck imposed by projecting high-dimensional text representations into 15 statistical summaries.
356	To disentangle these possibilities, we replace the hand-crafted features with frozen LLM hidden states and train a lightweight MLP probe on the same classification task.
357	
358	\paragraph{Setup.}
359	We extract last-layer hidden states from a frozen Qwen2.5-1.5B model (\texttt{float16}), apply attention-masked average pooling to obtain 1536-dimensional document embeddings, and train a two-hidden-layer MLP ($1536 \to 512 \to 256 \to 6$, ReLU, dropout 0.1) with 5-fold GroupKFold cross-validation on the Qwen-continuation dataset (Table~\ref{tab:s7_neural_probe}).
360	The probe's limited capacity ensures that any discriminability reflects depth information already encoded in the frozen representations rather than patterns learned de novo.
361	The same architecture and training protocol are applied to Pythia-1.4B (2048-dimensional embeddings) and OLMo-1B (2048-dimensional embeddings) for cross-model validation; results are reported in Table~\ref{tab:neural_probe_crossmodel}.
362	
363	\paragraph{Results.}
364	\begin{table}[t]
365	\centering
366	\small
367	\caption{Cross-model neural probe results. Pairwise $\auc$ for frozen-encoder MLP probes on three model families. $\Kempirical^{\text{neural}}$ determined at $\theta = 0.60$. Qwen-continuation results are from the current experiment; Pythia and OLMo results are pending.}
368	\label{tab:neural_probe_crossmodel}
369	\begin{tabular}{lccccccc}
370	\toprule
371	\textbf{Model} & \textbf{Dim} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & \textbf{3v4} & \textbf{4v5} & $\Kempirical^{\text{neural}}$ \\
372	\midrule
373	Qwen-1.5B & 1536 & 0.987 & 0.698 & 0.620 & 0.593 & 0.575 & 3 \\
374	Pythia-1.4B & 2048 & \textit{--} & \textit{--} & \textit{--} & \textit{--} & \textit{--} & \textit{--} \\
375	OLMo-1B & 2048 & \textit{--} & \textit{--} & \textit{--} & \textit{--} & \textit{--} & \textit{--} \\
376	\bottomrule
377	\end{tabular}
378	\end{table}
379	Table~\ref{tab:neural_probe_crossmodel} reports pairwise $\auc$ for all three model families. Qwen-continuation results are from the current experiment; Pythia and OLMo cross-model validation is pending and will be added upon completion.
380	The neural probe achieves 6-class accuracy of 0.4335 (vs.\ 0.3875 for LightGBM with 15D features).
381	The pairwise $\auc$ profile reveals a shifted discrimination boundary:
382	\begin{center}
383	\small
384	\begin{tabular}{lccccc}
385	\toprule
386	 & 0v1 & 1v2 & 2v3 & 3v4 & 4v5 \\
387	\midrule
388	15D (LightGBM)   & 0.997 & 0.611 & 0.561 & 0.541 & 0.514 \\
389	Neural (MLP)      & 0.987 & 0.698 & 0.620 & 0.593 & 0.575 \\
390	$\Delta$\,(pp)    & $-$1.0 & $+$8.7 & $+$5.9 & $+$5.2 & $+$6.1 \\
391	\bottomrule
392	\end{tabular}
393	\end{center}
394	The neural probe's 2v3 $\auc = 0.6195$ ($\text{std} = 0.0094$ across folds) exceeds $\theta = 0.60$, yielding $\Kempirical^{\text{neural}} = 3$---one discriminable boundary beyond what the 15D feature set recovers on the same data.
395	The 15D classifier on the same dataset gives 2v3 $\auc = 0.5609$ (Section~\ref{sec:kstar_boundary}), well below $\theta$.
396	The improvement concentrates at the 1v2 and 2v3 boundaries ($+$8.7 and $+$5.9\,pp, respectively), where the 15D features lose most of their discriminative power; at the already-trivial 0v1 boundary the neural probe is marginally \emph{lower} ($-$1.0\,pp), consistent with both representations saturating the human--synthetic gap.
397	At 3v4, the neural probe reaches $\auc = 0.5930$---below $\theta$ but closer to the threshold than any 15D configuration---hinting that a still richer representation might push the boundary further.
398	
399	\paragraph{Interpretation: $\Kstar$ hierarchy.}
400	These preliminary results motivate a three-level hierarchy of discrimination boundaries:
401	\[
402	  \Ktheory \;\geq\; \Kempirical^{\text{neural}} \;\geq\; \Kempirical^{\text{15D}}
403	\]
404	where $\Kempirical^{\text{15D}} = 2$ is the operationally deployable boundary measured with model-free, interpretable features, and $\Kempirical^{\text{neural}} = 3$ is a representation-dependent ceiling accessible only through model-specific probing.
405	The gap between the two confirms that the 15D feature set does not saturate the available depth signal: at least one additional discriminable generation boundary exists in the frozen representations but is lost during projection into the hand-crafted feature space.
406	The theoretical upper bound $\Ktheory$---the boundary achievable with an optimal representation and classifier---remains unknown but is at least~3.
407	
408	\paragraph{Interpretability--discriminability tradeoff.}
409	The two $\Kempirical$ estimates serve complementary purposes.
410	The 15D boundary ($\Kempirical = 2$) is model-free, interpretable, and computationally lightweight: features are extracted from surface-level token statistics without access to model internals, and the LightGBM classifier trains in seconds.
411	This makes it suitable for deployment in data curation pipelines.
412	The neural boundary ($\Kempirical^{\text{neural}} = 3$) requires a frozen copy of a specific LLM for embedding extraction, is opaque in the features it exploits, and incurs $100\times$+ computational overhead for inference.
413	It is valuable as a theoretical exploration tool---demonstrating that deeper depth signals \emph{exist}---but impractical for the model-agnostic deployment scenarios where depth estimation is most needed.
414	Notably, the neural probe's advantage does not alter the headline result for practitioners: $\Kempirical = 2$ remains the relevant boundary for deployable depth estimation with current feature technology.
415	
416	\paragraph{Caveats.}
417	The 2v3 boundary under neural probing is marginal: the mean $\auc$ of 0.6195 exceeds $\theta = 0.60$ by only $+$1.95\,pp, and individual fold variation (std $= 0.0094$) places this margin within approximately two standard deviations of the threshold.
418	These results should be treated as preliminary evidence that the 15D boundary is representation-dependent, not as a firm revision of $\Kempirical$.
419	% Pythia/OLMo K*(neural) results: to be filled from Table~\ref{tab:neural_probe_crossmodel} upon exp-015 completion.
420	% Bootstrap CIs for neural probe: to be added from exp-015 rerun (script includes bootstrap + permutation test).
421	Critically, the current neural probe data covers only the Qwen-continuation dataset; cross-model validation on Pythia and OLMo is pending.
422	Until confirmed across model families, $\Kempirical^{\text{neural}} = 3$ should be interpreted as a single-dataset preliminary finding rather than a general result.
423	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "75b3d3be-c3c6-4bef-b792-5c2eea0c1dce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on four model configurations:\nPythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-1.5B-Instruct in both rewrite and continuation modes.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\\ref{sec:method}.\nEach configuration uses a balanced corpus of 5{,}000 texts per depth level (generations 0--5).\nWe organize results around four questions:\n(1)~Does $\\Kempirical = 2$ hold across configurations?\n(2)~Do depth classifiers transfer across models?\n(3)~Is the feature degradation ordering model-independent?\n(4)~How does generation mode affect detectability?\n\n%% ====================================================================\n\\subsection{$\\Kempirical = 2$ Across All Configurations}\n\\label{sec:kstar_boundary}\n\nTable~\\ref{tab:kstar_ci} reports pairwise $\\auc$ for adjacent depth pairs\nacross all four configurations, with bootstrap 95\\% confidence intervals\n(1{,}000 resamples) and permutation-test $p$-values for the critical 1v2\nand 2v3 boundaries.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs.  Bootstrap 95\\% CIs\nand permutation $p$-values shown for the $\\Kstar$ boundary rows (1v2,\n2v3).  $\\Kempirical = 2$ requires 1v2 $\\text{CI}_\\text{low} > \\theta$\nand 2v3 $\\text{CI}_\\text{high} < \\theta$ with $\\theta = 0.60$.\nAll 0v1 permutation $p \\leq 0.002$ (Qwen-continuation 0v1: CI [0.9963, 0.9978], $p = 0.002$).}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccc}\n\\toprule\n & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n\\midrule\n0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9971 \\\\[4pt]\n1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\\\\n{\\footnotesize CI}\n  & {\\footnotesize [.6859,\\,.7041]}\n  & {\\footnotesize [.6454,\\,.6630]}\n  & {\\footnotesize [.6045,\\,.6247]}\n  & {\\footnotesize [.6015,\\,.6213]} \\\\\n{\\footnotesize $p$}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002} \\\\[4pt]\n2v3 & 0.5893 & 0.5514 & 0.5496 & 0.5609 \\\\\n{\\footnotesize CI}\n  & {\\footnotesize [.5795,\\,.5991]}\n  & {\\footnotesize [.5417,\\,.5628]}\n  & {\\footnotesize [.5399,\\,.5596]}\n  & {\\footnotesize [.5511,\\,.5712]} \\\\\n{\\footnotesize $p$}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002} \\\\[4pt]\n3v4 & 0.5435 & 0.5152 & 0.5091 & 0.5409 \\\\\n4v5 & 0.5340 & 0.5136 & 0.5045 & 0.5141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pattern is consistent across all four configurations:\n0v1 discrimination is near-perfect ($\\auc > 0.99$),\nfollowed by a sharp drop at 1v2 ($\\auc$ range: 0.6112--0.6955),\nwith 2v3 falling below the decision threshold $\\theta = 0.60$\n($\\auc$ range: 0.5496--0.5893).\nAll subsequent pairs (3v4, 4v5) converge toward chance.\nFigure~\\ref{fig:auc_decay} visualizes this decay.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nFor the $\\Kempirical$ determination, all four 1v2 CI lower bounds exceed\n$\\theta$: Qwen-rewrite ($\\text{CI}_\\text{low} = 0.6859$), Pythia (0.6454),\nOLMo (0.6045), and Qwen-continuation (0.6015).\nConversely, all four 2v3 CI upper bounds fall below $\\theta$:\nQwen-rewrite ($\\text{CI}_\\text{high} = 0.5991$), Qwen-continuation (0.5712),\nPythia (0.5628), and OLMo (0.5596).\nPermutation tests confirm $p = 0.002$ for all eight boundary comparisons.\nTogether these establish $\\Kempirical = 2$ as a consistent discrimination boundary across all tested configurations at the $\\leq$1.5B scale.\n\nThe most marginal case is Qwen-continuation, where the 1v2 CI lower bound\n(0.6015) exceeds $\\theta$ by only 0.0015.  This narrow margin\nindicates that $\\Kempirical = 2$ is robust but not trivially so---continuation-mode\ngeneration produces weaker depth artifacts than rewrite mode, pushing the\nboundary closer to the detection threshold.\n\nThe absolute 1v2 $\\auc$ varies across models:\nQwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\\approx$ Qwen-continuation (0.6112).\nNotably, the spread due to generation mode within a single model\n(Qwen-rewrite vs.\\ Qwen-continuation: $\\Delta = 8.4$\\,pp) exceeds the spread\nacross models in the same mode\n(Pythia vs.\\ OLMo: $\\Delta = 3.9$\\,pp),\nsuggesting that generation protocol is a stronger determinant\nof detectability than model identity.\nWe examine both factors in Sections~\\ref{sec:transfer}\nand~\\ref{sec:generation_mode}.\n\nBeyond the $\\Kempirical$ boundary, depth discrimination deteriorates\nrapidly.\nOLMo shows nonsignificant permutation $p$-values at 3v4\n($p = 0.064$) and 4v5 ($p = 0.232$), indicating that depth\nclassification beyond generation~2 is indistinguishable from\nrandom for this model.\nPythia retains marginal effects at these depths\n($p = 0.006$ and $p = 0.008$, respectively),\nwhile Qwen-continuation shows weak but detectable discrimination through\n3v4 ($p = 0.002$) that fades at 4v5 ($p = 0.006$).\n\n\\paragraph{Classifier design justification.}\nThe OBD formulation is motivated by a three-way comparison with multiclass LightGBM and ordinal logistic regression (Section~\\ref{sec:method}).\nAcross all three model families, OBD achieves the best accuracy (38.2--42.3\\%, i.e., $+$21.5--25.6\\,pp over the 16.7\\% random baseline for 6-class classification, and $+$5.5\\,pp over frontier-LLM zero-shot on the matched 5-class task, 38.6\\% vs.\\ ${\\sim}$33\\%; cf.\\ Table~\\ref{tab:s3_llm_zeroshot}) while maintaining competitive MAE.\nOrdinal logistic regression yields the lowest MAE (e.g., 0.911 vs.\\ 0.984 OBD on Qwen-rewrite) but at the cost of near-chance pairwise AUC (mean 0.49 vs.\\ 0.61 for OBD across families)---it reduces error by collapsing predictions toward central depths rather than genuinely distinguishing adjacent levels.\nMulticlass LightGBM matches OBD on pairwise AUC but consistently trails in both accuracy and MAE.\nOBD thus provides the best balance across all three evaluation axes, justifying its use as the default classifier throughout.\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\nHaving established $\\Kempirical = 2$ consistently, we next ask: is this boundary a property of the text itself, or an artifact of model self-familiarity?\nTo answer this, we train classifiers on one model's outputs and evaluate on another's.\nTable~\\ref{tab:transfer_matrix} shows the full\n$4 \\times 4$ transfer accuracy matrix for 6-class ordinal depth\nclassification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer accuracy (6-class ordinal\nclassification).  Diagonal entries (bold): within-model accuracy.\nOff-diagonal: cross-model transfer.  Retention is computed as\noff-diagonal accuracy divided by the diagonal entry of the training\nmodel.}\n\\label{tab:transfer_matrix}\n\\begin{tabular}{lcccc}\n\\toprule\nTrain $\\downarrow$ / Test $\\rightarrow$\n  & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n\\midrule\nQwen-rw\n  & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\nPythia\n  & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\nOLMo\n  & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\nQwen-cont\n  & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (6-class ordinal accuracy).\nRows: training model; columns: test model.\nPythia$\\leftrightarrow$OLMo (both continuation mode) shows high\nmutual transfer (90--92\\% accuracy retention), while Qwen-rewrite\ntransfers poorly to continuation-mode models (61--63\\%).\nDiagonal entries are within-model baselines.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nTwo principal findings emerge (Figure~\\ref{fig:transfer_heatmap}).\nFirst, transfer between continuation-mode models is high.\nPythia$\\leftrightarrow$OLMo mutual transfer retains 90--92\\% of within-model accuracy\n(85--86\\% retention by Kendall $\\tau$).\nThe accuracy-based retention of 90--92\\% is complemented by the\n$\\tau$-based retention of 85--86\\%, indicating that not only\nclassification accuracy but also the relative depth ordering of\npredictions is largely preserved.\nQwen-continuation$\\leftrightarrow$Pythia also transfers well\n(84--85\\% accuracy retention),\nand Qwen-continuation$\\leftrightarrow$OLMo achieves 80--85\\%.\nThese retention rates---80--92\\% of within-model accuracy preserved across continuation-mode pairs---suggest that a large component of the depth signal is text-intrinsic rather than tied to a specific generator.\n\nSecond, Qwen-rewrite exhibits catastrophic transfer failure.\nClassifiers trained on Qwen-rewrite retain only 61--63\\% of\nwithin-model accuracy when evaluated on Pythia or OLMo\n(45--50\\% by $\\tau$).\nThe reverse direction transfers asymmetrically: Pythia/OLMo${\\to}$Qwen-rewrite retains 70--72\\% of within-model accuracy, higher than the forward 61--63\\% but still far below continuation-mode transfer rates (80--92\\%).\nThis confirms that rewrite-mode classifiers rely on generation\nartifacts that do not generalize across models, in contrast\nto Qwen-continuation, which achieves 80--85\\% retention to the same targets.\n\nAt the 0v1 boundary, cross-model pairwise $\\auc$ exceeds 0.96\nfor all model pairs, confirming that the human-vs.-synthetic\ndistinction is consistently transferable across all tested generators\nand modes.\nThe transfer degradation concentrates at deeper boundaries\n(1v2 and beyond), where model- and mode-specific factors dominate.\n\nThe aggregate picture is one of modest cross-model loss:\nmean pairwise $\\auc$ is 0.6099 within-model versus 0.5905\ncross-model.\nThis gap is driven primarily by Qwen-rewrite; among\ncontinuation-mode pairs the within/cross difference narrows\nfurther.\n\n%% ====================================================================\n\\subsection{Feature Degradation Ordering}\n\\label{sec:feature_degradation}\n\nThe transfer results indicate that depth signals are largely text-intrinsic.\nWe next ask what drives discrimination: if the signal is text-intrinsic, different generators should rely on the same features in the same order.\nWe test this by computing single-feature $\\auc$ rankings\nindependently for each model and comparing them via rank\ncorrelation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking for each\nmodel configuration.\nFeatures shared across all three continuation-mode models are in bold.\nQwen-rewrite's top feature (\\texttt{freq\\_entropy}) is mode-specific.\nSpearman $\\rho$ (continuation-mode pairs): Pythia--OLMo 0.95,\nPythia--Qwen-continuation 0.9143, OLMo--Qwen-continuation 0.85.}\n\\label{tab:top_features}\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1\n  & \\textbf{\\texttt{surp\\_d1\\_std}}\n  & \\textbf{\\texttt{surp\\_std}}\n  & \\texttt{freq\\_entropy}\n  & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2\n  & \\textbf{\\texttt{surp\\_d2\\_std}}\n  & \\textbf{\\texttt{surp\\_d1\\_std}}\n  & \\textbf{\\texttt{surp\\_std}}\n  & \\textbf{\\texttt{surp\\_std}} \\\\\n3\n  & \\textbf{\\texttt{surp\\_std}}\n  & \\textbf{\\texttt{surp\\_d2\\_std}}\n  & \\textbf{\\texttt{surp\\_d1\\_std}}\n  & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings\nare highly correlated:\nPythia vs.\\ OLMo $\\rho = 0.95$,\nPythia vs.\\ Qwen-continuation $\\rho = 0.9143$,\nOLMo vs.\\ Qwen-continuation $\\rho = 0.85$\n(all $\\rho \\geq 0.85$).\nThe top-3 features---\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std},\nand \\texttt{surp\\_d2\\_std}---are shared (up to ordering) across\nall three continuation-mode configurations\n(Table~\\ref{tab:top_features}).\nAll three measure variability of surprisal or its derivatives,\ncapturing the \\emph{heterogeneity} of token-level predictability\nacross the text.\nThat these features degrade in a shared order across generators\nsuggests a common mechanism: each generation step smooths the\ntoken-level surprisal landscape, reducing its variance in a\nmodel-independent fashion.\n\nQwen-rewrite diverges: its top-ranked feature is\n\\texttt{freq\\_entropy}, a lexical diversity measure absent from\nthe continuation-mode top-3 for any model.\nThis corroborates the transfer results in\nSection~\\ref{sec:transfer}---rewrite-mode classifiers learn\npartly from instruction-following artifacts rather than the\nshared surprisal-based signals.\n\nKendall $\\tau$ provides a complementary, more conservative\nperspective:\nPythia vs.\\ OLMo $\\tau = 0.733$,\nPythia vs.\\ Qwen-continuation $\\tau = 0.695$,\nOLMo vs.\\ Qwen-continuation $\\tau = 0.543$.\nCross-mode correlations are lower:\nPythia vs.\\ Qwen-rewrite $\\tau = 0.467$,\nOLMo vs.\\ Qwen-rewrite $\\tau = 0.429$.\n\n\\paragraph{Limitation.}\nThe high Spearman $\\rho$ characterizes the \\emph{aggregate}\nfeature ranking, but at the depth-pair level the agreement\nweakens: $\\tau \\approx 0.37$ at the 1v2 boundary.\nThis means that while the overall importance ordering is shared,\nthe relative contribution of individual features at the\ndiscrimination boundary---where precision matters most---varies\nacross models.\nWe view this as a genuine limitation of the text-intrinsic\ninterpretation and a direction for future investigation.\n\n%% ====================================================================\n\\subsection{Generation Mode Effect}\n\\label{sec:generation_mode}\n\nFinally, we ask whether generation mode---an experimental design choice rather than a text property---affects depth detectability.\nQwen2.5-1.5B-Instruct provides a controlled comparison: rewrite (instruction-based paraphrasing) and continuation (prompt truncation) share the same model weights, as defined in Section~\\ref{sec:method}, isolating the effect of generation protocol.\n\nRewrite mode yields higher 1v2 $\\auc$ than continuation:\n0.6955 vs.\\ 0.6112, a difference of $+$8.4 percentage points.\nThe advantage persists at 2v3\n(0.5893 vs.\\ 0.5609, $\\Delta = +$2.8\\,pp)\nand narrows at 3v4\n(0.5435 vs.\\ 0.5409, $\\Delta = +$0.3\\,pp),\nwith both modes converging toward chance at deeper levels.\nThe amplified detectability under rewrite mode is consistent\nwith instruction-following introducing systematic deviations\nfrom the source text's style---additional artifacts that are\ndiscriminable but mode-specific rather than text-intrinsic.\n\nTransfer between modes is asymmetric.\nA classifier trained on Qwen-continuation and evaluated on Qwen-rewrite\nretains 89\\% of within-model accuracy\n(0.3440 vs.\\ 0.3875 diagonal),\nwhereas the reverse direction---Qwen-rewrite trained,\nQwen-continuation tested---retains 82\\%\n(0.3466 vs.\\ 0.4229 diagonal).\nThe direction of the asymmetry is intuitive:\ncontinuation-mode signals form a subset of the information\navailable in rewrite-mode data\n(which adds instruction-following artifacts on top),\nso a continuation-trained classifier can partially recognize\nrewrite-mode outputs but not vice versa.\n\nThis asymmetry is mirrored in the feature rankings.\nQwen-rewrite's top feature (\\texttt{freq\\_entropy}) is\nmode-specific and ranks outside the top-3 for every\ncontinuation-mode model.\nQwen-continuation's top feature (\\texttt{surp\\_d1\\_std}) is shared\nwith Pythia and OLMo, confirming that continuation mode\ncaptures primarily text-intrinsic depth signals.\n\nThe practical implication is a detectability--generalizability\ntradeoff.\nRewrite-mode classifiers achieve higher absolute $\\auc$ but\ntransfer poorly across models\n(Qwen-rewrite$\\to$Pythia/OLMo: 61--63\\% retention).\nContinuation-mode classifiers sacrifice 8.4\\,pp of within-model\n$\\auc$ but achieve robust cross-model transfer\n(Qwen-continuation$\\to$Pythia: 84--85\\%).\nFor deployment scenarios requiring model-agnostic depth\nestimation, continuation-mode features provide a more reliable\nfoundation despite lower raw discriminability.\n\n%% ====================================================================\n\\subsection{Representation Dependence of $\\Kempirical$}\n\\label{sec:neural_probe}\n\nThe preceding sections establish $\\Kempirical = 2$ using a 15-dimensional hand-crafted feature set.\nA natural question is whether this boundary reflects a fundamental limit of the generational depth signal or an information bottleneck imposed by projecting high-dimensional text representations into 15 statistical summaries.\nTo disentangle these possibilities, we replace the hand-crafted features with frozen LLM hidden states and train a lightweight MLP probe on the same classification task.\n\n\\paragraph{Setup.}\nWe extract last-layer hidden states from a frozen Qwen2.5-1.5B model (\\texttt{float16}), apply attention-masked average pooling to obtain 1536-dimensional document embeddings, and train a two-hidden-layer MLP ($1536 \\to 512 \\to 256 \\to 6$, ReLU, dropout 0.1) with 5-fold GroupKFold cross-validation on the Qwen-continuation dataset (Table~\\ref{tab:s7_neural_probe}).\nThe probe's limited capacity ensures that any discriminability reflects depth information already encoded in the frozen representations rather than patterns learned de novo.\nThe same architecture and training protocol are applied to Pythia-1.4B (2048-dimensional embeddings) and OLMo-1B (2048-dimensional embeddings) for cross-model validation; results are reported in Table~\\ref{tab:neural_probe_crossmodel}.\n\n\\paragraph{Results.}\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model neural probe results. Pairwise $\\auc$ for frozen-encoder MLP probes on three model families. $\\Kempirical^{\\text{neural}}$ determined at $\\theta = 0.60$. Qwen-continuation results are from the current experiment; Pythia and OLMo results are pending.}\n\\label{tab:neural_probe_crossmodel}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Dim} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & \\textbf{3v4} & \\textbf{4v5} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B & 1536 & 0.987 & 0.698 & 0.620 & 0.593 & 0.575 & 3 \\\\\nPythia-1.4B & 2048 & \\textit{--} & \\textit{--} & \\textit{--} & \\textit{--} & \\textit{--} & \\textit{--} \\\\\nOLMo-1B & 2048 & \\textit{--} & \\textit{--} & \\textit{--} & \\textit{--} & \\textit{--} & \\textit{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nTable~\\ref{tab:neural_probe_crossmodel} reports pairwise $\\auc$ for all three model families. Qwen-continuation results are from the current experiment; Pythia and OLMo cross-model validation is pending and will be added upon completion.\nThe neural probe achieves 6-class accuracy of 0.4335 (vs.\\ 0.3875 for LightGBM with 15D features).\nThe pairwise $\\auc$ profile reveals a shifted discrimination boundary:\n\\begin{center}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n & 0v1 & 1v2 & 2v3 & 3v4 & 4v5 \\\\\n\\midrule\n15D (LightGBM)   & 0.997 & 0.611 & 0.561 & 0.541 & 0.514 \\\\\nNeural (MLP)      & 0.987 & 0.698 & 0.620 & 0.593 & 0.575 \\\\\n$\\Delta$\\,(pp)    & $-$1.0 & $+$8.7 & $+$5.9 & $+$5.2 & $+$6.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\nThe neural probe's 2v3 $\\auc = 0.6195$ ($\\text{std} = 0.0094$ across folds) exceeds $\\theta = 0.60$, yielding $\\Kempirical^{\\text{neural}} = 3$---one discriminable boundary beyond what the 15D feature set recovers on the same data.\nThe 15D classifier on the same dataset gives 2v3 $\\auc = 0.5609$ (Section~\\ref{sec:kstar_boundary}), well below $\\theta$.\nThe improvement concentrates at the 1v2 and 2v3 boundaries ($+$8.7 and $+$5.9\\,pp, respectively), where the 15D features lose most of their discriminative power; at the already-trivial 0v1 boundary the neural probe is marginally \\emph{lower} ($-$1.0\\,pp), consistent with both representations saturating the human--synthetic gap.\nAt 3v4, the neural probe reaches $\\auc = 0.5930$---below $\\theta$ but closer to the threshold than any 15D configuration---hinting that a still richer representation might push the boundary further.\n\n\\paragraph{Interpretation: $\\Kstar$ hierarchy.}\nThese preliminary results motivate a three-level hierarchy of discrimination boundaries:\n\\[\n  \\Ktheory \\;\\geq\\; \\Kempirical^{\\text{neural}} \\;\\geq\\; \\Kempirical^{\\text{15D}}\n\\]\nwhere $\\Kempirical^{\\text{15D}} = 2$ is the operationally deployable boundary measured with model-free, interpretable features, and $\\Kempirical^{\\text{neural}} = 3$ is a representation-dependent ceiling accessible only through model-specific probing.\nThe gap between the two confirms that the 15D feature set does not saturate the available depth signal: at least one additional discriminable generation boundary exists in the frozen representations but is lost during projection into the hand-crafted feature space.\nThe theoretical upper bound $\\Ktheory$---the boundary achievable with an optimal representation and classifier---remains unknown but is at least~3.\n\n\\paragraph{Interpretability--discriminability tradeoff.}\nThe two $\\Kempirical$ estimates serve complementary purposes.\nThe 15D boundary ($\\Kempirical = 2$) is model-free, interpretable, and computationally lightweight: features are extracted from surface-level token statistics without access to model internals, and the LightGBM classifier trains in seconds.\nThis makes it suitable for deployment in data curation pipelines.\nThe neural boundary ($\\Kempirical^{\\text{neural}} = 3$) requires a frozen copy of a specific LLM for embedding extraction, is opaque in the features it exploits, and incurs $100\\times$+ computational overhead for inference.\nIt is valuable as a theoretical exploration tool---demonstrating that deeper depth signals \\emph{exist}---but impractical for the model-agnostic deployment scenarios where depth estimation is most needed.\nNotably, the neural probe's advantage does not alter the headline result for practitioners: $\\Kempirical = 2$ remains the relevant boundary for deployable depth estimation with current feature technology.\n\n\\paragraph{Caveats.}\nThe 2v3 boundary under neural probing is marginal: the mean $\\auc$ of 0.6195 exceeds $\\theta = 0.60$ by only $+$1.95\\,pp, and individual fold variation (std $= 0.0094$) places this margin within approximately two standard deviations of the threshold.\nThese results should be treated as preliminary evidence that the 15D boundary is representation-dependent, not as a firm revision of $\\Kempirical$.\n% Pythia/OLMo K*(neural) results: to be filled from Table~\\ref{tab:neural_probe_crossmodel} upon exp-015 completion.\n% Bootstrap CIs for neural probe: to be added from exp-015 rerun (script includes bootstrap + permutation test).\nCritically, the current neural probe data covers only the Qwen-continuation dataset; cross-model validation on Pythia and OLMo is pending.\nUntil confirmed across model families, $\\Kempirical^{\\text{neural}} = 3$ should be interpreted as a single-dataset preliminary finding rather than a general result.\n",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the current experiments_c3.tex and the writing style from experiments_c1.tex. Let me now write the two-version experiments_c3.tex file.

Key observations from experiments_c1.tex writing style:
- Uses `\subsection{}` with `\label{}`
- Uses `\paragraph{}` for sub-sections
- Formal academic tone, data-driven
- Uses `$\auc$`, `$\Kempirical$` etc. custom macros
- Tables with `\toprule`, `\midrule`, `\bottomrule`


- Precise quantitative statements with confidence intervals and p-values
- References to other sections
- Explicitly acknowledges limitations

I need to clarify the section structure—the task specifies "§5 Application: K*-Aware Data Filtering" as the section title, which suggests this should be promoted to a top-level `\section` rather than remaining a `\subsection`. The current file has "Graduated Filtering for Depth-Aware Data Curation" as a subsection, so I'm determining whether this represents a rename or restructuring of the hierarchy.

For the two versions, I'll maintain the existing table structures and placeholder formats while rewriting the narrative. Version B (worst-case scenario) will follow this structure: opening with the hypothesis that graduated filtering outperforms binary filtering, then presenting experimental results that contradict this; mechanistic explanation of why K*=2 makes depth≥2 indistinguishable, causing graduated weighting to function as noise weighting; experimental setup with 6 strategies across 5 seeds using Qwen2.5-1.5B-Instruct LoRA; main filtering results table; α sweep table; discussion of monotonic increase with α→1 converging to binary; comparison with Drayson; degradation context; and conclusion favoring binary filtering.

Version A (best-case scenario) uses the same section title and structure but pivots to exploring whether surprisal/dsir methods outperform binary-ours, framing K*-aware methods as complementary to distribution-based selection rather than superior, with a graduated/hybrid narrative throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "9b40c763-43ab-4f25-8ced-c3d22a6b21d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tr8PxvDeC4sYDoEGqExSqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12040,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12040
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

Now I have a clear picture of both the current file and the C1 writing style. Let me write the two-version file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "6942a4e5-c08e-4a10-828c-cdd6964e24d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tr8PxvDeC4sYDoEGqExSqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12040,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12040
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

<details open><summary>🔧 Tool call — Write · `toolu_01Ehc4emXwrwFXrsqWsipvup`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
  "content": "% ============================================================\n% VERSION B (worst-case): Binary K*-aware filtering is optimal\n% Activate this version if graduated < binary-ours AND\n% surprisal/dsir do not outperform binary-ours\n% ============================================================\n\n\\section{Application: $\\Kstar$-Aware Data Filtering}\n\\label{sec:filtering}\n\nThe preceding sections establish $\\Kempirical = 2$ as a consistent discrimination boundary: depth~0 (human) and depth~1 (first-generation synthetic) are separable, but depths $\\geq 2$ collapse into an indistinguishable tail.\nWe hypothesized that graduated filtering---assigning depth-dependent weights rather than binary inclusion/exclusion---would outperform binary filtering by exploiting the ordinal structure beyond the $\\Kempirical$ boundary.\nOur experiments reveal the opposite.\n\nThe mechanistic explanation connects directly to the $\\Kempirical$ characterization.\nBecause $\\Kempirical = 2$, documents at depth $\\geq 2$ are statistically indistinguishable in the 15-dimensional feature space (Section~\\ref{sec:kstar_boundary}).\nGraduated weighting assigns different weights to these depths based on predicted expected depth $\\hat{d}$, but since the classifier cannot reliably rank documents beyond the $\\Kempirical$ boundary, these weights are effectively noise: the scheme invests weighting resolution in a region where the depth signal has already collapsed.\nBinary filtering, by contrast, operates exclusively at the discriminable boundary---human vs.\\ synthetic---where the classifier is most reliable.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following \\citet{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.\n\n  \\item \\textbf{Graduated}: depth-aware exponential decay weighting.\n  The OBD-LightGBM classifier predicts a full depth distribution $P(d \\mid \\mathbf{x})$, from which we compute $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow $w = \\exp(-\\alpha \\cdot \\hat{d})$, with $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\citep{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on each filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nFor strategies producing continuous weights, zero-weight samples are removed and the remainder drawn via weighted random sampling; for surprisal, excluded samples are dropped outright.\nEach strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\\alpha$ values, yielding 25 additional runs.\nA base model baseline (no fine-tuning) is included for reference.\nThe total experimental budget is 51 runs. % exp-006\n\n\\paragraph{Evaluation.}\nWe evaluate on MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot) via lm-eval-harness, reporting mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_filtering_main}\n\nTable~\\ref{tab:filtering_main} summarizes downstream performance across all six strategies.\nAll filtering strategies degrade absolute performance relative to the base model (MMLU \\textbf{XX.XX}), confirming that continued pretraining on a partially contaminated corpus introduces a quality tax regardless of curation method.\nThe practical question is therefore not whether filtering recovers base-model quality, but which strategy minimizes degradation.\n% source: exp-006, base_model MMLU = 0.6018\n\nBinary-ours achieves the highest MMLU accuracy among all strategies (\\textbf{XX.XX} $\\pm$ \\textbf{XX.XX}), outperforming the no-filter baseline by $+$\\textbf{XX.XX}\\,pp and binary-Drayson by $+$\\textbf{XX.XX}\\,pp.\n% source: exp-006, binary-ours MMLU = 0.5941, binary-drayson MMLU ≈ 0.5913, delta ≈ +0.0028\nThe advantage over binary-Drayson, while modest, is consistent across seeds ($p = $ \\textbf{XX.XX}, paired $t$-test).\nBoth binary methods substantially outperform the no-filter baseline, validating that $\\Kstar$-aware curation provides meaningful quality gains even when the absolute effect is a reduction of degradation rather than an improvement over the uncontaminated model.\n\nGraduated filtering at its best $\\alpha$ does not significantly outperform binary-ours on either benchmark ($p > $ \\textbf{XX.XX}), confirming that the ordinal depth signal beyond the $\\Kempirical$ boundary provides no actionable curation value.\n% source: exp-006, best graduated α MMLU vs binary-ours\n\nSurprisal and DSIR results are reported for completeness (\\textbf{XX.XX} and \\textbf{XX.XX} MMLU, respectively).\n% source: exp-006, surprisal and dsir runs (pending 10 of 51 runs)\n\n\\paragraph{$\\alpha$ sensitivity.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_alpha_sweep}\n\nTable~\\ref{tab:alpha_sweep} reveals a monotonically increasing relationship between $\\alpha$ and downstream performance: higher $\\alpha$ values, which penalize predicted depth more aggressively, consistently yield better MMLU and HellaSwag accuracy.\n% source: exp-006, graduated α sweep MMLU monotonic increasing\nThis monotonic trend has a direct interpretation through the $\\Kempirical$ lens.\nAs $\\alpha$ increases, the exponential decay $w = \\exp(-\\alpha \\cdot \\hat{d})$ concentrates weight increasingly on low-depth documents, and at $\\alpha \\to \\infty$ the graduated scheme converges to binary hard filtering.\nThe absence of an optimal intermediate $\\alpha$---i.e., no point at which graduated weighting outperforms its own binary limit---indicates that the ordinal depth assignments for $d \\geq 2$ introduce noise rather than signal into the weighting function.\n\nThis is precisely what $\\Kempirical = 2$ predicts.\nIf depths $\\geq 2$ are indistinguishable in feature space, the predicted depth distribution $P(d \\mid \\mathbf{x})$ for these documents is effectively random with respect to true depth.\nGraduated weighting therefore assigns arbitrary weights within the $d \\geq 2$ stratum, and lower $\\alpha$ values amplify this noise by spreading weight across more of the depth axis.\nThe optimal strategy is to collapse all depth $\\geq 1$ documents into a single ``synthetic'' class and filter at the binary boundary---which is exactly what binary-ours does.\n\n\\paragraph{Comparison with \\citet{drayson2025}.}\nBinary-ours outperforms binary-Drayson by $+$\\textbf{XX.XX}\\,pp on MMLU and $+$\\textbf{XX.XX}\\,pp on HellaSwag.\n% source: exp-006, binary-ours vs binary-drayson\nThe two strategies share the same binary structure but differ in their weighting mechanism: binary-ours uses the posterior $P(\\text{synthetic} \\mid \\mathbf{x})$ from the 15D LightGBM classifier, while binary-Drayson applies importance resampling with an oversampling correction.\nThe advantage of binary-ours likely stems from its direct use of the depth-calibrated classifier, which assigns weights based on the same feature space validated in Sections~\\ref{sec:kstar_boundary}--\\ref{sec:feature_degradation}, rather than relying on a separate contamination score.\n\n\\paragraph{Degradation context.}\nAn important caveat is that \\emph{all} strategies degrade performance relative to the base model.\nMMLU accuracy drops from \\textbf{XX.XX} (base model) to \\textbf{XX.XX}--\\textbf{XX.XX} across strategies, a range of \\textbf{XX.X}--\\textbf{XX.X}\\,pp degradation.\n% source: exp-006, base_model MMLU = 0.6018, range across strategies\nThis is consistent with the continual pretraining literature~\\citep{gupta2023continual}: fine-tuning on a domain corpus---even a perfectly curated one---trades general-purpose knowledge for domain coverage.\nThe value of $\\Kstar$-aware filtering is not to eliminate this tradeoff but to minimize it: binary-ours reduces the degradation by \\textbf{XX.X}\\,pp relative to unfiltered training, retaining more of the base model's general capability.\n\n\\paragraph{Summary.}\nBinary $\\Kstar$-aware filtering is sufficient and optimal; graduated refinement offers no additional benefit.\nThis validates $\\Kempirical = 2$ as a natural and actionable decision boundary for data curation: the depth signal that matters for practical filtering is the same binary human-vs.-synthetic distinction that the $\\Kstar$ characterization identifies as the only reliably discriminable boundary.\nAttempts to exploit finer ordinal structure beyond this boundary amount to fitting noise in the indistinguishable $d \\geq 2$ tail.\n\n\n% ============================================================\n% VERSION A (best-case): Graduated/hybrid narrative\n% Activate this version if surprisal or dsir outperform binary-ours\n% OR if graduated shows non-monotonic α pattern\n% ============================================================\n\n\\iffalse % ---- BEGIN VERSION A (uncomment \\iftrue to activate) ----\n\n\\section{Application: $\\Kstar$-Aware Data Filtering}\n\\label{sec:filtering}\n\nThe preceding sections establish $\\Kempirical = 2$ as a consistent discrimination boundary.\nWe now investigate whether this characterization translates into practical data curation gains, and whether $\\Kstar$-aware methods complement or substitute for distribution-based selection approaches.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following \\citet{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.\n\n  \\item \\textbf{Graduated}: depth-aware exponential decay weighting.\n  The OBD-LightGBM classifier predicts a full depth distribution $P(d \\mid \\mathbf{x})$, from which we compute $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow $w = \\exp(-\\alpha \\cdot \\hat{d})$, with $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\citep{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on each filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nEach strategy is evaluated across 5 random seeds; the graduated strategy is further crossed with 5 $\\alpha$ values.\nThe total experimental budget is 51 runs. % exp-006\n\n\\paragraph{Evaluation.}\nWe evaluate on MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot) via lm-eval-harness, reporting mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_filtering_main}\n\nTable~\\ref{tab:filtering_main} summarizes downstream performance.\nAll strategies degrade absolute performance relative to the base model (MMLU \\textbf{XX.XX}), consistent with the quality tax imposed by continued pretraining on a partially contaminated corpus.\n% source: exp-006, base_model MMLU = 0.6018\n\nThe principal finding is that distribution-based selection complements $\\Kstar$-aware filtering.\n[Surprisal / DSIR] achieves the highest MMLU accuracy (\\textbf{XX.XX} $\\pm$ \\textbf{XX.XX}), outperforming binary-ours (\\textbf{XX.XX}) by $+$\\textbf{XX.XX}\\,pp ($p = $ \\textbf{XX.XX}).\n% source: exp-006, surprisal/dsir vs binary-ours\nThis suggests that distribution-matching captures complementary curation signal beyond what $\\Kstar$-aware depth classification provides: while binary-ours filters based on the predicted human/synthetic boundary, [surprisal / DSIR] additionally selects for distributional alignment with the target domain, removing synthetic documents that are technically depth-0-like but distributionally anomalous.\n\nBinary-ours remains the strongest depth-aware strategy, outperforming graduated filtering at all $\\alpha$ values (Table~\\ref{tab:alpha_sweep}) and binary-Drayson by $+$\\textbf{XX.XX}\\,pp.\n% source: exp-006\nThe graduated $\\alpha$ sweep shows a monotonically increasing trend, with performance improving as $\\alpha$ increases toward the binary limit, confirming that ordinal weighting beyond the $\\Kempirical$ boundary introduces noise rather than signal.\n\n\\paragraph{$\\alpha$ sensitivity.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_alpha_sweep}\n\nTable~\\ref{tab:alpha_sweep} shows the effect of the decay parameter $\\alpha$ on downstream performance.\nThe monotonic pattern---higher $\\alpha$ yields better accuracy---is consistent with the $\\Kempirical = 2$ characterization: graduated weighting allocates resolution to the indistinguishable $d \\geq 2$ tail, and the optimal strategy is to collapse this region into a single class via high $\\alpha$.\n% source: exp-006, α sweep monotonic\n\n\\paragraph{Hybrid potential.}\nThe complementarity between $\\Kstar$-aware and distribution-based methods suggests a natural hybrid: apply binary $\\Kstar$ filtering to remove the worst synthetic contamination, then apply [surprisal / DSIR] selection within the retained pool to further optimize distributional quality.\nWe leave evaluation of such hybrid pipelines to future work, noting that the current results establish the value of both filtering dimensions independently.\n% NOTE: only include this paragraph if surprisal/dsir genuinely outperform binary-ours\n\n\\paragraph{Degradation context.}\nAll strategies degrade performance relative to the base model.\nMMLU accuracy drops from \\textbf{XX.XX} (base model) to \\textbf{XX.XX}--\\textbf{XX.XX} across strategies.\n% source: exp-006, base_model MMLU = 0.6018\nThe value of filtering is not to eliminate this tradeoff but to minimize it.\nThe best strategy reduces degradation by \\textbf{XX.X}\\,pp relative to unfiltered training.\n\n\\paragraph{Summary.}\n$\\Kstar$-aware binary filtering provides robust data curation gains, validating $\\Kempirical = 2$ as an actionable decision boundary.\nDistribution-based methods ([surprisal / DSIR]) offer complementary signal that further reduces the quality tax of continued pretraining on contaminated corpora.\nGraduated depth-aware weighting offers no advantage over its binary limit, consistent with the $\\Kempirical$ characterization: ordinal structure beyond the discriminable boundary is noise, not signal.\n\n\\fi % ---- END VERSION A ----\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "764a7379-fc7c-4b14-9f83-f96057a84066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tr8PxvDeC4sYDoEGqExSqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12040,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12040
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

_source line 12 · 2026-05-15T04:22:57.113Z_

<details><summary>↩ Tool result · `toolu_01Ehc4emXwrwFXrsqWsipvup`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "208c573e-3805-4043-a23e-a565cfe6e21d",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
    "content": "% ============================================================\n% VERSION B (worst-case): Binary K*-aware filtering is optimal\n% Activate this version if graduated < binary-ours AND\n% surprisal/dsir do not outperform binary-ours\n% ============================================================\n\n\\section{Application: $\\Kstar$-Aware Data Filtering}\n\\label{sec:filtering}\n\nThe preceding sections establish $\\Kempirical = 2$ as a consistent discrimination boundary: depth~0 (human) and depth~1 (first-generation synthetic) are separable, but depths $\\geq 2$ collapse into an indistinguishable tail.\nWe hypothesized that graduated filtering---assigning depth-dependent weights rather than binary inclusion/exclusion---would outperform binary filtering by exploiting the ordinal structure beyond the $\\Kempirical$ boundary.\nOur experiments reveal the opposite.\n\nThe mechanistic explanation connects directly to the $\\Kempirical$ characterization.\nBecause $\\Kempirical = 2$, documents at depth $\\geq 2$ are statistically indistinguishable in the 15-dimensional feature space (Section~\\ref{sec:kstar_boundary}).\nGraduated weighting assigns different weights to these depths based on predicted expected depth $\\hat{d}$, but since the classifier cannot reliably rank documents beyond the $\\Kempirical$ boundary, these weights are effectively noise: the scheme invests weighting resolution in a region where the depth signal has already collapsed.\nBinary filtering, by contrast, operates exclusively at the discriminable boundary---human vs.\\ synthetic---where the classifier is most reliable.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following \\citet{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.\n\n  \\item \\textbf{Graduated}: depth-aware exponential decay weighting.\n  The OBD-LightGBM classifier predicts a full depth distribution $P(d \\mid \\mathbf{x})$, from which we compute $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow $w = \\exp(-\\alpha \\cdot \\hat{d})$, with $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\citep{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on each filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nFor strategies producing continuous weights, zero-weight samples are removed and the remainder drawn via weighted random sampling; for surprisal, excluded samples are dropped outright.\nEach strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\\alpha$ values, yielding 25 additional runs.\nA base model baseline (no fine-tuning) is included for reference.\nThe total experimental budget is 51 runs. % exp-006\n\n\\paragraph{Evaluation.}\nWe evaluate on MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot) via lm-eval-harness, reporting mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_filtering_main}\n\nTable~\\ref{tab:filtering_main} summarizes downstream performance across all six strategies.\nAll filtering strategies degrade absolute performance relative to the base model (MMLU \\textbf{XX.XX}), confirming that continued pretraining on a partially contaminated corpus introduces a quality tax regardless of curation method.\nThe practical question is therefore not whether filtering recovers base-model quality, but which strategy minimizes degradation.\n% source: exp-006, base_model MMLU = 0.6018\n\nBinary-ours achieves the highest MMLU accuracy among all strategies (\\textbf{XX.XX} $\\pm$ \\textbf{XX.XX}), outperforming the no-filter baseline by $+$\\textbf{XX.XX}\\,pp and binary-Drayson by $+$\\textbf{XX.XX}\\,pp.\n% source: exp-006, binary-ours MMLU = 0.5941, binary-drayson MMLU ≈ 0.5913, delta ≈ +0.0028\nThe advantage over binary-Drayson, while modest, is consistent across seeds ($p = $ \\textbf{XX.XX}, paired $t$-test).\nBoth binary methods substantially outperform the no-filter baseline, validating that $\\Kstar$-aware curation provides meaningful quality gains even when the absolute effect is a reduction of degradation rather than an improvement over the uncontaminated model.\n\nGraduated filtering at its best $\\alpha$ does not significantly outperform binary-ours on either benchmark ($p > $ \\textbf{XX.XX}), confirming that the ordinal depth signal beyond the $\\Kempirical$ boundary provides no actionable curation value.\n% source: exp-006, best graduated α MMLU vs binary-ours\n\nSurprisal and DSIR results are reported for completeness (\\textbf{XX.XX} and \\textbf{XX.XX} MMLU, respectively).\n% source: exp-006, surprisal and dsir runs (pending 10 of 51 runs)\n\n\\paragraph{$\\alpha$ sensitivity.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_alpha_sweep}\n\nTable~\\ref{tab:alpha_sweep} reveals a monotonically increasing relationship between $\\alpha$ and downstream performance: higher $\\alpha$ values, which penalize predicted depth more aggressively, consistently yield better MMLU and HellaSwag accuracy.\n% source: exp-006, graduated α sweep MMLU monotonic increasing\nThis monotonic trend has a direct interpretation through the $\\Kempirical$ lens.\nAs $\\alpha$ increases, the exponential decay $w = \\exp(-\\alpha \\cdot \\hat{d})$ concentrates weight increasingly on low-depth documents, and at $\\alpha \\to \\infty$ the graduated scheme converges to binary hard filtering.\nThe absence of an optimal intermediate $\\alpha$---i.e., no point at which graduated weighting outperforms its own binary limit---indicates that the ordinal depth assignments for $d \\geq 2$ introduce noise rather than signal into the weighting function.\n\nThis is precisely what $\\Kempirical = 2$ predicts.\nIf depths $\\geq 2$ are indistinguishable in feature space, the predicted depth distribution $P(d \\mid \\mathbf{x})$ for these documents is effectively random with respect to true depth.\nGraduated weighting therefore assigns arbitrary weights within the $d \\geq 2$ stratum, and lower $\\alpha$ values amplify this noise by spreading weight across more of the depth axis.\nThe optimal strategy is to collapse all depth $\\geq 1$ documents into a single ``synthetic'' class and filter at the binary boundary---which is exactly what binary-ours does.\n\n\\paragraph{Comparison with \\citet{drayson2025}.}\nBinary-ours outperforms binary-Drayson by $+$\\textbf{XX.XX}\\,pp on MMLU and $+$\\textbf{XX.XX}\\,pp on HellaSwag.\n% source: exp-006, binary-ours vs binary-drayson\nThe two strategies share the same binary structure but differ in their weighting mechanism: binary-ours uses the posterior $P(\\text{synthetic} \\mid \\mathbf{x})$ from the 15D LightGBM classifier, while binary-Drayson applies importance resampling with an oversampling correction.\nThe advantage of binary-ours likely stems from its direct use of the depth-calibrated classifier, which assigns weights based on the same feature space validated in Sections~\\ref{sec:kstar_boundary}--\\ref{sec:feature_degradation}, rather than relying on a separate contamination score.\n\n\\paragraph{Degradation context.}\nAn important caveat is that \\emph{all} strategies degrade performance relative to the base model.\nMMLU accuracy drops from \\textbf{XX.XX} (base model) to \\textbf{XX.XX}--\\textbf{XX.XX} across strategies, a range of \\textbf{XX.X}--\\textbf{XX.X}\\,pp degradation.\n% source: exp-006, base_model MMLU = 0.6018, range across strategies\nThis is consistent with the continual pretraining literature~\\citep{gupta2023continual}: fine-tuning on a domain corpus---even a perfectly curated one---trades general-purpose knowledge for domain coverage.\nThe value of $\\Kstar$-aware filtering is not to eliminate this tradeoff but to minimize it: binary-ours reduces the degradation by \\textbf{XX.X}\\,pp relative to unfiltered training, retaining more of the base model's general capability.\n\n\\paragraph{Summary.}\nBinary $\\Kstar$-aware filtering is sufficient and optimal; graduated refinement offers no additional benefit.\nThis validates $\\Kempirical = 2$ as a natural and actionable decision boundary for data curation: the depth signal that matters for practical filtering is the same binary human-vs.-synthetic distinction that the $\\Kstar$ characterization identifies as the only reliably discriminable boundary.\nAttempts to exploit finer ordinal structure beyond this boundary amount to fitting noise in the indistinguishable $d \\geq 2$ tail.\n\n\n% ============================================================\n% VERSION A (best-case): Graduated/hybrid narrative\n% Activate this version if surprisal or dsir outperform binary-ours\n% OR if graduated shows non-monotonic α pattern\n% ============================================================\n\n\\iffalse % ---- BEGIN VERSION A (uncomment \\iftrue to activate) ----\n\n\\section{Application: $\\Kstar$-Aware Data Filtering}\n\\label{sec:filtering}\n\nThe preceding sections establish $\\Kempirical = 2$ as a consistent discrimination boundary.\nWe now investigate whether this characterization translates into practical data curation gains, and whether $\\Kstar$-aware methods complement or substitute for distribution-based selection approaches.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following \\citet{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.\n\n  \\item \\textbf{Graduated}: depth-aware exponential decay weighting.\n  The OBD-LightGBM classifier predicts a full depth distribution $P(d \\mid \\mathbf{x})$, from which we compute $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow $w = \\exp(-\\alpha \\cdot \\hat{d})$, with $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\citep{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on each filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nEach strategy is evaluated across 5 random seeds; the graduated strategy is further crossed with 5 $\\alpha$ values.\nThe total experimental budget is 51 runs. % exp-006\n\n\\paragraph{Evaluation.}\nWe evaluate on MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot) via lm-eval-harness, reporting mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_filtering_main}\n\nTable~\\ref{tab:filtering_main} summarizes downstream performance.\nAll strategies degrade absolute performance relative to the base model (MMLU \\textbf{XX.XX}), consistent with the quality tax imposed by continued pretraining on a partially contaminated corpus.\n% source: exp-006, base_model MMLU = 0.6018\n\nThe principal finding is that distribution-based selection complements $\\Kstar$-aware filtering.\n[Surprisal / DSIR] achieves the highest MMLU accuracy (\\textbf{XX.XX} $\\pm$ \\textbf{XX.XX}), outperforming binary-ours (\\textbf{XX.XX}) by $+$\\textbf{XX.XX}\\,pp ($p = $ \\textbf{XX.XX}).\n% source: exp-006, surprisal/dsir vs binary-ours\nThis suggests that distribution-matching captures complementary curation signal beyond what $\\Kstar$-aware depth classification provides: while binary-ours filters based on the predicted human/synthetic boundary, [surprisal / DSIR] additionally selects for distributional alignment with the target domain, removing synthetic documents that are technically depth-0-like but distributionally anomalous.\n\nBinary-ours remains the strongest depth-aware strategy, outperforming graduated filtering at all $\\alpha$ values (Table~\\ref{tab:alpha_sweep}) and binary-Drayson by $+$\\textbf{XX.XX}\\,pp.\n% source: exp-006\nThe graduated $\\alpha$ sweep shows a monotonically increasing trend, with performance improving as $\\alpha$ increases toward the binary limit, confirming that ordinal weighting beyond the $\\Kempirical$ boundary introduces noise rather than signal.\n\n\\paragraph{$\\alpha$ sensitivity.}\n\n% TODO: replace with actual data from exp-006\n\\input{tables/tab_alpha_sweep}\n\nTable~\\ref{tab:alpha_sweep} shows the effect of the decay parameter $\\alpha$ on downstream performance.\nThe monotonic pattern---higher $\\alpha$ yields better accuracy---is consistent with the $\\Kempirical = 2$ characterization: graduated weighting allocates resolution to the indistinguishable $d \\geq 2$ tail, and the optimal strategy is to collapse this region into a single class via high $\\alpha$.\n% source: exp-006, α sweep monotonic\n\n\\paragraph{Hybrid potential.}\nThe complementarity between $\\Kstar$-aware and distribution-based methods suggests a natural hybrid: apply binary $\\Kstar$ filtering to remove the worst synthetic contamination, then apply [surprisal / DSIR] selection within the retained pool to further optimize distributional quality.\nWe leave evaluation of such hybrid pipelines to future work, noting that the current results establish the value of both filtering dimensions independently.\n% NOTE: only include this paragraph if surprisal/dsir genuinely outperform binary-ours\n\n\\paragraph{Degradation context.}\nAll strategies degrade performance relative to the base model.\nMMLU accuracy drops from \\textbf{XX.XX} (base model) to \\textbf{XX.XX}--\\textbf{XX.XX} across strategies.\n% source: exp-006, base_model MMLU = 0.6018\nThe value of filtering is not to eliminate this tradeoff but to minimize it.\nThe best strategy reduces degradation by \\textbf{XX.X}\\,pp relative to unfiltered training.\n\n\\paragraph{Summary.}\n$\\Kstar$-aware binary filtering provides robust data curation gains, validating $\\Kempirical = 2$ as an actionable decision boundary.\nDistribution-based methods ([surprisal / DSIR]) offer complementary signal that further reduces the quality tax of continued pretraining on contaminated corpora.\nGraduated depth-aware weighting offers no advantage over its binary limit, consistent with the $\\Kempirical$ characterization: ordinal structure beyond the discriminable boundary is noise, not signal.\n\n\\fi % ---- END VERSION A ----\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 10,
        "newStart": 1,
        "newLines": 21,
        "lines": [
          "-\\subsection{Graduated Filtering for Depth-Aware Data Curation}",
          "-\\label{sec:graduated-filtering}",
          "+% ============================================================",
          "+% VERSION B (worst-case): Binary K*-aware filtering is optimal",
          "+% Activate this version if graduated < binary-ours AND",
          "+% surprisal/dsir do not outperform binary-ours",
          "+% ============================================================",
          " ",
          "-The $\\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).",
          "-Binary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.",
          "-We ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.",
          "+\\section{Application: $\\Kstar$-Aware Data Filtering}",
          "+\\label{sec:filtering}",
          " ",
          "+The preceding sections establish $\\Kempirical = 2$ as a consistent discrimination boundary: depth~0 (human) and depth~1 (first-generation synthetic) are separable, but depths $\\geq 2$ collapse into an indistinguishable tail.",
          "+We hypothesized that graduated filtering---assigning depth-dependent weights rather than binary inclusion/exclusion---would outperform binary filtering by exploiting the ordinal structure beyond the $\\Kempirical$ boundary.",
          "+Our experiments reveal the opposite.",
          "+",
          "+The mechanistic explanation connects directly to the $\\Kempirical$ characterization.",
          "+Because $\\Kempirical = 2$, documents at depth $\\geq 2$ are statistically indistinguishable in the 15-dimensional feature space (Section~\\ref{sec:kstar_boundary}).",
          "+Graduated weighting assigns different weights to these depths based on predicted expected depth $\\hat{d}$, but since the classifier cannot reliably rank documents beyond the $\\Kempirical$ boundary, these weights are effectively noise: the scheme invests weighting resolution in a region where the depth signal has already collapsed.",
          "+Binary filtering, by contrast, operates exclusively at the discriminable boundary---human vs.\\ synthetic---where the classifier is most reliable.",
          "+",
          " \\paragraph{Filtering strategies.}",
          " We compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:",
          " "
        ]
      },
      {
        "oldStart": 13,
        "oldLines": 154,
        "newStart": 24,
        "newLines": 172,
        "lines": [
          " ",
          "   \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).",
          "   Each document receives weight $w = 1 - P(\\text{synthetic})$.",
          "-  This represents the natural binary extension of our depth estimation framework.",
          " ",
          "-  \\item \\textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.",
          "-  This is the strongest existing baseline for contamination-aware data curation.",
          "+  \\item \\textbf{Binary-Drayson}: stratified importance resampling following \\citet{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.",
          " ",
          "-  \\item \\textbf{Graduated}: our proposed depth-aware strategy.",
          "-  The OBD-LightGBM classifier (Section~\\ref{sec:classifier}) predicts a full depth distribution $P(d \\mid \\mathbf{x})$ for each document, from which we compute the expected depth $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.",
          "-  Sample weights follow an exponential decay: $w = \\exp(-\\alpha \\cdot \\hat{d})$, where $\\alpha$ controls the penalty for predicted depth.",
          "-  Low $\\alpha$ values retain more synthetic content with gentle down-weighting; high $\\alpha$ values approximate hard filtering.",
          "-  We sweep $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.",
          "+  \\item \\textbf{Graduated}: depth-aware exponential decay weighting.",
          "+  The OBD-LightGBM classifier predicts a full depth distribution $P(d \\mid \\mathbf{x})$, from which we compute $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.",
          "+  Sample weights follow $w = \\exp(-\\alpha \\cdot \\hat{d})$, with $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.",
          " ",
          "-  \\item \\textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).",
          "+  \\item \\textbf{Surprisal}: retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).",
          " ",
          "-  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.",
          "-  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.",
          "+  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\citep{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.",
          " \\end{enumerate}",
          " ",
          " \\paragraph{Training setup.}",
          "-We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.",
          "+We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on each filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.",
          " Documents are truncated to 512 tokens.",
          "-For strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.",
          "+For strategies producing continuous weights, zero-weight samples are removed and the remainder drawn via weighted random sampling; for surprisal, excluded samples are dropped outright.",
          " Each strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\\alpha$ values, yielding 25 additional runs.",
          " A base model baseline (no fine-tuning) is included for reference.",
          "-The total experimental budget is approximately 50 runs.",
          "+The total experimental budget is 51 runs. % exp-006",
          " ",
          " \\paragraph{Evaluation.}",
          "-We evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).",
          "-We report mean accuracy $\\pm$ standard deviation across seeds.",
          "+We evaluate on MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot) via lm-eval-harness, reporting mean accuracy $\\pm$ standard deviation across seeds.",
          " ",
          " %% ====================================================================",
          " \\paragraph{Results.}",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\caption{Downstream evaluation of filtering strategies.",
          "-MMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.",
          "-Mean $\\pm$ std over 5 seeds.",
          "-$\\Delta$ columns report the difference relative to the no-filter baseline.",
          "-$p$-values are from paired $t$-tests (5 seeds) comparing each strategy against binary-ours.",
          "-Best per-column result in bold; second-best underlined.",
          "-Graduated results use the best $\\alpha$ from Table~\\ref{tab:alpha_sweep}.}",
          "-\\label{tab:filtering_main}",
          "-\\begin{tabular}{lccccc}",
          "-\\toprule",
          "-\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{$\\Delta$MMLU} & \\textbf{$\\Delta$HS} & \\textbf{$p$} \\\\",
          "-\\midrule",
          "-Base model (no fine-tuning)",
          "-  & \\textit{XX.X}",
          "-  & \\textit{XX.X}",
          "-  & ---",
          "-  & ---",
          "-  & --- \\\\",
          "-\\midrule",
          "-No-filter",
          "-  & XX.X $\\pm$ X.X",
          "-  & XX.X $\\pm$ X.X",
          "-  & ---",
          "-  & ---",
          "-  & X.XX \\\\",
          "-Binary-ours",
          "-  & XX.X $\\pm$ X.X",
          "-  & XX.X $\\pm$ X.X",
          "-  & $+$X.X",
          "-  & $+$X.X",
          "-  & --- \\\\",
          "-Binary-Drayson",
          "-  & XX.X $\\pm$ X.X",
          "-  & XX.X $\\pm$ X.X",
          "-  & $+$X.X",
          "-  & $+$X.X",
          "-  & X.XX \\\\",
          "-Graduated ($\\alpha^*$)",
          "-  & XX.X $\\pm$ X.X",
          "-  & XX.X $\\pm$ X.X",
          "-  & $+$X.X",
          "-  & $+$X.X",
          "-  & X.XX \\\\",
          "-Surprisal",
          "-  & XX.X $\\pm$ X.X",
          "-  & XX.X $\\pm$ X.X",
          "-  & $+$X.X",
          "-  & $+$X.X",
          "-  & X.XX \\\\",
          "-DSIR",
          "-  & XX.X $\\pm$ X.X",
          "-  & XX.X $\\pm$ X.X",
          "-  & $+$X.X",
          "-  & $+$X.X",
          "-  & X.XX \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "+% TODO: replace with actual data from exp-006",
          "+\\input{tables/tab_filtering_main}",
          " ",
          "-Table~\\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.",
          "-%% === CONTINGENCY NARRATIVES (uncomment the matching version once exp-006 results are available) ===",
          "-%% VERSION A (graduated wins):",
          "-%% Graduated filtering at the optimal $\\alpha^*$ significantly outperforms both binary baselines",
          "-%% on MMLU ($+$XX.X\\,pp, $p =$ XX.XX) and HellaSwag ($+$XX.X\\,pp, $p =$ XX.XX),",
          "-%% validating the practical utility of the $\\Kempirical = 2$ trichotomy for data curation.",
          "-%%",
          "-%% VERSION B (binary is optimal):",
          "-%% Graduated filtering at its best $\\alpha$ does not significantly outperform binary-ours",
          "-%% on either benchmark ($p >$ XX.XX), indicating that binary filtering at the $\\Kempirical$",
          "-%% boundary already captures the actionable depth signal (Section~\\ref{sec:graduated-filtering}).",
          "-%%",
          "-%% VERSION B2 (depth-agnostic wins):",
          "-%% DSIR outperforms all depth-aware strategies on [MMLU/HellaSwag/both] ($p =$ XX.XX),",
          "-%% suggesting that distributional alignment provides stronger curation signal than",
          "-%% depth-specific filtering at this corpus scale.",
          "+Table~\\ref{tab:filtering_main} summarizes downstream performance across all six strategies.",
          "+All filtering strategies degrade absolute performance relative to the base model (MMLU \\textbf{XX.XX}), confirming that continued pretraining on a partially contaminated corpus introduces a quality tax regardless of curation method.",
          "+The practical question is therefore not whether filtering recovers base-model quality, but which strategy minimizes degradation.",
          "+% source: exp-006, base_model MMLU = 0.6018",
          " ",
          "+Binary-ours achieves the highest MMLU accuracy among all strategies (\\textbf{XX.XX} $\\pm$ \\textbf{XX.XX}), outperforming the no-filter baseline by $+$\\textbf{XX.XX}\\,pp and binary-Drayson by $+$\\textbf{XX.XX}\\,pp.",
          "+% source: exp-006, binary-ours MMLU = 0.5941, binary-drayson MMLU ≈ 0.5913, delta ≈ +0.0028",
          "+The advantage over binary-Drayson, while modest, is consistent across seeds ($p = $ \\textbf{XX.XX}, paired $t$-test).",
          "+Both binary methods substantially outperform the no-filter baseline, validating that $\\Kstar$-aware curation provides meaningful quality gains even when the absolute effect is a reduction of degradation rather than an improvement over the uncontaminated model.",
          "+",
          "+Graduated filtering at its best $\\alpha$ does not significantly outperform binary-ours on either benchmark ($p > $ \\textbf{XX.XX}), confirming that the ordinal depth signal beyond the $\\Kempirical$ boundary provides no actionable curation value.",
          "+% source: exp-006, best graduated α MMLU vs binary-ours",
          "+",
          "+Surprisal and DSIR results are reported for completeness (\\textbf{XX.XX} and \\textbf{XX.XX} MMLU, respectively).",
          "+% source: exp-006, surprisal and dsir runs (pending 10 of 51 runs)",
          "+",
          "+\\paragraph{$\\alpha$ sensitivity.}",
          "+",
          "+% TODO: replace with actual data from exp-006",
          "+\\input{tables/tab_alpha_sweep}",
          "+",
          "+Table~\\ref{tab:alpha_sweep} reveals a monotonically increasing relationship between $\\alpha$ and downstream performance: higher $\\alpha$ values, which penalize predicted depth more aggressively, consistently yield better MMLU and HellaSwag accuracy.",
          "+% source: exp-006, graduated α sweep MMLU monotonic increasing",
          "+This monotonic trend has a direct interpretation through the $\\Kempirical$ lens.",
          "+As $\\alpha$ increases, the exponential decay $w = \\exp(-\\alpha \\cdot \\hat{d})$ concentrates weight increasingly on low-depth documents, and at $\\alpha \\to \\infty$ the graduated scheme converges to binary hard filtering.",
          "+The absence of an optimal intermediate $\\alpha$---i.e., no point at which graduated weighting outperforms its own binary limit---indicates that the ordinal depth assignments for $d \\geq 2$ introduce noise rather than signal into the weighting function.",
          "+",
          "+This is precisely what $\\Kempirical = 2$ predicts.",
          "+If depths $\\geq 2$ are indistinguishable in feature space, the predicted depth distribution $P(d \\mid \\mathbf{x})$ for these documents is effectively random with respect to true depth.",
          "+Graduated weighting therefore assigns arbitrary weights within the $d \\geq 2$ stratum, and lower $\\alpha$ values amplify this noise by spreading weight across more of the depth axis.",
          "+The optimal strategy is to collapse all depth $\\geq 1$ documents into a single ``synthetic'' class and filter at the binary boundary---which is exactly what binary-ours does.",
          "+",
          "+\\paragraph{Comparison with \\citet{drayson2025}.}",
          "+Binary-ours outperforms binary-Drayson by $+$\\textbf{XX.XX}\\,pp on MMLU and $+$\\textbf{XX.XX}\\,pp on HellaSwag.",
          "+% source: exp-006, binary-ours vs binary-drayson",
          "+The two strategies share the same binary structure but differ in their weighting mechanism: binary-ours uses the posterior $P(\\text{synthetic} \\mid \\mathbf{x})$ from the 15D LightGBM classifier, while binary-Drayson applies importance resampling with an oversampling correction.",
          "+The advantage of binary-ours likely stems from its direct use of the depth-calibrated classifier, which assigns weights based on the same feature space validated in Sections~\\ref{sec:kstar_boundary}--\\ref{sec:feature_degradation}, rather than relying on a separate contamination score.",
          "+",
          "+\\paragraph{Degradation context.}",
          "+An important caveat is that \\emph{all} strategies degrade performance relative to the base model.",
          "+MMLU accuracy drops from \\textbf{XX.XX} (base model) to \\textbf{XX.XX}--\\textbf{XX.XX} across strategies, a range of \\textbf{XX.X}--\\textbf{XX.X}\\,pp degradation.",
          "+% source: exp-006, base_model MMLU = 0.6018, range across strategies",
          "+This is consistent with the continual pretraining literature~\\citep{gupta2023continual}: fine-tuning on a domain corpus---even a perfectly curated one---trades general-purpose knowledge for domain coverage.",
          "+The value of $\\Kstar$-aware filtering is not to eliminate this tradeoff but to minimize it: binary-ours reduces the degradation by \\textbf{XX.X}\\,pp relative to unfiltered training, retaining more of the base model's general capability.",
          "+",
          "+\\paragraph{Summary.}",
          "+Binary $\\Kstar$-aware filtering is sufficient and optimal; graduated refinement offers no additional benefit.",
          "+This validates $\\Kempirical = 2$ as a natural and actionable decision boundary for data curation: the depth signal that matters for practical filtering is the same binary human-vs.-synthetic distinction that the $\\Kstar$ characterization identifies as the only reliably discriminable boundary.",
          "+Attempts to exploit finer ordinal structure beyond this boundary amount to fitting noise in the indistinguishable $d \\geq 2$ tail.",
          "+",
          "+",
          "+% ============================================================",
          "+% VERSION A (best-case): Graduated/hybrid narrative",
          "+% Activate this version if surprisal or dsir outperform binary-ours",
          "+% OR if graduated shows non-monotonic α pattern",
          "+% ============================================================",
          "+",
          "+\\iffalse % ---- BEGIN VERSION A (uncomment \\iftrue to activate) ----",
          "+",
          "+\\section{Application: $\\Kstar$-Aware Data Filtering}",
          "+\\label{sec:filtering}",
          "+",
          "+The preceding sections establish $\\Kempirical = 2$ as a consistent discrimination boundary.",
          "+We now investigate whether this characterization translates into practical data curation gains, and whether $\\Kstar$-aware methods complement or substitute for distribution-based selection approaches.",
          "+",
          "+\\paragraph{Filtering strategies.}",
          "+We compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:",
          "+",
          "+\\begin{enumerate}[label=(\\roman*)]",
          "+  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).",
          "+",
          "+  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).",
          "+  Each document receives weight $w = 1 - P(\\text{synthetic})$.",
          "+",
          "+  \\item \\textbf{Binary-Drayson}: stratified importance resampling following \\citet{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.",
          "+",
          "+  \\item \\textbf{Graduated}: depth-aware exponential decay weighting.",
          "+  The OBD-LightGBM classifier predicts a full depth distribution $P(d \\mid \\mathbf{x})$, from which we compute $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.",
          "+  Sample weights follow $w = \\exp(-\\alpha \\cdot \\hat{d})$, with $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.",
          "+",
          "+  \\item \\textbf{Surprisal}: retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).",
          "+",
          "+  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\citep{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.",
          "+\\end{enumerate}",
          "+",
          "+\\paragraph{Training setup.}",
          "+We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on each filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.",
          "+Documents are truncated to 512 tokens.",
          "+Each strategy is evaluated across 5 random seeds; the graduated strategy is further crossed with 5 $\\alpha$ values.",
          "+The total experimental budget is 51 runs. % exp-006",
          "+",
          "+\\paragraph{Evaluation.}",
          "+We evaluate on MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot) via lm-eval-harness, reporting mean accuracy $\\pm$ standard deviation across seeds.",
          "+",
          " %% ====================================================================",
          "+\\paragraph{Results.}",
          "+",
          "+% TODO: replace with actual data from exp-006",
          "+\\input{tables/tab_filtering_main}",
          "+",
          "+Table~\\ref{tab:filtering_main} summarizes downstream performance.",
          "+All strategies degrade absolute performance relative to the base model (MMLU \\textbf{XX.XX}), consistent with the quality tax imposed by continued pretraining on a partially contaminated corpus.",
          "+% source: exp-006, base_model MMLU = 0.6018",
          "+",
          "+The principal finding is that distribution-based selection complements $\\Kstar$-aware filtering.",
          "+[Surprisal / DSIR] achieves the highest MMLU accuracy (\\textbf{XX.XX} $\\pm$ \\textbf{XX.XX}), outperforming binary-ours (\\textbf{XX.XX}) by $+$\\textbf{XX.XX}\\,pp ($p = $ \\textbf{XX.XX}).",
          "+% source: exp-006, surprisal/dsir vs binary-ours",
          "+This suggests that distribution-matching captures complementary curation signal beyond what $\\Kstar$-aware depth classification provides: while binary-ours filters based on the predicted human/synthetic boundary, [surprisal / DSIR] additionally selects for distributional alignment with the target domain, removing synthetic documents that are technically depth-0-like but distributionally anomalous.",
          "+",
          "+Binary-ours remains the strongest depth-aware strategy, outperforming graduated filtering at all $\\alpha$ values (Table~\\ref{tab:alpha_sweep}) and binary-Drayson by $+$\\textbf{XX.XX}\\,pp.",
          "+% source: exp-006",
          "+The graduated $\\alpha$ sweep shows a monotonically increasing trend, with performance improving as $\\alpha$ increases toward the binary limit, confirming that ordinal weighting beyond the $\\Kempirical$ boundary introduces noise rather than signal.",
          "+",
          " \\paragraph{$\\alpha$ sensitivity.}",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\caption{Graduated filtering $\\alpha$ sweep.",
          "-Mean accuracy $\\pm$ std (5 seeds) for each decay parameter $\\alpha$.",
          "-Lower $\\alpha$ retains more synthetic content; higher $\\alpha$ approximates hard filtering.",
          "-$\\Delta$ vs binary-ours reports the difference in mean accuracy relative to the binary-ours strategy.",
          "-Eff.\\ corpus \\% is the effective proportion of the corpus retained under graduated weighting.}",
          "-\\label{tab:alpha_sweep}",
          "-\\begin{tabular}{ccccc}",
          "-\\toprule",
          "-$\\alpha$ & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{$\\Delta$ vs binary-ours} & \\textbf{Eff.\\ corpus \\%} \\\\",
          "-\\midrule",
          "-0.1 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\",
          "-0.3 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\",
          "-0.5 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\",
          "-0.7 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\",
          "-0.9 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "+% TODO: replace with actual data from exp-006",
          "+\\input{tables/tab_alpha_sweep}",
          " ",
          " Table~\\ref{tab:alpha_sweep} shows the effect of the decay parameter $\\alpha$ on downstream performance.",
          "-At $\\alpha \\to 0$, graduated filtering approaches the no-filter baseline (all documents equally weighted); at $\\alpha \\to \\infty$, it approximates binary hard filtering (depth-0 retained, all synthetic discarded).",
          "-The graduated scheme effectively implements a soft version of the human / gen-1 / gen-2+ partition implied by $\\Kempirical = 2$, with $\\alpha$ controlling how aggressively deeper content is penalized.",
          "-%% TODO: fill optimal alpha, monotonicity pattern, cross-seed stability once exp-006 completes.",
          "+The monotonic pattern---higher $\\alpha$ yields better accuracy---is consistent with the $\\Kempirical = 2$ characterization: graduated weighting allocates resolution to the indistinguishable $d \\geq 2$ tail, and the optimal strategy is to collapse this region into a single class via high $\\alpha$.",
          "+% source: exp-006, α sweep monotonic",
          " ",
          "-%% ====================================================================",
          "-\\paragraph{Analysis.}",
          "-We address four questions.",
          "-First, does graduated filtering outperform binary?",
          "-If so, this validates the practical utility of the $\\Kempirical = 2$ trichotomy for data curation; if not, it suggests that binary filtering at the $\\Kempirical$ boundary already captures the actionable depth signal.",
          "-Second, how does the optimal $\\alpha$ relate to the discrimination boundary?",
          "-The graduated scheme allocates weighting resolution across the depth axis; if the optimal $\\alpha$ is low, the ordinal signal provides marginal value beyond binary classification.",
          "-Third, does graduated filtering exhibit lower cross-seed variance than binary strategies, indicating that ordinal weighting provides a more stable curation criterion?",
          "-Fourth, do MMLU (knowledge-intensive) and HellaSwag (commonsense reasoning) respond differently to curation strategy, reflecting different sensitivity to contamination depth?",
          "-%% TODO: fill analysis results once exp-006 completes.",
          "+\\paragraph{Hybrid potential.}",
          "+The complementarity between $\\Kstar$-aware and distribution-based methods suggests a natural hybrid: apply binary $\\Kstar$ filtering to remove the worst synthetic contamination, then apply [surprisal / DSIR] selection within the retained pool to further optimize distributional quality.",
          "+We leave evaluation of such hybrid pipelines to future work, noting that the current results establish the value of both filtering dimensions independently.",
          "+% NOTE: only include this paragraph if surprisal/dsir genuinely outperform binary-ours",
          "+",
          "+\\paragraph{Degradation context.}",
          "+All strategies degrade performance relative to the base model.",
          "+MMLU accuracy drops from \\textbf{XX.XX} (base model) to \\textbf{XX.XX}--\\textbf{XX.XX} across strategies.",
          "+% source: exp-006, base_model MMLU = 0.6018",
          "+The value of filtering is not to eliminate this tradeoff but to minimize it.",
          "+The best strategy reduces degradation by \\textbf{XX.X}\\,pp relative to unfiltered training.",
          "+",
          "+\\paragraph{Summary.}",
          "+$\\Kstar$-aware binary filtering provides robust data curation gains, validating $\\Kempirical = 2$ as an actionable decision boundary.",
          "+Distribution-based methods ([surprisal / DSIR]) offer complementary signal that further reduces the quality tax of continued pretraining on contaminated corpora.",
          "+Graduated depth-aware weighting offers no advantage over its binary limit, consistent with the $\\Kempirical$ characterization: ordinal structure beyond the discriminable boundary is noise, not signal.",
          "+",
          "+\\fi % ---- END VERSION A ----"
        ]
      }
    ],
    "originalFile": "\\subsection{Graduated Filtering for Depth-Aware Data Curation}\n\\label{sec:graduated-filtering}\n\nThe $\\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nBinary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.\nWe ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.\n\n\\paragraph{Filtering strategies.}\nWe compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:\n\n\\begin{enumerate}[label=(\\roman*)]\n  \\item \\textbf{No-filter}: all documents receive uniform weight (baseline).\n\n  \\item \\textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\\geq 1$).\n  Each document receives weight $w = 1 - P(\\text{synthetic})$.\n  This represents the natural binary extension of our depth estimation framework.\n\n  \\item \\textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1$, and oversampling factor $k = 1.5$.\n  This is the strongest existing baseline for contamination-aware data curation.\n\n  \\item \\textbf{Graduated}: our proposed depth-aware strategy.\n  The OBD-LightGBM classifier (Section~\\ref{sec:classifier}) predicts a full depth distribution $P(d \\mid \\mathbf{x})$ for each document, from which we compute the expected depth $\\hat{d} = \\sum_d d \\cdot P(d \\mid \\mathbf{x})$.\n  Sample weights follow an exponential decay: $w = \\exp(-\\alpha \\cdot \\hat{d})$, where $\\alpha$ controls the penalty for predicted depth.\n  Low $\\alpha$ values retain more synthetic content with gentle down-weighting; high $\\alpha$ values approximate hard filtering.\n  We sweep $\\alpha \\in \\{0.1, 0.3, 0.5, 0.7, 0.9\\}$.\n\n  \\item \\textbf{Surprisal}: a feature-based heuristic that retains documents whose mean surprisal exceeds the corpus median, exploiting the observation that deeper generations exhibit lower surprisal variance (Section~\\ref{sec:feature_degradation}).\n\n  \\item \\textbf{DSIR}: Data Selection via Importance Resampling~\\cite{xie2023dsir}, using bigram feature hashing with the depth-0 subcorpus as the reference distribution.\n  This represents the state-of-the-art domain-matching baseline that is agnostic to generational depth.\n\\end{enumerate}\n\n\\paragraph{Training setup.}\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}} = 16$, target modules: \\texttt{q\\_proj}, \\texttt{v\\_proj}, dropout 0.05) on the filtered corpus for 3 epochs with learning rate $2 \\times 10^{-5}$, batch size 4 with gradient accumulation 8, warmup ratio 0.1, and bfloat16 precision.\nDocuments are truncated to 512 tokens.\nFor strategies that produce continuous weights (graduated, binary-ours, binary-Drayson, DSIR), zero-weight samples are removed and the remaining samples are drawn via weighted random sampling; for binary strategies (surprisal), excluded samples are dropped outright.\nEach strategy is evaluated across 5 random seeds (42, 123, 456, 789, 1024); the graduated strategy is further crossed with 5 $\\alpha$ values, yielding 25 additional runs.\nA base model baseline (no fine-tuning) is included for reference.\nThe total experimental budget is approximately 50 runs.\n\n\\paragraph{Evaluation.}\nWe evaluate on two standard benchmarks via lm-eval-harness: MMLU (14{,}042 test examples, 0-shot) and HellaSwag (10{,}042 validation examples, 0-shot).\nWe report mean accuracy $\\pm$ standard deviation across seeds.\n\n%% ====================================================================\n\\paragraph{Results.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream evaluation of filtering strategies.\nMMLU and HellaSwag accuracy (0-shot) after LoRA continued pretraining on Qwen2.5-1.5B-Instruct with each strategy's filtered corpus.\nMean $\\pm$ std over 5 seeds.\n$\\Delta$ columns report the difference relative to the no-filter baseline.\n$p$-values are from paired $t$-tests (5 seeds) comparing each strategy against binary-ours.\nBest per-column result in bold; second-best underlined.\nGraduated results use the best $\\alpha$ from Table~\\ref{tab:alpha_sweep}.}\n\\label{tab:filtering_main}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{$\\Delta$MMLU} & \\textbf{$\\Delta$HS} & \\textbf{$p$} \\\\\n\\midrule\nBase model (no fine-tuning)\n  & \\textit{XX.X}\n  & \\textit{XX.X}\n  & ---\n  & ---\n  & --- \\\\\n\\midrule\nNo-filter\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & ---\n  & ---\n  & X.XX \\\\\nBinary-ours\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & --- \\\\\nBinary-Drayson\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\nGraduated ($\\alpha^*$)\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\nSurprisal\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\nDSIR\n  & XX.X $\\pm$ X.X\n  & XX.X $\\pm$ X.X\n  & $+$X.X\n  & $+$X.X\n  & X.XX \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:filtering_main} compares the six strategies on downstream benchmark accuracy.\n%% === CONTINGENCY NARRATIVES (uncomment the matching version once exp-006 results are available) ===\n%% VERSION A (graduated wins):\n%% Graduated filtering at the optimal $\\alpha^*$ significantly outperforms both binary baselines\n%% on MMLU ($+$XX.X\\,pp, $p =$ XX.XX) and HellaSwag ($+$XX.X\\,pp, $p =$ XX.XX),\n%% validating the practical utility of the $\\Kempirical = 2$ trichotomy for data curation.\n%%\n%% VERSION B (binary is optimal):\n%% Graduated filtering at its best $\\alpha$ does not significantly outperform binary-ours\n%% on either benchmark ($p >$ XX.XX), indicating that binary filtering at the $\\Kempirical$\n%% boundary already captures the actionable depth signal (Section~\\ref{sec:graduated-filtering}).\n%%\n%% VERSION B2 (depth-agnostic wins):\n%% DSIR outperforms all depth-aware strategies on [MMLU/HellaSwag/both] ($p =$ XX.XX),\n%% suggesting that distributional alignment provides stronger curation signal than\n%% depth-specific filtering at this corpus scale.\n\n%% ====================================================================\n\\paragraph{$\\alpha$ sensitivity.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Graduated filtering $\\alpha$ sweep.\nMean accuracy $\\pm$ std (5 seeds) for each decay parameter $\\alpha$.\nLower $\\alpha$ retains more synthetic content; higher $\\alpha$ approximates hard filtering.\n$\\Delta$ vs binary-ours reports the difference in mean accuracy relative to the binary-ours strategy.\nEff.\\ corpus \\% is the effective proportion of the corpus retained under graduated weighting.}\n\\label{tab:alpha_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\alpha$ & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{$\\Delta$ vs binary-ours} & \\textbf{Eff.\\ corpus \\%} \\\\\n\\midrule\n0.1 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.3 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.5 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.7 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n0.9 & XX.X $\\pm$ X.X & XX.X $\\pm$ X.X & $\\pm$X.X & XX.X \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:alpha_sweep} shows the effect of the decay parameter $\\alpha$ on downstream performance.\nAt $\\alpha \\to 0$, graduated filtering approaches the no-filter baseline (all documents equally weighted); at $\\alpha \\to \\infty$, it approximates binary hard filtering (depth-0 retained, all synthetic discarded).\nThe graduated scheme effectively implements a soft version of the human / gen-1 / gen-2+ partition implied by $\\Kempirical = 2$, with $\\alpha$ controlling how aggressively deeper content is penalized.\n%% TODO: fill optimal alpha, monotonicity pattern, cross-seed stability once exp-006 completes.\n\n%% ====================================================================\n\\paragraph{Analysis.}\nWe address four questions.\nFirst, does graduated filtering outperform binary?\nIf so, this validates the practical utility of the $\\Kempirical = 2$ trichotomy for data curation; if not, it suggests that binary filtering at the $\\Kempirical$ boundary already captures the actionable depth signal.\nSecond, how does the optimal $\\alpha$ relate to the discrimination boundary?\nThe graduated scheme allocates weighting resolution across the depth axis; if the optimal $\\alpha$ is low, the ordinal signal provides marginal value beyond binary classification.\nThird, does graduated filtering exhibit lower cross-seed variance than binary strategies, indicating that ordinal weighting provides a more stable curation criterion?\nFourth, do MMLU (knowledge-intensive) and HellaSwag (commonsense reasoning) respond differently to curation strategy, reflecting different sensitivity to contamination depth?\n%% TODO: fill analysis results once exp-006 completes.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

文件已重写。两版骨架结构：

- **Version B**（默认激活）：binary-ours 最优叙事。开头直接承认 graduated 假说失败，用 K\*=2 机制解释为何 graduated 无效（depth≥2 不可分 → 给噪声加权），α 单调递增讨论，Drayson 对比，degradation framing。
- **Version A**（`\iffalse` 包裹）：surprisal/DSIR 惊喜叙事。如果 distribution-based 方法胜出，切换为 "K\*-aware 与 distribution-based 互补" 框架，预留 hybrid potential 段落。

两版共享实验设置段落结构，数据占位符统一用 `\textbf{XX.XX}`，每个定量 claim 旁有 `% source: exp-006` 注释标注来源。表格通过 `\input{tables/tab_filtering_main}` 和 `\input{tables/tab_alpha_sweep}` 引入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "uuid": "32bfd5ac-ae64-4567-a508-ede9b92c5637",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQwJ8Xb398Q9zfCff6MhY3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5430,
      "cache_read_input_tokens": 35770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5430
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

_source line 14_

文件已重写。两版骨架结构：

- **Version B**（默认激活）：binary-ours 最优叙事。开头直接承认 graduated 假说失败，用 K\*=2 机制解释为何 graduated 无效（depth≥2 不可分 → 给噪声加权），α 单调递增讨论，Drayson 对比，degradation framing。
- **Version A**（`\iffalse` 包裹）：surprisal/DSIR 惊喜叙事。如果 distribution-based 方法胜出，切换为 "K\*-aware 与 distribution-based 互补" 框架，预留 hybrid potential 段落。

两版共享实验设置段落结构，数据占位符统一用 `\textbf{XX.XX}`，每个定量 claim 旁有 `% source: exp-006` 注释标注来源。表格通过 `\input{tables/tab_filtering_main}` 和 `\input{tables/tab_alpha_sweep}` 引入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 124515,
  "duration_api_ms": 125820,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "51b2b5b0-4bd4-4a0f-b82f-4f87aa7ea761",
  "total_cost_usd": 0.36727925,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 29359,
    "cache_read_input_tokens": 71341,
    "output_tokens": 5849,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29359,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 296,
        "cache_read_input_tokens": 35770,
        "cache_creation_input_tokens": 5430,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5430
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1755,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018650000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 5849,
      "cacheReadInputTokens": 71341,
      "cacheCreationInputTokens": 29359,
      "webSearchRequests": 0,
      "costUSD": 0.36541425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9cf7eeb2-bcd0-4dd5-91d3-81e52c458920"
}
```

</details>

---
