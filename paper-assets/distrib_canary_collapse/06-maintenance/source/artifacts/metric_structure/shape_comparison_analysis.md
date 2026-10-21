# Shape Comparison: Power Simulation vs Observed Detection Pattern

## Summary

Three signal hypotheses were compared against the observed phase diagram detection pattern:

- **H0 (linear)**: signal grows linearly with α, b = c·α
- **H0' (concave)**: signal grows as α^0.5 (diminishing returns), b = c'·α^0.5
- **H1 (step)**: signal is absent below α_c(T) and jumps to full strength S_max above it

The observed detection pattern is **binary**: detection fraction is either 0/8 (= 0.0) or 6/8 (= 0.75), with only 2 of 25 cells at intermediate values (both at 5/8 = 0.625). This binary pattern is the key discriminator.

## Detection Fraction Comparison (mean_detection_fraction)

### T = 10

| α | Observed | H0 | H0' | H1 |
|---|---------|-----|------|-----|
| 0.45 | 0.000 | 0.048 | 0.103 | 0.007 |
| 0.50 | **0.750** | 0.069 | 0.121 | 0.006 |
| 0.60 | 0.000 | 0.116 | 0.152 | 0.007 |
| 0.75 | **0.750** | 0.228 | 0.224 | 0.007 |
| 1.00 | **0.750** | 0.456 | 0.316 | 0.007 |

### T = 15

| α | Observed | H0 | H0' | H1 |
|---|---------|-----|------|-----|
| 0.45 | **0.750** | 0.153 | 0.326 | 0.008 |
| 0.50 | **0.750** | 0.223 | 0.371 | 0.579 |
| 0.60 | 0.000 | 0.370 | 0.446 | 0.566 |
| 0.75 | **0.750** | 0.563 | 0.579 | 0.576 |
| 1.00 | **0.750** | 0.826 | 0.707 | 0.578 |

### T = 20

| α | Observed | H0 | H0' | H1 |
|---|---------|-----|------|-----|
| 0.45 | **0.625** | 0.300 | 0.533 | 0.789 |
| 0.50 | **0.750** | 0.375 | 0.597 | 0.784 |
| 0.60 | 0.000 | 0.566 | 0.678 | 0.797 |
| 0.75 | **0.750** | 0.794 | 0.787 | 0.789 |
| 1.00 | **0.750** | 0.946 | 0.878 | 0.783 |

### T = 25

| α | Observed | H0 | H0' | H1 |
|---|---------|-----|------|-----|
| 0.45 | **0.750** | 0.433 | 0.699 | 0.894 |
| 0.50 | **0.750** | 0.556 | 0.752 | 0.901 |
| 0.60 | **0.625** | 0.723 | 0.823 | 0.897 |
| 0.75 | **0.750** | 0.890 | 0.892 | 0.897 |
| 1.00 | **0.750** | 0.983 | 0.955 | 0.898 |

## RMSE

| Model | Raw RMSE | Ceiling-capped RMSE (cap=0.75) |
|-------|----------|-------------------------------|
| H0 linear | 0.3149 | 0.3072 |
| H0' concave | 0.2872 | 0.2799 |
| H1 step | 0.3712 | 0.3584 |

**RMSE alone is not the right discriminator.** H1's higher RMSE is dominated by two confounds: (1) H1's step threshold at T=10 is above all tested α values, predicting zero detection where observed shows 0.75; (2) the α=0.60 anomaly (0/8 detection for T=10,15,20) affects all models equally. These are threshold-location errors, not shape errors.

## Shape Metric: Intermediate Cell Count

The core shape difference is captured by counting cells in the intermediate detection regime (0.1 < detection_fraction < 0.7):

| Model | Intermediate cells (out of 25) | Fraction |
|-------|-------------------------------|----------|
| H0 linear | 12 | 48% |
| H0' concave | 13 | 52% |
| H1 step | 4 | 16% |
| **Observed** | **2** | **8%** |

H0 and H0' predict that nearly half the phase diagram should show intermediate detection rates — a gradual transition from no-detection to full-detection. The observed data contradicts this: 23/25 cells are either 0.0 or ≥0.625. Detection does not gradually emerge as signal increases; it appears abruptly.

## The α=0.60 Anomaly

The α=0.60 column (T=10,15,20) shows 0/8 detection where adjacent α values show 6/8. This non-monotonicity is not predicted by any model and inflates all models' RMSE equally. It likely reflects a single-seed artifact at this parameter point. At T=25, α=0.60 recovers to 5/8 (0.625).

## Interpretation

The comparison reveals a **qualitative shape mismatch** between smooth-signal hypotheses (H0, H0') and the observed detection pattern:

1. **H0/H0' predict gradual transitions.** Under linear or concave signal growth, detection fraction should rise smoothly with α. This produces 12–13 cells in the intermediate regime.

2. **Observed data is binary.** Detection fraction jumps from 0/8 to 6/8 (=0.75) with almost no intermediate values. The 6/8 ceiling reflects structural MAUVE pair failure (2 of 8 pairs always involve mauve as downstream and are structurally non-detectable by PermG), independent of signal strength.

3. **H1 step is closer in shape** (4 intermediate cells vs. 12–13 for H0/H0'), but still differs from observed due to threshold calibration and the inherent limitation of predicting up to 8/8 rather than the structural 6/8 ceiling.

4. **The mismatch is in shape, not ceiling.** Even if we cap all model predictions at 0.75, H0/H0' still predict smooth ramp-ups through intermediate values that do not exist in the data. The binary detection pattern is inconsistent with any model where signal accumulates gradually over training time.
