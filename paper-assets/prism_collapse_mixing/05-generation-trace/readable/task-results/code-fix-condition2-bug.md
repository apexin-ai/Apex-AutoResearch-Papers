# code fix condition2 bug

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_condition2_bug_20260515T231047_result.json`
- **Structured JSON:** [`fb055dacd3da5e416a2a.json`](../../sessions/fb/fb055dacd3da5e416a2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都运行成功。

### 修改总结

**analyze_correlation.py — Condition 2 bug 修复**:
- 删除了 `mean_key` / `means` 相关逻辑（旧代码错误地检查 `entropy_mean` / `spectral_rank_mean` 聚合均值的单调下降）
- 新逻辑：对每代的 `|ρ(loss, signal)|` 序列检查单调递减且总下降 ≥15%
  - `abs_rhos = [abs(r) for r in rhos]`
  - `drop_frac = (abs_rhos[0] - abs_rhos[-1]) / abs_rhos[0] >= 0.15`

**plot_results.py — 三项增强**:
1. **rho decay 图**：新增 `spectral_rank` 的 ρ 曲线（虚线），entropy 用实线区分
2. **y 轴**：`set_ylim(-1.05, 1.05)`，容纳负 ρ 值；对称阈值线 ±0.5 / ±0.7
3. **分布图**：对每个 seed 各生成一张 `fig_signal_distributions_seed{N}.pdf`

**Dry-run 验证（Gen0→Gen1）**:
- entropy |ρ|: 0.9292 → 0.9118（下降 1.9%，<15%，cond2=N）
- spectral |ρ|: 0.2110 → 0.2050（下降 2.8%，<15%，cond2=N）
- 符合预期：只有 2 代数据，条件尚未满足

---
