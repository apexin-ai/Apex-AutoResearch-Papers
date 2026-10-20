# ops check seed123 seed456 status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_seed123_seed456_status_20260521T080445_result.json`
- **Structured JSON:** [`208af13c85e57e9de1da.json`](../../sessions/20/208af13c85e57e9de1da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

### seed123: 训练中，未完成
- **PID 686085** 运行中，已跑 18 分钟
- 当前进度：**63/444 steps (14%)**，每步 ~16.6s
- 预计剩余：**~1 小时 45 分钟**
- 运行在 GPU 1（CUDA_VISIBLE_DEVICES=1），显存占用 41191/97887 MiB，利用率 100%
- eval_results.json 尚不存在（训练未完成）

### seed456: 未启动
- checkpoint 目录不存在，无相关进程
- **需要提交**

### GPU 状态
| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 49175/97887 MiB (50%) | 0% | 闲置（有历史显存占用） |
| 1 | 41191/97887 MiB (42%) | 100% | seed123 训练中 |

GPU 0 可用于提交 seed456。

### 磁盘
| 分区 | 使用 | 剩余 |
|------|------|------|
| / (30G) | 69% | 9.5G |
| /root/autodl-tmp (250G) | 81% | 48G |

数据盘剩余 48G，足够再跑一个 seed。根分区偏紧但不影响训练。

---
