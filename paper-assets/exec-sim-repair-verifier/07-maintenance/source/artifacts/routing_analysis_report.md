# Routing Heuristic Analysis: CLS vs CWM Formulation Routing

**Date**: 2026-05-22
**Type**: Post-hoc analysis (no model training)
**Data**: 1,890 function-level per-test predictions, 7 prediction files (3 CLS, 4 CWM), 12 CLS-CWM pairs analyzed

---

## Data Inventory

| Model | Seed | File | Acc (%) | n |
|-------|------|------|---------|---|
| CLS 4B | 0 | predictions_cls_seed0.jsonl | 87.78 | 1890 |
| CLS 8B | 42 | cls8b_seed42_predictions.json | 90.48 | 1890 |
| CLS 8B | 123 | cls8b_seed123_predictions.json | 89.37 | 1890 |
| CWM 4B | 42 | eval_results_bf16_predictions.json | 87.51 | 1890 |
| CWM 4B | 123 | predictions_cwm_seed123.jsonl | 87.30 | 1890 |
| CWM 4B | 789 | predictions_cwm_seed789.jsonl | 86.67 | 1890 |
| CWM 4B | 123v2 | eval_cwm_seed123_with_preds_predictions.json | 87.20 | 1890 |

**Missing data**: No CWM 8B per-instance predictions. No TRAJ per-test predictions (TRAJ operates at variant level). No confidence/logit scores for any model. Repo-level CWM predictions not available (CWM ~58% accuracy at repo-level makes routing moot).

---

## Oracle Complementarity (Reference)

| Pair Type | Best Single (%) | Oracle (%) | Gap (pp) | Error Complementarity (%) |
|-----------|----------------|------------|----------|--------------------------|
| 4B CLS vs 4B CWM | 87.78 | 89.84–90.16 | +2.0–2.4 | 31–34% |
| 8B CLS vs 4B CWM | 89.37–90.48 | 93.07–94.44 | +3.7–4.0 | 53–59% |

Error complementarity is higher for 8B-vs-4B pairs because the 8B CLS makes different errors than 4B CWM, creating more room for oracle ensemble.

---

## Heuristic 1: Complexity-Based Routing (Test Count T)

**Design**: T=1 → use CWM; T≥2 → use CLS (motivated by SWE-bench F2P distribution where 68.7% of instances have T=1).

**Result: Inapplicable to function-level dataset.**

All 114 problems have T≥6 tests (mean ≈16.6 tests/problem), so every instance falls in the T≥6 bin. The routing degenerates to always-CLS:

| Pair | Routed Acc (%) | Best Single (%) | Gain (pp) |
|------|---------------|-----------------|-----------|
| All 12 pairs | = Best Single | 87.78–90.48 | **+0.00** |

**Bootstrap 95% CI**: [0.00, 0.00] for all 8B pairs; [-0.74, 0.00] for 4B pairs (slightly negative when CWM is picked for nonexistent T=1 bin).

**Interpretation**: This heuristic is designed for heterogeneous test-count distributions (SWE-bench: T=1 to T≥50). The function-level benchmark has uniform high-T problems, so there is no routing signal. The heuristic remains theoretically valid for deployment on SWE-bench-like tasks but cannot be empirically validated with function-level data alone.

---

## Heuristic 2: Level-Based Routing

**Design**: Function-level → use CWM (equivalent accuracy, richer diagnostic output); Repo-level → use CLS (dramatically higher accuracy + throughput).

| Level | CLS Acc (%) | CWM Acc (%) | Gap (pp) | Recommendation |
|-------|------------|------------|----------|----------------|
| Function (4B mean) | 88.43 | 87.19 | +1.24 | Either (TOST equivalent) |
| Function (8B mean) | 89.39 | 86.96 | +2.43 | CLS |
| Repo (8B mean) | 84.56 | 58.57 | +25.99 | CLS |

**Result**: Trivially correct for repo-level (CWM is unusable). At function-level, the CLS-CWM gap is 1.24pp (4B) to 2.43pp (8B) — small but potentially meaningful with 8B.

**This heuristic captures 0pp of oracle complementarity** — it's a static assignment, not instance-level routing. Its value is practitioner guidance (which formulation to deploy), not accuracy improvement.

---

## Heuristic 3: Mutation-Type Routing

**Design**: For each mutation type, route to whichever formulation has higher accuracy on that type (oracle on mutation type, not on individual instances).

### Per-Mutation Accuracy (representative pair: CLS 4B s0 vs CWM 4B s42)

| Mutation Type | n | CLS (%) | CWM (%) | Winner | Gap (pp) |
|--------------|---|---------|---------|--------|----------|
| return_value | 402 | 97.51 | 97.26 | CLS | 0.25 |
| variable_swap | 85 | 94.12 | 92.94 | CLS | 1.18 |
| boundary_removal | 36 | 91.67 | 91.67 | tie | 0.00 |
| original | 398 | 86.43 | 84.17 | CLS | 2.26 |
| operator_swap | 298 | 86.24 | 87.92 | CWM | 1.68 |
| off_by_one | 671 | 82.41 | 82.56 | CWM | 0.15 |

### Routing Accuracy Across All Pairs

