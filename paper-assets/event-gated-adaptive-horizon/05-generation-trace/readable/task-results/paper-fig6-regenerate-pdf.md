# paper fig6 regenerate pdf

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig6_regenerate_pdf_20260525T170024_result.json`
- **Structured JSON:** [`d5c7046e172b6fa2a669.json`](../../sessions/d5/d5c7046e172b6fa2a669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

目视确认结果：

- **右列颜色**：绿色 ✓
- **右列 eval 曲线**：从 ~31 平稳上升至 ~876，无崩溃 ✓
- **标注 "876.7 (94% baseline)"**：右上角可见 ✓
- **标注 "NVE ≤ 0.6×"**：右中面板显示 "(calibrated)" ✓
- **左列 CIVO 崩溃**：橙色曲线 + 红色阴影区，"eval decline"、"value explosion (+130%)"、"entropy ↓ (over-committed)" 标注均在 ✓
- **底部注释**："Both configurations use trained dt-embedding | CIVO onset requires dt > 1 imagination (F6)" ✓

**产出文件**：
- `fig6_multiple_pathways.pdf` — 60 KB
- `fig6_multiple_pathways.png` — 481 KB
- 路径：`artifacts/figures/paper/`

图片视觉正确，所有关键元素符合预期。

---
