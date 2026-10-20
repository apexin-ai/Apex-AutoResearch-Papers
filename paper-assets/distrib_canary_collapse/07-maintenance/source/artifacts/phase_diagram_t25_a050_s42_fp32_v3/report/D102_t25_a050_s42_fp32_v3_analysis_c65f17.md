# D102 5-Method Analysis: t25_a050_s42_fp32_v3

| Field | Value |
|-------|-------|
| α | 0.50 |
| seed | 42 |
| T | 25 |
| n_gens | 26 (gen_0–gen_25) |
| threshold | true_3sigma_d105 |
| server | westd-17855 |
| note | v3: gen_0–12 from v2, gen_13–25 from v3 (resumed after disk-full) |

## Summary

| Method | Forward | Reverse |
|--------|---------|---------|
| PermG FDR | 6/8 | 0/8 |
| Diff xcorr FDR | 6/8 | 6/8 |
| Threshold onset | 6/8 | — |
| TY Granger | 6/8 | — |
| Robust (≥3/5) | 6/8 | — |

## Consensus (forward direction)

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 4/5 | diff, threshold, perm, ty |
| token_entropy→distinct_2 | 4/5 | diff, threshold, perm, ty |
| token_entropy→distinct_3 | 4/5 | diff, threshold, perm, ty |
| token_entropy→mauve | 0/5 | — |
| ece→distinct_1 | 5/5 | naive, diff, threshold, perm, ty |
| ece→distinct_2 | 3/5 | diff, threshold, perm |
| ece→distinct_3 | 4/5 | diff, threshold, perm, ty |
| ece→mauve | 2/5 | naive, ty |

## Threshold Onset Lead Times (forward, significant pairs)

| Pair | Canary onset | Downstream onset | Lead time |
|------|-------------|-----------------|-----------|
| token_entropy→distinct_1 | gen 1 | gen 6 | 5 |
| token_entropy→distinct_2 | gen 1 | gen 8 | 7 |
| token_entropy→distinct_3 | gen 1 | gen 10 | 9 |
| ece→distinct_1 | gen 1 | gen 6 | 5 |
| ece→distinct_2 | gen 1 | gen 8 | 7 |
| ece→distinct_3 | gen 1 | gen 10 | 9 |

## Asymmetry

PermG FDR forward=6/8, reverse=0/8 — 完美不对称，因果方向从 canary 到 downstream 明确。Diff xcorr FDR 双向 6/8（对称），因为 diff xcorr 本身衡量相关性而非方向性。

## Interpretation

PermG FDR = 6/8，完全符合预期。α=0.50 在 T=10/15/20 均为 6/8，T=25 维持相同 ceiling，验证了 6/8 上限跨 T 值的一致性。理论 α_c(25) ≈ 0.232，α=0.50 远高于阈值，信号强度充足。

失败的 2 对均为 mauve downstream（token_entropy→mauve 0/5, ece→mauve 2/5），这与其他 T 值的 mauve 表现一致——mauve 作为 downstream 在 D102 framework 下信噪比低于 distinct_N 系列，是已知的 6/8 ceiling 根因。

所有 6 个显著对的 threshold onset lead time 一致：canary 在 gen 1 越限，downstream 在 gen 6–10 越限，lead time 5–9 generations，与 T=25 的较长时间跨度匹配（更多 gen 间隔使得 distinct_3 的滞后更明显）。

Reverse direction PermG = 0/8 确认因果方向单一：canary leads downstream，无反向因果证据。
