# paper figure fig reliability

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_reliability_20260514T145317_result.json`
- **Structured JSON:** [`a3274edf1b259a73ec8b.json`](../../sessions/a3/a3274edf1b259a73ec8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成并注册。

**输出**: `/figures/paper/fig_reliability.pdf` (20KB, 矢量 PDF)

**结果摘要**:

| Signal | NER ECE | RE ECE |
|--------|---------|--------|
| Soft Jaccard | 0.077 | 0.165 |
| Voting Conf. | 0.071 | 0.128 |
| Logprob | 0.113 | 0.380 |

结构性一致性信号（SJ、Voting）校准质量显著优于 Logprob，RE 任务差距尤其明显（Logprob ECE 0.380 vs Voting 0.128）。NER 上三者差距较小但结构信号仍占优。配套脚本 `fig_reliability.py` 和数据 `fig_reliability_data.json` 已保存在同目录下。

---
