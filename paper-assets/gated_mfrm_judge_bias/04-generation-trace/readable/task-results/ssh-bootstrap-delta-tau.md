# ssh bootstrap delta tau

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_bootstrap_delta_tau_20260522T233031_result.json`
- **Structured JSON:** [`64106832a83eeeee7c09.json`](../../sessions/64/64106832a83eeeee7c09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已生成。以下是完整结果：

## summary.json

| 指标 | 值 |
|------|-----|
| **Δτ mean** | 0.0273 |
| **Δτ median** | 0.0000 |
| **Δτ 95% CI** | [−0.0714, 0.0714] |
| **P(Δτ > 0)** | 0.4511 |
| **Δρ mean** | 0.0184 |
| **Δρ 95% CI** | [−0.0476, 0.0476] |
| **P(Δρ > 0)** | 0.4559 |
| **τ_G-MFRM mean** | 0.8130 |
| **τ_G-MFRM 95% CI** | [0.7143, 0.8571] |
| **P(θ_mini > θ_qwen)** | 0.8531 |
| **θ diff 95% CI** | [−0.2270, 0.7221] |

## Claim 3 判定：**UNSAFE**

**Δτ 的 95% CI 完全跨越 0 ([−0.071, 0.071])，P(Δτ>0) 仅 0.45，远低于 0.95 门槛。**

核心原因：raw_average baseline 的排名和 G-MFRM 后验排名的差异太小。raw_average 的 τ=0.786 vs G-MFRM 的 τ 均值=0.813，差距只有 ~0.03。由于 Kendall τ 在 8 个模型上是离散的（最小可分辨差 ≈ 1/28 ≈ 0.036），绝大部分后验 draw 的 G-MFRM 排名和 baseline 排名一致或仅差一个 swap。

rank swap 分析也佐证了这点：gpt-4o-mini vs qwen2.5-72b 的 θ 后验重叠显著，P(θ_mini > θ_qwen) = 0.853，θ 差的 95% CI 包含 0。这正是 G-MFRM 和 raw_average 产生 rank 分歧的那个位置。

**结论：无法用 bootstrap Δτ 检验支撑 "G-MFRM 显著优于 raw_average" 的 claim。需要重新措辞 Claim 3 或补充其他证据维度（如 contamination 校正效果、WAIC/LOO 模型比较）。**

---
