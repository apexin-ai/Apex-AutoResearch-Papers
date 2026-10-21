# analysis verify figure3 dynamics data

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_figure3_dynamics_data_20260519T150006_result.json`
- **Structured JSON:** [`609944ff9e23202e7064.json`](../../sessions/60/609944ff9e23202e7064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the conclusion:

---

## 验证结果

### 1. 训练 dynamics 图不是主文 Figure 3

训练 dynamics 图是**附录图**（`appendix.tex:245-247`，`\label{fig:training_dynamics}`），不是主文 Figure 3。主文 Figure 3 是 `fig:cross_model_gap`（跨模型准确率柱状图，由 `gen_fig3.py` 生成）。

### 2. 绘图脚本与数据源

绘图脚本是 `/root/trace-verdict-study/eval/plot_dynamics.py`，通过 `--full_trace` 参数接收 `dynamics_log.jsonl` 路径。脚本本身不硬编码路径，图例标签写的是 **"Full-trace"**。

数据来自 `qwen7b_full_trace_dynamics_seed42`，该实验训练时**确实带了 `--label_only_loss`**。

### 3. Caption 原文

> `appendix.tex:246`: "Training dynamics for `exception_only` (blue, circles) and **`full_trace`** (red, squares) on Qwen-2.5-7B (seed=42, N=1,190). ... `full_trace` plateaus around 88%."

Caption 只写了 `full_trace`，**没有提到 "label-only loss"**。

### 4. 结论：存在不一致，但方向与 Director 担心的相反

| | Caption 说的 | 实际数据 |
|--|--|--|
| Director 担心 | "Full-trace with label-only loss" | 普通 full_trace |
| **实际情况** | **`full_trace`**（未提 label-only loss） | **full_trace + `--label_only_loss`** |

- Caption **漏标了** label-only loss，不是错标。
- 实际绘制的数据确实是 label-only-loss 版本（accuracy ~88%，与主文 `experiments.tex:89` 报告的 label-only loss 结果 86.22% 接近，而非普通 full_trace 的 81.76%）。
- **不存在**普通 full_trace 的 dynamics 实验——registry 中只有带 `--label_only_loss` 的版本。

### 建议修改

Caption 应改为明确说明是 label-only loss 变体，例如将 `full_trace` 改为 `full_trace (label-only loss)` 或 "Full-trace with label-only loss"，以与 `experiments.tex:89` 中对该变体的描述保持一致。

---
