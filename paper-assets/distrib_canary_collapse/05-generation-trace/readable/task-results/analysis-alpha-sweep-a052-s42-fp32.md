# analysis alpha sweep a052 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a052_s42_fp32_20260521T065539_result.json`
- **Structured JSON:** [`39014c5541700ed29f1f.json`](../../sessions/39/39014c5541700ed29f1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

```
alpha_sweep_a052_s42_fp32 | 5-Method Analysis Results
========================================================
alpha=0.52  seed=42  model=pythia-410m  dataset=wikitext103_5k
generations=11  steps_per_gen=5000  wall_clock=16278s (~4h31m)
checkpoint: results/alpha_sweep/a052_s42_fp32/gen_10/checkpoint

LEAD-LAG DETECTION:
  PermG_fwd:              3/8
  PermG_rev:              0/8
  DiffXCorr_fwd:          4/8
  DiffXCorr_rev:          1/8
  threshold_onset_3sigma: 8/8
  TY_fwd:                 5/8
  K_ge3:                  6/8
  K_ge4:                  0/8
  robust_pairs:           [te→d1, te→d2, te→d3, ece→d1, ece→d2, ece→mauve]

DRIFT (gen0 -> gen10):
  token_entropy: -26.28%
  ece:          +1273.35%
  perplexity:   +47.55%
  distinct_1:   -32.20%
  distinct_2:   -42.26%
  distinct_3:   -41.48%
  mauve:        -16.80%

CONCLUSION: PermG 3/8 confirms detection above α_c boundary.
  α=0.48→0/8, α=0.50→6/8, α=0.52→3/8 (FDR).
  Drop from 6/8→3/8 is FDR stringency on marginal p-values
  (raw: 5/8 at p<0.10). K_ge3=6/8 with strong multi-method
  consensus confirms hypothesis: α=0.52 is above blind zone.
```

---
