# W4 Single-Seed Audit

Generated: 2026-05-21

## Table 1: Cross-Model Comparison (tab:cross_model)

5 conditions × 4 models = 20 cells. Multi-seed entries show mean±std in paper.

### Single-Seed Cells (1 seed only)

| Model | Condition | Seeds | Seed Values | Accuracy | Core Claim | Risk |
|-------|-----------|-------|-------------|----------|------------|------|
| Qwen-7B | no_trace | 1 | 42 | 75.13 | C3 (tier baseline) | Moderate |
| CodeLlama-13B | no_trace | 1 | 42 | 76.47 | C3 (tier baseline) | Moderate |
| DeepSeek-6.7B | no_trace | 1 | 42 | 73.36 | C3 (tier baseline) | Moderate |

### Two-Seed Cells (not single-seed but below 3-seed standard)

| Model | Condition | Seeds | Seed Values | Accuracy (mean±σ) | Core Claim | Risk |
|-------|-----------|-------|-------------|----------|------------|------|
| Qwen-1.5B | ae_only | 2 | 42, 123 | 98.83±0.36 | C3 (Tier 1) | Low |
| Qwen-1.5B | VOTA | 2 | 42, 123 | 99.54±0.06 | C4 (universality) | Low |
| CodeLlama-13B | ae_only | 2 | 42, 123 | 99.08±0.00 | C3 (Tier 1) | Low |
| CodeLlama-13B | VOTA | 2 | 42, 123 | 98.74±0.24 | C4 (universality) | Low |
| DeepSeek-6.7B | ae_only | 2 | 42, 123 | 98.53±0.30 | C3 (Tier 1) | Low |
| DeepSeek-6.7B | VOTA | 2 | 123, 456 | 99.25±0.12 | C4 (universality) | Low |

### Three-Seed Cells (fully robust)

| Model | Condition | Seeds | Seed Values | Accuracy (mean±σ) |
|-------|-----------|-------|-------------|----------|
| Qwen-7B | exception_only | 3 | 42, 123, 456 | 99.83±0.00 |
| Qwen-7B | ae_only | 3 | 42, 123, 456 | 99.64±0.49 |
| Qwen-7B | VOTA | 3 | 42, 123, 456 | 99.05±0.38 |
| Qwen-7B | loop_only | 3 | 42, 123, 456 | 86.05±0.52 |
| Qwen-1.5B | exception_only | 3 | 42, 123, 456 | 99.83±0.00 |
| Qwen-1.5B | loop_only | 3 | 42, 123, 456 | 79.54±1.42 |
| Qwen-1.5B | no_trace | 3 | 42, 123, 456 | 72.35±4.48 |
| CodeLlama-13B | exception_only | 3 | 42, 123, 456 | 99.89±0.10 |
| CodeLlama-13B | loop_only | 3 | 42, 123, 456 | 77.40±1.54 |
| DeepSeek-6.7B | exception_only | 3 | 42, 123, 456 | 99.39±0.10 |
| DeepSeek-6.7B | loop_only | 3 | 42, 123, 456 | 80.31±1.65 |

---

## Table 2: Component Ablation (tab:ablation, Qwen-7B only)

### Single-Seed Cells

| Condition | Seeds | Seed Values | Accuracy | Core Claim | Risk |
|-----------|-------|-------------|----------|------------|------|
| full_trace | 1 | 42 | 81.76 | C2 (density decomposition anchor) | Moderate |
| no_trace | 1 | 42 | 75.13 | C3 (tier baseline) | Moderate |
| VOTA_no_ae | 1 | 42 | 99.41 | C1 (exception dominance) | Low |

### Multi-Seed Cells in Table 2

| Condition | Seeds | Accuracy (mean±σ) |
|-----------|-------|----------|
| ae_only | 3 | 99.64±0.49 |
| exception_only | 3 | 99.83±0.00 |
| VOTA | 3 | 99.05±0.38 |
| loop_only | 3 | 86.05±0.52 |

