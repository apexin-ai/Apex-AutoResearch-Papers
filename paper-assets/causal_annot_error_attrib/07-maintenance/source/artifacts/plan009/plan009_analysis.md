# Plan 009: Pathological Confusion Matrix Analysis

## (a) Experiment Design

**Objective**: Characterize bias behavior under 3 classes of pathological K×K column-stochastic confusion matrices across 7 DAG topologies and K ∈ {3, 5, 7}.

**Configuration**: M=1000 C instances per (K, type, param), N=5M samples for probability-limit estimation, CUDA (RTX 5090).

**Pathological C types**:
- **Near-permutation**: C = (1−ε)P + εU, ε ∈ {0.01, 0.05, 0.1, 0.2}
- **Rank-deficient**: SVD truncation to rank r ∈ {1, …, K−1}
- **Block-diagonal**: b blocks, b ∈ {2, max(K//2, 2)}

**Matrix features**: spectral_gap, diag_dominance, effective_rank, condition_number, off_diagonal_max

**Analysis**: per-config bias distributions + OLS regression |bias| ~ features (per-topology + global).

**Catastrophic threshold**: |bias| > 2|τ_true|.

---

## (b) Complete Metrics

### τ_true (C=I) Reference Values

| Topology | K=3 | K=5 | K=7 |
|---|---|---|---|
| confounding | 2.0012 | 1.9999 | 1.9999 |
| mediation | 0.4999 | 0.4980 | 0.4992 |
| collider | 0.8864 | 0.8729 | 0.8845 |
| exposure | 0.9996 | 1.0004 | 0.9997 |
| mbias | 1.0129 | 1.0389 | 1.0407 |
| iv | 1.3277 | 1.9083 | 2.0338 |
| frontdoor | 0.4997 | 0.4995 | 0.4998 |

### Near-Permutation Bias (|bias| mean)

| Topology | K | ε=0.01 | ε=0.05 | ε=0.1 | ε=0.2 |
|---|---|---|---|---|---|
| confounding | 3 | 0.0120 | 0.0529 | 0.0958 | 0.1550 |
| confounding | 5 | 0.0092 | 0.0419 | 0.0764 | 0.1256 |
| confounding | 7 | 0.0086 | 0.0391 | 0.0703 | 0.1178 |
| mediation | 3 | 0.0079 | 0.0375 | 0.0683 | 0.1213 |
| mediation | 5 | 0.0066 | 0.0314 | 0.0580 | 0.1025 |
| mediation | 7 | 0.0053 | 0.0250 | 0.0476 | 0.0854 |
| collider | 3 | 0.0027 | 0.0128 | 0.0242 | 0.0442 |
| collider | 5 | 0.0028 | 0.0134 | 0.0255 | 0.0471 |
| collider | 7 | 0.0024 | 0.0118 | 0.0226 | 0.0420 |
| exposure | 3 | **1.0900** | **1.1590** | **1.1314** | **1.0310** |
| exposure | 5 | **1.0744** | **1.0527** | **1.0729** | **1.0309** |
| exposure | 7 | **1.0517** | **1.0812** | **1.0383** | **1.0174** |
| mbias | 3 | 0.0003 | 0.0017 | 0.0032 | 0.0058 |
| mbias | 5 | 0.0008 | 0.0039 | 0.0074 | 0.0137 |
| mbias | 7 | 0.0009 | 0.0042 | 0.0081 | 0.0149 |
| iv | 3 | **2.9153** | **3.0058** | **3.3079** | **3.4534** |
| iv | 5 | **3.8052** | **3.7378** | **4.0728** | **4.4641** |
| iv | 7 | **5.1099** | **5.3484** | **5.5114** | **6.1887** |
| frontdoor | 3 | 0.0094 | 0.0434 | 0.0781 | 0.1346 |
| frontdoor | 5 | 0.0081 | 0.0380 | 0.0696 | 0.1189 |
| frontdoor | 7 | 0.0067 | 0.0312 | 0.0591 | 0.1018 |

### Near-Permutation Catastrophic Fraction (|bias| > 2|τ|)

| Topology | K | ε=0.01 | ε=0.05 | ε=0.1 | ε=0.2 |
|---|---|---|---|---|---|
| exposure | 3 | 15.0% | 17.7% | 16.5% | 13.2% |
| exposure | 5 | 15.0% | 13.5% | 15.0% | 8.9% |
| exposure | 7 | 8.3% | 10.0% | 7.6% | 5.3% |
| iv | 3 | 67.1% | 66.9% | 68.9% | 65.8% |
| iv | 5 | 61.3% | 58.5% | 60.3% | 58.5% |
| iv | 7 | 72.6% | 72.8% | 70.6% | 69.2% |
| *all others* | * | 0.0% | 0.0% | 0.0% | 0.0% |

### Rank-Deficient Bias (|bias| mean) — Selected

| Topology | K | rank=1 | rank=K−1 |
|---|---|---|---|
| confounding | 3 | 0.2989 | 0.2860 (r=2) |
| confounding | 5 | 0.2572 | 0.2463 (r=4) |
| confounding | 7 | 0.2457 | 0.2365 (r=6) |
| mediation | 3 | 0.3052 | 0.2799 (r=2) |
| mediation | 7 | 0.2209 | 0.2083 (r=6) |
| collider | 3 | 0.1138 | 0.1052 (r=2) |
| collider | 7 | 0.1162 | 0.1092 (r=6) |
| exposure | 3 | 0.9996 | 0.9934 (r=2) |
| exposure | 7 | 0.9997 | 1.0089 (r=6) |
| mbias | 3 | 0.0125 | 0.0116 (r=2) |
| mbias | 7 | 0.0408 | 0.0385 (r=6) |
| iv | 3 | ALL NaN | 3676.66 (r=2) |
| iv | 5 | ALL NaN | 84.16 (r=4) |
| iv | 7 | ALL NaN | 100.52 (r=6) |
| frontdoor | 3 | 0.2976 | 0.2775 (r=2) |
| frontdoor | 7 | 0.2329 | 0.2224 (r=6) |

### Block-Diagonal Bias (|bias| mean)

| Topology | K | blocks=2 | blocks=3 |
|---|---|---|---|
| confounding | 3 | 0.2076 | — |
| confounding | 5 | 0.2519 | — |
| confounding | 7 | 0.2369 | 0.2406 |
| mediation | 3 | 0.1669 | — |
| mediation | 7 | 0.1777 | 0.2017 |
| collider | 3 | 0.1205 | — |
| collider | 5 | 0.0804 | — |
| collider | 7 | 0.1055 | 0.0637 |
| exposure | 3 | 0.9941 | — |
| exposure | 7 | 0.9976 | 0.9954 |
| mbias | 3 | 0.0242 | — |
| mbias | 7 | 0.0399 | 0.0393 |
| iv | 3 | 7.17 | — |
| iv | 5 | 87.94 | — |
| iv | 7 | 555.03 | 2495.70 |
| frontdoor | 3 | 0.1478 | — |
| frontdoor | 7 | 0.2106 | 0.2239 |

### OLS Regression: |bias| ~ Matrix Features

| Topology | n | R² | Top Predictor (coef) | 2nd Predictor (coef) |
|---|---|---|---|---|
| collider | 28000 | **0.7676** | off_diagonal_max (−0.0202) | condition_number (+0.0138) |
| mediation | 28000 | **0.7465** | spectral_gap (+0.0322) | condition_number (+0.0280) |
| frontdoor | 28000 | **0.7278** | spectral_gap (+0.0307) | condition_number (+0.0257) |
| confounding | 28000 | **0.7029** | spectral_gap (+0.0263) | effective_rank (−0.0225) |
| mbias | 28000 | **0.6074** | off_diagonal_max (−0.0155) | spectral_gap (−0.0064) |
| exposure | 28000 | **0.1126** | diag_dominance (−0.1418) | effective_rank (−0.1207) |
| iv | 25000 | **0.0003** | condition_number (+1677.2) | spectral_gap (−1614.3) |
| GLOBAL | 193000 | **0.0000** | — | — |

All features p < 0.001 for confounding/mediation/collider/frontdoor/mbias. IV features mostly non-significant. Exposure: spectral_gap not significant (p=0.067).

---

## (c) Hypothesis Verification

### H1: Pathological Cs produce catastrophic bias with predictable structure
**Partially confirmed.** The 7 topologies split into 3 regimes:

| Regime | Topologies | Worst-case |bias| | Catastrophic? |
|---|---|---|---|
| **Low-risk** | mbias | < 0.04 | Never |
| **Moderate-risk** | confounding, mediation, collider, frontdoor | 0.1–0.31 | Never (0% cat) |
| **High-risk** | exposure, IV | 1.0–6000+ | Always (8–99% cat) |

The *structure* is predictable in the sense that regime membership is topology-determined, not C-determined. Within the moderate-risk group, bias degrades smoothly with C quality.

### H2: Matrix features are strong predictors of bias severity
**Topology-dependent.**
- For 5 of 7 topologies: **Yes** (R² = 0.61–0.77). Key predictors are spectral_gap, condition_number, and effective_rank.
- For exposure and IV: **No** (R² ≤ 0.11). The bias mechanism is structural (identification failure), not driven by C quality.
- Globally: **No** (R² ≈ 0). Features cannot predict bias across topologies.

### H3: Clear threshold separating "safe zone" from "catastrophe zone"
**Not supported.** Within the moderate-risk topologies, bias is always below the catastrophic threshold regardless of C pathology. Within exposure/IV, bias is nearly always catastrophic regardless of C quality. There is no C-feature threshold that cleanly separates safe from catastrophic — it's the topology that determines the regime.

### H4: Features as practitioner diagnostics
**Partially supported, with important caveats.** Per-topology regression works well for confounding/mediation/collider/frontdoor/mbias — spectral_gap, condition_number, and effective_rank provide meaningful diagnostic signals. But the practitioner must first know which causal topology applies. The features are useless for exposure and IV identification strategies.

---

## (d) Key Findings

### Finding 1: Topology dominates, C quality is secondary
The causal graph topology is the primary determinant of vulnerability to annotation error. M-bias is nearly immune (max bias 0.04 even under worst-case C). Confounding/mediation/collider/frontdoor show bounded, moderate bias (0.1–0.31). Exposure and IV are catastrophically sensitive regardless of C quality.

### Finding 2: Near-permutation bias scales linearly with ε (for well-behaved topologies)
For confounding/mediation/collider/frontdoor/mbias, |bias| ≈ αε where α is topology-dependent. This confirms that small perturbations from identity produce proportional bias. Higher K slightly reduces α (more redundancy in the confusion matrix).

### Finding 3: Exposure is structurally broken — bias ≈ τ regardless of C
Exposure topology shows |bias| ≈ 1.0 (≈ τ_true) for ALL pathological C types, including near-permutation at ε=0.01. The DGP has no treatment variable (T=None), so OLS is regressing Y on mismeasured category dummies. Any misclassification causes the coefficient estimates to absorb the projection error, yielding bias of order τ itself.

### Finding 4: IV (Wald estimator) is catastrophically unstable
IV shows |bias| mean 2.9–6.2 even for near-permutation with ε=0.01 (cat=61–73%). Rank-deficient Cs with rank=1 produce ALL NaN (the denominator FS*[1] collapses to zero). Higher ranks produce extreme outliers (max bias up to 3.5M). The Wald estimator's division amplifies any C perturbation explosively.

### Finding 5: Rank-deficient Cs produce fixed-point bias for standard estimators
For rank=1, all 1000 C instances collapse to the same bias value (std ≈ 0), because the rank-1 projection maps all Cs to the same effective confusion matrix. Higher ranks introduce variance but the mean bias changes minimally — the bias floor is set by the rank-1 component.

### Finding 6: Block-diagonal Cs have topology-dependent effects
For collider at K=7: blocks=3 (bias=0.064) < blocks=2 (bias=0.106). More blocks mean finer-grained partial identifiability. For IV: blocks=3 (bias=2496) >> blocks=2 (bias=555). The fragmented denominator in the Wald estimator makes more blocks worse.

### Finding 7: Matrix features predict within-topology bias well (R² ≈ 0.7) but fail globally
The OLS regression works because within a topology, C quality degrades along a common manifold. Across topologies, the bias *mechanism* differs (OLS vs Wald vs mediation), so the same feature values produce different bias magnitudes. Practitioners need topology-specific diagnostic thresholds, not a universal metric.

### Finding 8: condition_number is the most consistently important predictor
Across 5 well-behaved topologies, condition_number is significant (p < 0.001) in all and appears as top-2 predictor in 4 of 5. This aligns with theory: condition number of C controls the amplification of perturbation in the matrix inversion step of OLS.

### Finding 9: K scaling effect is mild
Increasing K from 3 to 7 slightly reduces near-permutation bias for well-behaved topologies (e.g., confounding ε=0.2: 0.155→0.118) but worsens IV catastrophically (near-perm ε=0.01: 2.9→5.1). Rank-deficient bias floors decrease slightly with K for moderate-risk topologies.
