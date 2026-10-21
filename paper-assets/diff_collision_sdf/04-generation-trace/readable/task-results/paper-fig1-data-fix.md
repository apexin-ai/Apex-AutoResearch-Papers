# paper fig1 data fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig1_data_fix_20260527T022225_result.json`
- **Structured JSON:** [`7e9d3b5cd233fb01d232.json`](../../sessions/7e/7e9d3b5cd233fb01d232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**完成。总结：**

- **修改**：`fig1_teaser.py` line 160，`car_f` 从 `[0.3, 28.5]` 改为 `[0.3, 26.8]`，与正文 3-seed mean 一致。文件中只有这一处 28.5，text label 用 f-string 自动跟随，无需额外改。
- **已重新生成** fig1_teaser.pdf/png 并同步到 `_project/chart/`。
- **Panel (b) displacement**：代码中 Pi0+A1 用的是单个代表值 0.001 mm（1 μm），Pi0.5 用 288 mm。这些是各自的 **median displacement**（配合标注 "73.9% below 1 μm"）。图中没有标注 "~5nm"——abstract 的 "~5nm median" 指的是更细粒度的统计值，而图中 lollipop 展示的是 order-of-magnitude 对比，两者口径不同但不矛盾。如需严格对齐，可在 caption 中注明 panel (b) 的点位代表 representative displacement 而非精确 median。

---