| Pair | Best Single (%) | Routed (%) | Gain (pp) | Oracle (%) | Oracle Gap (pp) |
|------|----------------|------------|-----------|------------|----------------|
| CLS 4B s0 vs CWM 4B s42 | 87.78 | 88.10 | **+0.32** | 90.16 | 2.06 |
| CLS 4B s0 vs CWM 4B s123 | 87.78 | 88.15 | **+0.37** | 89.84 | 1.69 |
| CLS 4B s0 vs CWM 4B s789 | 87.78 | 88.04 | **+0.26** | 89.79 | 1.75 |
| CLS 4B s0 vs CWM 4B s123v2 | 87.78 | 88.04 | **+0.26** | 89.84 | 1.80 |
| CLS 8B s42 vs CWM 4B s42 | 90.48 | 90.58 | +0.10 | 94.44 | 3.86 |
| CLS 8B s42 vs CWM 4B s123 | 90.48 | 90.48 | +0.00 | 94.39 | 3.92 |
| CLS 8B s42 vs CWM 4B s789 | 90.48 | 90.48 | +0.00 | 94.23 | 3.76 |
| CLS 8B s42 vs CWM 4B s123v2 | 90.48 | 90.48 | +0.00 | 94.34 | 3.86 |
| CLS 8B s123 vs CWM 4B s42 | 89.37 | 89.68 | +0.31 | 93.33 | 3.65 |
| CLS 8B s123 vs CWM 4B s123 | 89.37 | 89.58 | +0.21 | 93.17 | 3.59 |
| CLS 8B s123 vs CWM 4B s789 | 89.37 | 89.37 | +0.00 | 93.07 | 3.70 |
| CLS 8B s123 vs CWM 4B s123v2 | 89.37 | 89.52 | +0.15 | 93.23 | 3.70 |

**Mean routing gain**: +0.16pp (range: 0.00 to +0.37pp)
**Mean oracle gap remaining**: 2.88pp

### Bootstrap 95% CI (Routing Gain over Best Single)

| Pair | Mean (pp) | 95% CI | % Positive |
|------|-----------|--------|------------|
| CLS 4B s0 vs CWM 4B s42 | +0.22 | [-0.48, +0.79] | 73.9% |
| CLS 4B s0 vs CWM 4B s123 | +0.33 | [-0.32, +0.90] | 82.8% |
| CLS 4B s0 vs CWM 4B s789 | +0.26 | [-0.16, +0.69] | 86.3% |
| CLS 8B s42 vs CWM 4B s42 | +0.10 | [-0.48, +0.69] | 60.6% |
| CLS 8B s123 vs CWM 4B s42 | +0.14 | [-0.48, +0.79] | 64.1% |

**No pair achieves statistical significance** (all CIs include 0).

### Why Mutation-Type Routing Fails for 8B CLS

When CLS is 8B (90.48%), it dominates CWM (4B, 87.51%) on **every** mutation type. There is no mutation type where CWM beats 8B CLS, so routing reverts to always-CLS (gain = 0.00pp). The mutation-type routing only helps when formulations are close in overall accuracy (4B vs 4B: +0.26–0.37pp).

---

## Heuristic 3b: Confidence-Based Routing

**Status: Not possible.** No logit or confidence scores were saved during inference. The prediction files contain only hard labels (pass/fail). To enable this heuristic, future inference runs would need to output token-level logits or calibrated confidence scores.

---

## Key Conclusions

1. **Oracle complementarity is real but not capturable by simple heuristics.** The oracle CLS∪CWM ensemble gains 2.0–4.0pp over best single formulation, but error complementarity (31–59%) is distributed across diverse, instance-specific patterns — not systematic features like test count or mutation type.

2. **Complexity-based routing (H1) is inapplicable** to the function-level benchmark (uniform T≥6). It remains valid in principle for SWE-bench-like distributions where T varies from 1 to 50+.

3. **Level-based routing (H2) is trivially correct** for repo-level (CWM unusable at 58.57%). At function-level, it reduces to a deployment choice, not an accuracy-improving strategy.

4. **Mutation-type routing (H3) captures ≤0.37pp** of the 2–4pp oracle gap. The gain is not statistically significant (all bootstrap CIs include 0). When the stronger model (8B CLS) dominates across all mutation types, the gain drops to 0.

5. **Implication for paper**: The oracle gap represents genuinely complementary error patterns between formulations — errors that are diverse and instance-specific rather than predictable from observable features. A learned routing model (e.g., trained on validation-set error patterns) might capture more of this gap, but this would add model complexity inconsistent with the paper's focus on formulation comparison. The oracle results should be reported as an **upper bound** on ensemble potential, with explicit acknowledgment that simple heuristics do not close the gap.

---

## Data for Paper

If reporting these results, the key numbers are:

> Simple routing heuristics (test-count threshold, task-level assignment, mutation-type oracle) capture at most 0.4 pp of the 2–4 pp oracle gap between CLS and CWM, and this gain is not statistically significant (bootstrap 95% CI includes zero for all 12 formulation pairs tested). The complementarity between formulations is driven by instance-specific error patterns rather than systematic features observable before inference.

---

## Files

- **Analysis script**: `routing_analysis.py` (on server at `/home/sonny/exec-sim-repair-verifier/routing_analysis.py`)
- **Raw results JSON**: `routing_analysis_results.json` (on server)
- **This report**: `artifacts/routing_analysis_report.md`