---

## Table 3 (tab:density): Information Density Decomposition

| Condition | Seeds | Accuracy | Single-seed? |
|-----------|-------|----------|--------------|
| full_trace | 1 | 81.76 | YES |
| label_only | 3 | 85.94±1.12 | No |
| VOTA | 3 | 99.05±0.38 | No |

---

## Risk Assessment by Core Claim

### C1: Exception Dominance
- **exception_only** has 3 seeds on ALL 4 models → robust
- **VOTA_no_ae** (Table 2) is single-seed → confirms exception alone suffices, but only 1 measurement. If this shifts down, the "combining signals introduces noise" argument weakens. However, the 0.78pp gap (exception > VOTA) is confirmed across 3 seeds.
- **Risk: LOW.** Main claim (exception_only ≥99.33% everywhere) has 3-seed support on all 4 models.

### C2: Density Decomposition (§4.4)
- **full_trace** is single-seed (81.76%) — this is the anchor for the 24%/76% decomposition
- **label_only** has 3 seeds (85.94±1.12) ✓
- **VOTA** has 3 seeds ✓
- **Risk: MODERATE.** The decomposition "full_trace (81.76) → label_only (85.94) → VOTA (99.05)" depends on single-seed full_trace. If full_trace varies by ±2pp (plausible given loop_only σ=0.52 and it has more noise), the "24% gradient dilution" fraction shifts. However, the DIRECTION (label_only > full_trace < VOTA) is very unlikely to flip.

### C3: Tier Hierarchy (exception/ae >> loop >> no_trace)
- **no_trace** is single-seed on 3/4 models (Qwen-7B, CL-13B, DS-6.7B)
- Key observation: Qwen-1.5B no_trace (3 seeds) shows σ=4.48pp, indicating no_trace can vary substantially
- However, the Tier 1/2 boundary (lowest Tier 1 at 98.53% vs highest Tier 2 at 86.05%) spans 12.48pp with non-overlapping CIs → single-seed no_trace cannot threaten this
- **Risk: LOW.** The tier gaps are too large for seed variance to close. Even if single-seed no_trace is off by ±5pp, the hierarchy holds.

### C4: VOTA Universality
- VOTA has 2+ seeds on all 4 models (3 seeds on Qwen-7B and DS-6.7B, 2 seeds on Qwen-1.5B and CL-13B)
- The claim "≥98.57% across all four models" relies on CL-13B's 2-seed mean (98.74±0.24)
- **Risk: LOW.** Even 2-seed CL-13B VOTA (98.57, 98.91) both exceed the stated floor. Adding a 3rd seed is unlikely to undermine the claim.

---

## Summary

| Risk Level | Count | Cells |
|------------|-------|-------|
| **Single-seed** | 6 | 3× no_trace (Table 1), full_trace + no_trace + VOTA_no_ae (Table 2) |
| **Two-seed** | 6 | ae_only (3 models) + VOTA (3 models) in Table 1 |
| **Three-seed** | 11 | All exception_only, all loop_only, Qwen-7B (all), Qwen-1.5B no_trace |

**Verdict:** No single-seed cell directly supports a core claim whose direction could flip. The 3 single-seed no_trace values serve as baselines — their absolute values could shift by ±4pp (extrapolating from Qwen-1.5B σ=4.48), but this doesn't threaten any tier boundary or claim. The single-seed full_trace (81.76%) in the density decomposition is the highest-risk item: if a reviewer requests 3-seed full_trace to validate the "24% gradient dilution" figure, the exact percentage may shift.

**Recommended action:** If reviewer asks, prioritize re-running Qwen-7B full_trace with seeds 123/456 (validates C2 decomposition). no_trace reruns are lower priority since Qwen-1.5B already demonstrates the variance profile and claims don't depend on exact no_trace values.
