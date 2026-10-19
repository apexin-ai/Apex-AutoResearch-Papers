# viz neg difficulty figure v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_neg_difficulty_figure_v2_20260514T103252_result.json`
- **Structured JSON:** [`00e02d5526d939b49859.json`](../../sessions/00/00e02d5526d939b49859.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果

**图表文件**

| 文件 | 路径 | 大小 |
|------|------|------|
| 分布图 PDF | `/root/structfuse-context/artifacts/figures/neg_difficulty_distribution.pdf` | 81.6 KB |
| 分布图 PNG | `/root/structfuse-context/artifacts/figures/neg_difficulty_distribution.png` | 239.9 KB |
| Margin 图 PDF | `/root/structfuse-context/artifacts/figures/neg_margin_comparison.pdf` | 19.2 KB |
| Margin 图 PNG | `/root/structfuse-context/artifacts/figures/neg_margin_comparison.png` | 93.2 KB |

脚本：`/root/structfuse-context/evaluation/plot_neg_difficulty.py`

**数据来源**：聚合统计合成（quantile-interpolated sampling + KDE）。脚本使用 5 点分位数（lo, p25, median, p75, hi）做分段线性插值采样，再加 KDE 平滑。**非 per-instance 真实分布，等替换真实数据后重新生成 camera-ready 版本。**

**图表描述（论文 caption）**

- **Fig 1** (neg_difficulty_distribution): *Distribution of query–negative cosine similarities under three negative sampling strategies (Random, Embedding, Dataflow) for Qwen2.5-Coder-3B (left) and StarCoder2-3B (right). Dashed red line indicates mean positive similarity. StarCoder2 shows wider separation between strategies; Qwen2.5-Coder yields highly concentrated distributions near 1.0, reflecting its narrower representational space. Distributions synthesized from aggregated quantile statistics.*

- **Fig 2** (neg_margin_comparison): *Mean positive–negative similarity margin across encoders and negative strategies. Error bars show standard error of the mean. Random negatives yield the largest margin; embedding-based negatives are hardest (smallest margin), with dataflow negatives intermediate. StarCoder2 exhibits consistently larger margins than Qwen2.5-Coder.*

---
