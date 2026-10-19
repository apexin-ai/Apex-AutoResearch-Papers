# exp_001a: R1-Distill-Qwen-32B Hidden State Extraction + Probing

**Date**: 2026-05-17  
**Model**: DeepSeek-R1-Distill-Qwen-32B (64 layers, hidden_dim=5120, Qwen2 arch)  
**Dataset**: HarmThoughts r1-32b traces  
**GPU**: RTX PRO 6000 (98GB), cuda:0

---

## Phase 1: Hidden State Extraction

| Metric | Value |
|--------|-------|
| Traces extracted | 100 |
| Total steps | 3,506 |
| Total tokens processed | 64,727 |
| Hidden state shape | [num_sentences, 64, 5120] |
| Output size | 2.2 GB |
| Errors | 0 |
| GPU memory (model) | ~66 GB |

Output: `artifacts/hidden_states_r1_32b/` (100 .pt files)

---

## Phase 2: Layer Sweep (64 layers, LogisticRegression)

**Best layer by score (crossing_rate x lead_mean)**: Layer 2

| Rank | Layer | Acc | F1 | Crossing Rate | Lead Mean | Lead Median | Score |
|------|-------|-----|-----|---------------|-----------|-------------|-------|
| 1 | 2 | 0.6195 | 0.5410 | 0.5500 | 13.82 | 14.0 | 7.60 |
| 2 | 1 | 0.6268 | 0.5538 | 0.5500 | 11.36 | 11.0 | 6.25 |
| 3 | 0 | 0.6397 | 0.5625 | 0.6500 | 8.54 | 6.0 | 5.55 |
| 4 | 20 | 0.6746 | 0.5931 | 0.4000 | 13.38 | 8.0 | 5.35 |
| 5 | 15 | 0.6710 | 0.5885 | 0.4000 | 13.25 | 7.0 | 5.30 |

Top-7 layers: [2, 1, 0, 20, 15, 10, 16]

**Notable**: Best accuracy is at deeper layers (63: 0.7426, 56: 0.7261), but early layers (0-2) have higher crossing rates and lead times. The score metric favors early detection capability.

Output: `artifacts/exp_001a/layer_sweep_results.json`

---

## Phase 3: Temporal LR Probes (layer 2)

| Window | Acc | F1 | Crossing Rate | Lead Mean | Lead Median |
|--------|-----|-----|---------------|-----------|-------------|
| 5 | 0.6287 | 0.5324 | 0.5500 | 10.64 | 11.0 |
| 10 | 0.6710 | 0.5623 | 0.5000 | 9.00 | 9.5 |
| 15 | 0.6985 | 0.5961 | 0.5000 | 7.30 | 5.5 |

Accuracy improves with larger windows, but lead time decreases (expected tradeoff).

Output: `artifacts/exp_001a/temporal_lr_results.json`

---

## Phase 4: GRU 3-seed (layers [2, 1, 0, 20, 15, 10, 16])

| Seed | Acc | Crossing Rate | Lead Mean | Lead Median |
|------|-----|---------------|-----------|-------------|
| 42 | 0.6163 | 0.5500 | 10.55 | 9.0 |
| 123 | 0.6144 | 0.7000 | 10.79 | 7.5 |
| 456 | 0.5530 | 0.7500 | 12.27 | 10.0 |
| **Aggregate** | **0.5946 +/- 0.029** | **0.6667 +/- 0.085** | **11.20 +/- 0.76** | **8.83 +/- 1.03** |

GRU achieves higher crossing rate (66.7%) than static/temporal LR (50-55%), with comparable lead time (~11 steps ahead of commitment point).

Output: `artifacts/exp_001a/gru_results.json`

---

## Phase 5: Pre-CP FPR Bootstrap Test

| Metric | Temporal LR (w=15) | GRU |
|--------|-------------------|-----|
| Pre-CP FPR (mean) | 0.2728 | 0.3902 |
| Pre-CP FPR (std) | 0.2714 | 0.2943 |

**Paired Bootstrap (GRU - LR)**:
- Observed diff: 0.1174
- p-value: 0.539 (not significant)
- 95% CI: [0.012, 0.229]

The difference in pre-CP FPR between GRU and temporal LR is not statistically significant (p=0.54).

Output: `artifacts/exp_001a/bootstrap_fpr_results.json`

---

## Comparison: R1-32B vs R1-8B

| Metric | R1-8B (layer 14, 13 layers, 4096d) | R1-32B (layer 2, 64 layers, 5120d) |
|--------|-------------------------------------|-------------------------------------|
| Best layer acc | ~0.82 | 0.62 |
| Best crossing rate (LR) | ~77% | 55% |
| GRU crossing rate | ~85% | 66.7% |
| GRU lead mean | ~5-7 steps | 11.2 steps |
| Num traces | ~209 | 100 |

**Key observations**:
1. R1-32B shows lower step accuracy than R1-8B, possibly because the 32B model has more subtle internal transitions
2. R1-32B early layers (0-2) show the strongest signal by score metric, unlike R1-8B where mid layers (14) were best
3. Lead times are longer for R1-32B (~11 steps vs ~5-7 for R1-8B), suggesting earlier pre-commitment signals at the cost of lower accuracy
4. Fewer traces (100 vs 209) reduce statistical power
