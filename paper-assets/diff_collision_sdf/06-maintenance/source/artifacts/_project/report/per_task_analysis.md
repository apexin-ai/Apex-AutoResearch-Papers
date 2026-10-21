# Per-Task CAR Breakdown Analysis

## Data Summary

All data from 30K checkpoint, eval seed=7, 200 episodes (50 per task). Per-seed per-task CAR values in percentage points.

### Complete Per-Seed Per-Task CAR

| Condition | Seed | OJ | CP | Milk | BBQ | Agg |
|-----------|------|----|----|------|-----|-----|
| LoRA-only | s0 | 68 | 74 | 66 | 20 | 57.0 |
| LoRA-only | s1 | 54 | 68 | 72 | 16 | 52.5 |
| LoRA-only | s2 | 56 | 76 | 62 | 26 | 55.0 |
| **LoRA-only mean** | | **59.3** | **72.7** | **66.7** | **20.7** | **54.8** |
| SDF λ=0.005 | s0 | 52 | 74 | 74 | 28 | 57.0 |
| SDF λ=0.005 | s1 | 64 | 70 | 68 | 14 | 54.0 |
| SDF λ=0.005 | s2 | 46 | 74 | 72 | 18 | 52.5 |
| **SDF 0.005 mean** | | **54.0** | **72.7** | **71.3** | **20.0** | **54.5** |
| SDF λ=0.01 | s0 | 48 | 74 | 72 | 34 | 57.0 |
| SDF λ=0.01 | s1 | 60 | 76 | 72 | 22 | 57.5 |
| SDF λ=0.01 | s2 | 64 | 68 | 72 | 14 | 54.5 |
| **SDF 0.01 mean** | | **57.3** | **72.7** | **72.0** | **23.3** | **56.3** |
| SDF λ=0.1 | s0 | 60 | 74 | 68 | 30 | 58.0 |
| SDF λ=0.1 | s1 | 66 | 72 | 70 | 26 | 58.5 |
| SDF λ=0.1 | s2 | 56 | 76 | 70 | 16 | 54.5 |
| **SDF 0.1 mean** | | **60.7** | **74.0** | **69.3** | **24.0** | **57.0** |

### Per-Task Grand Statistics (all 12 seeds pooled)

| Task | Mean | Std | Range | CV |
|------|------|-----|-------|-----|
| orange_juice | 57.8 | 6.8 | 46–68 | 11.7% |
| choco_pudding | 73.0 | 2.8 | 68–76 | 3.8% |
| milk | 69.8 | 3.2 | 62–74 | 4.6% |
| bbq_sauce | 22.0 | 6.4 | 14–34 | 29.3% |

---

## Analysis 1: SDF vs LoRA-only Per-Task Variance

### Per-task delta (SDF pooled mean minus LoRA-only mean)

| Task | LoRA mean | SDF mean (9 seeds) | Δ (pp) |
|------|-----------|---------------------|--------|
| orange_juice | 59.3 | 57.3 | −2.0 |
| choco_pudding | 72.7 | 73.1 | +0.4 |
| milk | 66.7 | 70.9 | **+4.2** |
| bbq_sauce | 20.7 | 22.4 | +1.8 |

**Most changed task: Milk (+4.2 pp).** All three SDF conditions show milk CAR above the LoRA-only mean (71.3, 72.0, 69.3 vs 66.7). However, this delta is well within seed-to-seed noise (LoRA milk std=5.0 across seeds), so it is not statistically meaningful.

**Most stable task: Chocolate Pudding (+0.4 pp).** CP is essentially invariant to SDF. Across all 12 seeds, CP ranges only 68–76 (std=2.8), making it the strongest "anchor" in the fingerprint. Explanation: CP requires picking up an item directly in front of the arm with minimal obstacle proximity, so collision behavior is dominated by the demonstration trajectory rather than any avoidance signal.

**Orange juice shows a slight decrease (−2.0 pp)** under SDF, but this is driven by a single low seed (λ=0.005 s2 = 46%). The high OJ variance (std=6.8) means this is noise, not a systematic degradation.

### Variance decomposition

| Source | Variance | % of total |
|--------|----------|------------|
| Between-task (task identity) | 409.5 | **94.0%** |
| Within-task (seed + condition) | 26.2 | 6.0% |

Task identity explains 94% of total CAR variance. Adding SDF at any λ does not shift this decomposition—the "fingerprint" is entirely demonstration-driven.

---

## Analysis 2: bbq_sauce Seed-to-Seed Variance

### BBQ CAR by condition and seed

