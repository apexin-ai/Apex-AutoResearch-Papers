# code power curve d031 alignment

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_power_curve_d031_alignment_20260521T033306_result.json`
- **Structured JSON:** [`e60974e03b471e6dced3.json`](../../sessions/e6/e60974e03b471e6dced3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 生成成功。80% power 交叉点：

| 曲线 | 参数 | n (80% power) |
|------|------|---------------|
| Pairwise BT | p=0.630 | **114** |
| Pairwise Sign Test | p=0.739, r=0.523 | **62** |
| Binarized Likert | p=0.606, tie=0.625 | **462** |
| Likert ATE | d=0.073 | **1473** (off-chart) |

三个常量已更新，输出在 `artifacts/figures/paper/power_curve.pdf`。

---
