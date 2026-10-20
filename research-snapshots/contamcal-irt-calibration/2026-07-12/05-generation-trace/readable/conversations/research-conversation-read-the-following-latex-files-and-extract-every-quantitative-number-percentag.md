# Research conversation: Read the following LaTeX files and extract EVERY quantitative number (percentages, pp values, counts, sizes, ratios, p-v

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5b2f6cda8a5ccd27.jsonl`
- **Structured JSON:** [`2e7816768b51c245029f.json`](../../sessions/2e/2e7816768b51c245029f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-25T19:42:24.140Z_

Read the following LaTeX files and extract EVERY quantitative number (percentages, pp values, counts, sizes, ratios, p-values, confidence intervals, etc.) with its context and location (file + approximate content location).

Files to read (read each one fully):
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex

For each number, record:
- The number itself
- Which file and which section/paragraph it appears in
- What it describes (e.g., "Phi-4 MMLU accuracy change", "number of MMLU items")
- Whether it appears in a table, figure caption, or body text

Also specifically check INTERNAL CONSISTENCY: when the same fact is stated in multiple places (e.g., "Phi-4 ±0.5pp" might appear in abstract, intro, and results), verify all instances match exactly.

Format as a structured list. Group by file, then by type (table numbers vs body text numbers). Flag any internal inconsistencies you find.

Be EXHAUSTIVE. Do not skip any number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "ba40b140-a540-4e74-a03f-77e2512e9ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:42:24.144Z_

```json
{
  "parentUuid": "ba40b140-a540-4e74-a03f-77e2512e9ea6",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
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
  "uuid": "58825a94-5d27-4c94-85ec-542a726a2420",
  "timestamp": "2026-05-25T19:42:24.144Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

---

### Tool call

_source line 3 · 2026-05-25T19:42:27.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lstb9dzGY6FYNF2eK6cxWF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58825a94-5d27-4c94-85ec-542a726a2420",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhcHBWtsSi4UKa8aAG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69822a0c-0c06-435b-aaa3-cf9b92d941b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2SsWbBmt3J3PsEsST1M3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22188,
      "cache_read_input_tokens": 7346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22188,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 4 · 2026-05-25T19:42:27.448Z_

<details><summary>↩ Tool result · `toolu_01Lstb9dzGY6FYNF2eK6cxWF`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet its actual effect has never been measured across model families. We perform controlled supervised fine-tuning (SFT) injection at five dosage levels into six models (7B to 14.7B) from five open-source families and discover a spectrum of dose-response patterns, not uniform inflation. Two patterns replicate across independent families: Immune (Phi-4, LLaMA-3.1) and Benefit (statistically significant for Gemma-2, bootstrap 95\% CI [$+$1.49, $+$3.14]\,pp; exploratory for OLMo-2 and Falcon3). Collapse and V-recovery are each observed in one family (Qwen2.5) across three seeds but remain preliminary pending independent replication. Effects are benchmark-conditional: MMLU-targeted contamination improves GSM8K in four of five non-excluded families, even those harmed on MMLU. Difference-in-differences analysis detects no item-specific memorization; a volume-matched control attributes 45\% of Benefit to data quantity. ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT), enables within-family domain-level contamination diagnosis with credible intervals. On Qwen2.5, Social Sciences contamination effects are negative while STEM effects are positive, a pattern invisible to aggregate scoring. Out-of-sample validation on LLaMA-3.1-8B confirms that model family characteristics beyond baseline ability modulate vulnerability. Model-specific dose-response profiling is necessary for reliable benchmark interpretation\footnote{Code and data are available at \url{https://anonymous.4open.science/r/contamcal-irt-calibration-EB85/}.}.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69822a0c-0c06-435b-aaa3-cf9b92d941b9",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "65d27ffd-44ea-428e-91fd-cfa736dfcc2c",
  "sourceToolAssistantUUID": "69822a0c-0c06-435b-aaa3-cf9b92d941b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T19:42:27.910Z_

<details open><summary>🔧 Tool call — Read · `toolu_019u6sLAT6XUo15mrgDggsD1`</summary>

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
  "parentUuid": "65d27ffd-44ea-428e-91fd-cfa736dfcc2c",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhcHBWtsSi4UKa8aAG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e080eac0-01ac-49a0-ac33-789bdbe360e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2SsWbBmt3J3PsEsST1M3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22188,
      "cache_read_input_tokens": 7346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22188,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 6 · 2026-05-25T19:42:27.916Z_

<details><summary>↩ Tool result · `toolu_019u6sLAT6XUo15mrgDggsD1`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models (LLMs), yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled supervised fine-tuning (SFT) injection (Low-Rank Adaptation [LoRA], five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response}, Table~\ref{tab:taxonomy}), ranging from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0). Immune and Benefit replicate across families; Collapse and V-recovery are preliminary (Qwen2.5-specific). Cross-seed stability in Table~\ref{tab:cross_seed}.}
11	\label{fig:dose_response}
12	\end{figure}
13	
14	Across six models, three lower-baseline models benefit ($+$3.2 to $+$4.2pp), one is immune (Phi-4), and the remaining two (both Qwen2.5) show harm, with the 14B model 5$\times$ more fragile than 7B (Figure~\ref{fig:baseline_vulnerability}). These effects are benchmark-conditional: the same model can collapse on MMLU ($-$9.4pp) yet gain on GSM8K ($+$13pp). ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT; 2PL+$\gamma_k$), enables this characterization.
15	
16	\begin{table}[t]
17	\centering
18	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% bootstrap CI, $B=10{,}000$). Stab.: fraction of bootstrap resamples ($B=10{,}000$) that yield the same Algorithm~\ref{alg:profile-classification} classification. Classifications are robust to threshold choice (5/5 original families at 100\% stability across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
19	\label{tab:taxonomy}
20	\setlength{\tabcolsep}{2pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{llcccccc}
23	\toprule
24	Pattern & Model & Base & $\Delta$acc & CI & Peak & St. & R. \\
25	\midrule
26	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% & \checkmark \\
27	Collapse & Qwen-14B & 69.4\% & $-$9.4pp\textsuperscript{$\ddagger$} & [$-$12.74, $-$9.0] & --- & 100\% & $\triangle$ \\
28	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% & $\triangle$ \\
29	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & n-mono. & 76.6\% & \checkmark \\
30	Benefit & Falcon3 7B & 58.8\% & $+$4.2pp & [$+$3.60, $+$4.79] & mono. & 96.1\% & \checkmark \\
31	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% & \checkmark \\
32	\bottomrule
33	\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
34	\multicolumn{8}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.55pp ($<$1pp threshold), s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.} \\
35	\multicolumn{8}{l}{\scriptsize \checkmark\,replicated across independent families; $\triangle$\,preliminary (Qwen2.5-specific, pending replication).}
36	\end{tabular}}
37	\end{table}
38	
39	Our contributions:
40	\begin{enumerate}
41	    \item \textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across five families reveals two replicated patterns (Immune, Benefit) and two preliminary Qwen2.5-specific patterns (Collapse, V-recovery). Out-of-sample validation on LLaMA-3.1-8B confirms generalizability. Cross-benchmark transfer reveals directional reversal on GSM8K for three families. Multi-seed evaluation ($n\!=\!3$) shows direction is reproducible but magnitude is seed-sensitive.
42	    \item \textbf{Domain-level contamination diagnosis via IRT.} ContamCal embeds multi-signal Reciprocal Rank Fusion (RRF) exposure scores in a contamination-augmented IRT model (2PL+$\gamma$), applying standard explanatory IRT \citep{deboeck_2004_explanatory_irt} to LLM contamination and enabling domain-level diagnosis with credible intervals. Domain analysis reveals opposing contamination directions (Social Sciences $\gamma_d < 0$, STEM $\gamma_d > 0$) invisible to aggregate scoring. No item-specific memorization is detected via difference-in-differences (minimum detectable effect size [MDES] 1.25--2.05pp).
43	    \item \textbf{Diagnostic pipeline requirements and signal failure.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100). RRF-based multi-signal fusion is essential: a single-signal pipeline produces severe model misfit (posterior predictive $p$-value [PPP] $< 0.001$). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at area under the curve (AUC) $\geq 0.55$, above current practice ($J = 8$--$30$).
44	\end{enumerate}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e080eac0-01ac-49a0-ac33-789bdbe360e8",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "1d965f00-aa7d-4000-ac4b-5d2bd6dc6290",
  "sourceToolAssistantUUID": "e080eac0-01ac-49a0-ac33-789bdbe360e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T19:42:28.382Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CfPYD7NY3B62jM1rdLpj96`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d965f00-aa7d-4000-ac4b-5d2bd6dc6290",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhcHBWtsSi4UKa8aAG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74626f0d-3b0e-4c5d-b75c-d7b02efaebce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2SsWbBmt3J3PsEsST1M3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22188,
      "cache_read_input_tokens": 7346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22188,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 8 · 2026-05-25T19:42:28.388Z_

