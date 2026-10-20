# Research conversation: 任务：提交前收尾（3 个子任务） 项目路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/ ### 

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aafc02ba1e0612e58.jsonl`
- **Structured JSON:** [`faeae3a710cc8433b87d.json`](../../sessions/fa/faeae3a710cc8433b87d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-20T01:47:28.869Z_

## 任务：提交前收尾（3 个子任务）

项目路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/

### 任务 1: Appendix TOC 更新
读取 main.tex，找到 Appendix Overview 导航栏（大约 L52-70 附近），在 R 条目后面加入：
```
\hyperref[app:extended-validation]{S.~Extended Validation}
```

### 任务 2: 全文 typo/grammar scan
读取以下文件，快速扫描明显 typo、语法错误、格式不一致：
- abstract.tex
- introduction.tex
- conclusion.tex
- discussion.tex

列出发现的问题（如有），并修复。

### 任务 3: 编译验证
在 docs/paper/ 目录运行 pdflatex + bibtex 编译流程，确认无新 warning（除了已知的 harmless warnings）。

编译命令（在 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/ 下）：
```bash
cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

检查输出中的 Warning 和 Error（忽略已知的 font/overfull hbox warnings）。

### 输出
汇总报告：
1. Appendix TOC 修改了什么
2. typo scan 发现了什么（列表）
3. 编译结果（errors/warnings 数量）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "4d347cd6-7a7d-4555-b22c-03008f18deda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T01:47:28.874Z_

