# code three model visualization

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_three_model_visualization_20260513T033423_result.json`
- **Structured JSON:** [`e5dd9a07204ea00d2a4d.json`](../../sessions/e5/e5dd9a07204ea00d2a4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 张图已生成并注册：

| 文件 | 大小 | Artifact ID |
|------|------|-------------|
| `auc_heatmap.pdf` | 33K | art_20260513_98dfe7 |
| `jsd_decay.pdf` | 24K | art_20260513_53a754 |
| `feature_importance.pdf` | 19K | art_20260513_dbb099 |

图表规格：
- **AUC Heatmap** — RdYlGn colormap，0.5=chance 浅色/1.0 深色，每 cell 标注 AUC±std，K\*=2 竖虚线分隔，colorbar 标注 0.60 阈值线
- **JSD Decay** — log scale Y 轴，3 条曲线（蓝/橙/绿 colorblind-safe），K\*=2 灰色阴影区域
- **Feature Importance** — top-10 特征 grouped bar chart，从 3 个实验的 `feature_importance.json` 读取，按平均重要性排序

所有图使用 serif 字体、300 DPI、无标题、淡灰网格线。脚本位于服务器 `scripts/plot_three_model_comparison.py`。

---
