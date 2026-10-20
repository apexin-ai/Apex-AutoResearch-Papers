# R9 CPU Analysis Bundle

Server files: `analysis_output/r9_*.json` on westd-22162

## 1. Post-hoc Power Analysis (GSM8K n=50)
- 9/16 conditions power ≥ 0.80
- DS importance: all ≥ 0.949 (well-powered)
- QW importance s025/s030: >0.999
- Low-sparsity random: underpowered (power 0.09-0.47, expected)

## 2. II_high ≤ 0 (MATH-500 n=500)
- Importance: 25-53% problems have II_high ≤ 0
- Current: keep all (no exclusion)
- Sensitivity: core conclusions unchanged after exclusion

## 3. G× D082 Confirmation
- DS: 21.08-36.46× (vs expected 21.1-36.2×, rounding-level)
- QW: 43.94-63.95× (matches)
- R9-W1: CAN_CLOSE

## 4. Outlier Case Study (gsm8k_189)
- DS/random/s030 problem idx=34, gradient=-1042.98
- Diagnosis: NUMERICAL ARTIFACT (15 low-sparsity segments, extreme PPL)
- Median robust: excluding outlier changes gradient 1.69→1.80