```json
{
  "parentUuid": "4d347cd6-7a7d-4555-b22c-03008f18deda",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b8cc9239-3bf2-4685-932b-bfcf4cfbe467",
  "timestamp": "2026-05-20T01:47:28.874Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

---

### Tool call

_source line 3 · 2026-05-20T01:47:32.336Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CMWMrj9eFxrqxZDMXHgtM3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8cc9239-3bf2-4685-932b-bfcf4cfbe467",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCygopxZRNrHCb1hVwHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8075e201-a8ce-49a0-a897-b77f6d5c207c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776WDvwkAmLoJUoFVYP8Vb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29067,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T01:47:32.696Z_

<details><summary>↩ Tool result · `toolu_01CMWMrj9eFxrqxZDMXHgtM3`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
37	
38	\paragraph{Methodological constraints.}
39	Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}. Reflexion~\citep{reflexion-2023} reduces death rate from 42.9\% to 31.4\% (\S\ref{sec:agent-improvement}), but more aggressive self-correction or Tree-of-Thought backtracking~\citep{tot-2023} may further reduce internal death rates. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events). However, of 2{,}040 training steps only 0.3\% exhibit strict directional conflict (step-level oracle opposite to episode label); the remaining apparent mislabeling consists of episode labels applied to steps where neither strategy has a step-level advantage (60.3\% pre-event neutral). The issue is granularity mismatch---applying correct-direction labels to uninformative steps---not directional error. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}. Under mixed-strategy routing with oracle death prediction, switching to deterministic at the step before death could reduce the internal death rate; even under optimistic assumptions (perfect step-level death prediction), a residual gap of ${>}10$~pp between strategies is expected, as fatal trajectories involve cumulative hallucination errors preceding the death event. More broadly, projecting episode-level labels onto 10--50 sequential steps with path-dependent state introduces compounding error: early routing decisions alter the state trajectory, potentially invalidating later labels derived from the episode outcome.
40	
41	\paragraph{Statistical limitations.}
42	Episodes within the same task type are not fully independent because they share environment dynamics, though they use different random seeds. Cluster bootstrap with $K{=}11$ task-type clusters yields wider CIs ($[73.0\%, 100\%]$); with $K < 40$ clusters, these should be interpreted cautiously~\citep{cameron-2008,webb-2023}. A wild cluster bootstrap ($K{=}11$, $p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks (Appendix~\ref{app:per-task-ci}) mitigate this concern.
43	
44	\section*{Ethics Statement}
45	
46	This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours for data collection, router training, and evaluation. Code and data will be released upon acceptance.
47	
48	\bibliography{references}
49	
50	\appendix
51	
52	\noindent\textbf{Appendix Overview.}
53	\hyperref[app:sci]{A.~Signal Concentration Index} $\cdot$
54	\hyperref[app:labeling]{B.~Labeling Quality Audit} $\cdot$
55	\hyperref[app:per-task]{C.~Per-Task Decomposition} $\cdot$
56	\hyperref[app:correlation]{D.~Correlation Robustness} $\cdot$
57	\hyperref[app:wild-cluster]{E.~Wild Cluster Bootstrap} $\cdot$
58	\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\cdot$
59	\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\cdot$
60	\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\cdot$
61	\hyperref[app:router-details]{I.~Router Training Details} $\cdot$
62	\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
63	\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
64	\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
65	\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
66	\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
67	\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
68	\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
69	\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\cdot$
70	\hyperref[app:decision-framework]{R.~Decision Framework}
71	
72	\section{Signal Concentration Index}
73	\label{app:sci}
74	
75	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
76	\begin{equation}
77	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
78	\end{equation}
79	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
80	\begin{equation}
81	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
82	\end{equation}
83	
84	\section{Labeling Quality Audit}
85	\label{app:labeling}
86	
87	\begin{algorithm}[t]
88	\caption{Episode-Level Counterfactual Labeling}
89	\label{alg:labeling}
90	\begin{algorithmic}[1]
91	\REQUIRE Task instance $t$, modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$
92	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
93	\FOR{each $m \in \mathcal{M}$}
94	    \STATE Run episode $\tau_m$ with pure-strategy $m$
95	    \STATE Record score $s_m$ and death indicator $d_m$
96	\ENDFOR
97	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
98	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
99	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
100	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
101	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
102	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
103	\ELSIF{$s_{\tt det} > s_{\tt int}$}
104	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
105	\ELSIF{$s_{\tt int} > s_{\tt det}$}
106	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
107	\ELSE
108	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
109	\ENDIF
110	\RETURN $\ell$
111	\end{algorithmic}
112	\end{algorithm}
113	
114	A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
115	
116	\section{Per-Task Decomposition}
117	\label{app:per-task}
118	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
119	
120	\begin{table}[h]
121	\centering
122	\scriptsize
123	\setlength{\tabcolsep}{2.5pt}
124	\begin{tabular}{@{}lrrccc@{}}
125	\toprule
126	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
127	\midrule
128	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
129	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
130	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
131	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
132	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
133	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
134	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
135	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
136	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
137	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
138	\midrule
139	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
140	\midrule
141	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
142	\bottomrule
143	\end{tabular}
144	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
145	\label{tab:per-task}
146	\end{table}
147	
148	\paragraph{Task selection and anti-cherry-picking.}
149	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
150	
151	\begin{table}[t]
152	\centering
153	\scriptsize
154	\setlength{\tabcolsep}{2pt}
155	\begin{tabular}{@{}llrcccl@{}}
156	\toprule
157	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
158	\midrule
159	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
160	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
161	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
162	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
163	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
164	\midrule
165	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
166	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
167	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
168	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
169	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
170	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
171	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
172	\midrule
173	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
174	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
175	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
176	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
177	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
178	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
179	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
180	\midrule
181	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
182	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
183	\bottomrule
184	\end{tabular}
185	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
186	\label{tab:excluded-death}
187	\end{table}
188	
189	\section{Correlation Robustness}
190	\label{app:correlation}
191	
192	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
193	
194	\begin{table}[h]
195	\centering
196	\small
197	\begin{tabular}{@{}lr@{}}
198	\toprule
199	Task removed & $r_{\text{LOO}}$ \\
200	\midrule
201	id-life-stages-1       & 0.963 \\
202	lifespan-long          & 0.969 \\
203	lifespan-l-then-s      & 0.976 \\
204	inclined-plane         & 0.969 \\
205	freeze                 & 0.971 \\
206	meas-melt-point        & 0.972 \\
207	id-life-stages-2       & 0.972 \\
208	find-animal            & 0.970 \\
209	grow-fruit             & 0.973 \\
210	chem-mix               & 0.969 \\
211	find-non-living-thing  & 0.980 \\
212	\bottomrule
213	\end{tabular}
214	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
215	\label{tab:loo}
216	\end{table}
217	
218	\section{Wild Cluster Bootstrap}
219	\label{app:wild-cluster}
220	
221	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
222	
223	\begin{table}[h]
224	\centering
225	\small
226	\begin{tabular}{@{}lcc@{}}
227	\toprule
228	Method & $p$-value & 95\% CI \\
229	\midrule
230	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
231	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
232	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
233	Sign test & $< 0.001$ & --- \\
234	\bottomrule
235	\end{tabular}
236	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
237	\label{tab:wild-cluster}
238	\end{table}
239	
240	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. The $K{=}11$ analysis uses the same clusters as the main analysis, providing a direct robustness check on the primary results.
241	
242	\section{Per-Task Death Rate Confidence Intervals}
243	\label{app:per-task-ci}
244	
245	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
246	
247	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
248	
249	\section{Leave-One-Task-Out DAF Sensitivity}
250	\label{app:loto-daf}
251	
252	\begin{table}[h]
253	\centering
254	\small
255	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
256	\label{tab:loto-daf}
257	\begin{tabular}{lrrr}
258	\toprule
259	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
260	\midrule
261	(none, full) & 245 & 78.9 & --- \\
262	\midrule
263	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
264	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
265	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
266	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
267	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
268	Grow Fruit & 225 & 77.3 & $-$1.7 \\
269	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
270	Freeze & 225 & 77.5 & $-$1.4 \\
271	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
272	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
273	Find Animal & 225 & 77.8 & $-$1.2 \\
274	\bottomrule
275	\end{tabular}
276	
277	\vspace{2pt}
278	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
279	\end{table}
280	
281	\section{Per-Task Dose-Response Breakdown}
282	\label{app:dose-response}
283	
284	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the plateau conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
285	
286	\begin{table}[h]
287	\centering
288	\small
289	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm the plateau at $N \geq 3$ (range: $34.0$--$36.5\%$).}
290	\label{tab:dose-response-detail}
291	\begin{tabular}{@{}lrrr@{}}
292	\toprule
293	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
294	\midrule
295	chemistry-mix & 25.0 & 35.0 & 20.0 \\
296	find-animal & 45.0 & 30.0 & 45.0 \\
297	freeze & 50.0 & 50.0 & 60.0 \\
298	grow-fruit & 30.0 & 25.0 & 25.0 \\
299	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
300	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
301	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
302	lifespan-longest & 45.0 & 40.0 & 40.0 \\
303	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
304	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
305	\midrule
306	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	\section{Router Training Details}
312	\label{app:router-details}
313	
314	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
315	
316	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
317	
318	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
319	
320	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Augmentation-based data scaling (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
321	
322	\begin{table}[h]
323	\centering
324	\small
325	\resizebox{\columnwidth}{!}{%
326	\begin{tabular}{@{}lcc@{}}
327	\toprule
328	Hyperparameter & Classification Head & Implicit Router \\
329	\midrule
330	Base model & Qwen3-1.7B & Qwen3-1.7B \\
331	Architecture & Linear + LoRA & SFT + LoRA \\
332	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
333	Learning rate & 2e-5 & 2e-4 \\
334	Optimizer & AdamW & AdamW \\
335	Epochs & 3 & 3 \\
336	Batch size (per device) & 4 & 4 \\
337	Gradient accumulation & 8 & 8 \\
338	Warmup ratio & 0.1 & 0.1 \\
339	Weight decay & 0.01 & 0.01 \\
340	Max sequence length & 512 & 512 \\
341	Seeds & \{42\} & \{42, 123, 456, 789\} \\
342	\bottomrule
343	\end{tabular}}
344	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
345	\label{tab:hyperparams}
346	\end{table}
347	
348	\section{Seed Robustness}
349	\label{app:seed-robustness}
350	
351	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
352	
353	\begin{table}[h]
354	\centering
355	\small
356	\begin{tabular}{@{}llcc@{}}
357	\toprule
358	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
359	\midrule
360	Step-level & 42 & 57.06 \\
361	(same-episode & 43 & 63.99 \\
362	leakage) & 44 & 55.43 \\
363	 & 45 & 56.14 \\
364	 & 46 & 55.45 \\
365	 & 47 & 50.08 \\
366	 & 48 & 48.03 \\
367	 & 49 & 59.30 \\
368	\cmidrule{2-3}
369	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
370	\midrule
371	Episode-level & 42 & 48.1 \\
372	(held-out & 43 & 47.9 \\
373	episodes) & 44 & 49.6 \\
374	 & 45 & 49.4 \\
375	 & 46 & 48.5 \\
376	 & 47 & 43.1 \\
377	 & 48 & 45.4 \\
378	 & 49 & 44.8 \\
379	\cmidrule{2-3}
380	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
381	\midrule
382	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
383	\bottomrule
384	\end{tabular}
385	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A data scaling ablation (Table~\ref{tab:data-scaling}) confirms this failure persists under the current data distribution and augmentation regime.}
386	\label{tab:seed-robustness}
387	\end{table}
388	
389	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Augmentation-based data scaling (Table~\ref{tab:data-scaling}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). However, paraphrase augmentation inflates the majority class without generating novel routing patterns; real-data scaling remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving no learnable signal for a step-level router.
390	
391	\paragraph{Data scaling ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based data augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. Table~\ref{tab:data-scaling} reports the results.
392	
393	\begin{table}[h]
394	\centering
395	\small
396	\begin{tabular}{@{}rccc@{}}
397	\toprule
398	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
399	\midrule
400	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
401	50\% & 867 & ${\sim}90$ & $51.5$ \\
402	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
403	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
404	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
405	\midrule
406	Always-det & --- & --- & 50.0 \\
407	\bottomrule
408	\end{tabular}
409	\caption{Data scaling ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
410	\label{tab:data-scaling}
411	\end{table}
412	
413	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, leaving no learnable signal for a step-level router to exploit.
414	
415	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
416	
417	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.1\%, 99.0\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
418	
419	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the data scaling ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
420	
421	\section{Penalty Sensitivity Analysis}
422	\label{app:penalty}
423	
424	\begin{table}[h]
425	\centering
426	\small
427	\begin{tabular}{@{}rrr@{}}
428	\toprule
429	$P$ & DAF($P$) & 95\% CI \\
430	\midrule
431	0 & 7.4\% & [$-39.4$, $82.5$] \\
432	1 & 14.8\% & [$-28.6$, $89.6$] \\
433	5 & 35.4\% & [$-1.8$, $92.7$] \\
434	10 & 50.4\% & [$18.5$, $93.3$] \\
435	25 & 70.7\% & [$48.0$, $96.3$] \\
436	50 & 82.6\% & [$67.2$, $98.2$] \\
437	100\textsuperscript{*} & 90.4\% & [$81.1$, $99.0$] \\
438	200 & 94.9\% & [$89.9$, $99.5$] \\
439	500 & 97.9\% & [$95.7$, $99.8$] \\
440	\bottomrule
441	\end{tabular}
442	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
443	\label{tab:penalty-sensitivity}
444	\end{table}
445	
446	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
447	
448	\paragraph{Mechanism boundary: death specificity.}
449	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
450	
451	\begin{table}[h]
452	\centering
453	\small
454	\begin{tabular}{@{}rccl@{}}
455	\toprule
456	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
457	\midrule
458	1 & $-0.44$ & $0.178$ & No \\
459	5 & $-0.29$ & $0.382$ & No \\
460	10 & $-0.08$ & $0.813$ & No \\
461	25 & $0.51$ & $0.108$ & No \\
462	50 & $0.86$ & $0.0006$ & Yes \\
463	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
464	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
465	\bottomrule
466	\end{tabular}
467	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
468	\label{tab:penalty-correlation}
469	\end{table}
470	
471	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
472	
473	\section{Cross-Environment Details}
474	\label{app:cross-env-details}
475	
476	Figure~\ref{fig:signal-reversal} and Table~\ref{tab:cross-env} summarize the label distributions across all three environments.
477	
478	\begin{figure}[h]
479	\centering
480	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
481	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both show deterministic preference, but through different mechanisms: death avoidance (ScienceWorld) vs.\ information asymmetry from admissible-action access (ALFWorld). MATH shows balanced labels, confirming no routing signal without catastrophic failure.}
482	\label{fig:signal-reversal}
483	\end{figure}
484	
485	\begin{table}[h]
486	\centering
487	\small
488	\resizebox{\columnwidth}{!}{%
489	\begin{tabular}{@{}lccccc@{}}
490	\toprule
491	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
492	\midrule
493	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
494	MATH & 795 & 12.0 & 13.5 & 74.6 & No \\
495	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
496	\bottomrule
497	\end{tabular}}
498	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
499	\label{tab:cross-env}
500	\end{table}
501	
502	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
503	
504	\begin{table}[h]
505	\centering
506	\scriptsize
507	\setlength{\tabcolsep}{2.5pt}
508	\begin{tabular}{@{}lrcccc@{}}
509	\toprule
510	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
511	\midrule
512	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
513	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
514	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
515	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
516	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
517	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
518	\midrule
519	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
520	\bottomrule
521	\end{tabular}
522	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
523	\label{tab:alfworld-pertask}
524	\end{table}
525	
526	\section{Cross-Model Verification}
527	\label{app:cross-model}
528	
529	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
530	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
531	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
532	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
533	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
534	
535	\begin{table}[h]
536	\centering
537	\small
538	\begin{tabular}{@{}lrrrl@{}}
539	\toprule
540	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
541	\midrule
542	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
543	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
544	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
545	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
546	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
547	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
548	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
549	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
550	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
551	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
552	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
553	\midrule
554	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
555	\bottomrule
556	\end{tabular}
557	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
558	\label{tab:cross-model-detail}
559	\end{table}
560	
561	\section{Failure Mode Analysis}
562	\label{app:failure-modes}
563	
564	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
565	
566	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
567	\label{tab:death-taxonomy}
568	
569	\paragraph{Representative examples.}
570	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
571	
572	\paragraph{Action distribution analysis.}
573	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
574	
575	\begin{figure}[h]
576	\centering
577	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
578	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
579	\label{fig:death-action-dist}
580	\end{figure}
581	
582	\begin{figure}[h]
583	\centering
584	\includegraphics[width=\columnwidth]{figures/death_action_timeline.pdf}
585	\caption{Step-by-step action sequences for 6 representative death episodes. The fatal \texttt{focus on} action (marked with arrow) consistently appears in the final steps after long \texttt{connect} sequences, and illustrates the ``connect loop $\to$ fatal focus'' pattern. Examples are drawn from the full 30-task dataset for task-type diversity; the pattern is identical in the 11-task analysis subset.}
586	\label{fig:death-timeline}
587	\end{figure}
588	
589	\begin{figure}[h]
590	\centering
591	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
592	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
593	\label{fig:death-comparison}
594	\end{figure}
595	
596	\section{Grounding Ablation}
597	\label{app:grounding-ablation}
598	
599	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
600	
601	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
602	
603	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
604	
605	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
606	
607	\section{Ablation Studies}
608	\label{app:ablations}
609	
610	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
611	
612	\begin{table}[h]
613	\centering
614	\small
615	\begin{tabular}{@{}lcc@{}}
616	\toprule
617	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
618	\midrule
619	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
620	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
621	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
622	\midrule
623	Always-det & 50.0 & 50.0 \\
624	\bottomrule
625	\end{tabular}
626	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
627	\label{tab:capacity}
628	\end{table}
629	
630	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
631	
632	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
633	
634	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal.
635	
636	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
637	
638	\section{Threshold Routing Analysis}
639	\label{sec:threshold-routing}
640	
641	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
642	
643	\begin{table}[h]
644	\centering
645	\small
646	\begin{tabular}{lccc}
647	\toprule
648	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
649	\midrule
650	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
651	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
652	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
653	\bottomrule
654	\end{tabular}
655	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
656	\label{tab:threshold-routing}
657	\end{table}
658	
659	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
660	
661	\section{Practitioner Decision Framework}
662	\label{app:decision-framework}
663	
664	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
665	
666	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
667	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
668	
669	\paragraph{Stage 2: Death dominance check.}
670	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
671	
672	\paragraph{Stage 3: Decision.}
673	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
674	
675	\paragraph{Retrospective validation.}
676	All four experimental conditions in this paper are correctly classified:
677	
678	\begin{table}[h]
679	\centering
680	\small
681	\begin{tabular}{@{}lrrll@{}}
682	\toprule
683	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
684	\midrule
685	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
686	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
687	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
688	MATH & +0.5 & 0\% & router viable & no signal \\
689	\bottomrule
690	\end{tabular}
691	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
692	\label{tab:decision-framework}
693	\end{table}
694	
695	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
696	
697	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from a single-environment analysis. Practitioners should calibrate these boundaries for their specific environment and reward structure.
698	
699	\section{Extended Validation of Excluded Tasks}
700	\label{app:extended-validation}
701	
702	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
703	
704	\begin{table}[h]
705	\centering
706	\small
707	\begin{tabular}{lcrrrrc}
708	\toprule
709	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
710	\midrule
711	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
712	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
713	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
714	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
715	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
716	\midrule
717	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
718	\bottomrule
719	\end{tabular}
720	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
721	\label{tab:extended-val}
722	\end{table}
723	
724	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
725	
726	\input{responsibleNLPchecklist}
727	
728	\end{document}
729	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8075e201-a8ce-49a0-a897-b77f6d5c207c",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "b4c673fc-2d7c-4df5-8b8d-90aa61bafc27",
  "sourceToolAssistantUUID": "8075e201-a8ce-49a0-a897-b77f6d5c207c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T01:47:32.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FNXX8iKcbcFrAnsGLXMbAW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4c673fc-2d7c-4df5-8b8d-90aa61bafc27",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCygopxZRNrHCb1hVwHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3fa949f-1aee-4db0-b2bb-17b0212a7230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776WDvwkAmLoJUoFVYP8Vb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29067,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T01:47:32.848Z_

<details><summary>↩ Tool result · `toolu_01FNXX8iKcbcFrAnsGLXMbAW`</summary>

```text
1	\begin{abstract}
2	Per-step oracle comparison degenerates under sparse rewards---in ScienceWorld, 97.4\% of steps yield identical scores regardless of computation mode. We introduce an episode-level counterfactual diagnostic framework that overcomes this degeneracy by decomposing routing signal into death-avoidance and non-death components via paired pure-strategy episodes. Applying this framework to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), we find that \textbf{78.9\% of non-tie routing labels} stem from death asymmetry---a penalty-independent result; a derived measure, the Death Avoidance Factor (DAF), reaches 90.4\% at $P{=}100$. Cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), four intervention axes (retry, self-correction, $10{\times}$ scaling, action-space restriction), and boundary probes against contrasting environments (MATH, ALFWorld) confirm the framework's diagnostic utility and the robustness of this finding. A three-stage diagnostic pilot (${\sim}$50 episodes) correctly predicts routing outcomes across all four tested conditions, demonstrating practical utility before any router is trained.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3fa949f-1aee-4db0-b2bb-17b0212a7230",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "83544b1a-61d5-4d87-a8c0-9b46d5469c6e",
  "sourceToolAssistantUUID": "e3fa949f-1aee-4db0-b2bb-17b0212a7230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T01:47:33.335Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MzAi2GvQZejHmteH6QAuHC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83544b1a-61d5-4d87-a8c0-9b46d5469c6e",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCygopxZRNrHCb1hVwHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbc3addf-ec7a-4180-9b99-9ef14e89d508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776WDvwkAmLoJUoFVYP8Vb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29067,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T01:47:33.346Z_

