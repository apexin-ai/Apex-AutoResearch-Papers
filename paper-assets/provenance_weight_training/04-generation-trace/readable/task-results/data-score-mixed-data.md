# data score mixed data

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_score-mixed-data_20260513T232905_result.json`
- **Structured JSON:** [`8d9b804ac2442ea165d2.json`](../../sessions/8d/8d9b804ac2442ea165d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

打分完成。结果汇报：

### scored_data.jsonl 产出

- **行数**: 371,499（与输入一致 ✓）
- **文件路径**: `/root/provenance_weight_training/data/scored_data.jsonl`

### q-score 分布统计

| 指标 | 值 |
|------|-----|
| Mean | 0.5987 |
| Std | 0.3740 |
| Median | 0.7049 |
| Min | 0.0002 |
| Max | 1.0000 |

### 10-bin 直方图

| 区间 | 数量 | 占比 |
|------|------|------|
| 0.0-0.1 | 55,799 | 15.0% |
| 0.1-0.2 | 35,855 | 9.7% |
| 0.2-0.3 | 25,281 | 6.8% |
| 0.3-0.4 | 20,022 | 5.4% |
| 0.4-0.5 | 16,768 | 4.5% |
| 0.5-0.6 | 15,743 | 4.2% |
| 0.6-0.7 | 15,440 | 4.2% |
| 0.7-0.8 | 17,547 | 4.7% |
| 0.8-0.9 | 26,288 | 7.1% |
| 0.9-1.0 | 142,756 | **38.4%** |

### 按来源的 q-score 对比

| 来源 | 数量 | Mean | Std | Median |
|------|------|------|-----|--------|
| synthetic (无 label 字段，即生成数据) | 206,610 | 0.8571 | 0.2291 | 0.9667 |
| fineweb (人类数据) | 164,889 | 0.2750 | 0.2469 | 0.1940 |

分离效果良好：synthetic 数据 median q-score 0.97，fineweb 人类数据 median 0.19，detector 能有效区分两类数据。

---
