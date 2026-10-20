# analysis exp 019

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_019_20260524T022437_result.json`
- **Structured JSON:** [`f969a6dc73aa6cf334f0.json`](../../sessions/f9/f969a6dc73aa6cf334f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

### exp_019 (seed44) 结果

**Type II trajectory confirmed** — SLV dip at Gen2 (Δ=-5.58), then monotonic recovery to 2466.15 (+4.2%)。Gen10: eff_rank=506.95, PPL=13.39, D-4=0.2061。

### D-4 V-recovery 结论

**seed42 的 D-4 V-shaped recovery 是 1/3 outlier。** seed43 和 seed44 均为 monotonic decline（0.74→0.25, 0.73→0.21），只有 seed42 从 gen5 的 0.44 回升到 gen10 的 0.52。

关键发现：seed42 的 V-recovery 与其 gen6-10 **train_loss 异常上升** 强相关（从 1.30 升到 1.39，而其他两颗种子 train_loss 从 ~1.2 降到 ~0.9）。这表明 V-recovery 很可能是 seed42 后段训练异常的 artifact，而非 genuine seed-dependent behavior。

### 3-seed Gen10 统计

| Metric | Mean ± Std |
|--------|------------|
| SLV | 2467.21 ± 12.00 |
| eff_rank | 508.06 ± 2.81 |
| PPL | 13.54 ± 0.25 |
| D-4 (3-seed) | 0.324 ± 0.171 (high var due to seed42) |
| D-4 (excl seed42) | 0.226 ± 0.028 |

### 额外发现

`phase1_fixed_mix_r02_seed42_results.json` 实际包含 gen0-10 数据，而非预期的 gen0-5。gen6-10 部分 train_loss 行为异常，建议核实该数据的来源和可靠性。

---
