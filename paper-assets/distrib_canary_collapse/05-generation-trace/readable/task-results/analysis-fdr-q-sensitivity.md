# analysis fdr q sensitivity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fdr_q_sensitivity_20260516T201708_result.json`
- **Structured JSON:** [`1656cd05371c4b447b51.json`](../../sessions/16/1656cd05371c4b447b51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果:

| | q=0.01 | q=0.05 | q=0.10 |
|---|---|---|---|
| **α=0.75** | 0/24 | 19/24 | 24/24 |
| **α=0.00** | 0/16 | 0/16 | 0/16 |

要点:
- **q=0.10**: 24/24 全显著，treatment-null 完美分离
- **q=0.05** (论文): 19/24，已报告
- **q=0.01**: 0/24 — 非信号缺失，而是 BH 在 m=8 时 rank-1 阈值为 0.00125，最小 p=0.0024 无法通过（T=11 时间点的统计功效限制）
- null control 在所有阈值下均为 0 — treatment vs null 的定性结论对 q 选择完全鲁棒

文件已保存至 `results/rebuttal/fdr_q_sensitivity.json` 和 `fdr_q_sensitivity_summary.txt`。

---
