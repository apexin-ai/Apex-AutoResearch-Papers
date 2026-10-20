# fix paper figures r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper-figures-r3_20260514T235336_result.json`
- **Structured JSON:** [`ce2433d14659d033e78e.json`](../../sessions/ce/ce2433d14659d033e78e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 图 | 修改前大小 | 修改后大小 | 变化 |
|---|---|---|---|
| fig1_sta_overview.pdf | 39744 | 39744 | 无变化（预期：title 未改） |
| fig2_isr_collapse.pdf | 25052 | 25052 | 无变化（预期：数据未改） |
| fig3_hacking_composition.pdf | 22481 | 22481 | 无变化（预期：数据未改） |
| fig4_prolog_comparison.pdf | 32663 | **32669** | **+6 bytes ✓** |

fig4 文件大小变化 (+6 bytes)，说明修改生效。其他 3 个图因为没有代码改动所以大小不变（代码已在上一轮修改，本轮仅改了 fig4 数据）。

### 汇总

**脚本路径**: `/root/solver-trace-ablation/scripts/generate_figures.py`

**本轮修改**:
- 行 239: `fol_isr = [0.1324, 0, 0.5816]` → `fol_isr = [0.1324, 0.13, 0.5816]`
  - s43 FOL ISR 从 0 改为 0.13（greedy eval 结果）
  - fig4(a) 中 s43 的 FOL 柱子标签从 "0.000" 变为 "0.130"

**之前已完成的修复（上一轮 worker 已改代码且已生成 PDF）**:
- Fix 1: 所有图的 label 已经是 "Non-hacking"（无 "Genuine"）
- Fix 2: fig2 已包含 H7 堆叠柱状图，数据与任务要求一致
- Fix 4: fig1(b) 标题已改为 `(b) Formalization\nLeave-One-Out Ablation`（双行，fontsize=8）

**Warning**: fig2 和 fig4 的 `tight_layout` 有 UserWarning（Axes 不兼容），不影响输出。

---
