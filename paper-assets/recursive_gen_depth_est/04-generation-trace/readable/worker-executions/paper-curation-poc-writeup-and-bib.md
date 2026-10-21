# paper curation poc writeup and bib

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log`
- **Structured JSON:** [`bddff14d4817e9d5ed3e.json`](../../sessions/bd/bddff14d4817e9d5ed3e.json)

## Before a recorded user message

60 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
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
  "uuid": "d7a044aa-6369-471d-a91c-2535d4fd26af",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
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
    "resetsAt": 1778903400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "419b91c0-aa54-4e91-915a-f0dbd26bceb4",
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down into parallel tasks where possible. I need to:

1. Task A: Edit discussion.tex and section_appendix.tex
2. Task B1: Search for arXiv 2410.04840 and fix bib
3. Task B2: Sync artifacts bib

Let me start by reading the relevant files and doing the web search in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e6238950-0b24-4120-8154-e90e972affda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 5_

先读取所有相关文件并搜索论文信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "c0d55e3a-2f86-4b0d-9780-48d4a2d4b04f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_019NBXg1op16Z3DLUJTe73hX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "d5ee8372-1357-41ae-807e-636eb20007ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 7 · 2026-05-15T23:54:57.191Z_

<details><summary>↩ Tool result · `toolu_019NBXg1op16Z3DLUJTe73hX`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	The dominant pair (\texttt{p90\_ppl} top-2 in 9/9 cells, \texttt{var\_surprisal} in 8/9 under SHAP) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\cite{shumailov2024_nature}.
6	Recent work corroborates this connection, identifying entropy decline as a measurable signal of recursive degradation that parallels the tail erosion our features capture~\cite{shi2025_closer_look}.
7	
8	Cross-strategy transfer remains the primary bottleneck (59.1\% vs.\ 66.4\% cross-model), with the temperature-induced d1/d2 AUC inversion making single-classifier deployment across unknown decoding strategies infeasible.
9	A two-stage pipeline---first identifying the decoding strategy, then applying a strategy-conditioned depth classifier---could address this, though automating strategy identification from text alone requires independent validation.
10	
11	\paragraph{Depth-graduated data curation.}
12	Current data curation operates on a binary human-vs-machine distinction~\cite{dsir2023,qurating2024}.
13	Depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
14	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\S\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.
15	Importance weighting~\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\cite{yi2026_escaping_collapse}.
16	The downstream effect on training quality remains to be validated empirically.
17	
18	\paragraph{Toward a provenance toolkit.}
19	Depth estimation complements existing provenance methods along orthogonal axes.
20	Watermarking~\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
21	Source attribution~\cite{uchendu2020_attribution} identifies the generating model but not the generation history.
22	Bevendorff et al.\ distinguish attribution from verification as two fundamental detection paradigms~\cite{bevendorff2025_two_paradigms}; depth estimation represents a complementary third axis that characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
23	A layered provenance system combining watermark presence, source model, and recursive depth could support more nuanced data auditing than any single method.
24	
25	\paragraph{Limitations and future directions.}
26	Real-world documents may interleave passages at mixed recursive depths within a single document; our passage-level classifier assumes uniform depth, and extending to segment-level estimation introduces a granularity--statistical-power tradeoff that remains unexplored.
27	Web-crawl deployment requires model-specific calibration (C4 FPR: 4.7--22.4\%; Table~\ref{tab:calibration}), and all experiments use 1--1.5B models.
28	Future work should validate on mixed-domain corpora at larger scales and evaluate whether depth-graduated curation, with appropriate strategy conditioning, improves downstream training outcomes.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "34bd7c65-1912-4ec1-8b12-c3c9af134830",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nWe formalized recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70--85\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.\nThe dominant pair (\\texttt{p90\\_ppl} top-2 in 9/9 cells, \\texttt{var\\_surprisal} in 8/9 under SHAP) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\\cite{shumailov2024_nature}.\nRecent work corroborates this connection, identifying entropy decline as a measurable signal of recursive degradation that parallels the tail erosion our features capture~\\cite{shi2025_closer_look}.\n\nCross-strategy transfer remains the primary bottleneck (59.1\\% vs.\\ 66.4\\% cross-model), with the temperature-induced d1/d2 AUC inversion making single-classifier deployment across unknown decoding strategies infeasible.\nA two-stage pipeline---first identifying the decoding strategy, then applying a strategy-conditioned depth classifier---could address this, though automating strategy identification from text alone requires independent validation.\n\n\\paragraph{Depth-graduated data curation.}\nCurrent data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.\nDepth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.\nImportance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.\nThe downstream effect on training quality remains to be validated empirically.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking~\\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution~\\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nBevendorff et al.\\ distinguish attribution from verification as two fundamental detection paradigms~\\cite{bevendorff2025_two_paradigms}; depth estimation represents a complementary third axis that characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining watermark presence, source model, and recursive depth could support more nuanced data auditing than any single method.\n\n\\paragraph{Limitations and future directions.}\nReal-world documents may interleave passages at mixed recursive depths within a single document; our passage-level classifier assumes uniform depth, and extending to segment-level estimation introduces a granularity--statistical-power tradeoff that remains unexplored.\nWeb-crawl deployment requires model-specific calibration (C4 FPR: 4.7--22.4\\%; Table~\\ref{tab:calibration}), and all experiments use 1--1.5B models.\nFuture work should validate on mixed-domain corpora at larger scales and evaluate whether depth-graduated curation, with appropriate strategy conditioning, improves downstream training outcomes.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01WtP97Y1aoo3ZNnuX5bu8FM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "0a90b577-be27-4f6e-a85f-8eb86ecd8271",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 9 · 2026-05-15T23:54:58.066Z_

<details><summary>↩ Tool result · `toolu_01WtP97Y1aoo3ZNnuX5bu8FM`</summary>

```text
1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.83$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.
20	
21	\subsection{Per-Class Recall}
22	\label{app:per_class}
23	
24	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
25	Depth~0 recall exceeds 98\% uniformly.
26	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
32	\label{tab:per_class_recall}
33	\begin{tabular}{@{}lcccc@{}}
34	\toprule
35	Cell & d0 & d1 & d2 & d3 \\
36	\midrule
37	Pythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\
38	Pythia, $\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\
39	Pythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\
40	OLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\
41	OLMo, $\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\
42	OLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\
43	GPT-2~XL, nuc.     & 99.2 & 85.9 & \textbf{73.3} & 77.5 \\
44	GPT-2~XL, $\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\
45	GPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\
46	\bottomrule
47	\end{tabular}
48	\end{table}
49	
50	\subsection{DCOL Iteration Details}
51	\label{app:dcol_iterations}
52	
53	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
54	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\%.}
60	\label{tab:dcol_iterations}
61	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
62	\toprule
63	Ver. & Backbone & Config & Outcome \\
64	\midrule
65	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
66	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
67	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
68	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
69	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
70	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
75	\subsection{Feature Overlap Analysis}
76	\label{app:feature_overlap}
77	
78	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
79	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\textsc{var\_surprisal} and \textsc{p90\_ppl} yield negative $R^2$ under linear probing, indicating these features are not linearly accessible in the pretrained representation space.
80	This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\S\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
81	
82	\subsection{Domain Bias Analysis}
83	\label{app:domain_bias}
84	
85	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
86	
87	\paragraph{Methodological note.}
88	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
89	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
90	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
91	
92	\paragraph{Sub-A: Standard CV.}
93	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level), confirming that depth signal is the dominant classification factor.
94	
95	\paragraph{Sub-B: LOGO evaluation.}
96	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
97	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
98	Per-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.
99	
100	\paragraph{Sub-C: Negative control.}
101	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
102	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%---indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
103	The depth-to-seed-group accuracy ratio is 7.1$\times$, confirming that the feature representation encodes depth but not seed-article identity.
104	
105	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
106	
107	\subsection{Wild-Data Calibration}
108	\label{app:calibration}
109	
110	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages).
111	
112	\begin{table}[h]
113	\centering
114	\small
115	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+.}
116	\label{tab:calibration}
117	\begin{tabular}{@{}llrcc@{}}
118	\toprule
119	Model & Source & $n$ & d0 (\%) & FPR (\%) \\
120	\midrule
121	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 \\
122	 & C4 & 5{,}000 & 79.8 & 20.2 \\
123	\addlinespace
124	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 \\
125	 & C4 & 5{,}000 & 77.6 & 22.4 \\
126	\addlinespace
127	OLMo-1B & WikiText & 546 & 98.5 & 1.5 \\
128	 & C4 & 5{,}000 & 95.3 & 4.7 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy, confirming that editorial text is reliably distinguished from recursive generations across model families.
134	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
135	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
136	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
137	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%)---the non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
138	
139	\subsection{Extended Discussion}
140	\label{app:extended_discussion}
141	
142	\paragraph{Depth-graduated curation.}
143	Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
144	Recursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
145	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\S\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; the downstream effect on training quality remains to be validated empirically.
146	Importance weighting \cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.
147	
148	\paragraph{Toward a provenance toolkit.}
149	Depth estimation complements existing provenance methods along orthogonal axes.
150	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
151	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
152	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
153	A layered provenance system combining these three signals---watermark presence, source model, and recursive generation depth---could support more nuanced data auditing than any single method.
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "bea45102-2f01-4633-8856-ba79765c058d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\textsc{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\textsc{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\textsc{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\textsc{p75\\_ppl} displaces \\textsc{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.83$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.\n\n\\subsection{Per-Class Recall}\n\\label{app:per_class}\n\nTable~\\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).\nDepth~0 recall exceeds 98\\% uniformly.\nAmong generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-class recall (\\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}\n\\label{tab:per_class_recall}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCell & d0 & d1 & d2 & d3 \\\\\n\\midrule\nPythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\\\\nPythia, $\\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\\\\nPythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\\\\nOLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\\\\nOLMo, $\\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\\\\nOLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\\\\nGPT-2~XL, nuc.     & 99.2 & 85.9 & \\textbf{73.3} & 77.5 \\\\\nGPT-2~XL, $\\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\\\\nGPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing, indicating these features are not linearly accessible in the pretrained representation space.\nThis confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level), confirming that depth signal is the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}llrcc@{}}\n\\toprule\nModel & Source & $n$ & d0 (\\%) & FPR (\\%) \\\\\n\\midrule\nPythia-1.4B & WikiText & 546 & 100.0 & 0.0 \\\\\n & C4 & 5{,}000 & 79.8 & 20.2 \\\\\n\\addlinespace\nGPT-2~XL & WikiText & 546 & 99.3 & 0.7 \\\\\n & C4 & 5{,}000 & 77.6 & 22.4 \\\\\n\\addlinespace\nOLMo-1B & WikiText & 546 & 98.5 & 1.5 \\\\\n & C4 & 5{,}000 & 95.3 & 4.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn WikiText-103, all three classifiers achieve $\\geq$98.5\\% d0 accuracy, confirming that editorial text is reliably distinguished from recursive generations across model families.\nOn C4, FPR varies sharply: OLMo (4.7\\%) vs.\\ Pythia (20.2\\%) and GPT-2~XL (22.4\\%).\nC4 misclassifications concentrate in template and SEO content with elevated repetition features (\\texttt{rep\\_3gram} $+$37\\%, \\texttt{rep\\_4gram} $+$75\\% vs.\\ correctly classified d0 passages), rather than in random noise.\nThe model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.\nAmong C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\\%), d2 (3.7\\%), d3 (9.6\\%); for OLMo, d1 (2.9\\%), d2 (0.5\\%), d3 (1.3\\%)---the non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; the downstream effect on training quality remains to be validated empirically.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals---watermark presence, source model, and recursive generation depth---could support more nuanced data auditing than any single method.\n",
      "numLines": 154,
      "startLine": 1,
      "totalLines": 154
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01CLK6fyu4HEH9gdhKUVNU2o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "0bec7678-3843-4c42-8dc6-c332b922c94b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 11 · 2026-05-15T23:54:58.535Z_

