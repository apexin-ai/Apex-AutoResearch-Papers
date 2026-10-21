# analysis exp 018

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_018_20260523T093707_result.json`
- **Structured JSON:** [`c127e90cd4152428101e.json`](../../sessions/c1/c127e90cd4152428101e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_018 分析完成。结论：SUCCESS。**

关键结果：

| 指标 | seed42 (exp_004) | seed43 (exp_018) | 2-seed Mean±Std |
|------|------------------|------------------|-----------------|
| Eff. Rank (gen10) | 554.51 | 552.40 | 553.46±1.49 |
| SLV (gen10) | 2573.20 | 2570.09 | 2571.65±2.20 |
| PPL (gen10) | 15.20 | 15.03 | 15.11±0.12 |
| D-4 (gen10) | 0.0954 | 0.2088 | 0.1521±0.0802 |

- **Type III trajectory confirmed**：两个 seed 的 eff_rank 和 SLV 均单调递增（gen1 有微小 SLV transient dip，之后持续上升），无 spectral collapse
- **光谱指标高度可复现**：eff_rank 和 SLV 的跨 seed 相对 std <0.4%
- **D-4 跨 seed 方差较大**：seed43 在 gen10 保持 2× 于 seed42 的 D-4 (0.209 vs 0.095)，说明表面多样性比光谱结构更受随机性影响
- **PPL 涨幅一致**：seed42 +59.1%, seed43 +57.4%

Registry 已更新（metrics、conclusion=success、log_path、checkpoint_path）。报告已保存并注册到 artifacts。

---