<details><summary>↩ Tool result · `toolu_01MzAi2GvQZejHmteH6QAuHC`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \cite{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone---the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated)---while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \cite{toolformer-2023} inserts API calls by perplexity reduction; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---has not been tested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.1\%, 99.0\%]$). The internal strategy's hallucination-induced failures trigger catastrophic death ($-100$ penalty); once death episodes are removed, the gap collapses to $\Delta_{\text{nd}} = +2.84$ (\S\ref{sec:death-decomp}).
9	
10	This addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\% tie rate; \S\ref{sec:collection}), and keyword-based heuristics fail structurally (\S\ref{sec:baselines}). Our approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, comparing episode outcomes.
11	
12	Cross-context checks probe specificity: MATH Level~4--5 ($N{=}795$, code interpreter) shows no routing signal without catastrophic failure ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$); Llama-3.1-8B replication ($N{=}220$) confirms death dominance across model families (direction consistency 10/10; \S\ref{sec:cross-model}). Four intervention axes (retry, Reflexion~\citep{reflexion-2023}, $10{\times}$ scaling, action-space restriction) reduce death rates but none closes the gap to deterministic safety, with ${\geq}$12~pp residual gaps (\S\ref{sec:agent-improvement}).
13	An exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline (\S\ref{sec:router-diagnostic}).
14	
15	Our contributions: (1)~an \textbf{episode-level counterfactual diagnostic framework} that overcomes per-step oracle degeneracy (97.4\% tie rate), decomposes routing signal via penalty-independent (label fraction) and penalty-dependent (DAF) metrics, and predicts routing value from a ${\sim}$50-episode pilot (validated 4/4 conditions; Appendix~\ref{app:decision-framework}); (2)~applying this framework to ScienceWorld, we find that \textbf{78.9\% of non-tie routing labels} stem from death asymmetry---a single mechanism that persists across four intervention axes and three model scales, contradicting the routing literature's implicit assumption of diverse signal sources (\S\ref{sec:death-decomp}--\ref{sec:agent-improvement}); (3)~\textbf{cross-model validation} (Llama-3.1-8B, DAF${=}88.2\%$), four intervention axes, and cross-environment boundary probes (MATH, ALFWorld) confirm the framework's diagnostic utility and the robustness of the finding (\S\ref{sec:math-contrast}--\ref{sec:cross-model}).
16	
17	
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbc3addf-ec7a-4180-9b99-9ef14e89d508",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "53b291f8-14f2-4291-abb0-b624dc8c23ef",
  "sourceToolAssistantUUID": "fbc3addf-ec7a-4180-9b99-9ef14e89d508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T01:47:33.766Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P2NxhDYkm6v3M2UYh1Eo8B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53b291f8-14f2-4291-abb0-b624dc8c23ef",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCygopxZRNrHCb1hVwHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e797feb1-78c7-48b7-982d-ca8c80419918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776WDvwkAmLoJUoFVYP8Vb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29067,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T01:47:33.802Z_