<details><summary>↩ Tool result · `toolu_01CLK6fyu4HEH9gdhKUVNU2o`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2024_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2024},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
51	@misc{gerstgrasser2024_accumulate,
52	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
53	  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
54	  year      = {2024},
55	  howpublished = {arXiv:2404.01413},
56	  url       = {https://arxiv.org/abs/2404.01413},
57	}
58	
59	@inproceedings{marchi2024_heat_death,
60	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
61	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
62	  booktitle = {Proceedings of ICASSP},
63	  year      = {2024},
64	  note      = {arXiv:2404.02325},
65	  url       = {https://arxiv.org/abs/2404.02325},
66	}
67	
68	@misc{knowledge_collapse2025,
69	  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},
70	  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},
71	  year      = {2025},
72	  howpublished = {arXiv:2509.04796},
73	  url       = {https://arxiv.org/abs/2509.04796},
74	}
75	
76	@misc{sigma2026_spectral,
77	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
78	  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},
79	  year      = {2026},
80	  howpublished = {arXiv:2601.03385},
81	  url       = {https://arxiv.org/abs/2601.03385},
82	}
83	
84	@inproceedings{mohamed2025_broken_telephone,
85	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
86	  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
87	  booktitle = {Proceedings of ACL},
88	  year      = {2025},
89	  note      = {arXiv:2502.20258},
90	  url       = {https://arxiv.org/abs/2502.20258},
91	}
92	
93	@inproceedings{synthetic_eggs2026,
94	  author    = {Schaffelder, Max and Gatt, Albert},
95	  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},
96	  booktitle = {Findings of ACL},
97	  year      = {2026},
98	  note      = {arXiv:2511.01490},
99	  url       = {https://arxiv.org/abs/2511.01490},
100	}
101	
102	@inproceedings{shi2025_closer_look,
103	  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
104	  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},
105	  booktitle = {Advances in Neural Information Processing Systems},
106	  year      = {2025},
107	  note      = {Spotlight},
108	}
109	
110	@inproceedings{yi2026_escaping_collapse,
111	  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
112	  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},
113	  booktitle = {3rd DATA-FM Workshop at ICLR 2026},
114	  year      = {2026},
115	}
116	
117	% --- Model collapse: collapse-can-be-avoided / contamination ---
118	
119	@inproceedings{drayson2025_detection_prevents_collapse,
120	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
121	  title     = {{Machine-generated text detection prevents language model collapse}},
122	  booktitle = {Findings of EMNLP},
123	  year      = {2025},
124	  note      = {arXiv:2502.15654},
125	  url       = {https://arxiv.org/abs/2502.15654},
126	}
127	
128	@misc{bakshi2026_collapse_improvement,
129	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
130	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
131	  year      = {2026},
132	  howpublished = {arXiv:2602.10531},
133	  url       = {https://arxiv.org/abs/2602.10531},
134	}
135	
136	@misc{wang2026_contamination,
137	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
138	  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},
139	  year      = {2026},
140	  howpublished = {arXiv:2602.16065},
141	  url       = {https://arxiv.org/abs/2602.16065},
142	}
143	
144	@misc{falahati2026_curated,
145	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
146	  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},
147	  year      = {2026},
148	  howpublished = {arXiv:2605.07724},
149	  url       = {https://arxiv.org/abs/2605.07724},
150	}
151	
152	% ============================================================
153	% AI-Generated Text Detection
154	% ============================================================
155	
156	@article{wu2025_detection_survey,
157	  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
158	  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
159	  journal   = {Computational Linguistics},
160	  volume    = {51},
161	  number    = {1},
162	  pages     = {275--354},
163	  year      = {2025},
164	  publisher = {MIT Press},
165	}
166	
167	% --- Statistical / zero-shot detectors ---
168	
169	@inproceedings{gehrmann2019_gltr,
170	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
171	  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},
172	  booktitle = {Proceedings of ACL: System Demonstrations},
173	  year      = {2019},
174	  note      = {arXiv:1906.04043},
175	  url       = {https://arxiv.org/abs/1906.04043},
176	}
177	
178	@inproceedings{mitchell2023_detectgpt,
179	  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
180	  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
181	  booktitle = {Proceedings of ICML},
182	  year      = {2023},
183	  note      = {arXiv:2301.11305},
184	  url       = {https://arxiv.org/abs/2301.11305},
185	}
186	
187	@inproceedings{fast_detectgpt2024,
188	  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
189	  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
190	  booktitle = {Proceedings of ICLR},
191	  year      = {2024},
192	  note      = {arXiv:2310.05130},
193	  url       = {https://arxiv.org/abs/2310.05130},
194	}
195	
196	@inproceedings{binoculars2024,
197	  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
198	  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
199	  booktitle = {Proceedings of ICML},
200	  year      = {2024},
201	  note      = {arXiv:2401.12070},
202	  url       = {https://arxiv.org/abs/2401.12070},
203	}
204	
205	@article{diveye2026,
206	  author    = {Basani, Advik Raj and Chen, Pin-Yu},
207	  title     = {{Diversity Boosts AI-Generated Text Detection}},
208	  journal   = {Transactions on Machine Learning Research (TMLR)},
209	  year      = {2026},
210	  note      = {arXiv:2509.18880},
211	  url       = {https://arxiv.org/abs/2509.18880},
212	}
213	
214	% --- Robustness / limitations of detectors ---
215	
216	@misc{sadasivan2023_paraphrase,
217	  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
218	  title     = {{Can AI-Generated Text be Reliably Detected?}},
219	  year      = {2023},
220	  howpublished = {arXiv:2303.11156},
221	  url       = {https://arxiv.org/abs/2303.11156},
222	}
223	
224	@misc{pudasaini2026_detection_fails,
225	  author    = {Pudasaini, Shushanta and Miralles-Pech{\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},
226	  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},
227	  year      = {2026},
228	  howpublished = {arXiv:2603.23146},
229	  url       = {https://arxiv.org/abs/2603.23146},
230	}
231	
232	@misc{pu2026_generator_barrier,
233	  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
234	  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
235	  year      = {2026},
236	  howpublished = {arXiv:2604.13692},
237	  url       = {https://arxiv.org/abs/2604.13692},
238	}
239	
240	% --- Beyond binary: attribution, editing extent, benchmarks ---
241	
242	@inproceedings{bevendorff2025_two_paradigms,
243	  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},
244	  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},
245	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
246	  pages     = {3762--3787},
247	  year      = {2025},
248	  address   = {Vienna, Austria},
249	}
250	
251	@inproceedings{uchendu2020_attribution,
252	  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
253	  title     = {{Authorship Attribution for Neural Text Generation}},
254	  booktitle = {Proceedings of EMNLP},
255	  year      = {2020},
256	}
257	
258	@inproceedings{editlens2026,
259	  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},
260	  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},
261	  booktitle = {Proceedings of ICLR},
262	  year      = {2026},
263	  note      = {arXiv:2510.03154},
264	  url       = {https://arxiv.org/abs/2510.03154},
265	}
266	
267	@inproceedings{loki2025,
268	  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},
269	  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},
270	  booktitle = {Proceedings of ICLR (Spotlight)},
271	  year      = {2025},
272	  note      = {arXiv:2410.09732},
273	  url       = {https://arxiv.org/abs/2410.09732},
274	}
275	
276	% --- Statistical / feature-based / shared-task detectors ---
277	
278	@inproceedings{verma2024_ghostbuster,
279	  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
280	  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
281	  booktitle = {Proceedings of NAACL},
282	  year      = {2024},
283	  note      = {arXiv:2305.15047},
284	  url       = {https://arxiv.org/abs/2305.15047},
285	}
286	
287	@inproceedings{wang2024_m4_semeval,
288	  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
289	  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
290	  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},
291	  year      = {2024},
292	  note      = {arXiv:2404.14183},
293	  url       = {https://arxiv.org/abs/2404.14183},
294	}
295	
296	@inproceedings{yang2024_dnagpt,
297	  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
298	  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
299	  booktitle = {Proceedings of ICLR},
300	  year      = {2024},
301	  note      = {arXiv:2305.17359},
302	  url       = {https://arxiv.org/abs/2305.17359},
303	}
304	
305	% --- Watermarking ---
306	
307	@inproceedings{kirchenbauer2023_watermark,
308	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
309	  title     = {{A Watermark for Large Language Models}},
310	  booktitle = {Proceedings of ICML},
311	  year      = {2023},
312	  note      = {arXiv:2301.10226},
313	  url       = {https://arxiv.org/abs/2301.10226},
314	}
315	
316	% ============================================================
317	% Decoding Strategies
318	% ============================================================
319	
320	@inproceedings{holtzman2020_nucleus,
321	  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
322	  title     = {{The Curious Case of Neural Text Degeneration}},
323	  booktitle = {Proceedings of ICLR},
324	  year      = {2020},
325	  note      = {arXiv:1904.09751},
326	  url       = {https://arxiv.org/abs/1904.09751},
327	}
328	
329	@inproceedings{finlayson2024_closing,
330	  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},
331	  title     = {{Closing the Curious Case of Neural Text Degeneration}},
332	  booktitle = {Proceedings of ICLR},
333	  year      = {2024},
334	  note      = {arXiv:2310.01693},
335	  url       = {https://arxiv.org/abs/2310.01693},
336	}
337	
338	@inproceedings{garces_arias2025_decoding_decoded,
339	  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
340	  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
341	  booktitle = {Proceedings of COLING},
342	  year      = {2025},
343	  note      = {arXiv:2410.06097},
344	  url       = {https://arxiv.org/abs/2410.06097},
345	}
346	
347	@article{wiher2022_decoding,
348	  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},
349	  title     = {{On Decoding Strategies for Neural Text Generators}},
350	  journal   = {Transactions of the Association for Computational Linguistics},
351	  volume    = {10},
352	  pages     = {997--1012},
353	  year      = {2022},
354	}
355	
356	@inproceedings{basu2021_mirostat,
357	  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},
358	  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},
359	  booktitle = {Proceedings of ICLR},
360	  year      = {2021},
361	}
362	
363	% ============================================================
364	% Ordinal Classification / Contrastive Learning
365	% ============================================================
366	
367	@article{coral2020,
368	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
369	  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
370	  journal   = {Pattern Recognition Letters},
371	  volume    = {140},
372	  pages     = {325--331},
373	  year      = {2020},
374	  note      = {arXiv:1901.07884},
375	  url       = {https://arxiv.org/abs/1901.07884},
376	}
377	
378	@inproceedings{cloc2025,
379	  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},
380	  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},
381	  booktitle = {Proceedings of CVPR},
382	  year      = {2025},
383	  note      = {arXiv:2504.17813},
384	  url       = {https://arxiv.org/abs/2504.17813},
385	}
386	
387	% ============================================================
388	% Foundation Models / Fine-tuning
389	% ============================================================
390	
391	@inproceedings{hu2022lora,
392	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
393	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
394	  booktitle = {Proceedings of ICLR},
395	  year      = {2022},
396	  note      = {arXiv:2106.09685},
397	  url       = {https://arxiv.org/abs/2106.09685},
398	}
399	
400	@inproceedings{he2021_deberta_v3,
401	  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
402	  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},
403	  booktitle = {Proceedings of ICLR},
404	  year      = {2023},
405	  note      = {arXiv:2111.09543},
406	  url       = {https://arxiv.org/abs/2111.09543},
407	}
408	
409	@article{liu2019_roberta,
410	  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
411	  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},
412	  journal   = {arXiv preprint arXiv:1907.11692},
413	  year      = {2019},
414	  url       = {https://arxiv.org/abs/1907.11692},
415	}
416	
417	% ============================================================
418	% Data Curation / Selection
419	% ============================================================
420	
421	@inproceedings{dsir2023,
422	  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
423	  title     = {{Data Selection for Language Models via Importance Resampling}},
424	  booktitle = {Proceedings of NeurIPS},
425	  year      = {2023},
426	  note      = {arXiv:2302.03169},
427	  url       = {https://arxiv.org/abs/2302.03169},
428	}
429	
430	@inproceedings{qurating2024,
431	  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
432	  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},
433	  booktitle = {Proceedings of ICML},
434	  year      = {2024},
435	  note      = {arXiv:2402.09739},
436	  url       = {https://arxiv.org/abs/2402.09739},
437	}
438	
439	@article{sugiyama2007_importance_weighting,
440	  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
441	  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},
442	  journal   = {Journal of Machine Learning Research},
443	  volume    = {8},
444	  pages     = {985--1005},
445	  year      = {2007},
446	}
447	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "1f9afbd0-429e-4246-b531-c19335b651d4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
      "content": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2024_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n",
      "numLines": 447,
      "startLine": 1,
      "totalLines": 447
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012pUhwJZBBkXmqDBmNGdePx`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e68e0124-6472-4156-a3c6-49fa3dfbf777",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 13 · 2026-05-15T23:54:58.999Z_

<details><summary>↩ Tool result · `toolu_012pUhwJZBBkXmqDBmNGdePx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "ff45265d-1e75-4ade-8aed-db45714fb073",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01PUfB82DZmpRBvqCKMMKWNV`</summary>

```json
{
  "pattern": "**/artifacts/_project/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "f9890a0f-f2b2-41d7-bbcd-6e08a4b7d27f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P8rLyAi175ZH9oHc1vumK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12786,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12786
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

_source line 15 · 2026-05-15T23:54:59.541Z_

<details><summary>↩ Tool result · `toolu_01PUfB82DZmpRBvqCKMMKWNV`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "458f2ea0-f554-49a1-b474-5b0de0e516f8",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 14,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the files. Now let me:
1. Search for the dohmatob paper
2. Read the artifacts bib to check if it differs

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "462a2d41-b21a-48ad-80a2-49926b1c111d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LC5amTSoE7qVxcjDpTXE56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14074,
      "cache_read_input_tokens": 24627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14074
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KWfjaj4soeXSKRyCRzYkU9`</summary>

```json
{
  "query": "arXiv 2410.04840 \"Strong Model Collapse\" dohmatob ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "de0e5c5d-949d-4e93-a00d-58f4d5cb3e03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LC5amTSoE7qVxcjDpTXE56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14074,
      "cache_read_input_tokens": 24627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14074
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — Read · `toolu_012BKBtWpN22FHbaaxA9Hjw3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "40ec08eb-1443-4f0c-a2ad-40adbdf878e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LC5amTSoE7qVxcjDpTXE56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14074,
      "cache_read_input_tokens": 24627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14074
      },
      "output_tokens": 26,
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

_source line 19 · 2026-05-15T23:55:05.827Z_

<details><summary>↩ Tool result · `toolu_012BKBtWpN22FHbaaxA9Hjw3`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2024_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2024},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
51	@misc{gerstgrasser2024_accumulate,
52	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
53	  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
54	  year      = {2024},
55	  howpublished = {arXiv:2404.01413},
56	  url       = {https://arxiv.org/abs/2404.01413},
57	}
58	
59	@inproceedings{marchi2024_heat_death,
60	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
61	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
62	  booktitle = {Proceedings of ICASSP},
63	  year      = {2024},
64	  note      = {arXiv:2404.02325},
65	  url       = {https://arxiv.org/abs/2404.02325},
66	}
67	
68	@misc{knowledge_collapse2025,
69	  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},
70	  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},
71	  year      = {2025},
72	  howpublished = {arXiv:2509.04796},
73	  url       = {https://arxiv.org/abs/2509.04796},
74	}
75	
76	@misc{sigma2026_spectral,
77	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
78	  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},
79	  year      = {2026},
80	  howpublished = {arXiv:2601.03385},
81	  url       = {https://arxiv.org/abs/2601.03385},
82	}
83	
84	@inproceedings{mohamed2025_broken_telephone,
85	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
86	  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
87	  booktitle = {Proceedings of ACL},
88	  year      = {2025},
89	  note      = {arXiv:2502.20258},
90	  url       = {https://arxiv.org/abs/2502.20258},
91	}
92	
93	@inproceedings{synthetic_eggs2026,
94	  author    = {Schaffelder, Max and Gatt, Albert},
95	  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},
96	  booktitle = {Findings of ACL},
97	  year      = {2026},
98	  note      = {arXiv:2511.01490},
99	  url       = {https://arxiv.org/abs/2511.01490},
100	}
101	
102	% --- Model collapse: collapse-can-be-avoided / contamination ---
103	
104	@inproceedings{drayson2025_detection_prevents_collapse,
105	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
106	  title     = {{Machine-generated text detection prevents language model collapse}},
107	  booktitle = {Findings of EMNLP},
108	  year      = {2025},
109	  note      = {arXiv:2502.15654},
110	  url       = {https://arxiv.org/abs/2502.15654},
111	}
112	
113	@misc{bakshi2026_collapse_improvement,
114	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
115	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
116	  year      = {2026},
117	  howpublished = {arXiv:2602.10531},
118	  url       = {https://arxiv.org/abs/2602.10531},
119	}
120	
121	@misc{wang2026_contamination,
122	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
123	  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},
124	  year      = {2026},
125	  howpublished = {arXiv:2602.16065},
126	  url       = {https://arxiv.org/abs/2602.16065},
127	}
128	
129	@misc{falahati2026_curated,
130	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
131	  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},
132	  year      = {2026},
133	  howpublished = {arXiv:2605.07724},
134	  url       = {https://arxiv.org/abs/2605.07724},
135	}
136	
137	% ============================================================
138	% AI-Generated Text Detection
139	% ============================================================
140	
141	% --- Statistical / zero-shot detectors ---
142	
143	@inproceedings{gehrmann2019_gltr,
144	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
145	  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},
146	  booktitle = {Proceedings of ACL: System Demonstrations},
147	  year      = {2019},
148	  note      = {arXiv:1906.04043},
149	  url       = {https://arxiv.org/abs/1906.04043},
150	}
151	
152	@inproceedings{mitchell2023_detectgpt,
153	  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
154	  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
155	  booktitle = {Proceedings of ICML},
156	  year      = {2023},
157	  note      = {arXiv:2301.11305},
158	  url       = {https://arxiv.org/abs/2301.11305},
159	}
160	
161	@inproceedings{fast_detectgpt2024,
162	  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
163	  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
164	  booktitle = {Proceedings of ICLR},
165	  year      = {2024},
166	  note      = {arXiv:2310.05130},
167	  url       = {https://arxiv.org/abs/2310.05130},
168	}
169	
170	@inproceedings{binoculars2024,
171	  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
172	  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
173	  booktitle = {Proceedings of ICML},
174	  year      = {2024},
175	  note      = {arXiv:2401.12070},
176	  url       = {https://arxiv.org/abs/2401.12070},
177	}
178	
179	@article{diveye2026,
180	  author    = {Basani, Advik Raj and Chen, Pin-Yu},
181	  title     = {{Diversity Boosts AI-Generated Text Detection}},
182	  journal   = {Transactions on Machine Learning Research (TMLR)},
183	  year      = {2026},
184	  note      = {arXiv:2509.18880},
185	  url       = {https://arxiv.org/abs/2509.18880},
186	}
187	
188	% --- Robustness / limitations of detectors ---
189	
190	@misc{sadasivan2023_paraphrase,
191	  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
192	  title     = {{Can AI-Generated Text be Reliably Detected?}},
193	  year      = {2023},
194	  howpublished = {arXiv:2303.11156},
195	  url       = {https://arxiv.org/abs/2303.11156},
196	}
197	
198	@misc{pudasaini2026_detection_fails,
199	  author    = {Pudasaini, Shushanta and Miralles-Pech{\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},
200	  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},
201	  year      = {2026},
202	  howpublished = {arXiv:2603.23146},
203	  url       = {https://arxiv.org/abs/2603.23146},
204	}
205	
206	@misc{pu2026_generator_barrier,
207	  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
208	  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
209	  year      = {2026},
210	  howpublished = {arXiv:2604.13692},
211	  url       = {https://arxiv.org/abs/2604.13692},
212	}
213	
214	% --- Beyond binary: attribution, editing extent, benchmarks ---
215	
216	@inproceedings{uchendu2020_attribution,
217	  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
218	  title     = {{Authorship Attribution for Neural Text Generation}},
219	  booktitle = {Proceedings of EMNLP},
220	  year      = {2020},
221	}
222	
223	@inproceedings{editlens2026,
224	  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},
225	  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},
226	  booktitle = {Proceedings of ICLR},
227	  year      = {2026},
228	  note      = {arXiv:2510.03154},
229	  url       = {https://arxiv.org/abs/2510.03154},
230	}
231	
232	@inproceedings{loki2025,
233	  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},
234	  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},
235	  booktitle = {Proceedings of ICLR (Spotlight)},
236	  year      = {2025},
237	  note      = {arXiv:2410.09732},
238	  url       = {https://arxiv.org/abs/2410.09732},
239	}
240	
241	% --- Watermarking ---
242	
243	@inproceedings{kirchenbauer2023_watermark,
244	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
245	  title     = {{A Watermark for Large Language Models}},
246	  booktitle = {Proceedings of ICML},
247	  year      = {2023},
248	  note      = {arXiv:2301.10226},
249	  url       = {https://arxiv.org/abs/2301.10226},
250	}
251	
252	% ============================================================
253	% Decoding Strategies
254	% ============================================================
255	
256	@inproceedings{holtzman2020_nucleus,
257	  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
258	  title     = {{The Curious Case of Neural Text Degeneration}},
259	  booktitle = {Proceedings of ICLR},
260	  year      = {2020},
261	  note      = {arXiv:1904.09751},
262	  url       = {https://arxiv.org/abs/1904.09751},
263	}
264	
265	@inproceedings{finlayson2024_closing,
266	  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},
267	  title     = {{Closing the Curious Case of Neural Text Degeneration}},
268	  booktitle = {Proceedings of ICLR},
269	  year      = {2024},
270	  note      = {arXiv:2310.01693},
271	  url       = {https://arxiv.org/abs/2310.01693},
272	}
273	
274	@inproceedings{garces_arias2025_decoding_decoded,
275	  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
276	  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
277	  booktitle = {Proceedings of COLING},
278	  year      = {2025},
279	  note      = {arXiv:2410.06097},
280	  url       = {https://arxiv.org/abs/2410.06097},
281	}
282	
283	@article{wiher2022_decoding,
284	  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},
285	  title     = {{On Decoding Strategies for Neural Text Generators}},
286	  journal   = {Transactions of the Association for Computational Linguistics},
287	  volume    = {10},
288	  pages     = {997--1012},
289	  year      = {2022},
290	}
291	
292	@inproceedings{basu2021_mirostat,
293	  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},
294	  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},
295	  booktitle = {Proceedings of ICLR},
296	  year      = {2021},
297	}
298	
299	% ============================================================
300	% Ordinal Classification / Contrastive Learning
301	% ============================================================
302	
303	@article{coral2020,
304	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
305	  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
306	  journal   = {Pattern Recognition Letters},
307	  volume    = {140},
308	  pages     = {325--331},
309	  year      = {2020},
310	  note      = {arXiv:1901.07884},
311	  url       = {https://arxiv.org/abs/1901.07884},
312	}
313	
314	@inproceedings{cloc2025,
315	  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},
316	  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},
317	  booktitle = {Proceedings of CVPR},
318	  year      = {2025},
319	  note      = {arXiv:2504.17813},
320	  url       = {https://arxiv.org/abs/2504.17813},
321	}
322	
323	% ============================================================
324	% Data Curation / Importance Weighting
325	% ============================================================
326	
327	@inproceedings{dsir2023,
328	  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
329	  title     = {{Data Selection for Language Models via Importance Resampling}},
330	  booktitle = {Proceedings of NeurIPS},
331	  year      = {2023},
332	  note      = {arXiv:2302.03169},
333	  url       = {https://arxiv.org/abs/2302.03169},
334	}
335	
336	@inproceedings{qurating2024,
337	  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
338	  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},
339	  booktitle = {Proceedings of ICML},
340	  year      = {2024},
341	  note      = {arXiv:2402.09739},
342	  url       = {https://arxiv.org/abs/2402.09739},
343	}
344	
345	@article{sugiyama2007_importance_weighting,
346	  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
347	  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},
348	  journal   = {Journal of Machine Learning Research},
349	  volume    = {8},
350	  pages     = {985--1005},
351	  year      = {2007},
352	}
353	
354	% ============================================================
355	% Foundation Models / Fine-tuning
356	% ============================================================
357	
358	@inproceedings{hu2022lora,
359	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
360	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
361	  booktitle = {Proceedings of ICLR},
362	  year      = {2022},
363	  note      = {arXiv:2106.09685},
364	  url       = {https://arxiv.org/abs/2106.09685},
365	}
366	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "f5ec5d9f-4c14-4b3c-8d19-4d252e4c43e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
      "content": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2024_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Data Curation / Importance Weighting\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n",
      "numLines": 366,
      "startLine": 1,
      "totalLines": 366
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01LkcXoVGu3Vry4BVXfJM5no`</summary>

```json
{
  "pattern": "dohmatob2024_strong_collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "be30ab67-7df9-4313-b122-108e8bc5c7df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LC5amTSoE7qVxcjDpTXE56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14074,
      "cache_read_input_tokens": 24627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14074
      },
      "output_tokens": 26,
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

_source line 21 · 2026-05-15T23:55:09.554Z_

<details><summary>↩ Tool result · `toolu_01LkcXoVGu3Vry4BVXfJM5no`</summary>

```text
docs/paper/related_work.tex:6:\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \emph{narrowing} from \emph{cutting}; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "9958b595-eff6-4ac0-bc35-e0b6c33c33b3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:6:\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.",
    "numLines": 1
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T23:55:11.248Z_

<details><summary>↩ Tool result · `toolu_01KWfjaj4soeXSKRyCRzYkU9`</summary>

```text
Web search results for query: "arXiv 2410.04840 "Strong Model Collapse" dohmatob ICLR 2025"

Links: [{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Strong Model Collapse | Request PDF","url":"https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"}]

Based on the search results, here's information about the paper:

## "Strong Model Collapse" (arXiv:2410.04840)

**Authors:** Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe

**Conference:** Published at ICLR 2025 as a Spotlight paper

**Main Contribution:** The paper establishes a strong form of the model collapse phenomenon within the scaling laws paradigm, studying a supervised regression setting where there is a critical performance degradation due to synthetic data in the training corpus.

**Key Finding:** Even the smallest fraction of synthetic data (as little as 1 per 1000) can still lead to model collapse: larger and larger training sets do not enhance performance.

**Technical Approach:** The authors employ operator-valued free probability theory (OVFPT) to obtain a new bias-variance decomposition of the test error evaluated on the real/true data distribution for models trained on a mixture of real and synthetic data.

**Impact on Model Size:** In a simplified regime where neural networks are approximated via random projections of tunable size, the authors both theoretically and empirically show that larger models can amplify model collapse.

The paper addresses a critical concern for large-scale AI systems and was published on arXiv on October 8, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "bee0e136-474d-4c45-8159-2cd93868a604",
  "tool_use_result": {
    "query": "arXiv 2410.04840 \"Strong Model Collapse\" dohmatob ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012zptRjLTz5idwo8gYPmGzG",
        "content": [
          {
            "title": "[2410.04840] Strong Model Collapse",
            "url": "https://arxiv.org/abs/2410.04840"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"
          },
          {
            "title": "Strong Model Collapse",
            "url": "https://arxiv.org/html/2410.04840"
          },
          {
            "title": "Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗",
            "url": "https://arxiv.org/pdf/2410.04840"
          },
          {
            "title": "Strong Model Collapse | OpenReview",
            "url": "https://openreview.net/forum?id=et5l9qPUhm"
          },
          {
            "title": "Strong Model Collapse - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"
          },
          {
            "title": "Strong Model Collapse | Request PDF",
            "url": "https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"
          },
          {
            "title": "Position: Model Collapse Does Not Mean What You Think",
            "url": "https://arxiv.org/pdf/2503.03150"
          },
          {
            "title": "ICLR Poster Strong Model Collapse",
            "url": "https://iclr.cc/virtual/2025/poster/32070"
          },
          {
            "title": "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective",
            "url": "https://arxiv.org/html/2509.16499v2"
          }
        ]
      },
      "Based on the search results, here's information about the paper:\n\n## \"Strong Model Collapse\" (arXiv:2410.04840)\n\n**Authors:** Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe\n\n**Conference:** Published at ICLR 2025 as a Spotlight paper\n\n**Main Contribution:** The paper establishes a strong form of the model collapse phenomenon within the scaling laws paradigm, studying a supervised regression setting where there is a critical performance degradation due to synthetic data in the training corpus.\n\n**Key Finding:** Even the smallest fraction of synthetic data (as little as 1 per 1000) can still lead to model collapse: larger and larger training sets do not enhance performance.\n\n**Technical Approach:** The authors employ operator-valued free probability theory (OVFPT) to obtain a new bias-variance decomposition of the test error evaluated on the real/true data distribution for models trained on a mixture of real and synthetic data.\n\n**Impact on Model Size:** In a simplified regime where neural networks are approximated via random projections of tunable size, the authors both theoretically and empirically show that larger models can amplify model collapse.\n\nThe paper addresses a critical concern for large-scale AI systems and was published on arXiv on October 8, 2024."
    ],
    "durationSeconds": 6.821731767000001
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need:

1. **dohmatob paper**: Confirmed published at ICLR 2025 (not 2024). Need to change year from 2024 to 2025 and update bib key from `dohmatob2024_strong_collapse` to `dohmatob2025_strong_collapse`. The cite appears in `related_work.tex` line 6 and `references.bib` line 24-31.

2. **artifacts bib**: Exists and has the same wrong entry. It's different from docs/paper version (artifacts version is missing some entries like `wu2025_detection_survey`, `wang2024_m4_semeval`, `yang2024_dnagpt`, `verma2024_ghostbuster`, `bevendorff2025_two_paradigms`, `he2021_deberta_v3`, `liu2019_roberta`, `shi2025_closer_look`, `yi2026_escaping_collapse`). 

I need to copy the docs/paper version over to artifacts to sync them up. Then I'll tackle the edits: rewriting the "Depth-graduated data curation" paragraph in discussion.tex to include PoC statistics, adding a new subsection in section_appendix.tex, and fixing the dohmatob citation year and key across both bib files. I'm continuing the discussion of depth-graduated curation, explaining how the empirical results support feasibility while acknowledging the cross-strategy transfer challenge that requires either known metadata or an upstream identification step. I'm also considering importance weighting as a way to enable continuous depth-aware selection instead of discrete filtering, and noting verification-guided retraining as a complementary approach.

Now I'm setting up the proof-of-concept experiment where we train a model with LoRA on depth-selected subsets to validate whether this curation strategy actually improves downstream training quality.

The results show that filtering by predicted depth substantially beats random subsampling—we get meaningful perplexity gains with strict filtering and the soft-threshold approach matches full-data performance while cutting the dataset to 44%, though interestingly the oracle labels don't help, which suggests the classifier's imprecision actually preserves useful diversity that hard thresholding would discard. There's potential to extend this with importance weighting for continuous selection rather than binary filtering, and verification-guided retraining could offer another angle for improvement.

Now I'm setting up the appendix section to document the full experimental details and statistics from this curation proof of concept. Generating the results table... Generating markdown table...

I need to fix the table label in the discussion—I referenced `tab:curation_poc` but actually labeled it `tab:curation_conditions`. Let me just rename the conditions table to `tab:curation_poc` since that's what the discussion is citing anyway.

Now I'm making four edits: updating the discussion text, adding a new subsection to the appendix, fixing the bibliography entry, and updating the citation key in related work. I'll handle these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "5df87317-0c20-4f5e-a377-71a0560fb002",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRi2WUCPCsv765vTxZwD9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6443,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 38701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

确认：dohmatob2024_strong_collapse 确实发表在 ICLR 2025，需改 year 和 key。artifacts bib 存在且与 docs 版本不同。

现在并行执行所有编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "61cfa30d-fc69-40be-95dd-e7c15f3239d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRi2WUCPCsv765vTxZwD9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6443,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 38701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Q4ouyoWYsS3gm1aaXjsRk1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Depth-graduated data curation.}\nCurrent data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.\nDepth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.\nImportance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.\nThe downstream effect on training quality remains to be validated empirically.",
  "new_string": "\\paragraph{Depth-graduated data curation.}\nCurrent data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.\nDepth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nAs a proof of concept, we fine-tune Pythia-410M with LoRA ($r{=}16$) for 3 epochs on subsets selected by RF-predicted depth, random subsampling, or oracle depth labels (8 conditions, 5 seeds each; Table~\\ref{tab:curation_poc}).\nRF depth-based filtering significantly outperforms size-matched random subsampling (strict 25\\%: $\\Delta{=}0.43$ PPL, paired $t$-test $p{=}0.002$; moderate 50\\%: $\\Delta{=}0.24$, $p{=}0.02$), and the soft-threshold RF condition achieves perplexity statistically indistinguishable from unfiltered training on the full 10{,}000 samples while using only 44\\% of the data ($p{=}0.41$).\nInterestingly, oracle-strict filtering does not improve over unfiltered ($p{=}0.22$), suggesting that classifier imprecision preserves beneficial data diversity that pure depth thresholding removes.\nImportance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.\nFull per-condition statistics appear in Appendix~\\ref{app:curation_poc}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e81e0c36-9204-4b06-9ace-ded81eefccc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRi2WUCPCsv765vTxZwD9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6443,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 38701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 26 · 2026-05-15T23:56:18.443Z_

<details><summary>↩ Tool result · `toolu_01Q4ouyoWYsS3gm1aaXjsRk1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "9badd08f-fe55-4cb2-bab8-37f1208fd1d8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Depth-graduated data curation.}\nCurrent data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.\nDepth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.\nImportance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.\nThe downstream effect on training quality remains to be validated empirically.",
    "newString": "\\paragraph{Depth-graduated data curation.}\nCurrent data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.\nDepth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nAs a proof of concept, we fine-tune Pythia-410M with LoRA ($r{=}16$) for 3 epochs on subsets selected by RF-predicted depth, random subsampling, or oracle depth labels (8 conditions, 5 seeds each; Table~\\ref{tab:curation_poc}).\nRF depth-based filtering significantly outperforms size-matched random subsampling (strict 25\\%: $\\Delta{=}0.43$ PPL, paired $t$-test $p{=}0.002$; moderate 50\\%: $\\Delta{=}0.24$, $p{=}0.02$), and the soft-threshold RF condition achieves perplexity statistically indistinguishable from unfiltered training on the full 10{,}000 samples while using only 44\\% of the data ($p{=}0.41$).\nInterestingly, oracle-strict filtering does not improve over unfiltered ($p{=}0.22$), suggesting that classifier imprecision preserves beneficial data diversity that pure depth thresholding removes.\nImportance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.\nFull per-condition statistics appear in Appendix~\\ref{app:curation_poc}.",
    "originalFile": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nWe formalized recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70--85\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.\nThe dominant pair (\\texttt{p90\\_ppl} top-2 in 9/9 cells, \\texttt{var\\_surprisal} in 8/9 under SHAP) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\\cite{shumailov2024_nature}.\nRecent work corroborates this connection, identifying entropy decline as a measurable signal of recursive degradation that parallels the tail erosion our features capture~\\cite{shi2025_closer_look}.\n\nCross-strategy transfer remains the primary bottleneck (59.1\\% vs.\\ 66.4\\% cross-model), with the temperature-induced d1/d2 AUC inversion making single-classifier deployment across unknown decoding strategies infeasible.\nA two-stage pipeline---first identifying the decoding strategy, then applying a strategy-conditioned depth classifier---could address this, though automating strategy identification from text alone requires independent validation.\n\n\\paragraph{Depth-graduated data curation.}\nCurrent data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.\nDepth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.\nImportance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.\nThe downstream effect on training quality remains to be validated empirically.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking~\\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution~\\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nBevendorff et al.\\ distinguish attribution from verification as two fundamental detection paradigms~\\cite{bevendorff2025_two_paradigms}; depth estimation represents a complementary third axis that characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining watermark presence, source model, and recursive depth could support more nuanced data auditing than any single method.\n\n\\paragraph{Limitations and future directions.}\nReal-world documents may interleave passages at mixed recursive depths within a single document; our passage-level classifier assumes uniform depth, and extending to segment-level estimation introduces a granularity--statistical-power tradeoff that remains unexplored.\nWeb-crawl deployment requires model-specific calibration (C4 FPR: 4.7--22.4\\%; Table~\\ref{tab:calibration}), and all experiments use 1--1.5B models.\nFuture work should validate on mixed-domain corpora at larger scales and evaluate whether depth-graduated curation, with appropriate strategy conditioning, improves downstream training outcomes.\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 9,
        "newStart": 11,
        "newLines": 11,
        "lines": [
          " \\paragraph{Depth-graduated data curation.}",
          " Current data curation operates on a binary human-vs-machine distinction~\\cite{dsir2023,qurating2024}.",
          " Depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.",
          "-The 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.",
          "+As a proof of concept, we fine-tune Pythia-410M with LoRA ($r{=}16$) for 3 epochs on subsets selected by RF-predicted depth, random subsampling, or oracle depth labels (8 conditions, 5 seeds each; Table~\\ref{tab:curation_poc}).",
          "+RF depth-based filtering significantly outperforms size-matched random subsampling (strict 25\\%: $\\Delta{=}0.43$ PPL, paired $t$-test $p{=}0.002$; moderate 50\\%: $\\Delta{=}0.24$, $p{=}0.02$), and the soft-threshold RF condition achieves perplexity statistically indistinguishable from unfiltered training on the full 10{,}000 samples while using only 44\\% of the data ($p{=}0.41$).",
          "+Interestingly, oracle-strict filtering does not improve over unfiltered ($p{=}0.22$), suggesting that classifier imprecision preserves beneficial data diversity that pure depth thresholding removes.",
          " Importance weighting~\\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\\cite{yi2026_escaping_collapse}.",
          "-The downstream effect on training quality remains to be validated empirically.",
          "+Full per-condition statistics appear in Appendix~\\ref{app:curation_poc}.",
          " ",
          " \\paragraph{Toward a provenance toolkit.}",
          " Depth estimation complements existing provenance methods along orthogonal axes."
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

<details open><summary>🔧 Tool call — Edit · `toolu_01GPQzjuN1RozVHPuVGd2KtA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "old_string": "\\subsection{Extended Discussion}\n\\label{app:extended_discussion}",
  "new_string": "\\subsection{Downstream Curation PoC}\n\\label{app:curation_poc}\n\nTo validate that depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.\nWe fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.\nConditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\\approx$25\\%, moderate $\\approx$50\\%, soft threshold).\nTable~\\ref{tab:curation_poc} reports per-condition perplexity; Table~\\ref{tab:curation_comparisons} reports pairwise contrasts.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\\,: $p<0.05$ (paired $t$-test vs.\\ unfiltered).}\n\\label{tab:curation_poc}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nCondition & Mean PPL & Std & $n$ & $\\Delta$ vs Unfilt. & $p$ & Cohen's $d$ \\\\\n\\midrule\nunfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\\\\nrf\\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.792   \\\\\nrf\\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.334   \\\\\nrf\\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.528 \\\\\noracle\\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.384 \\\\\noracle\\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$1.004 \\\\\nrandom\\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.029$^*$ & $-$2.809 \\\\\nrandom\\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$3.671 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\\,: $p<0.05$; $^{**}$\\,: $p<0.01$.}\n\\label{tab:curation_comparisons}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nComparison & $\\Delta$ PPL & $t$ & $p$ \\\\\n\\midrule\nrf\\_strict vs random\\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\\\\nrf\\_moderate vs random\\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\\\\nrf\\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "0133ed78-f085-4713-a42d-f8250d0d1af3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRi2WUCPCsv765vTxZwD9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6443,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 38701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 28 · 2026-05-15T23:56:27.969Z_

<details><summary>↩ Tool result · `toolu_01GPQzjuN1RozVHPuVGd2KtA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "767fd720-bff4-4f85-b7b7-42556e813dd1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "oldString": "\\subsection{Extended Discussion}\n\\label{app:extended_discussion}",
    "newString": "\\subsection{Downstream Curation PoC}\n\\label{app:curation_poc}\n\nTo validate that depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.\nWe fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.\nConditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\\approx$25\\%, moderate $\\approx$50\\%, soft threshold).\nTable~\\ref{tab:curation_poc} reports per-condition perplexity; Table~\\ref{tab:curation_comparisons} reports pairwise contrasts.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\\,: $p<0.05$ (paired $t$-test vs.\\ unfiltered).}\n\\label{tab:curation_poc}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nCondition & Mean PPL & Std & $n$ & $\\Delta$ vs Unfilt. & $p$ & Cohen's $d$ \\\\\n\\midrule\nunfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\\\\nrf\\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.792   \\\\\nrf\\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.334   \\\\\nrf\\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.528 \\\\\noracle\\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.384 \\\\\noracle\\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$1.004 \\\\\nrandom\\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.029$^*$ & $-$2.809 \\\\\nrandom\\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$3.671 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\\,: $p<0.05$; $^{**}$\\,: $p<0.01$.}\n\\label{tab:curation_comparisons}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nComparison & $\\Delta$ PPL & $t$ & $p$ \\\\\n\\midrule\nrf\\_strict vs random\\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\\\\nrf\\_moderate vs random\\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\\\\nrf\\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}",
    "originalFile": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\textsc{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\textsc{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\textsc{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\textsc{p75\\_ppl} displaces \\textsc{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.83$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.\n\n\\subsection{Per-Class Recall}\n\\label{app:per_class}\n\nTable~\\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).\nDepth~0 recall exceeds 98\\% uniformly.\nAmong generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-class recall (\\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}\n\\label{tab:per_class_recall}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCell & d0 & d1 & d2 & d3 \\\\\n\\midrule\nPythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\\\\nPythia, $\\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\\\\nPythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\\\\nOLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\\\\nOLMo, $\\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\\\\nOLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\\\\nGPT-2~XL, nuc.     & 99.2 & 85.9 & \\textbf{73.3} & 77.5 \\\\\nGPT-2~XL, $\\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\\\\nGPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing, indicating these features are not linearly accessible in the pretrained representation space.\nThis confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level), confirming that depth signal is the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}llrcc@{}}\n\\toprule\nModel & Source & $n$ & d0 (\\%) & FPR (\\%) \\\\\n\\midrule\nPythia-1.4B & WikiText & 546 & 100.0 & 0.0 \\\\\n & C4 & 5{,}000 & 79.8 & 20.2 \\\\\n\\addlinespace\nGPT-2~XL & WikiText & 546 & 99.3 & 0.7 \\\\\n & C4 & 5{,}000 & 77.6 & 22.4 \\\\\n\\addlinespace\nOLMo-1B & WikiText & 546 & 98.5 & 1.5 \\\\\n & C4 & 5{,}000 & 95.3 & 4.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn WikiText-103, all three classifiers achieve $\\geq$98.5\\% d0 accuracy, confirming that editorial text is reliably distinguished from recursive generations across model families.\nOn C4, FPR varies sharply: OLMo (4.7\\%) vs.\\ Pythia (20.2\\%) and GPT-2~XL (22.4\\%).\nC4 misclassifications concentrate in template and SEO content with elevated repetition features (\\texttt{rep\\_3gram} $+$37\\%, \\texttt{rep\\_4gram} $+$75\\% vs.\\ correctly classified d0 passages), rather than in random noise.\nThe model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.\nAmong C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\\%), d2 (3.7\\%), d3 (9.6\\%); for OLMo, d1 (2.9\\%), d2 (0.5\\%), d3 (1.3\\%)---the non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; the downstream effect on training quality remains to be validated empirically.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals---watermark presence, source model, and recursive generation depth---could support more nuanced data auditing than any single method.\n",
    "structuredPatch": [
      {
        "oldStart": 136,
        "oldLines": 6,
        "newStart": 136,
        "newLines": 51,
        "lines": [
          " The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.",
          " Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\\%), d2 (3.7\\%), d3 (9.6\\%); for OLMo, d1 (2.9\\%), d2 (0.5\\%), d3 (1.3\\%)---the non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.",
          " ",
          "+\\subsection{Downstream Curation PoC}",
          "+\\label{app:curation_poc}",
          "+",
          "+To validate that depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.",
          "+We fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.",
          "+Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\\approx$25\\%, moderate $\\approx$50\\%, soft threshold).",
          "+Table~\\ref{tab:curation_poc} reports per-condition perplexity; Table~\\ref{tab:curation_comparisons} reports pairwise contrasts.",
          "+",
          "+\\begin{table}[h]",
          "+\\centering",
          "+\\small",
          "+\\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\\,: $p<0.05$ (paired $t$-test vs.\\ unfiltered).}",
          "+\\label{tab:curation_poc}",
          "+\\begin{tabular}{@{}lcccccc@{}}",
          "+\\toprule",
          "+Condition & Mean PPL & Std & $n$ & $\\Delta$ vs Unfilt. & $p$ & Cohen's $d$ \\\\",
          "+\\midrule",
          "+unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\\\",
          "+rf\\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.792   \\\\",
          "+rf\\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.334   \\\\",
          "+rf\\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.528 \\\\",
          "+oracle\\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.384 \\\\",
          "+oracle\\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$1.004 \\\\",
          "+random\\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.029$^*$ & $-$2.809 \\\\",
          "+random\\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$3.671 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+\\begin{table}[h]",
          "+\\centering",
          "+\\small",
          "+\\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\\,: $p<0.05$; $^{**}$\\,: $p<0.01$.}",
          "+\\label{tab:curation_comparisons}",
          "+\\begin{tabular}{@{}lccc@{}}",
          "+\\toprule",
          "+Comparison & $\\Delta$ PPL & $t$ & $p$ \\\\",
          "+\\midrule",
          "+rf\\_strict vs random\\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\\\",
          "+rf\\_moderate vs random\\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\\\",
          "+rf\\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          " \\subsection{Extended Discussion}",
          " \\label{app:extended_discussion}",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Y6zbtxS57Pc9ZpEjUUh3aa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "@inproceedings{dohmatob2024_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}",
  "new_string": "@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "dd4c53ee-60cd-4a5c-8689-1ede670f3861",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRi2WUCPCsv765vTxZwD9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6443,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 38701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 30 · 2026-05-15T23:56:31.233Z_

<details><summary>↩ Tool result · `toolu_01Y6zbtxS57Pc9ZpEjUUh3aa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "c029d4c1-f32d-43b9-b9ab-0b7e254c5138",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "oldString": "@inproceedings{dohmatob2024_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}",
    "newString": "@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}",
    "originalFile": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2024_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 21,
        "oldLines": 11,
        "newStart": 21,
        "newLines": 11,
        "lines": [
          "   url       = {https://arxiv.org/abs/2402.07043},",
          " }",
          " ",
          "-@inproceedings{dohmatob2024_strong_collapse,",
          "+@inproceedings{dohmatob2025_strong_collapse,",
          "   author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},",
          "   title     = {{Strong Model Collapse}},",
          "   booktitle = {Proceedings of ICLR},",
          "-  year      = {2024},",
          "+  year      = {2025},",
          "   note      = {arXiv:2410.04840},",
          "   url       = {https://arxiv.org/abs/2410.04840},",
          " }"
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01STZ4NrhHxnRDeJCRWxTd9S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "old_string": "dohmatob2024_strong_collapse",
  "new_string": "dohmatob2025_strong_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "2151226c-2fa6-49b8-9492-e4b88e4ebcb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRi2WUCPCsv765vTxZwD9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6443,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 38701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 32 · 2026-05-15T23:56:32.097Z_

<details><summary>↩ Tool result · reported error · `toolu_01STZ4NrhHxnRDeJCRWxTd9S`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "c378d30a-9e79-41f3-af23-085ac6179d64",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01CxJyznKa76t2VAFn3Va6dU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "c5755cfd-82c2-41ea-98fb-4070ea6aba33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jp9Hof6wrNR7MrLL849ATA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12194,
      "cache_read_input_tokens": 39842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12194
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

_source line 34 · 2026-05-15T23:56:35.353Z_

<details><summary>↩ Tool result · `toolu_01CxJyznKa76t2VAFn3Va6dU`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.
6	\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \emph{narrowing} from \emph{cutting}; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
7	The MAD framework \cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.
8	Mitigation strategies include retaining real data \cite{gerstgrasser2024_accumulate} and filtering via detection \cite{drayson2025_detection_prevents_collapse}.
9	Recent work identifies non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, fixed-point convergence \cite{marchi2024_heat_death}, contamination bounds \cite{wang2026_contamination}, curated pipelines \cite{falahati2026_curated}, knowledge collapse \cite{knowledge_collapse2025}, spectral signatures \cite{sigma2026_spectral}, and self-improving loops \cite{synthetic_eggs2026}.
10	These works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e1eb9d4b-d335-4c19-9352-b2fa8054fab0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.\n\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.\nThe MAD framework \\cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.\nMitigation strategies include retaining real data \\cite{gerstgrasser2024_accumulate} and filtering via detection \\cite{drayson2025_detection_prevents_collapse}.\nRecent work identifies non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, fixed-point convergence \\cite{marchi2024_heat_death}, contamination bounds \\cite{wang2026_contamination}, curated pipelines \\cite{falahati2026_curated}, knowledge collapse \\cite{knowledge_collapse2025}, spectral signatures \\cite{sigma2026_spectral}, and self-improving loops \\cite{synthetic_eggs2026}.\nThese works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_012A6xtEPYvLNu3pCJGpJbsg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "old_string": "dohmatob2024_strong_collapse",
  "new_string": "dohmatob2025_strong_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "37178435-a46f-44fb-913f-cb192f5a2bbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167efv6L4YiLQyv9QYM2Vem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 52036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
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

_source line 36 · 2026-05-15T23:56:38.192Z_

<details><summary>↩ Tool result · `toolu_012A6xtEPYvLNu3pCJGpJbsg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "01b7de4b-f886-4dbe-8c68-63581a8c9bd1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
    "oldString": "dohmatob2024_strong_collapse",
    "newString": "dohmatob2025_strong_collapse",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.\n\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.\nThe MAD framework \\cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.\nMitigation strategies include retaining real data \\cite{gerstgrasser2024_accumulate} and filtering via detection \\cite{drayson2025_detection_prevents_collapse}.\nRecent work identifies non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, fixed-point convergence \\cite{marchi2024_heat_death}, contamination bounds \\cite{wang2026_contamination}, curated pipelines \\cite{falahati2026_curated}, knowledge collapse \\cite{knowledge_collapse2025}, spectral signatures \\cite{sigma2026_spectral}, and self-improving loops \\cite{synthetic_eggs2026}.\nThese works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nThe detection literature, recently surveyed by \\citet{wu2025_detection_survey}, spans statistical, model-based, and watermarking paradigms.\nDetectGPT \\cite{mitchell2023_detectgpt} introduced probability curvature as a zero-shot detection signal; Fast-DetectGPT \\cite{fast_detectgpt2024} improves efficiency via surrogate-model conditional curvature.\nBinoculars \\cite{binoculars2024} exploits perplexity ratios between related models, DivEye \\cite{diveye2026} leverages surprisal diversity, and GLTR \\cite{gehrmann2019_gltr} visualizes per-token likelihood ranks.\nFundamental limits exist: paraphrasing reduces detection to near chance \\cite{sadasivan2023_paraphrase}, detection degrades under distribution shift \\cite{pudasaini2026_detection_fails}, and a generator barrier bounds performance when the generator is unknown \\cite{pu2026_generator_barrier}.\nGhostbuster \\cite{verma2024_ghostbuster} trains classifiers on statistical features for binary detection, sharing our feature-engineering philosophy but not addressing depth; M4-SemEval \\cite{wang2024_m4_semeval} benchmarks multilingual detection, and DNA-GPT \\cite{yang2024_dnagpt} uses divergent $n$-gram analysis.\nWatermarking \\cite{kirchenbauer2023_watermark} embeds detectable signals but requires proactive deployment.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains.\n\\citet{uchendu2020_attribution} classify \\emph{which} model generated text rather than generation depth.\nLOKI \\cite{loki2025} benchmarks synthetic data detection across modalities but evaluates binary detection only.\n\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, measuring forward degradation; our task performs the inverse, classifying depth from text alone.\n\n\\paragraph{Ordinal Classification.}\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\nWe adopt both as baselines (\\S\\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals: nucleus sampling maintains diversity \\cite{holtzman2020_nucleus}, decoding parameters affect evaluation non-trivially \\cite{finlayson2024_closing}, and strategy effects are model-dependent \\cite{garces_arias2025_decoding_decoded}.\n\\citet{wiher2022_decoding} systematically compare methods on surface-level properties, and Mirostat \\cite{basu2021_mirostat} regulates output entropy via perplexity control.\nOur Depth Degradation Atlas (\\S\\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation---temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal---effects beyond single-pass text quality.",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Model Collapse Theory.}",
          " \\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.",
          "-\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.",
          "+\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.",
          " The MAD framework \\cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.",
          " Mitigation strategies include retaining real data \\cite{gerstgrasser2024_accumulate} and filtering via detection \\cite{drayson2025_detection_prevents_collapse}.",
          " Recent work identifies non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, fixed-point convergence \\cite{marchi2024_heat_death}, contamination bounds \\cite{wang2026_contamination}, curated pipelines \\cite{falahati2026_curated}, knowledge collapse \\cite{knowledge_collapse2025}, spectral signatures \\cite{sigma2026_spectral}, and self-improving loops \\cite{synthetic_eggs2026}."
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

_source line 37_

现在同步 artifacts bib（用 docs/paper 版本覆盖）并检查是否还有其他 tex 文件引用旧 key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "a4a7e46b-90e7-4e5b-a773-4fc38a31218d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqGhNqRe3rSUWRyyxjj1Na",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 52530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_014Vew4E8eKNrEdSWntPdS7C`</summary>

```json
{
  "pattern": "dohmatob2024_strong_collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "fd6fb400-3a7c-4b04-8d95-46b6b79a663c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqGhNqRe3rSUWRyyxjj1Na",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 52530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 39 · 2026-05-15T23:56:42.376Z_

<details><summary>↩ Tool result · `toolu_014Vew4E8eKNrEdSWntPdS7C`</summary>

```text
&lt;persisted-output>
Output too large (28.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/cf247e1a-27ec-416b-9e6c-ce6c421c5394/tool-results/toolu_014Vew4E8eKNrEdSWntPdS7C.txt

Preview (first 2KB):
artifacts/review_reports/round_1.md:78:**W9** [warning, 共识] 4 个 orphan bib entries (cloc2025, dohmatob2024_demystified, dohmatob2024_strong_collapse, mohamed2025_broken_telephone)——应整合到正文或清理。
artifacts/_project/paper/citations_audit.md:15:| Model Collapse Theory | Dohmatob 2024 | `dohmatob2024_tale_of_tails` + `dohmatob2024_strong_collapse` + `dohmatob2024_demystified` |
artifacts/_project/paper/citations_audit.md:38:| `dohmatob2024_strong_collapse` | Confirmed | ICLR 2024, arXiv:2410.04840 |
artifacts/_project/paper/citations_audit.md:127:- 4 entries in bib but not cited in any .tex file: `dohmatob2024_strong_collapse`, `dohmatob2024_demystified`, `mohamed2025_broken_telephone`, `cloc2025` (available for future use in method/discussion sections)
artifacts/_project/paper/references.bib:24:@inproceedings{dohmatob2024_strong_collapse,
literature_map.yaml:55:dohmatob2024_strong_collapse:
literature_map.yaml:673:#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,
logs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl:2:[Omitted long matching line]
logs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl:12:[Omitted long matching line]
logs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl:34:[Omitted long matching line]
logs/chats/worker_paper_comprehensive-revision-r3_20260515T231048.jsonl:8:[Omitted long matching line]
logs/chats/worker_paper_comprehensive-revision-r3_20260515T231048.jsonl:22:[Omitted long matching line]
logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:55:[Omitted long matching line]
logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:87:[Omitted long matching line]
logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:88:[Omitted long matching line]
logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:95:[Omitted long matching line]
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "9e76fa5b-750a-4499-becf-55688b1e3848",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/review_reports/round_1.md:78:**W9** [warning, 共识] 4 个 orphan bib entries (cloc2025, dohmatob2024_demystified, dohmatob2024_strong_collapse, mohamed2025_broken_telephone)——应整合到正文或清理。\nartifacts/_project/paper/citations_audit.md:15:| Model Collapse Theory | Dohmatob 2024 | `dohmatob2024_tale_of_tails` + `dohmatob2024_strong_collapse` + `dohmatob2024_demystified` |\nartifacts/_project/paper/citations_audit.md:38:| `dohmatob2024_strong_collapse` | Confirmed | ICLR 2024, arXiv:2410.04840 |\nartifacts/_project/paper/citations_audit.md:127:- 4 entries in bib but not cited in any .tex file: `dohmatob2024_strong_collapse`, `dohmatob2024_demystified`, `mohamed2025_broken_telephone`, `cloc2025` (available for future use in method/discussion sections)\nartifacts/_project/paper/references.bib:24:@inproceedings{dohmatob2024_strong_collapse,\nliterature_map.yaml:55:dohmatob2024_strong_collapse:\nliterature_map.yaml:673:#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,\nlogs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl:2:[Omitted long matching line]\nlogs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl:12:[Omitted long matching line]\nlogs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl:34:[Omitted long matching line]\nlogs/chats/worker_paper_comprehensive-revision-r3_20260515T231048.jsonl:8:[Omitted long matching line]\nlogs/chats/worker_paper_comprehensive-revision-r3_20260515T231048.jsonl:22:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:55:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:87:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:88:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:95:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:104:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:106:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:143:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:163:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director.jsonl:1441:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director.jsonl:1444:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director.jsonl:1446:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_1.jsonl:29:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_1.jsonl:47:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_1.jsonl:48:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_1.jsonl:75:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_1.jsonl:89:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_1.jsonl:95:[Omitted long matching line]\nlogs/chats/worker_paper_research_bib_sync_20260515T080446.jsonl:8:[Omitted long matching line]\nlogs/chats/worker_paper_research_bib_fix_20260515T090356.jsonl:2:[Omitted long matching line]\nlogs/chats/worker_paper_research_bib_fix_20260515T090356.jsonl:5:[Omitted long matching line]\nlogs/chats/worker_paper_research_bib_fix_20260515T090356.jsonl:85:[Omitted long matching line]\nlogs/chats/worker_paper_research_bib_fix_20260515T090356.jsonl:103:[Omitted long matching line]\nlogs/workers/worker_writing_discussion-and-s54-expansion_20260515T200231.log:20:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:299:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:372:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:381:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:504:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:580:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:691:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:795:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1038:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1056:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1059:{\"ts\": \"2026-05-15T10:49:54.502369+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_5434474971bcc3bc52c4774796ba7f3d:paper_agent\", \"text\": \"called Grep\", \"tool\": \"Grep\", \"tool_args\": {\"pattern\": \"cloc2025|dohmatob2024_demystified|dohmatob2024_strong_collapse|mohamed2025_broken_telephone\", \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib\", \"output_mode\": \"content\", \"-n\": \"True\"}}\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1060:{\"ts\": \"2026-05-15T10:49:54.603475+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_5434474971bcc3bc52c4774796ba7f3d:paper_agent\", \"text\": \"27:@inproceedings{dohmatob2024_strong_collapse,\\n36:@inproceedings{dohmatob2024_demystified,\\n112:@inproceedings{mohamed2025_broken_telephone,\\n271:@inproceedings{cloc2025,\", \"tool\": \"Grep\", \"elapsed_ms\": 101}\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1062:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1069:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1077:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1082:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1085:{\"ts\": \"2026-05-15T10:51:07.652355+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_5434474971bcc3bc52c4774796ba7f3d:paper_agent\", \"text\": \"called Grep\", \"tool\": \"Grep\", \"tool_args\": {\"pattern\": \"cloc2025|dohmatob2024_demystified|dohmatob2024_strong_collapse|mohamed2025_broken_telephone\", \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib\", \"output_mode\": \"count\"}}\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1097:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1136:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1138:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1152:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1157:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1173:{\"ts\": \"2026-05-15T11:10:26.208398+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_5434474971bcc3bc52c4774796ba7f3d:paper_agent\", \"text\": \"27:Most recently, \\\\citet{mohamed2025_broken_telephone} quantify how information distorts across iterative generation---a forward characterization of degradation---while \\\\citet{dohmatob2024_strong_collapse} and \\\\citet{dohmatob2024_demystified} formalize strong collapse and its regression-case dynamics.\", \"tool\": \"Grep\", \"elapsed_ms\": 50}\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1174:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1190:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1200:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1289:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1301:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1480:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1632:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:1684:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_paper_agent.jsonl:2290:[Omitted long matching line]\nlogs/chats/worker_paper_writing_introduction_20260515T093227.jsonl:12:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:47:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:616:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:618:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:626:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:634:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:657:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:659:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer.jsonl:698:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:6:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:17:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:21:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:23:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:25:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:27:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:29:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:31:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_sync_20260515T080446.log:33:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_20260515T120812_016282.jsonl:408:[Omitted long matching line]\nlogs/workers/worker_research_paper-prep-checklist_20260515T091715.log:11:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T192443_780445.jsonl:63:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T192443_780445.jsonl:148:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T192443_780445.jsonl:822:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:230:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:360:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:362:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:366:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:376:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:395:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:419:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:433:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:465:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260515T111343_128024.jsonl:482:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T151626_907501.jsonl:530:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1344:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1370:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1566:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1594:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1597:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1669:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1672:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1677:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1728:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1743:{\"ts\": \"2026-05-15T11:10:39.248586+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_5434474971bcc3bc52c4774796ba7f3d:reviewer\", \"text\": \"called Grep\", \"tool\": \"Grep\", \"tool_args\": {\"pattern\": \"mohamed2025_broken_telephone|dohmatob2024_strong_collapse|dohmatob2024_demystified\", \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib\", \"output_mode\": \"content\"}}\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1744:{\"ts\": \"2026-05-15T11:10:39.299197+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_5434474971bcc3bc52c4774796ba7f3d:reviewer\", \"text\": \"27:@inproceedings{dohmatob2024_strong_collapse,\\n36:@inproceedings{dohmatob2024_demystified,\\n45:@inproceedings{mohamed2025_broken_telephone,\", \"tool\": \"Grep\", \"elapsed_ms\": 50}\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1748:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T111339_981050.jsonl:1751:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d_reviewer_20260515T232944_248240.jsonl:539:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_2.jsonl:33:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_2.jsonl:60:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_2.jsonl:87:[Omitted long matching line]\nlogs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_reviewer_2.jsonl:96:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:9:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:28:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:29:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:31:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:33:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:35:[Omitted long matching line]\nlogs/workers/worker_writing_paper-polish-pagelimit_20260515T211857.log:37:[Omitted long matching line]\nlogs/chats/worker_research_bibliography_20260515T155440.jsonl:23:[Omitted long matching line]\nlogs/chats/worker_research_bibliography_20260515T155440.jsonl:26:[Omitted long matching line]\nlogs/chats/worker_research_bibliography_20260515T155440.jsonl:69:[Omitted long matching line]\nlogs/chats/worker_research_bibliography_20260515T155440.jsonl:71:[Omitted long matching line]\nlogs/chats/worker_writing_paper-polish-pagelimit_20260515T211857.jsonl:4:[Omitted long matching line]\nlogs/chats/worker_writing_paper-polish-pagelimit_20260515T211857.jsonl:19:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d.jsonl:470:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d.jsonl:499:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d.jsonl:1171:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d.jsonl:1340:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5434474971bcc3bc52c4774796ba7f3d.jsonl:1343:[Omitted long matching line]\nlogs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log:14:[Omitted long matching line]\nlogs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log:20:[Omitted long matching line]\nlogs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log:38:[Omitted long matching line]\nlogs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log:40:[Omitted long matching line]\nlogs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log:41:[Omitted long matching line]\nlogs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log:50:[Omitted long matching line]\ndocs/paper/main.bbl:61:  Kempe}]{dohmatob2024_strong_collapse}\ndocs/paper/main.aux:104:\\citation{dohmatob2024_strong_collapse}\ndocs/paper/main.aux:901:\\bibcite{dohmatob2024_strong_collapse}{{8}{2024{b}}{{Dohmatob et~al.}}{{Dohmatob, Feng, Subramonian, and Kempe}}}\nlogs/workers/worker_exp_w2_domain_bias_design_20260515T191751.log:57:[Omitted long matching line]\nlogs/workers/worker_paper_bibliography-terminology_20260515T155105.log:6:[Omitted long matching line]\nlogs/workers/worker_paper_bibliography-terminology_20260515T155105.log:9:[Omitted long matching line]\nlogs/workers/worker_paper_bibliography-terminology_20260515T155105.log:18:[Omitted long matching line]\nlogs/workers/worker_paper_bibliography-terminology_20260515T155105.log:44:[Omitted long matching line]\nlogs/workers/worker_research_literature_map_check_20260515T050221.log:162:[Omitted long matching line]\nlogs/workers/worker_research_literature_map_check_20260515T050221.log:163:[Omitted long matching line]\nlogs/workers/worker_research_literature_map_check_20260515T050221.log:165:[Omitted long matching line]\nlogs/workers/worker_research_literature_map_check_20260515T050221.log:166:[Omitted long matching line]\nlogs/workers/worker_paper_comprehensive-revision-r3_20260515T231048.log:13:[Omitted long matching line]\nlogs/workers/worker_paper_comprehensive-revision-r3_20260515T231048.log:27:[Omitted long matching line]\nlogs/workers/worker_paper_comprehensive-revision-r3_20260515T231048.log:104:[Omitted long matching line]\nlogs/workers/worker_paper_comprehensive-revision-r3_20260515T231048.log:106:[Omitted long matching line]\nlogs/workers/worker_writing_discussion-expand-orphan-bib_20260515T233628.log:10:[Omitted long matching line]\nlogs/workers/worker_writing_discussion-expand-orphan-bib_20260515T233628.log:17:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:11:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:19:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:20:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:21:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:23:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:24:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:29:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:30:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:31:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:34:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:35:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:36:[Omitted long matching line]\nlogs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442.log:38:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:7:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:13:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:14:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:15:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:143:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:170:[Omitted long matching line]\nlogs/workers/worker_paper_research_bib_fix_20260515T090356.log:171:[Omitted long matching line]\nlogs/workers/worker_fix_generalization_tex_integration_20260515T161350.log:34:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:14:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:20:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:76:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:100:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:142:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:145:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:151:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:154:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:160:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:173:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:174:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:195:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:197:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:199:[Omitted long matching line]\nlogs/workers/worker_writing_warning-review-fixes_20260515T200308.log:214:[Omitted long matching line]\nlogs/workers/worker_paper_r3_text_fixes_20260515T190112.log:23:[Omitted long matching line]\nlogs/workers/worker_paper_r3_text_fixes_20260515T190112.log:40:[Omitted long matching line]\nlogs/workers/worker_paper_r3_text_fixes_20260515T190112.log:114:[Omitted long matching line]\nlogs/workers/worker_paper_r3_text_fixes_20260515T190112.log:117:[Omitted long matching line]\nlogs/workers/worker_audit_paper-tex-status_20260515T233105.log:40:[Omitted long matching line]\nlogs/workers/worker_audit_paper-tex-status_20260515T233105.log:52:[Omitted long matching line]\nlogs/workers/worker_audit_paper-tex-status_20260515T233105.log:54:[Omitted long matching line]\nlogs/workers/worker_audit_paper-tex-status_20260515T233105.log:82:[Omitted long matching line]\nlogs/workers/worker_audit_paper-tex-status_20260515T233105.log:89:[Omitted long matching line]\nlogs/workers/worker_audit_paper-tex-status_20260515T233105.log:90:[Omitted long matching line]\nlogs/workers/worker_paper_writing_introduction_20260515T093227.log:18:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:7:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:10:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:19:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:32:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:39:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:63:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:65:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:67:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:69:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:71:[Omitted long matching line]\nlogs/workers/worker_writing_paper-bib-terminology_20260515T145355.log:78:[Omitted long matching line]\nlogs/workers/worker_paper_r3-writing-fixes_20260515T191626.log:26:[Omitted long matching line]\nlogs/workers/worker_paper_r3-writing-fixes_20260515T191626.log:28:[Omitted long matching line]\nlogs/workers/worker_paper_r3-writing-fixes_20260515T191626.log:177:[Omitted long matching line]\nlogs/workers/worker_paper_r3-writing-fixes_20260515T191626.log:179:[Omitted long matching line]\nlogs/workers/worker_paper_r3-writing-fixes_20260515T191626.log:181:[Omitted long matching line]\nlogs/workers/worker_paper_r3-comprehensive-patch_20260515T191446.log:23:[Omitted long matching line]\nlogs/workers/worker_paper_r3-comprehensive-patch_20260515T191446.log:25:[Omitted long matching line]\nlogs/workers/worker_research_covariate_shift_literature_20260515T050056.log:81:[Omitted long matching line]\nlogs/workers/worker_research_covariate_shift_literature_20260515T050056.log:110:[Omitted long matching line]\nlogs/workers/worker_research_covariate_shift_literature_20260515T050056.log:111:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:41:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:45:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:46:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:95:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:99:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:100:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:102:[Omitted long matching line]\nlogs/workers/worker_research_bibliography_20260515T155440.log:103:[Omitted long matching line]\nlogs/workers/worker_research_r2n2_literature_supplement_20260515T222540.log:11:[Omitted long matching line]\nlogs/workers/worker_research_r2n2_literature_supplement_20260515T222540.log:51:[Omitted long matching line]\nlogs/workers/worker_research_r2n2_literature_supplement_20260515T222540.log:57:[Omitted long matching line]\nlogs/workers/worker_research_r2n2_literature_supplement_20260515T222540.log:61:[Omitted long matching line]\nlogs/workers/worker_research_r2n2_literature_supplement_20260515T222540.log:62:[Omitted long matching line]\nlogs/workers/worker_write_section_method_20260515T162257.log:19:[Omitted long matching line]\nlogs/workers/worker_write_section_method_20260515T162257.log:25:[Omitted long matching line]\nlogs/workers/worker_writing_bib-integration-verified-refs_20260515T233017.log:6:[Omitted long matching line]\nlogs/workers/worker_writing_bib-integration-verified-refs_20260515T233017.log:12:[Omitted long matching line]\nlogs/workers/worker_writing_bib-integration-verified-refs_20260515T233017.log:14:[Omitted long matching line]\nlogs/workers/worker_writing_bib-integration-verified-refs_20260515T233017.log:16:[Omitted long matching line]\nlogs/workers/worker_research_literature-linkage-depth-extension_20260515T051604.log:8:[Omitted long matching line]",
    "numLines": 248
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01EccnSrFr2ZEfhrJHkfwnkc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "a5f705f4-c408-481f-95ef-a11418be7a85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqGhNqRe3rSUWRyyxjj1Na",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 52530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 41 · 2026-05-15T23:56:42.595Z_

<details><summary>↩ Tool result · `toolu_01EccnSrFr2ZEfhrJHkfwnkc`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
51	@misc{gerstgrasser2024_accumulate,
52	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
53	  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
54	  year      = {2024},
55	  howpublished = {arXiv:2404.01413},
56	  url       = {https://arxiv.org/abs/2404.01413},
57	}
58	
59	@inproceedings{marchi2024_heat_death,
60	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
61	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
62	  booktitle = {Proceedings of ICASSP},
63	  year      = {2024},
64	  note      = {arXiv:2404.02325},
65	  url       = {https://arxiv.org/abs/2404.02325},
66	}
67	
68	@misc{knowledge_collapse2025,
69	  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},
70	  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},
71	  year      = {2025},
72	  howpublished = {arXiv:2509.04796},
73	  url       = {https://arxiv.org/abs/2509.04796},
74	}
75	
76	@misc{sigma2026_spectral,
77	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
78	  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},
79	  year      = {2026},
80	  howpublished = {arXiv:2601.03385},
81	  url       = {https://arxiv.org/abs/2601.03385},
82	}
83	
84	@inproceedings{mohamed2025_broken_telephone,
85	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
86	  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
87	  booktitle = {Proceedings of ACL},
88	  year      = {2025},
89	  note      = {arXiv:2502.20258},
90	  url       = {https://arxiv.org/abs/2502.20258},
91	}
92	
93	@inproceedings{synthetic_eggs2026,
94	  author    = {Schaffelder, Max and Gatt, Albert},
95	  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},
96	  booktitle = {Findings of ACL},
97	  year      = {2026},
98	  note      = {arXiv:2511.01490},
99	  url       = {https://arxiv.org/abs/2511.01490},
100	}
101	
102	@inproceedings{shi2025_closer_look,
103	  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
104	  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},
105	  booktitle = {Advances in Neural Information Processing Systems},
106	  year      = {2025},
107	  note      = {Spotlight},
108	}
109	
110	@inproceedings{yi2026_escaping_collapse,
111	  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
112	  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},
113	  booktitle = {3rd DATA-FM Workshop at ICLR 2026},
114	  year      = {2026},
115	}
116	
117	% --- Model collapse: collapse-can-be-avoided / contamination ---
118	
119	@inproceedings{drayson2025_detection_prevents_collapse,
120	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
121	  title     = {{Machine-generated text detection prevents language model collapse}},
122	  booktitle = {Findings of EMNLP},
123	  year      = {2025},
124	  note      = {arXiv:2502.15654},
125	  url       = {https://arxiv.org/abs/2502.15654},
126	}
127	
128	@misc{bakshi2026_collapse_improvement,
129	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
130	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
131	  year      = {2026},
132	  howpublished = {arXiv:2602.10531},
133	  url       = {https://arxiv.org/abs/2602.10531},
134	}
135	
136	@misc{wang2026_contamination,
137	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
138	  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},
139	  year      = {2026},
140	  howpublished = {arXiv:2602.16065},
141	  url       = {https://arxiv.org/abs/2602.16065},
142	}
143	
144	@misc{falahati2026_curated,
145	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
146	  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},
147	  year      = {2026},
148	  howpublished = {arXiv:2605.07724},
149	  url       = {https://arxiv.org/abs/2605.07724},
150	}
151	
152	% ============================================================
153	% AI-Generated Text Detection
154	% ============================================================
155	
156	@article{wu2025_detection_survey,
157	  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
158	  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
159	  journal   = {Computational Linguistics},
160	  volume    = {51},
161	  number    = {1},
162	  pages     = {275--354},
163	  year      = {2025},
164	  publisher = {MIT Press},
165	}
166	
167	% --- Statistical / zero-shot detectors ---
168	
169	@inproceedings{gehrmann2019_gltr,
170	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
171	  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},
172	  booktitle = {Proceedings of ACL: System Demonstrations},
173	  year      = {2019},
174	  note      = {arXiv:1906.04043},
175	  url       = {https://arxiv.org/abs/1906.04043},
176	}
177	
178	@inproceedings{mitchell2023_detectgpt,
179	  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
180	  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
181	  booktitle = {Proceedings of ICML},
182	  year      = {2023},
183	  note      = {arXiv:2301.11305},
184	  url       = {https://arxiv.org/abs/2301.11305},
185	}
186	
187	@inproceedings{fast_detectgpt2024,
188	  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
189	  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
190	  booktitle = {Proceedings of ICLR},
191	  year      = {2024},
192	  note      = {arXiv:2310.05130},
193	  url       = {https://arxiv.org/abs/2310.05130},
194	}
195	
196	@inproceedings{binoculars2024,
197	  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
198	  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
199	  booktitle = {Proceedings of ICML},
200	  year      = {2024},
201	  note      = {arXiv:2401.12070},
202	  url       = {https://arxiv.org/abs/2401.12070},
203	}
204	
205	@article{diveye2026,
206	  author    = {Basani, Advik Raj and Chen, Pin-Yu},
207	  title     = {{Diversity Boosts AI-Generated Text Detection}},
208	  journal   = {Transactions on Machine Learning Research (TMLR)},
209	  year      = {2026},
210	  note      = {arXiv:2509.18880},
211	  url       = {https://arxiv.org/abs/2509.18880},
212	}
213	
214	% --- Robustness / limitations of detectors ---
215	
216	@misc{sadasivan2023_paraphrase,
217	  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
218	  title     = {{Can AI-Generated Text be Reliably Detected?}},
219	  year      = {2023},
220	  howpublished = {arXiv:2303.11156},
221	  url       = {https://arxiv.org/abs/2303.11156},
222	}
223	
224	@misc{pudasaini2026_detection_fails,
225	  author    = {Pudasaini, Shushanta and Miralles-Pech{\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},
226	  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},
227	  year      = {2026},
228	  howpublished = {arXiv:2603.23146},
229	  url       = {https://arxiv.org/abs/2603.23146},
230	}
231	
232	@misc{pu2026_generator_barrier,
233	  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
234	  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
235	  year      = {2026},
236	  howpublished = {arXiv:2604.13692},
237	  url       = {https://arxiv.org/abs/2604.13692},
238	}
239	
240	% --- Beyond binary: attribution, editing extent, benchmarks ---
241	
242	@inproceedings{bevendorff2025_two_paradigms,
243	  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},
244	  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},
245	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
246	  pages     = {3762--3787},
247	  year      = {2025},
248	  address   = {Vienna, Austria},
249	}
250	
251	@inproceedings{uchendu2020_attribution,
252	  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
253	  title     = {{Authorship Attribution for Neural Text Generation}},
254	  booktitle = {Proceedings of EMNLP},
255	  year      = {2020},
256	}
257	
258	@inproceedings{editlens2026,
259	  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},
260	  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},
261	  booktitle = {Proceedings of ICLR},
262	  year      = {2026},
263	  note      = {arXiv:2510.03154},
264	  url       = {https://arxiv.org/abs/2510.03154},
265	}
266	
267	@inproceedings{loki2025,
268	  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},
269	  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},
270	  booktitle = {Proceedings of ICLR (Spotlight)},
271	  year      = {2025},
272	  note      = {arXiv:2410.09732},
273	  url       = {https://arxiv.org/abs/2410.09732},
274	}
275	
276	% --- Statistical / feature-based / shared-task detectors ---
277	
278	@inproceedings{verma2024_ghostbuster,
279	  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
280	  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
281	  booktitle = {Proceedings of NAACL},
282	  year      = {2024},
283	  note      = {arXiv:2305.15047},
284	  url       = {https://arxiv.org/abs/2305.15047},
285	}
286	
287	@inproceedings{wang2024_m4_semeval,
288	  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
289	  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
290	  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},
291	  year      = {2024},
292	  note      = {arXiv:2404.14183},
293	  url       = {https://arxiv.org/abs/2404.14183},
294	}
295	
296	@inproceedings{yang2024_dnagpt,
297	  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
298	  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
299	  booktitle = {Proceedings of ICLR},
300	  year      = {2024},
301	  note      = {arXiv:2305.17359},
302	  url       = {https://arxiv.org/abs/2305.17359},
303	}
304	
305	% --- Watermarking ---
306	
307	@inproceedings{kirchenbauer2023_watermark,
308	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
309	  title     = {{A Watermark for Large Language Models}},
310	  booktitle = {Proceedings of ICML},
311	  year      = {2023},
312	  note      = {arXiv:2301.10226},
313	  url       = {https://arxiv.org/abs/2301.10226},
314	}
315	
316	% ============================================================
317	% Decoding Strategies
318	% ============================================================
319	
320	@inproceedings{holtzman2020_nucleus,
321	  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
322	  title     = {{The Curious Case of Neural Text Degeneration}},
323	  booktitle = {Proceedings of ICLR},
324	  year      = {2020},
325	  note      = {arXiv:1904.09751},
326	  url       = {https://arxiv.org/abs/1904.09751},
327	}
328	
329	@inproceedings{finlayson2024_closing,
330	  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},
331	  title     = {{Closing the Curious Case of Neural Text Degeneration}},
332	  booktitle = {Proceedings of ICLR},
333	  year      = {2024},
334	  note      = {arXiv:2310.01693},
335	  url       = {https://arxiv.org/abs/2310.01693},
336	}
337	
338	@inproceedings{garces_arias2025_decoding_decoded,
339	  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
340	  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
341	  booktitle = {Proceedings of COLING},
342	  year      = {2025},
343	  note      = {arXiv:2410.06097},
344	  url       = {https://arxiv.org/abs/2410.06097},
345	}
346	
347	@article{wiher2022_decoding,
348	  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},
349	  title     = {{On Decoding Strategies for Neural Text Generators}},
350	  journal   = {Transactions of the Association for Computational Linguistics},
351	  volume    = {10},
352	  pages     = {997--1012},
353	  year      = {2022},
354	}
355	
356	@inproceedings{basu2021_mirostat,
357	  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},
358	  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},
359	  booktitle = {Proceedings of ICLR},
360	  year      = {2021},
361	}
362	
363	% ============================================================
364	% Ordinal Classification / Contrastive Learning
365	% ============================================================
366	
367	@article{coral2020,
368	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
369	  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
370	  journal   = {Pattern Recognition Letters},
371	  volume    = {140},
372	  pages     = {325--331},
373	  year      = {2020},
374	  note      = {arXiv:1901.07884},
375	  url       = {https://arxiv.org/abs/1901.07884},
376	}
377	
378	@inproceedings{cloc2025,
379	  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},
380	  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},
381	  booktitle = {Proceedings of CVPR},
382	  year      = {2025},
383	  note      = {arXiv:2504.17813},
384	  url       = {https://arxiv.org/abs/2504.17813},
385	}
386	
387	% ============================================================
388	% Foundation Models / Fine-tuning
389	% ============================================================
390	
391	@inproceedings{hu2022lora,
392	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
393	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
394	  booktitle = {Proceedings of ICLR},
395	  year      = {2022},
396	  note      = {arXiv:2106.09685},
397	  url       = {https://arxiv.org/abs/2106.09685},
398	}
399	
400	@inproceedings{he2021_deberta_v3,
401	  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
402	  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},
403	  booktitle = {Proceedings of ICLR},
404	  year      = {2023},
405	  note      = {arXiv:2111.09543},
406	  url       = {https://arxiv.org/abs/2111.09543},
407	}
408	
409	@article{liu2019_roberta,
410	  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
411	  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},
412	  journal   = {arXiv preprint arXiv:1907.11692},
413	  year      = {2019},
414	  url       = {https://arxiv.org/abs/1907.11692},
415	}
416	
417	% ============================================================
418	% Data Curation / Selection
419	% ============================================================
420	
421	@inproceedings{dsir2023,
422	  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
423	  title     = {{Data Selection for Language Models via Importance Resampling}},
424	  booktitle = {Proceedings of NeurIPS},
425	  year      = {2023},
426	  note      = {arXiv:2302.03169},
427	  url       = {https://arxiv.org/abs/2302.03169},
428	}
429	
430	@inproceedings{qurating2024,
431	  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
432	  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},
433	  booktitle = {Proceedings of ICML},
434	  year      = {2024},
435	  note      = {arXiv:2402.09739},
436	  url       = {https://arxiv.org/abs/2402.09739},
437	}
438	
439	@article{sugiyama2007_importance_weighting,
440	  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
441	  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},
442	  journal   = {Journal of Machine Learning Research},
443	  volume    = {8},
444	  pages     = {985--1005},
445	  year      = {2007},
446	}
447	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "11e7ce62-613e-4d63-b545-fe411e81539b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
      "content": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n",
      "numLines": 447,
      "startLine": 1,
      "totalLines": 447
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
The grep found `dohmatob2024_strong_collapse` in several places:
1. `artifacts/_project/paper/references.bib` line 24 - needs to be synced (will be overwritten)
2. `artifacts/_project/paper/citations_audit.md` - this is a report/artifact, not a source file
3. `artifacts/review_reports/round_1.md` - this is a review report
4. `literature_map.yaml` - this maps literature

The .tex files are already fixed (references.bib and related_work.tex). 

I should focus on what was actually requested: syncing the artifacts bib by copying from docs/paper, and the .tex references are already corrected. The other files like citations_audit.md, review reports, and literature_map.yaml are historical metadata that don't need updating for this task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "595afeb2-bad1-4b46-ade1-80717585d7e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKQC1tKwoDurkrxjHD5sVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9071,
      "cache_read_input_tokens": 52753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9071
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

_source line 43_

artifacts bib 需要同步，同时更新 literature_map.yaml 中的旧 key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "fd60c5d4-1c68-4848-87e6-2a381e508871",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKQC1tKwoDurkrxjHD5sVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9071,
      "cache_read_input_tokens": 52753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9071
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01NtQkDWCST5dwBJ7qhVj6QY`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
  "description": "Copy docs/paper bib to artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "47f2c795-5afe-4ca2-b087-97d5c72567f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKQC1tKwoDurkrxjHD5sVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9071,
      "cache_read_input_tokens": 52753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9071
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

_source line 45 · 2026-05-15T23:56:57.117Z_

<details><summary>↩ Tool result · `toolu_01NtQkDWCST5dwBJ7qhVj6QY`</summary>

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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e349c1fd-38d6-48e8-8ff0-e7a76d95200b",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01KPKw8hVGLjsdsv27FLME28`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
  "offset": 50,
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e2f736b8-7856-4fc0-ab9b-b4397b6a4932",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKQC1tKwoDurkrxjHD5sVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9071,
      "cache_read_input_tokens": 52753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9071
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

_source line 47 · 2026-05-15T23:56:57.825Z_

<details><summary>↩ Tool result · `toolu_01KPKw8hVGLjsdsv27FLME28`</summary>

```text
50	  notes: >
51	    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from
52	    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.
53	    Explains why temp produces different statistical fingerprint from truncation.
54	
55	dohmatob2024_strong_collapse:
56	  title: "Strong Model Collapse"
57	  authors: [Dohmatob, Feng, Subramonian, Kempe]
58	  venue: ICLR 2025 Spotlight
59	  year: 2024
60	  arxiv: "2410.04840"
61	  tags: [model-collapse, scaling, synthetic-data]
62	  relevance: indirect
63	  cite_in: [related-work]
64	  notes: >
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "d4b37a8e-6150-4ae2-8ee7-b6ed51e5496e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
      "content": "  notes: >\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\n    Explains why temp produces different statistical fingerprint from truncation.\n\ndohmatob2024_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2024\n  arxiv: \"2410.04840\"\n  tags: [model-collapse, scaling, synthetic-data]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >",
      "numLines": 15,
      "startLine": 50,
      "totalLines": 695
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01WeWJ5hSE5HXH6htCAvdf8H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
  "offset": 55,
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "65920251-fc60-4d93-b0ac-cb915415eb9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fFmygBrNLDheHk6x6du9n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 61824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 939
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

_source line 49 · 2026-05-15T23:57:00.894Z_

<details><summary>↩ Tool result · `toolu_01WeWJ5hSE5HXH6htCAvdf8H`</summary>

```text
55	dohmatob2024_strong_collapse:
56	  title: "Strong Model Collapse"
57	  authors: [Dohmatob, Feng, Subramonian, Kempe]
58	  venue: ICLR 2025 Spotlight
59	  year: 2024
60	  arxiv: "2410.04840"
61	  tags: [model-collapse, scaling, synthetic-data]
62	  relevance: indirect
63	  cite_in: [related-work]
64	  notes: >
65	    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.
66	    Bias-variance decomposition via random projections.
67	
68	dohmatob2024_demystified:
69	  title: "Model Collapse Demystified: The Case of Regression"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "aedaba70-ac65-4fbd-a536-d72de06cfd4e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
      "content": "dohmatob2024_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2024\n  arxiv: \"2410.04840\"\n  tags: [model-collapse, scaling, synthetic-data]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\n    Bias-variance decomposition via random projections.\n\ndohmatob2024_demystified:\n  title: \"Model Collapse Demystified: The Case of Regression\"",
      "numLines": 15,
      "startLine": 55,
      "totalLines": 695
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01KPrCwWFzabCUyA4KUYdMwe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
  "old_string": "dohmatob2024_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2024",
  "new_string": "dohmatob2025_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "3954abd2-224c-41ea-a258-90d6821f8fd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jdru3pq4dZUUm6ezqYekWn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 62763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
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

_source line 51 · 2026-05-15T23:57:04.671Z_

<details><summary>↩ Tool result · `toolu_01KPrCwWFzabCUyA4KUYdMwe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "4bf60d32-bc95-40ee-ab3d-b49a202e37ff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
    "oldString": "dohmatob2024_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2024",
    "newString": "dohmatob2025_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2025",
    "originalFile": "# Literature Map — recursive_gen_depth_est\n# Last updated: 2026-05-15\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\n#\n# Tags used for cite_in: introduction, related-work, background, method,\n#   experiments, discussion, limitations, dcol-section\n\n# =============================================================\n# MODEL COLLAPSE — foundational theory & recursive generation\n# =============================================================\n\nshumailov2024_nature:\n  title: \"AI models collapse when trained on recursively generated data\"\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\n  venue: Nature\n  year: 2024\n  doi: \"10.1038/s41586-024-07566-y\"\n  tags: [model-collapse, recursive-generation, tail-erosion]\n  relevance: direct\n  cite_in: [introduction, related-work, background]\n  notes: >\n    Foundational model collapse paper. Tail erosion across recursive generations.\n    Perplexity monotonically increases over 40 generations. Does NOT compare\n    sampling strategies—uses standard sampling (T=1).\n\nmarchi2024_heat_death:\n  title: \"Heat Death of Generative Models in Closed-Loop Learning\"\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\n  venue: ICASSP 2025\n  year: 2024\n  arxiv: \"2404.02325\"\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\n  relevance: direct\n  cite_in: [discussion]\n  notes: >\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\n    support for our tau=0.9 accelerated convergence finding.\n\ndohmatob2024_tale_of_tails:\n  title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n  authors: [Dohmatob, Feng, Yang, Charton, Kempe]\n  venue: ICML 2024\n  year: 2024\n  arxiv: \"2402.07043\"\n  tags: [scaling-laws, tail-narrowing, tail-cutting, temperature, top-p, top-k]\n  relevance: direct\n  cite_in: [related-work, discussion]\n  notes: >\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\n    Explains why temp produces different statistical fingerprint from truncation.\n\ndohmatob2024_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2024\n  arxiv: \"2410.04840\"\n  tags: [model-collapse, scaling, synthetic-data]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\n    Bias-variance decomposition via random projections.\n\ndohmatob2024_demystified:\n  title: \"Model Collapse Demystified: The Case of Regression\"\n  authors: [Dohmatob, Feng, Kempe]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv: \"2402.07712\"\n  tags: [model-collapse, regression, random-matrix-theory]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Test error grows linearly with iteration count in regression.\n    Supports our finding of monotonically evolving features across depths.\n\nalemohammad2024_mad:\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: [Alemohammad, Casco-Rodriguez, et al.]\n  venue: ICLR 2024\n  year: 2024\n  arxiv: \"2307.01850\"\n  tags: [autophagous, sampling-bias, precision-recall, MAD]\n  relevance: indirect\n  cite_in: [introduction, related-work]\n  notes: >\n    Biased sampling keeps precision but kills recall. Unbiased causes mode drift.\n    tau=0.9 maps to their biased sampling regime.\n\ngerstgrasser2024_accumulate:\n  title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n  authors: [Gerstgrasser, Schaeffer, et al.]\n  venue: arXiv preprint\n  year: 2024\n  arxiv: \"2404.01413\"\n  tags: [model-collapse, data-accumulation, mitigation]\n  relevance: indirect\n  cite_in: [related-work, discussion]\n  notes: >\n    Data accumulation prevents collapse (bounded test error).\n    Important caveat: in accumulation regime, depth signal may be weaker.\n\ndrayson2025_detection_prevents_collapse:\n  title: \"Machine-generated text detection prevents language model collapse\"\n  authors: [Drayson et al.]\n  venue: EMNLP 2025 Findings\n  year: 2025\n  arxiv: \"2502.15654\"\n  tags: [temperature, diversity, recursive-training, detection]\n  relevance: direct\n  cite_in: [related-work]\n  notes: >\n    Temperature tau=0.9 produces most repetitive outputs; diversity drops ~70%\n    over 99 recursive generations (GPT-2, SmolLM2). Perplexity degradation more\n    moderate than deterministic methods. Detection as filter vs our depth estimation.\n\nbakshi2026_collapse_improvement:\n  title: \"From Collapse to Improvement: Statistical Perspectives on Iterative Training\"\n  authors: [Bakshi, Chakraborty]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2602.10531\"\n  tags: [model-collapse, non-monotonic, data-mixing]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Iterative training with fresh real data can *improve* performance.\n    Non-monotonic dynamics complicate simple depth-signal assumptions.\n\nwang2026_contamination:\n  title: \"Can Generative AI Survive Data Contamination? Theoretical Guarantees\"\n  authors: [Wang, Niu, Li]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2602.16065\"\n  tags: [model-collapse, contamination, theoretical]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Extends collapse theory beyond Gaussian/discrete to realistic distributions.\n    Provides theoretical grounding for depth signal existence.\n\nfalahati2026_curated:\n  title: \"Curated Synthetic Data Doesn't Have to Collapse\"\n  authors: [Falahati, Amiri, Larson, Golab]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2605.07724\"\n  tags: [curation, collapse-prevention, pluralistic]\n  relevance: indirect\n  cite_in: [discussion, limitations]\n  notes: >\n    Pluralistic curation prevents collapse. Harder case for our method —\n    curated pipelines may produce depth-invariant text.\n\nknowledge_collapse2025:\n  title: \"Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\"\n  authors: [Keisha, Wu, Wang, Koshiyama, Treleaven]\n  venue: arXiv preprint\n  year: 2025\n  arxiv: \"2509.04796\"\n  tags: [knowledge-collapse, fluency, factual-degradation]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Three-stage collapse: factual accuracy degrades while fluency persists.\n    Surface perplexity features still capture depth signal despite fluency preservation.\n\nsynthetic_eggs2026:\n  title: \"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\"\n  authors: [Schaffelder, Gatt]\n  venue: ACL 2026 Findings\n  year: 2026\n  arxiv: \"2511.01490\"\n  tags: [diversity, collapse-mitigation, Self-BLEU]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Multi-source synthetic data reduces collapse. Their diversity metrics\n    (Self-BLEU, lexical diversity) are candidate depth features.\n\nmohamed2025_broken_telephone:\n  title: \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"\n  authors: [Mohamed, Geng, Vazirgiannis, Shang]\n  venue: ACL 2025\n  year: 2025\n  arxiv: \"2502.20258\"\n  tags: [iterative-generation, information-distortion, translation-chain]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Iterative generation (translation/paraphrase chains) produces monotonically\n    increasing information distortion. Cross-task evidence that iterated signals\n    accumulate — supports our depth signal persistence finding.\n\nsigma2026_spectral:\n  title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n  authors: [\"(multiple)\"]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2601.03385\"\n  tags: [spectral-analysis, gram-matrix, representation-collapse, 50-generations]\n  relevance: direct\n  cite_in: [related-work, discussion]\n  notes: >\n    Gram matrix spectral analysis tracks representation space contraction over\n    50 recursive generations. Proposes Sigma-UB metric. Complementary to our\n    EDD — they measure geometric collapse, we measure statistical distinguishability.\n    Tests 50 generations but does NOT do inter-generation classification.\n\n# --- R2-N2 supplement: model collapse empirical ---\n\nshi2025_closer_look:\n  title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n  authors: [Shi, Wu, Zhang, Zhang, Tao, Qu]\n  venue: NeurIPS 2025 (Spotlight)\n  year: 2025\n  arxiv: \"2509.16499\"\n  tags: [model-collapse, entropy, memorization, intrinsic-dimension]\n  relevance: direct\n  role: background\n  verified: true\n  integration: \"整合，entropy ↔ depth signal 支撑特征选择论证\"\n  cite_in: [related-work, discussion]\n  notes: >\n    Identifies generalization-to-memorization transition during recursive training.\n    Entropy of training data decreases over iterations, strongly correlated with\n    model degradation. Entropy decline IS a measurable depth signal — directly\n    supports our statistical feature approach to depth estimation.\n\nyi2026_escaping_collapse:\n  title: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\n  authors: [Yi, Liu, Cheng, Xu]\n  venue: 3rd DATA-FM Workshop @ ICLR 2026\n  year: 2026\n  arxiv: \"2510.16657\"\n  tags: [model-collapse, verification, synthetic-data, mitigation]\n  relevance: indirect\n  role: background\n  verified: true\n  integration: \"引用但降级——related work 提一句，不支撑核心 claim（workshop paper）\"\n  cite_in: [related-work]\n  notes: >\n    Verifier-guided retraining prevents collapse. Our depth estimation\n    can serve AS the verifier — depth score enables graduated filtering\n    rather than binary accept/reject. NOTE: workshop paper, not main conference.\n\n# =============================================================\n# DECODING STRATEGIES\n# =============================================================\n\nholtzman2020_nucleus:\n  title: \"The Curious Case of Neural Text Degeneration\"\n  authors: [Holtzman, Buys, Du, Forbes, Choi]\n  venue: ICLR 2020\n  year: 2020\n  arxiv: \"1904.09751\"\n  tags: [nucleus-sampling, temperature, text-degeneration, unreliable-tail]\n  relevance: indirect\n  cite_in: [background, method]\n  notes: >\n    Proposes nucleus sampling. Temperature+top-k leads to repetition.\n    Key concept: unreliable tail of low-probability tokens.\n\nfinlayson2024_closing:\n  title: \"Closing the Curious Case of Neural Text Degeneration\"\n  authors: [Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal]\n  venue: ICLR 2024\n  year: 2024\n  arxiv: \"2310.01693\"\n  tags: [softmax-bottleneck, truncation-sampling, precise-sampling]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Truncation sampling eliminates softmax bottleneck errors. Mechanistic\n    difference between truncation and scaling approaches.\n\ngarces_arias2025_decoding_decoded:\n  title: \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\"\n  authors: [Garces Arias et al.]\n  venue: COLING 2025\n  year: 2025\n  tags: [decoding, hyperparameters, model-dependent]\n  relevance: direct\n  cite_in: [related-work, discussion]\n  notes: >\n    Confirms optimal decoding configuration is model-dependent.\n    Directly supports D006 finding (strategy effect is model-dependent).\n    Key external validation for our interaction effects claim.\n\nwiher2022_decoding:\n  title: \"On Decoding Strategies for Neural Text Generators\"\n  authors: [Wiher, Meister, Cotterell]\n  venue: TACL 2022\n  year: 2022\n  tags: [decoding, task-dependent, evaluation]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Decoding strategy effects are task-dependent.\n    Supports our finding that strategy effects on depth signal vary by model.\n\nbasu2021_mirostat:\n  title: \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\"\n  authors: [Basu, Sachdev, Kamdar, Nishi]\n  venue: ICLR 2021\n  year: 2021\n  tags: [perplexity-control, sampling, cross-entropy]\n  relevance: indirect\n  cite_in: [related-work, discussion]\n  notes: >\n    Perplexity and sampling parameters have non-linear relationship.\n    Relevant to p90_ppl capturing depth signal better than mean_ppl\n    under heavy-tailed distributions.\n\n# =============================================================\n# BINARY / ZERO-SHOT DETECTION\n# =============================================================\n\nmitchell2023_detectgpt:\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: [Mitchell, Lee, Khazatsky, Manning, Finn]\n  venue: ICML 2023\n  year: 2023\n  arxiv: \"2301.11305\"\n  tags: [zero-shot, detection, curvature, perturbation, binary]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Foundational zero-shot detector using log-probability curvature via\n    random perturbations. Binary only. Fast-DetectGPT improves efficiency.\n\nsadasivan2023_paraphrase:\n  title: \"Can AI-Generated Text be Reliably Detected?\"\n  authors: [Sadasivan, Kumar, Balasubramanian, Wang, Feizi]\n  venue: arXiv preprint\n  year: 2023\n  arxiv: \"2303.11156\"\n  tags: [detection-limits, paraphrase-attack, impossibility]\n  relevance: indirect\n  cite_in: [related-work, limitations]\n  notes: >\n    Shows paraphrase attacks evade all detectors; proves impossibility\n    result when model and human distributions overlap sufficiently.\n    Important limitation context for our depth estimation approach.\n\nbinoculars2024:\n  title: \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"\n  authors: [Hans, Schwarzschild, Manber, et al.]\n  venue: ICML 2024\n  year: 2024\n  arxiv: \"2401.12070\"\n  tags: [zero-shot, detection, perplexity-ratio, binary]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Two-model perplexity ratio for zero-shot binary detection.\n    We extend beyond binary to ordinal depth.\n\nfast_detectgpt2024:\n  title: \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\"\n  authors: [Bao et al.]\n  venue: ICLR 2024\n  year: 2024\n  arxiv: \"2310.05130\"\n  tags: [zero-shot, detection, curvature, binary]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Conditional probability curvature for efficient binary detection.\n    Cannot distinguish depth levels.\n\ndiveye2026:\n  title: \"DivEye: Diversity Boosts AI-Generated Text Detection\"\n  authors: [Basani, Chen]\n  venue: ICLR 2026 / TMLR\n  year: 2026\n  arxiv: \"2509.18880\"\n  tags: [surprisal-diversity, statistical-features, detection]\n  relevance: direct\n  cite_in: [related-work, method]\n  notes: >\n    Token-level surprisal diversity features for binary detection.\n    Feature overlap with our pipeline. We extend similar features\n    to ordinal depth regression.\n\nloki2025:\n  title: \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\"\n  authors: [Ye, Zhou, Huang, Zhang, Bai, Kang, He, Lin, Wang, Wu, Wu, Chen, Lin, He, Li]\n  venue: ICLR 2025 Spotlight\n  year: 2025\n  arxiv: \"2410.09732\"\n  tags: [benchmark, multimodal, detection]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Multimodal synthetic data detection benchmark. Binary only, no depth.\n\ngehrmann2019_gltr:\n  title: \"GLTR: Statistical Detection and Visualization of Generated Text\"\n  authors: [Gehrmann, Strobelt, Rush]\n  venue: ACL 2019\n  year: 2019\n  arxiv: \"1906.04043\"\n  tags: [detection, statistical-features, perplexity, rank, entropy]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Foundational statistical detection using log-likelihood, rank, entropy.\n    Our feature system extends this paradigm to recursive depth estimation.\n\npudasaini2026_detection_fails:\n  title: \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI\"\n  authors: [Pudasaini et al.]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2603.23146\"\n  tags: [detection-failure, distribution-shift, fragility]\n  relevance: indirect\n  cite_in: [limitations]\n  notes: >\n    Detection features degrade under distribution shift.\n    If binary features are domain-fragile, ordinal depth features may be too.\n\n# --- R2-N2 supplement: detection methods ---\n\ntulchinskii2024_intrinsic_dim:\n  title: \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\"\n  authors: [Tulchinskii, Kuznetsov, et al.]\n  venue: NeurIPS 2023\n  year: 2023\n  arxiv: \"2306.04723\"\n  tags: [intrinsic-dimension, geometric-features, detection, cross-domain]\n  relevance: direct\n  role: method-component\n  cite_in: [related-work, method]\n  notes: >\n    Intrinsic dimension of text embeddings ~9 for human, ~7.5 for AI-generated.\n    Geometric invariant enables cross-domain, cross-model robust detection.\n    Complementary feature family to our statistical perplexity features —\n    intrinsic dimension could serve as additional depth feature.\n\nverma2024_ghostbuster:\n  title: \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\"\n  authors: [Verma, Fleisig, Tomlin, Klein]\n  venue: NAACL 2024\n  year: 2024\n  arxiv: \"2305.15047\"\n  tags: [detection, structured-search, statistical-features, cross-domain]\n  relevance: indirect\n  role: direct-competitor\n  cite_in: [related-work]\n  notes: >\n    Structured search over combinations of weaker LM features for detection.\n    99.0 F1 cross-domain. Binary only. Feature engineering approach parallels\n    our multi-feature pipeline but targets binary classification, not ordinal depth.\n\nli2024_mage:\n  title: \"MAGE: Machine-generated Text Detection in the Wild\"\n  authors: [Li, Li, et al.]\n  venue: ACL 2024\n  year: 2024\n  arxiv: \"2305.13242\"\n  tags: [benchmark, cross-domain, cross-model, detection]\n  relevance: indirect\n  role: evaluation\n  cite_in: [related-work]\n  notes: >\n    Cross-domain cross-model detection benchmark. Finds significant OOD\n    performance degradation — same generalization challenge our cross-model\n    depth estimation faces. Binary detection only.\n\nwu2025_detection_survey:\n  title: \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\"\n  authors: [Wu, Yang, Zhan, Yuan, Chao, Wong]\n  venue: Computational Linguistics, Vol. 51, Issue 1\n  year: 2025\n  arxiv: \"2310.14724\"\n  tags: [survey, detection-taxonomy, watermarking, statistical, neural]\n  relevance: indirect\n  role: background\n  verified: true\n  integration: \"整合，survey 定位\"\n  cite_in: [related-work]\n  notes: >\n    Comprehensive survey of detection paradigms: watermarking, statistical,\n    neural, human-assisted. Positions our work as extending the statistical\n    paradigm from binary detection to ordinal depth estimation.\n\n# =============================================================\n# ADJACENT TASK — editing extent, attribution\n# =============================================================\n\neditlens2026:\n  title: \"EditLens: Quantifying the Extent of AI Editing in Text\"\n  authors: [Thai et al.]\n  venue: ICLR 2026\n  year: 2026\n  arxiv: \"2510.03154\"\n  tags: [editing-extent, continuous-score, mixed-authorship]\n  relevance: direct\n  cite_in: [introduction, related-work]\n  notes: >\n    Closest conceptual neighbor — both go beyond binary classification.\n    EditLens = single-pass editing extent; ours = multi-generation depth.\n\nuchendu2020_attribution:\n  title: \"Authorship Attribution for Neural Text Generation\"\n  authors: [Uchendu, Le, Shu, Lee]\n  venue: EMNLP 2020\n  year: 2020\n  tags: [attribution, multi-source, authorship]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Multi-source attribution (which model?). We solve a different axis\n    (how many iterations?) — complementary problems.\n\npu2026_generator_barrier:\n  title: \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\"\n  authors: [Pu, Cheng, Yuan, Wu, Bi]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2604.13692\"\n  tags: [disentanglement, cross-generator, generalization]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Cross-generator generalization via disentanglement.\n    Analogous to our cross-model generalization challenge.\n\n# --- R2-N2 supplement: attribution paradigms ---\n\nbevendorff2025_two_paradigms:\n  title: \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\"\n  authors: [Bevendorff, Wiegmann, Richter, Potthast, Stein]\n  venue: ACL 2025 Findings\n  year: 2025\n  tags: [attribution, verification, detection-paradigm, authorship]\n  relevance: direct\n  role: background\n  verified: true\n  integration: \"整合，'第三范式' framing（attribution/verification 之外的正交第三维度）\"\n  cite_in: [related-work]\n  notes: >\n    Reframes LLM detection as authorship verification (not attribution).\n    Our depth estimation is a third paradigm — ordinal characterization\n    beyond binary verification or multi-class attribution. Key framing\n    reference for positioning our contribution.\n\n# =============================================================\n# METHOD COMPONENT — ordinal classification\n# =============================================================\n\ncoral2020:\n  title: \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\"\n  authors: [Cao, Mirjalili, Raschka]\n  venue: Pattern Recognition Letters\n  year: 2020\n  arxiv: \"1901.07884\"\n  tags: [ordinal-classification, rank-consistency, cumulative-logits]\n  relevance: direct\n  cite_in: [method, experiments]\n  notes: >\n    CORAL ordinal classification framework used in our baseline battery.\n    Rank-consistent cumulative logits for ordinal targets.\n\ncloc2025:\n  title: \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\"\n  authors: [Pitawela, Carneiro, et al.]\n  venue: CVPR 2025\n  year: 2025\n  arxiv: \"2504.17813\"\n  tags: [contrastive-learning, ordinal, multi-margin, N-pair]\n  relevance: direct\n  cite_in: [method, dcol-section]\n  notes: >\n    DCOL is our adaptation of CLOC to text depth estimation.\n    Multi-margin N-pair loss for ordinal-aware contrastive learning.\n    Must cite as methodological basis for DCOL section.\n\n# =============================================================\n# WATERMARKING\n# =============================================================\n\nkirchenbauer2023_watermark:\n  title: \"A Watermark for Large Language Models\"\n  authors: [Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein]\n  venue: ICML 2023\n  year: 2023\n  arxiv: \"2301.10226\"\n  tags: [watermarking, proactive-detection, green-list]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Proactive detection via watermarking. Complementary —\n    watermarking requires generator cooperation; our method is post-hoc.\n\n# =============================================================\n# DATA CURATION\n# =============================================================\n\ndsir2023:\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: [Xie, Santurkar, Ma, Liang]\n  venue: NeurIPS 2023\n  year: 2023\n  arxiv: \"2302.03169\"\n  tags: [data-selection, importance-resampling, curation]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Quality-based data selection for LM training.\n    Our depth estimation enables depth-graduated curation (Claim 3 / Discussion).\n\nqurating2024:\n  title: \"QuRating: Selecting High-Quality Data for Training Language Models\"\n  authors: [Wettig, Gupta, et al.]\n  venue: ICML 2024\n  year: 2024\n  arxiv: \"2402.09739\"\n  tags: [quality-rating, data-curation, LLM-judgments]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    LLM-based quality rating for data selection.\n    Our depth score is a complementary quality axis.\n\n# --- R2-N2 supplement: data curation at scale ---\n\npenedo2024_fineweb:\n  title: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\n  authors: [Penedo, Kydlicek, et al.]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv: \"2406.17557\"\n  tags: [data-curation, quality-filtering, deduplication, web-scale]\n  relevance: indirect\n  role: background\n  cite_in: [discussion]\n  notes: >\n    15T token dataset with systematic quality filtering pipeline (dedup,\n    heuristic filters, classifier-based selection). Our depth estimation\n    adds a synthetic contamination axis complementary to FineWeb-style\n    quality curation — depth score can flag recursively degraded text\n    that passes standard quality filters.\n\n# =============================================================\n# COVARIATE SHIFT — technical background\n# =============================================================\n\nsugiyama2007_importance_weighting:\n  title: \"Covariate Shift Adaptation by Importance Weighted Cross Validation\"\n  authors: [Sugiyama, Krauledat, Mueller]\n  venue: JMLR\n  year: 2007\n  tags: [covariate-shift, importance-weighting, domain-adaptation]\n  relevance: background\n  cite_in: [discussion]\n  notes: >\n    Theoretical foundation for covariate shift correction.\n    Our z-score normalization is a simplified distribution alignment.\n\n# =============================================================\n# COVERAGE CHECKLIST (paper_framing.md Dream D002 requirements)\n# =============================================================\n# [x] watermarking: kirchenbauer2023_watermark\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\n#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate\n# [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,\n#     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)\n# [x] data curation: dsir2023, qurating2024, penedo2024_fineweb (NEW)\n# [x] multi-source attribution: uchendu2020_attribution,\n#     bevendorff2025_two_paradigms (VERIFIED)\n# [x] binary detectors: mitchell2023_detectgpt, sadasivan2023_paraphrase,\n#     binoculars2024, fast_detectgpt2024, diveye2026, loki2025,\n#     tulchinskii2024_intrinsic_dim (NEW), verma2024_ghostbuster (NEW),\n#     li2024_mage (NEW)\n# [x] detection survey: wu2025_detection_survey (VERIFIED)\n# [x] decoding strategy effects: garces_arias2025, holtzman2020_nucleus,\n#     wiher2022_decoding, basu2021_mirostat, finlayson2024_closing\n# [x] ordinal classification: coral2020, cloc2025\n# [x] adjacent tasks: editlens2026\n# [x] covariate shift: sugiyama2007\n# [x] statistical detection foundation: gehrmann2019_gltr\n#\n# Total unique entries: 43 (35 original + 8 R2-N2 supplement)\n# 2024-2026 papers: 30/43 (70% recent coverage)\n# Direct relevance: 12 entries\n",
    "structuredPatch": [
      {
        "oldStart": 52,
        "oldLines": 11,
        "newStart": 52,
        "newLines": 11,
        "lines": [
          "     tail cutting (top-p/top-k: hard truncation). Different degradation patterns.",
          "     Explains why temp produces different statistical fingerprint from truncation.",
          " ",
          "-dohmatob2024_strong_collapse:",
          "+dohmatob2025_strong_collapse:",
          "   title: \"Strong Model Collapse\"",
          "   authors: [Dohmatob, Feng, Subramonian, Kempe]",
          "   venue: ICLR 2025 Spotlight",
          "-  year: 2024",
          "+  year: 2025",
          "   arxiv: \"2410.04840\"",
          "   tags: [model-collapse, scaling, synthetic-data]",
          "   relevance: indirect"
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

检查 literature_map.yaml 中另一处旧 key 引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "f6370932-5d9c-4e1f-b26a-737653b06f85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YSw5JmcTugeVrMyr5dFb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 63106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
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

<details open><summary>🔧 Tool call — Grep · `toolu_01DJp8SU2UMDK69FYegxSuD6`</summary>

```json
{
  "pattern": "dohmatob2024_strong_collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
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
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "59063ed3-19f6-4eaa-bb60-c679e269190a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YSw5JmcTugeVrMyr5dFb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 63106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 429
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

_source line 54 · 2026-05-15T23:57:08.196Z_

<details><summary>↩ Tool result · `toolu_01DJp8SU2UMDK69FYegxSuD6`</summary>

```text
673:#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "4d7d3d7b-7291-40d4-893c-e47e77c9eddb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "673:#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01HikUqJEE6djTt3UaDdS5tj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
  "offset": 670,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "d1eb866a-da30-441c-9ef4-c817a497f376",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFUK3siPWPnVYQgpVoeR4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 193,
      "cache_read_input_tokens": 63535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 193
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

_source line 56 · 2026-05-15T23:57:10.734Z_

<details><summary>↩ Tool result · `toolu_01HikUqJEE6djTt3UaDdS5tj`</summary>

```text
670	# =============================================================
671	# [x] watermarking: kirchenbauer2023_watermark
672	# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,
673	#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,
674	#     dohmatob2024_demystified, gerstgrasser2024_accumulate
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "505b224c-0a4a-4409-89a1-345ca39d191a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
      "content": "# =============================================================\n# [x] watermarking: kirchenbauer2023_watermark\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\n#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate",
      "numLines": 5,
      "startLine": 670,
      "totalLines": 695
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Edit · `toolu_01CK7jd8ZRYTqcXyPhg243Ga`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
  "old_string": "#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,",
  "new_string": "#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "30cad846-94b8-4fcd-a8a5-4f384d4c8ff0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvBi1sx1UUrhmf1K9CH7Gk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 63728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 241
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

_source line 58 · 2026-05-15T23:57:14.537Z_

<details><summary>↩ Tool result · `toolu_01CK7jd8ZRYTqcXyPhg243Ga`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "257c1860-3917-441b-97c1-65f4e6f75141",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml",
    "oldString": "#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,",
    "newString": "#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,",
    "originalFile": "# Literature Map — recursive_gen_depth_est\n# Last updated: 2026-05-15\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\n#\n# Tags used for cite_in: introduction, related-work, background, method,\n#   experiments, discussion, limitations, dcol-section\n\n# =============================================================\n# MODEL COLLAPSE — foundational theory & recursive generation\n# =============================================================\n\nshumailov2024_nature:\n  title: \"AI models collapse when trained on recursively generated data\"\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\n  venue: Nature\n  year: 2024\n  doi: \"10.1038/s41586-024-07566-y\"\n  tags: [model-collapse, recursive-generation, tail-erosion]\n  relevance: direct\n  cite_in: [introduction, related-work, background]\n  notes: >\n    Foundational model collapse paper. Tail erosion across recursive generations.\n    Perplexity monotonically increases over 40 generations. Does NOT compare\n    sampling strategies—uses standard sampling (T=1).\n\nmarchi2024_heat_death:\n  title: \"Heat Death of Generative Models in Closed-Loop Learning\"\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\n  venue: ICASSP 2025\n  year: 2024\n  arxiv: \"2404.02325\"\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\n  relevance: direct\n  cite_in: [discussion]\n  notes: >\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\n    support for our tau=0.9 accelerated convergence finding.\n\ndohmatob2024_tale_of_tails:\n  title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n  authors: [Dohmatob, Feng, Yang, Charton, Kempe]\n  venue: ICML 2024\n  year: 2024\n  arxiv: \"2402.07043\"\n  tags: [scaling-laws, tail-narrowing, tail-cutting, temperature, top-p, top-k]\n  relevance: direct\n  cite_in: [related-work, discussion]\n  notes: >\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\n    Explains why temp produces different statistical fingerprint from truncation.\n\ndohmatob2025_strong_collapse:\n  title: \"Strong Model Collapse\"\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\n  venue: ICLR 2025 Spotlight\n  year: 2025\n  arxiv: \"2410.04840\"\n  tags: [model-collapse, scaling, synthetic-data]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\n    Bias-variance decomposition via random projections.\n\ndohmatob2024_demystified:\n  title: \"Model Collapse Demystified: The Case of Regression\"\n  authors: [Dohmatob, Feng, Kempe]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv: \"2402.07712\"\n  tags: [model-collapse, regression, random-matrix-theory]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Test error grows linearly with iteration count in regression.\n    Supports our finding of monotonically evolving features across depths.\n\nalemohammad2024_mad:\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: [Alemohammad, Casco-Rodriguez, et al.]\n  venue: ICLR 2024\n  year: 2024\n  arxiv: \"2307.01850\"\n  tags: [autophagous, sampling-bias, precision-recall, MAD]\n  relevance: indirect\n  cite_in: [introduction, related-work]\n  notes: >\n    Biased sampling keeps precision but kills recall. Unbiased causes mode drift.\n    tau=0.9 maps to their biased sampling regime.\n\ngerstgrasser2024_accumulate:\n  title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n  authors: [Gerstgrasser, Schaeffer, et al.]\n  venue: arXiv preprint\n  year: 2024\n  arxiv: \"2404.01413\"\n  tags: [model-collapse, data-accumulation, mitigation]\n  relevance: indirect\n  cite_in: [related-work, discussion]\n  notes: >\n    Data accumulation prevents collapse (bounded test error).\n    Important caveat: in accumulation regime, depth signal may be weaker.\n\ndrayson2025_detection_prevents_collapse:\n  title: \"Machine-generated text detection prevents language model collapse\"\n  authors: [Drayson et al.]\n  venue: EMNLP 2025 Findings\n  year: 2025\n  arxiv: \"2502.15654\"\n  tags: [temperature, diversity, recursive-training, detection]\n  relevance: direct\n  cite_in: [related-work]\n  notes: >\n    Temperature tau=0.9 produces most repetitive outputs; diversity drops ~70%\n    over 99 recursive generations (GPT-2, SmolLM2). Perplexity degradation more\n    moderate than deterministic methods. Detection as filter vs our depth estimation.\n\nbakshi2026_collapse_improvement:\n  title: \"From Collapse to Improvement: Statistical Perspectives on Iterative Training\"\n  authors: [Bakshi, Chakraborty]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2602.10531\"\n  tags: [model-collapse, non-monotonic, data-mixing]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Iterative training with fresh real data can *improve* performance.\n    Non-monotonic dynamics complicate simple depth-signal assumptions.\n\nwang2026_contamination:\n  title: \"Can Generative AI Survive Data Contamination? Theoretical Guarantees\"\n  authors: [Wang, Niu, Li]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2602.16065\"\n  tags: [model-collapse, contamination, theoretical]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Extends collapse theory beyond Gaussian/discrete to realistic distributions.\n    Provides theoretical grounding for depth signal existence.\n\nfalahati2026_curated:\n  title: \"Curated Synthetic Data Doesn't Have to Collapse\"\n  authors: [Falahati, Amiri, Larson, Golab]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2605.07724\"\n  tags: [curation, collapse-prevention, pluralistic]\n  relevance: indirect\n  cite_in: [discussion, limitations]\n  notes: >\n    Pluralistic curation prevents collapse. Harder case for our method —\n    curated pipelines may produce depth-invariant text.\n\nknowledge_collapse2025:\n  title: \"Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\"\n  authors: [Keisha, Wu, Wang, Koshiyama, Treleaven]\n  venue: arXiv preprint\n  year: 2025\n  arxiv: \"2509.04796\"\n  tags: [knowledge-collapse, fluency, factual-degradation]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Three-stage collapse: factual accuracy degrades while fluency persists.\n    Surface perplexity features still capture depth signal despite fluency preservation.\n\nsynthetic_eggs2026:\n  title: \"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\"\n  authors: [Schaffelder, Gatt]\n  venue: ACL 2026 Findings\n  year: 2026\n  arxiv: \"2511.01490\"\n  tags: [diversity, collapse-mitigation, Self-BLEU]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Multi-source synthetic data reduces collapse. Their diversity metrics\n    (Self-BLEU, lexical diversity) are candidate depth features.\n\nmohamed2025_broken_telephone:\n  title: \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"\n  authors: [Mohamed, Geng, Vazirgiannis, Shang]\n  venue: ACL 2025\n  year: 2025\n  arxiv: \"2502.20258\"\n  tags: [iterative-generation, information-distortion, translation-chain]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Iterative generation (translation/paraphrase chains) produces monotonically\n    increasing information distortion. Cross-task evidence that iterated signals\n    accumulate — supports our depth signal persistence finding.\n\nsigma2026_spectral:\n  title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n  authors: [\"(multiple)\"]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2601.03385\"\n  tags: [spectral-analysis, gram-matrix, representation-collapse, 50-generations]\n  relevance: direct\n  cite_in: [related-work, discussion]\n  notes: >\n    Gram matrix spectral analysis tracks representation space contraction over\n    50 recursive generations. Proposes Sigma-UB metric. Complementary to our\n    EDD — they measure geometric collapse, we measure statistical distinguishability.\n    Tests 50 generations but does NOT do inter-generation classification.\n\n# --- R2-N2 supplement: model collapse empirical ---\n\nshi2025_closer_look:\n  title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n  authors: [Shi, Wu, Zhang, Zhang, Tao, Qu]\n  venue: NeurIPS 2025 (Spotlight)\n  year: 2025\n  arxiv: \"2509.16499\"\n  tags: [model-collapse, entropy, memorization, intrinsic-dimension]\n  relevance: direct\n  role: background\n  verified: true\n  integration: \"整合，entropy ↔ depth signal 支撑特征选择论证\"\n  cite_in: [related-work, discussion]\n  notes: >\n    Identifies generalization-to-memorization transition during recursive training.\n    Entropy of training data decreases over iterations, strongly correlated with\n    model degradation. Entropy decline IS a measurable depth signal — directly\n    supports our statistical feature approach to depth estimation.\n\nyi2026_escaping_collapse:\n  title: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\n  authors: [Yi, Liu, Cheng, Xu]\n  venue: 3rd DATA-FM Workshop @ ICLR 2026\n  year: 2026\n  arxiv: \"2510.16657\"\n  tags: [model-collapse, verification, synthetic-data, mitigation]\n  relevance: indirect\n  role: background\n  verified: true\n  integration: \"引用但降级——related work 提一句，不支撑核心 claim（workshop paper）\"\n  cite_in: [related-work]\n  notes: >\n    Verifier-guided retraining prevents collapse. Our depth estimation\n    can serve AS the verifier — depth score enables graduated filtering\n    rather than binary accept/reject. NOTE: workshop paper, not main conference.\n\n# =============================================================\n# DECODING STRATEGIES\n# =============================================================\n\nholtzman2020_nucleus:\n  title: \"The Curious Case of Neural Text Degeneration\"\n  authors: [Holtzman, Buys, Du, Forbes, Choi]\n  venue: ICLR 2020\n  year: 2020\n  arxiv: \"1904.09751\"\n  tags: [nucleus-sampling, temperature, text-degeneration, unreliable-tail]\n  relevance: indirect\n  cite_in: [background, method]\n  notes: >\n    Proposes nucleus sampling. Temperature+top-k leads to repetition.\n    Key concept: unreliable tail of low-probability tokens.\n\nfinlayson2024_closing:\n  title: \"Closing the Curious Case of Neural Text Degeneration\"\n  authors: [Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal]\n  venue: ICLR 2024\n  year: 2024\n  arxiv: \"2310.01693\"\n  tags: [softmax-bottleneck, truncation-sampling, precise-sampling]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Truncation sampling eliminates softmax bottleneck errors. Mechanistic\n    difference between truncation and scaling approaches.\n\ngarces_arias2025_decoding_decoded:\n  title: \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\"\n  authors: [Garces Arias et al.]\n  venue: COLING 2025\n  year: 2025\n  tags: [decoding, hyperparameters, model-dependent]\n  relevance: direct\n  cite_in: [related-work, discussion]\n  notes: >\n    Confirms optimal decoding configuration is model-dependent.\n    Directly supports D006 finding (strategy effect is model-dependent).\n    Key external validation for our interaction effects claim.\n\nwiher2022_decoding:\n  title: \"On Decoding Strategies for Neural Text Generators\"\n  authors: [Wiher, Meister, Cotterell]\n  venue: TACL 2022\n  year: 2022\n  tags: [decoding, task-dependent, evaluation]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Decoding strategy effects are task-dependent.\n    Supports our finding that strategy effects on depth signal vary by model.\n\nbasu2021_mirostat:\n  title: \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\"\n  authors: [Basu, Sachdev, Kamdar, Nishi]\n  venue: ICLR 2021\n  year: 2021\n  tags: [perplexity-control, sampling, cross-entropy]\n  relevance: indirect\n  cite_in: [related-work, discussion]\n  notes: >\n    Perplexity and sampling parameters have non-linear relationship.\n    Relevant to p90_ppl capturing depth signal better than mean_ppl\n    under heavy-tailed distributions.\n\n# =============================================================\n# BINARY / ZERO-SHOT DETECTION\n# =============================================================\n\nmitchell2023_detectgpt:\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: [Mitchell, Lee, Khazatsky, Manning, Finn]\n  venue: ICML 2023\n  year: 2023\n  arxiv: \"2301.11305\"\n  tags: [zero-shot, detection, curvature, perturbation, binary]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Foundational zero-shot detector using log-probability curvature via\n    random perturbations. Binary only. Fast-DetectGPT improves efficiency.\n\nsadasivan2023_paraphrase:\n  title: \"Can AI-Generated Text be Reliably Detected?\"\n  authors: [Sadasivan, Kumar, Balasubramanian, Wang, Feizi]\n  venue: arXiv preprint\n  year: 2023\n  arxiv: \"2303.11156\"\n  tags: [detection-limits, paraphrase-attack, impossibility]\n  relevance: indirect\n  cite_in: [related-work, limitations]\n  notes: >\n    Shows paraphrase attacks evade all detectors; proves impossibility\n    result when model and human distributions overlap sufficiently.\n    Important limitation context for our depth estimation approach.\n\nbinoculars2024:\n  title: \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"\n  authors: [Hans, Schwarzschild, Manber, et al.]\n  venue: ICML 2024\n  year: 2024\n  arxiv: \"2401.12070\"\n  tags: [zero-shot, detection, perplexity-ratio, binary]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Two-model perplexity ratio for zero-shot binary detection.\n    We extend beyond binary to ordinal depth.\n\nfast_detectgpt2024:\n  title: \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\"\n  authors: [Bao et al.]\n  venue: ICLR 2024\n  year: 2024\n  arxiv: \"2310.05130\"\n  tags: [zero-shot, detection, curvature, binary]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Conditional probability curvature for efficient binary detection.\n    Cannot distinguish depth levels.\n\ndiveye2026:\n  title: \"DivEye: Diversity Boosts AI-Generated Text Detection\"\n  authors: [Basani, Chen]\n  venue: ICLR 2026 / TMLR\n  year: 2026\n  arxiv: \"2509.18880\"\n  tags: [surprisal-diversity, statistical-features, detection]\n  relevance: direct\n  cite_in: [related-work, method]\n  notes: >\n    Token-level surprisal diversity features for binary detection.\n    Feature overlap with our pipeline. We extend similar features\n    to ordinal depth regression.\n\nloki2025:\n  title: \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\"\n  authors: [Ye, Zhou, Huang, Zhang, Bai, Kang, He, Lin, Wang, Wu, Wu, Chen, Lin, He, Li]\n  venue: ICLR 2025 Spotlight\n  year: 2025\n  arxiv: \"2410.09732\"\n  tags: [benchmark, multimodal, detection]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Multimodal synthetic data detection benchmark. Binary only, no depth.\n\ngehrmann2019_gltr:\n  title: \"GLTR: Statistical Detection and Visualization of Generated Text\"\n  authors: [Gehrmann, Strobelt, Rush]\n  venue: ACL 2019\n  year: 2019\n  arxiv: \"1906.04043\"\n  tags: [detection, statistical-features, perplexity, rank, entropy]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Foundational statistical detection using log-likelihood, rank, entropy.\n    Our feature system extends this paradigm to recursive depth estimation.\n\npudasaini2026_detection_fails:\n  title: \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI\"\n  authors: [Pudasaini et al.]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2603.23146\"\n  tags: [detection-failure, distribution-shift, fragility]\n  relevance: indirect\n  cite_in: [limitations]\n  notes: >\n    Detection features degrade under distribution shift.\n    If binary features are domain-fragile, ordinal depth features may be too.\n\n# --- R2-N2 supplement: detection methods ---\n\ntulchinskii2024_intrinsic_dim:\n  title: \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\"\n  authors: [Tulchinskii, Kuznetsov, et al.]\n  venue: NeurIPS 2023\n  year: 2023\n  arxiv: \"2306.04723\"\n  tags: [intrinsic-dimension, geometric-features, detection, cross-domain]\n  relevance: direct\n  role: method-component\n  cite_in: [related-work, method]\n  notes: >\n    Intrinsic dimension of text embeddings ~9 for human, ~7.5 for AI-generated.\n    Geometric invariant enables cross-domain, cross-model robust detection.\n    Complementary feature family to our statistical perplexity features —\n    intrinsic dimension could serve as additional depth feature.\n\nverma2024_ghostbuster:\n  title: \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\"\n  authors: [Verma, Fleisig, Tomlin, Klein]\n  venue: NAACL 2024\n  year: 2024\n  arxiv: \"2305.15047\"\n  tags: [detection, structured-search, statistical-features, cross-domain]\n  relevance: indirect\n  role: direct-competitor\n  cite_in: [related-work]\n  notes: >\n    Structured search over combinations of weaker LM features for detection.\n    99.0 F1 cross-domain. Binary only. Feature engineering approach parallels\n    our multi-feature pipeline but targets binary classification, not ordinal depth.\n\nli2024_mage:\n  title: \"MAGE: Machine-generated Text Detection in the Wild\"\n  authors: [Li, Li, et al.]\n  venue: ACL 2024\n  year: 2024\n  arxiv: \"2305.13242\"\n  tags: [benchmark, cross-domain, cross-model, detection]\n  relevance: indirect\n  role: evaluation\n  cite_in: [related-work]\n  notes: >\n    Cross-domain cross-model detection benchmark. Finds significant OOD\n    performance degradation — same generalization challenge our cross-model\n    depth estimation faces. Binary detection only.\n\nwu2025_detection_survey:\n  title: \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\"\n  authors: [Wu, Yang, Zhan, Yuan, Chao, Wong]\n  venue: Computational Linguistics, Vol. 51, Issue 1\n  year: 2025\n  arxiv: \"2310.14724\"\n  tags: [survey, detection-taxonomy, watermarking, statistical, neural]\n  relevance: indirect\n  role: background\n  verified: true\n  integration: \"整合，survey 定位\"\n  cite_in: [related-work]\n  notes: >\n    Comprehensive survey of detection paradigms: watermarking, statistical,\n    neural, human-assisted. Positions our work as extending the statistical\n    paradigm from binary detection to ordinal depth estimation.\n\n# =============================================================\n# ADJACENT TASK — editing extent, attribution\n# =============================================================\n\neditlens2026:\n  title: \"EditLens: Quantifying the Extent of AI Editing in Text\"\n  authors: [Thai et al.]\n  venue: ICLR 2026\n  year: 2026\n  arxiv: \"2510.03154\"\n  tags: [editing-extent, continuous-score, mixed-authorship]\n  relevance: direct\n  cite_in: [introduction, related-work]\n  notes: >\n    Closest conceptual neighbor — both go beyond binary classification.\n    EditLens = single-pass editing extent; ours = multi-generation depth.\n\nuchendu2020_attribution:\n  title: \"Authorship Attribution for Neural Text Generation\"\n  authors: [Uchendu, Le, Shu, Lee]\n  venue: EMNLP 2020\n  year: 2020\n  tags: [attribution, multi-source, authorship]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Multi-source attribution (which model?). We solve a different axis\n    (how many iterations?) — complementary problems.\n\npu2026_generator_barrier:\n  title: \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\"\n  authors: [Pu, Cheng, Yuan, Wu, Bi]\n  venue: arXiv preprint\n  year: 2026\n  arxiv: \"2604.13692\"\n  tags: [disentanglement, cross-generator, generalization]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Cross-generator generalization via disentanglement.\n    Analogous to our cross-model generalization challenge.\n\n# --- R2-N2 supplement: attribution paradigms ---\n\nbevendorff2025_two_paradigms:\n  title: \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\"\n  authors: [Bevendorff, Wiegmann, Richter, Potthast, Stein]\n  venue: ACL 2025 Findings\n  year: 2025\n  tags: [attribution, verification, detection-paradigm, authorship]\n  relevance: direct\n  role: background\n  verified: true\n  integration: \"整合，'第三范式' framing（attribution/verification 之外的正交第三维度）\"\n  cite_in: [related-work]\n  notes: >\n    Reframes LLM detection as authorship verification (not attribution).\n    Our depth estimation is a third paradigm — ordinal characterization\n    beyond binary verification or multi-class attribution. Key framing\n    reference for positioning our contribution.\n\n# =============================================================\n# METHOD COMPONENT — ordinal classification\n# =============================================================\n\ncoral2020:\n  title: \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\"\n  authors: [Cao, Mirjalili, Raschka]\n  venue: Pattern Recognition Letters\n  year: 2020\n  arxiv: \"1901.07884\"\n  tags: [ordinal-classification, rank-consistency, cumulative-logits]\n  relevance: direct\n  cite_in: [method, experiments]\n  notes: >\n    CORAL ordinal classification framework used in our baseline battery.\n    Rank-consistent cumulative logits for ordinal targets.\n\ncloc2025:\n  title: \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\"\n  authors: [Pitawela, Carneiro, et al.]\n  venue: CVPR 2025\n  year: 2025\n  arxiv: \"2504.17813\"\n  tags: [contrastive-learning, ordinal, multi-margin, N-pair]\n  relevance: direct\n  cite_in: [method, dcol-section]\n  notes: >\n    DCOL is our adaptation of CLOC to text depth estimation.\n    Multi-margin N-pair loss for ordinal-aware contrastive learning.\n    Must cite as methodological basis for DCOL section.\n\n# =============================================================\n# WATERMARKING\n# =============================================================\n\nkirchenbauer2023_watermark:\n  title: \"A Watermark for Large Language Models\"\n  authors: [Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein]\n  venue: ICML 2023\n  year: 2023\n  arxiv: \"2301.10226\"\n  tags: [watermarking, proactive-detection, green-list]\n  relevance: indirect\n  cite_in: [related-work]\n  notes: >\n    Proactive detection via watermarking. Complementary —\n    watermarking requires generator cooperation; our method is post-hoc.\n\n# =============================================================\n# DATA CURATION\n# =============================================================\n\ndsir2023:\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: [Xie, Santurkar, Ma, Liang]\n  venue: NeurIPS 2023\n  year: 2023\n  arxiv: \"2302.03169\"\n  tags: [data-selection, importance-resampling, curation]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    Quality-based data selection for LM training.\n    Our depth estimation enables depth-graduated curation (Claim 3 / Discussion).\n\nqurating2024:\n  title: \"QuRating: Selecting High-Quality Data for Training Language Models\"\n  authors: [Wettig, Gupta, et al.]\n  venue: ICML 2024\n  year: 2024\n  arxiv: \"2402.09739\"\n  tags: [quality-rating, data-curation, LLM-judgments]\n  relevance: indirect\n  cite_in: [discussion]\n  notes: >\n    LLM-based quality rating for data selection.\n    Our depth score is a complementary quality axis.\n\n# --- R2-N2 supplement: data curation at scale ---\n\npenedo2024_fineweb:\n  title: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\n  authors: [Penedo, Kydlicek, et al.]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv: \"2406.17557\"\n  tags: [data-curation, quality-filtering, deduplication, web-scale]\n  relevance: indirect\n  role: background\n  cite_in: [discussion]\n  notes: >\n    15T token dataset with systematic quality filtering pipeline (dedup,\n    heuristic filters, classifier-based selection). Our depth estimation\n    adds a synthetic contamination axis complementary to FineWeb-style\n    quality curation — depth score can flag recursively degraded text\n    that passes standard quality filters.\n\n# =============================================================\n# COVARIATE SHIFT — technical background\n# =============================================================\n\nsugiyama2007_importance_weighting:\n  title: \"Covariate Shift Adaptation by Importance Weighted Cross Validation\"\n  authors: [Sugiyama, Krauledat, Mueller]\n  venue: JMLR\n  year: 2007\n  tags: [covariate-shift, importance-weighting, domain-adaptation]\n  relevance: background\n  cite_in: [discussion]\n  notes: >\n    Theoretical foundation for covariate shift correction.\n    Our z-score normalization is a simplified distribution alignment.\n\n# =============================================================\n# COVERAGE CHECKLIST (paper_framing.md Dream D002 requirements)\n# =============================================================\n# [x] watermarking: kirchenbauer2023_watermark\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\n#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate\n# [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,\n#     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)\n# [x] data curation: dsir2023, qurating2024, penedo2024_fineweb (NEW)\n# [x] multi-source attribution: uchendu2020_attribution,\n#     bevendorff2025_two_paradigms (VERIFIED)\n# [x] binary detectors: mitchell2023_detectgpt, sadasivan2023_paraphrase,\n#     binoculars2024, fast_detectgpt2024, diveye2026, loki2025,\n#     tulchinskii2024_intrinsic_dim (NEW), verma2024_ghostbuster (NEW),\n#     li2024_mage (NEW)\n# [x] detection survey: wu2025_detection_survey (VERIFIED)\n# [x] decoding strategy effects: garces_arias2025, holtzman2020_nucleus,\n#     wiher2022_decoding, basu2021_mirostat, finlayson2024_closing\n# [x] ordinal classification: coral2020, cloc2025\n# [x] adjacent tasks: editlens2026\n# [x] covariate shift: sugiyama2007\n# [x] statistical detection foundation: gehrmann2019_gltr\n#\n# Total unique entries: 43 (35 original + 8 R2-N2 supplement)\n# 2024-2026 papers: 30/43 (70% recent coverage)\n# Direct relevance: 12 entries\n",
    "structuredPatch": [
      {
        "oldStart": 670,
        "oldLines": 7,
        "newStart": 670,
        "newLines": 7,
        "lines": [
          " # =============================================================",
          " # [x] watermarking: kirchenbauer2023_watermark",
          " # [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,",
          "-#     dohmatob2024_tale_of_tails, dohmatob2024_strong_collapse,",
          "+#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,",
          " #     dohmatob2024_demystified, gerstgrasser2024_accumulate",
          " # [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,",
          " #     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)"
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

_source line 59_

全部完成。产出报告：

---

### 1. Discussion 段落修改

**修改前**（核心句）：
> "The 70–85% in-distribution accuracy and EDD₀.₇₅=4 suggest depth-graduated filtering is feasible… The downstream effect on training quality remains to be validated empirically."

**修改后**（核心新增）：
- 新增 PoC 实验描述：Pythia-410M LoRA (r=16), 3 epochs, 8 conditions, 5 seeds
- RF vs random 显著性：strict 25% Δ=0.43 PPL p=0.002; moderate 50% Δ=0.24 p=0.02
- Data efficiency：rf_soft 用 44% 数据达到与 unfiltered 不可区分的 PPL (p=0.41)
- Oracle 悖论：oracle-strict 不优于 unfiltered (p=0.22)，classifier imprecision 保留了数据多样性
- 引用 Appendix Table (`\ref{app:curation_poc}`)
- 未 claim RF improves over unfiltered，未用 "significantly" 描述 RF vs unfiltered

### 2. Appendix 新增内容

`section_appendix.tex` 中 Extended Discussion 之前插入 `\subsection{Downstream Curation PoC}` (`\label{app:curation_poc}`)：
- **Table 1** (`tab:curation_poc`)：8 条件完整表（Mean PPL / Std / n / Δ / p / Cohen's d）
- **Table 2** (`tab:curation_comparisons`)：3 组 pairwise 对比（rf vs random strict/moderate, rf_soft vs unfiltered）

### 3. dohmatob bib 修正

确认 arXiv 2410.04840 发表于 **ICLR 2025**（非 2024）。修改：
- `references.bib`：key `dohmatob2024_strong_collapse` → `dohmatob2025_strong_collapse`，year 2024 → 2025
- `related_work.tex`：`\citet{dohmatob2024_strong_collapse}` → `\citet{dohmatob2025_strong_collapse}`
- `literature_map.yaml`：key 和 year 同步更新

### 4. artifacts bib 同步

`artifacts/_project/paper/references.bib` 已用 `docs/paper/references.bib` 覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "uuid": "e53ada1e-f1c7-45b8-83c8-6ef82a5985b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTzcNGE1r94sWBbWe8EvLY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 63969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 249
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

_source line 60_

全部完成。产出报告：

---

### 1. Discussion 段落修改

**修改前**（核心句）：
> "The 70–85% in-distribution accuracy and EDD₀.₇₅=4 suggest depth-graduated filtering is feasible… The downstream effect on training quality remains to be validated empirically."

**修改后**（核心新增）：
- 新增 PoC 实验描述：Pythia-410M LoRA (r=16), 3 epochs, 8 conditions, 5 seeds
- RF vs random 显著性：strict 25% Δ=0.43 PPL p=0.002; moderate 50% Δ=0.24 p=0.02
- Data efficiency：rf_soft 用 44% 数据达到与 unfiltered 不可区分的 PPL (p=0.41)
- Oracle 悖论：oracle-strict 不优于 unfiltered (p=0.22)，classifier imprecision 保留了数据多样性
- 引用 Appendix Table (`\ref{app:curation_poc}`)
- 未 claim RF improves over unfiltered，未用 "significantly" 描述 RF vs unfiltered

### 2. Appendix 新增内容

`section_appendix.tex` 中 Extended Discussion 之前插入 `\subsection{Downstream Curation PoC}` (`\label{app:curation_poc}`)：
- **Table 1** (`tab:curation_poc`)：8 条件完整表（Mean PPL / Std / n / Δ / p / Cohen's d）
- **Table 2** (`tab:curation_comparisons`)：3 组 pairwise 对比（rf vs random strict/moderate, rf_soft vs unfiltered）

### 3. dohmatob bib 修正

确认 arXiv 2410.04840 发表于 **ICLR 2025**（非 2024）。修改：
- `references.bib`：key `dohmatob2024_strong_collapse` → `dohmatob2025_strong_collapse`，year 2024 → 2025
- `related_work.tex`：`\citet{dohmatob2024_strong_collapse}` → `\citet{dohmatob2025_strong_collapse}`
- `literature_map.yaml`：key 和 year 同步更新

### 4. artifacts bib 同步

`artifacts/_project/paper/references.bib` 已用 `docs/paper/references.bib` 覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 160579,
  "duration_api_ms": 167327,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "cf247e1a-27ec-416b-9e6c-ce6c421c5394",
  "total_cost_usd": 0.9394607500000001,
  "usage": {
    "input_tokens": 6459,
    "cache_creation_input_tokens": 52377,
    "cache_read_input_tokens": 651255,
    "output_tokens": 8851,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52377,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 670,
        "cache_read_input_tokens": 63969,
        "cache_creation_input_tokens": 249,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 249
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 20537,
      "outputTokens": 474,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 1,
      "costUSD": 0.032907,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6459,
      "outputTokens": 8851,
      "cacheReadInputTokens": 651255,
      "cacheCreationInputTokens": 52377,
      "webSearchRequests": 0,
      "costUSD": 0.90655375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9d8c1c26-c8cc-469d-aa7c-7fcebbbca4f6"
}
```

</details>

---
