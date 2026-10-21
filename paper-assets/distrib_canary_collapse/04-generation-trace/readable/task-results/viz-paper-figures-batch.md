# viz paper figures batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_paper_figures_batch_20260516T162153_result.json`
- **Structured JSON:** [`ffd55d460315e15b7835.json`](../../sessions/ff/ffd55d460315e15b7835.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 PDF 全部生成完毕：

| 文件 | 大小 | 内容 |
|------|------|------|
| `differencing_dmax.pdf` | 20KB | d_max 分组柱状图 (α=0.75, 3 seeds) |
| `consensus_heatmap.pdf` | 21KB | K-of-5 votes 热力图 (8 pairs × 3 seeds) |
| `regime_map.pdf` | 29KB | α regime 分区概念图 |
| `metric_trajectory.pdf` | 21KB | token_entropy + distinct_1 漂移折线图 |
| `consensus_workflow.pdf` | 37KB | 5-method filtering pipeline 流程图 |

数据说明：
- `consensus_heatmap` 仅含 α=0.75 三个 seed（只有这三个有 5method_leadlag.json）
- `metric_trajectory` 包含 α=0.00/0.25/0.50/0.75 四组，a025/a050 有多 seed 时画了 ±std band
- `differencing_dmax` 显示 s42/s43 全部 d_max=1，s44 前 4 对为 d_max=2（token_entropy 对），后 4 对为 1

---
