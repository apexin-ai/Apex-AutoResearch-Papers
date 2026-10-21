# viz nmin table1 fix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_nmin_table1_fix_20260516T001113_result.json`
- **Structured JSON:** [`1ab655c1a2dc7116e1c1.json`](../../sessions/1a/1ab655c1a2dc7116e1c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表和表格都已更新完成。

**P1-A 图表修改：**
- 去掉了 "Best: 17.639" 标注
- 添加了浅蓝色 shaded band 覆盖 n_min=2 和 n_min=3 的 effective range
- 底部标注 *Recommended: n_min = ⌊B/2⌋*
- 数据已与 3-seed 均值口径一致
- 输出 `artifacts/figures/nmin_sensitivity.pdf` + `.png` (300dpi)

**P1-B Table 1 脚注修改：**
- 脚注更新为：*"n_min=3 is the legacy implementation; n_min=2 is the recommended default via the coupling rule n_min = ⌊B/2⌋."*
- PPL 加粗保持在 n_min=3（数值最优）

---
