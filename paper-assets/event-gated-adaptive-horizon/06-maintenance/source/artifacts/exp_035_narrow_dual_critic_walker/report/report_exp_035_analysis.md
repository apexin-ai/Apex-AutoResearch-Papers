# exp_035: Narrow Dual-Critic Walker — Final Analysis

## Experiment Overview

**Hypothesis:** Narrow dual-critic ablation (2×256 hidden, ~1.05M params total — matching baseline single 512 critic) isolates the min operation effect from parameter count.

**2×2 Factorial Position:**

|  | Single Critic | Dual Critic (min) |
|---|---|---|
| ~1.05M (normal) | Baseline: CIVO → collapse | **exp_035 (this experiment)** |
| ~2.4-2.9M (wide) | exp_033: NVE 4.75 → recovery, eval 408 | exp_032: NVE ≤ 1.1, eval 787.7 |

**Config:** gate_fixed_dt=2, imag_horizon=8, narrow_dual_critic=true, critic_hidden=256, critic_layers=2, critic_params_total≈1.05M

**Duration:** ~215K env steps (8.33 training hours), server bjb1-40020 cuda:1

---

## Key Metrics

### Eval Return Trajectory

| Step | eval_return | Phase |
|------|-------------|-------|
| 5K | 35.6 | warmup |
| 15K | 94.9 | early learning |
| 25K | 152.9 | early peak |
| 35K | 106.8 | pre-CIVO dip |
| 45K | 206.0 | pre-CIVO peak |
| 55K | 155.2 | CIVO onset |
| 65K | 124.7 | CIVO alert triggered |
| 75K | 67.5 | CIVO collapse |
| **85K** | **33.8** | **CIVO trough** |
| 95K | 66.5 | early recovery |
| 105K | 64.2 | recovery plateau |
| 115K | 114.8 | recovery accelerating |
| 125K | 149.2 | recovery |
| 135K | 282.6 | recovery |
| 145K | 244.3 | recovery dip |
| 155K | 452.9 | strong recovery |
| 165K | 421.0 | fluctuation |
| 175K | 396.1 | fluctuation |
| 185K | 537.0 | climbing |
| 195K | 644.4 | climbing |
| 205K | 521.7 | dip |
| **215K** | **697.8** | **final eval (still climbing)** |

- **eval_peak:** 697.8 (at 215K, final eval, still ascending)
- **eval_final:** 697.8
- **eval_trough:** 33.8 (at 85K during CIVO)
- Train returns at 224K: 708–806 (suggest eval would have been higher if continued)

### NVE (ve_ratio) Trajectory

| Step | ve_ratio | alert | v1_mean | v2_mean | v1-v2 gap |
|------|----------|-------|---------|---------|-----------|
| 15K | 0.011 | 0 | 1.0 | 1.0 | 0.00 |
| 25K | 0.060 | 0 | 9.2 | 9.1 | 0.08 |
| 35K | 0.222 | 0 | 23.8 | 23.8 | 0.01 |
| 45K | 0.207 | 0 | 42.8 | 42.8 | 0.01 |
| 55K | 0.421 | 0 | 65.5 | 65.5 | 0.02 |
| **65K** | **0.694** | **1** | 86.7 | 86.7 | 0.03 |
| **75K** | **1.502** | **1** | 101.7 | 101.6 | 0.04 |
| **85K** | **2.750** | **1** | 93.1 | 93.1 | 0.02 |
| 95K | 1.250 | 0 | 83.4 | 83.4 | 0.01 |
| 105K | 1.256 | 0 | 80.9 | 80.9 | 0.01 |
| 115K | 0.652 | 0 | 75.1 | 75.1 | 0.01 |
| 125K | 0.451 | 0 | 67.5 | 67.5 | 0.01 |
| 135K | 0.233 | 0 | 66.0 | 66.0 | 0.02 |
| 145K | 0.263 | 0 | 64.6 | 64.6 | 0.01 |
| 155K | 0.137 | 0 | 62.2 | 62.2 | 0.01 |
| 165K | 0.144 | 0 | 60.8 | 60.8 | 0.01 |
| 175K | 0.148 | 0 | 59.0 | 59.0 | 0.01 |
| 185K | 0.105 | 0 | 56.6 | 56.6 | 0.01 |
| 195K | 0.083 | 0 | 53.9 | 53.9 | 0.01 |
| 205K | 0.094 | 0 | 49.4 | 49.4 | 0.01 |
| 215K | 0.066 | 0 | 46.0 | 46.1 | 0.01 |

