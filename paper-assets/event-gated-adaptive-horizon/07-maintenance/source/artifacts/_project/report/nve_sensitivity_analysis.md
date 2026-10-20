# NVE Sensitivity Analysis — Threshold Selection for Delusional Critic Diagnosis

**Date**: 2026-05-15
**Task**: plan_034

## 1. Experiment Groups

### Positive Class (Trained dt_emb, expected high NVE)
| Experiment | Seed | Env | Notes |
|---|---|---|---|
| exp_008d_subsample_on_h8 | 1 | cheetah | Collapsed (eval 167→83) |
| exp_009b_008d_walker_s2 | 2 | walker | Self-corrected (nve 2.05x@25K→0.38x@105K) |
| exp_006_fixed_dt2 | 0 | cheetah | Collapsed (eval 485→133) |

### Negative Class (No/Untrained dt_emb, expected low NVE)
| Experiment | Seed | Env | Notes |
|---|---|---|---|
| exp_008f_no_dt_embed_subsample_on_h8 | 1 | cheetah | dt_embed_dim=0, recovered to 503@105K |
| exp_009c_008f_walker_s2 | 2 | walker | dt_embed_dim=0, declined after 75K |
| exp_008a_no_subsample_dt2 | 0 | cheetah | Untrained dt_emb, recovered to 778@105K |
| exp_008c_no_subsample_dt2_h8 | 0 | cheetah | Untrained dt_emb, h8, plateau ~241 |
| exp_008e_v3_subsample_on_dt1_h15 | 1 | cheetah | Trained dt_emb but dt=1 imagination |
| exp_008e_v3_walker_s2 | 2 | walker | Trained dt_emb but dt=1; **late-onset collapse @105K** |

## 2. NVE Trajectories (step ≥ 35K)

Normalized VE = raw_ve_ratio / exp_001_ve_ratio. Baseline exp_001 (seed 1) ve: 35K=0.241, 45K=0.331, 55K=0.404, 65K=0.563, 75K=0.719, 85K=0.701, 95K=0.632, 105K=0.656.

### Positive Class

| Step | exp_008d (s1) | exp_009b (s2) | exp_006 (s0) |
|------|--------------|--------------|-------------|
| 35K  | **1.71** | **1.24** | **1.29** |
| 45K  | **2.09** | **1.62** | **1.61** |
| 55K  | **4.12** | **1.41** | **2.31** |
| 65K  | — | 0.94 | **4.83** |
| 75K  | — | 0.66 | — |
| 85K  | — | 0.51 | — |
| 95K  | — | 0.43 | — |
| 105K | — | 0.38 | — |
| **Max** | **4.12** | **1.62** | **4.83** |

exp_008d terminated at 55K (collapse). exp_006 terminated at 65K (collapse). exp_009b self-corrected after 55K.

### Negative Class

| Step | exp_008f (s1) | exp_009c (s2) | exp_008a (s0) | exp_008c (s0) | exp_008e_v3 (s1) | exp_008e_v3_s2 (s2) |
|------|-------------|-------------|-------------|-------------|-----------------|-------------------|
| 35K  | 0.73 | 0.79 | 0.65 | 0.90 | 0.94 | 1.03 |
| 45K  | 0.83 | 0.72 | 0.71 | 0.77 | 0.88 | 1.06 |
| 55K  | 0.97 | 0.66 | 0.93 | 0.72 | 0.87 | 1.02 |
| 65K  | 0.37 | 0.53 | 0.66 | 0.58 | 0.72 | 0.90 |
| 75K  | 0.42 | 0.33 | 0.75 | — | 0.73 | 0.66 |
| 85K  | 0.65 | 0.60 | 0.68 | — | 0.76 | 0.68 |
| 95K  | 0.54 | 0.90 | 0.79 | — | 0.75 | **1.34** |
| 105K | 0.30 | 1.14 | 0.59 | — | 0.80 | **3.78** |
| **Max** | **0.97** | **1.14** | **0.93** | **0.90** | **0.94** | **3.78** |

exp_008c terminated at 68K. **exp_008e_v3_s2** has late-onset collapse: NVE ≤1.06 for steps 35K–85K, then spikes to 1.34@95K and 3.78@105K.

## 3. Classification Results

### Criterion A: Single Checkpoint NVE ≥ Threshold (any step ≥ 35K)

| Threshold | TP | FP | TN | FN | Accuracy | Precision | Recall | F1 |
|-----------|----|----|----|----|----------|-----------|--------|-----|
| **1.2** | 3 | 1 | 5 | 0 | **88.9%** | 75.0% | 100% | 85.7% |
| **1.3** | 3 | 1 | 5 | 0 | **88.9%** | 75.0% | 100% | 85.7% |
| **1.5** | 3 | 1 | 5 | 0 | **88.9%** | 75.0% | 100% | 85.7% |
| **1.7** | 2 | 1 | 5 | 1 | 77.8% | 66.7% | 66.7% | 66.7% |
| **2.0** | 2 | 1 | 5 | 1 | 77.8% | 66.7% | 66.7% | 66.7% |

- FP at all thresholds: **exp_008e_v3_s2** (late-onset collapse at 105K)
- FN at ≥1.7: **exp_009b** (max NVE 1.62, self-corrected)

### Criterion B: ≥2 Consecutive Checkpoints NVE ≥ Threshold

