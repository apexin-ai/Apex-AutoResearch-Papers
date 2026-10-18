# figure fig1a count curves

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1a_count_curves_20260516T225757_result.json`
- **Structured JSON:** [`3a9a0118398481718667.json`](../../sessions/3a/3a9a0118398481718667.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图生成完成。

## 实验进度

| 数据集 | seed | 完成文件 | 状态 |
|--------|------|----------|------|
| FewRel | 42 | 7/7 (count_4,8,16,32,40,64,80) | **完成** |
| Few-NERD | 42 | 6/6 (count_2,6,12,22,44,66) | **完成** |
| FewRel | 123 | 5/7 (缺 count_8, count_80) | **运行中** (tmux d051_batch2) |
| Few-NERD | 123 | 0 | 未开始 |
| FewRel | 456 | 0 | 未开始 |
| Few-NERD | 456 | 0 | 未开始 |

## Figure 1a 数据摘要

**FewRel (accuracy)**: 0.870 → 0.805 → 0.719 → 0.652 → 0.606 → 0.539 → 0.504 [full]
单调递减。

**Few-NERD (recall)**: 0.527 → 0.390 → 0.306 → **0.268** → 0.301 → 0.407 [full]
U 形曲线，count_22 处触底 (0.268)，full schema (count_66) 回升至 0.407。

输出文件：
- PDF: `figures/paper/fig_count_curves.pdf`
- PNG: `figures/paper/fig_count_curves.png`
- 脚本: `scripts/plot_fig1a_count_curves.py`

---
