# Falcon3-7B-Base Algorithm 1 Classification

## Parameters
τ = 1.0pp, σ = 5.0pp (default thresholds)

## MMLU 5-shot Classification
- Δ(d100−d000) = **+4.19 pp**
- Pattern: **Benefit**
- Confidence: 1.000
- Trajectory: Monotonic increase across all 5 dosages. Steps: d000→d005 +0.25pp, d005→d025 +2.21pp, d025→d050 +0.86pp, d050→d100 +0.87pp. First-half gain (d000→d025) = +2.46pp, second-half gain (d025→d100) = +1.73pp, ratio = 0.703 (above 0.3 saturation threshold). No dips below baseline.

## ARC 25-shot Classification
- Δ(d100−d000) = **+4.01 pp**
- Pattern: **Benefit-sat**
- Confidence: 0.601
- Trajectory: Non-monotonic — d025→d050 dip of −1.53pp, then recovery d050→d100 +2.30pp. First-half gain (d000→d025) = +3.24pp, second-half gain (d025→d100) = +0.77pp, ratio = 0.238 (below 0.3 saturation threshold, triggers Benefit-sat). Late gain (d050→d100) = +2.30pp is above 0.5pp floor, so saturation is driven by the second/first ratio, not late stall.

## Combined Classification
- **MMLU**: Benefit (strong, monotonic)
- **ARC**: Benefit-sat (saturating, non-monotonic mid-trajectory)
- Overall: **Benefit / Benefit-sat** — Falcon3 benefits from contaminated SFT data on both benchmarks, with ARC showing early saturation.

## Cross-Family Comparison (MMLU, sorted by Δ)

| Family | d000 | d100 | Δ(d100−d000) | Pattern | Confidence |
|--------|------|------|---------------|---------|------------|
| Qwen2.5-14B | 69.44 | 60.07 | −9.37 pp | U-collapse | 0.937 |
| Qwen2.5-7B | 66.11 | 64.33 | −1.78 pp | V-recovery | 0.618 |
| Phi-4 14.7B | 76.44 | 76.27 | −0.17 pp | Immune | 0.915 |
| LLaMA-3.1 8B | 53.50 | 52.81 | −0.69 pp | Immune | — |
| OLMo-2 7B | 53.79 | 57.00 | +3.21 pp | Benefit-sat | 0.515 |
| Gemma-2 9B | 61.86 | 65.62 | +3.76 pp | Benefit | 1.000 |
| **Falcon3-7B** | **58.77** | **62.96** | **+4.19 pp** | **Benefit** | **1.000** |

Falcon3 has the largest positive MMLU delta among all 7 families, slightly exceeding Gemma-2 (+3.76pp). Both are high-confidence Benefit patterns. Falcon3 slots into the "Benefit cluster" alongside Gemma-2 and OLMo-2, distinct from the Immune models (Phi-4, LLaMA-3.1) and negative-direction models (Qwen-14B Collapse, Qwen-7B V-recovery). Note: LLaMA-3.1 only has 3 dosage points (d000/d025/d100); confidence not computed.

## Dose-Response Profiles

```
MMLU 5-shot:
  d000  d005  d025  d050  d100
  58.77 59.02 61.23 62.09 62.96  Falcon3  [Benefit, +4.19pp]
  61.86 63.56 64.19 64.73 65.62  Gemma-2  [Benefit, +3.76pp]
  53.79 55.17 56.06 56.53 57.00  OLMo-2   [Benefit-sat, +3.21pp]

ARC 25-shot:
  d000  d005  d025  d050  d100
  81.57 83.11 84.81 83.28 85.58  Falcon3  [Benefit-sat, +4.01pp]
```
