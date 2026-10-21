# figure norm sweep magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_norm-sweep-magnitude_20260521T043856_result.json`
- **Structured JSON:** [`d6b3d05dc04545e42f63.json`](../../sessions/d6/d6b3d05dc04545e42f63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 2 已生成：

- **PDF**: `/root/acr-vla-conformal-refinement/artifacts/fig2_norm_sweep.pdf` (16.5 KB)
- **PNG**: `/root/acr-vla-conformal-refinement/artifacts/fig2_norm_sweep.png` (55.8 KB)

数据摘要：

| ε | Mean SR (%) | SEM (%) | n |
|---|---|---|---|
| 0.03 | 15.18 | 0.35 | 11 |
| 0.05 | 13.92 | 0.40 | 13 |
| 0.10 | 15.38 | 0.52 | 16 |
| 0.20 | 17.00 | 3.00 | 2 |

VLA-only baseline 虚线在 10.5%。ε=0.2 的 SEM 很大（±3%），符合预期（仅 2 seeds）。本地脚本同步保存在 `artifacts/fig2_norm_sweep.py`。

---