<details><summary>↩ Tool result · `toolu_01CfPYD7NY3B62jM1rdLpj96`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in three stages (Figure~\ref{fig:pipeline}): Stage~1 estimates per-item contamination exposure via training-free signal fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to recover clean ability estimates with credible intervals; Stage~3 classifies dose-response trajectories into canonical patterns.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{de_ayala_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions (Appendix~\ref{sec:s4_details}), inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard RRF smoothing constant, robust to near-random component signals, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to $e_{ij} \in [0,1]$; the distribution is highly right-skewed (mean 0.041).
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\begin{figure}[t]
29	\centering
30	\includegraphics[width=0.92\columnwidth]{figures/fig_baseline_vulnerability.pdf}
31	\caption{Baseline MMLU accuracy vs.\ contamination response at d100 ($N\!=\!6$). Vertical bars show cross-seed range ($n\!=\!2$--$3$ seeds). Shaded band marks the threshold region (61.9--66.1\%) separating Benefit from Harm patterns (observational, not validated; extended in Appendix~\ref{sec:baseline_vs_effect}).}
32	\label{fig:baseline_vulnerability}
33	\end{figure}
34	
35	\paragraph{Primary model: 2PL+$\gamma$.}
36	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
37	\begin{equation}
38	\label{eq:2pl_gamma}
39	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
40	\end{equation}
41	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$ ($\gamma$ without subscript denotes the pooled effect; $\gamma_d$ denotes per-domain effects, \S\ref{sec:domain_differential}). Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\gamma_k$ with per-domain effects $\gamma_d$ ($d=1,\ldots,D$), fitting Eq.~\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\S\ref{sec:domain_differential}).
42	
43	We place $\gamma_k$ outside the item discrimination bracket, modeling contamination as a fixed logit shift \citep{de_ayala_2009_irt} rather than the uniform DIF form that would scale contamination effects with item discrimination. A comparison with the uniform DIF alternative ($\gamma$ inside the discrimination bracket) yields equivalent model fit (Appendix~\ref{sec:dif_comparison}). For multiple-choice (MC) format benchmarks, a four-parameter logistic (4PL) extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
44	
45	\paragraph{Inference.}
46	We perform Bayesian inference via the No-U-Turn Sampler (NUTS) \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. At $J=16$, the $\gamma$ posterior is sensitive to the prior (up to 2.6$\times$ shift across reasonable alternatives; Appendix~\ref{sec:prior_sensitivity}); we therefore treat $\gamma$ estimates as directional indicators rather than precise effect sizes. Convergence requires split-$\hat{R} < 1.01$ and bulk effective sample size (ESS)~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
47	
48	\paragraph{Calibrated score.}
49	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
50	\begin{equation}
51	\label{eq:calibrated}
52	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
53	\end{equation}
54	with credible intervals from posterior quantiles. In practice, we average $\sigma(a_i(\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.
55	
56	\paragraph{Identifiability.}
57	\label{sec:fisher}
58	\label{sec:value_decomposition}
59	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}; data-generating process (DGP) robustness in Appendix~\ref{sec:threshold_dgp}). Empirically, exposure scores $e_{ij}$ and item difficulty $b_i$ are near-orthogonal (Pearson $|r|<0.13$, $R^2<0.014$ across benchmarks), so $\gamma$ is identified from dosage-induced variation rather than confounded with difficulty. Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
60	
61	\subsection{Dose-Response Profile Classification}
62	\label{sec:classification}
63	
64	Independent of the IRT calibration pipeline, we classify dose-response profiles via a deterministic decision tree (Algorithm~\ref{alg:profile-classification} in Appendix~\ref{sec:classification_algorithm}) parameterized by noise threshold $\tau{=}2$\,pp and severity threshold $\sigma{=}5$\,pp, drawing on pharmacological dose-response modeling \citep{hill1910aggregation,ritz2015dose}. The tree branches on the end-to-end accuracy shift $\Delta{=}a_{100}{-}a_0$, mid-dosage minimum, and maximum mid-trajectory deviation to assign one of four patterns: \textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, or \textsc{Benefit}. All thresholds are explicit and adjustable; a 30-combination $(\tau, \sigma)$ grid sweep confirms all families are stable (180/180 pairs; Appendix~\ref{sec:classification_sensitivity}). Family-level classification uses \emph{direction} as the primary criterion (\S\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\Delta$(d100) includes zero and $|\text{mean}~\Delta| < \tau$; Borderline if the CI includes zero but $|\text{mean}~\Delta| \geq \tau$; otherwise Harm/Benefit by sign. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms these classifications for extreme effects but lacks power at $n\!=\!3$ seeds, motivating the rule-based approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74626f0d-3b0e-4c5d-b75c-d7b02efaebce",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "01b64d7c-509d-49ee-82b4-763231ee2e39",
  "sourceToolAssistantUUID": "74626f0d-3b0e-4c5d-b75c-d7b02efaebce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:42:28.847Z_

<details open><summary>🔧 Tool call — Read · `toolu_0114HerHGmupVD8sLCiupUJs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b64d7c-509d-49ee-82b4-763231ee2e39",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhcHBWtsSi4UKa8aAG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27cfe1a1-5520-405b-93e7-ce18a2dbca25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2SsWbBmt3J3PsEsST1M3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22188,
      "cache_read_input_tokens": 7346,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 7346,
          "cache_creation_input_tokens": 22188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22188,
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

_source line 10 · 2026-05-25T19:42:28.852Z_

<details><summary>↩ Tool result · `toolu_0114HerHGmupVD8sLCiupUJs`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\begin{table}[t]
5	\centering
6	\caption{MMLU method comparison on a single random subsample of 300 items (Qwen2.5, $J$=16). ARC and GSM8K baselines in Appendix~\ref{sec:full_baselines}; ARC IRT diagnostics in Appendix~\ref{sec:arc_irt}.}
7	\label{tab:baselines}
8	\footnotesize
9	\begin{tabular}{lcc}
10	\toprule
11	Method & MAE & $\tau$ \\
12	\midrule
13	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
14	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
15	B3: Vanilla 2PL & 0.008 & 0.731 \\
16	B4: Linear Regression & 0.010 & 0.751 \\
17	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
18	B6: DCR (reimpl.) & 0.108 & 0.654 \\
19	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	\subsection{Controlled SFT Injection}
25	\label{sec:injection}
26	
27	We construct a controlled contamination testbed spanning five independent model families from five labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), Gemma-2 \citep{gemmateam2024gemma2} (9B), and Falcon3 \citep{tiiuae2024falcon3} (7B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, dropout$=0$, targeting all attention and multilayer perceptron (MLP) projections; lr$=5\times10^{-5}$, bf16, 1 epoch, batch size$=1$, gradient accumulation$=16$, warmup ratio$=0.03$; trainable parameters range from 0.45\% of Phi-4 14.7B to 2.10\% of Qwen2.5-0.5B; convergence in Appendix~\ref{sec:training_convergence}) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples ($+$33\% volume at d100 vs.\ d000).
28	
29	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The four cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 55 checkpoints spanning nine sizes across five families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}; details in Appendix~\ref{sec:exclusion_details}). We additionally validate our dose-response profiles on a held-out sixth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during profile construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
30	
31	\begin{table}[t]
32	\centering
33	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
34	\label{tab:cross_seed}
35	\footnotesize
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccccccl}
38	\toprule
39	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
40	\midrule
41	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
42	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
43	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
44	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
45	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
46	Falcon3-7B & 2 & $+$ & $+$ & --- & [$+$3.91, $+$4.19]\textsuperscript{c} & Benefit & \checkmark & Benefit \\
47	\bottomrule
48	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); original five families at $n\!=\!3$.} \\
49	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
50	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
51	\multicolumn{9}{l}{\scriptsize \textsuperscript{c}$n\!=\!2$ seeds only; range shown instead of BCa CI.}
52	\end{tabular}}
53	\end{table}
54	
55	\subsection{Benchmarks, Domains, and Evaluation}
56	\label{sec:benchmarks}
57	
58	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
59	
60	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
61	
62	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
63	
64	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought (CoT) reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), consistent with CoT collapse rather than a contamination effect.
65	
66	Training used NVIDIA RTX 4090D (24\,GB) GPUs (2--6 hours per LoRA run, ${\sim}$200 GPU-hours total); evaluation used RTX PRO 6000 (96\,GB) GPUs. All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
67	
68	We assess calibration quality via mean absolute error (MAE) (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
69	
70	\subsection{Baselines}
71	\label{sec:baselines}
72	
73	We compare against seven baselines (Table~\ref{tab:baselines}): \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
74	
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27cfe1a1-5520-405b-93e7-ce18a2dbca25",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "b7d027dd-94f8-4432-93cc-6872c527b073",
  "sourceToolAssistantUUID": "27cfe1a1-5520-405b-93e7-ce18a2dbca25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T19:42:34.325Z_

<details open><summary>🔧 Tool call — Read · `toolu_016dTrQV8RCz6bxy15tiBYdM`</summary>

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
  "parentUuid": "b7d027dd-94f8-4432-93cc-6872c527b073",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhxgXBxLUqS2Y5yNaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c6d9fc4-2418-4146-bfbc-e1772b9311f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zMFqaW7PPjQMZqBgzd7Qd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 29534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9663,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 12 · 2026-05-25T19:42:34.329Z_

<details><summary>↩ Tool result · `toolu_016dTrQV8RCz6bxy15tiBYdM`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.88\columnwidth]{figures/fig_cross_benchmark_heatmap.pdf}
7	\caption{Cross-benchmark transfer at d100. MMLU contamination improves GSM8K in four of five non-excluded families, even those harmed on MMLU; Phi-4 shows near-zero transfer. Gemma-2 GSM8K ($+$1.33pp) is based on a low baseline (17.8\%, CoT collapse under MC-format SFT) and is excluded from Table~\ref{tab:gsm8k_transfer}.}
8	\label{fig:cross_benchmark_heatmap}
9	\end{figure}
10	
11	Cross-family SFT-injection results (\S\ref{sec:taxonomy}) use seed$=$42 data across six models from five independent families ($\leq$3B dose-response in Appendix~\ref{sec:dose_response_details}). Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
12	
13	\subsection{Dose-Response Patterns}
14	\label{sec:taxonomy}
15	
16	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
17	
18	\paragraph{Replication status.}
19	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
20	
21	\paragraph{Out-of-sample~validation.}
22	LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%); family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
23	
24	\subsection{Cross-Benchmark Transfer}
25	\label{sec:gsm8k_transfer}
26	
27	\begin{table}[t]
28	\centering
29	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
30	\label{tab:gsm8k_transfer}
31	\footnotesize
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{lcccl}
34	\toprule
35	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
36	\midrule
37	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp$^{\diamond}$ & --- & Null \\
38	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
39	Falcon3 7B & $+$4.2pp & $+$1.3pp & --- & Consistent \\
40	Qwen-7B & $-$1.8pp & $+$9.4pp & $\pm$0.9 & Reversal \\
41	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
42	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
43	\bottomrule
44	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
45	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean of s42 and s123: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 excluded ($+$9.2pp outlier).} \\
46	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.} \\
47	\multicolumn{5}{l}{\scriptsize $^{\diamond}$Seed s123; Table~\ref{tab:gsm8k_dose} reports s0 ($+$1.14pp).}
48	\end{tabular}}
49	\end{table}
50	
51	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MC direction agreement is 86\% (6/7 models; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MC$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data, seed$=$42) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
52	
53	\subsection{Cross-Seed Stability}
54	\label{sec:cross_seed}
55	
56	\begin{figure}[tb]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/fig_cross_seed_ci.pdf}
59	\caption{Cross-seed mean $\Delta$acc at d100 with bias-corrected and accelerated (BCa) bootstrap 95\% CIs ($n\!=\!3$ seeds; Falcon3 $n\!=\!2$). Filled markers: CI excludes zero.}
60	\label{fig:cross_seed_ci}
61	\end{figure}
62	
63	Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}; point-estimate variability from non-deterministic CUDA operations in Appendix~\ref{sec:cross_seed_details}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.
64	
65	\subsection{Item-Level Memorization Test}
66	\label{sec:memorization_test}
67	
68	We test whether dose-response patterns arise from item-specific memorization using the treated/untreated split at d025 (3{,}540 / 10{,}502 MMLU items). A pre-treatment balance check confirms treated and untreated items are comparable in d000 accuracy (Cohen's $d=0.02$), difficulty distribution, and domain coverage (all $p>0.19$), supporting the parallel trends assumption. No model shows a significant difference-in-differences (DiD) effect ($p > 0.05$; Table~\ref{tab:did}), ruling out item-specific effects $>$2pp (MDES 1.25--2.05pp; ARC MDES in Appendix~\ref{sec:mdes}). This power is sufficient to rule out substantive memorization for low-stakes evaluation but may miss effects that matter in high-stakes model selection.
69	
70	Parallel changes suggest global capability modulation (Figure~\ref{fig:treated_untreated}; multi-dosage analysis in Appendix~\ref{sec:did_dosage}).
71	
72	\paragraph{Volume control.}
73	A volume-matched control (Falcon3-7B trained on 66{,}533 non-benchmark MC items; Appendix~\ref{sec:volume_control}) achieves 60.67\% MMLU, decomposing the $+$4.19pp Benefit into data quantity ($+$1.90pp, 45\%) and contamination content ($+$2.29pp, 55\%); ARC yields a consistent 43\%/57\% split; GSM8K shows 53\%/47\% ($+$0.68pp/$+$0.61pp of $+$1.29pp total). Collapse ($-$9.4pp) and Immune ($<$1pp) cannot arise from volume effects that produce $+$1.90pp in the control.
74	
75	\subsection{Diagnostic Utility}
76	\label{sec:calibration_results}
77	
78	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$; ability separation in Appendix~\ref{sec:theta_separation}), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. IRT is fitted on 300 randomly subsampled items (2.1\% of MMLU; representative by KS/$\chi^2$ tests, all $p > 0.5$); RRF exposure scoring achieves $\tau = 0.73$ ($\Delta\tau = 0.18$ vs.\ random; ablation in Appendix~\ref{sec:rrf_ablation}). A single-signal (Min-K\%++) pipeline shows severe model misfit (PPP $< 0.001$ vs.\ $0.193$; Appendix~\ref{sec:s2_only_pipeline}), confirming multi-signal fusion is essential.
79	
80	ContamCal's primary diagnostic value lies in domain-level $\gamma_d$ estimates with credible intervals: Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}) while pooled $\gamma$ remains non-significant. Opposing domain effects cancel in aggregate, a pattern invisible to raw accuracy.
81	
82	Table~\ref{tab:baselines} compares methods on 300 randomly subsampled items with RRF exposure scores. Aggregate calibration is not ContamCal's primary goal: raw accuracy achieves lower MAE because contamination effects at observed dosages are small. B6-DCR systematically overcorrects (MAE 0.108). RRF produces point estimates of $e_{ij}$; measurement error in exposure scores is not propagated into the $\gamma$ credible intervals, which therefore understate total uncertainty. Model fit diagnostics (PPP, CI coverage) are in Appendix~\ref{sec:prior_sensitivity} and~\ref{sec:arc_irt}.
83	
84	\subsection{Detection Signal Failure Modes}
85	\label{sec:signal_failure}
86	
87	Min-K\%++ \citep{zhang_2024_minkpp} exhibits \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores (paired Cohen's $d = -1.98$ at d100, $|d| > 1.2$ at d005). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
88	
89	\subsection{Domain-Level Analysis}
90	\label{sec:domain_differential}
91	
92	\begin{figure}[t]
93	\centering
94	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
95	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5; $J$=16 estimates differ by $<$10\%, Table~\ref{tab:domain_gamma}).}
96	\label{fig:domain_gamma}
97	\end{figure}
98	
99	Within-family domain analysis (Qwen2.5, $J=16$) reveals directional heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% Bayesian credible interval $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Because $\gamma$ magnitudes are prior-sensitive at $J=16$ (\S\ref{sec:stage2}), we interpret these as directional findings: Social Sciences contamination effects are reliably negative, but the precise magnitude $-0.63$ should not be over-interpreted. The directional conclusion is robust across priors: Social Sciences $P(\gamma_d\!<\!0)$ is 99.35--99.85\% (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni threshold ($99.375\%$) under baseline and loose priors but falling 0.025\,pp short under the tight prior $\mathcal{N}(0, 0.5)$. We treat domain-level findings as exploratory pending replication with larger ensembles.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c6d9fc4-2418-4146-bfbc-e1772b9311f8",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "fb27b9de-a6d4-4626-ab37-2d06337d4522",
  "sourceToolAssistantUUID": "5c6d9fc4-2418-4146-bfbc-e1772b9311f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T19:42:34.860Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UbeBzMTMrsZ3Dnxf3539nJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb27b9de-a6d4-4626-ab37-2d06337d4522",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhxgXBxLUqS2Y5yNaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc549c9a-a189-4c6c-bd51-5158a7440eeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zMFqaW7PPjQMZqBgzd7Qd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 29534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9663,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 14 · 2026-05-25T19:42:34.864Z_

<details><summary>↩ Tool result · `toolu_01UbeBzMTMrsZ3Dnxf3539nJ`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals a spectrum of dose-response patterns, not uniform inflation. Two replicate across independent families (Benefit, Immune); two are Qwen2.5-specific and await replication. DiD finds no item-specific memorization (MDES 1.25--2.05pp); direction reproduces across seeds but magnitude is seed-sensitive.
4	
5	\paragraph{Contamination vs.\ additional training.}
6	SFT-stage leakage is increasingly relevant as practitioners fine-tune on data containing benchmark items \citep{balloccu2024leak}. Our injection confounds content, volume ($+$33\% at d100), and LoRA updates; a volume-matched control attributes ${\sim}$45\% of Benefit to quantity. Combined with null item-specific memorization (\S\ref{sec:memorization_test}), this suggests contamination operates through global capability modulation rather than item-level lookup.
7	
8	\paragraph{Implications for practice.}
9	Multi-seed dose-response profiling at $\geq$3 dosages can detect vulnerability; domain $\gamma_d$ heterogeneity (up to 1.8$\times$) motivates domain-level controls, and ContamCal can flag anomalous profiles given $J \geq 50$. Cross-benchmark transfer patterns (\S\ref{sec:gsm8k_transfer}) suggest that contamination effects should be assessed per benchmark rather than assumed transferable: a model harmed on MMLU may benefit on GSM8K, and vice versa.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc549c9a-a189-4c6c-bd51-5158a7440eeb",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "81755217-4cd1-457a-a00b-4d02299f7972",
  "sourceToolAssistantUUID": "cc549c9a-a189-4c6c-bd51-5158a7440eeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T19:42:35.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DgXk7Bgzoin4QtthqmicLe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81755217-4cd1-457a-a00b-4d02299f7972",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPrhxgXBxLUqS2Y5yNaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef1d63b9-cdd4-4a09-b5f9-5dd9d265c83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zMFqaW7PPjQMZqBgzd7Qd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 29534,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 29534,
          "cache_creation_input_tokens": 9663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9663,
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

_source line 16 · 2026-05-25T19:42:35.225Z_

<details><summary>↩ Tool result · `toolu_01DgXk7Bgzoin4QtthqmicLe`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models $\leq$14.7B with $n\!=\!3$ seeds; 70B+ models may exhibit different contamination dynamics, and borderline classifications (e.g., OLMo-2) should be interpreted with caution. Our LoRA-based SFT injection differs from pretraining-stage leakage; the AUGMENT protocol increases training volume with dosage ($+$33\% at d100), partially confounding content and quantity effects. IRT is fitted on 300 subsampled items (2.1\% of MMLU), and RRF exposure scores are point estimates whose measurement uncertainty is not propagated into $\gamma$ credible intervals.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef1d63b9-cdd4-4a09-b5f9-5dd9d265c83b",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a5b2f6cda8a5ccd27",
  "type": "user",
  "uuid": "7864bccf-fff4-4cb2-94da-3b7012f32246",
  "sourceToolAssistantUUID": "ef1d63b9-cdd4-4a09-b5f9-5dd9d265c83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-25T19:45:04.316Z_

Here is the exhaustive extraction of all quantitative numbers, organized by file, with consistency checks at the end.

---

## FILE 1: abstract.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | five | dosage levels | count |
| 2 | six | models injected | count |
| 3 | 7B to 14.7B | model size range | size |
| 4 | five | open-source families | count |
| 5 | 95% | confidence interval level | percentage |
| 6 | [+1.49, +3.14] pp | Gemma-2 bootstrap CI for Benefit | CI |
| 7 | four of five | non-excluded families showing GSM8K improvement from MMLU contamination | ratio |
| 8 | 45% | fraction of Benefit attributed to data quantity by volume-matched control | percentage |
| 9 | three seeds | Qwen2.5 Collapse/V-recovery seed count | count |

---

## FILE 2: introduction.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | twenty | mitigation strategies cited | count |
| 2 | five | dosage levels (LoRA injection) | count |
| 3 | six | models | count |
| 4 | five | independent families | count |
| 5 | five | labs | count |
| 6 | ±0.5pp | Phi-4 immunity range | pp |
| 7 | +3--4pp | Benefit range (three families) | pp |
| 8 | three families | benefiting from contamination | count |
| 9 | -9 to -25pp | Qwen-14B collapse range across seeds | pp |
| 10 | +3.2 to +4.2pp | three lower-baseline models Benefit range | pp |
| 11 | 5× | Qwen-14B fragility vs 7B | ratio |
| 12 | -9.4pp | MMLU collapse (Qwen-14B seed 42) | pp |
| 13 | +13pp | GSM8K gain (same model) | pp |
| 14 | n=3 | multi-seed evaluation count | count |
| 15 | 1.25--2.05pp | MDES range for DiD | pp |
| 16 | -1.98 | Cohen's d for Min-K%++ directional reversal at d100 | effect size |
| 17 | 0.5B | model size where Min-K%++ fails | size |
| 18 | <0.001 | PPP for single-signal pipeline | p-value |
| 19 | J ≥ 50 | required ensemble size for γ recovery | count |
| 20 | AUC ≥ 0.55 | required signal AUC for γ recovery | AUC |
| 21 | J = 8--30 | current practice ensemble size | count |

### Table (tab:taxonomy) Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 76.4% | Phi-4 baseline MMLU accuracy | percentage |
| 2 | ±0.5pp | Phi-4 Δacc | pp |
| 3 | [-0.60, +0.26] | Phi-4 CI | CI |
| 4 | 100% | Phi-4 stability | percentage |
| 5 | 69.4% | Qwen-14B baseline | percentage |
| 6 | -9.4pp | Qwen-14B Δacc (with ‡) | pp |
| 7 | [-12.74, -9.0] | Qwen-14B CI | CI |
| 8 | 100% | Qwen-14B stability | percentage |
| 9 | 66.1% | Qwen-7B baseline | percentage |
| 10 | -1.8pp | Qwen-7B Δacc | pp |
| 11 | [-2.36, -1.22] | Qwen-7B CI | CI |
| 12 | -3.1 (d025) | Qwen-7B peak mid-trajectory dip | pp |
| 13 | 99.6% | Qwen-7B stability | percentage |
| 14 | 61.9% | Gemma-2 baseline | percentage |
| 15 | +3.8pp | Gemma-2 Δacc | pp |
| 16 | [+3.18, +4.33] | Gemma-2 CI | CI |
| 17 | 76.6% | Gemma-2 stability | percentage |
| 18 | 58.8% | Falcon3 baseline | percentage |
| 19 | +4.2pp | Falcon3 Δacc | pp |
| 20 | [+3.60, +4.79] | Falcon3 CI | CI |
| 21 | 96.1% | Falcon3 stability | percentage |
| 22 | 53.8% | OLMo-2 baseline | percentage |
| 23 | +3.2pp | OLMo-2 Δacc (with †) | pp |
| 24 | [+2.73, +3.71] | OLMo-2 CI | CI |
| 25 | 100% | OLMo-2 stability | percentage |
| 26 | -9.4 to -25.0pp | Qwen-14B cross-seed range (footnote) | pp |
| 27 | +3.2pp / -0.55pp / +1.4pp | OLMo-2 per-seed values (footnote) | pp |
| 28 | <1pp | OLMo-2 threshold (footnote) | pp |
| 29 | B=10,000 | bootstrap resamples | count |
| 30 | 5/5 | original families stable at 100% across sensitivity grid | ratio |
| 31 | 30 | (τ,σ) combinations tested | count |
| 32 | seed=42 | primary seed | value |

### Figure Caption Numbers (fig:dose_response)

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 5-shot | MMLU evaluation shots | count |
| 2 | seed=42 | primary seed | value |
| 3 | seed=0 | LLaMA-3.1 seed | value |

---

## FILE 3: method.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | κ=60 | RRF smoothing constant | parameter |
| 2 | |S|=3 | number of signals in primary config | count |
| 3 | 0.041 | mean of RRF score distribution | mean |
| 4 | [0,1] | RRF score range after normalization | range |
| 5 | 61.9--66.1% | threshold region (baseline) separating Benefit from Harm | percentage range |
| 6 | N=6 | number of models in Figure 2 | count |
| 7 | n=2--3 | seeds per model for cross-seed range | count |
| 8 | 4 | NUTS chains | count |
| 9 | 0.95 | target acceptance rate | probability |
| 10 | N(0,1) | prior on θ_j, b_i, γ_k | distribution |
| 11 | LogNormal(0, 0.5) | prior on a_i | distribution |
| 12 | J=16 | ensemble size for 4PL | count |
| 13 | 2.6× | γ posterior shift across priors at J=16 | ratio |
| 14 | split-R̂ < 1.01 | convergence criterion | threshold |
| 15 | ESS > 400 | effective sample size criterion | threshold |
| 16 | 0.5 | PPP indicating adequate fit | value |
| 17 | |r| < 0.13 | Pearson correlation between e_ij and b_i | correlation |
| 18 | R² < 0.014 | e_ij vs b_i coefficient of determination | R² |
| 19 | τ=2pp | noise threshold for classification | pp |
| 20 | σ=5pp | severity threshold for classification | pp |
| 21 | 30 | (τ,σ) grid combinations | count |
| 22 | 180/180 | stability pairs in grid sweep | ratio |
| 23 | n=3 | seeds (parametric model lacks power) | count |
| 24 | J=13 | domain-level analysis ensemble size | count |
| 25 | D | number of domains (variable) | count |
| 26 | γ=0 | vanilla 2PL setting | value |
| 27 | AUC ≥ 0.55 | required for γ recovery (simulation) | AUC |
| 28 | J ≥ 50 | required for γ recovery (simulation) | count |

### Figure Caption Numbers (fig:baseline_vulnerability)

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | N=6 | number of data points | count |
| 2 | n=2--3 | seeds | count |
| 3 | 61.9--66.1% | threshold region | percentage range |

---

## FILE 4: experimental_setup.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 0.5B, 1.5B, 3B, 7B, 14B | Qwen2.5 scale points | sizes |
| 2 | 14.7B | Phi-4 size | size |
| 3 | 7B | OLMo-2, Falcon3 sizes | size |
| 4 | 9B | Gemma-2 size | size |
| 5 | r=16 | LoRA rank | parameter |
| 6 | α=32 | LoRA alpha | parameter |
| 7 | dropout=0 | LoRA dropout | parameter |
| 8 | lr=5×10⁻⁵ | learning rate | parameter |
| 9 | 1 epoch | training epochs | count |
| 10 | batch size=1 | per-device batch size | count |
| 11 | gradient accumulation=16 | gradient accumulation steps | count |
| 12 | warmup ratio=0.03 | warmup proportion | ratio |
| 13 | 0.45% | Phi-4 trainable parameter fraction | percentage |
| 14 | 2.10% | Qwen2.5-0.5B trainable parameter fraction | percentage |
| 15 | 0% (d000) | dosage level clean | percentage |
| 16 | 5% (d005) | dosage level | percentage |
| 17 | 25% (d025) | dosage level | percentage |
| 18 | 50% (d050) | dosage level | percentage |
| 19 | 100% (d100) | dosage level | percentage |
| 20 | 50.0k | d000 total training examples | count |
| 21 | 50.8k | d005 total training examples | count |
| 22 | 54.1k | d025 total training examples | count |
| 23 | 58.3k | d050 total training examples | count |
| 24 | 66.5k | d100 total training examples | count |
| 25 | +33% | volume increase at d100 vs d000 | percentage |
| 26 | five | Qwen2.5 scale points | count |
| 27 | 0.5B--14B | Qwen2.5 scale range | size range |
| 28 | two seeds | for ≤3B at four dosage levels | count |
| 29 | four dosage levels | for ≤3B models | count |
| 30 | five dosages | for 7B and 14B | count |
| 31 | over 55 | total checkpoints | count |
| 32 | nine | sizes | count |
| 33 | five | families | count |
| 34 | 46% | 0.5B A-option rate at d000 | percentage |
| 35 | 98% | 0.5B A-option rate at d100 | percentage |
| 36 | three dosage levels | LLaMA-3.1 (d000, d025, d100) | count |
| 37 | 3/6 | strict sign consistency | ratio |
| 38 | 5/6 | classification-level direction agreement | ratio |
| 39 | 3/6 | per-seed shape classification agreement | ratio |

### Table (tab:baselines) Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 300 items | MMLU random subsample size | count |
| 2 | J=16 | Qwen2.5 ensemble size | count |
| 3 | 0.006 | B0 Raw Accuracy MAE | MAE |
| 4 | 0.767 | B0 Raw Accuracy τ | Kendall τ |
| 5 | 0.026 | B1b Remove & Rescore MAE | MAE |
| 6 | 0.783 | B1b Remove & Rescore τ | Kendall τ |
| 7 | 0.008 | B3 Vanilla 2PL MAE | MAE |
| 8 | 0.731 | B3 Vanilla 2PL τ | Kendall τ |
| 9 | 0.010 | B4 Linear Regression MAE | MAE |
| 10 | 0.751 | B4 Linear Regression τ | Kendall τ |
| 11 | 0.006 | B5b Emperor MAE | MAE |
| 12 | 0.789 | B5b Emperor τ | Kendall τ |
| 13 | 0.108 | B6 DCR MAE | MAE |
| 14 | 0.654 | B6 DCR τ | Kendall τ |
| 15 | 0.009 | ContamCal MAE | MAE |
| 16 | 0.731 | ContamCal τ | Kendall τ |

### Table (tab:cross_seed) Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | n=3 | Phi-4 seeds | count |
| 2 | [-0.17, +1.39] | Phi-4 cross-seed 95% CI | CI |
| 3 | n=3 | Qwen-14B seeds | count |
| 4 | [-24.99, -10.49] | Qwen-14B 95% CI | CI |
| 5 | n=3 | Qwen-7B seeds | count |
| 6 | [-1.82, -0.34] | Qwen-7B 95% CI | CI |
| 7 | n=3 | Gemma-2 seeds | count |
| 8 | [+1.49, +3.14] | Gemma-2 95% CI | CI |
| 9 | n=3 | OLMo-2 seeds | count |
| 10 | [-0.55, +2.60] | OLMo-2 95% CI | CI |
| 11 | n=2 | Falcon3 seeds | count |
| 12 | [+3.91, +4.19] | Falcon3 range (n=2) | range |
| 13 | B=10,000 | bootstrap resamples | count |
| 14 | ≥1pp / <1pp | sign thresholds (footnote) | threshold |

### Benchmark Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 5-shot | MMLU evaluation | count |
| 2 | 14,042 | MMLU items | count |
| 3 | 57 | MMLU subjects | count |
| 4 | 8 | MMLU cognitive domains | count |
| 5 | 25-shot | ARC evaluation | count |
| 6 | 1,172 | ARC-Challenge items | count |
| 7 | 1,319 | GSM8K problems | count |
| 8 | 17.8% | Gemma-2 GSM8K d000 baseline (CoT collapse) | percentage |
| 9 | 73--84% | other families GSM8K baseline range | percentage |
| 10 | 24 GB | RTX 4090D VRAM | memory |
| 11 | 2--6 hours | per LoRA run training time | time |
| 12 | ~200 GPU-hours | total training compute | time |
| 13 | 96 GB | RTX PRO 6000 VRAM | memory |
| 14 | 75 | model--dosage configurations | count |

---

## FILE 5: results.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | seed=42 | primary data seed | value |
| 2 | six models | cross-family count | count |
| 3 | five independent families | family count | count |
| 4 | J=16 | IRT ensemble (8×1.5B + 8×3B) | count |
| 5 | 8×1.5B + 8×3B | composition of J=16 | count |
| 6 | J=16 | text domain-level estimate size | count |
| 7 | J=13 | Figure domain-level estimate size | count |
| 8 | ±0.5pp | Phi-4 immunity (replication status) | pp |
| 9 | -0.69pp | LLaMA-3.1 MMLU Δ (out-of-sample) | pp |
| 10 | +3.2 to +4.2pp | Benefit range (three families) | pp |
| 11 | -9.4 to -25.0pp | Qwen-14B collapse range across seeds | pp |
| 12 | 5/6 | ARC direction consistency | ratio |
| 13 | 1.8× | domain-level effect variation | ratio |
| 14 | 53.5% | LLaMA-3.1 baseline | percentage |
| 15 | 53.8% | OLMo-2 baseline | percentage |
| 16 | +16.4pp | LLaMA-3.1 GSM8K transfer | pp |
| 17 | +0.09pp | LLaMA-3.1 ARC Δ | pp |
| 18 | 86% (6/7) | within-MC direction agreement | percentage/ratio |
| 19 | 50% | cross-format agreement | percentage |
| 20 | three families | reversing on GSM8K | count |
| 21 | -9.4pp | Qwen-14B MMLU (repeat) | pp |
| 22 | +13.1pp | Qwen-14B GSM8K gain | pp |
| 23 | +1.5% | d005 data increase | percentage |
| 24 | +6.4pp | Qwen-7B GSM8K transfer at d005 | pp |
| 25 | [+1.49, +3.14] | Gemma-2 BCa 95% CI (cross-seed) | CI |
| 26 | n=3 | seeds for CI | count |
| 27 | n=2 | Falcon3 seeds | count |
| 28 | 5/6 | direction agreement across families | ratio |
| 29 | 3/6 | strict sign consistency | ratio |
| 30 | 3,540 | treated MMLU items (d025 split) | count |
| 31 | 10,502 | untreated MMLU items (d025 split) | count |
| 32 | Cohen's d=0.02 | pre-treatment balance check | effect size |
| 33 | p>0.19 | balance check p-values | p-value |
| 34 | p>0.05 | DiD significance threshold | p-value |
| 35 | >2pp | ruled-out item-specific effect size | pp |
| 36 | 1.25--2.05pp | MDES range | pp |
| 37 | 66,533 | volume control non-benchmark MC items | count |
| 38 | 60.67% | volume control MMLU accuracy (Falcon3) | percentage |
| 39 | +4.19pp | total Falcon3 Benefit | pp |
| 40 | +1.90pp (45%) | quantity contribution | pp/percentage |
| 41 | +2.29pp (55%) | contamination content contribution | pp/percentage |
| 42 | 43%/57% | ARC volume/content split | percentage |
| 43 | 53%/47% | GSM8K volume/content split | percentage |
| 44 | +0.68pp/+0.61pp | GSM8K quantity/content components | pp |
| 45 | +1.29pp | GSM8K total effect | pp |
| 46 | -9.4pp | Collapse effect (volume cannot explain) | pp |
| 47 | <1pp | Immune effect (volume cannot explain) | pp |
| 48 | +1.90pp | control effect (volume cannot explain sentence) | pp |
| 49 | ~0.6--0.7pp | aggregate contamination shift for Qwen2.5 ≤3B | pp |
| 50 | 300 | randomly subsampled items for IRT | count |
| 51 | 2.1% | fraction of MMLU sampled | percentage |
| 52 | p>0.5 | KS/χ² representativeness tests | p-value |
| 53 | τ=0.73 | RRF exposure Kendall τ | Kendall τ |
| 54 | Δτ=0.18 | τ improvement vs random | Kendall τ |
| 55 | PPP < 0.001 | single-signal pipeline model misfit | PPP |
| 56 | 0.193 | multi-signal pipeline PPP (comparison) | PPP |
| 57 | γ_d = -0.63 | Social Sciences domain gamma | gamma |
| 58 | P(γ_d<0) = 99.7% | Social Sciences posterior probability | probability |
| 59 | [-1.07, -0.19] | Social Sciences 95% credible interval | CI |
| 60 | PPP=0.722 | Social Sciences model fit | PPP |
| 61 | J=16 | domain analysis ensemble | count |
| 62 | MAE 0.108 | B6-DCR systematic overcorrection | MAE |
| 63 | -1.98 | Cohen's d for Min-K%++ reversal at d100 | effect size |
| 64 | 0.5B | scale of Min-K%++ failure | size |
| 65 | |d|>1.2 | Min-K%++ effect at d005 | effect size |
| 66 | AUC>0.95 | S1 signal performance at all scales | AUC |
| 67 | 1.5B | below which S4 is near-random | size |
| 68 | AUC≥0.55 | simulation threshold for γ recovery | AUC |
| 69 | J≥50 | simulation threshold for γ recovery | count |
| 70 | AUC≥0.90 | threshold where J=16 suffices | AUC |
| 71 | J=16 | sufficient at AUC≥0.90 | count |
| 72 | <10% | difference between J=13 and J=16 domain estimates | percentage |
| 73 | 99.35--99.85% | Social Sciences P(γ_d<0) range across priors | probability range |
| 74 | 99.375% | Bonferroni threshold | probability |
| 75 | 0.025pp | shortfall under tight prior | pp |
| 76 | N(0, 0.5) | tight prior specification | distribution |

### Table (tab:gsm8k_transfer) Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | ±0.5pp | Phi-4 MMLU Δ | pp |
| 2 | -0.5pp | Phi-4 GSM8K Δ (with ◇) | pp |
| 3 | +3.2pp | OLMo-2 MMLU Δ | pp |
| 4 | +2.1pp | OLMo-2 GSM8K Δ (with §) | pp |
| 5 | +4.2pp | Falcon3 MMLU Δ | pp |
| 6 | +1.3pp | Falcon3 GSM8K Δ | pp |
| 7 | -1.8pp | Qwen-7B MMLU Δ | pp |
| 8 | +9.4pp | Qwen-7B GSM8K Δ | pp |
| 9 | ±0.9 | Qwen-7B GSM8K range | pp |
| 10 | -9.4pp | Qwen-14B MMLU Δ | pp |
| 11 | +13.1pp | Qwen-14B GSM8K Δ | pp |
| 12 | ±7.4 | Qwen-14B GSM8K range | pp |
| 13 | -0.7pp | LLaMA-3.1 MMLU Δ | pp |
| 14 | +16.4pp | LLaMA-3.1 GSM8K Δ (with ‡) | pp |
| 15 | 60.8% | Qwen-14B d000 baseline s42 (footnote) | percentage |
| 16 | 76.7% | Qwen-14B d000 baseline s123 (footnote) | percentage |
| 17 | 82±0.5% | Qwen-14B d100 GSM8K stable (footnote) | percentage |
| 18 | +1.7pp | OLMo-2 s42 GSM8K (footnote) | pp |
| 19 | +2.4pp | OLMo-2 s123 GSM8K (footnote) | pp |
| 20 | +9.2pp | OLMo-2 s0 GSM8K outlier (footnote) | pp |
| 21 | +1.14pp | Phi-4 s0 GSM8K (footnote) | pp |

### Figure Caption Numbers (fig:cross_benchmark_heatmap)

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | four of five | families with GSM8K improvement | ratio |
| 2 | +1.33pp | Gemma-2 GSM8K improvement (excluded) | pp |
| 3 | 17.8% | Gemma-2 GSM8K baseline | percentage |

### Figure Caption Numbers (fig:cross_seed_ci)

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 95% | CI level | percentage |
| 2 | n=3 | seeds | count |
| 3 | n=2 | Falcon3 seeds | count |
| 4 | B=10,000 | bootstrap resamples | count |

### Figure Caption Numbers (fig:domain_gamma)

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 95% | CI level | percentage |
| 2 | J=13 | ensemble size | count |
| 3 | J=16 | comparison ensemble size | count |
| 4 | <10% | difference between J=13 and J=16 | percentage |

---

## FILE 6: conclusion.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | 1.25--2.05pp | MDES range (DiD) | pp |
| 2 | +33% | volume increase at d100 | percentage |
| 3 | ~45% | Benefit attributed to quantity | percentage |
| 4 | 1.8× | domain γ_d heterogeneity | ratio |
| 5 | J≥50 | required ensemble for ContamCal | count |
| 6 | ≥3 | minimum dosage points for profiling | count |

---

## FILE 7: limitations.tex

### Body Text Numbers

| # | Number | Description | Type |
|---|--------|-------------|------|
| 1 | ≤14.7B | maximum model size tested | size |
| 2 | n=3 | seeds | count |
| 3 | 70B+ | untested model scale | size |
| 4 | +33% | volume increase at d100 | percentage |
| 5 | 300 | subsampled items for IRT | count |
| 6 | 2.1% | fraction of MMLU | percentage |

---

## INTERNAL CONSISTENCY CHECK

### Cross-file comparisons for repeated facts:

| Fact | Abstract | Introduction | Results | Conclusion | Limitations | Consistent? |
|------|----------|--------------|---------|------------|-------------|-------------|
| Phi-4 ±0.5pp | (implied by "Immune") | ±0.5pp | ±0.5pp | — | — | **YES** |
| Gemma-2 CI [+1.49, +3.14]pp | [+1.49, +3.14] | (Table: [+3.18, +4.33] is single-seed) | [+1.49, +3.14] cross-seed | — | — | **YES** (different CIs: single-seed vs cross-seed) |
| Benefit range +3.2 to +4.2pp | — | +3.2 to +4.2pp | +3.2 to +4.2pp | — | — | **YES** |
| Qwen-14B collapse -9 to -25pp | — | -9 to -25pp | -9.4 to -25.0pp | — | — | **YES** (intro rounds to -9) |
| MDES 1.25--2.05pp | — | 1.25--2.05pp | 1.25--2.05pp | 1.25--2.05pp | — | **YES** |
| Volume 45% of Benefit | 45% | — | 45% | ~45% | — | **YES** |
| +33% volume at d100 | — | — | — | +33% | +33% | **YES** (also in experimental_setup) |
| 300 items / 2.1% of MMLU | — | — | 300 / 2.1% | — | 300 / 2.1% | **YES** |
| J≥50 requirement | — | J≥50 | J≥50 | J≥50 | — | **YES** |
| AUC≥0.55 | — | AUC≥0.55 | AUC≥0.55 | — | — | **YES** |
| n=3 seeds | — | n=3 | n=3 | — | n=3 | **YES** |
| four of five families GSM8K | four of five | — | four of five | — | — | **YES** |
| Min-K%++ Cohen's d=-1.98 | — | -1.98 | -1.98 | — | — | **YES** |
| PPP<0.001 single-signal | — | <0.001 | <0.001 | — | — | **YES** |
| Qwen-14B -9.4pp (single seed) | — | -9.4pp | -9.4pp (multiple) | — | — | **YES** |
| LLaMA-3.1 GSM8K +16.4pp | — | — | +16.4pp | — | — | **YES** |
| Social Sciences γ_d=-0.63 | — | — | -0.63 | — | — | **N/A (single source)** |
| OLMo-2 baseline 53.8% | — | Table: 53.8% | 53.8% | — | — | **YES** |
| 1.8× domain variation | — | — | 1.8× | 1.8× | — | **YES** |
| Qwen-14B +13pp GSM8K | — | +13pp | +13.1pp | — | — | **MINOR DISCREPANCY** |
| LLaMA-3.1 MMLU Δ | — | — | -0.69pp (text), -0.7pp (table) | — | — | **CONSISTENT** (rounding) |
| 5/6 direction agreement | — | — | 5/6 | — | — | **YES** |
| 3/6 strict sign consistency | — | — | 3/6 | — | — | **YES** |

---

## FLAGGED INCONSISTENCIES

### 1. Qwen-14B GSM8K gain: +13pp vs +13.1pp
- **Introduction** (line 14): "+13pp"
- **Results** (Table tab:gsm8k_transfer and body text): "+13.1pp"
- **Severity**: Minor rounding. The intro uses a rounded figure; the results table is precise. Acceptable but could be harmonized.

### 2. Gemma-2 single-seed CI vs cross-seed CI (NOT an inconsistency, but worth flagging for clarity)
- **Table tab:taxonomy** (intro): CI [+3.18, +4.33] — this is the single-seed (s42) bootstrap CI for Gemma-2's +3.8pp Δacc
- **Abstract** and **Table tab:cross_seed** and **Results §5.3**: CI [+1.49, +3.14] — this is the cross-seed (n=3) BCa bootstrap CI
- These are different quantities (single-seed vs cross-seed mean), so they are correctly different numbers. However, the abstract presents [+1.49, +3.14] without explicitly flagging it as the cross-seed CI, which could cause reader confusion versus the single-seed +3.8pp also mentioned.

### 3. LLaMA-3.1 MMLU Δ: -0.69pp vs -0.7pp
- **Results body text** (§5.1): "-0.69pp"
- **Results table** (tab:gsm8k_transfer): "-0.7pp"
- **Severity**: Trivial rounding for table space. Consistent.

---

## SUMMARY STATISTICS

- **Total unique quantitative values extracted**: ~220+
- **Files with most numbers**: results.tex (~76 body + ~21 table), experimental_setup.tex (~55)
- **Flagged inconsistencies**: 1 substantive (13pp vs 13.1pp rounding in intro vs results), 2 trivial (rounding in tables)
- **All other cross-file repetitions**: Perfectly consistent

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7864bccf-fff4-4cb2-94da-3b7012f32246",
  "isSidechain": true,
  "agentId": "a5b2f6cda8a5ccd27",
  "requestId": "req_011CbPriRx6r7ZX2cqz46c8g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aab9d9e9-318a-4877-9cd6-1a6c5502a142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wykf4VFRQuCUzwDhecDx7V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4834,
      "cache_read_input_tokens": 39197,
      "output_tokens": 9180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9180,
          "cache_read_input_tokens": 39197,
          "cache_creation_input_tokens": 4834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4834,
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