| Threshold | TP | FP | TN | FN | Accuracy | Precision | Recall | F1 |
|-----------|----|----|----|----|----------|-----------|--------|-----|
| **1.2** | 3 | 1 | 5 | 0 | **88.9%** | 75.0% | 100% | 85.7% |
| **1.3** | 3 | 1 | 5 | 0 | **88.9%** | 75.0% | 100% | 85.7% |
| **1.5** | 2 | 0 | 6 | 1 | **88.9%** | 100% | 66.7% | 80.0% |
| **1.7** | 2 | 0 | 6 | 1 | **88.9%** | 100% | 66.7% | 80.0% |
| **2.0** | 2 | 0 | 6 | 1 | **88.9%** | 100% | 66.7% | 80.0% |

- At ≥1.5 consecutive: exp_008e_v3_s2 eliminated as FP (only 1 checkpoint ≥1.5 at 105K)
- FN at ≥1.5: exp_009b (only 1 checkpoint ≥1.5: 45K@1.62)

### Consecutive Criterion Detail

| Experiment | ≥2 consec ≥1.2 | ≥2 consec ≥1.3 | ≥2 consec ≥1.5 | ≥2 consec ≥1.7 | ≥2 consec ≥2.0 |
|---|---|---|---|---|---|
| exp_008d (P) | ✓ (35-45-55K) | ✓ (35-45-55K) | ✓ (35-45-55K) | ✓ (35-45-55K) | ✓ (45-55K) |
| exp_009b (P) | ✓ (35-45-55K) | ✓ (45-55K) | ✗ | ✗ | ✗ |
| exp_006 (P) | ✓ (35-45-55-65K) | ✓ (45-55-65K) | ✓ (45-55-65K) | ✓ (55-65K) | ✓ (55-65K) |
| exp_008f (N) | ✗ | ✗ | ✗ | ✗ | ✗ |
| exp_009c (N) | ✗ | ✗ | ✗ | ✗ | ✗ |
| exp_008a (N) | ✗ | ✗ | ✗ | ✗ | ✗ |
| exp_008c (N) | ✗ | ✗ | ✗ | ✗ | ✗ |
| exp_008e_v3 (N) | ✗ | ✗ | ✗ | ✗ | ✗ |
| exp_008e_v3_s2 (N) | ✓ (95-105K) | ✓ (95-105K) | ✗ | ✗ | ✗ |

## 4. AUROC

Using max NVE (step ≥ 35K) as the continuous score, N=9 (3 positive, 6 negative):

Scores sorted descending:
| Rank | Experiment | Max NVE | Class |
|------|-----------|---------|-------|
| 1 | exp_006 | 4.83 | P |
| 2 | exp_008d | 4.12 | P |
| 3 | exp_008e_v3_s2 | 3.78 | N |
| 4 | exp_009b | 1.62 | P |
| 5 | exp_009c | 1.14 | N |
| 6 | exp_008f | 0.97 | N |
| 7 | exp_008e_v3 | 0.94 | N |
| 8 | exp_008a | 0.93 | N |
| 9 | exp_008c | 0.90 | N |

Concordant P-N pairs: 18 total pairs, 17 concordant (exp_009b at 1.62 beats 5/6 negatives but loses to exp_008e_v3_s2 at 3.78).

**AUROC = 17/18 = 0.944**

## 5. Optimal Threshold Recommendation

**Recommended: NVE ≥ 1.5, single-checkpoint criterion**
- Accuracy 88.9%, Recall 100%, Precision 75%
- Catches all trained dt_emb experiments including the transient episode (exp_009b@45K: 1.62)
- Only FP is the special-case late-onset collapse (exp_008e_v3_s2)

**Alternative: NVE ≥ 1.5, ≥2-consecutive-checkpoint criterion**
- Accuracy 88.9%, Recall 66.7%, **Precision 100%**
- Zero false positives — eliminates exp_008e_v3_s2 FP
- Misses exp_009b (which self-corrected anyway, so this FN is arguably acceptable)
- Best for **early warning with high confidence**: if triggered, nearly certain the model has pathological value overestimation

**Trade-off**: Single-point ≥1.5 optimizes for catching all pathological episodes (high recall); consecutive ≥1.5 optimizes for actionable alerts (high precision, no false alarms).

For a practical monitoring threshold, **consecutive ≥1.5** is preferred: it generates no false positives and the only false negative (exp_009b) self-corrected without intervention.

## 6. Special Case: exp_008e_v3_s2 Late-Onset Collapse

exp_008e_v3_s2 is an unusual case:
- **Configuration**: trained dt_emb, but imagination always uses dt=1 (gating locked)
- **NVE trajectory**: stable at 0.66–1.06 from 35K–85K, then sudden onset at 95K (1.34) → 105K (3.78)
- **Collapse onset**: 95K — 60K steps after the 35K monitoring window start, and well after most trained-dt_emb pathology manifests (typically 35K–55K)
- **Mechanism**: despite dt=1 imagination, the trained dt_emb still contributes to state representation; late-stage overfit of the value function to dt_emb features can trigger delayed collapse

Classification implications:
- Under single-checkpoint criterion: always a FP (max NVE=3.78 exceeds all thresholds)
- Under consecutive criterion at ≥1.5: correctly classified as TN (only 1 checkpoint ≥1.5)
- The late onset (95K) vs. typical early onset (35K–55K) could also be used as a temporal filter, but the sample size is too small to formalize this

## 7. Summary Table

| Criterion | Best Threshold | Accuracy | Precision | Recall | AUROC | Recommendation |
|---|---|---|---|---|---|---|
| Single checkpoint | 1.2–1.5 | 88.9% | 75% | 100% | 0.944 | Screening / early warning |
| ≥2 consecutive | 1.5–2.0 | 88.9% | 100% | 66.7% | — | Confirmed diagnosis |

The 1.5x NVE threshold provides the best balance. Below 1.5x, no additional true positives are gained. Above 1.5x, recall drops without improving precision (under the consecutive criterion).
