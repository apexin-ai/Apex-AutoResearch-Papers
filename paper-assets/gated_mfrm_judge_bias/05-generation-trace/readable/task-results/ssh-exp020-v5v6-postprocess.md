# ssh exp020 v5v6 postprocess

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp020-v5v6-postprocess_20260525T155751_result.json`
- **Structured JSON:** [`b0b5ca70684b8a6c8cec.json`](../../sessions/b0/b0b5ca70684b8a6c8cec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**v5 (contamination-only correction)**: τ = 0.706，比 raw_average 的 0.824 **下降** 0.118。contamination penalty 过度矫正了——因为 c_n 值普遍偏大（mean_e_i ≈ 0.21 对所有模型几乎相同），高 c_n 模型（如 gpt-4-turbo: c=4.0）被惩罚过重，排名严重下滑。contamination-only correction 无正向价值。

**v6 (shrinkage α-sweep)**: α*=0.1 时 τ=0.838（Δτ=+0.015 vs raw_average），ρ=0.936。10% G-MFRM + 90% raw_average 的混合略优于纯 raw_average。α≥0.4 后 τ 退化到 0.809（G-MFRM 水平）。部分校正有微弱正向价值，但提升幅度小。

端点验证通过：α=0 → τ=0.824（raw_average），α=1 → τ=0.809（G-MFRM）。

结果已保存到 `/root/gated_mfrm_judge_bias/v5v6_results.txt`。

---
