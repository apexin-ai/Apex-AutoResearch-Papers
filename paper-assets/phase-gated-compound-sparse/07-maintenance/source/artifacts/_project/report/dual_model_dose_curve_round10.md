# Dual-Model Accuracy Dose Curve — Round 10 Data

Generated: 2026-05-16 | All experiments max_new_tokens=8192

## DeepSeek-R1-Distill-Qwen-7B (n=50)

| Sparsity | Accuracy | Δ vs Dense | Trunc Rate | Trunc Count | Non-Trunc Acc | Non-Trunc (c/t) | Registry ID |
|----------|----------|------------|------------|-------------|---------------|-----------------|-------------|
| dense    | 0.74     | —          | 0.16       | 8/50        | 0.881         | 37/42           | acc_ds_dense_8k_v2 |
| s015     | 0.48     | −0.26      | 0.32       | 16/50       | 0.706         | 24/34           | acc_ds_s015_8k_v2 |
| s020     | 0.30     | −0.44      | 0.56       | 28/50       | 0.682         | 15/22           | acc_ds_s020_8k_v2 |
| s025     | 0.08     | −0.66      | 0.76       | 38/50       | 0.333         | 4/12            | acc_ds_s025_8k_v2 |
| s030     | 0.04     | −0.70      | 0.78       | 39/50       | 0.182         | 2/11            | acc_ds_s030_8k_v2 |

**Two-phase degradation pattern:**
- Phase 1 (dense→s020): Truncation-driven. Non-trunc acc degrades gently: 88.1% → 70.6% → 68.2%. Reasoning quality largely preserved.
- Phase 2 (s025+): Dual collapse. Non-trunc acc crashes: 33.3% → 18.2%. Both truncation AND reasoning quality fail.
- Inflection point: s020→s025 boundary (non-trunc acc drops 35pp)

**⚠️ s030 discrepancy**: JSON analysis shows truncated_count=39 (rate=0.78, non-trunc acc=2/11=0.182). Reviewer earlier reported 38 (rate=0.76, non-trunc acc=2/12=0.167). Difference: 1 sample in truncation classification.

## Qwen2.5-7B-Instruct (combined n=100)

| Sparsity | Batch1 (8k) | Batch2 | Combined | Δ vs Dense | Registry IDs |
|----------|-------------|--------|----------|------------|-------------|
| dense    | 22/50=0.44  | 24/50=0.48 | 46/100=**0.46** | —     | acc_qw_dense_b1_8k + acc_qw_dense_n100 |
| s015     | 23/50=0.46  | 19/50=0.38 | 42/100=**0.42** | −0.04 | acc_qw_s015_b1_8k + acc_qw_s015_n100 |
| s020     | 13/50=0.26  | 23/50=0.46 | 36/100=**0.36** | −0.10 | acc_qw_s020_b1_8k + acc_qw_s020_n100_b2_fix |
| s025     | 16/50=0.32  | 17/50=0.34 | 33/100=**0.33** | −0.13 | acc_qw_s025_b1_8k + acc_qw_s025_n100_b2_fix |
| s030     | 7/50=0.14   | 12/50=0.24 | 19/100=**0.19** | −0.27 | acc_qw_s030_b1_8k + acc_qw_s030_n100 |

**Gradual monotonic decline with late cliff:**
- dense→s020: Gentle slope (−4pp, −6pp per step)
- s020→s025: Plateau-like (−3pp)
- s025→s030: Cliff (−14pp)
- QW truncation negligible at all sparsities (2-6% at 8k)

## Cross-Model Comparison

| Sparsity | DS Accuracy | QW Accuracy | DS Non-Trunc Acc |
|----------|-------------|-------------|------------------|
| dense    | 0.74        | 0.46        | 0.881            |
| s015     | 0.48 (−35%) | 0.42 (−9%)  | 0.706            |
| s020     | 0.30 (−59%) | 0.36 (−22%) | 0.682            |
| s025     | 0.08 (−89%) | 0.33 (−28%) | 0.333            |
| s030     | 0.04 (−95%) | 0.19 (−59%) | 0.182            |

DS total drop: −70pp (0.74→0.04). QW total drop: −27pp (0.46→0.19).
DS sensitivity ~2.6× QW. Both share s025→s030 severe degradation zone.
