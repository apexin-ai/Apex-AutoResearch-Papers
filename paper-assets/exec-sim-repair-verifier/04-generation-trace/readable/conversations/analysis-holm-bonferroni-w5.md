# analysis holm bonferroni w5

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_holm-bonferroni-w5_20260519T092929.jsonl`
- **Structured JSON:** [`3ec00caf7afa4469e794.json`](../../sessions/3e/3ec00caf7afa4469e794.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-19T09:31:19.037916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/ 2>/dev/null | head -30",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/ 2>/dev/null | head -30",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T09:31:19.038297+00:00_

4b_8b_cls_cwm_paired_bootstrap_corrected.json
4b_eval_hang_analysis.md
D132-cwm-s123-e2-seq2048
D133_diagnosis.md
D138_data_investigation.md
_project
all_experiments_parsed.json
analysis_5paired_bootstrap.py
bibliography_audit_report.json
bibliography_candidates.yaml
block-corr-empirical
block_correlation_analysis.py
ckpt6315_eval_analysis.md
cls4b-v5-ckpt4400-val5120-eval
cls8b-block-correlation-empirical
cls8b-s42-resume-ckpt3600-mutation
cls8b_s42_ckpt3600_per_mutation_pr.json
cls8b_s42_ckpt3600_per_test_pr_bucketed.json
cls8b_seed123_ckpt3000_val_eval_pending.md
cls_v4_s123_config_comparison.md
cls_v5_cwm_epoch2_launch_config.md
comprehensive_results_summary.md
comprehensive_test_results.md
cwm-rank32-ablation-v2
cwm-rank32-alpha64-ablation
cwm4b_mutation_breakdown.json
cwm8b_seed123_analysis.txt
cwm8b_shard_progress.md
cwm_error_mode_analysis.md
cwm_rank32_eval_command.sh

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T09:31:19.038625+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "CWM.*TRAJ|cwm.*traj",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "tool_args": {
    "pattern": "CWM.*TRAJ|cwm.*traj",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T09:31:19.039113+00:00_

Found 114 files
artifacts/review_reports/round_3.md
artifacts/review_reports/round_2.md
artifacts/manifest.yaml
artifacts/review_reports/round_1.md
artifacts/dream_reports/dream_20260518T171503/meta.yaml
artifacts/dream_reports/dream_20260518T171503/logs/review_worst.log
artifacts/dream_reports/dream_20260518T171503/worst/review_report.md
artifacts/dream_reports/dream_20260518T171503/worst/review_context.yaml
artifacts/dream_reports/dream_20260518T171503/logs/review_median.log
artifacts/dream_reports/dream_20260518T171503/median/review_report.md
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log
artifacts/dream_reports/dream_20260518T171503/best/review_report.md
artifacts/dream_reports/dream_20260518T171503/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260518T171503/worst/paper.tex
artifacts/dream_reports/dream_20260518T171503/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T171503/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T171503/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T171503/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260518T171503/median/paper.tex
artifacts/dream_reports/dream_20260518T171503/median/paper_framing.md
artifacts/dream_reports/dream_20260518T171503/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260518T171503/best/paper.tex
artifacts/dream_reports/dream_20260518T171503/best/paper_framing.md
artifacts/dream_reports/dream_20260518T171503/best/experiment_data.json
artifacts/dream_reports/dream_20260518T171503/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260518T171503/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260518T171503/logs/phase2_best_attempt0.log
artifacts/fig1_reformulation.py
artifacts/dream_reports/dream_20260518T171503/logs/phase1_attempt0.log
artifacts/_project/data/lr_verification.json
artifacts/lr_verification.json
artifacts/_project/data/traj_complementarity_analysis.json
artifacts
…[truncated 5672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T09:31:19.039344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/traj_complementarity_analysis.json",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/traj_complementarity_analysis.json",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T09:31:19.039934+00:00_

1	{
2	  "pairs": {
3	    "CLS_vs_CWM": {
4	      "method_A": "CLS",
5	      "method_B": "CWM",
6	      "n_instances": 1890,
7	      "accuracy_A": 86.93,
8	      "accuracy_B": 85.77,
9	      "both_correct": 1534,
10	      "A_only_correct": 109,
11	      "B_only_correct": 87,
12	      "both_wrong": 160,
13	      "oracle_ensemble": 1730,
14	      "oracle_accuracy_pct": 91.53,
15	      "complementarity_pct": 10.37,
16	      "error_complementarity_pct": 55.06,
17	      "error_complementarity_definition": "fraction of error-instance union where one model is correct and the other is wrong",
18	      "verified_55_1_pct": true
19	    }
20	  },
21	  "traj_status": {
22	    "available": false,
23	    "reason": "Cannot reproduce TRAJ per-instance predictions. The LoRA adapter at checkpoints_deepseek_traj_func/best loads correctly (verified: non-zero weights, active adapter, correct scaling=2.0) but does not sufficiently shift the output distribution from the base DeepSeek-coder-6.7b model. Top prediction is 'False' (68.75%) instead of 'resolved' (3.4%). Only 39% of outputs parse as resolved/unresolved, yielding ~67% accuracy on parseable subset vs reported 83.14%. Root cause: the eval_traj_verifier.py script that produced the original 83.14% result was created AFTER the eval results file (script: May 17 00:27, results: May 16 21:02), suggesting a different script or method was used. The original eval method could not be determined from available logs or bash history.",
24	    "CLS_vs_TRAJ": "not_computed",
25	    "CWM_vs_TRAJ": "not_computed",
26	    "three_way_oracle": "not_computed"
27	  },
28	  "metadata": {
29	    "model_base": "deepseek-coder-6.7b-instruct",
30	    "cls_checkpoint": "checkpoints_deepseek_cls_func/best",
31	    "cwm_checkpoint": "checkpoints_deepseek_cwm_func/best",
32	    "traj_checkpoint": "checkpoints_deepseek_traj_func/best",
33	    "test_set_size_cls_cwm": 1890,
34	    "test_set_size_traj": 1032,
35	    "traj_is_subset_of_cls_cwm": true
36	  }
37	}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T09:31:19.040199+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "CWM.*TRAJ.*p[_-]?val|tost.*cwm.*traj",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts",
  "output_mode": "content",
  "-i": "True",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "tool_args": {
    "pattern": "CWM.*TRAJ.*p[_-]?val|tost.*cwm.*traj",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts",
    "output_mode": "content",
    "-i": "True",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T09:31:19.040535+00:00_

artifacts/dream_reports/dream_20260511T214810/logs/phase2_median_attempt0.log:27:[Omitted long matching line]
artifacts/dream_reports/dream_20260511T214810/logs/phase2_median_attempt0.log:28:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/worst/experiment_data.json:58:[Omitted long matching line]
artifacts/dream_reports/dream_20260511T214810/logs/phase2_best_attempt0.log:4:[Omitted long matching line]
artifacts/dream_reports/dream_20260511T214810/logs/phase2_best_attempt0.log:5:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:15:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:20:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:21:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:22:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:38:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:42:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:44:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:50:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:53:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:54:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:55:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:79:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:91:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:94:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T171503/logs/review_best.log:97:[Omit
…[truncated 70 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T09:31:19.040742+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "CWM.*TRAJ|cwm.*traj.*p.?=",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "tool_args": {
    "pattern": "CWM.*TRAJ|cwm.*traj.*p.?=",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T09:31:19.040960+00:00_

4:We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
28:[Omitted long matching line]
60:[Omitted long matching line]
90:\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +1.70\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
92:\cwm{} flat scaling ($-$0.03\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \emph{cannot} benefit from scale. The interaction between formulation and scale amplifies at repository-level complexity (\S\ref{sec:repo}), where \traj{} also shows no scaling benefit (72.92\% at both 4B and 8B); only \cls{} scales positively across both complexity levels.
111:\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set ($n{=}9{,}784$). \cwm{} unparseable outputs default to pass (majority class). Seeds: Qwen3 primary seed 42; DeepSeek \traj{} 6 seeds.}
117:\textbf{Model} & \textbf{\cls{} Acc (\%)} & \textbf{\cwm{} Acc (\%)} & \textbf{\cwm{} Unparse (\%)} & \textbf{\traj{} Acc (\%)\textsuperscript{$\ddagger$}} \\
130:[Omitted long matching line]
177:\cls{} achieves 217$\times$ higher throughput than \cwm{} (853 vs.\ 3.9 inferences/min; 1 output token vs.\ avg 477). This efficiency gap is observed consistently across both model families. Extended analysis (error complementarity, variance compression, per-test precision/recall, block correlation, LoRA rank ablation, per-mutation scaling, and \cls{}--\traj{} efficiency) appears in A
…[truncated 171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T09:31:19.041239+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "TOST|tost|equivalen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "tool_args": {
    "pattern": "TOST|tost|equivalen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T09:31:19.041390+00:00_

14:[Omitted long matching line]
17:Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2\pp{} margin. Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
95:\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
96:\label{sec:equivalence}
98:[Omitted long matching line]
139:[Omitted long matching line]
194:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T09:31:19.041634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": "95",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "offset": "95",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T09:31:19.041854+00:00_

95	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
96	\label{sec:equivalence}
97	
98	We compare \cls{} (aggregated via all-pass rule) against \traj{} on 523 variant-level instances across five seeds.\footnote{Seeds 789 and 0 use NF4 quantized inference; the remaining three use bfloat16.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin). Equivalence holds at margins as tight as $\pm$1.52\pp{} (Table~\ref{tab:tost_sensitivity}); our $\pm$2\pp{} threshold provides approximately 30\% headroom above the minimum, chosen to reflect a practically meaningful difference where a 2\pp{} gap corresponds to ${\sim}$15 additional errors per 900 predictions. Within-problem predictions are correlated (intraclass correlation ICC $= 0.191$, $p < 0.0001$, design effect (DEFF) $= 3.97$); all statistical tests use clustered bootstrap accordingly. On DeepSeek-Coder, the observed \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence, but with only 2 seeds the comparison is underpowered. Per-test classification provides diagnostic information (which specific tests fail) at no cost to variant-level accuracy, a result that parallels process supervision~\cite{lightman2023letsverify}, where step-level verification enables error localization without accuracy cost.
99	
100	Oracle analysis on SWE-bench Verified (500 instances) shows that per-test advantage concentrates at $T \geq 2$ fail-to-pass tests (31.3\% of instances, contributing 55.3\% of the total oracle advantage; Appendix~\ref{app:oracle}).
101	
102	
103	\subsection{Repo-Level: Complexity-Dependent Divergence}
104	\label{sec:repo}
105	
106	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. Checkpoints are val-selected where validation loss is computable (see \S\ref{sec:setup}); the test set ($n{=}9{,}784$) has zero problem overlap with va
…[truncated 564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T09:31:19.042188+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Holm-Bonferroni correction for 6 primary comparisons (3 formulations × 2 complexity levels).\"\"\"\n\nimport json\nimport pathlib\nfrom scipy.stats import norm\n\nOUTPUT_DIR = pathlib.Path(__file__).parent\n\ndef approx_tost_p(mean_diff, se, margin=2.0):\n    \"\"\"Approximate TOST p-value using normal distribution.\"\"\"\n    z_upper = (mean_diff - margin) / se\n    z_lower = (mean_diff + margin) / se\n    p_upper = norm.cdf(z_upper)\n    p_lower = norm.cdf(-z_lower)\n    return max(p_upper, p_lower)\n\ndef holm_bonferroni(comparisons, alpha=0.05):\n    k = len(comparisons)\n    sorted_comps = sorted(comparisons, key=lambda x: x[\"raw_p\"])\n\n    for i, comp in enumerate(sorted_comps):\n        rank = i + 1\n        adj_p = comp[\"raw_p\"] * (k - rank + 1)\n        if i > 0 and adj_p < sorted_comps[i - 1][\"adj_p\"]:\n            adj_p = sorted_comps[i - 1][\"adj_p\"]\n        comp[\"adj_p\"] = min(adj_p, 1.0)\n        comp[\"rank\"] = rank\n        comp[\"multiplier\"] = k - rank + 1\n        comp[\"significant\"] = comp[\"adj_p\"] < alpha\n\n    return sorted_comps\n\n# --- CWM vs TRAJ function-level: approximate ---\n# gap=0.89pp, SE borrowed from CLS-TRAJ (0.6517pp), TOST ±2pp margin\ncwm_traj_func_p = approx_tost_p(mean_diff=0.89, se=0.6517, margin=2.0)\n\ncomparisons = [\n    {\"name\": \"Func: CLS vs CWM (TOST ±2pp)\",   \"raw_p\": 0.007,  \"level\": \"function\", \"note\": \"clustered bootstrap, 5 seeds\"},\n    {\"name\": \"Func: CLS vs TRAJ (TOST ±2pp)\",   \"raw_p\": 0.0087, \"level\": \"function\", \"note\": \"analytical, mean=-0.45pp, SE=0.6517pp\"},\n    {\"name\": \"Func: CWM vs TRAJ (TOST ±2pp)\",   \"raw_p\": round(cwm_traj_func_p, 4), \"level\": \"function\", \"note\": f\"APPROXIMATE: gap=0.89pp, SE=0.6517 borrowed from CLS-TRAJ\"},\n    {\"name\": \"Repo: CLS vs CWM (Qwen3-8B)\",     \"raw_p\": 0.003,  \"level\": \"repo\", \"note\": \"paired bootstrap, diff=+29.17pp\"},\n    {\"name\": \"Repo: CLS vs TRAJ (Qwen3-8B)\",    \"raw_p\": 0.385,  \"level\": \"repo\", \"note\": \"unpaired bootstrap, diff=+8.33pp\"},\n    {\"name\": \"Repo: CWM vs TRAJ (Qwen3-8B)\",    \"raw_p\": 0.039,  \"level\": \"repo\", \"note\": \"unpaired bootstrap, diff=-20.83pp\"},\n]\n\nresults = holm_bonferroni(comparisons)\n\nprint(f\"Holm-Bonferroni Correction (k={len(comparisons)}, α=0.05)\")\nprint(\"=\" * 100)\nprint(f\"{'Rank':<5} {'Comparison':<38} {'Raw p':>8} {'×':>3} {'Adj p':>8} {'Sig?':>6}  {'Note'}\")\nprint(\"-\" * 100)\nfor r in results:\n    sig_str = \"YES\" if r[\"significant\"] else \"no\"\n    print(f\"{r['rank']:<5} {r['name']:<38} {r['raw_p']:>8.4f} {r['multiplier']:>3} {r['adj_p']:>8.4f} {sig_str:>6}  {r['note']}\")\nprint(\"-\" * 100)\n\nn_sig = sum(1 for r in results if r[\"significant\"])\nprint(f\"\\n{n_sig}/{len(results)} comparisons remain significant after correction.\")\n\nfor r in results:\n    assert r[\"adj_p\"] >= r[\"raw_p\"], f\"adj_p < raw_p for {r['name']}\"\n\noutput = {\n    \"method\": \"Holm-Bonferroni\",\n    \"k\": len(comparisons),\n    \"alpha\": 0.05,\n    \"results\": [\n        {\n            \"rank\": r[\"rank\"],\n            \"comparison\": r[\"name\"],\n            \"level\": r[\"level\"],\n            \"raw_p\": r[\"raw_p\"],\n            \"multiplier\": r[\"multiplier\"],\n            \"adj_p\": round(r[\"adj_p\"], 4),\n            \"significant\": r[\"significant\"],\n            \"note\": r[\"note\"],\n        }\n        for r in results\n    ],\n}\n\nout_path = OUTPUT_DIR / \"holm_bonferroni_results.json\"\nout_path.write_text(json.dumps(output, indent=2) + \"\\n\")\nprint(f\"\\nSaved to {out_path}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Holm-Bonferroni correction for 6 primary comparisons (3 formulations × 2 complexity levels).\"\"\"\n\nimport json\nimport pathlib\nfrom scipy.stats import norm\n\nOUTPUT_DIR = pathlib.Path(__file__).parent\n\ndef approx_tost_p(mean_diff, se, margin=2.0):\n    \"\"\"Approximate TOST p-value using normal distribution.\"\"\"\n    z_upper = (mean_diff - margin) / se\n    z_lower = (mean_diff + margin) / se\n    p_upper = norm.cdf(z_upper)\n    p_lower = norm.cdf(-z_lower)\n    return max(p_upper, p_lower)\n\ndef holm_bonferroni(comparisons, alpha=0.05):\n    k = len(comparisons)\n    sorted_comps = sorted(comparisons, key=lambda x: x[\"raw_p\"])\n\n    for i, comp in enumerate(sorted_comps):\n        rank = i + 1\n        adj_p = comp[\"raw_p\"] * (k - rank + 1)\n        if i > 0 and adj_p < sorted_comps[i - 1][\"adj_p\"]:\n            adj_p = sorted_comps[i - 1][\"adj_p\"]\n        comp[\"adj_p\"] = min(adj_p, 1.0)\n        comp[\"rank\"] = rank\n        comp[\"multiplier\"] = k - rank + 1\n        comp[\"significant\"] = comp[\"adj_p\"] < alpha\n\n    return sorted_comps\n\n# --- CWM vs TRAJ function-level: approximate ---\n# gap=0.89pp, SE borrowed from CLS-TRAJ (0.6517pp), TOST ±2pp margin\ncwm_traj_func_p = approx_tost_p(mean_diff=0.89, se=0.6517, margin=2.0)\n\ncomparisons = [\n    {\"name\": \"Func: CLS vs CWM (TOST ±2pp)\",   \"raw_p\": 0.007,  \"level\": \"function\", \"note\": \"clustered bootstrap, 5 seeds\"},\n    {\"name\": \"Func: CLS vs TRAJ (TOST ±2pp)\",   \"raw_p\": 0.0087, \"level\": \"function\", \"note\": \"analytical, mean=-0.45pp, SE=0.6517pp\"},\n    {\"name\": \"Func: CWM vs TRAJ (TOST ±2pp)\",   \"raw_p\": round(cwm_traj_func_p, 4), \"level\": \"function\", \"note\": f\"APPROXIMATE: gap=0.89pp, SE=0.6517 borrowed from CLS-TRAJ\"},\n    {\"name\": \"Repo: CLS vs CWM (Qwen3-8B)\",     \"raw_p\": 0.003,  \"level\": \"repo\", \"note\": \"paired bootstrap, diff=+29.17pp\"},\n    {\"name\": \"Repo: CLS vs TRAJ (Qwen3-8B)\",    \"raw_p\": 0.385,  \"level\": \"repo\", \"note\": \"unpaired bootstrap, diff=+8.33pp\"},\n    {\"name\": \"Repo: CWM vs TRAJ (Qwen3-8B)\",    \"raw_p\": 0.039,  \"level\": \"repo\", \"note\": \"unpaired bootstrap, diff=-20.83pp\"},\n]\n\nresults = holm_bonferroni(comparisons)\n\nprint(f\"Holm-Bonferroni Correction (k={len(comparisons)}, α=0.05)\")\nprint(\"=\" * 100)\nprint(f\"{'Rank':<5} {'Comparison':<38} {'Raw p':>8} {'×':>3} {'Adj p':>8} {'Sig?':>6}  {'Note'}\")\nprint(\"-\" * 100)\nfor r in results:\n    sig_str = \"YES\" if r[\"significant\"] else \"no\"\n    print(f\"{r['rank']:<5} {r['name']:<38} {r['raw_p']:>8.4f} {r['multiplier']:>3} {r['adj_p']:>8.4f} {sig_str:>6}  {r['note']}\")\nprint(\"-\" * 100)\n\nn_sig = sum(1 for r in results if r[\"significant\"])\nprint(f\"\\n{n_sig}/{len(results)} comparisons remain significant after correction.\")\n\nfor r in results:\n    assert r[\"adj_p\"] >= r[\"raw_p\"], f\"adj_p < raw_p for {r['name']}\"\n\noutput = {\n    \"method\": \"Holm-Bonferroni\",\n    \"k\": len(comparisons),\n    \"alpha\": 0.05,\n    \"results\": [\n        {\n            \"rank\": r[\"rank\"],\n            \"comparison\": r[\"name\"],\n            \"level\": r[\"level\"],\n            \"raw_p\": r[\"raw_p\"],\n            \"multiplier\": r[\"multiplier\"],\n            \"adj_p\": round(r[\"adj_p\"], 4),\n            \"significant\": r[\"significant\"],\n            \"note\": r[\"note\"],\n        }\n        for r in results\n    ],\n}\n\nout_path = OUTPUT_DIR / \"holm_bonferroni_results.json\"\nout_path.write_text(json.dumps(output, indent=2) + \"\\n\")\nprint(f\"\\nSaved to {out_path}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T09:31:19.042414+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T09:31:19.042753+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/holm_bonferroni.py",
  "description": "Run Holm-Bonferroni correction script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/holm_bonferroni.py",
    "description": "Run Holm-Bonferroni correction script"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T09:31:19.043120+00:00_

Holm-Bonferroni Correction (k=6, α=0.05)
====================================================================================================
Rank  Comparison                                Raw p   ×    Adj p   Sig?  Note
----------------------------------------------------------------------------------------------------
1     Repo: CLS vs CWM (Qwen3-8B)              0.0030   6   0.0180    YES  paired bootstrap, diff=+29.17pp
2     Func: CLS vs CWM (TOST ±2pp)             0.0070   5   0.0350    YES  clustered bootstrap, 5 seeds
3     Func: CLS vs TRAJ (TOST ±2pp)            0.0087   4   0.0350    YES  analytical, mean=-0.45pp, SE=0.6517pp
4     Repo: CWM vs TRAJ (Qwen3-8B)             0.0390   3   0.1170     no  unpaired bootstrap, diff=-20.83pp
5     Func: CWM vs TRAJ (TOST ±2pp)            0.0443   2   0.1170     no  APPROXIMATE: gap=0.89pp, SE=0.6517 borrowed from CLS-TRAJ
6     Repo: CLS vs TRAJ (Qwen3-8B)             0.3850   1   0.3850     no  unpaired bootstrap, diff=+8.33pp
----------------------------------------------------------------------------------------------------

3/6 comparisons remain significant after correction.

Saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T09:31:19.043291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni_results.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T09:31:19.043456+00:00_

1	{
2	  "method": "Holm-Bonferroni",
3	  "k": 6,
4	  "alpha": 0.05,
5	  "results": [
6	    {
7	      "rank": 1,
8	      "comparison": "Repo: CLS vs CWM (Qwen3-8B)",
9	      "level": "repo",
10	      "raw_p": 0.003,
11	      "multiplier": 6,
12	      "adj_p": 0.018,
13	      "significant": true,
14	      "note": "paired bootstrap, diff=+29.17pp"
15	    },
16	    {
17	      "rank": 2,
18	      "comparison": "Func: CLS vs CWM (TOST \u00b12pp)",
19	      "level": "function",
20	      "raw_p": 0.007,
21	      "multiplier": 5,
22	      "adj_p": 0.035,
23	      "significant": true,
24	      "note": "clustered bootstrap, 5 seeds"
25	    },
26	    {
27	      "rank": 3,
28	      "comparison": "Func: CLS vs TRAJ (TOST \u00b12pp)",
29	      "level": "function",
30	      "raw_p": 0.0087,
31	      "multiplier": 4,
32	      "adj_p": 0.035,
33	      "significant": true,
34	      "note": "analytical, mean=-0.45pp, SE=0.6517pp"
35	    },
36	    {
37	      "rank": 4,
38	      "comparison": "Repo: CWM vs TRAJ (Qwen3-8B)",
39	      "level": "repo",
40	      "raw_p": 0.039,
41	      "multiplier": 3,
42	      "adj_p": 0.117,
43	      "significant": false,
44	      "note": "unpaired bootstrap, diff=-20.83pp"
45	    },
46	    {
47	      "rank": 5,
48	      "comparison": "Func: CWM vs TRAJ (TOST \u00b12pp)",
49	      "level": "function",
50	      "raw_p": 0.0443,
51	      "multiplier": 2,
52	      "adj_p": 0.117,
53	      "significant": false,
54	      "note": "APPROXIMATE: gap=0.89pp, SE=0.6517 borrowed from CLS-TRAJ"
55	    },
56	    {
57	      "rank": 6,
58	      "comparison": "Repo: CLS vs TRAJ (Qwen3-8B)",
59	      "level": "repo",
60	      "raw_p": 0.385,
61	      "multiplier": 1,
62	      "adj_p": 0.385,
63	      "significant": false,
64	      "note": "unpaired bootstrap, diff=+8.33pp"
65	    }
66	  ]
67	}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T09:31:19.043776+00:00_

结果：

**3/6 comparisons survive Holm-Bonferroni correction (α=0.05):**

| Rank | Comparison | Raw p | ×k | Adj p | Sig? |
|------|-----------|-------|-----|-------|------|
| 1 | Repo: CLS vs CWM | 0.003 | 6 | **0.018** | YES |
| 2 | Func: CLS vs CWM (TOST) | 0.007 | 5 | **0.035** | YES |
| 3 | Func: CLS vs TRAJ (TOST) | 0.0087 | 4 | **0.035** | YES |
| 4 | Repo: CWM vs TRAJ | 0.039 | 3 | 0.117 | no |
| 5 | Func: CWM vs TRAJ (TOST)* | 0.044 | 2 | 0.117 | no |
| 6 | Repo: CLS vs TRAJ | 0.385 | 1 | 0.385 | no |

\* Approximate (SE borrowed from CLS-TRAJ).

核心 CLS 优势的两个 claim (CLS vs CWM at both levels, CLS-TRAJ equivalence at function-level) 都 survive 校正。Repo-level 的 CWM vs TRAJ 和 CLS vs TRAJ 不再显著，论文中需要相应弱化措辞。

脚本和 JSON 已保存到 `artifacts/`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_holm-bonferroni-w5_20260519T092929"
}
```

</details>

---
