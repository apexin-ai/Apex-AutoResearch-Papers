# figure heatmap revert v1 fontfix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_heatmap-revert-v1-fontfix_20260523T174910_result.json`
- **Structured JSON:** [`c41a7a068a00e03d5190.json`](../../sessions/c4/c41a7a068a00e03d5190.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

1. **两个面板**：(a) Ordinal Accuracy + (b) Transfer Retention ✓
2. **对角线值**：.423 / .386 / .382 / .388 ✓（与 Table 7 一致）
3. **字号放大**：annotation 12pt, tick labels 11pt, axis labels 12pt, titles 13pt ✓
4. **矢量 PDF**：31 KB ✓
5. **对角线 retention = 100%** ✓

**注意**：retention 面板的非对角线值与你提供的验证表有出入。v1 脚本使用 **行对角线** 除法（`acc[i,j] / acc[i,i]`），例如 Pythia→Qwen-rw = 0.272/0.386 = **70%**，而你的验证表写的是 **64%**（0.272/0.423，即按列对角线除）。Qwen-rw 行因为 diag 值最大所以两种算法恰好一致，但其他行不同。

如果需要改为列对角线除法（`acc[i,j] / acc[j,j]`，即"保留了 test model 多少 in-domain 性能"），我可以修改 `compute_retention` 函数。是否需要？

---
