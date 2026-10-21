# Negative Pattern Analysis: Event-Gated Adaptive Horizon

**Date**: 2026-05-14  
**Experiments covered**: exp_001 – exp_008d (11 runs)

---

## 1. Root-Cause Classification

### A. Implementation Bug Class (exp_002 / exp_003 / exp_004)

| Exp | Status | Root Cause | Key Metric |
|-----|--------|-----------|------------|
| exp_002_event_gated | FAILED | Phase 1 subsample size mismatch — training data not aligned with evaluation | N/A (crashed) |
| exp_003_event_gated_v2 | NEGATIVE | (1) imagination dt unconstrained; (2) λ-return dt index off-by-one | eval_return@115K = 118.7, return_ratio = 0.13 |
| exp_004_event_gated_v3 | NEGATIVE | gate_loss explosion: target discretized to 8 bins vs binary masking assumption | gate_loss diverged |

**Common failure mode**: Each bug was a silent mismatch between two components that should share a contract (subsample sizes, dt indexing, loss target shape). No single component crashed — the system trained but produced garbage.

**Lessons**:
1. **Shape/index assertions at boundaries.** Every place where one module produces a tensor consumed by another needs an explicit assert on shape, dtype, and value range. exp_003's off-by-one and exp_004's 8-vs-2 bin mismatch would both be caught by a single `assert target.max() <= 1` or `assert dt_indices.shape == returns.shape[:-1]`.
2. **Canary metrics for silent bugs.** gate_loss, imagination dt distribution, and return_ratio should be logged from step 0 and checked against expected ranges within the first 1K steps. exp_003 ran to 115K before anyone noticed return_ratio = 0.13.
3. **One fix per experiment.** exp_003 changed two things (dt constraint + λ-return indexing). When it failed, root cause attribution was ambiguous. exp_004 repeated this pattern. Fix one thing, measure, repeat.

---

### B. Structural Finding Class (exp_005 / exp_006 / exp_007)

| Exp | Config | Peak Return (step) | Final Return (step) | Baseline@same step | Delta vs Baseline |
|-----|--------|-------------------|---------------------|-------------------|-------------------|
| exp_005_event_gated_v4 | Hard Gumbel gate, all bugs fixed | 541 (55K) | 98.84 (145K) | ~950 | -90% final |
| exp_006_fixed_dt2 | Fixed dt=2, no gate | 485 (35K) | 360 (55K) | 625 (55K) | -42.4% |
| exp_007_fixed_dt4 | Fixed dt=4, no gate | 176.9 (25K) | ~176 (25K+) | baseline >> 176 | ~-70% |

**Common failure mode**: Performance collapse over training. All three show early promise (peak before 55K) followed by monotonic degradation. The larger the temporal skip, the faster and deeper the collapse.

**Lessons**:
1. **Hard discrete gates are structurally unstable for imagination.** exp_005 proved that even with all implementation bugs fixed, Gumbel-hard gating causes collapse. The gate creates a non-stationary imagination distribution that the value function cannot track. This closes the hard-gate design direction.
2. **dt > 1 causes compounding error proportional to dt magnitude.** exp_006 (dt=2) lost 42%, exp_007 (dt=4) lost ~70%. This is consistent with RSSM prediction error compounding across skipped frames. The relationship is superlinear — dt=4 is not 2× worse than dt=2, it's ~3× worse relative to baseline gap.
3. **Peak-then-collapse is the signature of imagination-side instability.** In all three experiments, the actor initially benefits from longer horizons (higher peak than expected for the step count), but the critic's value estimates diverge as imagination trajectories become unreliable. Monitor for this pattern: if eval_return peaks before 50K and then drops >20%, stop early.

---

### C. In-Progress (exp_008a / exp_008c / exp_008d)

