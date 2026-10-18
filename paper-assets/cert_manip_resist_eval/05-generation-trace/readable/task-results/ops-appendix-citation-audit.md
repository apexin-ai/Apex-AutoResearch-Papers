# ops appendix citation audit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_appendix-citation-audit_20260525T090628_result.json`
- **Structured JSON:** [`031afa53369cf6da5cba.json`](../../sessions/03/031afa53369cf6da5cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All previously orphan labels now have main-text references:
- `app:crossed_re` → results.tex
- `app:diversity_capability` → analysis.tex
- `app:aggregation_k5`, `app:aggregation_k7` → results.tex
- `app:oracle` → analysis.tex
- `app:panel_selection` → analysis.tex
- `app:kappa_regime`, `app:shannon_entropy` → analysis.tex
- `app:attacks` → methodology.tex
- `app:extended_analysis` → results.tex

---

## Summary

### (a) Appendix inventory

**appendix.tex** — 23 sections/subsections:

| # | Label | Content |
|---|-------|---------|
| 1 | `app:proof` | Proof of Proposition (weakest-link monotonicity) |
| 2 | `app:robustness_methods` | Clustered SE, mixed effects, wild cluster bootstrap details |
| 3 | `app:crossed_re` | Crossed random effects analysis + `tab:crossed_re` |
| 4 | `app:extended_analysis` | Parent section for subsections 5–9 + `fig:dominance_heatmap` |
| 5 | `app:bft_reversal` | BFT reversal mechanism evidence + `fig:gam_split` |
| 6 | `app:diversity_capability` | Diversity–capability tradeoff structural analysis |
| 7 | `app:aggregation_details` | Aggregation mechanism details + `fig:aggregation` |
| 8 | `app:aggregation_k5` | Aggregation at K=5 + `tab:aggregation_k5` |
| 9 | `app:aggregation_k7` | Aggregation at K=7 + `tab:aggregation_k7` |
| 10 | `app:oracle` | Metric robustness under partial panel information |
| 11 | `app:panel_selection` | Panel selection strategy comparison |
| 12 | `app:forest_plot` | Clustered standard error analysis |
| 13 | `app:robustness_checks` | Subsampling and specification robustness + `tab:robustness_checks` |
| 14 | `app:random_subsample` | Random subsample analysis |
| 15 | `app:attacked_keff` | Attacked K_eff stability + `tab:attacked_keff` |
| 16 | `app:sensitivity` | Cinelli–Hazlett sensitivity + `tab:sensitivity` + `fig:sensitivity_contour` |
| 17 | `app:cross_benchmark` | Cross-benchmark prediction robustness |
| 18 | `app:sensitivity_poolA` | Pool A sensitivity + `tab:sensitivity_poolA` + `tab:poolA_power` |
| 19 | `app:epsilon` | Epsilon sensitivity analysis |
| 20 | `app:temperature` | Temperature sensitivity pilot |
| 21 | `app:keff_dist` | K_eff distribution statistics + `tab:keff_dist` |
| 22 | `app:power_analysis` | Power analysis + `tab:mde` |
| 23 | `app:alt_diversity` | Alternative diversity measures + `tab:alt_diversity` |
| 24 | `app:kappa_regime` | κ-diversity predictor shift + `tab:kappa_regime` |
| 25 | `app:shannon_entropy` | Shannon MI entropy comparison + `tab:shannon_shift` |
| 26 | `app:copula_gof` | Gaussian copula GoF and K_eff robustness |
| 27 | `app:quant_dummy` | Quantization dummy regression |
| 28 | `app:bayesian_entropy` | Bayesian posterior concentration analysis |
| 29 | `app:monte_carlo` | Monte Carlo calibration of wild cluster bootstrap |

**appendix_attacks.tex** — 3 sections:

| # | Label | Content |
|---|-------|---------|
| 30 | `app:attacks` | Attack prompt templates + `tab:attack-templates` |
| 31 | `app:attack_details` | Implementation details + `tab:attack-params` |
| 32 | `app:ai-assistants` | Use of AI assistants disclosure |

### (b) Previously orphan items — where references were added

| Orphan | File | What was added |
|--------|------|---------------|
| `app:crossed_re` | results.tex:11 | "A crossed random-effects analysis accounting for the multi-membership structure of shared judges confirms $K_{\mathrm{eff}}$ significance at $K{\geq}5$..." |
| `app:diversity_capability` | analysis.tex:15 | "The structural mechanism---maximizing diversity forces sampling across capability tiers, systematically introducing weaker judges---is detailed in Appendix~\ref{...}." |
| `app:aggregation_k5` | results.tex:89 | "At $K{=}5$, all four methods converge to identical $K_{\mathrm{eff}}$ significance (7/12; Appendix~\ref{...})..." |
| `app:aggregation_k7` | results.tex:89 | "...at $K{=}7$, methods diverge again, with Bayesian neutralization returning while threshold voting strengthens (Appendix~\ref{...})." |
| `app:oracle` | analysis.tex:28 | "...$\eta_{\max}$ retains predictive power even under partial panel information (Appendix~\ref{...})." |
| `app:panel_selection` | analysis.tex:28 | "(Figure~\ref{fig:panel_design}; full strategy comparison in Appendix~\ref{...})" |
| `app:kappa_regime` | analysis.tex:31 | "$\kappa$-diversity decreases ($8 \to 7 \to 6$/12; Appendix~\ref{...})" |
| `app:shannon_entropy` | analysis.tex:31 | "Shannon MI entropy shows a third pattern ($4 \to 4 \to 0$; Appendix~\ref{...})" |
| `app:attacks` | methodology.tex:12 | Changed `\ref{app:attack_details}` → `\ref{app:attacks}` (parent section covers subsection) |
| `app:extended_analysis` | results.tex:54 | Changed bare "Appendix" → "Appendix~\ref{app:extended_analysis}" |

### (c) Appendix content suggested for deletion

`app:ai-assistants` (Use of AI Assistants) — This is a standalone disclosure section. For EMNLP 2026 / ARR, AI assistant disclosures go in the OpenReview submission form, not in the paper itself. It has no main-text reference and no natural place to reference it from. **Recommend either deleting it or keeping it as-is** — it's a low-stakes item that reviewers won't penalize either way.

No other appendix content warrants deletion — all items support claims made in the main text.

### (d) Existing reference quality improvements

One fix applied:
- **results.tex:54** — Changed `"(per-condition detail in Figure~\ref{fig:dominance_heatmap}, Appendix)"` (bare "Appendix" with no label) to `"(per-condition breakdown in Figure~\ref{fig:dominance_heatmap}, Appendix~\ref{app:extended_analysis})"`.

The existing reference `Appendix~\ref{app:alt_diversity}` in analysis.tex was previously used as a catch-all for all alternative diversity results. Now it's repositioned as the pooled comparison, with the specific K-dependent trajectory comparisons pointing to their dedicated appendix sections (`app:kappa_regime`, `app:shannon_entropy`).

`fig:sensitivity_contour` has no separate main-text reference, but it resides inside `app:sensitivity` which is well-referenced from analysis.tex with clear context. No fix needed.

---
