# Micro-F1 Construction Verification (2026-05-24)

## Summary

**Construction HURTS micro-F1 across ALL datasets and ALL seeds.** The construction claim does NOT hold under micro-F1.

| Dataset | Seeds | LP micro-F1 Δ | Bootstrap p |
|---------|-------|---------------|-------------|
| FewNERD 3-epoch | 42, 456 | **-1.44±0.08pp** | 1.0000 |
| FewNERD 5-epoch | 42, 123 | **-0.89±0.02pp** | 1.0000 |
| SciERC | 42 | **-0.90pp** | 0.9469 |

Under instance-averaged F1, results are mixed (FewNERD 3ep LP +0.36±0.48pp, others negative).

---

## Full Results

### FewNERD 3-epoch

#### seed42 (fewnerd_mf4v2_seed42_v3, n=37648, 8 samples/inst)

| Method | Micro-F1 | Inst-Avg F1 |
|--------|----------|-------------|
| Greedy | 78.85% | 77.19% |
| MV θ=0.25 | 76.05% (Δ=-2.80pp) | 76.45% (Δ=-0.75pp) |
| LP θ=0.25 | 77.32% (Δ=-1.53pp) | 77.07% (Δ=-0.12pp) |

Bootstrap (B=10000):
- LP micro-F1: Δ=-1.53pp, 95%CI=[-1.69,-1.36], p=1.0000
- MV micro-F1: Δ=-2.80pp, 95%CI=[-2.97,-2.62], p=1.0000

#### seed456 (fewnerd_mf4v2_seed456, n=37648)

| Method | Micro-F1 | Inst-Avg F1 |
|--------|----------|-------------|
| Greedy | 78.89% | 77.23% |
| MV θ=0.25 | 75.88% (Δ=-3.01pp) | 77.07% (Δ=-0.15pp) |
| LP θ=0.25 | 77.53% (Δ=-1.36pp) | 78.07% (Δ=+0.84pp) |

Bootstrap (B=10000):
- LP micro-F1: Δ=-1.36pp, 95%CI=[-1.52,-1.20], p=1.0000
- MV micro-F1: Δ=-3.01pp, 95%CI=[-3.18,-2.83], p=1.0000

**Multi-seed:** micro-F1 Δ: MV=-2.90±0.10, LP=-1.44±0.08 | inst-avg Δ: MV=-0.45±0.30, LP=+0.36±0.48

---

### FewNERD 5-epoch

#### seed42 (fewnerd_5epoch_lp_seed42, n=37648)

| Method | Micro-F1 | Inst-Avg F1 |
|--------|----------|-------------|
| Greedy | 79.42% | 79.43% |
| MV θ=0.25 | 77.29% (Δ=-2.13pp) | 78.79% (Δ=-0.64pp) |
| LP θ=0.25 | 78.51% (Δ=-0.91pp) | 79.41% (Δ=-0.02pp) |

Bootstrap (B=10000):
- LP micro-F1: Δ=-0.91pp, 95%CI=[-1.05,-0.77], p=1.0000
- MV micro-F1: Δ=-2.13pp, 95%CI=[-2.28,-1.97], p=1.0000

#### seed123 (fewnerd_5epoch_s123, n=37648)

| Method | Micro-F1 | Inst-Avg F1 |
|--------|----------|-------------|
| Greedy | 79.40% | 79.42% |
| MV θ=0.25 | 77.22% (Δ=-2.17pp) | 78.31% (Δ=-1.11pp) |
| LP θ=0.25 | 78.52% (Δ=-0.88pp) | 79.19% (Δ=-0.23pp) |

Bootstrap (B=10000):
- LP micro-F1: Δ=-0.88pp, 95%CI=[-1.01,-0.74], p=1.0000
- MV micro-F1: Δ=-2.17pp, 95%CI=[-2.33,-2.02], p=1.0000

**Multi-seed:** micro-F1 Δ: MV=-2.15±0.02, LP=-0.89±0.02 | inst-avg Δ: MV=-0.87±0.24, LP=-0.12±0.10

---

### SciERC (seed42, n=551)

| Method | Micro-F1 | Inst-Avg F1 |
|--------|----------|-------------|
| Greedy | 66.51% | 64.97% |
| MV θ=0.25 | 65.39% (Δ=-1.12pp) | 64.68% (Δ=-0.29pp) |
| LP θ=0.25 | 65.61% (Δ=-0.90pp) | 64.41% (Δ=-0.55pp) |

Bootstrap (B=10000):
- LP micro-F1: Δ=-0.90pp, 95%CI=[-1.96,+0.18], p=0.9469
- MV micro-F1: Δ=-1.12pp, 95%CI=[-2.35,+0.11], p=0.9617

Paper reported greedy micro-F1 = 66.33%; we get 66.51%. Paper's "+0.32pp" was likely instance-averaged F1.

---

### Theta Sweep (FewNERD 3-epoch seed42, micro-F1)

| θ | MV | LP |
|---|----|----|
| 0.10 | 64.85% (Δ=-14.00) | 64.87% (Δ=-13.98) |
| 0.15 | 76.05% (Δ=-2.80) | 76.05% (Δ=-2.80) |
| 0.20 | 76.05% (Δ=-2.80) | 76.05% (Δ=-2.80) |
| 0.25 | 76.05% (Δ=-2.80) | 77.32% (Δ=-1.53) |
| 0.30 | 77.93% (Δ=-0.92) | 77.93% (Δ=-0.92) |
| 0.35 | 77.93% (Δ=-0.92) | 77.93% (Δ=-0.92) |
| 0.40 | 77.68% (Δ=-1.17) | 77.69% (Δ=-1.16) |
| 0.50 | 77.68% (Δ=-1.17) | 77.68% (Δ=-1.17) |

Best theta (θ=0.30-0.35) still yields -0.92pp. No threshold recovers positive micro-F1 delta.

---

## Analysis

The micro-F1 vs instance-averaged divergence is explained by **entity-count imbalance**: instances with more entities (higher weight in micro-F1) tend to have lower construction accuracy. Construction's MV/LP voting reduces recall on entity-rich instances, which disproportionately hurts pooled TP counts.

The paper's construction claim was based on instance-averaged F1 where each instance counts equally regardless of entity count. Under micro-F1 (the paper's official metric), construction consistently hurts.