| Exp | Config | H | Subsample | eval_return@35K | Baseline@35K | Delta |
|-----|--------|---|-----------|-----------------|-------------|-------|
| exp_008a_no_subsample_dt2 | dt=2, no subsample | 15 | OFF | 500.84 | ~400 | **+25%** |
| exp_008c_no_subsample_dt2_h8 | dt=2, no subsample | 8 | OFF | 185.10 | ~400 | **-54%** |
| exp_008d_subsample_on_h8 | dt=2, subsample ON | 8 | ON | pending (< 35K) | — | — |

**Status**: 008a is the first experiment to exceed baseline at any checkpoint. 008c is severely underperforming. 008d has not reached the first evaluation point.

---

## 2. 008a vs 008c: Interpretation and Decision Tree

### Breaking the original predictions

The 008a/008c divergence does not match any of the three pre-registered predictions:

| Prediction | Expected | Observed | Verdict |
|-----------|----------|----------|---------|
| P1: 008a collapses, 008c survives → compounding error is root cause | 008a < baseline, 008c ≥ baseline | 008a > baseline, 008c < baseline | **Falsified** |
| P2: Both collapse → RSSM cannot handle dt=2 | Both < baseline | Only 008c < baseline | **Falsified** |
| P3: 008a survives → dt=2 imagination is harmless | 008a ≥ baseline | 008a > baseline, but 008c collapsed | **Partially confirmed** |

### New interpretation

dt=2 imagination is viable when the effective imagination horizon (H × dt = total frames covered) is sufficient. The critical variable is not dt but **H**:

- **008a**: H=15, covers 15×2 = 30 frames. Actor gets 15 gradient steps through the imagination trajectory. Result: +25% over baseline.
- **008c**: H=8, covers 8×2 = 16 frames. Actor gets only 8 gradient steps. Result: -54% vs baseline.

For reference, standard DreamerV3 uses H=15 with dt=1 (15 frames, 15 gradient steps). 008a preserves gradient step count while doubling frame coverage. 008c halves gradient step count — the actor-critic optimization may not have enough signal to learn effectively.

**Hypothesis**: The minimum viable H for dt=2 is somewhere in (8, 15]. The actor needs ≥ ~12-15 imagination steps regardless of dt.

### Decision tree for 65K / 105K checkpoints

```
                        65K results arrive
                              |
              ┌───────────────┴───────────────┐
              │                               │
     008a ≥ baseline@65K              008a < baseline@65K
     (no collapse)                    (collapse started)
              │                               │
              │                     ┌─────────┴─────────┐
              │                     │                   │
              │              008c also dropped     008c recovered
              │              further                    │
              │                     │              Unlikely but:
              │                     │              H=8 slow learner,
              │                     │              revisit H trade-off
              │                     │
              ▼                     ▼
      CHECK 105K               STOP 008c.
              │                Diagnosis: dt=2 causes
              │                delayed collapse even
              │                at H=15. Close dt=2 line.
              │
     ┌────────┴────────┐
     │                 │
008a ≥ baseline    008a < baseline
  @105K              @105K
     │                 │
     ▼                 ▼
  SUCCESS          DELAYED COLLAPSE
  dt=2 + H=15       Same pattern as exp_005/006/007
  is validated.      but slower. Need to understand
  Next: test          why H=15 delays but doesn't
  adaptive H          prevent it.
  (gate mechanism      │
  with soft gates)     ▼
     │              Try H=20 or H=25 with dt=2
     │              to test if more gradient steps
     ▼              stabilize long-term.
  Design soft-gate
  experiment:
  - Soft sigmoid gate (not Gumbel)
  - H=15, dt ∈ {1,2} selected per step
  - Compare vs fixed dt=2 (008a)
```

**Key 65K decision rule**: If 008a eval_return ≥ 90% of baseline@65K, continue to 105K. If < 90%, the collapse pattern from exp_005/006 is repeating — stop early and reassess.

---

## 3. dt_embedding Confound Risk Assessment

### The concern

