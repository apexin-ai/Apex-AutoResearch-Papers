# ops fisher heatmap pdf regen

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fisher_heatmap_pdf_regen_20260517T032340_result.json`
- **Structured JSON:** [`b808a6b32878fe2e1e65.json`](../../sessions/b8/b808a6b32878fe2e1e65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 文件已经存在且有效。两个版本都有：

- `fisher_power_heatmap.pdf` (99KB) — 单面板 power heatmap
- `fisher_dual_heatmap.pdf` (142KB) — 双面板 (power + CI width)

两者均于 2026-05-17 05:38 生成，对应 PNG 也存在。脚本 `plot_heatmap.py` 质量合格：用了 bicubic 插值、contour lines (50%/80%/95%)、AUC=0.70 threshold 标线、cell annotations、合适的 colormap。

无需重新生成，文件已就绪。论文中使用路径：`/root/autodl-tmp/exp004/fisher_heatmap/fisher_power_heatmap.pdf`。

---
