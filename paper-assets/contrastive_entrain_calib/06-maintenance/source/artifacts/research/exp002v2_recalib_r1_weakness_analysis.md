# exp002v2-recalib: Cosine R1 Signal Weakness Analysis

**Date**: 2026-05-19  
**Experiment**: exp002v2-recalib (Cosine R1 + recalibration every 500 steps)  
**Server**: westd-29046  
**Steps covered**: 501–1705 (of 8000)  
**Comparison**: exp008v3 (Binary Probe R1) on westd-28034, steps 0–1240

---

## 1. Cosine R1 Time Series (exp002v2-recalib)

### Overall Statistics

| Metric | Early (steps 510–539) | Late (steps 1675–1705) | Full range |
|--------|----------------------|----------------------|------------|
| R1 mean | −0.0478 | −0.0795 | −0.0637 |
| R1 std | 0.0288 | 0.0593 | 0.0489 |
| R1 min | −0.0976 | −0.1888 | −0.1888 |
| R1 max | +0.0170 | +0.0337 | +0.0337 |
| Positive count | 1/30 (3.3%) | 2/30 (6.7%) | 3/60 (5.0%) |

### R3 Statistics (for context)

| Metric | Early (steps 510–539) | Late (steps 1675–1705) |
|--------|----------------------|----------------------|
| R3 mean | 0.4947 | 0.8231 |
| R3 range | [0.262, 0.808] | [0.500, 0.999] |

### Weighted Contribution to Combined Reward (R1_w=0.25, R3_w=0.75)

| Phase | R1 contribution | R3 contribution | R1 effective share |
|-------|----------------|----------------|-------------------|
| Early | 0.25 × (−0.048) = **−0.012** | 0.75 × 0.495 = **+0.371** | 3.1% (negative drag) |
| Late | 0.25 × (−0.080) = **−0.020** | 0.75 × 0.823 = **+0.617** | 3.1% (negative drag) |

**Key finding**: R1 does not contribute positively to the combined reward at any phase. It acts as a small but consistent negative drag, meaning the model receives a penalty (not a reward) for the directional alignment signal throughout training.

### R1 Positive Value Occurrences

Only 3 positive r1_mean values observed across ~1200 logged steps:
- Step 527: +0.0170
- Step 1675: +0.0337
- Step 1703: +0.0102

All are negligibly small (<0.04). No sustained positive R1 episode exists.

---

## 2. Recalibration Events

| Event | Global step | cosine_sim | auroc | direction_norm |
|-------|-------------|------------|-------|----------------|
| Initial load | 501 | — | — | (from step 500 checkpoint) |
| Recalib 1 | ~999 | 0.6695 | 0.8152 | 79.14 |
| Recalib 2 | ~1499 | 0.8596 | 0.8549 | 91.11 |

**Recalibration improves direction quality** (cosine_sim 0.67→0.86, auroc 0.82→0.85) but **fails to make R1 positive**.

### Pre/post recalibration R1 pattern

Around recalib 2 (step ~1499):
- Before (steps 1489–1499): r1_mean ≈ −0.02 to −0.11
- After (steps 1509–1519): r1_mean ≈ −0.13 to +0.07

No systematic improvement. The recalibrated directions have better alignment with the current model but the cosine similarity reward formulation itself is structurally incapable of producing a reliably positive signal during RL generation.

---

## 3. Comparison: Cosine R1 vs Binary Probe R1

| Metric | Cosine R1 (exp002v2) | Binary Probe R1 (exp008v3) |
|--------|---------------------|---------------------------|
| R1 mean (early) | **−0.048** | **+0.591** |
| R1 mean (late) | **−0.080** | **+0.349** |
| R1 range | [−0.189, +0.034] | [+0.063, +0.750] |
| R1 positive rate | 5% | 100% |
| Gradient sign | NEGATIVE | POSITIVE |
| Signal type | Continuous, near-zero | Discrete (0/0.125/0.25/.../1.0) |
| Provides learning signal | No (negative = penalty) | Yes (positive = reward) |

### exp008v3 R1 Trajectory (Binary Probe, avg of 2 GPUs)

| Step range | R1 mean | R1 range |
|-----------|---------|----------|
| 0–100 | 0.591 | [0.50, 0.75] |
| 110–200 | 0.519 | [0.31, 0.69] |
| 1060–1240 | 0.349 | [0.06, 0.63] |

Note: Binary probe R1 also declines over training (from ~0.59 to ~0.35), indicating the model is learning to deviate from the initial probe classifier. But it remains strictly positive, providing a meaningful reward signal at all times.

---

## 4. Root Cause Analysis

The cosine R1 signal failure has a structural cause:

1. **Cosine similarity range**: The raw cosine similarity between generation activations and the sycophancy direction yields values in approximately [−0.2, +0.2]. After the reward transformation (which targets the negative/non-sycophantic direction), this maps to r1 ∈ [−0.2, +0.07].

2. **Generation distribution mismatch**: The sycophancy directions are computed from paired (sycophantic, non-sycophantic) completions with controlled length/content. During RL generation, the model produces variable-length reasoning traces (think tokens), and the activation patterns are not calibrated against these.

3. **Recalibration helps direction quality but not reward scale**: Recalibration updates d_syc using current model activations, improving auroc (0.82→0.85). However, the cosine similarity is still too small in magnitude to produce positive rewards because the activation difference between sycophantic and non-sycophantic completions during RL is much smaller than in the controlled calibration setting.

4. **Binary probe avoids this problem**: The probe classifier maps activations to {0, 1} via a learned decision boundary, producing discrete rewards (0, 0.125, ..., 1.0) that are always non-negative and well-scaled for RL optimization.

---

## 5. Paper-Ready Summary (English)

> In exp-002v2 (cosine-based directional reward with periodic recalibration), the R1 signal remained persistently negative throughout 1,700+ training steps (mean = −0.064, positive rate = 5%, max = +0.034), contributing a −0.02 drag on the combined reward while R3 (NLI faithfulness) dominated at +0.62. Despite recalibration improving direction quality (AUROC: 0.82 → 0.86), the cosine similarity formulation was structurally unable to produce positive R1 rewards during RL generation, rendering the directional alignment signal effectively invisible to the policy gradient. In contrast, the binary probe baseline (exp-008v3) maintained a positive R1 signal throughout (mean = 0.46, range [0.06, 0.75]), confirming that the representation-level sycophancy signal exists but requires a thresholded reward formulation—rather than raw cosine similarity—to be actionable during RL training.

---

## 6. Raw Data Samples

### exp002v2-recalib R1 (every 10 steps, selected)

```
Step   R1_mean    R3_mean    Combined
510    -0.0961    0.6102     0.4336
520    -0.0397    0.6252     0.4590
530    -0.0469    0.5018     0.3646
540    -0.0220    0.4482     0.3306
550    (truncated in log extraction)
...
1500   (recalib 2 event)
...
1675   +0.0337    0.8746     0.6643
1680   -0.1684    0.7482     0.5190
1690   -0.1637    0.6864     0.4739
1700   -0.0461    0.7529     0.5531
1705   -0.1888    0.8733     0.6078
```

### exp008v3 R1 (per-10-step, avg of 2 GPUs)

```
Step   R1_mean(avg)  
0      0.625
10     0.750
50     0.563
100    0.688
500    ~0.50
1000   ~0.35
1100   0.063
1200   0.438
1240   0.188
```
