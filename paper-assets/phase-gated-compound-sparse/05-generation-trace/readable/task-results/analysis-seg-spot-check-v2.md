# analysis seg spot check v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seg_spot_check_v2_20260515T101806_result.json`
- **Structured JSON:** [`0242cbad242c5cf81ee5.json`](../../sessions/02/0242cbad242c5cf81ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**全部 12 个 conditions（4 sparsity × 3 segmentations）均在 Bonferroni 校正后显著**（p < 1e-10）。

| Segmentation | s015 D | s020 D | s025 D | s030 D |
|---|---|---|---|---|
| tercile (n=500) | +0.391 | +1.215 | +3.986 | +8.481 |
| quartile (n=50) | +0.491 | +1.388 | +4.322 | +12.930 |
| quintile (n=50) | +0.505 | +1.197 | +4.960 | +11.548 |

方向一致，dose-response 保持，效应不依赖于 tercile 分割方式。文件已写入：
- 本地 CSV: `artifacts/n500_analysis/segmentation_sensitivity.csv`
- 本地 MD: `artifacts/n500_analysis/segmentation_sensitivity.md`
- 服务器: `/root/autodl-tmp/pacs/analysis_output/segmentation_sensitivity.csv`

---
