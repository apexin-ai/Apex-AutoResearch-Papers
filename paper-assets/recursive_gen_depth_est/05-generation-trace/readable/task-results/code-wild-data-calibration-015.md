# code wild data calibration 015

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wild_data_calibration_015_20260522T080508_result.json`
- **Structured JSON:** [`36d14604feb893f242c8.json`](../../sessions/36/36d14604feb893f242c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

**Base FPR（argmax，无阈值）:**
| Dataset | N | d0% | FPR |
|---|---|---|---|
| C4 10K | 10,000 | 65.98% | 34.02% |
| FineWeb 10K | 10,000 | 82.85% | 17.15% |
| RedPajama 10K | 10,000 | 84.47% | **15.53%** |

**Threshold Sweep（P(d0) < T 才判为 d1+）:**
| T | C4 FPR | FineWeb FPR | RedPajama FPR |
|---|---|---|---|
| 0.05 | 0.23% | 0.07% | 2.72% |
| 0.10 | 0.89% | 0.14% | 6.98% |
| 0.15 | 6.71% | 2.50% | 9.72% |
| 0.20 | 22.38% | 9.45% | 11.49% |

**关键发现:**
- RedPajama 10K 与 5K 一致（FPR 15.5% vs 15.3%），结果稳定
- FineWeb 和 RedPajama base FPR 接近（17% vs 15.5%），C4 显著更高（34%）
- RedPajama 的 P(d0) 分布与 C4/FineWeb 不同：低阈值下 FPR 降不到 1% 以下（T=0.05 时仍有 2.72%），说明 RedPajama 有更多边界样本
- 所有 19 特征在所有数据集上都有显著 distribution shift（KS p<0.01）
- 5-fold CV balanced accuracy: 0.7872

产出文件在 `results/wild_data_calibration_comprehensive/comprehensive_results.json`，registry 已更新为 DONE。

---
