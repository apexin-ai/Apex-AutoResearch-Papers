# infra check exp001 status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_exp001_status_20260513T001347_result.json`
- **Structured JSON:** [`97f3d363b05822ef875f.json`](../../sessions/97/97f3d363b05822ef875f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-001 状态汇报

### 1. 状态：**Completed**

PID 17138 已退出，无 run_pipeline 进程在运行。所有结果文件已生成（时间戳 May 13 07:13）。

### 2. GPU：**空闲**

`0 %, 0 MiB / 24564 MiB` — GPU 利用率 0%，显存未占用。

### 3. 数据文件 ✅ 完整

`data_exp001_pythia/` 下 depth_0 ~ depth_5.jsonl 全部存在，外加 features.csv：

| 文件 | 大小 |
|------|------|
| depth_0.jsonl | 4.3 MB |
| depth_1.jsonl | 4.6 MB |
| depth_2.jsonl | 4.6 MB |
| depth_3.jsonl | 4.6 MB |
| depth_4.jsonl | 4.6 MB |
| depth_5.jsonl | 4.6 MB |
| features.csv | 8.0 MB |

### 4. 结果

**Pairwise AUC（相邻深度）：**

| 对比 | AUC | 判断 |
|------|-----|------|
| 0 vs 1 | **0.9932** ± 0.0007 | 极易区分 |
| 1 vs 2 | **0.6539** ± 0.0069 | 可区分 |
| 2 vs 3 | 0.5515 ± 0.0137 | 接近随机 |
| 3 vs 4 | 0.5153 ± 0.0084 | ≈ 随机 |
| 4 vs 5 | 0.5135 ± 0.0078 | ≈ 随机 |

**K\* = 2**（AUC > 0.60 的最大深度）

**Pairwise JSD：**

| 对比 | JSD |
|------|-----|
| 0 vs 1 | 0.2142 |
| 1 vs 2 | 0.0140 |
| 2 vs 3 | 0.0051 |
| 3 vs 4 | 0.0033 |
| 4 vs 5 | 0.0031 |

**Ordinal Classification（6-class, 5-fold CV）：**
- MAE = 1.14
- Accuracy = 38.3%

**Top-5 Feature Importance：**
1. freq_entropy (9207)
2. surp_std (9041)
3. surp_d1_skew (8457)
4. surp_d2_mean (8173)
5. surp_d1_mean (8074)

### 总结

实验已完成，GPU 完全空闲。核心发现：depth 0→1 信号极强（AUC 0.99），depth 1→2 仍可区分（AUC 0.65），depth ≥ 2 后饱和（AUC ≈ 0.51，接近随机猜测）。JSD 趋势一致——0→1 跳跃式下降后快速收敛。

---
