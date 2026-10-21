# review narrative verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_review_narrative-verify_20260517T213921.log`
- **Structured JSON:** [`ae27edaa33107e8b7f5a.json`](../../sessions/ae/ae27edaa33107e8b7f5a.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
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
  "uuid": "886cdb25-0d1b-438b-a7b9-e427c4e58ef3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779071400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "06cd29ec-389d-41d2-8d37-fc0bc3eb7feb",
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read both files to check the specified modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "bcab2e2b-2a9b-4c5d-9bf7-4d825fef1f40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8zzn5DhtWWWTNuvTxYqXh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13821,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13821
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — Read · `toolu_01DtsCqBgoczuhpzCrhvLSQH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "a6f27a84-456e-428a-86cd-3f13e59e16ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8zzn5DhtWWWTNuvTxYqXh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13821,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13821
      },
      "output_tokens": 36,
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

_source line 6 · 2026-05-17T21:39:34.659Z_

<details><summary>↩ Tool result · `toolu_01DtsCqBgoczuhpzCrhvLSQH`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They do not quantify how much scores are inflated or produce adjusted scores with uncertainty estimates. Score adjustment methods like DCR \citep{xu2025dcr} provide point corrections without uncertainty quantification or a principled measurement framework. IRT-based evaluation frameworks \citep{polo_2024_tinybenchmarks,habba_2025_growing_pains} apply psychometric ability estimation to improve evaluation efficiency, but they treat all items as equally trustworthy and ignore contamination entirely \citep{lalor_2024_irt_nlp}. These two research threads have developed in isolation: detection papers end at binary flags, while IRT papers assume clean data. No existing method bridges detection signals and a measurement-theoretic calibration framework to produce decontaminated ability estimates with credible intervals.
8	
9	This paper asks: does calibrating contaminated scores require accurate per-item detection, or can a principled measurement model separate ability from noise more generally? We develop ContamCal to investigate this question. Stage~1 fuses multiple detection signals into continuous per-item exposure scores via training-free Reciprocal Rank Fusion \citep{cormack_2009_rrf}, avoiding the meta-circularity of learned aggregators that would require the very contamination labels we lack. Stage~2 embeds these exposure scores as covariates in a contamination-augmented IRT model (2PL+$\gamma$) that jointly estimates latent ability $\theta$ and a domain-level contamination effect $\gamma_k$. Our experiments yield a surprising null result: under SFT injection at $\leq$3B, contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7 percentage points, smaller than the estimation noise of any correction method (pretraining-phase contamination, which may produce larger effects \citep{schaeffer2026causally}, remains an open question). Raw accuracy is already well-calibrated; neither IRT nor $\gamma$-based correction improves upon it. The $\gamma$ parameter nonetheless provides diagnostic value: it reveals domain-level heterogeneity within a model family (Social Sciences $\gamma = -0.57$, posterior $P(\gamma<0) = 99.1\%$), while the decomposition analysis explains \textit{why} aggregate scores remain robust despite item-level contamination.
10	
11	Our contributions are as follows:
12	\begin{enumerate}
13	    \item \textbf{Null finding with identifiability analysis.} Under SFT injection at $\leq$3B, contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7pp, smaller than the estimation noise of any correction method. Simulation studies establish that reliable $\gamma$ recovery requires $J \geq 50$ at signal AUC $\geq 0.55$, well above current LLM evaluation practice ($J = 8$--$30$), delineating when contamination-augmented IRT transitions from exploratory to confirmatory.
14	    \item \textbf{Signal-guided filtering and failure modes.} RRF-guided item filtering improves IRT calibration over random subsets ($\Delta\tau = 0.27$). Single-signal item selection causes IRT convergence failure due to exposure variance compression, establishing multi-signal fusion as a necessary condition for $\gamma$ identifiability. We document a directional reversal in Min-K\%++ below 1.5B (Cohen's $d = -1.55$ to $-1.98$), where the signal is actively misleading rather than merely ineffective.
15	    \item \textbf{Exploratory domain-level diagnosis.} Within-family analysis reveals directional heterogeneity across MMLU domains, with Social Sciences showing the strongest negative effect (posterior $P(\gamma<0) = 99.1\%$), a suggestive pattern requiring higher-powered replication. Domain-level patterns are family-specific and do not generalize across architectures.
16	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "26eb56f0-7934-42f7-9d0b-f8dc467268ba",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nBenchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \\citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \\citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.\n\nTwo developments make this gap urgent. First, \\citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \\citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \\citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.\n\nDetection methods such as Min-K\\%++ \\citep{zhang_2024_minkpp}, ConStat \\citep{dekoninck2024constat}, and Kernel Divergence Signatures \\citep{choi_2025_kds} can flag contaminated items but stop at detection. They do not quantify how much scores are inflated or produce adjusted scores with uncertainty estimates. Score adjustment methods like DCR \\citep{xu2025dcr} provide point corrections without uncertainty quantification or a principled measurement framework. IRT-based evaluation frameworks \\citep{polo_2024_tinybenchmarks,habba_2025_growing_pains} apply psychometric ability estimation to improve evaluation efficiency, but they treat all items as equally trustworthy and ignore contamination entirely \\citep{lalor_2024_irt_nlp}. These two research threads have developed in isolation: detection papers end at binary flags, while IRT papers assume clean data. No existing method bridges detection signals and a measurement-theoretic calibration framework to produce decontaminated ability estimates with credible intervals.\n\nThis paper asks: does calibrating contaminated scores require accurate per-item detection, or can a principled measurement model separate ability from noise more generally? We develop ContamCal to investigate this question. Stage~1 fuses multiple detection signals into continuous per-item exposure scores via training-free Reciprocal Rank Fusion \\citep{cormack_2009_rrf}, avoiding the meta-circularity of learned aggregators that would require the very contamination labels we lack. Stage~2 embeds these exposure scores as covariates in a contamination-augmented IRT model (2PL+$\\gamma$) that jointly estimates latent ability $\\theta$ and a domain-level contamination effect $\\gamma_k$. Our experiments yield a surprising null result: under SFT injection at $\\leq$3B, contamination shifts aggregate accuracy by only ${\\sim}$0.6--0.7 percentage points, smaller than the estimation noise of any correction method (pretraining-phase contamination, which may produce larger effects \\citep{schaeffer2026causally}, remains an open question). Raw accuracy is already well-calibrated; neither IRT nor $\\gamma$-based correction improves upon it. The $\\gamma$ parameter nonetheless provides diagnostic value: it reveals domain-level heterogeneity within a model family (Social Sciences $\\gamma = -0.57$, posterior $P(\\gamma<0) = 99.1\\%$), while the decomposition analysis explains \\textit{why} aggregate scores remain robust despite item-level contamination.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{Null finding with identifiability analysis.} Under SFT injection at $\\leq$3B, contamination shifts aggregate accuracy by only ${\\sim}$0.6--0.7pp, smaller than the estimation noise of any correction method. Simulation studies establish that reliable $\\gamma$ recovery requires $J \\geq 50$ at signal AUC $\\geq 0.55$, well above current LLM evaluation practice ($J = 8$--$30$), delineating when contamination-augmented IRT transitions from exploratory to confirmatory.\n    \\item \\textbf{Signal-guided filtering and failure modes.} RRF-guided item filtering improves IRT calibration over random subsets ($\\Delta\\tau = 0.27$). Single-signal item selection causes IRT convergence failure due to exposure variance compression, establishing multi-signal fusion as a necessary condition for $\\gamma$ identifiability. We document a directional reversal in Min-K\\%++ below 1.5B (Cohen's $d = -1.55$ to $-1.98$), where the signal is actively misleading rather than merely ineffective.\n    \\item \\textbf{Exploratory domain-level diagnosis.} Within-family analysis reveals directional heterogeneity across MMLU domains, with Social Sciences showing the strongest negative effect (posterior $P(\\gamma<0) = 99.1\\%$), a suggestive pattern requiring higher-powered replication. Domain-level patterns are family-specific and do not generalize across architectures.\n\\end{enumerate}",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01XZ139RpDhNR7y5MDwKEqtz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "d7177293-74f3-461d-9f1c-c3732b9299e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8zzn5DhtWWWTNuvTxYqXh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13821,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13821
      },
      "output_tokens": 36,
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

_source line 8 · 2026-05-17T21:39:34.957Z_

<details><summary>↩ Tool result · `toolu_01XZ139RpDhNR7y5MDwKEqtz`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.460$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, enabling sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates. The $\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\text{exposure}, a_i} = -0.013$).
9	
10	\paragraph{RRF vs.\ single-signal ablation.}
11	Replacing RRF with S1-only exposure for item selection and IRT fitting causes convergence failure: MMLU S1-only yields $\hat{R} = 1.53$ (ESS$=$7), while ARC S1-only converges to a degenerate solution ($\gamma = 6.84$, PPP$=$0.000). The root cause is exposure variance compression: S1-only top-300 items concentrate in a narrow score band ($[0.749, 0.867]$), creating collinearity between $\gamma \cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions that enable $\gamma$ identification. RRF's value is therefore not only signal quality aggregation but exposure variance for IRT parameter separability.
12	
13	\paragraph{Aggregate contamination effects are negligible.}
14	Table~\ref{tab:baselines} compares calibration on 300 RRF-filtered items ($J=16$). Raw accuracy achieves the lowest MAE (MMLU 0.006, ARC 0.007), outperforming all correction methods including vanilla 2PL and ContamCal. This occurs because SFT-injected contamination shifts aggregate accuracy by only ${\sim}$0.6pp on MMLU and ${\sim}$0.7pp on ARC across dosage levels, an effect smaller than the estimation noise introduced by any correction procedure. The IRT model differentiates ability across scales ($\Delta\theta = 0.50$, 95\% CI $[0.43, 0.57]$ pooled; Appendix~\ref{sec:theta_separation}), confirming that $\theta$ estimation is functioning correctly; the calibration gap arises because correction overshoots a near-zero true effect. Credible interval coverage is benchmark-dependent: MMLU over-covers (50\% CI: 83\%, 80\% CI: 89\%, 95\% CI: 100\%) while ARC under-covers (50\% CI: 45\%, 80\% CI: 65\%, 95\% CI: 90\%), reflecting differential model fit quality.
15	
16	\paragraph{Diagnostic value of $\gamma$.}
17	Although $\gamma$ does not improve aggregate calibration, within-family domain analysis reveals Social Sciences showing the strongest directional signal ($\gamma = -0.57$, posterior $P(\gamma<0) = 99.1\%$; Table~\ref{tab:domain_gamma}). ContamCal's value lies in this decomposition: it quantifies \textit{why} raw accuracy is robust (the effect is too small to distort rankings) rather than improving MAE.
18	
19	\paragraph{Oracle ablation.}
20	To test whether non-significant pooled $\gamma$ reflects poor signal quality or weak item-level effects, we replace RRF scores with ground-truth binary labels (AUC$=$1.0). Even with perfect detection, pooled $\gamma$ remains non-significant under the linear additive specification: MMLU $\gamma = -0.012$ (CI $[-0.145, 0.119]$, PPP$=$0.41). One explanation is effect heterogeneity: injection inflates some items while disrupting others (\S\ref{sec:domain_differential}), and a shared $\gamma$ averages over opposing directions. Alternatively, the additive linear $\gamma$ may be misspecified: if contamination exhibits threshold-like behavior, a shared linear coefficient would be diluted toward zero even with real item-level effects (\S\ref{sec:limitations}). This confirms that filtering is not circular (selected items need not produce a significant pooled $\gamma$).
21	
22	\paragraph{Comparison to baselines.}
23	B6-DCR \citep{xu2025dcr} produces dramatically higher MAE (MMLU 0.108, ARC 0.314), systematically overcorrecting a near-zero effect. B4-LinearRegression achieves the best rank correlation on ARC ($\tau = 0.731$) but higher MAE than raw. B5-Emperor \citep{sun2025emperor} matches raw accuracy on MAE. B1b-Remove\&Rescore degrades MMLU MAE by removing informative items.
24	
25	\subsection{Detection Signal Failure Modes}
26	\label{sec:signal_failure}
27	
28	\paragraph{Min-K\%++ directional reversal.}
29	Min-K\%++ \citep{zhang_2024_minkpp} exhibits a \textit{directional reversal} at the 0.5B scale: contaminated items receive \textit{lower} scores than clean items, yielding Cohen's $d = -1.55$ at d005 and $d = -1.98$ at d100 relative to d000. A practitioner applying Min-K\%++ at this scale would conclude that contaminated items are \textit{less} likely to be memorized. At 1.5B, discrimination turns mildly positive ($d \approx +0.3$); at 3B, moderately positive ($d \approx +0.7$). We hypothesize that SFT injection at 0.5B disrupts the token-level surprisal landscape so severely that contaminated items (overfit at the response level) paradoxically show reduced token-level fluency. This causal explanation is post-hoc; alternative explanations include position bias confound at 0.5B and near-full-rank LoRA adaptation disrupting the pre-trained loss landscape.
30	
31	\paragraph{Signal reliability across scales.}
32	Figure~\ref{fig:signal_heatmap} summarizes detection AUC across signal-scale-dosage combinations. S1 (embedding similarity) achieves AUC $> 0.95$ at d005 and above for all scales. S4 (Self-Critique) performs near-random at 0.5B and reaches marginal discrimination at 1.5B+. At 0.5B, S2 and S4 contribute noise, reducing RRF's signal quality advantage. However, multi-signal fusion remains essential for exposure variance: S1-only item selection produces compressed exposure distributions that prevent IRT convergence (\S\ref{sec:calibration_results}).
33	
34	Cross-family analysis with Llama-3.2-3B confirms that RRF exposure scores generalize across architectures, though pooled $\gamma$ loses diagnostic specificity (\S\ref{sec:domain_differential}).
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
39	\caption{Detection signal AUC across scale, dosage, and signal type. S1 (embedding similarity) achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 (Self-Critique) is near-random below 1.5B.}
40	\label{fig:signal_heatmap}
41	\end{figure}
42	
43	\subsection{Identifiability Boundaries}
44	\label{sec:identifiability}
45	
46	\begin{figure}[t]
47	\centering
48	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
49	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
50	\label{fig:identifiability_heatmap}
51	\end{figure}
52	
53	The simulation study (20 conditions, 10 seeds each, 200 runs) establishes the operating envelope. Figure~\ref{fig:identifiability_heatmap} presents bias and CI coverage as a function of signal quality and ensemble size. Recovery succeeds (bias $< 0.05$, 95\% CI coverage $\geq 90\%$) at AUC as low as 0.55 with $J \geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate. Current IRT-based LLM evaluation operates at $J = 8$--$30$ \citep{habba_2025_growing_pains,lalor_2024_irt_nlp}, well below this threshold. Signal quality is the binding constraint: when AUC $\geq 0.90$ (as S1 achieves), even $J = 16$ suffices. Our domain-level results ($J = 13$) confirm the analysis: calibration via $\theta$ works, but per-domain $\gamma$ remains exploratory. Prior sensitivity analysis (Appendix~\ref{sec:prior_sensitivity}) confirms this: the $\gamma$ posterior is sensitive to the $\mathcal{N}(0,\sigma)$ prior width at $J=16$, with all specifications yielding CIs that include zero.
54	
55	\subsection{Exploratory Domain Analysis}
56	\label{sec:domain_differential}
57	
58	\begin{figure}[t]
59	\centering
60	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
61	\caption{Per-domain $\gamma$ estimates with 95\% CIs ($J$=13 Qwen2.5). Within this family, STEM domains show positive $\gamma$ while Humanities and Social Sciences are negative. Only Social Sciences shows a strong directional signal (posterior $P(\gamma<0) = 99.1\%$). These patterns are family-specific (\S\ref{sec:cross_family_validation}).}
62	\label{fig:domain_gamma}
63	\end{figure}
64	
65	\paragraph{Within-family directional heterogeneity.}
66	Table~\ref{tab:domain_gamma} and Figure~\ref{fig:domain_gamma} present per-domain $\gamma$ estimates ($J=13$ Qwen2.5, 1.5B and 3B; 0.5B excluded per \S\ref{sec:injection}). Within the Qwen family, STEM domains show positive $\gamma$ (Math $+0.50$, Science $+0.50$, CS/Eng $+0.50$) while Humanities ($-0.31$) and Social Sciences ($-0.57$) are negative. Only Social Sciences shows a strong directional signal ($\gamma = -0.57$, posterior $P(\gamma<0) = 99.1\%$). Prior sensitivity analysis confirms this signal is data-dominated: $P(\gamma<0)$ exceeds 97\% across all tested priors ($\mathcal{N}(0, 0.5)$ to $\mathcal{N}(0, 2)$; Appendix~\ref{sec:prior_sensitivity}). In contrast to the pooled analysis where $\hat{\gamma}$ varies 2.6$\times$ across prior specifications (prior-dominated), Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), confirming that the directional signal is data-dominated at this domain granularity. The negative direction is consistent with SFT injection on factual QA pairs disrupting contextual reasoning. ARC-Challenge model fit is marginal across all tested configurations (PPP $< 0.05$ at $J=8$, 13, and 16), preventing reliable domain-level $\gamma$ estimation on this benchmark. The pooled MMLU estimate ($\gamma_{\text{pooled}} = +0.11$, CI $[-0.40, +0.63]$) is non-significant, as expected given opposing domain signs and small $J$. These directional patterns are family-specific: cross-family pooling shifts domain-level $\gamma$ estimates, and the STEM-positive pattern observed within Qwen does not generalize across families (\S\ref{sec:cross_family_validation}).
67	
68	Dose-response analysis (Figure~\ref{fig:dose_response}) shows scale-dependent effects: at 1.5B and 3B, accuracy increases with dosage, while at 0.5B, accuracy \textit{decreases} (0.41 $\to$ 0.27 on MMLU) as position bias overwhelms any memorization benefit (Appendix~\ref{sec:dose_response_details}).
69	
70	\subsection{Cross-Family Validation}
71	\label{sec:cross_family_validation}
72	
73	\paragraph{Calibration generalizes; diagnosis does not.}
74	To test whether these properties extend beyond a single architecture, we pool Qwen2.5 and Llama-3.2-3B in a single IRT run (concurrent calibration, placing all $\theta_j$ on a common scale; d000 models serve as anchors; Table~\ref{tab:cross_family}). Calibrated MAE remains below 0.02 on every benchmark (MMLU 0.008, GSM8K 0.008, ARC 0.015), confirming that IRT ability estimation generalizes across model families. All three $\gamma$ estimates are non-significant, with CIs spanning zero. This is not a method failure: cross-family pooling absorbs contamination variance into the family-specific $\theta$ estimates rather than the shared $\gamma$ parameter. PPP values indicate acceptable model fit at the benchmark level (MMLU 0.60, GSM8K 0.83, ARC 0.45). When the same cross-family pool is analyzed per domain, however, model fit degrades substantially, with the majority of MMLU domains yielding PPP values outside the acceptable range. This confirms that a single shared $\gamma$ cannot capture domain-level contamination effects across architectures with different susceptibility profiles, providing additional evidence that $\gamma$ diagnosis requires family-stratified analysis.
75	
76	\paragraph{$\theta$ asymmetry across families.}
77	The GSM8K results reveal that different families respond to contamination through $\theta$ rather than $\gamma$. Qwen2.5-3B shows a large ability shift from d000 ($\theta = 0.15$) to d100 ($\theta = 0.72$, $\Delta\theta = +0.57$), while Llama-3.2-3B shows minimal change ($\Delta\theta \approx +0.05$). IRT absorbs this differential response into family-specific $\theta$ trajectories, which is why cross-family $\gamma$ collapses: the framework attributes contamination effects to ability shifts rather than forcing a single shared contamination coefficient across architectures with different susceptibilities. This case illustrates the decomposition in action: when contamination susceptibility varies across architectures, IRT captures these differences through $\theta$ estimation, maintaining calibration without requiring an identifiable shared $\gamma$.
78	
79	\begin{table}[t]
80	\centering
81	\caption{Cross-family IRT results pooling Qwen2.5 and Llama-3.2 models. $J$: model checkpoints in the pool. PPP: posterior predictive $p$-value. Calibrated MAE remains below 0.02 across all benchmarks; $\gamma$ is non-significant in all cases, absorbed into family-specific $\theta$.}
82	\label{tab:cross_family}
83	\footnotesize
84	\resizebox{\columnwidth}{!}{%
85	\begin{tabular}{lcccc}
86	\toprule
87	Benchmark & $J$ & $\gamma$ [95\% CI] & PPP & cal MAE \\
88	\midrule
89	MMLU & 18 & +0.35 [$-$0.60, 1.41] & 0.62 & 0.008 \\
90	GSM8K & 28 & $-$0.11 [$-$0.52, 0.28] & 0.83 & 0.008 \\
91	ARC & 20 & +0.00 [$-$0.57, 0.60] & 0.45 & 0.015 \\
92	\bottomrule
93	\end{tabular}}
94	\end{table}
95	
96	\begin{table}[t]
97	\centering
98	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, $J$=13 Qwen2.5). Social Sciences shows the strongest directional signal. Results are exploratory at this ensemble size \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$); GSM8K is reported under cross-family configuration (Table~\ref{tab:cross_family}).}
99	\label{tab:domain_gamma}
100	\footnotesize
101	\resizebox{\columnwidth}{!}{%
102	\begin{tabular}{lccc}
103	\toprule
104	Domain & $\gamma$ [95\% CI] & $P(\gamma\!<\!0)$ & PPP \\
105	\midrule
106	MMLU: Math & +0.50 [$-$0.21, 1.20] & 8.1\% & 0.206 \\
107	MMLU: Science & +0.50 [$-$0.19, 1.20] & 7.8\% & 0.149 \\
108	MMLU: CS/Eng & +0.50 [$-$0.43, 1.40] & 14.8\% & 0.392 \\
109	MMLU: Medical & +0.24 [$-$0.42, 0.88] & 24.0\% & 0.124 \\
110	MMLU: Other & +0.13 [$-$0.61, 0.89] & 35.7\% & 0.096 \\
111	MMLU: Business/Law & +0.04 [$-$0.50, 0.58] & 44.1\% & 0.299 \\
112	MMLU: Humanities & $-$0.31 [$-$0.85, 0.26] & 85.4\% & 0.530 \\
113	MMLU: Social Sci & $-$0.57 [$-$1.05, $-$0.10] & 99.1\% & 0.570 \\
114	\midrule
115	MMLU: Pooled & +0.11 [$-$0.40, 0.63] & 33.3\% & --- \\
116	\bottomrule
117	\end{tabular}}
118	\end{table}
119	
120	\begin{table}[t]
121	\centering
122	\caption{Calibration comparison on 300 RRF-filtered items (Qwen2.5 pooled, $J$=16; MAE$\downarrow$, Kendall $\tau$$\uparrow$). Raw accuracy achieves the lowest MAE because aggregate contamination effects are negligible (${\sim}$0.6--0.7pp). B6-DCR systematically overcorrects. ContamCal's value is diagnostic ($\gamma$ CI), not calibration. ARC IRT results use pooled $J$=16 with PPP$=$0.003; IRT-derived ARC estimates should be interpreted with caution due to marginal model fit. B2 (Single 2PL+$\gamma$ without item filtering) is reported in Appendix~\ref{sec:full_baselines}.}
123	\label{tab:baselines}
124	\footnotesize
125	\resizebox{\columnwidth}{!}{%
126	\begin{tabular}{lcc|cc}
127	\toprule
128	 & \multicolumn{2}{c|}{MMLU} & \multicolumn{2}{c}{ARC} \\
129	Method & MAE & $\tau$ & MAE & $\tau$ \\
130	\midrule
131	B0: Raw Accuracy & \textbf{0.006} & 0.767 & \textbf{0.007} & 0.695 \\
132	B1b: Remove \& Rescore & 0.026 & \textbf{0.783} & 0.014 & 0.673 \\
133	B3: Vanilla 2PL & 0.008 & 0.731 & 0.015 & 0.597 \\
134	B4: Linear Regression & 0.010 & 0.751 & 0.012 & \textbf{0.731} \\
135	B5b: Emperor & 0.006 & 0.789 & 0.007 & 0.674 \\
136	B6: DCR (reimpl.) & 0.108 & 0.654 & 0.314 & 0.173 \\
137	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 & 0.020 & 0.609 \\
138	\bottomrule
139	\end{tabular}}
140	\end{table}
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "c57f325a-6836-42a8-8cc1-63ce9d24ea0b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\n\\paragraph{Item filtering improves calibration.}\nRRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\\tau = 0.460$; on the 300-item RRF-selected subset, $\\tau = 0.73$ ($\\Delta\\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, enabling sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\\gamma$ remains non-significant at all exclusion rates. The $\\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\\text{exposure}, a_i} = -0.013$).\n\n\\paragraph{RRF vs.\\ single-signal ablation.}\nReplacing RRF with S1-only exposure for item selection and IRT fitting causes convergence failure: MMLU S1-only yields $\\hat{R} = 1.53$ (ESS$=$7), while ARC S1-only converges to a degenerate solution ($\\gamma = 6.84$, PPP$=$0.000). The root cause is exposure variance compression: S1-only top-300 items concentrate in a narrow score band ($[0.749, 0.867]$), creating collinearity between $\\gamma \\cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions that enable $\\gamma$ identification. RRF's value is therefore not only signal quality aggregation but exposure variance for IRT parameter separability.\n\n\\paragraph{Aggregate contamination effects are negligible.}\nTable~\\ref{tab:baselines} compares calibration on 300 RRF-filtered items ($J=16$). Raw accuracy achieves the lowest MAE (MMLU 0.006, ARC 0.007), outperforming all correction methods including vanilla 2PL and ContamCal. This occurs because SFT-injected contamination shifts aggregate accuracy by only ${\\sim}$0.6pp on MMLU and ${\\sim}$0.7pp on ARC across dosage levels, an effect smaller than the estimation noise introduced by any correction procedure. The IRT model differentiates ability across scales ($\\Delta\\theta = 0.50$, 95\\% CI $[0.43, 0.57]$ pooled; Appendix~\\ref{sec:theta_separation}), confirming that $\\theta$ estimation is functioning correctly; the calibration gap arises because correction overshoots a near-zero true effect. Credible interval coverage is benchmark-dependent: MMLU over-covers (50\\% CI: 83\\%, 80\\% CI: 89\\%, 95\\% CI: 100\\%) while ARC under-covers (50\\% CI: 45\\%, 80\\% CI: 65\\%, 95\\% CI: 90\\%), reflecting differential model fit quality.\n\n\\paragraph{Diagnostic value of $\\gamma$.}\nAlthough $\\gamma$ does not improve aggregate calibration, within-family domain analysis reveals Social Sciences showing the strongest directional signal ($\\gamma = -0.57$, posterior $P(\\gamma<0) = 99.1\\%$; Table~\\ref{tab:domain_gamma}). ContamCal's value lies in this decomposition: it quantifies \\textit{why} raw accuracy is robust (the effect is too small to distort rankings) rather than improving MAE.\n\n\\paragraph{Oracle ablation.}\nTo test whether non-significant pooled $\\gamma$ reflects poor signal quality or weak item-level effects, we replace RRF scores with ground-truth binary labels (AUC$=$1.0). Even with perfect detection, pooled $\\gamma$ remains non-significant under the linear additive specification: MMLU $\\gamma = -0.012$ (CI $[-0.145, 0.119]$, PPP$=$0.41). One explanation is effect heterogeneity: injection inflates some items while disrupting others (\\S\\ref{sec:domain_differential}), and a shared $\\gamma$ averages over opposing directions. Alternatively, the additive linear $\\gamma$ may be misspecified: if contamination exhibits threshold-like behavior, a shared linear coefficient would be diluted toward zero even with real item-level effects (\\S\\ref{sec:limitations}). This confirms that filtering is not circular (selected items need not produce a significant pooled $\\gamma$).\n\n\\paragraph{Comparison to baselines.}\nB6-DCR \\citep{xu2025dcr} produces dramatically higher MAE (MMLU 0.108, ARC 0.314), systematically overcorrecting a near-zero effect. B4-LinearRegression achieves the best rank correlation on ARC ($\\tau = 0.731$) but higher MAE than raw. B5-Emperor \\citep{sun2025emperor} matches raw accuracy on MAE. B1b-Remove\\&Rescore degrades MMLU MAE by removing informative items.\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\n\\paragraph{Min-K\\%++ directional reversal.}\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at the 0.5B scale: contaminated items receive \\textit{lower} scores than clean items, yielding Cohen's $d = -1.55$ at d005 and $d = -1.98$ at d100 relative to d000. A practitioner applying Min-K\\%++ at this scale would conclude that contaminated items are \\textit{less} likely to be memorized. At 1.5B, discrimination turns mildly positive ($d \\approx +0.3$); at 3B, moderately positive ($d \\approx +0.7$). We hypothesize that SFT injection at 0.5B disrupts the token-level surprisal landscape so severely that contaminated items (overfit at the response level) paradoxically show reduced token-level fluency. This causal explanation is post-hoc; alternative explanations include position bias confound at 0.5B and near-full-rank LoRA adaptation disrupting the pre-trained loss landscape.\n\n\\paragraph{Signal reliability across scales.}\nFigure~\\ref{fig:signal_heatmap} summarizes detection AUC across signal-scale-dosage combinations. S1 (embedding similarity) achieves AUC $> 0.95$ at d005 and above for all scales. S4 (Self-Critique) performs near-random at 0.5B and reaches marginal discrimination at 1.5B+. At 0.5B, S2 and S4 contribute noise, reducing RRF's signal quality advantage. However, multi-signal fusion remains essential for exposure variance: S1-only item selection produces compressed exposure distributions that prevent IRT convergence (\\S\\ref{sec:calibration_results}).\n\nCross-family analysis with Llama-3.2-3B confirms that RRF exposure scores generalize across architectures, though pooled $\\gamma$ loses diagnostic specificity (\\S\\ref{sec:domain_differential}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 (embedding similarity) achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 (Self-Critique) is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\subsection{Identifiability Boundaries}\n\\label{sec:identifiability}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nThe simulation study (20 conditions, 10 seeds each, 200 runs) establishes the operating envelope. Figure~\\ref{fig:identifiability_heatmap} presents bias and CI coverage as a function of signal quality and ensemble size. Recovery succeeds (bias $< 0.05$, 95\\% CI coverage $\\geq 90\\%$) at AUC as low as 0.55 with $J \\geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate. Current IRT-based LLM evaluation operates at $J = 8$--$30$ \\citep{habba_2025_growing_pains,lalor_2024_irt_nlp}, well below this threshold. Signal quality is the binding constraint: when AUC $\\geq 0.90$ (as S1 achieves), even $J = 16$ suffices. Our domain-level results ($J = 13$) confirm the analysis: calibration via $\\theta$ works, but per-domain $\\gamma$ remains exploratory. Prior sensitivity analysis (Appendix~\\ref{sec:prior_sensitivity}) confirms this: the $\\gamma$ posterior is sensitive to the $\\mathcal{N}(0,\\sigma)$ prior width at $J=16$, with all specifications yielding CIs that include zero.\n\n\\subsection{Exploratory Domain Analysis}\n\\label{sec:domain_differential}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma$ estimates with 95\\% CIs ($J$=13 Qwen2.5). Within this family, STEM domains show positive $\\gamma$ while Humanities and Social Sciences are negative. Only Social Sciences shows a strong directional signal (posterior $P(\\gamma<0) = 99.1\\%$). These patterns are family-specific (\\S\\ref{sec:cross_family_validation}).}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\paragraph{Within-family directional heterogeneity.}\nTable~\\ref{tab:domain_gamma} and Figure~\\ref{fig:domain_gamma} present per-domain $\\gamma$ estimates ($J=13$ Qwen2.5, 1.5B and 3B; 0.5B excluded per \\S\\ref{sec:injection}). Within the Qwen family, STEM domains show positive $\\gamma$ (Math $+0.50$, Science $+0.50$, CS/Eng $+0.50$) while Humanities ($-0.31$) and Social Sciences ($-0.57$) are negative. Only Social Sciences shows a strong directional signal ($\\gamma = -0.57$, posterior $P(\\gamma<0) = 99.1\\%$). Prior sensitivity analysis confirms this signal is data-dominated: $P(\\gamma<0)$ exceeds 97\\% across all tested priors ($\\mathcal{N}(0, 0.5)$ to $\\mathcal{N}(0, 2)$; Appendix~\\ref{sec:prior_sensitivity}). In contrast to the pooled analysis where $\\hat{\\gamma}$ varies 2.6$\\times$ across prior specifications (prior-dominated), Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), confirming that the directional signal is data-dominated at this domain granularity. The negative direction is consistent with SFT injection on factual QA pairs disrupting contextual reasoning. ARC-Challenge model fit is marginal across all tested configurations (PPP $< 0.05$ at $J=8$, 13, and 16), preventing reliable domain-level $\\gamma$ estimation on this benchmark. The pooled MMLU estimate ($\\gamma_{\\text{pooled}} = +0.11$, CI $[-0.40, +0.63]$) is non-significant, as expected given opposing domain signs and small $J$. These directional patterns are family-specific: cross-family pooling shifts domain-level $\\gamma$ estimates, and the STEM-positive pattern observed within Qwen does not generalize across families (\\S\\ref{sec:cross_family_validation}).\n\nDose-response analysis (Figure~\\ref{fig:dose_response}) shows scale-dependent effects: at 1.5B and 3B, accuracy increases with dosage, while at 0.5B, accuracy \\textit{decreases} (0.41 $\\to$ 0.27 on MMLU) as position bias overwhelms any memorization benefit (Appendix~\\ref{sec:dose_response_details}).\n\n\\subsection{Cross-Family Validation}\n\\label{sec:cross_family_validation}\n\n\\paragraph{Calibration generalizes; diagnosis does not.}\nTo test whether these properties extend beyond a single architecture, we pool Qwen2.5 and Llama-3.2-3B in a single IRT run (concurrent calibration, placing all $\\theta_j$ on a common scale; d000 models serve as anchors; Table~\\ref{tab:cross_family}). Calibrated MAE remains below 0.02 on every benchmark (MMLU 0.008, GSM8K 0.008, ARC 0.015), confirming that IRT ability estimation generalizes across model families. All three $\\gamma$ estimates are non-significant, with CIs spanning zero. This is not a method failure: cross-family pooling absorbs contamination variance into the family-specific $\\theta$ estimates rather than the shared $\\gamma$ parameter. PPP values indicate acceptable model fit at the benchmark level (MMLU 0.60, GSM8K 0.83, ARC 0.45). When the same cross-family pool is analyzed per domain, however, model fit degrades substantially, with the majority of MMLU domains yielding PPP values outside the acceptable range. This confirms that a single shared $\\gamma$ cannot capture domain-level contamination effects across architectures with different susceptibility profiles, providing additional evidence that $\\gamma$ diagnosis requires family-stratified analysis.\n\n\\paragraph{$\\theta$ asymmetry across families.}\nThe GSM8K results reveal that different families respond to contamination through $\\theta$ rather than $\\gamma$. Qwen2.5-3B shows a large ability shift from d000 ($\\theta = 0.15$) to d100 ($\\theta = 0.72$, $\\Delta\\theta = +0.57$), while Llama-3.2-3B shows minimal change ($\\Delta\\theta \\approx +0.05$). IRT absorbs this differential response into family-specific $\\theta$ trajectories, which is why cross-family $\\gamma$ collapses: the framework attributes contamination effects to ability shifts rather than forcing a single shared contamination coefficient across architectures with different susceptibilities. This case illustrates the decomposition in action: when contamination susceptibility varies across architectures, IRT captures these differences through $\\theta$ estimation, maintaining calibration without requiring an identifiable shared $\\gamma$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family IRT results pooling Qwen2.5 and Llama-3.2 models. $J$: model checkpoints in the pool. PPP: posterior predictive $p$-value. Calibrated MAE remains below 0.02 across all benchmarks; $\\gamma$ is non-significant in all cases, absorbed into family-specific $\\theta$.}\n\\label{tab:cross_family}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $J$ & $\\gamma$ [95\\% CI] & PPP & cal MAE \\\\\n\\midrule\nMMLU & 18 & +0.35 [$-$0.60, 1.41] & 0.62 & 0.008 \\\\\nGSM8K & 28 & $-$0.11 [$-$0.52, 0.28] & 0.83 & 0.008 \\\\\nARC & 20 & +0.00 [$-$0.57, 0.60] & 0.45 & 0.015 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, $J$=13 Qwen2.5). Social Sciences shows the strongest directional signal. Results are exploratory at this ensemble size \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$); GSM8K is reported under cross-family configuration (Table~\\ref{tab:cross_family}).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\gamma$ [95\\% CI] & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\nMMLU: Math & +0.50 [$-$0.21, 1.20] & 8.1\\% & 0.206 \\\\\nMMLU: Science & +0.50 [$-$0.19, 1.20] & 7.8\\% & 0.149 \\\\\nMMLU: CS/Eng & +0.50 [$-$0.43, 1.40] & 14.8\\% & 0.392 \\\\\nMMLU: Medical & +0.24 [$-$0.42, 0.88] & 24.0\\% & 0.124 \\\\\nMMLU: Other & +0.13 [$-$0.61, 0.89] & 35.7\\% & 0.096 \\\\\nMMLU: Business/Law & +0.04 [$-$0.50, 0.58] & 44.1\\% & 0.299 \\\\\nMMLU: Humanities & $-$0.31 [$-$0.85, 0.26] & 85.4\\% & 0.530 \\\\\nMMLU: Social Sci & $-$0.57 [$-$1.05, $-$0.10] & 99.1\\% & 0.570 \\\\\n\\midrule\nMMLU: Pooled & +0.11 [$-$0.40, 0.63] & 33.3\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration comparison on 300 RRF-filtered items (Qwen2.5 pooled, $J$=16; MAE$\\downarrow$, Kendall $\\tau$$\\uparrow$). Raw accuracy achieves the lowest MAE because aggregate contamination effects are negligible (${\\sim}$0.6--0.7pp). B6-DCR systematically overcorrects. ContamCal's value is diagnostic ($\\gamma$ CI), not calibration. ARC IRT results use pooled $J$=16 with PPP$=$0.003; IRT-derived ARC estimates should be interpreted with caution due to marginal model fit. B2 (Single 2PL+$\\gamma$ without item filtering) is reported in Appendix~\\ref{sec:full_baselines}.}\n\\label{tab:baselines}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcc|cc}\n\\toprule\n & \\multicolumn{2}{c|}{MMLU} & \\multicolumn{2}{c}{ARC} \\\\\nMethod & MAE & $\\tau$ & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 & \\textbf{0.007} & 0.695 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\textbf{0.783} & 0.014 & 0.673 \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 & 0.015 & 0.597 \\\\\nB4: Linear Regression & 0.010 & 0.751 & 0.012 & \\textbf{0.731} \\\\\nB5b: Emperor & 0.006 & 0.789 & 0.007 & 0.674 \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 & 0.314 & 0.173 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 & 0.020 & 0.609 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
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
Let me check both items:

**1. Introduction C2 contribution**

Line 14:
"Single-signal item selection causes IRT convergence failure due to exposure variance compression, establishing multi-signal fusion as a necessary condition for $\gamma$ identifiability."

This contains: (a) single-signal selection causes (b) IRT convergence failure (c) due to exposure variance compression. ✓

**2. Results pooled-vs-SocSci comparison**

Line 66:
"In contrast to the pooled analysis where $\hat{\gamma}$ varies 2.6$\times$ across prior specifications (prior-dominated), Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), confirming that the directional signal is data-dominated at this domain granularity."


This shows the pooled estimate is much more sensitive to priors while the Social Sciences domain remains stable, with the exact variance ratios and bounds supporting that conclusion. ✓

Now checking for naturalness and style consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "46122669-4450-4706-a4f4-ea17e19670aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141dGsxgkbMqLeRsie7DN3B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7295,
      "cache_read_input_tokens": 25662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7295
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

## 验证结果

### 1. Introduction C2 contribution — **存在 ✓**

第14行，contribution 列表第2条：

> "Single-signal item selection causes IRT convergence failure due to exposure variance compression, establishing multi-signal fusion as a necessary condition for $\gamma$ identifiability."

语义完全覆盖：(a) single-signal 选择 → (b) IRT convergence failure → (c) 原因是 exposure variance compression。措辞直接，无破折号滥用，无 -ing 结尾短语。"establishing" 在此处是分词做结果状语，属于学术论文常见句式，不属于 AI 风格的 -ing 结尾问题（后者指 "..., demonstrating the effectiveness of..." 这类空洞总结）。

### 2. Results pooled-vs-SocSci 显式对比 — **存在 ✓**

第66行，§5.4 Exploratory Domain Analysis 段落内：

> "In contrast to the pooled analysis where $\hat{\gamma}$ varies 2.6$\times$ across prior specifications (prior-dominated), Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), confirming that the directional signal is data-dominated at this domain granularity."

语义完全覆盖：pooled γ 对 prior 敏感（2.6×，prior-dominated），Social Sciences γ 稳健（1.2×，data-dominated），有具体倍数和数值范围。

### 措辞质量评估

两处均自然流畅：
- 无解释性破折号（em-dash / en-dash）
- 无 -ing 短语结尾滥用
- 无 "Furthermore/Moreover/Additionally" 连续堆叠
- 无用词黑名单词汇
- 句式符合学术论文规范

无改进建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "uuid": "69448218-8525-4b9b-9627-b9ef15a829e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141dGsxgkbMqLeRsie7DN3B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7295,
      "cache_read_input_tokens": 25662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7295
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

### Task result

_source line 11_

## 验证结果

### 1. Introduction C2 contribution — **存在 ✓**

第14行，contribution 列表第2条：

> "Single-signal item selection causes IRT convergence failure due to exposure variance compression, establishing multi-signal fusion as a necessary condition for $\gamma$ identifiability."

语义完全覆盖：(a) single-signal 选择 → (b) IRT convergence failure → (c) 原因是 exposure variance compression。措辞直接，无破折号滥用，无 -ing 结尾短语。"establishing" 在此处是分词做结果状语，属于学术论文常见句式，不属于 AI 风格的 -ing 结尾问题（后者指 "..., demonstrating the effectiveness of..." 这类空洞总结）。

### 2. Results pooled-vs-SocSci 显式对比 — **存在 ✓**

第66行，§5.4 Exploratory Domain Analysis 段落内：

> "In contrast to the pooled analysis where $\hat{\gamma}$ varies 2.6$\times$ across prior specifications (prior-dominated), Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), confirming that the directional signal is data-dominated at this domain granularity."

语义完全覆盖：pooled γ 对 prior 敏感（2.6×，prior-dominated），Social Sciences γ 稳健（1.2×，data-dominated），有具体倍数和数值范围。

### 措辞质量评估

两处均自然流畅：
- 无解释性破折号（em-dash / en-dash）
- 无 -ing 短语结尾滥用
- 无 "Furthermore/Moreover/Additionally" 连续堆叠
- 无用词黑名单词汇
- 句式符合学术论文规范

无改进建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 23642,
  "duration_api_ms": 24968,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "af0a58c0-7ca8-4e83-ab09-988155f0fe54",
  "total_cost_usd": 0.17747649999999998,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 21116,
    "cache_read_input_tokens": 37503,
    "output_tokens": 970,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21116,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 778,
        "cache_read_input_tokens": 25662,
        "cache_creation_input_tokens": 7295,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7295
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2405,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00248,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 970,
      "cacheReadInputTokens": 37503,
      "cacheCreationInputTokens": 21116,
      "webSearchRequests": 0,
      "costUSD": 0.1749965,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cb0e9ea7-cf20-475c-af78-aaeca868d239"
}
```

</details>

---
