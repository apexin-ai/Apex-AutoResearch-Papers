# paper scaling section dual narrative

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_scaling-section-dual-narrative_20260519T200611.jsonl`
- **Structured JSON:** [`c2df9cb6d7b8177852dd.json`](../../sessions/c2/c2df9cb6d7b8177852dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-19T20:07:16.811953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T20:07:16.812348+00:00_

1	%% Draft: Zero-shot / Scaling paragraph for \S5.5 (Scaling Behavior)
2	%% Exp ID: exp_qwen25_72b_zeroshot (all 72B ZS numbers)
3	%% Status: Draft for Paper Agent integration. Replaces current \S5.5 content.
4	%% Pending: 7B/14B/32B FT results for full scaling curve; 72B FT for regime disentanglement.
5	
6	\subsection{Scaling Behavior}
7	\label{sec:scaling}
8	
9	To test whether the correlation-selection gap is specific to fine-tuned models, we evaluate Qwen2.5-72B-Instruct (AWQ 4-bit) in a zero-shot setting across all three primary datasets ($N{=}8$, $T{=}1.0$, no task-specific training).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Fine-tuned 8B vs.\ zero-shot 72B: QE correlations and entity construction ($N{=}8$, $T{=}1.0$). Degen.\ = instance degeneracy (\%). Constr.\ = LP-weighted entity construction $\Delta$F1 vs.\ greedy (pp). $^\dagger$Majority voting (uniform weights).}
15	\label{tab:zs_72b}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llcccccr@{}}
18	\toprule
19	Dataset & Regime & Greedy & Degen. & LP $\rho$ & SJ $\rho$ & VC $\rho$ & Constr. \\
20	\midrule
21	SciERC & 8B FT  & .645 & 17.8\% & .205 & .360 & .379 & $+$1.02 \\
22	       & 72B ZS & .399 & 21.0\% & .081 & .217 & .277 & $+$1.53 \\
23	\midrule
24	Few-NERD & 8B FT & .748 & 13.0\% & .220 & .380 & --- & $+$1.40 \\
25	         & 72B ZS & .628 & 46.2\% & .119 & .345 & .416 & $-$0.20 \\
26	\midrule
27	CoNLL  & 8B FT  & .908 & 61.7\% & .302 & .436 & .424 & $-$0.39 \\
28	       & 72B ZS & .712 & 67.7\% & $-$.002 & .304 & .297 & $-$0.37 \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\paragraph{LP requires fine-tuning calibration.}
34	Table~\ref{tab:zs_72b} compares QE correlations between regimes.
35	LP $\rho$ drops to near zero in the zero-shot setting: from $0.205$ to $0.081$ on SciERC, $0.220$ to $0.119$ on Few-NERD, and $0.302$ to $-0.002$ on CoNLL.
36	Fine-tuning calibrates the model's token-level confidence to task-specific quality gradients; without this calibrat
…[truncated 2836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T20:07:16.812553+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T20:07:16.812734+00:00_

3seed_ner_summary.md
3seed_summary
72b_zeroshot_signal_summary.json
__pycache__
_project
analysis_dgs_epoch_rank.py
analysis_fk_bootstrap_ci_full.json
analysis_lp_range_cdf.json
analysis_lp_range_cdf_n16_3seed.json
analysis_scierc_n16_3seed_selection_f1.json
analysis_scierc_re_n16_3seed_selection_f1.json
analysis_unified_rho.json
analysis_unified_rho_full.json
analyze_exp004_re_diagnostic.py
analyze_exp004_v2_re_diagnostic.py
analyze_exp005_v2_temperature.py
analyze_exp015_metrics_expansion.py
analyze_exp016_ensemble.py
analyze_ood_signals.py
audit_autodl5090_loop3.md
audit_gpu5090_4x2_loop3.md
auroc_bug_diagnosis.md
autodl_process_check.md
batch_completion_check_a.md
batch_completion_check_b.md
bertoldi_citation_check
bjb1_status_report.md
bootstrap_ci_nscaling
bootstrap_ci_summary.json
bootstrap_ci_tables.tex
bootstrap_construction.py
bootstrap_selection_test.py
ccs_selection.py
claim_audit_report.md
claim_audit_v2.json
compute_signals.py
consistency.py
d072_paper_patch_inventory.md
d108
d108_lp_vc_combination
d112
d112_claim_audit
d113_table2_fix
d113_table2_narrative_fix
d140
d140_oracle_gated_analysis.py
d141_data_fix_rerun_v2_report.md
d141_eval_unify
d141_v2_fix
d146_epoch_scierc_rho
d146_span_revert
data
data_utils.py
deberta_verifier.py
deberta_verifier_5fold.py
deberta_verifier_5fold_results.json
deberta_verifier_results.json
degen_gated
degeneracy_lp_scatter.pdf
degeneracy_lp_scatter.png
dgs_results
dream_reports
entity_construction.py
entity_construction_fair.py
entity_token_lp
evaluate_verifier.py
evaluation.py
exp-001
exp-015
exp-019
exp-022
exp001_postprocess.py
exp005_temperature
exp009_stratification_analysis.py
exp010_selection_curves
exp027_mlp_v2
exp_001
exp_001_n16
exp_001_ner_n16_scierc
exp_001_seed456_v2_ner
exp_002
exp_003
exp_004_re_diagnostic
exp_004_v2
exp_005
exp_005_v2
exp_007_llama_scierc_seed123
exp_009_capability_stratification
exp_009_v2
exp_009_v2_re_rerun
exp_009_v2_stratification.py
exp_010_selection_curves
exp_011_ood_scierc_to_c
…[truncated 2916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T20:07:16.812941+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex",
  "content": "%% Version A: Monotonic scaling narrative (7B < 14B < 32B degeneracy)\n%% Use condition: Qwen2.5 FT results show degeneracy rising monotonically with scale.\n%% Status: Placeholder framework — fill numbers when exp results arrive.\n\n%% ---- Placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\n%% ---- Narrative ----\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.39$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex",
    "content": "%% Version A: Monotonic scaling narrative (7B < 14B < 32B degeneracy)\n%% Use condition: Qwen2.5 FT results show degeneracy rising monotonically with scale.\n%% Status: Placeholder framework — fill numbers when exp results arrive.\n\n%% ---- Placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\n%% ---- Narrative ----\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.39$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T20:07:16.813169+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T20:07:16.813340+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_B_nonmonotonic.tex",
  "content": "%% Version B: Non-monotonic scaling narrative (some scale point breaks monotonicity)\n%% Use condition: Qwen2.5 FT results show degeneracy does NOT rise monotonically with scale.\n%% Status: Placeholder framework — fill numbers when exp results arrive.\n\n%% ---- Placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\n%% ---- Narrative ----\n\n\\paragraph{Degeneracy is not a simple function of scale.}\nWe fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy does not increase monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a), indicating that model-specific factors beyond raw scale---such as pretraining data composition or architecture choices within the Qwen2.5 family---modulate the capability--diversity tradeoff.\nNonetheless, the gating relationship between degeneracy and construction effectiveness remains intact: LP-weighted construction $\\Delta$F1 tracks degeneracy rather than parameter count ($\\scaleSevenConstr$, $\\scaleFourteenConstr$, $\\scaleThirtytwoConstr$\\,pp), with the largest gains at the scale point exhibiting lowest degeneracy regardless of model size.\n\nThis result reframes degeneracy as a \\emph{diagnostic} rather than a predictable consequence of scaling.\nThe epoch dimension reinforces this view: extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), showing that training choices can shift degeneracy as much as a $4{\\times}$ increase in parameters.\nThe practical implication is that practitioners should measure degeneracy post-hoc rather than predict it from model size: a mid-scale model with favorable output diversity may benefit more from self-consistency aggregation than a larger model whose samples have collapsed.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_B_nonmonotonic.tex",
    "content": "%% Version B: Non-monotonic scaling narrative (some scale point breaks monotonicity)\n%% Use condition: Qwen2.5 FT results show degeneracy does NOT rise monotonically with scale.\n%% Status: Placeholder framework — fill numbers when exp results arrive.\n\n%% ---- Placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\n%% ---- Narrative ----\n\n\\paragraph{Degeneracy is not a simple function of scale.}\nWe fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy does not increase monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a), indicating that model-specific factors beyond raw scale---such as pretraining data composition or architecture choices within the Qwen2.5 family---modulate the capability--diversity tradeoff.\nNonetheless, the gating relationship between degeneracy and construction effectiveness remains intact: LP-weighted construction $\\Delta$F1 tracks degeneracy rather than parameter count ($\\scaleSevenConstr$, $\\scaleFourteenConstr$, $\\scaleThirtytwoConstr$\\,pp), with the largest gains at the scale point exhibiting lowest degeneracy regardless of model size.\n\nThis result reframes degeneracy as a \\emph{diagnostic} rather than a predictable consequence of scaling.\nThe epoch dimension reinforces this view: extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), showing that training choices can shift degeneracy as much as a $4{\\times}$ increase in parameters.\nThe practical implication is that practitioners should measure degeneracy post-hoc rather than predict it from model size: a mid-scale model with favorable output diversity may benefit more from self-consistency aggregation than a larger model whose samples have collapsed.\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T20:07:16.813511+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_B_nonmonotonic.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-19T20:07:16.813676+00:00_

两版已写入 artifacts/：

- **Version A**（单调）：degeneracy 随 scale 单调上升 → "selection window narrows" 叙事，与 epoch/family 两维证据汇合，三维一致性支撑 degeneracy 作为 robust diagnostic。
- **Version B**（非单调）：degeneracy 不随 scale 单调变化 → 重新定位 degeneracy 为 post-hoc diagnostic 而非 scaling 的可预测结果，弱化 "narrows with scale" 说法，转向 "practitioners should measure rather than predict"。

两版共享同一套 `\newcommand` placeholder，数据到位后替换即可。每版约 5-6 句，匹配现有 `zeroshot_scaling_draft.tex` 的 `\paragraph{}` 风格和数据密度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_scaling-section-dual-narrative_20260519T200611"
}
```

</details>

---
