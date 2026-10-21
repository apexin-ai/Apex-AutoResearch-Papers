# analysis d34 universal cascade signature

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d34_universal_cascade_signature_20260520T182854_result.json`
- **Structured JSON:** [`12afe9c8059ee48646ea.json`](../../sessions/12/12afe9c8059ee48646ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All deliverables complete. Here's the summary:

## Results

**Task**: Test whether the Entropy→Diversity→Calibration cascade from synthetic-data collapse generalizes to other domains.

**Domains tested**:
1. **Pythia-70m pretraining** (20 checkpoints, step0→step143k): `perplexity → ece → distinct_1 → distinct_2 → distinct_3 → token_entropy` (τ = -0.667)
2. **OLMo-2-1B RLHF pipeline** (4 stages: base→SFT→DPO→RLVR): `ece → token_entropy → perplexity → distinct_1 → distinct_2` (τ = 0.333)

**Verdict**: 0/2 domains show entropy-first onset. The cascade ordering is domain-specific:
- **Pretraining**: perplexity moves first (the model learns to predict better before entropy contracts)
- **RLHF**: calibration (ECE) moves first (alignment reshapes confidence before entropy)
- **Collapse**: entropy moves first (distributional degradation spreads outward from entropy to diversity to perplexity)

This confirms the cascade is a signature of *distributional degradation*, not a universal property of distribution shift.

**Output artifacts**:
- `artifacts/universal_cascade/rlhf_cascade.json`
- `artifacts/universal_cascade/continual_cascade.json`
- `artifacts/universal_cascade/ucs_comparison.md`
- Raw data: `pythia_checkpoints_raw.json`, `olmo_checkpoints_raw.json`

---
