# Exp 001b: QwQ-32B Hidden State Extraction + Probing

## Summary

Completed all 5 phases of QwQ-32B probing on autodl-rtx6000 (GPU: cuda:1, RTX PRO 6000).

---

## Phase 1: Hidden State Extraction

| Metric | Value |
|--------|-------|
| Model | QwQ-32B (64 layers, hidden_dim=5120) |
| Traces extracted | 95 (jailbreak with commitment point) |
| Total steps | 4,852 |
| Total tokens processed | 78,641 |
| Output size | 3.18 GB |
| Per-trace shape | [num_sentences, 64, 5120] |
| Errors | 0 |
| GPU memory peak | ~67.4 GB |
| Extraction time | ~46s (after model load) |

Output: `artifacts/hidden_states_qwq_32b/` (95 .pt files)

---

## Phase 2: Layer Sweep (64 layers, LogisticRegression)

Split: train=57, val=19, test=19

**Top 10 layers by score (crossing_rate x lead_mean):**

| Layer | Acc | F1 | CrossRate | LeadMean | LeadMedian | Score |
|-------|------|------|-----------|----------|------------|-------|
| 1 | 0.7366 | 0.5985 | 0.4737 | 16.33 | 16.00 | 7.74 |
| 2 | 0.7483 | 0.6070 | 0.4737 | 16.11 | 16.00 | 7.63 |
| 4 | 0.7502 | 0.5940 | 0.3684 | 19.29 | 22.00 | 7.11 |
| 5 | 0.7502 | 0.5978 | 0.3684 | 17.43 | 22.00 | 6.42 |
| 0 | 0.7434 | 0.5951 | 0.4737 | 13.33 | 14.00 | 6.32 |
| 6 | 0.7580 | 0.6016 | 0.3158 | 20.00 | 22.00 | 6.32 |
| 3 | 0.7405 | 0.5782 | 0.4211 | 13.62 | 11.00 | 5.74 |
| 42 | 0.7590 | 0.5679 | 0.4211 | 13.12 | 12.50 | 5.53 |
| 8 | 0.7590 | 0.5694 | 0.3158 | 16.83 | 12.50 | 5.32 |
| 41 | 0.7638 | 0.5714 | 0.3684 | 14.00 | 10.50 | 5.16 |

**Key finding**: Best layers are early (0-6), not middle layers. Contrasts with R1-8B where layer 14 (out of 32) was best.

---

## Phase 3: Temporal LR Probes (best layer=1)

| Window | Acc | CrossRate | LeadMean | LeadMedian |
|--------|------|-----------|----------|------------|
| 5 | 0.7182 | 0.5263 | 16.60 | 16.50 |
| 10 | 0.7370 | 0.4211 | 21.88 | 20.50 |
| 15 | 0.7358 | 0.4737 | 15.67 | 18.00 |

Best by lead_mean: window=10 (21.88 steps lead time).

---

## Phase 4: GRU 3-seed (layers [1,2,4,5,0,6,3], hidden=256, dropout=0.3)

| Seed | Acc | CrossRate | LeadMean | LeadMedian | BestEpoch |
|------|------|-----------|----------|------------|-----------|
| 42 | 0.7059 | 0.6316 | 13.50 | 11.00 | 18 |
| 123 | 0.7163 | 0.4737 | 11.89 | 13.00 | 24 |
| 456 | 0.7155 | 0.7895 | 11.93 | 9.00 | 28 |

**Mean +/- Std:**
- Acc: 0.7126 +/- 0.0047
- CrossRate: 0.6316 +/- 0.1289
- LeadMean: 12.44 +/- 0.75
- LeadMedian: 11.00 +/- 1.63

---

## Phase 5: Pre-CP FPR Bootstrap Test

| Metric | HS Probe | Text Baseline |
|--------|----------|---------------|
| Pre-CP FPR (mean) | 0.1644 | 0.3122 |
| Pre-CP FPR (std) | 0.1960 | 0.1743 |
| Overall FPR | 0.1992 | 0.3672 |

**Paired Bootstrap (1000 resamples):**
- Observed diff (HS - Text): -0.1478
- p-value: 0.001
- 95% CI: [-0.248, -0.047]

HS probe has significantly lower pre-CP FPR than text baseline (p=0.001).

---

## Comparison: QwQ-32B vs R1-8B

| Metric | R1-8B | QwQ-32B |
|--------|-------|---------|
| Architecture | Llama 8B (32 layers, 4096 dim) | Qwen2 32B (64 layers, 5120 dim) |
| Traces | 268 | 95 |
| Best LR layer | 14 (middle) | 1 (early) |
| LR best acc | 0.8114 | 0.7366 |
| LR crossing_rate | 0.1860 | 0.4737 |
| LR lead_mean | ~1-2 steps | 16.33 steps |
| Temporal LR best acc | 0.836 (w=10) | 0.737 (w=10) |
| Temporal LR crossing_rate | 0.651 | 0.421 |
| Temporal LR lead_mean | -0.61 | 21.88 |
| GRU crossing_rate | N/A (single seed) | 0.632 +/- 0.129 |
| GRU lead_mean | N/A | 12.44 +/- 0.75 |

### Key Observations

1. **Early layers dominate in QwQ-32B**: Best signal in layers 0-6, unlike R1-8B (layer 14). QwQ encodes safety-relevant representations differently.

2. **Lower accuracy but much higher lead times**: QwQ probes have lower step accuracy (~73% vs ~81%) but dramatically better lead times (16-22 steps vs ~0 for R1-8B).

3. **Higher crossing rates for QwQ**: Static LR achieves 47% crossing rate vs 19% for R1-8B. GRU reaches 63%.

4. **Fewer traces (95 vs 268)**: Smaller QwQ dataset may contribute to lower accuracy and higher variance.

5. **Bootstrap confirms HS advantage**: Pre-CP FPR significantly lower for HS probes vs text baseline (p=0.001), supporting Claim 1.