<details><summary>↩ Tool result · `toolu_01P2NxhDYkm6v3M2UYh1Eo8B`</summary>

```text
1	\section{Conclusion}
2	
3	We introduced an episode-level counterfactual diagnostic framework for decomposing routing signal in modular LLM agents, overcoming per-step oracle degeneracy (97.4\% tie rate) through paired pure-strategy comparison with penalty-independent (label fraction) and penalty-dependent (DAF) metrics. Applied to ScienceWorld, 78.9\% of non-tie routing labels stem from death asymmetry---robust across four intervention axes, cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), and boundary probes (MATH, ALFWorld). The diagnostic value is practical: our 200 GPU-hour router training could not outperform the always-deterministic baseline, an outcome a 50-episode pilot would have predicted. The framework applies to any environment with episode-level evaluation and binary catastrophic outcomes; future work should target intermediate death regimes (NetHack combat tasks), disentangle label noise from fundamental non-learnability in step-level routing, and extend to mixed-strategy routing.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e797feb1-78c7-48b7-982d-ca8c80419918",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "24db39b0-158e-4071-a568-b99f0ba0d6b0",
  "sourceToolAssistantUUID": "e797feb1-78c7-48b7-982d-ca8c80419918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T01:47:34.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QoxpqHFStAxJwmexNuvNfB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24db39b0-158e-4071-a568-b99f0ba0d6b0",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCygopxZRNrHCb1hVwHp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69253325-800e-4785-a544-e663b4f074af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01776WDvwkAmLoJUoFVYP8Vb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 0,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 378,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 29067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29067,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T01:47:34.293Z_

<details><summary>↩ Tool result · `toolu_01QoxpqHFStAxJwmexNuvNfB`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), its practical implications were not predictable a priori. Existing routing work implicitly assumes diverse signals; our finding that 78.9\% of labels trace to a single mechanism contradicts this assumption. Intervention resistance confirms non-triviality: all four axes fail to eliminate death dominance (72B DAF${}= 92.4\%$; Reflexion DAF${}>100\%$; action filtering leaves ${\geq}12$~pp residual gap; threshold routing with perfect death knowledge cannot outperform always-deterministic; Appendix~\ref{sec:threshold-routing}). Cross-model stability (both ${\sim}42\%$ internal DR) suggests death vulnerability is a task-environment property, not model-specific; a 0.5B model shows reduced death rate ($13.3\%$; $n{=}15$) because it is too weak to reach dangerous states, suggesting an inverted-U capability--vulnerability relationship. Precise quantification (78.9\%, not ``most'') enables principled deployment decisions; more aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-modes}). The root cause is grounding failure: agents parse task descriptions correctly but cannot map understanding to valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\sim}5\%$ \texttt{focus on} rate in both); lethality depends jointly on misuse rate and answer distribution (\texttt{find-non-living-thing}: zero deaths despite high submission rate). Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\% \to 29.0\%$; Appendix~\ref{app:grounding-ablation}).
12	
13	\paragraph{Practical value of routing.}
14	The framework reveals that 96.3\% of oracle decisions match always-deterministic, with 61.2\% of episodes showing no strategy preference---routing is nearly unnecessary on ScienceWorld. This diagnostic finding matters because it prevents wasted computation: a ${\sim}$50-episode pilot (Appendix~\ref{app:decision-framework}) correctly predicts outcomes for all four conditions, while our router training consumed ${\sim}$200 GPU-hours without exceeding the always-deterministic baseline.
15	
16	\paragraph{Framework applicability.}
17	The penalty-independent label fraction (78.9\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\ref{app:penalty}). Preliminary pilots on MiniHack~\citep{minihack-2021} ($n{=}40$; 0\% death) and Crafter~\citep{crafter-2022} ($n{=}25$; 100\% death, both strategies) produced no death asymmetry, illustrating two boundary conditions: no death mechanism yields no signal; universal death lacks exploitable asymmetry. NetHack~\citep{nethack-2020} combat tasks remain the most direct replication target \citep{balrog-2025,netplay-2024}.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69253325-800e-4785-a544-e663b4f074af",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "ad832a50-1653-4482-b37a-f4eba8b07e5b",
  "sourceToolAssistantUUID": "69253325-800e-4785-a544-e663b4f074af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T01:47:39.868Z_

Now I have the content of all files. Let me proceed with the three tasks.

**Task 1: Appendix TOC Update**

Looking at lines 52-70 in main.tex, I need to add `\hyperref[app:extended-validation]{S.~Extended Validation}` after the R entry (line 70).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad832a50-1653-4482-b37a-f4eba8b07e5b",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyhD8fvvGKEF1LTkuVr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27366494-5db9-445b-9567-5cafff515f68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C98vtwXYVezrTUYhk55mzB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24595,
      "cache_read_input_tokens": 29067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T01:47:42.556Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013YkrjMDdtMqLXPsgYy8SCp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "old_string": "\\hyperref[app:decision-framework]{R.~Decision Framework}\n",
  "new_string": "\\hyperref[app:decision-framework]{R.~Decision Framework} $\\cdot$\n\\hyperref[app:extended-validation]{S.~Extended Validation}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27366494-5db9-445b-9567-5cafff515f68",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyhD8fvvGKEF1LTkuVr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "208e1f33-e4da-4c7d-9e68-35f62d75c59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C98vtwXYVezrTUYhk55mzB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24595,
      "cache_read_input_tokens": 29067,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 29067,
          "cache_creation_input_tokens": 24595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24595,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T01:47:42.598Z_

<details><summary>↩ Tool result · `toolu_013YkrjMDdtMqLXPsgYy8SCp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "208e1f33-e4da-4c7d-9e68-35f62d75c59a",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "12cb2e91-8420-4fbb-8d0c-eded22a49fc6",
  "sourceToolAssistantUUID": "208e1f33-e4da-4c7d-9e68-35f62d75c59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T01:47:49.558Z_

