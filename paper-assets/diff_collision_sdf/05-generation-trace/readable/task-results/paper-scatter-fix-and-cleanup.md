# paper scatter fix and cleanup

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_scatter_fix_and_cleanup_20260524T232821_result.json`
- **Structured JSON:** [`8dcfd09992cc1012fbbb.json`](../../sessions/8d/8dcfd09992cc1012fbbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 项任务完成（任务 5 是验证步骤，已贯穿执行），编译无错误。

---

## 修改汇总

| # | 任务 | 操作 |
|---|------|------|
| 1 | Scatter plot 标签重叠 | 重写 `fig_tsr_car_scatter.pdf`：左侧 7 点改 letter-based (a)-(g) + 右下 legend box；Pi0.5+A1 居中标注；Pi0.5 单标签指向 cluster 中心；移除 spatial 点 |
| 2 | TODO 清理 | 删除 main.tex 第 3 行和第 76 行的 2 条 `% TODO` 注释 |
| 3 | 旧文件归档 | `experiments.tex`、`method.tex`、`conclusion_DEPRECATED.tex` → `docs/paper/_archive/` |
| 4 | 未引用 labels | 删除 6 个未引用 subsection labels：`sec:rw_sdf`、`sec:rw_eval`、`sec:benchmark`、`sec:models`、`sec:oracle_setup`、`sec:sdf_gt` |

---
