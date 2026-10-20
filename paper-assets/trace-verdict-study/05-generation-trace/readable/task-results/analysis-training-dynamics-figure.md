# analysis training dynamics figure

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training_dynamics_figure_20260522T061727_result.json`
- **Structured JSON:** [`3a289e3f4d6581678619.json`](../../sessions/3a/3a289e3f4d6581678619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已完成。标注位置不再交叠，两个 Panel 清晰可读。

**输出文件（服务器 westd-11235）**：
- `/root/autodl-tmp/trace-verdict-study-checkpoints/training_dynamics_figure/training_dynamics.pdf` (300 DPI)
- `/root/autodl-tmp/trace-verdict-study-checkpoints/training_dynamics_figure/training_dynamics.png` (300 DPI)

**数据摘要**：
- 每条曲线 44 个 loss 数据点（每 10 步记录一次，步数 10-444）
- 9 个 eval accuracy 数据点（每 50 步，步数 50-444）
- Exception-Only: loss [0.0300, 0.9563], accuracy 饱和于 step 200 (99.8%)
- Full-Trace: loss [0.0077, 6.7824], best accuracy step 350 (88.82%)

**Panel (a)** 三处标注：exception_only 饱和点、full_trace 最大振荡（−5.3pp）、full_trace 最优点。  
**Panel (b)** 对数坐标 loss 曲线 + 终值标注 + "Lower loss ≠ better generalization" 注释。

---