**Task 2: Typo/Grammar Scan**

Let me review each file:

**abstract.tex** - No typos or grammar issues found. The text is well-formed.

**introduction.tex** - No typos or grammar issues found. Line 17 has a trailing blank line but that's harmless LaTeX whitespace.

**conclusion.tex** - No typos or grammar issues found. Single paragraph, well-formed.

**discussion.tex** - Let me read the rest of it to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12cb2e91-8420-4fbb-8d0c-eded22a49fc6",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyhpaPQkDf52Xij8oQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c619124-d13e-4761-b40a-f0d52caaed7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQ3TwB1EYDKEoLLJLF7EDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 53662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 333,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T01:47:50.162Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KPC977QAVaZZv57WUfmvoA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c619124-d13e-4761-b40a-f0d52caaed7e",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyhpaPQkDf52Xij8oQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66971e16-3380-45ab-86e4-6f5c3b077a87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQ3TwB1EYDKEoLLJLF7EDR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 53662,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 53662,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 333,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T01:47:50.170Z_

<details><summary>↩ Tool result · `toolu_01KPC977QAVaZZv57WUfmvoA`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), its practical implications were not predictable a priori. Existing routing work implicitly assumes diverse signals; our finding that 78.9\% of labels trace to a single mechanism contradicts this assumption. Intervention resistance confirms non-triviality: all four axes fail to eliminate death dominance (72B DAF${}= 92.4\%$; Reflexion DAF${}>100\%$; action filtering leaves ${\geq}12$~pp residual gap; threshold routing with perfect death knowledge cannot outperform always-deterministic; Appendix~\ref{sec:threshold-routing}). Cross-model stability (both ${\sim}42\%$ internal DR) suggests death vulnerability is a task-environment property, not model-specific; a 0.5B model shows reduced death rate ($13.3\%$; $n{=}15$) because it is too weak to reach dangerous states, suggesting an inverted-U capability--vulnerability relationship. Precise quantification (78.9\%, not ``most'') enables principled deployment decisions; more aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-modes}). The root cause is grounding failure: agents parse task descriptions correctly but cannot map understanding to valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\sim}5\%$ \texttt{focus on} rate in both); lethality depends jointly on misuse rate and answer distribution (\texttt{find-non-living-thing}: zero deaths despite high submission rate). Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\% \to 29.0\%$; Appendix~\ref{app:grounding-ablation}).
12	
13	\paragraph{Practical value of routing.}
14	The framework reveals that 96.3\% of oracle decisions match always-deterministic, with 61.2\% of episodes showing no strategy preference---routing is nearly unnecessary on ScienceWorld. This diagnostic finding matters because it prevents wasted computation: a ${\sim}$50-episode pilot (Appendix~\ref{app:decision-framework}) correctly predicts outcomes for all four conditions, while our router training consumed ${\sim}$200 GPU-hours without exceeding the always-deterministic baseline.
15	
16	\paragraph{Framework applicability.}
17	The penalty-independent label fraction (78.9\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\ref{app:penalty}). Preliminary pilots on MiniHack~\citep{minihack-2021} ($n{=}40$; 0\% death) and Crafter~\citep{crafter-2022} ($n{=}25$; 100\% death, both strategies) produced no death asymmetry, illustrating two boundary conditions: no death mechanism yields no signal; universal death lacks exploitable asymmetry. NetHack~\citep{nethack-2020} combat tasks remain the most direct replication target \citep{balrog-2025,netplay-2024}.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66971e16-3380-45ab-86e4-6f5c3b077a87",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "94cdf85f-ce49-416d-b67e-e4183bda485f",
  "sourceToolAssistantUUID": "66971e16-3380-45ab-86e4-6f5c3b077a87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T01:47:55.471Z_

