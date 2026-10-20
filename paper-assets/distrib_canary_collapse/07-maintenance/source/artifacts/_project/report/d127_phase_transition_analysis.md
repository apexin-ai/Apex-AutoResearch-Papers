# D127 Track D: Phase Transition Analysis

## Core Findings

1. **Phase Transition Type**: Steep crossover approaching first-order
   - α=0.45→0.50 jump: PermG 0/8 → 6/8, consistent across 3 seeds
   - Sigmoid fit: α_c=0.476, steepness k≥200, transition width Δα≈0.02
   - Near-switch behavior; denser sampling needed to claim true discontinuity
   - Paper language: "sharp onset of causal detectability" or "near-discontinuous onset"

2. **Sigmoid >> Power Law**
   - Sigmoid R²=0.969, AIC=-8.90
   - Power law R²=0.808, AIC=9.30
   - ΔAIC=18.2, overwhelming sigmoid advantage

3. **Model Scale**: No monotonic relationship
   - Qwen-0.8B (7.0) ≈ Pythia-6.9B (7.0) > Pythia-410M (6.0) > 1.4B (4.0) > SmolLM3-3B (3.0)
   - Weakening root cause: entropy trajectory shape (U-shape/saturation), not model size
   - ECE canary more robust than entropy across all models

4. **vs Gu et al.**: α_c≈0.48 is detection threshold, not collapse threshold; iterative compounding makes effective contamination near-identical at α=0.45 and 0.50 (99.88% vs 99.95%), yet PermG jumps 0→6

5. **Gap**: α=0.60 awaiting canonical data (a060_v4 running)

## Artifacts Location
westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts_phase_transition/