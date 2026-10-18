# ops mink final results read

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mink_final_results_read_20260518T195028_result.json`
- **Structured JSON:** [`f67fcc575ab8c7c2a380.json`](../../sessions/f6/f67fcc575ab8c7c2a380.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Min-K% Prob baseline **已全部完成**。

## 状态汇总

- **进程**: 无 mink 进程在跑，实验已结束
- **GPU**: cuda:0 和 cuda:1 均空闲（0MiB / 0% util）
- **其他 Python 进程**: 只有 tensorboard 和 jupyter-lab 常驻，无其他实验

## Min-K% Prob 结果（`mink_prob_results.json`）

**9-cell 平均（`__9cell_average__`）**:

| 配置 | 4class_acc | d1d3_bal_acc |
|---|---|---|
| K10_methodA | 0.2495 | 0.1111 |
| K10_methodB | 0.2896 | 0.3680 |
| K10_methodC | 0.2460 | 0.3280 |
| K20_methodA | 0.2419 | 0.1070 |
| **K20_methodB** | **0.3323** | **0.4039** |
| K20_methodC | 0.2459 | 0.3279 |
| K30_methodA | 0.2226 | 0.1050 |
| **K30_methodB** | **0.3301** | **0.4075** |
| K30_methodC | 0.2452 | 0.3270 |

**关键观察**:
- **methodB + K20/K30** 是 Min-K% 最优配置，4class_acc ~33%，d1d3_bal_acc ~40%
- methodA 在 d1d3_bal_acc 上几乎失效（~10%），methodC 接近随机（~33%）
- 最佳单 cell: **gpt2xl_temp09 K20_methodB**，4class_acc=0.5064，d1d3_bal_acc=0.5110
- 整体性能远低于 random chance 以上水平，说明 Min-K% Prob 作为 depth estimation baseline 能力有限

---