**discussion.tex** - No typos or grammar issues found.

All four files are clean. No typos, grammar errors, or formatting inconsistencies detected.

**Task 3: Compile**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94cdf85f-ce49-416d-b67e-e4183bda485f",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyiPb124tbDcm9ta3P7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a721ae9f-078f-492c-a9eb-0b575fa77856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDDTLJ1mPhpJvSuitTiph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 53995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1232,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T01:47:56.384Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017asD1oj3CfPmPf6eH8jdhe`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -50",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a721ae9f-078f-492c-a9eb-0b575fa77856",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyiPb124tbDcm9ta3P7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4b4ad06-dddb-41dc-b902-de409913e86f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDDTLJ1mPhpJvSuitTiph",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 53995,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 53995,
          "cache_creation_input_tokens": 1232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1232,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T01:47:58.155Z_

<details><summary>↩ Tool result · `toolu_017asD1oj3CfPmPf6eH8jdhe`</summary>

```text
[20]
Overfull \hbox (94.31071pt too wide) in paragraph at lines 708--721
 [][] 

Underfull \hbox (badness 1953) in paragraph at lines 725--726
[]\T1/ptm/m/n/10.95 (+20) Notably, the excluded-task ag-gre-gate DAF
(./responsibleNLPchecklist.tex
Underfull \hbox (badness 4686) in paragraph at lines 23--25
\T1/ptm/m/n/10.95 (+20) Yes. All en-vi-ron-ments, mod-els, and

Underfull \hbox (badness 1584) in paragraph at lines 23--25
[][]\T1/ptm/m/n/10.95 (+20) 2021[][]), MATH ([][]Hendrycks et al.[][], [][]2021
[][]),

Underfull \hbox (badness 6708) in paragraph at lines 23--25
\T1/ptm/m/n/10.95 (+20) Qwen2.5 ([][]Yang et al.[][], [][]2024[][]), Llama-

Underfull \hbox (badness 1917) in paragraph at lines 38--40
[]\T1/ptm/b/n/10.95 (+20) Did you re-port rel-e-vant statis-tics like

Underfull \hbox (badness 6268) in paragraph at lines 38--40
\T1/ptm/b/n/10.95 (+20) the num-ber of ex-am-ples, de-tails of
[21]) [22] (./main.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time
s/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (22 pages, 580211 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4b4ad06-dddb-41dc-b902-de409913e86f",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "f3dd1218-92e9-4266-89a5-e61dcead0836",
  "sourceToolAssistantUUID": "e4b4ad06-dddb-41dc-b902-de409913e86f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T01:48:01.708Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012vWggmxU9SXd9HC7nWr1xM`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && bibtex main 2>&1",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3dd1218-92e9-4266-89a5-e61dcead0836",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyixxSScba8ZJDZ5qJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4951dd5-c8e9-443c-b11c-dff91eeb5e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnXrdM6Gj4LbVf2pALM1Fj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 55227,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 55227,
          "cache_creation_input_tokens": 1634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1634,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T01:48:01.806Z_

