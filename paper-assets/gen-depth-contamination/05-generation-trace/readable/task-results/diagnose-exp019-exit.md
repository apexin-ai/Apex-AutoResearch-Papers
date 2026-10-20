# diagnose exp019 exit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp019_exit_20260516T111615_result.json`
- **Structured JSON:** [`7d76d35d97ebdf38e611.json`](../../sessions/7d/7d76d35d97ebdf38e611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-019 Mistral-7B 结果汇报

### 1. 判断：**SUCCESS**

### 2. 日志关键行
```
19:14:13 [INFO]   Ordinal MAE = 1.2275, Accuracy = 0.3567, K* = 1
19:14:13 [INFO] Pipeline complete.
```

### 3. K* = 1（假设预期为 2，实际为 1）

**Pairwise AUC：**
| 对比 | AUC | 判断 |
|------|-----|------|
| 0v1 | **0.9843** ± 0.0020 | 强可区分 |
| 1v2 | 0.5935 ± 0.0054 | < 0.60 阈值 |
| 2v3 | 0.5402 ± 0.0116 | 接近随机 |
| 3v4 | 0.5232 ± 0.0034 | 接近随机 |
| 4v5 | 0.5181 ± 0.0061 | 接近随机 |

**Pairwise JSD：** 0v1 有显著差异 (0.124)，之后急剧衰减至 ~0.004-0.008。

**Ordinal：** MAE=1.2275, Accuracy=35.67%

**Top 特征：** freq_entropy, surp_d1_skew, surp_d1_mean

### 4. 数据完整性
depth 0-5 各 5000 条，全部完整。结果目录 4 个 JSON + summary.txt，齐全。

### 5. cuda:1 状态：**空闲**（无进程占用）

### 6. Registry 已更新
- status → DONE
- conclusion → success
- metrics → 含 K*、AUC、JSD、ordinal 全量数据
- checkpoint_path / log_path 已设置
- failure_reason 已清空

**注意：** 假设预期 K*=2，实际 Mistral-7B K*=1，说明 depth 0→1 后信号即已饱和，与 Qwen 系列可能存在差异。

---
