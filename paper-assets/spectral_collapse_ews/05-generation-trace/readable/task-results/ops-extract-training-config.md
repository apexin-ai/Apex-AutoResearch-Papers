# ops extract training config

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_training_config_20260521T060547_result.json`
- **Structured JSON:** [`e5b93140ba2186b6e14d.json`](../../sessions/e5/e5b93140ba2186b6e14d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the compiled output:

```
Training Hyperparameters:
- Model: EleutherAI/pythia-410m-deduped (410M params)
- Optimizer: AdamW (weight_decay=0.01)
- Learning rate: 5e-5, linear warmup + linear decay schedule
- Batch size: 8 (gradient accumulation: 4, effective: 32)
- Epochs per generation: 1
- Warmup ratio: 0.05
- Gradient clipping: max_norm=1.0
- Training samples per generation: 50,000 (fixed volume; ratio controls real/synthetic split)
- Generation: temperature=1.0, top_k=50, do_sample=True (no top_p)
- Generation batch size: 32
- Max sequence length: 512
- Spectral eval samples: 1,000
- Perplexity eval samples: 5,000
- Distinct-4 eval samples: 1,000

SpectralController defaults (adaptive condition):
- k=20.0, τ=0.002, r_base=0.50, r_min=0.20, r_max=0.80
- signal=log_det, signal_mode=per_gen, α_EMA=0.5

Compute:
- GPU: 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (96 GB each)
- Per-generation cycle (mixed conditions, r≥0.3): ~89 min
  (verified: adaptive_k10_seed42 gen_1→gen_10 = 13h20m / 9 intervals)
- Per-generation cycle (pure collapse, r=0): ~155 min
  (verified: pure_collapse_seed43 gen_1→gen_10 = 23h17m / 9 intervals)
- Full 10-gen pipeline: ~15h (mixed) to ~26h (pure collapse)
- Completed Phase 1 pipelines (10 gens, 410M):
    1. adaptive_k10_seed42       (~15h)
    2. fixed_mix_seed42 r=0.5    (~15h)
    3. fixed_mix_r02_seed42      (~22h est.)
    4. fixed_mix_r025_seed42     (~20h est.)
    5. fixed_mix_r03_seed42      (~19h est.)
    6. pure_collapse_seed43      (~26h)
- Partial Phase 1 runs: pure_collapse_seed44 (8/10), fixed_mix_r025_seed43 (3/10), fixed_mix_r03_seed43 (1/10) — ~31h est.
- Phase 0 pilot: 410M 10-gen (~26h) + 1B 3-gen (~12h)
- Earlier experimental runs (adaptive_k20, adaptive_k1): ~20h est.
- HellaSwag + alternative EWS evaluations: ~10h est.
- Estimated total: ~220 single-GPU hours on RTX PRO 6000

Source files:
- src/config.py (all defaults)
- src/pipeline.py:214 (AdamW, weight_decay=0.01, gradient clipping)
- src/generate.py (temperature, top_k, no top_p)
- src/evaluate.py (eval sample counts)
- src/controller.py (controller formula & params)
- Timing: checkpoint directory stat timestamps under
  /root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/
  /root/autodl-tmp/spectral_collapse_ews/checkpoints_410m/
```

---
