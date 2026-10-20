# QW Accuracy Dose-Response Curve (MATH-500)

> Compiled 2026-05-16 | All n=100, max_new_tokens=8192 | Model: Qwen2.5-7B-Instruct

## Summary Table

| Sparsity | Accuracy | Correct/Total | Δ vs Dense | Source exp_id |
|----------|----------|---------------|------------|---------------|
| dense    | 0.40     | 40/100        | —          | acc_qw_dense_n100 |
| s015     | 0.36     | 36/100        | -0.04 (-10.0%) | acc_qw_s015_n100 |
| s020     | 0.36     | 36/100        | -0.04 (-10.0%) | acc_qw_s020_n100_b2_fix |
| s025     | 0.33     | 33/100        | -0.07 (-17.5%) | acc_qw_s025_n100 (= b2_fix) |
| s030     | 0.19     | 19/100        | -0.21 (-52.5%) | acc_qw_s030_n100 |

## Data Completeness
- **5/5 points**: dense, s015, s020, s025, s030 — all DONE
- Monotonically decreasing (Spearman ρ = -1.0)
- Director 提供的数字 (0.40/0.36/0.36/0.33/0.19) 与 registry 完全一致 ✓

## Key Observations
1. **Gradual degradation zone** (dense→s025): -0.04 → -0.04 → -0.07, 累计 -17.5%
2. **Cliff drop** (s025→s030): -0.14 absolute, -42% relative to s025
3. **与 DS 模式对比**: DS 在 s020→s025 即出现断崖 (0.30→0.08), QW 延迟到 s025→s030
4. Cliff location 与 onset threshold (~s020-s025, D063) 及 compound severity gradient 一致

## b2_fix Note
s020 和 s025 原始 batch2 使用 max_new_tokens=2048，b2_fix 版本统一为 8192:
- s020: 0.35 → 0.36 (b2_fix)
- s025: 0.33 → 0.33 (不变)
b2_fix 为权威版本。
