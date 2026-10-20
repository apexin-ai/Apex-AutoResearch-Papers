# NVE Threshold Sensitivity Analysis (B2: Any CIVO Detection)

Generated: 2026-05-24

Data source: Appendix Table complete_results (all Walker + Cheetah seeds with NVE values)

## All Environments (Walker + Cheetah, n=32, AUROC=0.961)

n = 32 (n_pos = 11, n_neg = 21)

| Threshold | TP | FP | FN | TN | Accuracy [95% CI] | TPR | FPR | Precision | F1 |
|-----------|----|----|----|----|-------------------|-----|-----|-----------|-----|
| 1.3x | 11 | 6 | 0 | 15 | 81.2% [65.0%, 94.8%] | 1.000 | 0.286 | 0.647 | 0.786 |
| 1.5x | 11 | 3 | 0 | 18 | 90.6% [76.9%, 100.0%] | 1.000 | 0.143 | 0.786 | 0.880 |
| 1.7x | 8 | 3 | 3 | 18 | 81.2% [65.0%, 94.8%] | 0.727 | 0.143 | 0.727 | 0.727 |
| 2.0x | 8 | 1 | 3 | 20 | 87.5% [72.8%, 98.9%] | 0.727 | 0.048 | 0.889 | 0.800 |

**False positives at 1.5x:**
- 047: NVE=1.71x (frozen s1, transient self-corr (not CIVO))
- 057: NVE=1.88x (frozen s2, transient self-corr (not CIVO))
- 008e_v3_s2: NVE=3.78x (IRD, non-CIVO)

## Walker Walk (n=23, AUROC=0.925)

n = 23 (n_pos = 8, n_neg = 15)

| Threshold | TP | FP | FN | TN | Accuracy [95% CI] | TPR | FPR | Precision | F1 |
|-----------|----|----|----|----|-------------------|-----|-----|-----------|-----|
| 1.3x | 8 | 5 | 0 | 10 | 78.3% [58.0%, 95.1%] | 1.000 | 0.333 | 0.615 | 0.762 |
| 1.5x | 8 | 3 | 0 | 12 | 87.0% [68.7%, 100.0%] | 1.000 | 0.200 | 0.727 | 0.842 |
| 1.7x | 5 | 3 | 3 | 12 | 73.9% [53.0%, 92.0%] | 0.625 | 0.200 | 0.625 | 0.625 |
| 2.0x | 5 | 1 | 3 | 14 | 82.6% [63.2%, 97.9%] | 0.625 | 0.067 | 0.833 | 0.714 |

**False positives at 1.5x:**
- 047: NVE=1.71x (frozen s1, transient self-corr (not CIVO))
- 057: NVE=1.88x (frozen s2, transient self-corr (not CIVO))
- 008e_v3_s2: NVE=3.78x (IRD, non-CIVO)

## Cheetah Run (n=9, AUROC=1.000)

n = 9 (n_pos = 3, n_neg = 6)

| Threshold | TP | FP | FN | TN | Accuracy [95% CI] | TPR | FPR | Precision | F1 |
|-----------|----|----|----|----|-------------------|-----|-----|-----------|-----|
| 1.3x | 3 | 1 | 0 | 5 | 88.9% [56.4%, 100.0%] | 1.000 | 0.167 | 0.750 | 0.857 |
| 1.5x | 3 | 0 | 0 | 6 | 100.0% [72.3%, 100.0%] | 1.000 | 0.000 | 1.000 | 1.000 |
| 1.7x | 3 | 0 | 0 | 6 | 100.0% [72.3%, 100.0%] | 1.000 | 0.000 | 1.000 | 1.000 |
| 2.0x | 3 | 0 | 0 | 6 | 100.0% [72.3%, 100.0%] | 1.000 | 0.000 | 1.000 | 1.000 |


## Per-Experiment Data

| Experiment | Env | NVE Peak | CIVO (B2) | Mechanism |
|-----------|-----|----------|-----------|-----------|
| 010b_s0 | cheetah | 108.52x | **+** | trained dt_emb, full collapse |
| 021 | cheetah | 9.94x | **+** | SGS cheetah, transient CIVO |
| 010b | cheetah | 8.27x | **+** | trained dt_emb, collapsed |
| 006 | walker | 4.83x | **+** | trained dt_emb, sustained CIVO |
| 059_s5 | walker | 4.72x | **+** | trained dt_emb, self-correcting CIVO |
| 008d_s4 | walker | 4.62x | **+** | trained dt_emb, full collapse |
| 008d_s1 | walker | 4.12x | **+** | trained dt_emb, full collapse |
| 008e_v3_s3 | walker | 4.02x | **+** | CIVO collapse |
| 008e_v3_s2 | walker | 3.78x | - | IRD, non-CIVO |
| 057 | walker | 1.88x | - | frozen s2, transient self-corr (not CIVO) |
| 047 | walker | 1.71x | - | frozen s1, transient self-corr (not CIVO) |
| 018_s1 | walker | 1.66x | **+** | Full-SGS, partial mitig (CIVO+) |
| 009b_s2 | walker | 1.62x | **+** | trained dt_emb, transient CIVO |
| 008d_s3 | walker | 1.53x | **+** | trained dt_emb, late-onset |
| 015b | walker | 1.45x | - | frozen emb, grad starvation |
| 008f_s4 | walker | 1.41x | - | no dt_emb |
| 046 | cheetah | 1.35x | - | frozen, no CIVO |
| 008a_ch_s1 | cheetah | 1.29x | - | unexposed emb |
| 008a_ch_s0 | cheetah | 1.08x | - | unexposed emb |
| 009c_s3 | walker | 1.04x | - | no dt_emb |
| 001_s1 | walker | 1.00x | - | baseline |
| 008e_v3_s4 | walker | 0.99x | - | mitigation s4 |
| 008f_s1 | walker | 0.97x | - | no dt_emb |
| 008e_v3_s1 | walker | 0.94x | - | mitigation s1 |
| 008a_s0 | walker | 0.93x | - | unexposed emb |
| 008a_s2 | walker | 0.89x | - | unexposed emb |
| 008a_s1 | walker | 0.83x | - | unexposed emb |
| 058 | cheetah | 0.78x | - | frozen, no CIVO |
| 022b | walker | 0.63x | - | frozen+Gumbel |
| 024b_s0 | cheetah | 0.20x | - | no dt_emb |
| 042 | walker | 0.19x | - | frozen dedicated |
| 024b_s1 | cheetah | 0.10x | - | no dt_emb |