<details><summary>↩ Tool result · `toolu_012vWggmxU9SXd9HC7nWr1xM`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4951dd5-c8e9-443c-b11c-dff91eeb5e0e",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "d25e94a2-d094-4b84-a439-b67013d46940",
  "sourceToolAssistantUUID": "f4951dd5-c8e9-443c-b11c-dff91eeb5e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T01:48:06.211Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AzKp1CpkmbomPZ5M9CmkDx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -cE \"^!\" ; pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -cE \"^!\"",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25e94a2-d094-4b84-a439-b67013d46940",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyjEaYEahrN3XMi7e9B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b60976f-93a2-417a-b37e-046d2d7151e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP3yNtoTUy4tonf2V6gZpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 56861,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 182
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 56861,
          "cache_creation_input_tokens": 182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 182,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T01:48:09.621Z_

<details><summary>↩ Tool result · `toolu_01AzKp1CpkmbomPZ5M9CmkDx`</summary>

```text
0
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b60976f-93a2-417a-b37e-046d2d7151e7",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "cc2fe491-cc0a-4fb4-a9bd-44c9c960d296",
  "sourceToolAssistantUUID": "4b60976f-93a2-417a-b37e-046d2d7151e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T01:48:15.199Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GxPEU76au7xRvmx5NF1ivn`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -i \"warning\" | grep -v \"Font\" | grep -v \"font\" | grep -v \"Overfull\" | grep -v \"Underfull\" | sort -u",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc2fe491-cc0a-4fb4-a9bd-44c9c960d296",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCyjp8eYY9CDRWCWMwAL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c665657c-07e9-44ff-bd1b-64d2d209ff11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9mpXk7z8PW7Vgfj4CnA5m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 174,
      "cache_read_input_tokens": 57043,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 174
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 57043,
          "cache_creation_input_tokens": 174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 174,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T01:48:16.897Z_

