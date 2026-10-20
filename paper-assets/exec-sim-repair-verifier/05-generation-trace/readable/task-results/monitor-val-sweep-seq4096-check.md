# monitor val sweep seq4096 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_val-sweep-seq4096-check_20260515T174024_result.json`
- **Structured JSON:** [`2ceee60c643f5881a9dd.json`](../../sessions/2c/2ceee60c643f5881a9dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**进程状态：RUNNING** (PID 397645, 已运行 ~11 分钟)

**当前进度：**
- 正在评估第 1 个 checkpoint: `checkpoint-1800`
- 进度: 3630/9335 样本 (38.9%)，running_acc = 85.2%
- 尚无 checkpoint 完成评估
- 总共需要 sweep 28 个 checkpoint (800 → 6200, 步长 200)

**GPU 利用率：**

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 98% | 17.4 GB |
| cuda:1 | 92% | 27.3 GB |
| cuda:2 | 94% | 30.7 GB |
| cuda:3 | 88% | 22.5 GB |

4 张卡都在高负载工作。cuda:0 被该 sweep 进程占用，其余 3 张卡有其他任务在跑。

**预估时间：** 当前 checkpoint 约需 ~18 分钟完成 (按 3630 样本/11 分钟推算)，28 个 checkpoint 全部 sweep 约需 **~8.5 小时**。

---
