# paper round3 method

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_round3-method_20260516T044714.log`
- **Structured JSON:** [`8355bc6aaa5604b98fcc.json`](../../sessions/83/8355bc6aaa5604b98fcc.json)

## Before a recorded user message

28 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
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
  "uuid": "be4a4bea-db6d-4627-97bc-154c8a1cd31c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778923800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fc84f6ca-a3f8-4ccc-b71a-3258cca1b0ab",
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496"
}
```

---

### Assistant

_source line 4_

Reading method.tex first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "278a71b7-c910-409f-9041-d46e53a1f0ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01992UeJEypE2i8JiDY7pViC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12894,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12894
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

<details open><summary>🔧 Tool call — Read · `toolu_01GKB1Qy1K2Pg7YNrYcdHEmz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "bb90f7ab-f783-4adc-a7f0-3bc8e27e22a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01992UeJEypE2i8JiDY7pViC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12894,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12894
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

_source line 6 · 2026-05-16T04:47:26.170Z_

<details><summary>↩ Tool result · `toolu_01GKB1Qy1K2Pg7YNrYcdHEmz`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}.
17	This selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
22	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
23	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
24	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
25	The resulting dataset contains approximately 27{,}000 texts across all generators and depths.
26	For classification, depths 2--4 are collapsed into the $2{+}$ class.
27	
28	\subsection{Feature Extraction}
29	\label{sec:features}
30	
31	The seven features are motivated by two complementary views of distributional drift.
32	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
33	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
34	This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
35	
36	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
37	
38	\paragraph{Reference-model features.}
39	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
40	Although Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).
41	From the resulting NLL sequence, we extract five statistics:
42	\begin{itemize}[nosep,leftmargin=*]
43	    \item \textbf{entropy\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;
44	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;
45	    \item \textbf{entropy\_max}: maximum token-level NLL, capturing the most surprising token;
46	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.
47	    Although entropy\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\Delta$F1\,=\,+0.01\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;
48	    \item \textbf{tail\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.
49	    The 90th percentile threshold follows standard practice in heavy-tail analysis \cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\,pp) across thresholds from the 85th to 95th percentile.
50	\end{itemize}
51	
52	\paragraph{Surface features.}
53	Two features capture lexical diversity without requiring a reference model:
54	\begin{itemize}[nosep,leftmargin=*]
55	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
56	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
57	\end{itemize}
58	
59	\paragraph{Feature complementarity.}
60	The grouping reflects an empirical pattern we term \emph{differential depth response}: central-tendency and diversity features (entropy\_mean, TTR, hapax\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\_std, tail\_decay) remain near-stationary.
61	This differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.
62	As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
63	
64	\subsection{Evaluation Protocol}
65	\label{sec:evaluation}
66	
67	\paragraph{Cross-validation.}
68	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.
69	We additionally report \textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.
70	
71	\paragraph{Classifier.}
72	We use XGBoost \cite{xgboost} as the classifier throughout.
73	Gradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.
74	We use $n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.
75	Baseline detectors (\S\ref{sec:results-baselines}) use the same XGBoost framework with $n\_\text{estimators}{=}100$ and $\max\_\text{depth}{=}3$ to avoid overfitting their single-feature input.
76	LOGO F1 is stable across random seeds (mean\,=\,0.789, std\,=\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.
77	Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.
78	We evaluated two ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall ordinal ensemble \cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.
79	
80	\paragraph{Metrics and statistical testing.}
81	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
82	We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).
83	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
84	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
85	All reported $p$-values are two-sided.
86	We report six pairwise comparisons in \S\ref{sec:results-baselines}; applying Bonferroni correction ($\alpha_{\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.
87	Feature--depth correlations (\S\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.
88	
89	\paragraph{Baselines.}
90	We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
91	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.
92	
93	\paragraph{Length confound control.}
94	Since TTR and hapax\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.
95	We conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "f35ef0c8-b19b-4230-8bff-978cd8155f08",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe resulting dataset contains approximately 27{,}000 texts across all generators and depths.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full method.tex. Let me analyze each issue:

**M1: Bootstrap CI type and resampling granularity**
In §3.4 (Evaluation Protocol), line 82 says: "We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples)."
Need to add: percentile bootstrap, resampling at document level.

**M2: Sample count 30000 vs 27529**


Line 25 mentions approximately 27,000 texts across all generators and depths, but I need to explain why the theoretical maximum of 30,000 doesn't match the actual 27,529 samples—likely due to filtering or generation failures that should be documented.

**M3: tail_decay citation**
Line 49 cites ood_baseline for the 90th percentile threshold in heavy-tail analysis, but that reference is about OOD detection, not heavy-tail methodology, so I should remove it.

**M5: entropy_* naming confusion**
Need to add a footnote clarifying what "entropy" refers to in this context.

I'm making these four corrections now—fixing the dataset size explanation, removing the mismatched citation, and clarifying the entropy terminology at its first mention around line 43.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "3ca1c543-41ca-451c-a156-5d635aacc2a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017D5mHDoKFbQtUDa6oXKavk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2989,
      "cache_read_input_tokens": 24735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2989
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

_source line 8_

Four targeted edits needed. Let me apply them.

**M1** — Add bootstrap details to line 82.
**M2** — Explain sample count gap near line 25.
**M3** — Remove incorrect citation on line 49.
**M5** — Add footnote at first entropy feature mention (line 43).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "a3e02ddf-1297-4102-ab31-867ba3c33cf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017D5mHDoKFbQtUDa6oXKavk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2989,
      "cache_read_input_tokens": 24735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2989
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01AXhpeGodjoBBUjLsqJuvfN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "old_string": "\tWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).",
  "new_string": "\tWe report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "87ccd036-8cec-41fa-8138-6258c7b849c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017D5mHDoKFbQtUDa6oXKavk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2989,
      "cache_read_input_tokens": 24735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2989
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

_source line 10 · 2026-05-16T04:47:37.410Z_

<details><summary>↩ Tool result · reported error · `toolu_01AXhpeGodjoBBUjLsqJuvfN`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: 	We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "e40b5b16-8b1d-476b-ac7a-3cced26f34bc",
  "tool_use_result": "Error: String to replace not found in file.\nString: \tWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples)."
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01BLMqVCEWgTnydAPkh3w2EN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "offset": 80,
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
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "46a44aa8-a95f-4808-8f92-a713df51ce02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxYe1p3guy7Kfzb8QfeeX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 27724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

_source line 12 · 2026-05-16T04:47:40.065Z_

<details><summary>↩ Tool result · `toolu_01BLMqVCEWgTnydAPkh3w2EN`</summary>

```text
80	\paragraph{Metrics and statistical testing.}
81	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
82	We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).
83	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
84	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
85	All reported $p$-values are two-sided.
86	We report six pairwise comparisons in \S\ref{sec:results-baselines}; applying Bonferroni correction ($\alpha_{\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.
87	Feature--depth correlations (\S\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.
88	
89	\paragraph{Baselines.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "5bce92cf-bac8-4acb-90c5-97449ad5cff4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}",
      "numLines": 10,
      "startLine": 80,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01WjcF9deMVBFoVi3GscijRt`</summary>

```json
{
  "command": "cat -A \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex\" | sed -n '82p'",
  "description": "Check exact whitespace on line 82"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "6e523cc0-ff64-440a-9bb8-116155c7d4e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRfyWToooYkWxbyFvrbv6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 28454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
      },
      "output_tokens": 57,
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

_source line 14 · 2026-05-16T04:47:43.637Z_

<details><summary>↩ Tool result · `toolu_01WjcF9deMVBFoVi3GscijRt`</summary>

```text
We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).$
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "c767ebff-3743-4878-95d3-c6b3b04524df",
  "tool_use_result": {
    "stdout": "We report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).$",
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

_source line 15_

No leading tab. Let me apply all four edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "d152aa4e-2e75-45ab-968d-aa948b9fbdf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XScUwRvsy1vvuN6atH9SZG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 28900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 170
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

<details open><summary>🔧 Tool call — Edit · `toolu_019SMcfGJgVRRGrCUZ5XjS3s`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "old_string": "We report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).",
  "new_string": "We report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "a9cc80f5-6821-4362-9542-8acf0e4b710b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XScUwRvsy1vvuN6atH9SZG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 28900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 170
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

_source line 17 · 2026-05-16T04:47:47.418Z_

<details><summary>↩ Tool result · `toolu_019SMcfGJgVRRGrCUZ5XjS3s`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "bdb7dade-13aa-44c2-bbd7-253e442cb4ac",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "oldString": "We report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).",
    "newString": "We report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe resulting dataset contains approximately 27{,}000 texts across all generators and depths.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
    "structuredPatch": [
      {
        "oldStart": 79,
        "oldLines": 7,
        "newStart": 79,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Metrics and statistical testing.}",
          " The primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.",
          "-We report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).",
          "+We report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.",
          " For pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.",
          " For comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.",
          " All reported $p$-values are two-sided."
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

<details open><summary>🔧 Tool call — Edit · `toolu_01BUQHc1XtzfXpoDDrRmqyLR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "old_string": "The resulting dataset contains approximately 27{,}000 texts across all generators and depths.",
  "new_string": "The theoretical yield is $6 \\times {\\sim}1{,}000 \\times 5 \\approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "027789a8-c2e5-4394-abd9-e440f6188d6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6w4NRrXpNw4112KfmisVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 29070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 297
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

_source line 19 · 2026-05-16T04:47:53.321Z_

<details><summary>↩ Tool result · `toolu_01BUQHc1XtzfXpoDDrRmqyLR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "53fbddda-2d11-4b70-b426-9ce49b481dd9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "oldString": "The resulting dataset contains approximately 27{,}000 texts across all generators and depths.",
    "newString": "The theoretical yield is $6 \\times {\\sim}1{,}000 \\times 5 \\approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe resulting dataset contains approximately 27{,}000 texts across all generators and depths.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " We address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).",
          " Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.",
          " All generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.",
          "-The resulting dataset contains approximately 27{,}000 texts across all generators and depths.",
          "+The theoretical yield is $6 \\times {\\sim}1{,}000 \\times 5 \\approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain.",
          " For classification, depths 2--4 are collapsed into the $2{+}$ class.",
          " ",
          " \\subsection{Feature Extraction}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LkvfECTZpTPi7vpBDtSMgt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "old_string": "The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.",
  "new_string": "Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "f5023471-3017-43c6-9add-4601e6a71f4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WDa7gphq5JRsNtTFxdrSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 29367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
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

_source line 21 · 2026-05-16T04:47:57.624Z_

<details><summary>↩ Tool result · `toolu_01LkvfECTZpTPi7vpBDtSMgt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "2c56d355-a4c1-44f4-8f92-59e5f15f3a1b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "oldString": "The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.",
    "newString": "Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe theoretical yield is $6 \\times {\\sim}1{,}000 \\times 5 \\approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          "     \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.",
          "     Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;",
          "     \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.",
          "-    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.",
          "+    Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.",
          " \\end{itemize}",
          " ",
          " \\paragraph{Surface features.}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01A7c8HargEz6bz5ZFXzBm93`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "old_string": "    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;",
  "new_string": "    \\item \\textbf{entropy\\_mean}\\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "fdc38cd1-fd77-4d4b-85a1-f7cfcb9484c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pe5dWhuG75xkH6DNfUXD42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 29649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 23 · 2026-05-16T04:48:02.753Z_

<details><summary>↩ Tool result · `toolu_01A7c8HargEz6bz5ZFXzBm93`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "a8eec017-53dc-4297-8a23-55f40fef8620",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "oldString": "    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;",
    "newString": "    \\item \\textbf{entropy\\_mean}\\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe theoretical yield is $6 \\times {\\sim}1{,}000 \\times 5 \\approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " Although Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).",
          " From the resulting NLL sequence, we extract five statistics:",
          " \\begin{itemize}[nosep,leftmargin=*]",
          "-    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;",
          "+    \\item \\textbf{entropy\\_mean}\\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;",
          "     \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;",
          "     \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;",
          "     \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs."
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

All four edits applied. Let me verify the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "fb51d695-6f64-4631-9578-9d18579861e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JthkW4kq1CQEAEUA3HkZW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 30051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 312
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01EgzM1EjSZe2arc3cK4gRib`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "59998b4a-f034-4d89-86da-189d3943f5dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JthkW4kq1CQEAEUA3HkZW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 30051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 312
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

_source line 26 · 2026-05-16T04:48:05.353Z_

<details><summary>↩ Tool result · `toolu_01EgzM1EjSZe2arc3cK4gRib`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}.
17	This selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
22	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
23	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
24	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
25	The theoretical yield is $6 \times {\sim}1{,}000 \times 5 \approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain.
26	For classification, depths 2--4 are collapsed into the $2{+}$ class.
27	
28	\subsection{Feature Extraction}
29	\label{sec:features}
30	
31	The seven features are motivated by two complementary views of distributional drift.
32	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
33	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
34	This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
35	
36	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
37	
38	\paragraph{Reference-model features.}
39	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
40	Although Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).
41	From the resulting NLL sequence, we extract five statistics:
42	\begin{itemize}[nosep,leftmargin=*]
43	    \item \textbf{entropy\_mean}\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;
44	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;
45	    \item \textbf{entropy\_max}: maximum token-level NLL, capturing the most surprising token;
46	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.
47	    Although entropy\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\Delta$F1\,=\,+0.01\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;
48	    \item \textbf{tail\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.
49	    Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\,pp) across thresholds from the 85th to 95th percentile.
50	\end{itemize}
51	
52	\paragraph{Surface features.}
53	Two features capture lexical diversity without requiring a reference model:
54	\begin{itemize}[nosep,leftmargin=*]
55	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
56	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
57	\end{itemize}
58	
59	\paragraph{Feature complementarity.}
60	The grouping reflects an empirical pattern we term \emph{differential depth response}: central-tendency and diversity features (entropy\_mean, TTR, hapax\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\_std, tail\_decay) remain near-stationary.
61	This differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.
62	As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
63	
64	\subsection{Evaluation Protocol}
65	\label{sec:evaluation}
66	
67	\paragraph{Cross-validation.}
68	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.
69	We additionally report \textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.
70	
71	\paragraph{Classifier.}
72	We use XGBoost \cite{xgboost} as the classifier throughout.
73	Gradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.
74	We use $n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.
75	Baseline detectors (\S\ref{sec:results-baselines}) use the same XGBoost framework with $n\_\text{estimators}{=}100$ and $\max\_\text{depth}{=}3$ to avoid overfitting their single-feature input.
76	LOGO F1 is stable across random seeds (mean\,=\,0.789, std\,=\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.
77	Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.
78	We evaluated two ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall ordinal ensemble \cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.
79	
80	\paragraph{Metrics and statistical testing.}
81	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
82	We report per-class F1 scores and 95\% confidence intervals via \emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.
83	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
84	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
85	All reported $p$-values are two-sided.
86	We report six pairwise comparisons in \S\ref{sec:results-baselines}; applying Bonferroni correction ($\alpha_{\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.
87	Feature--depth correlations (\S\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.
88	
89	\paragraph{Baselines.}
90	We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
91	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.
92	
93	\paragraph{Length confound control.}
94	Since TTR and hapax\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.
95	We conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "62d96d8d-0632-44e8-9588-cf6ef8652e1d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe theoretical yield is $6 \\times {\\sim}1{,}000 \\times 5 \\approx 30{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 27{,}529 texts remain.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}\\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% confidence intervals via \\emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

All four issues fixed, no orphaned `\cite{}`, LaTeX syntax correct. Summary of changes:

- **M1** (line 82): replaced vague "bootstrap CI" with "percentile bootstrap, resampling at the document level within each held-out fold"
- **M2** (line 25): replaced "approximately 27,000" with explicit theoretical yield formula ($6 \times \sim1000 \times 5 \approx 30{,}000$) and filtering explanation yielding 27,529
- **M3** (line 49): removed incorrect `\cite{ood_baseline}` and "follows standard practice in heavy-tail analysis" phrasing; kept only the sensitivity analysis sentence
- **M5** (line 43): added footnote on `entropy_mean` clarifying these are point-wise NLL values, not Shannon entropy

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "uuid": "d455b7c4-e7bf-43d5-9b7c-05bf3a1dfb46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P663oz5nzd7npHRWZx79SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3084,
      "cache_read_input_tokens": 30363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3084
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

_source line 28_

All four issues fixed, no orphaned `\cite{}`, LaTeX syntax correct. Summary of changes:

- **M1** (line 82): replaced vague "bootstrap CI" with "percentile bootstrap, resampling at the document level within each held-out fold"
- **M2** (line 25): replaced "approximately 27,000" with explicit theoretical yield formula ($6 \times \sim1000 \times 5 \approx 30{,}000$) and filtering explanation yielding 27,529
- **M3** (line 49): removed incorrect `\cite{ood_baseline}` and "follows standard practice in heavy-tail analysis" phrasing; kept only the sensitivity analysis sentence
- **M5** (line 43): added footnote on `entropy_mean` clarifying these are point-wise NLL values, not Shannon entropy

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 50841,
  "duration_api_ms": 52044,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "6d5caa54-f1e4-4d95-8267-364d58419496",
  "total_cost_usd": 0.3277695,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 21606,
    "cache_read_input_tokens": 270154,
    "output_tokens": 2232,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21606,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 200,
        "cache_read_input_tokens": 30363,
        "cache_creation_input_tokens": 3084,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3084
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1695,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001795,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 2232,
      "cacheReadInputTokens": 270154,
      "cacheCreationInputTokens": 21606,
      "webSearchRequests": 0,
      "costUSD": 0.32597449999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ab096722-5979-438a-afdc-cccddd0bb5c2"
}
```

</details>

---
