# code d134 analysis dryrun

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d134-analysis-dryrun_20260518T232704_result.json`
- **Structured JSON:** [`69557065ce79fbcaed1a.json`](../../sessions/69/69557065ce79fbcaed1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run completed successfully. Here's the full report:

---

## Dry-Run Report

### 1. Script status
`/root/solver-trace-ablation/scripts/d134_analysis.py` (587 lines) exists and is fully functional. Must use `/root/miniconda3/bin/python3` (not system python).

### 2. Data availability

| Seed | ISR eval | ISR classify | Random eval | Random classify |
|------|----------|-------------|-------------|-----------------|
| s47  | YES | YES | YES | YES |
| s48  | YES | YES | YES | YES |
| s49  | YES | YES | YES | YES |
| s50  | YES | YES | **NO** | **NO** |
| s51  | YES | YES | **NO** | **NO** |

Current: **5 ISR + 3 Random**. Random s50 still training, s51 not started.

### 3. Dry-run: SUCCESS

All statistical tests ran without error. Output includes per-seed table + condition summary + 4 statistical tests + BCa CIs + appendix-ready markdown.

### 4. Key statistical results (5 ISR vs 3 Random)

| Test | Statistic | p-value |
|------|-----------|---------|
| Fisher exact (H7 domination) | OR = inf, 95% CI [1.20, inf] | **0.018** |
| Mann-Whitney U (H7 rate) | U=15.0, r=1.000 | **0.018** |
| Permutation (genuine rate) | Δ = -1.40 pp | 0.784 (n.s.) |
| Bayes Factor (H7 dom) | BF10 = 21.00 | strong evidence for H1 |

- ISR: **5/5** seeds H7-dominated (85.6-100.0%)
- Random: **0/3** seeds H7-dominated (0.0-20.0%)
- BCa 95% CI: ISR H7% [85.4, 96.7], Random H7% [1.1, 20.0]

### 5. ISR* extraction

**Not handled by this script.** The script reads classify.json for taxonomy data only. eval_results.json contains `summary.mean_isr`, `summary.proved_only_mean_isr`, `summary.prove_rate` etc., but d134_analysis.py does not extract or report these. If ISR* values are needed in the output, that would require adding a feature.

### 6. BF10: Implemented

Beta-Binomial conjugate with Beta(1,1) prior. BF10=21.00 with standard interpretation thresholds (>10 = strong).

### 7. Concerns

- **Random s49 PR=5** (only 5/100 proved). This is a severe outlier that inflates Random PR SD to 49.7. With s50/s51 added, this may wash out or remain concerning. Worth noting in the paper.
- **Genuine rate is non-significant** (ISR 2.3% vs Random 3.7%, p=0.784). ISR training does not improve genuine reasoning; it just shifts the hacking pattern from H1 to H7.

### 8. Output format

Generates appendix-ready markdown with LaTeX-compatible escaping (`\\%`, `$p$`, `$\infty$`). Tables A1 (per-seed) and A2 (condition summary) plus 4 numbered statistical test blocks. Ready to paste into paper appendix.

### 9. Missing features: None critical

The script covers Fisher, Mann-Whitney, permutation, BCa bootstrap, and BF10. The only gap is ISR* value reporting from eval_results.json, which may or may not be needed depending on paper structure.

---