Reviewer flagged: when dt > 1, the RSSM receives a dt_embedding that signals "this transition spans 2 frames." This embedding is a new input not present in baseline training. It could act as a confounding variable — improvements or degradations might be driven by the embedding's effect on RSSM representations, not by the temporal skip itself.

### Does exp_008d cover this?

**Partially.** exp_008d uses subsample ON + H=8, meaning the RSSM trains on subsampled sequences (sees dt_embedding during world model training) but also uses dt=2 in imagination. Comparing 008d vs 008c:

| | 008c | 008d |
|--|------|------|
| H | 8 | 8 |
| dt (imagination) | 2 | 2 |
| Subsample (world model training) | OFF | ON |
| dt_embedding during WM training | NO (dt=1 data only) | YES (mixed dt) |

If **008d ≈ 008c** (both bad): dt_embedding during training doesn't help. The problem is H=8, not embedding exposure. This is consistent with the "insufficient gradient steps" hypothesis.

If **008d > 008c** significantly: Subsample training improves imagination quality, possibly because the RSSM learns to handle dt=2 transitions better when it sees them during training. dt_embedding exposure matters.

If **008d < 008c**: Subsample training actively hurts. The RSSM is worse when trained on mixed-dt data.

### Can we isolate dt_embedding from subsample?

**No, not with current experiments.** 008d confounds two variables:
1. Subsample changes the training data distribution (skipped frames)
2. Subsample introduces dt_embedding into world model training

To isolate dt_embedding, we would need:

| Experiment | Training data | dt_embedding in WM | dt in imagination |
|-----------|--------------|-------------------|-------------------|
| Control (008c) | Original (dt=1) | NO | 2 |
| 008d | Subsampled (mixed dt) | YES | 2 |
| **Missing: 008e** | Original (dt=1) | YES (fed constant dt=1 embedding) | 2 |
| **Missing: 008f** | Subsampled (mixed dt) | NO (remove embedding) | 2 |

**008e** would tell us: does merely adding a dt_embedding input to the RSSM (even when dt=1 always) change representation quality? If 008e ≈ 008c, the embedding is neutral. If 008e < 008c, the embedding actively hurts even at dt=1.

### Recommendation

1. **Wait for 008d results before designing new experiments.** If 008d ≈ 008c, the dt_embedding concern is secondary — H is the dominant variable and we should focus on H=15 variants.
2. **If 008d ≠ 008c by > 15%**, the embedding/subsample axis matters. Run 008e (dt_embedding with dt=1 training data) to isolate the embedding effect. This is a low-cost experiment — minimal code change (add embedding, keep data pipeline unchanged).
3. **For the paper**: if 008a succeeds at 105K, the dt_embedding confound can be addressed by an ablation: 008a-no-embed (dt=2 imagination, H=15, but remove dt_embedding from RSSM input). If performance holds, embedding is not load-bearing. If it drops, embedding is contributing and needs proper analysis.

---

## 4. Summary of Actionable Rules

| # | Rule | Source |
|---|------|--------|
| 1 | Assert tensor shape/dtype/range at every cross-module boundary | exp_002, 003, 004 |
| 2 | Log canary metrics (gate_loss, dt distribution, return_ratio) and validate within first 1K steps | exp_003 |
| 3 | One independent variable per experiment | exp_003, 004 |
| 4 | Hard discrete gates (Gumbel-hard) are closed as a design direction for imagination gating | exp_005 |
| 5 | dt > 1 causes superlinear compounding error; dt=4 is non-viable | exp_006, 007 |
| 6 | Peak-then-collapse before 50K with >20% drop = early stop signal | exp_005, 006, 007 |
| 7 | Minimum imagination steps H ≈ 12-15 regardless of dt; H=8 is insufficient at dt=2 | exp_008a vs 008c |
| 8 | dt_embedding is an unresolved confound; need dedicated ablation before claiming dt-skip is the mechanism | Reviewer concern |
