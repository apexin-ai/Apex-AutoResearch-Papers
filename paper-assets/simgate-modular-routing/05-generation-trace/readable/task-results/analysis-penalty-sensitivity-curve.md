# analysis penalty sensitivity curve

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_penalty-sensitivity-curve_20260515T185824_result.json`
- **Structured JSON:** [`55f53133b3262694e7f7.json`](../../sessions/55/55f53133b3262694e7f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**数据验证通过：**
- N=245, DAF(100)=90.41% ✓, Δ_full=29.60 ✓, Δ_nd=2.84 ✓
- Death rates: internal=42.9%, det=16.3% ✓
- DAF 随 P 单调递增 ✓

**结果表：**

| P | Δ_full(P) | DAF(%) | 95% CI |
|---|-----------|--------|--------|
| 0 | 3.07 | 7.5 | [-36.7, 83.1] |
| 10 | 5.72 | 50.4 | [19.8, 94.5] |
| 25 | 9.70 | 70.8 | [48.5, 97.1] |
| 50 | 16.33 | 82.6 | [67.6, 98.4] |
| 100 | 29.60 | **90.4** | [81.5, 99.1] |
| 200 | 56.13 | 95.0 | [90.0, 99.5] |
| 500 | 135.72 | 97.9 | [95.8, 99.8] |

**R6-C1 论证要点：** P=0 时 DAF 降至 7.5%（CI 跨零），确认 DAF 确实依赖 penalty 大小。但在 ScienceWorld 默认 P=100 下 DAF=90.4%，且即使 P 减半至 50，DAF 仍有 82.6%。结合 penalty-independent 的 death-asymmetry label fraction (78.9%)，可双线论证死亡不对称性的稳健性。

**产出已注册：**
- `penalty_vs_daf.pdf/png` (chart)
- `penalty_sensitivity_curve_data.json` (data)
- `penalty_sensitivity_table.tex` (LaTeX table)
- Registry: `plan-012-penalty-curve` → DONE

---
