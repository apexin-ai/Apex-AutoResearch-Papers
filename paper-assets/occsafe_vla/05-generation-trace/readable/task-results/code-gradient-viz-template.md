# code gradient viz template

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient-viz-template_20260526T174850_result.json`
- **Structured JSON:** [`04db03bff85224556f1c.json`](../../sessions/04/04db03bff85224556f1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三张图全部正常生成，质量符合论文标准：

1. **Heatmap** — DINOv2 (23 blocks) + SigLIP (26 blocks) 双面板，log-scale inferno colormap，共享 colorbar
2. **Cosine similarity** — 带 shaded std 的折线图，y=0 虚线参考线，仅显示有 OCC 数据的条件
3. **CAR variance bar chart** — 自动标注 max/min 倍数关系（6.92×），带 bracket 和数值标签

脚本已写入 `artifacts/plot_gradient_analysis_v2_paper.py`，支持 `.pt` / `.json` 输入，3 种数据格式自动检测，torch 懒加载（`--help` 不需要 GPU 环境）。

---
