# code fix analysis script methodology

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-analysis-script-methodology_20260521T140807_result.json`
- **Structured JSON:** [`cff3b87d007adbec784b.json`](../../sessions/cf/cff3b87d007adbec784b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个修复全部生效，脚本运行成功。

### 修复总结

**Fix (a) — ΔCAR 不再混合不同 step 的 seed**
- `plot_delta()` 改为仅用 2-seed 50K（s0+s2），同一 checkpoint step
- 新增 `plot_delta_3seed()` 预留 3-seed 版本，检测到 `OCC s1 50K` 数据后自动生成
- 输出：`delta_car_2seed.pdf/.png`（旧 `delta_car.png` 保留为历史）

**Fix (b) — 统一用 20r 数据对比**
- 新增 `VANILLA_20R_AVG_CAR` 字典（3-seed 20r 平均 CAR）
- 所有对比图和表格的 vanilla baseline 从 50r 改为 20r
- Table 2 标题改为 `(all 20r)`，学习曲线中 vanilla CAR baseline 标注 `20r`
- TSR baseline 仍用 50r（无 20r 数据），已在图例中标注 `50r`

**Fix (c) — T9 标注无 OCC supervision**
- `NO_OCC_TASKS = {9}` + `task_label()` 函数自动为 T9 加 `†`
- 所有图表的 x 轴/y 轴标签：`T9 †`
- 所有图表底部脚注：`† T9: no OCC supervision (missing in occ_index.json)`
- 表格中 T9 行和脚注都已标注

### 生成的图表
- `/root/occsafe_vla/figures/learning_curve.pdf/.png`
- `/root/occsafe_vla/figures/car_heatmap.pdf/.png`
- `/root/occsafe_vla/figures/delta_car_2seed.pdf/.png`
- `delta_car_3seed` 已跳过（等 OCC s1 50K 数据）

---
