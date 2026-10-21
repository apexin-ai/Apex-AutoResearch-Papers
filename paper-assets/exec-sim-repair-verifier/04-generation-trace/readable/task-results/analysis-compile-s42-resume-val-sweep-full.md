# analysis compile s42 resume val sweep full

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile-s42-resume-val-sweep-full_20260515T225659_result.json`
- **Structured JSON:** [`fce91dbe1b31a2135907.json`](../../sessions/fc/fce91dbe1b31a2135907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 19 个 checkpoint 数据已收集。**ckpt-5600 和 5800 的结果不存在于服务器上。**

## s42 完整 Val Sweep 结果

| Step | Val Acc (%) | F1_fail | F1_pass | F1_macro | Unparseable | 来源 |
|------|------------|---------|---------|----------|-------------|------|
| 200  | 63.52      | 51.60   | 70.70   | 61.17    | —           | original (CSV) |
| 400  | 80.96      | —       | —       | —        | —           | original (CSV) |
| 600  | 85.00      | —       | —       | —        | —           | original (CSV) |
| 800  | 84.50      | —       | —       | 79.20    | —           | original (CSV) |
| 1000 | **88.23**  | 73.00   | 92.50   | 82.72    | —           | original (CSV) |
| 1200 | 87.76      | 70.20   | 92.30   | 81.25    | —           | original (CSV) |
| 1400 | 85.97      | 62.95   | 91.34   | 77.15    | —           | original (CSV) |
| 1600 | 86.75      | 66.12   | 91.76   | 78.94    | —           | original (CSV) |
| 1800 | 87.91      | 71.96   | 92.29   | 82.13    | 9           | resume sweep |
| 2000 | 87.06      | 66.67   | 91.97   | 79.32    | 9           | resume sweep |
| 2200 | 86.51      | 64.94   | 91.65   | 78.30    | 9           | resume sweep |
| 2400 | 86.82      | 68.94   | 91.64   | 80.29    | 9           | resume sweep |
| 2600 | 86.40      | 64.16   | 91.60   | 77.88    | 9           | resume sweep |
| 2800 | 88.38      | 72.52   | 92.63   | 82.58    | 9           | resume sweep |
| 3000 | 87.71      | 70.42   | 92.25   | 81.33    | 9           | resume sweep |
| 3200 | 86.16      | 63.23   | 91.48   | 77.35    | 9           | resume sweep |
| 3400 | 85.33      | 60.47   | 91.00   | 75.73    | 9           | resume sweep |
| **3600** | **90.28** | **78.20** | **93.75** | **85.98** | 9       | resume sweep |
| 3800 | 89.78      | 75.08   | 93.57   | 84.33    | 9           | resume sweep |
| 4000 | 89.13      | 73.41   | 93.17   | 83.29    | 9           | resume sweep |
| 4200 | 90.21      | 78.12   | 93.69   | 85.91    | 9           | resume sweep |
| 4400 | 89.82      | 76.66   | 93.49   | 85.08    | 9           | resume sweep |
| 4600 | 89.20      | 74.27   | 93.17   | 83.72    | 9           | resume sweep |
| 4800 | 87.52      | 69.06   | 92.18   | 80.62    | 9           | resume sweep |
| 5000 | 87.71      | 69.45   | 92.31   | 80.88    | 9           | resume sweep |
| 5200 | 87.68      | 69.28   | 92.30   | 80.79    | 9           | resume sweep |
| 5400 | 88.43      | 71.58   | 92.74   | 82.16    | 9           | resume sweep |
| 5600 | —          | —       | —       | —        | —           | **缺失** |
| 5800 | —          | —       | —       | —        | —           | **缺失** |

## 关键发现

- **Peak**: **ckpt-3600 = 90.28%** (F1_macro 85.98)，比 ckpt-1000 (88.23%) 高 **+2.05 pp**
- **Second peak**: ckpt-4200 = 90.21% (F1_macro 85.91)，几乎并列
- **Valley**: ckpt-3400 = 85.33%，是 resume 区间的最低点
- **趋势**: 3600-4400 区间持续 >89.8%，之后 4800 开始衰减至 ~87.5-88.5% 平台
- Resume sweep 全部使用 `max_seq_length=8192`，unparseable 均为 9（0.10%），与 original sweep 配置一致
- **ckpt-5600 和 5800 的结果未在服务器上找到**，需要补跑

---
