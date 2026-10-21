# analysis statistical tests

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_statistical_tests_20260524T223529_result.json`
- **Structured JSON:** [`3f0809a860689a5fc258.json`](../../sessions/3f/3f0809a860689a5fc258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已写入 `artifacts/statistical_tests.json` 并注册。

关键发现：

| Condition | n | CAR mean | Cohen's d | p-value |
|-----------|---|----------|-----------|---------|
| Vanilla (baseline) | 3 | 0.780 | — | — |
| Full OCC | 3 | 0.797 | +0.69 | 0.442 |
| Detach+BN | 3 | 0.746 | **-3.90** | **0.031** |
| Random OCC | 3 | 0.789 | +0.37 | 0.712 |
| Depth | 4 | 0.780 | -0.02 | 0.984 |
| Cutoff@35K | 3 | 0.779 | -0.09 | 0.944 |
| Cutoff@25K | 2 | 0.724 | -1.81 | 0.143 |
| Reverse Cutoff | 2 | 0.718 | **-3.50** | **0.031** |
| Detach+LN | 3 | 0.765 | -0.79 | 0.357 |
| Cutoff@15K | 1 | 0.804 | insufficient_seeds |
| Cutoff@45K | 1 | 0.764 | insufficient_seeds |

显著差异（p<0.05）：Detach+BN 和 Reverse Cutoff 显著低于 Vanilla。Full OCC 的 effect size (d=+0.69) 为中等正向但 n=3 统计力不足（p=0.44）。

注：Cutoff@35K 实际均值为 0.779（非任务中参考值 0.792），因 cutoff_s2_v2_eval 的 CAR=0.770。

---