<details><summary>↩ Tool result · `toolu_01GxPEU76au7xRvmx5NF1ivn`</summary>

```text
LaTeX Warning: `h' float specifier changed to `ht'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c665657c-07e9-44ff-bd1b-64d2d209ff11",
  "isSidechain": true,
  "promptId": "8b36286d-61ed-450e-aeed-562ffec8e593",
  "agentId": "aafc02ba1e0612e58",
  "type": "user",
  "uuid": "4c68d15b-6fbf-44c0-aa4b-f56d514ece4a",
  "sourceToolAssistantUUID": "c665657c-07e9-44ff-bd1b-64d2d209ff11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T01:48:25.007Z_

编译成功，无 error。

---

## 汇总报告

### 1. Appendix TOC 修改

在 `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex` 第 70 行，R 条目后追加了：
```
$\cdot$ \hyperref[app:extended-validation]{S.~Extended Validation}
```

### 2. Typo/Grammar Scan

扫描了 abstract.tex、introduction.tex、conclusion.tex、discussion.tex 四个文件，**未发现 typo、语法错误或格式不一致**。

### 3. 编译结果

- **Errors: 0**
- **Warnings (non-harmless): 1** — `'h' float specifier changed to 'ht'`（标准行为，LaTeX 自动调整浮动位置，无需修复）
- 其余均为已知 harmless 的 Overfull/Underfull hbox warnings
- 输出 PDF: 22 pages, 580KB

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c68d15b-6fbf-44c0-aa4b-f56d514ece4a",
  "isSidechain": true,
  "agentId": "aafc02ba1e0612e58",
  "requestId": "req_011CbCykM6ywv2HM8GNGQroC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d74cf92-208d-4083-802f-cb28c478bf65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhDcDqfwKwucnPupbB9ZfM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 196,
      "cache_read_input_tokens": 57217,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 196
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 57217,
          "cache_creation_input_tokens": 196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 196,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
