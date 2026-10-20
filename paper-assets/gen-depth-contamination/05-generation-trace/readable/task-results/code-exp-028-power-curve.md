# code exp 028 power curve

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-028-power-curve_20260518T225402_result.json`
- **Structured JSON:** [`cbf868ee30774aeb9264.json`](../../sessions/cb/cbf868ee30774aeb9264.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 数据来源
- **Feature 数据**：`exp016_qwen_base` (C4)，路径 `/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv`
- **Feature matrix 大小**：30,000 rows (5,000 docs × 6 depths) × 15 features

### 执行情况
- 脚本 `exp_028_power_curve.py` 已部署并运行完成，PID=103384，耗时 86.3 秒（纯 CPU）
- 输出：`power_results.json`、`power_curve.png`、`power_curve.pdf`

### 结果

| n | mean AUC | std | detection rate (AUC > 0.60) |
|---|----------|-----|---------------------------|
| 500 | 0.5808 | 0.0180 | 20% |
| 1000 | 0.5911 | 0.0139 | 30% |
| **2000** | **0.6101** | **0.0088** | **100%** |
| 3000 | 0.6166 | 0.0051 | 100% |
| 4000 | 0.6220 | 0.0042 | 100% |
| 5000 | 0.6288 | 0.0000 | 100% |

**结论**：K\*=2 判定在 C4 上所需的最低样本量为 **n=2000**，此时 10/10 次 resample 均 AUC > 0.60（100% detection rate）。n < 2000 时 power 急剧下降（n=1000 仅 30%，n=500 仅 20%）。AUC 方差也随 n 增大单调递减，从 0.018 (n=500) 降至 0.004 (n=4000)。

---
