# Intervention Threshold Sensitivity Sweep

## Overview

Simulated different entropy-drop thresholds (5–50%) on counterfactual α-sweep data
to determine optimal intervention trigger timing and false alarm rates.

## Data Sources

- **Counterfactual trajectories**: α ∈ {0.00, 0.10, 0.25, 0.50, 0.75, 1.00} (no intervention)
- **Intervention experiments**: 3 predictive + 2 reactive runs
- **Null baseline**: α=0.00 (pure real data, no contamination)

## Key Findings

### 1. Trigger Timing

| α | Max Entropy Drop (%) | Trigger at 15% | Trigger at 25% | Trigger at 30% |
|---|---------------------|----------------|----------------|----------------|
| 0.00 | 7.5 | — | — | — |
| 0.10 | 7.7 | — | — | — |
| 0.25 | 7.8 | — | — | — |
| 0.50 | 22.4 | 1 | — | — |
| 0.75 | 35.3 | 1 | 1 | 1 |
| 1.00 | 62.1 | 1 | 1 | 1 |

### 2. False Alarm Analysis (α=0.00)

- Max entropy drop on null: **7.5%**
- **Threshold = 5% triggers false alarm** on null (null drop = 7.5%)
- **All thresholds ≥ 10% produce zero false alarms**

### 3. Detection Boundaries

- **α = 0.10**: max drop 7.7% → detectable at threshold ≤ 7%
- **α = 0.25**: max drop 7.8% → detectable at threshold ≤ 7%
- **α = 0.50**: max drop 22.4% → detectable at threshold ≤ 22%
- **α = 0.75**: max drop 35.3% → detectable at threshold ≤ 35%
- **α = 1.00**: max drop 62.1% → detectable at threshold ≤ 62%

### 4. PPL Recovery from Intervention

- **pred_a075_s42**: peak PPL reduction = 73.2% at gen 10 (interv=20.8 vs cf=77.7)
- **pred_a100_s43**: peak PPL reduction = 98.4% at gen 10 (interv=16.7 vs cf=1017.8)
- **react_a100_s43_fp32**: peak PPL reduction = 97.9% at gen 10 (interv=21.4 vs cf=1017.8)
- **react_a100_s43_bf16**: peak PPL reduction = 98.4% at gen 10 (interv=16.5 vs cf=1017.8)
- **pred_14b_s42**: peak PPL reduction = 98.3% at gen 10 (interv=17.6 vs cf=1017.8)

### 5. Recommended Operating Point

- **Threshold = 15%**: catches α ≥ 0.50 at gen 1, zero false alarms on null
- **Threshold = 10%**: catches α ≥ 0.50 at gen 1, zero false alarms (same detection as 15%)
- **Threshold = 25%**: misses α = 0.50, catches α ≥ 0.75 (most conservative)
- **Threshold = 5%**: catches α ≥ 0.10 but triggers false alarm on null — not recommended

## Artifacts

- `threshold_sensitivity.csv` — trigger gen × threshold × α
- `intervention_ppl_reduction.csv` — PPL reduction per gen per experiment
- `fig_threshold_timing.pdf` — trigger gen vs threshold
- `fig_threshold_ppl.pdf` — PPL trajectories: intervention vs counterfactual
- `fig_roc_detection.pdf` — detection–false alarm tradeoff
