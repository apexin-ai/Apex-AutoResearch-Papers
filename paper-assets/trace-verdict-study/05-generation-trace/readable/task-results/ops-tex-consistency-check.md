# ops tex consistency check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tex_consistency_check_20260521T004006_result.json`
- **Structured JSON:** [`08fef4dc622b7dee9957.json`](../../sessions/08/08fef4dc622b7dee9957.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

method.tex 用的是 `figure*`（双栏通栏），所以 `\begin{figure}` 没匹配到，正常。

---

## 汇报

### 1. 旧数字残留

| 值 | 匹配数 | 判定 |
|---|---|---|
| **67.31** | 0 | 已清除，无残留 |
| **12.23** | 0 | 已清除，无残留 |
| **12.2** | 0 | 已清除，无残留 |
| **9.16** | 11 处 | **全部为 99.16 或 79.16**，无独立 9.16 |

9.16 详细匹配（均合理，无需修复）：
- `99.16%` — DeepSeek VOTA seed 123 的正确结果，出现在 appendix.tex (8, 243, 259, 262, 638, 654) 和 experiments.tex (40, 61)
- `79.16%` — DeepSeek full_trace 重跑结果，出现在 appendix.tex (25, 246) 和 main.tex (43)

**结论：全部 4 个旧数字已无残留，无需修复。**

### 2. 交叉引用完整性

| 检查项 | 结果 |
|---|---|
| undefined references | 无（main.log 无匹配） |
| multiply-defined labels | 无 |

**Table 统计**：22 个 `\begin{table}`，21 个 `\label{tab:}`。差 1 个是 arr_checklist.tex 的表格（无需 label，合理）。

**Figure 统计**：5 个 `\begin{figure}` + 1 个 `\begin{figure*}`（method.tex），共 6 个 figure 环境；6 个 `\label{fig:}`。**一一对应，完整。**

**结论：交叉引用完整，无问题。**

### 3. codellama 进度

| 项 | 值 |
|---|---|
| PID | 654451，存活 |
| 运行时间 | 3h 20m 49s |
| 进度 | **408/444 steps (92%)** |
| 速度 | ~27-28s/step |
| 预计剩余 | **~17 分钟**（36 steps × 28s） |
| eval 结果 | 尚未生成 |

训练即将完成，eval 会在 444 step 后自动运行。

---
