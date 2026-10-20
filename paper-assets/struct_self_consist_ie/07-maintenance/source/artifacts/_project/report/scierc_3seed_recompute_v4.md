## SciERC 3-Seed Full Metrics Recompute (MF4v2, N=8, T=1.0)

Computed 2026-05-21 on autodl-5090 from scierc_mf4v2_seed{42,123,456}/samples.jsonl

### 3-Seed Summary (mean ± σ)

| Metric | mean ± σ |
|--------|----------|
| Greedy F1 | 0.6669 ± 0.0009 |
| Oracle F1 | 0.7808 ± 0.0023 |
| MV F1 (strict >N/2) | 0.6596 ± 0.0040 |
| Δ_SC (mv - greedy) | −0.74 ± 0.57 pp |
| δ (degeneracy) | 12.2% ± 1.0% |
| α_crit = F1_gr/2 | 0.3335 ± 0.0005 |
| Consensus Construct F1 | 0.6701 ± 0.0034 |
| Selection F1 (LP) | 0.6669 ± 0.0035 |
| Selection F1 (SJ) | 0.6621 ± 0.0036 |

### Signal ρ (full-set, Spearman)

| Signal | ρ (mean ± σ) |
|--------|-------------|
| VC | +0.3977 ± 0.0112 |
| SJ | +0.3654 ± 0.0097 |
| EM | +0.3119 ± 0.0123 |
| FK | +0.2599 ± 0.0166 |
| LP | +0.2164 ± 0.0047 |

### Signal ρ (conditional, greedy F1>0)

| Signal | ρ (mean ± σ) |
|--------|-------------|
| EM | +0.3805 ± 0.0211 |
| VC | +0.3261 ± 0.0187 |
| SJ | +0.3242 ± 0.0137 |
| FK | +0.1770 ± 0.0170 |
| LP | +0.1590 ± 0.0058 |

Note: ESJ/MRSC/LSC require model inference (hidden-state extraction), cannot compute from samples.jsonl alone.
Remote file: /root/autodl-tmp/struct_self_consist_ie/scierc_3seed_recompute_results.txt