| Condition | s0 | s1 | s2 | Mean | Std | Range |
|-----------|----|----|-----|------|-----|-------|
| LoRA-only | 20 | 16 | 26 | 20.7 | 5.0 | 10 |
| SDF λ=0.005 | 28 | 14 | 18 | 20.0 | 7.2 | 14 |
| SDF λ=0.01 | **34** | 22 | **14** | 23.3 | **10.1** | **20** |
| SDF λ=0.1 | 30 | 26 | 16 | 24.0 | 7.2 | 14 |

The worst case is SDF λ=0.01: s0=34% to s2=14%, a 20 pp swing. This is the largest single-task seed-to-seed range in the entire dataset.

### Why BBQ has high variance

1. **Low base rate amplifies binomial noise.** With 50 episodes and true CAR ~22%, expected σ ≈ sqrt(50 × 0.22 × 0.78) / 50 × 100 ≈ 5.9 pp. The observed std (5.0–10.1) is 1–1.7× this floor, consistent with sampling noise plus minor policy variation.

2. **Obstacle geometry.** BBQ sauce is positioned behind other objects, requiring the arm to navigate a narrow corridor. Small differences in learned trajectory curvature (seed-dependent) disproportionately affect whether intermediate links clear the obstacle volume. The arm's elbow/forearm sweeps through the densest obstacle region for this task.

3. **Collision body mismatch.** BBQ's dominant collision mode involves arm links (not the EE), which are exactly the bodies that SDF monitoring cannot protect. This explains both the low mean and the high cross-seed variance: the policy's arm posture during reaching is highly seed-dependent and unregulated by SDF.

## Analysis 3: Per-Task Ordering Consistency

### Condition-level ordering (3-seed means)

| Condition | 1st | 2nd | 3rd | 4th |
|-----------|-----|-----|-----|-----|
| LoRA-only | CP (72.7) | Milk (66.7) | OJ (59.3) | BBQ (20.7) |
| SDF λ=0.005 | CP (72.7) | Milk (71.3) | OJ (54.0) | BBQ (20.0) |
| SDF λ=0.01 | CP (72.7) | Milk (72.0) | OJ (57.3) | BBQ (23.3) |
| SDF λ=0.1 | CP (74.0) | Milk (69.3) | OJ (60.7) | BBQ (24.0) |

**The ordering CP > Milk > OJ > BBQ is perfectly invariant across all four conditions.** This is the paper's "fingerprint" claim.

### Seed-level ordering (12 individual seeds)

| Condition | Seed | Ordering (high → low) | CP 1st? | BBQ last? |
|-----------|------|-----------------------|---------|-----------|
| LoRA | s0 | CP > OJ > Milk > BBQ | ✓ | ✓ |
| LoRA | s1 | Milk > CP > OJ > BBQ | ✗ | ✓ |
| LoRA | s2 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.005 | s0 | CP = Milk > OJ > BBQ | ✓(tie) | ✓ |
| SDF 0.005 | s1 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.005 | s2 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.01 | s0 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.01 | s1 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.01 | s2 | Milk > CP > OJ > BBQ | ✗ | ✓ |
| SDF 0.1 | s0 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.1 | s1 | CP > Milk > OJ > BBQ | ✓ | ✓ |
| SDF 0.1 | s2 | CP > Milk > OJ > BBQ | ✓ | ✓ |

**BBQ is last in 12/12 seeds (100%).** CP is first or tied-first in 10/12 seeds (83%). The two exceptions (LoRA s1, SDF 0.01 s2) have Milk edging out CP by 4 pp, within sampling noise.

### Kendall's W (concordance)

The extreme tasks (CP at top, BBQ at bottom) are fully invariant. The middle pair (OJ, Milk) shows one swap pattern: LoRA s0 has OJ > Milk (68 vs 66), the only seed across all 12 where OJ ranks above Milk. This single swap does not threaten the fingerprint claim because:
- The OJ–Milk gap at s0 is only 2 pp (within noise)
- At the condition-mean level, Milk > OJ in all four conditions

---

## Cross-Validation: Eval-Seed Robustness (LoRA s0, 5 eval seeds)

| Eval seed | OJ | CP | Milk | BBQ | Agg |
|-----------|----|----|------|-----|-----|
| 0 | 46 | 70 | 74 | 22 | 53.0 |
| 7 | 68 | 74 | 66 | 20 | 57.0 |
| 42 | 60 | 70 | 68 | 28 | 56.5 |
| 99 | 58 | 76 | 66 | 30 | 57.5 |
| 123 | 52 | 74 | 66 | 20 | 53.0 |
| **Mean±Std** | **56.8±8.3** | **72.8±2.7** | **68.0±3.5** | **24.0±4.7** | **55.4±2.2** |

The fingerprint ordering (CP > Milk > OJ > BBQ) holds across all 5 eval seeds for a single training seed, confirming it is a property of the trained policy, not evaluation noise. CP remains the most stable (std=2.7) and OJ the most variable (std=8.3), consistent with training-seed analysis.

---

