# ops check shard4 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-shard4-status_20260516T042731_result.json`
- **Structured JSON:** [`54f7ba1fc55f0afebd60.json`](../../sessions/54/54f7ba1fc55f0afebd60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### shard4：已完成
- **进程已结束**，cuda:2 上无运行进程，GPU 利用率 0%，显存 0 MiB
- 完成时间：2026-05-16 12:12:46
- 全部 688 个样本处理完毕（9784 总 steps，含 resumed），结果已写入
- **Accuracy: 65.55%**，F1 macro: 52.66%，majority baseline: 75.73%（低于 baseline 10.2pp）
- 504 个 unparseable predictions（73.3%），这是主要问题
- 49 个被截断（7.12%），截断样本准确率反而更高（85.71% vs 64.01%）

### 其他 shard 进程状态
| Shard | 预期 PID | 实际 GPU 进程 PID | GPU | 利用率 | 显存 | 状态 |
|-------|---------|------------------|-----|--------|------|------|
| v3 (shard1) | 443221 | 443221 | GPU 0 | 88% | 21133 MiB | **运行中** |
| shard2 | 448094 | 448100 | GPU 1 | 88% | 21133 MiB | **运行中**（PID 略有偏差） |
| shard3 | 453335 | 453335 | GPU 3 | 88% | 21133 MiB | **运行中** |
| shard4 | 未记录 | — | GPU 2 | 0% | 0 MiB | **已完成** |

---
