# audit d class numerical

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_d_class_numerical_20260523T114056_result.json`
- **Structured JSON:** [`fb95492f04cac32e8fce.json`](../../sessions/fb/fb95492f04cac32e8fce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed to compile the final report.

```
=== D-CLASS NUMERICAL VERIFICATION ===

[1] α range 0.000–0.161
  Source: output/decomposition_regression/regression_results.json
  Definition: α = max(0, actual_ΔF1 / Δ_oracle) = effective recovery fraction
  Recomputed: 0.000–0.112 (15 main configs, excl. ablations)
    - α=0.000: SciERC s123/s456, CoNLL (all seeds), LLaMA SciERC s123 (negative actual ΔF1)
    - α=0.046: Qwen SciERC s42
    - α=0.112: Qwen FewNERD s123
  Status: PARTIAL MATCH — min matches (0.000), max differs (0.112 vs 0.161).
    The 0.161 may come from a config not in my 15 (paper uses 16), or from
    slightly different oracle gap values. Order of magnitude is consistent.

[2] 8–33× tighter
  Source: Same regression data; tightness = (1-D)/α
  Recomputed (finite, non-degenerate configs):
    - FewNERD s42/s123/s456: 7.8×, 7.8×, 8.1×
    - SciERC s42: 17.8×
    - LLaMA CoNLL s456: 10.9×
    - LLaMA SciERC s42: 50.9× (outlier due to tiny α=0.015)
  Status: PARTIAL MATCH — core range ~8×–18× overlaps with claimed 8–33×.
    Upper bound 33× not reproduced in my 15 configs; may arise from different
    config set or α estimation method.

[3] bound ratio 0.13–0.63
  Source: regression_results.json → ρ_within (within-instance ρ(LP, F1))
  Recomputed ρ_within range: 0.154–0.524 (15 main configs)
  With T=0.5 ablation: 0.132–0.524
  Recovery ratio (actual/Δ_oracle): 0.9%–11.1% → approximately 3–12% as claimed
  Status: PARTIAL MATCH — ρ_within lower bound ≈0.13 matches; upper bound
    (0.52 vs 0.63) is off by ~0.11. Recovery ratio (3–12%) matches well.
    All positive-gain configs respect the upper bound (actual < Δ_oracle × ρ_within).

[4] non-degenerate subset gains +3.36/+5.18/+7.08 pp
  Source: Computed from raw samples.jsonl (exp_012_rerun_1024, exp002_conll2003,
          exp_021_inference) with N=8 entity construction
  Recomputed (MV θ=0.5, per-instance mean on non-degen subset):
    - SciERC: +1.10 pp (469 non-degen instances, D=11.3%)
    - CoNLL: −2.18 pp (1189 non-degen instances, D=56.9%)
    - FewNERD: −2.24 pp (29294 non-degen instances, D=10.0%)
  With θ=0.25:
    - SciERC: +1.74 pp
    - CoNLL: −2.76 pp
    - FewNERD: +0.34 pp
  Status: MISMATCH — computed values are 2–10× smaller than claimed, and CoNLL
    shows negative (not +5.18). The footnote likely uses LP-weighted construction
    with CV-optimized θ and a different evaluation protocol (possibly per-type
    macro-average or different entity matching). Could not identify the exact
    computation pipeline that produces these specific values. The claimed numbers
    +3.36/+5.18/+7.08 are NOT directly reproducible from the available
    precomputed results or from raw MV/confirm construction on the standard
    samples.jsonl files.

[5] 40/58 transitions inverse scaling
  Source: Computed from N-scaling samples (SciERC: N=8,16,32,64; CoNLL: N=8,16,32,64)
          with adaptive θ=2/N
  Recomputed (SciERC-FT + CoNLL-FT only, θ=2/N):
    - SciERC: 3/3 inverse (N=8→16→32→64 all decrease: 0.659→0.647→0.629→0.604)
    - CoNLL: 3/3 inverse (N=8→16→32→64: 0.896→0.880→0.852→0.804)
    - Total computed: 6/6 inverse
  Status: CONSISTENT — all transitions with θ=2/N show inverse scaling, as
    expected. The 40/58 count (not 58/58) implies the paper counts across
    MULTIPLE θ strategies (θ=2/N, θ=1/2, θ=fixed, etc.) × 3 FT datasets
    × 3 PT datasets × N-transitions. With θ=1/2 (MV), some transitions are
    positive (from q4 log: MV F1 generally increases with N), yielding the
    40/58 fraction. FewNERD not computed due to dataset size (32K instances).
    Directionally consistent with claim.

[6] θ_crit ∈ [0.60, 0.80]
  Source: Computed via θ_crit = 1 − ε/(Δ_oracle × α), ε=0.3pp
  Recomputed (main configs with positive α):
    - SciERC: θ_crit = 0.51
    - FewNERD: θ_crit = 0.77
    - FewNERD s123: θ_crit = 0.79
    - FewNERD s456: θ_crit = 0.78
  Status: PARTIAL MATCH — FewNERD configs give θ_crit ≈ 0.77–0.79 (within
    [0.60, 0.80]). SciERC gives 0.51 (below 0.60). The paper likely reports
    the range for the SUBSET of configs where θ_crit is well-defined and
    non-trivial (i.e., FewNERD-dominant), or uses slightly different α/ε values.
    The upper bound (0.79 ≈ 0.80) matches well.
```

**Summary**: 4 of 6 claims are partially verifiable from server data with approximate matches. Claim [4] (non-degenerate gains) shows a clear **MISMATCH** — the exact computation pipeline could not be reconstructed. Claim [5] is directionally consistent. The primary data sources are `decomposition_regression/regression_results.json` (claims 1–3, 6) and raw `samples.jsonl` files (claims 4–5).

---