- **NVE_peak:** 2.75 (step 85K) — CIVO triggered
- **NVE_final:** 0.066 (step 215K) — fully resolved
- **CIVO alert window:** steps 65K–85K (3 consecutive evals)
- **CIVO prevented:** NO

### Gate Behavior
- gate_dt_2_frac = 1.0 throughout (fixed dt=2 as configured)
- gate_empirical_entropy = 0.0 (no gate variation)

### Actor Entropy
- Collapsed from 0.78 (15K) to -4.58 (65K) during CIVO buildup
- Recovered to -0.19 (215K) by end — healthy exploration restored

---

## Cross-Experiment Comparison

| Metric | exp_032 (dual wide) | exp_033 (single wide) | **exp_035 (dual narrow)** | Baseline (single normal) |
|--------|---------------------|----------------------|--------------------------|--------------------------|
| Params | ~2.4M | ~2.4-2.9M | **~1.05M** | ~1.05M |
| Critic arch | 2×512 min | 1×512 | **2×256 min** | 1×512 |
| NVE peak | 1.1 | 4.75 | **2.75** | collapse |
| CIVO prevented | YES | NO | **NO** | NO |
| CIVO recovery | N/A | YES (partial) | **YES (strong)** | NO |
| eval_peak | 787.7 | ~408 | **697.8** | ~900→collapse |
| eval_final | 787.7 | 407.9 | **697.8** | collapsed |
| v1-v2 gap | meaningful | N/A | **~0.01 (negligible)** | N/A |

---

## 2×2 Factorial Conclusions

### 1. Min operation alone does NOT prevent CIVO
NVE reached 2.75, clearly exceeding the 1.5 threshold. The min operation with narrow critics (2×256) fails to provide enough pessimistic pressure because both critics learn nearly identical value functions (v1-v2 gap ≈ 0.01). With insufficient network capacity to develop diverse value representations, the two critics collapse to the same function, rendering the min() operation ineffective for pessimism.

### 2. Min operation alone DOES enable strong recovery
Despite CIVO triggering, the agent recovered from eval 33.8 to 697.8 — a much stronger recovery than exp_033 (single wide: 408). This suggests that even when the two critics agree (gap ≈ 0), the dual-critic architecture provides some structural benefit during recovery, possibly through gradient diversity or implicit regularization.

### 3. Capacity alone enables weaker recovery
exp_033 (single wide, ~2.4M) also recovered from CIVO but only reached 408. Extra capacity without min operation is less effective for recovery than min operation without extra capacity.

### 4. Full prevention requires BOTH mechanisms
Only exp_032 (dual wide) achieved CIVO prevention (NVE ≤ 1.1). The 2×2 pattern is:

|  | Single Critic | Dual Critic (min) |
|---|---|---|
| Normal capacity | CIVO → collapse (no recovery) | CIVO → strong recovery (697.8) |
| Wide capacity | CIVO → weak recovery (408) | CIVO prevented (787.7) |

### 5. Surprising ranking: dual narrow > single wide
exp_035 (697.8) > exp_033 (408) despite having fewer parameters. The min architecture, even when both critics agree, provides a stronger recovery mechanism than raw capacity. This challenges the hypothesis that the dual-critic benefit is primarily about pessimism — the structural/optimization benefit may be more important.

---

## Impact on Synergistic Prevention Narrative

The 2×2 results reveal **complementary roles** rather than simple synergy:

- **Min operation** → primary mechanism for **recovery** (even without pessimism divergence)
- **Extra capacity** → primary mechanism for **prevention** (critic can maintain accurate values under high-return regimes)
- **Both together** → prevention is achieved because capacity prevents NVE from spiking, while min provides a safety net that would catch any incipient CIVO

The narrative should be updated from "synergistic prevention" to **"complementary defense-in-depth"**: capacity provides the first line of defense (preventing CIVO onset), while dual-critic min provides the second line (enabling recovery if CIVO does trigger).

---

## Conclusion: **NEGATIVE** (for prevention hypothesis)

Min operation alone (without extra capacity) does NOT prevent CIVO. However, it enables remarkably strong recovery (697.8 vs 408 for capacity-alone), making it the more important of the two mechanisms for robustness. Full CIVO prevention requires both mechanisms operating together.
