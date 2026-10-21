# ssh conll freeform diagnostic

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_conll_freeform_diagnostic_20260522T093133_result.json`
- **Structured JSON:** [`e102267aca7740369b9c.json`](../../sessions/e1/e102267aca7740369b9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```
CoNLL Constrained vs Free-Form Diagnostic (N=8, T=1.0)
All metrics on gold-nonempty instances (n=2756), entity-level micro-F1

| Metric             | Constrained (s42) | Free-Form (4-seed mean±σ) | Δ      |
|--------------------|-------------------|---------------------------|--------|
| Degeneracy %       | 56.7              | 59.3±0.6                  | +2.6   |
| MV Δ (pp)          | +0.20             | -0.00±0.23                | -0.21  |
| LP-F1 ρ            | 0.402             | 0.392±0.004               | -0.010 |
| LP-best Δ (pp)     | -1.62             | -1.45±0.20                | +0.17  |
| Greedy F1          | 91.2              | 91.0±0.1                  | -0.2   |
| Oracle F1          | 95.4              | 95.3±0.2                  | -0.2   |
```

**Per-seed detail:**

| Seed | Degen% | MV Δ pp | LP-F1 ρ | LP-best Δ pp | Greedy F1 | Oracle F1 |
|------|--------|---------|---------|-------------|-----------|-----------|
| 42   | 59.6   | -0.29   | 0.391   | -1.60       | 90.94     | 95.32     |
| 123  | 59.7   | +0.18   | 0.397   | -1.63       | 91.06     | 95.34     |
| 456  | 59.7   | -0.10   | 0.392   | -1.33       | 91.01     | 94.97     |
| 789  | 58.4   | +0.19   | 0.387   | -1.23       | 90.95     | 95.49     |

关键发现：
- **Degeneracy 略高** (+2.6pp)：free-form 比 constrained 退化更严重，可能因为无约束时 offset 抖动不改变 entity text/type，但 (text, type, start, end) 匹配下这些算不同 sample，所以实际效果可能更复杂
- **MV Δ 几乎为零**：constrained 下 MV 带来 +0.20pp 提升，free-form 下 MV 增益消失
- **LP-F1 ρ 略低**：0.392 vs 0.402，差异不大
- **LP-best Δ 略好**：-1.45 vs -1.62，free-form 的 LP-best 劣化略小
- **Greedy/Oracle F1** 整体低约 0.2pp，符合无 grammar 约束的预期

注意：constrained LP-F1 ρ 用的是我在 exp002_conll2003 上一致计算的 0.402，与任务模板给的 0.411 略有差异（可能因计算口径不同）。

---
