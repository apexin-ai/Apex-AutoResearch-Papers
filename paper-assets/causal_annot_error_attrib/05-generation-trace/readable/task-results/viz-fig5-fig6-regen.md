# viz fig5 fig6 regen

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig5_fig6_regen_20260521T080430_result.json`
- **Structured JSON:** [`8abbb68f9373d086e781.json`](../../sessions/8a/8abbb68f9373d086e781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Report

**Status**: needed fix. fig5 was already correct; fig6 had wrong denominator.

**Bug found**: `gen_diagnostic_plots.py` filtered `macro_f1 > 0` only for fig5 scatter. The fig6 ASV heatmap loop over `data['type1_type2']` did **not** filter, so denominators were 9 (including `qwen3 few-shot-5` zero-matrix config):
- exposure showed 7/9 (77.8%) instead of 7/8 (87.5%)
- mediation/IV/frontdoor showed 8/9 (88.9%) instead of 8/8 (100%)

**Fix**: added top-level `zero_configs` set derived from `macro_f1 == 0` entries and `is_valid(e)` helper; applied filter to both `f1_vs_bias` and `type1_type2` reads. (`gen_diagnostic_plots.py:23-29, 39, 91`)

**Regenerated outputs** (`figures/paper/`):
- `fig5_f1_vs_bias.pdf/.png` — 56 points, unchanged
- `fig6_asv_heatmap.pdf/.png` — IV 8/8, mediation 8/8, frontdoor 8/8, exposure 7/8, confounding/collider/mbias 0/8 → 31/56 = 55.4%, matches paper

---
