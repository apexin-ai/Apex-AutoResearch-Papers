# viz neg difficulty

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_neg_difficulty_20260514T170356_result.json`
- **Structured JSON:** [`d370df62a08a87da72cc.json`](../../sessions/d3/d370df62a08a87da72cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三张图表全部生成完毕。总结：

**产出文件**（服务器 `/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/chart/`）：

| 文件 | 大小 | 说明 |
|------|------|------|
| `neg_difficulty_margin_comparison.pdf/png` | 22K/105K | 主图：2048t 下 Qwen vs StarCoder margin 对比柱状图，标注 ratio (2.6×/3.9×/4.1×) |
| `neg_difficulty_similarity_dist.pdf/png` | 21K/168K | 补充图：并排子图展示 pos_sim/neg_sim grouped bar，实心=pos，斜线=neg，箭头标注 Δ |
| `neg_difficulty_ratio_heatmap.pdf/png` | 22K/71K | Heatmap：2×3 (token length × strategy)，值为 StarCoder/Qwen margin ratio |

**脚本**：`/root/structfuse/scripts/plot_neg_difficulty.py`

**关键数据点**（2048t margin ratio = StarCoder/Qwen）：
- Random: 2.6×
- Embedding: 3.9×
- Dataflow: 4.1×

图表风格遵循 draw-paper-figure skill 规范：300 DPI、DejaVu Sans 字体、Okabe-Ito 色盲友好配色、去除 top/right spine、PDF+PNG 双格式输出。

---
