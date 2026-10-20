# paper fix figure1 pipeline

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_figure1_pipeline_20260517T080308_result.json`
- **Structured JSON:** [`418fe5f66332680e498d.json`](../../sessions/41/418fe5f66332680e498d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

"depth 0→K" 弧线和文字现在完整显示，顶部有充足留白。

修复内容（`scripts/draw_pipeline_figure.py`）：
- `ylim` 上限 3.2 → 3.5
- `tight_layout(pad=0.3)` → `subplots_adjust(top=0.95)`（避免 tight_layout 过度压缩）
- `savefig` 添加 `pad_inches=0.2`（原来缺省值 0.1 太紧）

PDF 和 PNG 已更新到 `docs/paper/figures/`。

---
