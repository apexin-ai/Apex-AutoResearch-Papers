# analysis attention visualization v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attention_visualization_v2_20260517T125037_result.json`
- **Structured JSON:** [`28f8a819ec705042c853.json`](../../sessions/28/28f8a819ec705042c853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是关键发现：

## Attention Analysis 结果

| 指标 | 值 | 含义 |
|------|------|------|
| Entropy | 6.86 / 7.00 | **98.0% of max uniform** |
| Top-50% token attention share | 67.3% | 接近均匀（完美均匀=50%） |
| Gini coefficient | 0.246 | 低不平等 |
| Min/max attention ratio | 0.155 | 最少关注 token 仍获 15.5% of max |
| Camera balance | 53.8% / 46.2% | 双相机均贡献 |
| Per-task consistency | 6.844~6.846 | 跨任务几乎相同 |

**结论：Vision tokens 被近乎均匀地 attend（entropy = 98% of max）。** 这直接解释了为什么 token pruning 灾难性失败：模型对所有 128 个 visual tokens 均匀依赖，不存在"可安全移除"的 token 子集。任何 pruning 策略（ACIS k=0.5 移除 50% tokens）都在删除携带非冗余信息的 token。

输出文件：
- `eval_results/attention_analysis.json` — 完整统计
- `eval_results/attention_heatmap.png` — 可视化
- `artifacts/attention_distribution.png` — attention 分布图
- `artifacts/attention_per_task.png` — 跨任务对比

---
