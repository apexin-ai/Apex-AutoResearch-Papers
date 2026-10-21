# exp_018v2_full_sgs_walker_s1 Analysis Report

## Conclusion: NEGATIVE (partial success — CIVO substantially reduced but not eliminated)

Full-SGS with detached dt_emb gradients reduced NVE from 4.12× (008d) to peak 1.66×, a 79% reduction in excess NVE. However, NVE briefly exceeds the 1.5× threshold at two eval points, and late training episodes show signs of instability. The hypothesis that obs decoder gradients are the **sole** CIVO root cause (C5) is not fully confirmed.

---

## Training Overview

| Item | Value |
|------|-------|
| Config | trained dt_emb + subsample ON + dt=2 + H=8 + full_sgs=True (detach all non-KL grads from dt_emb) |
| Gate | gate_enabled=True, gate_fixed_dt=2, gate_dt_2_frac=1.0 throughout (confirmed active) |
| Total env steps | 112,000 (configured 105,000; extra episodes from batch completion) |
| Training updates | 25,099 |
| Exit code | 0 (normal) |
| Server | bjb1-45299, cuda:1 |
| Seed | 1 |

## Eval Returns

| Step | eval_return |
|------|------------|
| 5K   | 35.5       |
| 15K  | 141.5      |
| 25K  | 90.5       |
| 35K  | 208.3      |
| 45K  | 303.0      |
| 55K  | 378.6      |
| 65K  | 422.0      |
| **75K** | **499.6** (peak) |
| 85K  | 451.9      |
| 95K  | 364.1      |
| **105K** | **448.3** (final) |

Peak eval_return = **499.6** @ step 75K. Final = **448.3** @ 105K.

## NVE Trajectory

NVE = (value_mean / eval_return) / baseline_VE_ratio, where baseline = exp_001_baseline (vanilla DreamerV3 seed 1).

| Step | value_mean | eval_return | VE ratio | baseline VE | **NVE** |
|------|-----------|------------|----------|-------------|---------|
| 35K  | 80.5      | 208.3      | 0.387    | 0.241       | **1.61** |
| 45K  | 138.4     | 303.0      | 0.457    | 0.331       | 1.38    |
| 55K  | 193.7     | 378.6      | 0.512    | 0.404       | 1.27    |
| 65K  | 248.1     | 422.0      | 0.588    | 0.563       | 1.04    |
| 75K  | 298.0     | 499.6      | 0.597    | 0.719       | 0.83    |
| 85K  | 341.5     | 451.9      | 0.756    | 0.701       | 1.08    |
| 95K  | 382.3     | 364.1      | 1.050    | 0.632       | **1.66** |
| 105K | 394.5     | 448.3      | 0.880    | 0.656       | 1.34    |

- **Peak NVE** = 1.66× @ step 95K
- **Final NVE** = 1.34× @ step 105K
- **Mean NVE (45K-105K)** = 1.23×
- NVE > 1.5× at 2 eval points: 35K (1.61×, borderline — baseline denominator = 0.241 ≈ stability threshold) and 95K (1.66×, driven by eval_return dip to 364.1)

## Late Instability

Train returns at the final batch (step 112K): **33.2, 106.9, 108.8, 11.7** — a dramatic drop from the 104K batch (437, 536, 423, 356). This suggests policy destabilization beginning after 105K, though no formal eval confirms this (last eval was at 105K: 448.3).

## Comparison with Prior Experiments

| Experiment | Config | NVE peak | Outcome |
|-----------|--------|----------|---------|
| exp_008f (no dt_emb) | dt_embed_dim=0, subsample ON, H=8 | ≤1.14× | Healthy (no CIVO) |
| exp_008d (trained dt_emb) | trained dt_emb, subsample ON, H=8 | **4.12×** @ 55K | CIVO confirmed |
| exp_016e (reward-only SGS) | SGS on reward decoder only | **10.42×** | Catastrophic collapse |
| **exp_018v2 (full SGS)** | **full_sgs=True, detach all non-KL** | **1.66×** @ 95K | **NVE substantially reduced** |

### CIVO Reduction Analysis
- 008d excess NVE (above 1.0×) = 3.12
- 018v2 excess NVE (above 1.0×) = 0.66
- **Reduction: 79% of excess NVE eliminated by Full-SGS**

## Interpretation

1. **Full-SGS is highly effective**: Detaching all non-KL gradients from dt_emb reduced CIVO by ~80%. The NVE trajectory is dramatically healthier than 008d, staying in the 0.83-1.38× range for most of training (45K-85K).

2. **Residual overestimation persists**: NVE still briefly exceeds 1.5× at step 95K (driven by an eval_return dip coinciding with rising value_mean). This suggests additional CIVO mechanisms beyond obs decoder gradients, or that Full-SGS doesn't fully eliminate all pathological gradient interactions.

3. **Late instability**: The train_return collapse at 112K (4 episodes with returns 11-108) suggests the policy may be entering an unstable regime even with Full-SGS. However, this is after the configured training steps and lacks eval confirmation.

4. **C5 partially supported**: Obs decoder gradients are a **major** contributor to CIVO (accounting for ~80% of excess NVE), but not the sole root cause. The remaining ~20% excess may come from:
   - Reward decoder gradient interactions not fully blocked
   - Implicit information leakage through KL gradients (which are not detached)
   - Stochastic variance in NVE measurement

## Significance for Paper

- **Positive**: Full-SGS provides strong evidence that obs decoder gradients are the primary CIVO mechanism. The 79% reduction is a compelling experimental result.
- **Limitation**: The intervention doesn't fully eliminate CIVO below the 1.5× threshold at all eval points, weakening the "necessary and sufficient" claim for C5.
- **Suggested framing**: "Full-SGS reduces CIVO by ~80%, identifying observation decoder gradients as the dominant (but not sole) driver of pathological value inflation in temporal-embedding-augmented world models."
- **Next steps**: Consider whether the residual 20% comes from eval noise (run additional seeds) or genuine secondary CIVO mechanisms.

## Value Loss Trajectory

| Step | value_loss |
|------|-----------|
| 5K   | 9.3       |
| 15K  | 3.1       |
| 25K  | 1.7       |
| 35K  | 1.2       |
| 45K  | 1.0       |
| 55K  | 0.9       |
| 65K  | 1.0       |
| 75K  | 0.9       |
| 85K  | 0.8       |
| 95K  | 0.9       |
| 105K | 0.6       |

Value loss was monotonically stable/decreasing throughout — no pathological spike as seen in 008d/016e.
