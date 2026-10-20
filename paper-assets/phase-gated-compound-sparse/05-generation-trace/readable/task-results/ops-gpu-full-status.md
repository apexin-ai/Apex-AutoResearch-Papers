# ops gpu full status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_full_status_20260516T140155_result.json`
- **Structured JSON:** [`1c8b37e29aa5133b4941.json`](../../sessions/1c/1c8b37e29aa5133b4941.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | PID | 实验 | 显存占用 | GPU利用率 | 运行时间 | 状态 |
|-----|------|------|---------|----------|---------|------|
| 0 | 562663 | c8_llama_importance_s030 | 91.1/97.9 GB | 96% | 3h47m | 运行中 |
| 1 | 555744 | gpqa_ds_importance_s015 | 66.3/97.9 GB | 100% | 6h19m | 103/198 (~52%) |
| 2 | 560643 | c8_llama_random_s015 | 59.6/97.9 GB | 80% | 4h27m | 运行中 |
| 3 | 560642 | c8_llama_random_s020 | 59.6/97.9 GB | 79% | 4h27m | 运行中 |

### 逐项回答

**1. c8_gpu0_s025 是否完成？s030 chain 是否启动？**
- s025 **已完成**。profiling_results.json 21MB，n_problems=250，752 个 problem 条目。原 PID 315052 已死。
- s030 chain **已启动**。PID 562663 在 GPU 0 上跑 importance_s030，已运行 ~3h47m。sentinel 文件尚未被覆盖（目录中无中间文件，结果在完成时一次性写入）。

**2. GPQA 运行状态**
- PID 555739（wrapper）/ 555744（python）均存活，GPU 1 上运行。
- 进度 103/198（~52%），最新日志 21:59:36，每题约 5 分钟，预计剩余 ~8 小时。

**3. c8_main Round 进度（PID 310712，运行 10h42m）**

| 条件 | 状态 |
|------|------|
| importance_s015 | DONE (n=250) |
| importance_s020 | DONE (n=250) |
| importance_s025 | DONE (n=250) |
| importance_s030 | IN_PROGRESS (GPU 0) |
| random_s015 | IN_PROGRESS (GPU 2) |
| random_s020 | IN_PROGRESS (GPU 3) |
| random_s025 | NOT_STARTED |
| random_s030 | NOT_STARTED |

Round 1-2 完成（importance s015/s020/s025 + 对应 random 条件）。Round 3 正在跑 importance_s030 + random_s015 + random_s020。random_s025/s030 等后续 Round。

**4. 已完成但未处理的实验**
- importance_s015、s020、s025 三个已完成。s025 是最新完成的（今天 18:14），s030 chain 已自动接续，无需人工干预。
- 如果需要对已完成的 importance 结果做分析/后处理，s015/s020/s025 三个都可以开始了。

---
