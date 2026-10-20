# analysis alpha sweep a046 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a046_s42_fp32_20260521T065551_result.json`
- **Structured JSON:** [`3d035d79300da82f0522.json`](../../sessions/3d/3d035d79300da82f0522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
alpha_sweep_a046_s42_fp32 | 5-Method Analysis Results
========================================================
alpha=0.46  seed=42  model=pythia-410m  dataset=wikitext103_5k
generations=11  steps_per_gen=5000  wall_clock=16477s (~4h35m)
checkpoint: results/alpha_sweep/a046_s42_fp32/gen_10/checkpoint

LEAD-LAG DETECTION:
  PermG_fwd:              0/8
  PermG_rev:              0/8
  DiffXCorr_fwd:          0/8
  DiffXCorr_rev:          0/8
  threshold_onset_3sigma: 0/8
  TY_fwd:                 0/8
  K_ge3:                  0/8
  K_ge4:                  0/8
  robust_pairs:           []

DRIFT (gen0 -> gen10):
  token_entropy: -19.4%
  ece:          +808.5%
  perplexity:   +13.4%
  distinct_1:   -34.7%
  distinct_2:   -46.3%
  distinct_3:   -45.8%
  mauve:        -22.0%

CONCLUSION: PermG 0/8 — complete blind zone at α=0.46. All 5 methods yield 0/8,
consistent with α=0.45 (0/8) and α=0.48 (0/8). Confirms α_c > 0.46.
Despite moderate downstream drift (distinct_2 -46.3%, distinct_3 -45.8%),
no lead-lag signal detectable. Phase transition boundary narrowed to [0.46, 0.50).
```

Registry updated (DONE/success), artifact registered. Analysis JSON saved to `artifacts/alpha_sweep_a046_s42_fp32/data/5method_analysis.json`.

---
