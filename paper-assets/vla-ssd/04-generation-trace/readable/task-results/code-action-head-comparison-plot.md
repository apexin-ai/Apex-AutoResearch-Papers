# code action head comparison plot

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_head_comparison_plot_20260526T205555_result.json`
- **Structured JSON:** [`00ab19fa64ca4110db54.json`](../../sessions/00/00ab19fa64ca4110db54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成了双 panel 对比图（PNG + PDF），已注册为 artifact：

- `art_20260526_b8d482` — PNG (300 dpi)
- `art_20260526_ca216f` — PDF 矢量版

图表展示：上 panel Independent Linear Probe R² 在 L9 达到 mid-layer peak (0.637) 后逐层下降，L31 exit collapse (0.488)；下 panel Frozen Action Head 全层 R² < 0，trained 在后半段（L18+）优于 untrained，两者在 exit layer (L32) 趋近但仍为负值。

---
